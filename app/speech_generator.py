import torch
# from TTS.api import TTS
from extract_from_pdf import Extract_From_PDF

def speech_generator(text):

    device = "cuda" if torch.cuda.is_available() else "cpu"

    # tts = TTS( "tts_models/multilingual/multi-dataset/xtts_v2").to(device)
    
    print(text)

    # wav = tts.tts( text = text, speaker_wav = "/Users/abhinay/audio_book/8y10l4.wav", language="en")
    # tts.tts_to_file( text = text, speaker_wav = "/Users/abhinay/audio_book/8y10l4.wav", language="en", file_path = "/Users/abhinay/audio_book/peter_with_jokes.wav")

if __name__ == "__main__":
    text = Extract_From_PDF()
    speech_generator(text)