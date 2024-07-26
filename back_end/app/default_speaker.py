from TTS.api import TTS
from extract_from_pdf import Extract_From_PDF
import os
import time

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")
tts = TTS("xtts")

def speech_generator(pdf_path, speaker_path, start_text, end_text):
    i = 0
    
    text = Extract_From_PDF(pdf_path, start_text, end_text).replace('\n', ' ')
    speaker_path = speaker_path.strip("'\"")

    while i < len(text):
        start_time = time.time()
        print(f"Processing text from {i} to {min(i + 250, len(text))}")

        # make a file path name for every part
        pdf_name = os.path.splitext(os.path.basename(pdf_path))[0].replace(' ', '_')
        speaker_name = os.path.splitext(os.path.basename(speaker_path))[0].replace(' ', '_') + '_part_' + str(i+1)
        new_file_name = f"{pdf_name}_{speaker_name}.wav"
        new_file_path = os.path.join("/Users/achimmula/Desktop/audio_books", new_file_name)

        end_index = min(i + 250, len(text))
        slice = text[i:end_index]
        last_full_stop = slice.rfind('.')
        
        if last_full_stop != -1:
            slice_end = i + last_full_stop + 1 
        else:
            slice_end = end_index
        
        tts.tts_to_file(text=text[i:slice_end],
                        file_path=new_file_path,
                        speaker_wav=speaker_path,
                        language="en",
                        )
        
        i = slice_end

        elapsed_time = time.time() - start_time
        print(f"\rProcessing took {elapsed_time} seconds", end='', flush=True)
        print('done processing index ', i + 1) 

if __name__ == "__main__":
    pdf_path = input("Please enter the path to the PDF file: ")
    speaker_path = input("Please enter the path to the speaker file: ")
    start_text = input("Please enter the starting text: ")
    end_text = input("Please enter the ending text: ")
    speech_generator(pdf_path, speaker_path, start_text, end_text)
