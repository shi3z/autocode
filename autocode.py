import os
import tempfile
import sounddevice as sd
import soundfile as sf
import numpy as np
from transformers import WhisperProcessor, WhisperForConditionalGeneration
from anthropic import Client

import re

def extract_python_code(text):
    pattern = r"```python(.*?)```"
    matches = re.findall(pattern, text, re.DOTALL)
    return matches[0]

# Anthropic APIキーの設定
os.environ["ANTHROPIC_API_KEY"] = "" #YOUR API KEY

def record_audio(duration, sample_rate):
    print("Recording...")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()
    print("Recording finished.")
    return recording

def save_audio(recording, sample_rate):
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
        sf.write(temp_audio.name, recording, sample_rate)
        return temp_audio.name

def transcribe_audio(audio_path):
    processor = WhisperProcessor.from_pretrained("openai/whisper-large")
    model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-large")

    audio_data, sample_rate = sf.read(audio_path)
    input_features = processor(audio_data, sampling_rate=sample_rate, return_tensors="pt").input_features

    generated_ids = model.generate(input_features)
    transcription = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return transcription

def generate_code(prompt):
    client = Client(api_key=os.environ["ANTHROPIC_API_KEY"])
    formatted_prompt = f"\n\nHuman: Write a Python code that fulfills the following requirements: {prompt}\n\nAssistant:"
    response = client.completions.create(prompt=formatted_prompt, model="claude-v1", max_tokens_to_sample=1000)
    return response.completion

def save_code_to_file(code, filename):
    with open(filename, "w") as file:
        file.write(code)

def main():
    duration = 5  
    sample_rate = 16000  
    recording = record_audio(duration, sample_rate)

    audio_path = save_audio(recording, sample_rate)

    prompt = transcribe_audio(audio_path)
    print(f"Recognized prompt: {prompt}")

    generated_code = generate_code(prompt)
    print(f"Generated code:\n{generated_code}")

    filename = "generated_code.py"
    generated_code = extract_python_code(generated_code)
    print(generated_code)
    save_code_to_file(generated_code, filename)
    print(f"Code saved to {filename}")


    os.remove(audio_path)

if __name__ == "__main__":
    main()
