import os
import csv
from PIL import Image
from transformers import Qwen2_5_VLForConditionalGeneration, AutoProcessor
from qwen_vl_utils import process_vision_info

# Load the model and processor
model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
    "Qwen/Qwen2.5-VL-7B-Instruct", torch_dtype="auto", device_map="auto"
)
processor = AutoProcessor.from_pretrained("Qwen/Qwen2.5-VL-7B-Instruct")

# Input and output paths
input_folder = "../../sample dataset/images"
output_csv = "../qwen_captions_200.csv"

# Caption prompt
caption_prompt = (
    "Describe this image precisely so someone could redraw it exactly."
)

# Generate captions and write to csv
with open(output_csv, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Image", "Caption"])

    # Loop through each image in the folder
    for filename in sorted(os.listdir(input_folder)):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp")):
            try:
                image_path = os.path.join(input_folder, filename)
                print(f"Processing: {filename}")

                image = Image.open(image_path).convert("RGB")

                # Construct message
                messages = [
                    {
                        "role": "user",
                        "content": [
                            {"type": "image", "image": image},
                            {"type": "text", "text": caption_prompt}
                        ]
                    }
                ]

                # Prepare inputs
                text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
                image_inputs, video_inputs = process_vision_info(messages)

                inputs = processor(
                    text=[text],
                    images=image_inputs,
                    videos=video_inputs,
                    padding=True,
                    return_tensors="pt"
                ).to("cuda")

                # Generate caption
                outputs = model.generate(**inputs, max_new_tokens=256)
                caption_raw = processor.tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]

                # Clean output
                cleaned_caption = caption_raw.strip()
                if cleaned_caption.lower().startswith(caption_prompt.lower()):
                    cleaned_caption = cleaned_caption[len(caption_prompt):].strip(": \n")

                for prefix in [
                    "You are a helpful assistant.",
                    "system\nYou are a helpful assistant.\nuser",
                    "assistant",
                    "user"
                ]:
                    cleaned_caption = cleaned_caption.replace(prefix, "").strip()

                print(f"Caption for {filename}:\n{cleaned_caption}\n")
                writer.writerow([filename, cleaned_caption])

            except Exception as e:
                print(f"Error processing {filename}: {e}")
