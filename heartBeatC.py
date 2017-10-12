import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import image as mpimg

### Figure parameters
fig, (ax,ax1) = plt.subplots(1,2,figsize=(15,4))
ax.set_position([-0.1, 0.3, 0.4, 0.4])
ax1.set_position([0.25, 0.15, 0.7, 0.75])
ax1.grid(True)
ax1.tick_params(labelsize=16)

### Data load
## See specific data files in data/ folder
dat = np.loadtxt('data/c1rr.txt',usecols=0)
dat = dat[:100] # pick up first 100 points
## Ice data
# dat = np.loadtxt('data/ice.csv',usecols=0,delimiter=';',comments=';')
## sauna/ice-swimming change point + convert to sec
# dat = dat[55085:55185] * 0.001
## Specific intervals of the ice-data
## dat[53900:53950] -- ice-swimming
## dat[54725:54775] -- sauna
## Fake data
# dat = 0.1*np.ones((1,10))
# dat = np.concatenate((1.0*np.ones((1,10)),dat),axis=0)
# dat.shape = (20,)

### Load the beating heart frames
img = mpimg.imread('rheart.png')
imgB = mpimg.imread('rheart11.png')
imgC = mpimg.imread('rheart22.png')

### Plot initial RR curve
xdata, ydata = [], []
ln, = ax1.plot([], [], '-r', animated=True)
ax1.plot(np.arange(1,dat.size+1),dat,'-',color='grey')

### Init function for the animation
def init():
    ### The RR plot
    ax1.set_ylabel('RR, s',fontsize=16)
    ax1.set_xlabel('# beats',fontsize=16)
    ax1.set_xlim(1-0.5, dat.size+0.5)
    ax1.set_ylim(np.min(dat)-0.1, np.max(dat)+0.1)
    ax1.set_title('Inter-beat intervals, RR',fontsize=20)
    ### Heart-plot
    imgplot = ax.imshow(imgB,animated=True)
    ax.axis('off')
    ### Wait addition 5 sec to get screen recording software ready
    #ani.event_source.interval = 5000
    return imgplot,ln

def update(frame):
    ### The update function for the animation
    global xdata
    global ydata
    global ln
    ### A single beat is divided into four consecutive frames
    if((frame % 4) == 0): # the frame 1
        ## RR data update
        xdata.append(frame//4+1)
        ydata.append(dat[frame//4])
        ln, = ax1.plot(xdata,ydata,'-or')
        ## Heart beat data (icon at rest, smallest amplitude)
        ax.clear()
        imgplot = ax.imshow(imgB,animated=True)
        ax.axis('off')
        # ax.set_title('Duration: '+ str(1000*dat[frame//4])+' ms')
        ## Specific interval corresponding to the RR interval
        ani.event_source.interval = 1000*dat[frame//4]
    elif ((frame % 4) == 1): # the frame 2
        ## Heart beat (full amplitude)
        ax.clear()
        imgplot = ax.imshow(img,animated=True)
        ax.axis('off')
        ## small delay for the visualiation of the beat itself
        ani.event_source.interval = 40
    elif ((frame % 4) == 2): # the frame 3
        ## Heart beat (at rest)
        ax.clear()
        imgplot = ax.imshow(imgB,animated=True)
        ax.axis('off')
        ## small delay for the visualiation of the beat itself
        ani.event_source.interval = 40
    elif ((frame % 4) == 3): # the frame 4
        ## Heart beat (small amplitude to mimick two-phase beating)
        ax.clear()
        imgplot = ax.imshow(imgC,animated=True)
        ax.axis('off')
        ## small delay for the visualiation of the beat itself
        ani.event_source.interval = 40

    return imgplot,ln

### Animation 
ani = FuncAnimation(fig, update, frames=dat.size*4,
                    init_func=init, blit=False, repeat=False)

### Saving options (do not really work to keep the "real-time" of the animation
#ani.save(filename='anim.mp4')
# ani.save('anim.gif',writer='imagemagick')
# ani.to_html5_video()

### Show the animation
plt.show()
