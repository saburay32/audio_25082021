import pyaudio
import librosa
import IPython

import matplotlib.pyplot as plt
import librosa.display

audio_data = 'audio_file1.wav'
x , sr = librosa.load(audio_data)
IPython.display.Audio(audio_data)
print(type(x), type(sr))#<class 'numpy.ndarray'> <class 'int'>print(x.shape, sr)#(94316,) 22050
plt.figure(figsize=(14, 5))
librosa.display.waveplot(x, sr=sr)
plt.show()

X = librosa.stft(x)
Xdb = librosa.amplitude_to_db(abs(X))
plt.figure(figsize=(14, 5))
librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
plt.colorbar()
plt.show()