#  This file is used to process the audio file and 
# enhance the audio quality by reducing the noise and enhancing the audio quality.

from pedalboard.io import AudioFile
from pedalboard import *
import noisereduce as nr

sr=44100
with AudioFile('/Users/achimmula/Desktop/audio_books/Daniel_Kahneman-Thinking,_Fast_and_Slow___Trevor_Noah.wav').resampled_to(sr) as f:
    audio = f.read(f.frames)

reduced_noise = nr.reduce_noise(y=audio, sr=sr, stationary=True, prop_decrease=0.85)  # Increase prop_decrease for better noise reduction

board = Pedalboard([
    NoiseGate(threshold_db=-40, ratio=2.0, release_ms=200),  # Softer threshold, slightly higher ratio, faster release
    Compressor(threshold_db=-20, ratio=3.0, attack_ms=10, release_ms=100),  # Softer threshold, gentle compression, quick attack and release
    LowShelfFilter(cutoff_frequency_hz=300, gain_db=6, q=0.7),  # Lower cutoff, moderate gain, softer Q for a smoother low-end boost
    Gain(gain_db=5)  # Reduced gain to prevent over-amplification
])

effected = board(reduced_noise, sr)


with AudioFile('audio1_enhenced.wav', 'w', sr, effected.shape[0]) as f:
  f.write(effected)