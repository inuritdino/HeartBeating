import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from threading import Timer


dat = np.loadtxt('data/n1rr.txt',usecols=0)
img0 = mpimg.imread('heart.png')
img1 = mpimg.imread('heart2.png')
img2 = mpimg.imread('heart3.png')

fig, ax = plt.subplots()

def beat():
    ax.clear()
    plt.imshow(img1)

def relax():
    ax.clear()
    plt.imshow(img0)

def afterbeat():
    plt.imshow(img2)


relax()
t = Timer(1.5, beat)
t.start()
t = Timer(1.5, relax)
t.start()

