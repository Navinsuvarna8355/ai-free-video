import streamlit as st
from utils.generate_script import generate_story
from utils.generate_images import generate_images
from utils.generate_audio import generate_voiceover
from utils.assemble_video import assemble_video

st.title("🎬 AI Cartoon Video Generator")
language = st.selectbox("Choose Language", ["Hindi", "English"])
input_text = st.text_area("Enter your story idea or topic")

if st.button("Generate Video"):
    with st.spinner("Generating story..."):
        scenes = generate_story(input_text, language)
    with st.spinner("Creating visuals..."):
        generate_images(scenes)
    with st.spinner("Generating voiceover..."):
        generate_voiceover(scenes, language)
    with st.spinner("Assembling video..."):
        video_path = assemble_video(scenes)
    st.success("Video generated successfully!")
    st.video(video_path)
