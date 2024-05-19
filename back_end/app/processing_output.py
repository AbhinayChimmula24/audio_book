import librosa
import numpy as np
from scipy.signal import lfilter
import soundfile as sf

def load_audio(file_path, target_sr=None):
    y, sr = librosa.load(file_path, sr=target_sr)
    return y, sr

def save_audio(y, sr, output_path):
    sf.write(output_path, y, sr)

def extract_features(y, sr):
    # Extract spectral centroid
    spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
    
    # Extract spectral bandwidth
    spectral_bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)[0]
    
    # Extract harmonic-percussive source separation
    y_harmonic, y_percussive = librosa.effects.hpss(y)
    
    return spectral_centroid, spectral_bandwidth, y_harmonic, y_percussive

def apply_features(y_robotic, sr, features_clear):
    spectral_centroid, spectral_bandwidth, y_harmonic, y_percussive = features_clear
    
    # Apply spectral centroid (simplistic approach)
    y_filtered = lfilter([1.0], [1.0, -spectral_centroid.mean()], y_robotic)
    
    # Combine harmonic part from clear sample (for illustration)
    y_combined = y_harmonic + y_percussive * 0.5
    
    return y_combined

def pad_audio(y1, y2):
    if len(y1) > len(y2):
        y2 = np.pad(y2, (0, len(y1) - len(y2)), 'constant')
    elif len(y1) < len(y2):
        y1 = np.pad(y1, (0, len(y2) - len(y1)), 'constant')
    return y1, y2

def main():
    target_sr = 44100  # Target sample rate

    # Load audio files
    y_clear, sr_clear = load_audio('/Users/achimmula/Desktop/audio_books/simon_vauce_rd_pd_test1.wav', target_sr)
    y_robotic, sr_robotic = load_audio('/Users/achimmula/Desktop/speakers/simon_vausce.wav', target_sr)
    
    # Ensure both audios have the same sample rate (resampled already to target_sr)
    if sr_clear != sr_robotic:
        raise ValueError("Sample rates of the audio files do not match after resampling.")

    # Pad audio samples to match their lengths
    y_clear, y_robotic = pad_audio(y_clear, y_robotic)

    # Extract features from the clear audio sample
    features_clear = extract_features(y_clear, sr_clear)
    
    # Apply features to the robotic audio sample
    y_enhanced = apply_features(y_robotic, sr_robotic, features_clear)
    
    # Save the enhanced audio
    save_audio(y_enhanced, sr_robotic, 'enhanced_sample.wav')

if __name__ == "__main__":
    main()
