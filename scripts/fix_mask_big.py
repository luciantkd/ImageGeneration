# ============================================================================
# SCRIPT 3: Convert a black/white mask to proper alpha channel format
# ============================================================================
from pathlib import Path
from PIL import Image

# Set up directory paths using Path objects
BASE_DIR = Path(__file__).resolve().parent.parent  # Project root directory
IMAGES_DIR = BASE_DIR / "images"  # Images folder

# Paths for input and output mask files
src_path = IMAGES_DIR / "mask_big.png"  # Original black/white mask
dst_path = IMAGES_DIR / "mask_big_fixed.png"  # Output mask with alpha

print(f"Loading: {src_path}")
# Open mask and convert to grayscale (L mode)
mask_bw = Image.open(src_path).convert("L")

# Get image dimensions
w, h = mask_bw.size
print(f"Mask size: {w}x{h}")

# Create alpha channel: white areas (>128) = transparent (0), black areas = opaque (255)
# This inverts the mask so white = editable, black = keep original
alpha = mask_bw.point(lambda p: 0 if p > 128 else 255)

# Create a solid black RGBA image
mask_rgba = Image.new("RGBA", (w, h), (0, 0, 0, 255))
# Apply the alpha channel (transparency map)
mask_rgba.putalpha(alpha)

# Save the properly formatted mask
mask_rgba.save(dst_path)
print(f"Saved fixed mask with alpha to: {dst_path}")