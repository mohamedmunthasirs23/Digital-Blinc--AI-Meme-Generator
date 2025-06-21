import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import os

# 🚫 Remove OpenAI dependency entirely
# openai.api_key = "..." → no longer needed

# ✅ Sample local meme caption dataset
local_caption_dataset = {
    "exam": "When you realize you studied the wrong chapter!",
    "monday": "Me trying to get out of bed on Monday.",
    "coffee": "Decaf? That’s not even a real drink!",
    "coding": "It worked... but I don’t know why!",
    "internship": "Expectation: AI wizard. Reality: Spreadsheet ninja.",
    "friday": "Mood: Friday vibes only!",
    "sleep": "I'll sleep after one more episode... at 3 AM."
}

# Ensure required directories exist
if not os.path.exists("templates"):
    os.makedirs("templates")
    for i in range(1, 4):
        img = Image.new("RGB", (500, 500), color=(200 + i*10, 150 + i*20, 100 + i*30))
        d = ImageDraw.Draw(img)
        d.text((50, 200), f"Template {i}", fill=(255, 255, 255))
        img.save(f"templates/template{i}.jpg")

if not os.path.exists("output"):
    os.makedirs("output")

# Local caption generator from dictionary
def generate_caption(topic):
    topic_lower = topic.strip().lower()
    return local_caption_dataset.get(topic_lower, f"When you have no idea what's going on — like '{topic}'.")

# Overlay text on image
def add_caption_to_image(image_path, caption):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    
    # Use textbbox instead of textsize
    bbox = draw.textbbox((0, 0), caption, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    width, height = image.size
    x = (width - text_width) / 2
    y = height - text_height - 10

    draw.text((x, y), caption, font=font, fill="white")
    return image


# Streamlit UI
st.title("📸 AI Meme Generator (Offline Edition)")
topic = st.text_input("Enter a topic or emotion:")
template_list = os.listdir("templates")

if template_list:
    template = st.selectbox("Choose a template", template_list)

    if st.button("Generate Meme"):
        caption = generate_caption(topic)
        meme = add_caption_to_image(f"templates/{template}", caption)
        st.image(meme, caption=caption)
        meme_path = "output/generated_meme.png"
        meme.save(meme_path)
        with open(meme_path, "rb") as file:
            st.download_button(label="Download Meme", data=file, file_name="meme.png", mime="image/png")
else:
    st.warning("No meme templates found in 'templates/' folder.")
