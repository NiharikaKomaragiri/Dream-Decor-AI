import os
import streamlit as st
from image_generator import generate_room
from styles import ROOM_STYLES

st.set_page_config(
    page_title="Dream Decor AI",
    page_icon="🏡",
    layout="wide"
)

st.title("🏡 Dream Decor AI")
st.caption("Generate beautiful AI-designed room concepts")

# Sidebar / Input section
style = st.selectbox(
    "🎨 Interior Style",
    ROOM_STYLES
)

budget = st.slider(
    "💰 Budget (₹)",
    min_value=10000,
    max_value=500000,
    value=100000,
    step=10000
)

color = st.text_input(
    "🎨 Theme Color",
    "White"
)

generate = st.button(
    "✨ Generate AI Room",
    width="stretch"
)

# Generate Image
if generate:

    with st.spinner("🎨 AI is designing your room..."):

        generated_image = generate_room(
            style,
            budget,
            color
        )

    st.subheader("🏡 AI Generated Room")

    st.image(
        generated_image,
        width="stretch"
    )

    os.makedirs("outputs", exist_ok=True)

    output_path = "outputs/generated_room.png"

    generated_image.save(output_path)

    with open(output_path, "rb") as file:
        st.download_button(
            label="⬇ Download Image",
            data=file,
            file_name="dream_room.png",
            mime="image/png",
            width="stretch"
        )

    st.success("✅ AI Room Generated Successfully!")

st.markdown("---")
st.caption("Dream Decor AI | Powered by Streamlit + Hugging Face")