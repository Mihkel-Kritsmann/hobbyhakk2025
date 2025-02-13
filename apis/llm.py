# services/llm_service.py
from transformers import pipeline


class LLM:
    def __init__(self):
        # Initialize local model
        self.pipe = pipeline("image-text-to-text", model="unsloth/Llama-3.2-11B-Vision-Instruct-unsloth-bnb-4bit", )
    
    def generate(self, text, max_new_tokens=128):
        response = self.pipe(text, max_new_tokens=max_new_tokens)[0]['generated_text']
        response_filtered = response.replace(text, '')
        return response_filtered

