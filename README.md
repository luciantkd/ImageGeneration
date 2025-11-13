# 🐉 Image Generation with OpenAI (DALL·E / GPT-Image-1)

This project demonstrates how to generate images using the **OpenAI Images API** in Python.  
It includes scripts for:

- Generating an image from a text prompt  
- Creating variations of an existing image  
- Saving images locally as PNG files  
- Loading API keys securely using a `.env` file  

This is a clean, minimal, and practical example of building AI image workflows using Python.

---

## 🚀 Features

### **1. Generate a New Image**
- Describe anything with text  
- OpenAI creates a PNG image in 1024×1024  
- File is saved locally (e.g., `dragon.png`)

### **2. Create Variations**
- Load an existing PNG  
- Ask the model to create stylised or modified versions  
- Saves images such as `variation_1.png`, `variation_2.png`

### **3. Secure Environment Setup**
- No API keys stored in code  
- `.env` file handles secrets  
- Compatible with Python virtual environments

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd ImageGeneration
````

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install openai python-dotenv
```

---

## 🔑 Environment Variables

Create a file called `.env` in the project directory:

```
OPENAI_API_KEY=your-real-api-key-here
```

⚠️ Do **not** commit your `.env` file to GitHub.

---

## 🖼️ Generate an Image

Run:

```bash
python3 generate.py
```

This will:

* Send your prompt to the OpenAI Images API
* Save the generated image as `dragon.png`

Example prompt used in the script:

```
"A cute baby dragon flying over a futuristic Glasgow skyline, digital art"
```

---

## 🎨 Create Variations of an Image

Ensure you have `dragon.png` (or any PNG) in the folder, then run:

```bash
python3 vary.py
```

This creates:

```
variation_1.png
variation_2.png
```

You can adjust the prompt inside the script to control the style and mood.

---

## 📁 Project Structure

```
ImageGeneration/
│
├── generate.py          # Create a brand new image from a text prompt
├── vary.py              # Create variations of an existing PNG image
├── dragon.png           # Example generated image
├── variation_1.png      # Example variation
├── variation_2.png      # Example variation
├── .env                 # (Ignored) API key storage
├── .gitignore           # Ensures clean repo
└── venv/                # Virtual environment (ignored)
```

---

## 🛑 Ignored Files

`materials-openai-dalle/`
→ Tutorial sample files; not part of this project

`.env`
→ Keeps API key private

`venv/`
→ Virtual environment; not for GitHub
