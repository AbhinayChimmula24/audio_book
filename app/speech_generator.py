import torch
from TTS.api import TTS

def speech_generator():

    device = "cuda" if torch.cuda.is_available() else "cpu"

    print(TTS().list_models())

    tts = TTS( "tts_models/multilingual/multi-dataset/xtts_v2").to(device)

    wav = tts.tts( text = "Hello, this is peter griffin you wanna subscribe to my audio book come on this is gonna be Fun I promise you. If it is not fun Its your fault not mine have some sense of humor ", speaker_wav = "/Users/abhinay/audio_book/8y10l4.wav", language="en")
    tts.tts_to_file( text = "The dominant sequence transduction models are based on intricate RNNs or CNNs, sporting an encoder and decoder, with an attention mechanism connecting them like a secret handshake. But we're not into secrets! So, we propose a new, simple network architecture called the Transformer, which only believes in the power of attention and shuns recurrence and convolutions like a vampire avoids garlic. We tested our model on two machine translation tasks and, voila, it outperformed the competition in quality while being more parallelizable and requiring less time to train. Our Transformer scored 28.4 BLEU points on the WMT 2014 Englishto-German task, leaving other models green with envy and over 2 BLEU points behind. On the WMT 2014 English-to-French task, our Transformer set a new single-model state-of-the-art BLEU score of 41.0 after training for just 3.5 days on eight GPUs – a fraction of the training costs for the best models from the literature! And don't even get us started on the training time savings; it's like comparing a snail to a cheetah!", speaker_wav = "/Users/abhinay/audio_book/8y10l4.wav", language="en", file_path = "/Users/abhinay/audio_book/peter_with_jokes.wav")

if __name__ == "__main__":
    speech_generator()