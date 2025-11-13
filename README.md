# 🐉 Image Generation & Editing with OpenAI (DALL·E / GPT-Image-1)

This project demonstrates how to generate, vary, inpaint, and outpaint images using the **OpenAI Images API** in Python.

It includes:

* 🖼️ Generating images from text
* 🎭 Creating variations of existing images
* 🎯 Inpainting with masks (tattoos, edits, selective changes)
* 🌄 Outpainting to expand scenes
* 🔐 Secure `.env` key loading
* 📂 Clean directory structure for scripts & images

---

# 🚀 Features

### **1. Generate Images**

* Simple prompt → PNG output
* High-resolution 1024×1024
* Uses `gpt-image-1`

### **2. Create Variations**

* Automatically stylise an existing image
* Produces multiple alternative looks

### **3. Inpaint with Alpha Masks**

* Only edit white areas in a mask
* Used here to add dragon tattoos

### **4. Outpaint (Scene Expansion)**

* Expands image beyond original canvas
* Maintains consistency & style

### **5. Clean Project Structure**

* All scripts in `/scripts`
* All images in `/images`
* API keys hidden with `.env`

---

# 📦 Installation

### **1. Clone the repository**

```bash
git clone <your-repo-url>
cd ImageGeneration
```

### **2. Create & activate a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

### **3. Install dependencies**

```bash
pip install openai python-dotenv pillow
```

---

# 🔑 Environment Setup

Create a `.env` file:

```
OPENAI_API_KEY=your-secret-key-here
```

⚠️ Never commit `.env` to GitHub.

---

# 🖼️ Generate a New Image

Run:

```bash
python3 scripts/generate.py
```

The script will:

* Send a prompt to OpenAI
* Receive a Base64 image
* Save it as `images/dragon.png`

Example prompt:

```
A cute baby dragon flying over a futuristic Glasgow skyline, digital art
```

---

# 🎨 Create Variations

Run:

```bash
python3 scripts/vary.py
```

Outputs:

```
images/dragon_variation_1.png
images/dragon_variation_2.png
```

---

# 📁 Project Structure

```
ImageGeneration/
│
├── images/
│   ├── dragon.png
│   ├── mask.png
│   ├── canvas.png
│   ├── mask_big_fixed.png
│   └── (all output images saved here)
│
└── scripts/
    ├── generate.py
    ├── vary.py
    ├── edit_inpaint.py
    ├── edit_outpaint.py
    ├── fix_mask_big.py   # optional
    └── __init__.py
```

---

# 📝 Script Explanations

## 🎨 **1. generate.py — Create the base dragon image**

* Loads `.env`
* Sends your text prompt to `gpt-image-1`
* Saves output to `/images/dragon.png`

Example output:

```
images/dragon.png
```

---

## 🔁 **2. vary.py — Create stylistic variations**

* Loads `/images/dragon.png`
* Requests 2 alternative versions
* Saves:

```
images/dragon_variation_1.png
images/dragon_variation_2.png
```

---

## 🎯 **3. edit_inpaint.py — Tattoo inpainting**

Uses `mask.png` where:

* **White = editable**
* **Transparent = untouched**

Adds:

* Celtic knotwork tattoos
* Runes
* Tribal patterns
* Chest piece, sleeves, tail patterns

Outputs:

```
images/tattoo_inpaint_1.png
images/tattoo_inpaint_2.png
```

---

## 🌄 **4. edit_outpaint.py — Expand the whole scene**

Uses:

* `canvas.png` — a larger canvas with dragon centered
* `mask_big_fixed.png` — transparent outside, white around edges

Adds:

* Extended scene
* Glasgow skyline
* Sunset colour palette
* Preserves tattoos

Output:

```
images/tattoo_outpaint.png
```

---

## 🛠️ **5. fix_mask_big.py — Ensure mask transparency**

Fixes:

```
Invalid mask image format - mask image missing alpha channel
```

Produces:

```
images/mask_big_fixed.png
```

---

# 🧪 Recommended Full Workflow

1. Generate base dragon
   `python3 scripts/generate.py`

2. Create artistic variations
   `python3 scripts/vary.py`

3. Add tattoos using inpainting
   `python3 scripts/edit_inpaint.py`

4. Expand to full environmental scene
   `python3 scripts/edit_outpaint.py`

---

# 🛑 Ignored Items

```
.env
venv/
materials-openai-dalle/
__pycache__/
```

