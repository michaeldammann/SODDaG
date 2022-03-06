import config
from Drawer import Drawer

def main():
    drawer = Drawer()
    for i in range(config.N_IMAGES):
        drawer.save_single_image(i)

if __name__ == "__main__":
    main()
