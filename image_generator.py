import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from prompts import create_prompt

load_dotenv()

client = InferenceClient(
    api_key=os.getenv("HF_API_TOKEN")
)

def generate_room(style, budget, color):

    prompt = create_prompt(style, budget, color)

    image = client.text_to_image(
        prompt=prompt,
        model="black-forest-labs/FLUX.1-schnell"
    )

    return image