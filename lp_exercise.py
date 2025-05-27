import numpy as np
import matplotlib.pyplot as plt

N = 101
n = range(-50,51)

X = np.ones((N))
X[0:20] = 0
X[80:101] = 0

plt.figure()
plt.stem(n,X)

E = np.exp(2*np.pi*1j/N*np.outer(n,n))

x = np.dot(X,E)
x.shape

plt.figure()
plt.plot(n, x)

E2 = np.exp(-2*np.pi*1j/N*np.outer(n,n))
X2 = np.dot(x, E2)

plt.figure()
plt.plot(n, X2)

w = np.arange(-np.pi, np.pi, 0.01)
E3 = np.exp(-1j*np.outer(w, n))
X3 = np.dot(E3, x)

plt.figure()
plt.plot(w, np.abs(X3))
plt.plot(np.linspace(-np.pi, np.pi, len(X)), N*X)
