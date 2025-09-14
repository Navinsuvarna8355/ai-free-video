from transformers import pipeline

def generate_story(topic, lang):
    prompt = f"Write a short cartoon-style story in {lang} about: {topic}"
    generator = pipeline("text-generation", model="gpt2")
    story = generator(prompt, max_length=300)[0]['generated_text']
    scenes = story.split(". ")
    return scenes

