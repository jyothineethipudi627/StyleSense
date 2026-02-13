import streamlit as st
import google.generativeai as genai
from PIL import Image

# ---------------- CONFIG ----------------
st.set_page_config(page_title="StyleSense AI", layout="wide")

# ---------------- API KEY ----------------
API_KEY = "AIzaSyDu4wpXoyCZv26rMQUx1q8RyhM-t0gEZIs"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

# ---------------- UI ----------------
st.title("👗 StyleSense : AI Fashion Recommendation System")
st.markdown("### Generative AI Powered Virtual Stylist")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Select Gender", ["Male", "Female", "Other"])
    age = st.slider("Select Age", 10, 70, 22)
    occasion = st.selectbox("Occasion", ["Casual", "Office", "Party", "Wedding", "Festival", "Travel"])
    style = st.selectbox("Style Preference", ["Trendy", "Classic", "Sporty", "Minimal", "Traditional"])

with col2:
    uploaded_image = st.file_uploader("Upload Outfit Image (optional)", type=["jpg", "png", "jpeg"])

# ---------------- AI PROMPT ----------------
def generate_fashion_advice():
    prompt = f"""
    You are an expert fashion stylist.

    User Details:
    Gender: {gender}
    Age: {age}
    Occasion: {occasion}
    Style Preference: {style}

    Give:
    1. Outfit recommendations
    2. Color combinations
    3. Styling tips
    4. Accessories suggestions
    5. Footwear suggestions

    Keep it simple, trendy, and practical.
    """

    response = model.generate_content(prompt)
    return response.text

# ---------------- IMAGE ANALYSIS ----------------
def analyze_image(img):
    prompt = """
    Analyze this clothing image and give fashion improvement suggestions,
    matching accessories, and better styling ideas.
    """
    response = model.generate_content([prompt, img])
    return response.text

# ---------------- BUTTON ----------------
if st.button("✨ Get AI Fashion Recommendation"):
    with st.spinner("AI is generating fashion advice..."):
        advice = generate_fashion_advice()
        st.subheader("👕 Personalized Outfit Suggestions")
        st.write(advice)

# ---------------- IMAGE SECTION ----------------
if uploaded_image:
    st.image(uploaded_image, caption="Uploaded Outfit", use_column_width=True)
    img = Image.open(uploaded_image)

    if st.button("🧠 Analyze Outfit Image"):
        with st.spinner("AI analyzing your outfit..."):
            result = analyze_image(img)
            st.subheader("🖼 Image-Based Fashion Analysis")
            st.write(result)

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("🚀 **StyleSense - Powered by Gemini AI & Streamlit**")
