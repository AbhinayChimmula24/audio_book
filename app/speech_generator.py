import torch
from TTS.api import TTS
# from extract_from_pdf import Extract_From_PDF

def speech_generator():

    device = "cuda" if torch.cuda.is_available() else "cpu"

    tts = TTS( "tts_models/multilingual/multi-dataset/xtts_v2").to(device)
    
    wav = tts.tts( text = "The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 Englishto-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.0 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature.", speaker_wav = "/Users/achimmula/Documents/GitHub/audio_book/8y10l4.wav", language="en")
    tts.tts_to_file( text = "The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 Englishto-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.0 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature.", speaker_wav = "/Users/achimmula/Documents/GitHub/audio_book/8y10l4.wav", language="en", file_path = "peter_with_jokes.wav")

if __name__ == "__main__":
    # text = Extract_From_PDF()
    speech_generator()