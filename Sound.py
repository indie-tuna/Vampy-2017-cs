# in this approach to making sound, we'll need a few
# libraries. matplotlib.pyplot, which will be abbreviated
# "plt" from now on, will be used to plot a sound wave, useful
# for debugging. numpy will be used to create and manipulate
# C-like arrays. We have to use C-like arrays because that's what
# the sound card is expecting: a continuous block of memory, not
# python's built-in lists, which are actually linked lists scattered
# throughout memory. random will be used to generate white noise, and
# time will be used to make sure the program doesn't close before
# the sound finishes playing. sounddevice is how we tell the sound
# card to play a sound, given a C-like array and a sampling frequency.
# and math will be used to create sine-tones.
import matplotlib.pyplot as plt
import numpy
import random
import time
import sounddevice
import math

# fs = the sampling frequency
# this means the number of data points we're using for 1 second of sound
# higher means better sound quality but more memory needed
# a good default is 48 thousand, but try 1 thousand and see what happens
fs = 48000

# numpy.zeros(N) = a C-like array of N zeros
# so, silence = a second's worth of zeros
# try replacing "fs" here with "int(fs/2)" or "2*fs"
silence = numpy.zeros(fs)

# A4 = the fourth A in music, which has a frequency of 440hz
# first, we make an array of zeros, then we fill it with
# real data using a for loop
# spend a moment understanding how the equations for volume,
# freq, and A4[x] work.
# it might be useful to know that all notes in music follow this
# rule: a note k half steps above A4 has the frequency 440*2**(k/12).
# that means that every 12 half steps, or one octave, the frequency
# doubles.
# What is the maximum and minimum values that A4[x] could be? these
# are the same maximums and minimums that we're allowed to send
# to the sound card.
A4 = numpy.zeros(fs)
for x in range(int(len(A4)/2.0)):
	volume = 1.25
	freq   = 440 * 2**(0/12)
	A4[x]  = volume * math.sin(2*math.pi * freq*x/fs)

# B4 is two half steps above the central A4, so we use "2/12" instead
# of "0/12" in the freq equation. also take a moment to see how the
# volume equation in this one differs from above. How would you make it
# have a constant 75% volume?

Bb4 = numpy.zeros(fs)
for x in range(len(Bb4)):
	volume = .75
	freq   = 440 * 2**(1/12)
	Bb4[x]  = volume * math.sin(2*math.pi * freq*x/fs)


B4 = numpy.zeros(fs)
for x in range(len(B4)):
	volume = 1.5
	freq   = 440 * 2**(2/12)
	B4[x]  = volume * math.sin(2*math.pi * freq*x/fs)

C4 = numpy.zeros(fs)
for x in range(len(C4)):
	volume = .75
	freq   = 440 * 2**(3/12)
	C4[x]  = volume * math.sin(2*math.pi * freq*x/fs)

D4 = numpy.zeros(fs)
for x in range(len(D4)):
	volume = .75
	freq   = 440 * 2**(5/12)
	D4[x]  = volume * math.sin(2*math.pi * freq*x/fs)

E4 = numpy.zeros(fs)
for x in range(len(E4)):
	volume = .75
	freq   = 440 * 2**(7/12)
	E4[x]  = volume * math.sin(2*math.pi * freq*x/fs)

F4 = numpy.zeros(fs)
for x in range(len(F4)):
	volume = .75
	freq   = 440 * 2**(8/12)
	F4[x]  = volume * math.sin(2*math.pi * freq*x/fs)

G4 = numpy.zeros(fs)
for x in range(len(G4)):
	volume = .75
	freq   = 440 * 2**(10/12)
	G4[x]  = volume * math.sin(2*math.pi * freq*x/fs)

# white noise is simply random data points uniformly
# distributed.
noise = numpy.zeros(fs)
for x in range(len(noise)):
	noise[x] = random.uniform(-1, 1)

# we have to send a single C-like array to sounddevice,
# so we can make a python list of all of the pieces we
# want in our "song," then have numpy concatenate them
# into a single C-like array. we made a "noise" piece
# up above but never used it. try inserting it between
# the A4 and B4.
pieces = [A4]
song = numpy.concatenate(pieces)

# we finally tell the sound card to play our song, and
# tell it what the sampling frequency of our song is
# so it doesn't play it too fast or too slow.
# try sending it the wrong sampling rate (for example,
# "2*fs" instead of "fs").
sounddevice.play(song, fs)

# before we quit, plot the values of the song. a pygame-like
# window will pop up that you can interact with. I suggest
# clicking the "pan" button in the bottom, then using right-
# mouse-click-and-drag to zoom around.
plt.plot(song)
plt.show()

# sleep for the length of the song. remember, the fs means
# the number of data points per second, so the number of
# the data points in our song divided by that number should
# give us the length in time of the song.
# note, we only have to do this because there isn't something
# else keeping the program alive, like a game loop or server.
time.sleep(len(song)/fs)
