import os
import base64
from dotenv import load_dotenv
from openai import OpenAI

# 📦 "load_dotenv()" opens our secret treasure box
#    and remembers our magic key (API key).
load_dotenv()

# 🤖 Make a tiny robot helper called "client".
#    We give it our magic key so it can make pictures for us.
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 🐉 We already have a picture called "dragon.png".
#    Now we want to make NEW versions of this dragon!
#    So we open the picture like opening a book.
with open("dragon.png", "rb") as f:

    # 🎨 Ask the robot:
    #    "Please make me 2 new dragon pictures,
    #     but make them neon and cyberpunk and night-time!"
    result = client.images.edit(
        model="gpt-image-1",      # the art robot we use
        image=f,                  # the picture we want to change
        prompt="A neon cyberpunk night-time version of this dragon",
        size="1024x1024",         # how big the new pictures should be
        n=2                       # how many new pictures to make
    )

# 💾 The robot sends back the new pictures as secret letters (base64).
#    Now we need to turn those letters into real pictures!
for i, item in enumerate(result.data):

    # 🔓 Change the secret letters into picture bits
    img_bytes = base64.b64decode(item.b64_json)

    # 📁 Give each picture a name like "variation_1.png"
    out_name = f"variation_{i+1}.png"

    # 🖼️ Save the picture bits into a real file we can open
    with open(out_name, "wb") as out:
        out.write(img_bytes)

    # 🎉 Tell us that the picture is ready!
    print(f"Saved {out_name}")
