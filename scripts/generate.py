# ============================================================================
# SCRIPT 2: Generate a new dragon image from scratch
# ============================================================================
import os
import base64
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Set up directory paths
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # Get project root
IMAGES_DIR = os.path.join(BASE_DIR, "images")  # Path to images folder

# Define where to save the generated image
output_path = os.path.join(IMAGES_DIR, "dragon.png")

# Text description of what to generate
prompt = "A cute baby dragon flying over a futuristic Glasgow skyline, digital art"

# Generate a new image from the text prompt
result = client.images.generate(
    model="gpt-image-1",  # OpenAI's image generation model
    prompt=prompt,  # Text description of desired image
    size="1024x1024",  # Output dimensions
)

# Extract the base64-encoded image from the response
image_base64 = result.data[0].b64_json
# Decode base64 string to actual image bytes
image_bytes = base64.b64decode(image_base64)

# Save the image to the images folder
with open(output_path, "wb") as f:
    f.write(image_bytes)

print(f"Saved new image to: {output_path}")