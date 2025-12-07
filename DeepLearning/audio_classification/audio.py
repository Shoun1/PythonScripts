import os
import librosa
import torchaudio
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"D:\pythonenv\DeepLearning\audio_classification\audio2.wav.wav"

if not os.path.isfile(file_path):
    raise FileNotFoundError(f"Audio file not found: {file_path}")

waveform, sample_rate = torchaudio.load(file_path)
print("✅ Loaded with torchaudio:", waveform.shape, sample_rate)

# Convert waveform tensor to numpy array and flatten to 1D
y = waveform.numpy().squeeze()
sr = sample_rate

plt.figure(figsize=(10, 4))
librosa.display.waveshow(y, sr=sr)
plt.title("Waveform")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.tight_layout()
plt.savefig('D:\pythonenv\DeepLearning\plots\waveform.png')

# Generate mel spectrogram
#spectrogram = librosa.feature.melspectrogram(y=y,sr=sr)

'''import wave
obj = wave.open("audio2.wav.wav","rb")
sample_freq = obj.getframerate()
n_samples = obj.getnframes()
print(sample_freq)
print(n_samples)

#get the digital signal
signal_wave = obj.readframes(-1)
obj.close()

#length of signal in bytes
t_audio = n_samples / sample_freq
print(t_audio)

signal_array = np.frombuffer(signal_wave, dtype=np.int16)
print("Bytes array: {}".format(signal_array))

sns.heatmap(signal_array)
sns.savefig('D:\pythonenv\plots\heatmap.png')

# If the audio is stereo, reshape to (n_samples, n_channels) and select one channel
if obj.getnchannels() > 1:
    signal_array = signal_array.reshape(-1, obj.getnchannels())
    signal_array = signal_array[:, 0]  # Use the first channel

# Ensure times and signal_array have the same length
times = np.linspace(0, t_audio, num=signal_array.shape[0])

plt.figure(figsize=(15,5))
plt.plot(times, signal_array)
plt.title("Audio signal")
plt.xlabel("Time (s)")
plt.ylabel("Signal wave")
plt.xlim(0, t_audio)
plt.savefig('D:\pythonenv\plots\wave.png')'''