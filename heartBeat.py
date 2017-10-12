import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import image as mpimg

fig, (ax,ax1) = plt.subplots(1,2,figsize=(15,4))
ax.set_position([-0.1, 0.3, 0.4, 0.4])
ax1.set_position([0.25, 0.15, 0.7, 0.75])
ax1.grid(True)
ax1.tick_params(labelsize=16)

xdata, ydata = [], []
ln, = ax1.plot([], [], '-r', animated=True)
# dat = np.loadtxt('data/c1rr.txt',usecols=0)
# dat = dat[:100]
# Ice data
dat = np.loadtxt('data/ice.csv',usecols=0,delimiter=';',comments=';')
dat = dat[55085:55185] * 0.001 ## sauna/ice-swimming change, convert to sec
## dat[53900:53950] -- ice-swimming
## dat[54725:54775] -- sauna
# Fake data
# dat = 0.1*np.ones((1,10))
# dat = np.concatenate((1.0*np.ones((1,10)),dat),axis=0)
# dat.shape = (20,)

img = mpimg.imread('rheart.png')
imgB = mpimg.imread('rheart11.png')
imgC = mpimg.imread('rheart22.png')

ax1.plot(np.arange(1,dat.size+1),dat,'-',color='grey')

def init():
    ax1.set_ylabel('RR, s',fontsize=16)
    ax1.set_xlabel('# beats',fontsize=16)
    ax1.set_xlim(1-0.5, dat.size+0.5)
    ax1.set_ylim(np.min(dat)-0.1, np.max(dat)+0.1)
    # ln, = ax1.plot(xdata,ydata,animated=True)
    ax1.set_title('Inter-beat intervals, RR',fontsize=20)
    imgplot = ax.imshow(imgB,animated=True)
    ax.axis('off')
    ani.event_source.interval = 5000
    return imgplot,ln

def update(frame):
    global xdata
    global ydata
    global ln
    if((frame % 4) == 0):
        ## RR data
        xdata.append(frame//4+1)
        ydata.append(dat[frame//4])
        ln, = ax1.plot(xdata,ydata,'-or')
        ## Heart data
        ax.clear()
        imgplot = ax.imshow(imgB,animated=True)
        ax.axis('off')
        # ax.set_title('Duration: '+ str(1000*dat[frame//4])+' ms')
        ani.event_source.interval = 1000*dat[frame//4]
    elif ((frame % 4) == 1):
        ## Heart beat (full amplitude)
        ax.clear()
        imgplot = ax.imshow(img,animated=True)
        ax.axis('off')
        ani.event_source.interval = 40 #infinitesimal beat itself
    elif ((frame % 4) == 2):
        ax.clear()
        imgplot = ax.imshow(imgB,animated=True)
        ax.axis('off')
        ani.event_source.interval = 40 #infinitesimal beat itself
    elif ((frame % 4) == 3):
        ax.clear()
        imgplot = ax.imshow(imgC,animated=True)
        ax.axis('off')
        ani.event_source.interval = 40 #infinitesimal beat itself

    return imgplot,ln

ani = FuncAnimation(fig, update, frames=dat.size*4,
                    init_func=init, blit=False, repeat=False)

#ani.save(filename='anim.mp4')
# ani.save('anim.gif',writer='imagemagick')
# ani.to_html5_video()

plt.show()
