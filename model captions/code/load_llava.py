import os
import csv
from PIL import Image
import torch
from transformers import LlavaForConditionalGeneration, AutoProcessor


#Load model and processor


processor = AutoProcessor.from_pretrained("llava-hf/llava-1.5-7b-hf")
model = LlavaForConditionalGeneration.from_pretrained("llava-hf/llava-1.5-7b-hf", device_map="auto", torch_dtype="auto")

# Input and output paths
input_folder = "../../sample dataset/images"
output_csv = "../llava_captions_200.csv"

# Generate captions and write to CSV
with open(output_csv, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Image", "Caption"])

    # Loop through each image in the folder
    for filename in sorted(os.listdir(input_folder)):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp")):
            try:
                image_path = os.path.join(input_folder, filename)
                print(f"Processing: {filename}")

               
                try:
                    image = Image.open(image_path).convert("RGB")
                except Exception as img_err:
                    print(f"Skipping invalid image {filename}: {img_err}")
                    continue

                # Prompt setup
                prompt = (
                    "Describe this image precisely so someone could redraw it."
                )
                messages = [
                    {
                        "role": "user",
                        "content": [
                            {"type": "image", "image": image},
                            {"type": "text", "text": prompt}
                        ]
                    }
                ]

                text_input = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
                inputs = processor(text=text_input, images=[image], return_tensors="pt").to("cuda")

                # Generate caption
                outputs = model.generate(**inputs, max_new_tokens=256)
                caption_raw = processor.tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

                # Clean output
                for prefix in [
                  "USER:", "User:", "user:",
                  prompt.strip(),
                  "ASSISTANT:", "Assistant:", "assistant:"
                  ]:
                  caption_raw = caption_raw.replace(prefix, "")

                caption = caption_raw.strip()

                print(f"Caption for {filename}: {caption}")
                writer.writerow([filename, caption])

            except Exception as e:
                print(f"Error processing {filename}: {e}")
