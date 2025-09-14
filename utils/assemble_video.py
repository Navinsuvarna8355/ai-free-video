import os
from moviepy.editor import *

def assemble_video(scenes):
    clips = []
    for i in range(len(scenes)):
        img = ImageClip(f"assets/images/scene_{i}.png").set_duration(4)
        audio = AudioFileClip(f"assets/audio/scene_{i}.mp3")
        clip = img.set_audio(audio)
        clips.append(clip)
    final = concatenate_videoclips(clips)
    os.makedirs("assets/video", exist_ok=True)
    final_path = "assets/video/final_video.mp4"
    final.write_videofile(final_path, fps=24)
    return final_path

