# services/llm_service.py
from transformers import pipeline


class LLM:
    messages = [
    {"role": "user", "content": "Who are you?"},
    ]
    def __init__(self):
        # Initialize local model
        self.pipe = pipeline("image-text-to-text", model="unsloth/Llama-3.2-11B-Vision-unsloth-bnb-4bit")
    
    def generate(self, text):
        response = self.pipe(text)
        return response

