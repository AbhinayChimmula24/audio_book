import librosa
import numpy as np
import soundfile as sf

# Assuming audio_path_1 and audio_path_2 are defined
y1, sr1 = librosa.load('')
y2, sr2 = librosa.load('')

# Simple feature extraction: RMS (root mean square) energy for loudness matching
rms_energy_1 = np.sqrt(np.mean(np.square(y1)))

# Calculate the RMS energy of the second file
rms_energy_2 = np.sqrt(np.mean(np.square(y2)))

# Calculate the adjustment factor to match the loudness
adjustment_factor = rms_energy_1 / rms_energy_2

# Apply the adjustment to the second file to match the loudness of the first file
y2_adjusted = y2 * adjustment_factor

# Save the adjusted audio as a new third file

audio_path_3 = 'this_is_it.wav'
sf.write(audio_path_3, y2_adjusted, sr2)