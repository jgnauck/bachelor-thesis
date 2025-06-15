import os
import csv
from PIL import Image
import torch
from transformers import Blip2Processor, Blip2ForConditionalGeneration

os.environ['HF_HOME'] = '/work/jgnauck'

# Load processor and model
processor = Blip2Processor.from_pretrained("Salesforce/blip2-opt-6.7b")
model = Blip2ForConditionalGeneration.from_pretrained(
    "Salesforce/blip2-opt-6.7b",
    device_map="auto",
    torch_dtype=torch.float32
)

# Input/output
input_folder = "/home/jgnauck/images200"
output_csv = "blip2_captions_200.csv"

# Create CSV
with open(output_csv, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Image", "Caption"])

    for filename in sorted(os.listdir(input_folder)):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp")):
            try:
                image_path = os.path.join(input_folder, filename)
                print(f"Processing: {filename}")

                # Load and validate image
                try:
                    image = Image.open(image_path).convert("RGB")
                except Exception as img_err:
                    print(f"Skipping corrupted image {filename}: {img_err}")
                    continue

                inputs = processor(images=image, return_tensors="pt").to("cuda")

                # Generate caption
                outputs = model.generate(**inputs, max_new_tokens=256)
                caption = processor.batch_decode(outputs, skip_special_tokens=True)[0].strip()

                print(f"Caption for {filename}: {caption}")
                writer.writerow([filename, caption])

            except Exception as e:
                print(f"Error processing {filename}: {e}")

