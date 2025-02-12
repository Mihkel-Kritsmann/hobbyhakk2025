# services/llm_service.py
from transformers import pipeline


class LLM:
    messages = [
    {"role": "user", "content": "Who are you?"},
    ]
    def __init__(self):
        # Initialize local model
        self.pipe = pipeline("text-generation", model="deepseek-ai/DeepSeek-R1", trust_remote_code=True)
    
    def generate(self, text):
        response = self.pipe(messages)
        return response

