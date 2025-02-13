# services/translate_service.py
import requests

class Translate:
    def __init__(self):
        self.base_url = "https://libretranslate.com"  
        
    def translate(self, text, target_lang):
        url = f"{self.base_url}/translate"
        payload = {
            "q": text,
            "source": "auto",
            "target": "ee"
        }
        
        response = requests.post(url, json=payload)
        return response.json()['translatedText']
    