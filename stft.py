import scipy.io.wavfile
from scipy.signal.windows import hann as hann
import numpy as np
import matplotlib.pyplot as plt

fs, z = scipy.io.wavfile.read('aai_input.wav')

plt.plot(z)

Z = np.log(np.abs(np.fft.fft(z)))

plt.plot(Z)

T = 1

def stft(T):

	N = int(T*fs)

	wins = np.arange(0, z.shape[0], N)

	Z = []

	for n in range(len(wins)-1):

		x = z[wins[n]:wins[n+1]]
		X = np.log(np.abs(np.fft.fft(x*hann(N))))
		Z.append(X)

	Q = np.vstack(Z)
	Q = Q[:, 0:int(N/2)]
	Q = Q[:, ::-1].T

	plt.figure()
	plt.imshow(Q, aspect='auto')
	plt.colorbar()