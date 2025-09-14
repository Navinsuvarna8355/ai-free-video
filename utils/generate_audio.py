from gtts import gTTS
import os

def generate_voiceover(scenes, lang):
    os.makedirs("assets/audio", exist_ok=True)
    lang_code = "hi" if lang == "Hindi" else "en"
    for i, scene in enumerate(scenes):
        tts = gTTS(text=scene, lang=lang_code)
        tts.save(f"assets/audio/scene_{i}.mp3")

