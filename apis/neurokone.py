# services/speech_service.py
import requests
import os
import base64
import wave
import io

class Neurokone:
    def __init__(self):
        self.base_url = "https://api.tartunlp.ai/text-to-speech/v2"
        self.output_dir = 'static/audio'
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Get available speakers
        self.speakers = self._get_speakers()
    
    def _get_speakers(self):
        try:
            response = requests.get(f"{self.base_url}")
            if response.status_code == 200:
                config = response.json()
                return {speaker['name']: speaker for speaker in config['speakers']}
            return {}
        except Exception as e:
            print(f"Error fetching speakers: {e}")
            return {}

    def text_to_speech(self, text, speaker="mari", speed=1.0):
        try:
            # Prepare the request payload
            payload = {
                "text": text,
                "speaker": speaker,
                "speed": speed
            }

            # Make request to TartuNLP API
            response = requests.post(
                f"{self.base_url}",
                json=payload
            )

            if response.status_code == 200:
                # Generate unique filename
                filename = f"{self.output_dir}/speech_{hash(text)}.wav"
                
                # Save the audio file
                with open(filename, 'wb') as f:
                    f.write(response.content)
                
                return filename
            else:
                print(f"API Error: {response.status_code} - {response.text}")
                return None

        except Exception as e:
            print(f"Error in text_to_speech: {e}")
            return None

    def get_available_speakers(self):
        return list(self.speakers.keys())

