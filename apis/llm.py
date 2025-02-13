# services/llm_service.py
from transformers import pipeline
import gc
import torch
gc.collect()
torch.cuda.empty_cache()

class LLM:
    def __init__(self):
        # Initialize local model
        self.pipe = pipeline("image-text-to-text", model="unsloth/Llama-3.2-11B-Vision-Instruct-unsloth-bnb-4bit")
    
    def generate(self, text):
        response = self.pipe(text)
        return response[0]['generated_text']

