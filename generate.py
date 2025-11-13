import base64
from openai import OpenAI
from dotenv import load_dotenv
import os

# 📦 "load_dotenv()" opens a secret box (.env file)
#     and remembers the magic password inside it.
load_dotenv()

# 🤖 Make a little robot helper called "client"
#     and give it our secret password so it can make pictures for us.
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 🐉 This is what we want the robot to draw!
prompt = "A cute baby dragon flying over a futuristic Glasgow skyline, digital art"

# 🎨 Tell the robot:
#     "Please draw this picture for me!"
#     We also tell it what size the picture should be.
result = client.images.generate(
    model="gpt-image-1",   # The art robot we want to use
    prompt=prompt,         # What we want it to draw
    size="1024x1024",      # How big the picture should be
)

# 📥 The robot sends back the picture as secret numbers (base64)
image_base64 = result.data[0].b64_json

# 🔓 Turn the secret numbers into real picture bits
image_bytes = base64.b64decode(image_base64)

# 💾 Open a new file called "dragon.png"
#     and put the picture bits inside it.
with open("dragon.png", "wb") as f:
    f.write(image_bytes)

# 🎉 Tell the person:
print("Image saved as dragon.png!")
#     "Your picture is ready!"