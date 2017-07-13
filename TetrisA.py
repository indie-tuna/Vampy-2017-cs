import matplotlib.pyplot as plt
import numpy
import random
import time
import sounddevice
import math

fs = 48000

silence = numpy.zeros(fs)

A2 = numpy.zeros(fs)
for x in range(len(A2)):
	volume = .50
	freq   = 440 * 2**(0/12)
	A2[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if A2[x] > 0:
		A2[x] = 1
	else:
		A2[x] = 0

A4 = numpy.zeros(int(fs/2))
for x in range(len(A4)):
	volume = .50
	freq   = 440 * 2**(0/12)
	A4[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if A2[x] > 0:
		A4[x] = 1
	else:
		A4[x] = 0
A8 = numpy.zeros(int(fs/4))
for x in range(len(A8)):
	volume = .50
	freq   = 440 * 2**(0/12)
	A8[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if A8[x] > 0:
		A8[x] = 1
	else:
		A8[x] = 0
B8 = numpy.zeros(int(fs/4))
for x in range(len(B8)):
	volume = .50
	freq   = 440 * 2**(2/12)
	B8[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if B8[x] > 0:
		B8[x] = 1
	else:
		B8[x] = 0
B38 = numpy.zeros(int(fs*.75))
for x in range(len(B38)):
	volume = .50
	freq   = 440 * 2**(2/12)
	B38[x] = volume * math.sin(2*math.pi * freq*x/fs)
	if B38[x] > 0:
		B38[x] = 1
	else:
		B38[x] = 0
C4 = numpy.zeros(int(fs/2))
for x in range(len(C4)):
	volume = .50
	freq   = 440 * 2**(3/12)
	C4[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if C4[x] > 0:
		C4[x] = 1
	else:
		C4[x] = 0
C8 = numpy.zeros(int(fs/4))
for x in range(len(C8)):
	volume = .50
	freq   = 440 * 2**(3/12)
	C8[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if C8[x] > 0:
		C8[x] = 1
	else:
		C8[x] = 0
D4 = numpy.zeros(int(fs/2))
for x in range(len(D4)):
	volume = .50
	freq   = 440 * 2**(5/12)
	D4[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if D4[x] > 0:
		D4[x] = 1
	else:
		D4[x] = 0
D8 = numpy.zeros(int(fs/4))
for x in range(len(A8)):
	volume = .50
	freq   = 440 * 2**(5/12)
	D8[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if D8[x] > 0:
		D8[x] = 1
	else:
		D8[x] = 0
E4 = numpy.zeros(int(fs/2))
for x in range(len(E4)):
	volume = .50
	freq   = 440 * 2**(7/12)
	E4[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if E4[x] > 0:




		E4[x] = 1
	else:
		E4[x] = 0

noise = numpy.zeros(fs)
intro = numpy.zeros(fs)
stac = numpy.zeros(int(fs/40))
for x in range(len(noise)):
	noise[x] = random.uniform(-1, 1)
pieces = [intro, E4, B8, C8, D4, C8, B8, A4, stac, A8, C8, E4, D8, C8, B38, C8, D4, E4, C4, A4, stac, A2]
song = numpy.concatenate(pieces)

sounddevice.play(song, fs)
plt.plot(song)
plt.show()

time.sleep(len(song)/fs)
