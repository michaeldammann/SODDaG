import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
from config import config
import random

#define Matplotlib figure and axis
fig, ax = plt.subplots()
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)

ax.set_xlim([0, config.IMG_WIDTH])
ax.set_ylim([0, config.IMG_HEIGHT])

def show_frame(is_visible):
    ax.spines['top'].set_visible(is_visible)
    ax.spines['right'].set_visible(is_visible)
    ax.spines['bottom'].set_visible(is_visible)
    ax.spines['left'].set_visible(is_visible)

show_frame(config.SHOW_FRAME)

shapelist = [Rectangle]

#add rectangle to plot
ax.add_patch(Rectangle((random.uniform(0, config.IMG_WIDTH), random.uniform(0, config.IMG_HEIGHT)),
                       random.uniform(0, config.IMG_WIDTH), random.uniform(0, config.IMG_HEIGHT),
                       facecolor=random.sample(config.COLORS, 1)[0],edgecolor=random.sample(config.EDGECOLORS,1)[0]))

#display plot
plt.show()