import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
import config
import random
from pathlib import Path
import numpy as np
import json


class Drawer:
    def __init__(self):
        self.shapes = self.init_shapes()
        random.seed(config.GENERATION_SEED)
        self.fig, self.ax = plt.subplots()
        # Generate save paths if not exist
        Path('..', config.ROOTSAVEDIR).mkdir(parents=True, exist_ok=True)
        Path('..', config.ROOTSAVEDIR, 'imgs').mkdir(parents=True, exist_ok=True)
        Path('..', config.ROOTSAVEDIR, 'bboxes').mkdir(parents=True, exist_ok=True)

    def init_shapes(self):
        all_shapes = []
        for shape in config.SHAPES:
            if shape == 'RECTANGLE':
                all_shapes.append(self.add_rectangle)
            elif shape == 'CIRCLE':
                all_shapes.append(self.add_circle)
            else:
                raise ValueError("{} is not an implemented object shape.".format(shape))

        return all_shapes

    def init_plt(self):
        # define Matplotlib figure and axis
        plt.cla()
        self.ax.axes.xaxis.set_visible(False)
        self.ax.axes.yaxis.set_visible(False)

        self.ax.set_xlim([0, config.IMG_WIDTH])
        self.ax.set_ylim([0, config.IMG_HEIGHT])

        self.ax.spines['top'].set_visible(config.SHOW_FRAME)
        self.ax.spines['right'].set_visible(config.SHOW_FRAME)
        self.ax.spines['bottom'].set_visible(config.SHOW_FRAME)
        self.ax.spines['left'].set_visible(config.SHOW_FRAME)

        plt.gca().set_axis_off()
        plt.subplots_adjust(top=1, bottom=0, right=1, left=0,
                            hspace=0, wspace=0)
        plt.margins(0, 0)
        plt.gca().xaxis.set_major_locator(plt.NullLocator())
        plt.gca().yaxis.set_major_locator(plt.NullLocator())

    def add_rectangle(self, ax):
        '''
        Adds a rectangle at random location with random size to given axes.
        :param ax: Matplotlib Ayes to draw on
        :return: Relative bounding box of the generated and drawn rectangle
        '''
        xy_orig = (random.uniform(config.EDGE_BUFFER, config.IMG_WIDTH - config.EDGE_BUFFER),
                   random.uniform(config.EDGE_BUFFER, config.IMG_HEIGHT - config.EDGE_BUFFER))
        dxy_orig = random.uniform(config.MIN_SIZE / 2, config.MAX_SIZE / 2), random.uniform(config.MIN_SIZE / 2,
                                                                                            config.MAX_SIZE / 2)
        ax.add_patch(Rectangle((xy_orig[0] - dxy_orig[0], xy_orig[1] - dxy_orig[1]),
                               dxy_orig[0] * 2, dxy_orig[1] * 2,
                               facecolor=(random.uniform(0., 1.), random.uniform(0., 1.), random.uniform(0., 1.)),
                               edgecolor=(random.uniform(0., 1.), random.uniform(0., 1.), random.uniform(0., 1.))))

        xy_min = np.clip((np.array(xy_orig) - np.array(dxy_orig)) / config.IMG_WIDTH, 0., 1.)
        xy_max = np.clip((np.array(xy_orig) + np.array(dxy_orig)) / config.IMG_HEIGHT, 0., 1.)

        return {'x_min': xy_min[0], 'x_max': xy_max[0], 'y_min': xy_min[1], 'y_max': xy_max[1]}, 'rectangle'

    def add_circle(self, ax):
        '''
        Adds a circle at random location with random size to given axes.
        :param ax: Matplotlib Ayes to draw on
        :return: Relative bounding box of the generated and drawn circle
        '''

        xy_orig = (random.uniform(config.EDGE_BUFFER, config.IMG_WIDTH - config.EDGE_BUFFER),
                   random.uniform(config.EDGE_BUFFER, config.IMG_HEIGHT - config.EDGE_BUFFER))
        radius = random.uniform(config.MIN_SIZE / 2, config.MAX_SIZE / 2)
        ax.add_patch(Circle(xy_orig, radius,
                            facecolor=(random.uniform(0., 1.), random.uniform(0., 1.), random.uniform(0., 1.)),
                            edgecolor=(random.uniform(0., 1.), random.uniform(0., 1.), random.uniform(0., 1.))
                            ))

        xy_min = np.clip((np.array(xy_orig) - radius) / config.IMG_WIDTH, 0., 1.)
        xy_max = np.clip((np.array(xy_orig) + radius) / config.IMG_HEIGHT, 0., 1.)

        return {'x_min': xy_min[0], 'x_max': xy_max[0], 'y_min': xy_min[1], 'y_max': xy_max[1]}, 'circle'

    def save_single_image(self, i_img):
        self.init_plt()
        n_objects = random.randint(config.N_OBJECTS_MIN, config.N_OBJECTS_MAX)
        bboxes = []  # entries are (x_min, x_max, y_min, y_max)
        for obj_i in range(n_objects):
            bbox, class_obj = random.sample(self.shapes, 1)[0](self.ax)
            bboxes.append({class_obj:bbox})

        # display plot
        plt.savefig(Path('..', config.ROOTSAVEDIR, 'imgs', str(i_img) + '.png'),
                    bbox_inches='tight',
                    pad_inches=0.0)
        with open(Path('..', config.ROOTSAVEDIR, 'bboxes', str(i_img) + '.json'), 'w') as fp:
            json.dump(bboxes, fp)
        '''
        fig.clear()
        plt.close(fig)
        plt.close()
        '''
