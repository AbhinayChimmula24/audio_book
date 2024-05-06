# from TTS.api import TTS
from extract_from_pdf import Extract_From_PDF

# tts  = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

# tts = TTS("xtts")

def speech_generator():
    text = Extract_From_PDF()
    print(text)
    # tts.tts_to_file( text=text,
    #                 file_path="/Users/achimmula/Desktop/audio_books/simon_vauce.wav",
    #                 speaker_wav= "/Users/achimmula/Desktop/speakers/simon_vausce.wav",
    #                 language="en",
    #                 split_sentences=True
    #                 )

if __name__ == "__main__":
    speech_generator()