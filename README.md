
# 📸 AI Meme Generator (Offline Edition)

## 📝 Description  
A lightweight, offline meme generator built using Streamlit and Python. It allows users to input a topic or emotion and generates a meme using predefined local captions, without relying on external APIs like OpenAI.

---

## ✨ Features  
- Choose from locally stored meme templates  
- Generate funny captions based on topic using a local dictionary  
- Overlay captions on meme images  
- Download the final meme instantly  
- Works **completely offline** — no internet or API keys required  

---

## 🚀 Setup  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/offline-meme-generator.git
   cd offline-meme-generator
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**  
   ```bash
   streamlit run app.py
   ```

---

## 🧑‍💻 Usage  

1. Enter a topic or emotion (e.g., `exam`, `monday`, `coffee`).  
2. Choose a meme template from the dropdown.  
3. Click **"Generate Meme"**.  
4. View the meme and download it as an image.

---

## 📁 Folder Structure  

```
offline-meme-generator/
│
├── app.py                   # Streamlit app logic
├── templates/               # Predefined meme background images
│   └── template1.jpg        # Example template images
├── output/                  # Folder for saving generated memes
├── requirements.txt         # Dependencies (Streamlit, Pillow, etc.)
└── README.md                # Project documentation
```

---

## 📦 Sample Caption Mapping  

The generator uses the following local dictionary to produce memes:

```python
{
    "exam": "When you realize you studied the wrong chapter!",
    "monday": "Me trying to get out of bed on Monday.",
    "coffee": "Decaf? That’s not even a real drink!",
    "coding": "It worked... but I don’t know why!",
    "internship": "Expectation: AI wizard. Reality: Spreadsheet ninja.",
    "friday": "Mood: Friday vibes only!",
    "sleep": "I'll sleep after one more episode... at 3 AM."
}
```

For unknown topics, it returns a generic fallback:  
`"When you have no idea what's going on — like '<your topic>'."`

---

## 📌 Notes  
- Custom templates can be added to the `templates/` directory.  
- No API keys or internet access are required.  

---

## 🤝 License  
MIT License — free to use, modify, and distribute.
