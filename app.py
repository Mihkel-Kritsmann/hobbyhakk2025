# app.py
from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
from apis.llm import LLM
from apis.translate import Translate
from apis.neurokone import Neurokone


app = Flask(__name__)

# Initialize services
llm_service = LLM()
translate_service = Translate()
speech_service = Neurokone()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    try:
        data = request.json
        text = data.get('text', '')
        target_language = data.get('target_language', 'en')
        speaker = data.get('speaker', 'mari')  # Default speaker
        
        # Process with LLM
        llm_response = llm_service.generate(text)
        
        # Translate into estonian
        
        #translated_text = translate_service.translate( llm_response, target_language)
        
        # Generate speech
        audio_file = speech_service.text_to_speech(
            "Tere minu nimi on Mari",
            speaker=speaker
        )
        
        return jsonify({
            'original_text': text,
            'llm_response': llm_response,
            'translated_text': "Not working",
            'audio_file': audio_file
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_speakers')
def get_speakers():
    speakers = speech_service.get_available_speakers()
    return jsonify({'speakers': speakers})

