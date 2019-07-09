import tkinter
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

word = []
frequency = []
filename = "trump_word_frequencies.txt"
file = open(filename, "r")
for line in file:
    w = line.split(", ")
    word.append(w[0])
    frequency.append(w[1])

plt.bar(word, frequency, color='r')
fh = open("hello.txt","w")
write(plt)
fh.close()
#plt.show()
