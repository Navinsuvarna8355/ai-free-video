import streamlit as st
from gtts import gTTS
from moviepy.editor import *
import requests
import os

# Replace with your Unsplash API key
UNSPLASH_ACCESS_KEY = "YOUR_UNSPLASH_API_KEY"

def fetch_image(query):
    url = f"https://api.unsplash.com/photos/random?query={query}&client_id={UNSPLASH_ACCESS_KEY}"
    response = requests.get(url)
    if response.status_code != 200:
        st.error("Failed to fetch image. Check your API key or internet connection.")
        return None
    data = response.json()
    image_url = data['urls']['regular']
    img_data = requests.get(image_url).content
    with open("selected.jpg", "wb") as handler:
        handler.write(img_data)
    return "selected.jpg"

def generate_audio(text):
    tts = gTTS(text=text, lang='hi')
    tts.save("voice.mp3")
    return "voice.mp3"

def create_video(image_path, audio_path, duration=10):
    clip = ImageClip(image_path).set_duration(duration).resize(height=720)
    audioclip = AudioFileClip(audio_path)
    final = clip.set_audio(audioclip)
    final.write_videofile("final_video.mp4", fps=24)
    return "final_video.mp4"

# Streamlit UI
st.set_page_config(page_title="Hindi Text to Video", layout="centered")
st.title("🎥 Hindi Text to Video Generator")

text_input = st.text_area("Enter your Hindi text below:", height=150)

if st.button("Generate Video"):
    if not text_input.strip():
        st.warning("Please enter some text to proceed.")
    else:
        with st.spinner("Generating video..."):
            image_path = fetch_image("India culture")
            if image_path:
                audio_path = generate_audio(text_input)
                video_path = create_video(image_path, audio_path)
                st.success("✅ Video generated successfully!")
                st.video(video_path)
                with open(video_path, "rb") as file:
                    st.download_button("📥 Download Video", file, file_name="final_video.mp4")
