import os
import base64
import csv
from openai import OpenAI
from PIL import Image
from io import BytesIO

# Load API Key from Environment
API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

#Initialize OpenAI client
client = OpenAI(api_key=API_KEY)

# Function to encode image to base64
def encode_image(image_path):
    with Image.open(image_path) as img:
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode()

# Function to send image and prompt to OpenAI
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

# Input/Output paths
image_directory = "sample dataset/images"
output_csv = "model captions/gpt_captions_200.csv"

# Sort image files numerically
def extract_number(name):
    return int(''.join(filter(str.isdigit, name)) or -1)

image_files = sorted(
    [f for f in os.listdir(image_directory) if f.lower().endswith((".png", ".jpg", ".jpeg"))],
    key=extract_number
)

# Write captions to CSV
with open(output_csv, mode='w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["filename", "caption"])

    for filename in image_files:
        image_path = os.path.join(image_directory, filename)
        image_base64 = encode_image(image_path)
        caption = generate_caption(image_base64)
        writer.writerow([filename, caption])
        print(f"Processed {filename}")

