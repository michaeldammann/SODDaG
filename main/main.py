import config
from Drawer import Drawer
from BBoxDrawer import BBoxDrawer

def main():
    if config.DRAW_BBOXES_MODE:
        bboxdrawer = BBoxDrawer()
        for i in range(config.N_DRAWN_BBOXES):
            bboxdrawer.bboxes_single_image(i)
    else:
        drawer = Drawer()
        for i in range(config.N_IMAGES):
            drawer.save_single_image(i)

if __name__ == "__main__":
    main()
