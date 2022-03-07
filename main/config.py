'''
Global configurations
'''

N_IMAGES = 100
'''
N_IMAGES: Number of images to be generated
'''

GENERATION_SEED = 42
'''
GENERATION_SEED: Seed for (pseudo-)random image generation (helpful e.g. for reproducibility)
'''

SHAPES = ["CIRCLE", "RECTANGLE"]
'''
SHAPES: List of what kind of objects can occur in the images.
Implemented: "CIRCLE", "RECTANGLE" not yet implemented: "ANNULUS", "ARROW", "ELLIPSE", "POLYGON",
'''

IMG_HEIGHT= 15
'''
IMG_HEIGHT: "Matplotlib Dimension" of the generated images
'''
IMG_WIDTH = 15
'''
IMG_WIDTH: "Matplotlib Dimension" of the generated images
'''

N_OBJECTS_MIN=2
'''
N_OBJECTS_MIN: Minimum number of objects that can occur in one image
'''
N_OBJECTS_MAX=2
'''
N_OBJECTS_MAX: Maximum number of objects that can occur in one image
'''

MIN_SIZE = 2.0
'''
MIN_SIZE: Minimal size of object in "Matplotlib Dimensions" 
'''

MAX_SIZE = 8.0
'''
MAX_SIZE: Maximum size of object in "Matplotlib Dimensions" 
E.g., if IMG_HEIGHT=15 and MAX_SIZE=8, then an objects spans at maximum 8/15 of the height of the image
'''

EDGE_BUFFER = 0.5
'''
EDGE_BUFFER: Minimum distance between frame and center of object 
(depending on MAX_SIZE, objects might still go over image limits)
'''

SHOW_FRAME = True
'''
SHOW_FRAME: Whether to show black frame around image'''

ROOTSAVEDIR = 'dataset'
'''
ROOTSAVEDIR: Where generated dataset will be located
'''

DRAW_BBOXES_MODE = False
'''
DRAW_BBOXES_MODE: Mode that adds bboxes of already generated images to those images 
(in a new directory, original images not overwritten). Mainly used for testing.
'''

N_DRAWN_BBOXES = 100
'''
N_DRAWN_BBOXES: If DRAW_BBOXES_MODE: Number of Images with BBoxes to be drawn.
'''