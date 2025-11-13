# ============================================================================
# SCRIPT 1: Create stylistic variations of an existing dragon image
# ============================================================================
import os
import base64
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file (contains API key)
load_dotenv()
# Initialize OpenAI client with API key from environment
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Set up directory paths
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # Get project root directory
IMAGES_DIR = os.path.join(BASE_DIR, "images")  # Path to images folder

# Path to the original dragon image
dragon_path = os.path.join(IMAGES_DIR, "dragon.png")

# Open the dragon image and send it to OpenAI for editing
with open(dragon_path, "rb") as img:
    result = client.images.edit(
        model="gpt-image-1",  # OpenAI's image editing model
        image=img,  # The original dragon image
        prompt=(
            "Create two stylistic variations of this dragon. "
            "Keep the same general pose and composition but change colours, "
            "lighting, and art style."
        ),
        size="1024x1024",  # Output image dimensions
        n=2,  # Generate 2 variations
    )

# Loop through each generated variation and save it
for i, item in enumerate(result.data):
    # Decode the base64-encoded image data to bytes
    img_bytes = base64.b64decode(item.b64_json)
    # Create output filename (dragon_variation_1.png, dragon_variation_2.png)
    out_path = os.path.join(IMAGES_DIR, f"dragon_variation_{i+1}.png")
    # Write the image bytes to file
    with open(out_path, "wb") as f:
        f.write(img_bytes)
    print(f"Saved {out_path}")