import os
import base64
import csv
from openai import OpenAI
from PIL import Image
from io import BytesIO

# Initialize OpenAI client
client = OpenAI(api_key="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")  # Replace with your actual key or set via env

def encode_image(image_path):
    with Image.open(image_path) as img:
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode()

def generate_caption(image_base64):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{image_base64}"
                        }
                    },
                    {
                        "type": "text",
                        "text": (
                             "Describe this image precisely so someone could redraw it."
                        )
                    }
                ]
            }
        ],
        max_tokens=256
    )
    return response.choices[0].message.content.strip()

# Input/Output
image_directory = "/home/jgnauck/images200"
output_csv = "gpt_captions_200.csv"

# Get and sort image filenames numerically
def extract_number(name):
    return int(''.join(filter(str.isdigit, name)) or -1)

image_files = sorted(
    [f for f in os.listdir(image_directory) if f.lower().endswith((".png", ".jpg", ".jpeg"))],
    key=extract_number
)

# Write results to CSV
with open(output_csv, mode='w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["filename", "caption"])

    for filename in image_files:
        image_path = os.path.join(image_directory, filename)
        image_base64 = encode_image(image_path)
        caption = generate_caption(image_base64)
        writer.writerow([filename, caption])
        print(f"Processed {filename}")

