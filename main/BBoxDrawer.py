from pathlib import Path
import config
from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import json

class BBoxDrawer:

    def __init__(self):
        self.imgs_path = Path('..', config.ROOTSAVEDIR, 'imgs')
        self.bboxs_path = Path('..', config.ROOTSAVEDIR, 'bboxes')
        Path('..', config.ROOTSAVEDIR, 'bboximgs').mkdir(parents=True, exist_ok=True)
        self.bboximgs_path = Path('..', config.ROOTSAVEDIR, 'bboximgs')

    def bboxes_single_image(self, i_img):
        source_img = Image.open(self.imgs_path/(str(i_img)+'.png')).convert("RGBA")
        with open(self.bboxs_path/(str(i_img)+'.json'), 'r') as f:
            bboxes = json.load(f)

        for i, elem in enumerate(bboxes):
            for key in elem:
                x_min = float(bboxes[i][key]['x_min']) * source_img.size[0]
                x_max = float(bboxes[i][key]['x_max']) * source_img.size[0]
                y_min = source_img.size[1]-float(bboxes[i][key]['y_min']) * source_img.size[1]
                y_max = source_img.size[1]-float(bboxes[i][key]['y_max']) * source_img.size[1]

                draw = ImageDraw.Draw(source_img)
                draw.rectangle(((x_min, y_min), (x_max, y_max)), outline="black")

            source_img.save(self.bboximgs_path/(str(i_img)+'.png'), "PNG")
