import os
import base64
from dotenv import load_dotenv
from openai import OpenAI

# Load .env file
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Paths to your images folder
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # go up from /scripts
IMAGES_DIR = os.path.join(BASE_DIR, "images")

dragon_path = os.path.join(IMAGES_DIR, "dragon.png")
mask_path = os.path.join(IMAGES_DIR, "mask.png")

with open(dragon_path, "rb") as img, open(mask_path, "rb") as mask:
    result = client.images.edit(
        model="gpt-image-1",
        image=img,
        mask=mask,
        prompt=(
            "Add detailed full-body tattoos on the white-marked areas: "
            "Celtic knotwork, glowing runes, tribal patterns, chest piece, "
            "arm sleeves, leg tattoos, and tail markings. "
            "Make them stylish, integrated with the dragon’s scales, and vivid."
        ),
        size="1024x1024",
        n=2
    )

# Save results into /images/
for i, item in enumerate(result.data):
    image_bytes = base64.b64decode(item.b64_json)
    out_name = os.path.join(IMAGES_DIR, f"tattoo_inpaint_{i+1}.png")
    with open(out_name, "wb") as f:
        f.write(image_bytes)
    print(f"Saved {out_name}")
