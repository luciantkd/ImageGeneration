# ============================================================================
# SCRIPT 5: Inpaint - Add tattoos to specific areas of the dragon
# ============================================================================
import os
import base64
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()
# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Set up directory paths
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # Project root
IMAGES_DIR = os.path.join(BASE_DIR, "images")  # Images folder

# Define paths to original dragon and mask
dragon_path = os.path.join(IMAGES_DIR, "dragon.png")  # Original dragon image
mask_path = os.path.join(IMAGES_DIR, "mask.png")  # Mask showing where to add tattoos

# Open both image and mask files
with open(dragon_path, "rb") as img, open(mask_path, "rb") as mask:
    # Edit only the masked areas (inpainting)
    result = client.images.edit(
        model="gpt-image-1",
        image=img,  # Original dragon image
        mask=mask,  # White areas = edit, black areas = keep original
        prompt=(
            "Add detailed full-body tattoos on the white-marked areas: "
            "Celtic knotwork, glowing runes, tribal patterns, chest piece, "
            "arm sleeves, leg tattoos, and tail markings. "
            "Make them stylish, integrated with the dragon's scales, and vivid."
        ),
        size="1024x1024",  # Output dimensions
        n=2  # Generate 2 variations
    )

# Save each generated variation
for i, item in enumerate(result.data):
    # Decode base64 image data to bytes
    image_bytes = base64.b64decode(item.b64_json)
    # Create output filename (tattoo_inpaint_1.png, tattoo_inpaint_2.png)
    out_name = os.path.join(IMAGES_DIR, f"tattoo_inpaint_{i+1}.png")
    # Write image to file
    with open(out_name, "wb") as f:
        f.write(image_bytes)
    print(f"Saved {out_name}")