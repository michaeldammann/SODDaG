'''
Global configurations
'''

SHAPES = ["CIRCLE", "RECTANGLE"]
'''
SHAPES: List of what kind of objects can occur in the images.
Implemented: "CIRCLE", "RECTANGLE" not yet implemented: "ANNULUS", "ARROW", "ELLIPSE", "POLYGON",
'''

COLORS = ["red", "green", "blue", "black", "grey", "pink"]
'''
COLORS: List of colors the occurring objects can have.
Implemented: "RED", "GREEN"
'''

EDGECOLORS = ["red", "green", "blue", "black", "grey", "white"]

OVERLAP = False
'''
OVERLAP: Are occurring objects allowed to overlap? 
Implemented: False, not yet implemented: True
'''

IMG_HEIGHT= 15
'''
IMG_HEIGHT: "Matplotlib Dimension" of the generated images
'''
IMG_WIDTH = 15
'''
IMG_WIDTH: "Matplotlib Dimension" of the generated images
'''

N_OBJECTS_MIN=1
'''
N_OBJECTS_MIN: Minimum number of objects that can occur in one image
'''
N_OBJECTS_MAX=1
'''
N_OBJECTS_MAX: Maximum number of objects that can occur in one image
'''

MIN_SIZE = 0.5
'''
MIN_SIZE: Minimal size of object in "Matplotlib Dimensions" 
'''

MAX_SIZE = 6.0
'''
MAX_SIZE: Maximum size of object in "Matplotlib Dimensions" 
'''

SHOW_FRAME = True
'''
SHOW_FRAME: Whether to show black frame around image'''