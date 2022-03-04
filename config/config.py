'''
Global configurations
'''

SHAPES = ["CIRCLE", "RECTANGLE"]
'''
SHAPES: List of what kind of objects can occur in the images.
Implemented: "CIRLCE", "RECTANGLE" not yet implemented: "ANNULUS", "ARROW", "ELLIPSE", "POLYGON",
'''

COLORS = ["RED", "GREEN"]
'''
COLORS: List of colors the occurring objects can have.
Implemented: "RED", "GREEN"
'''

OVERLAP = False
'''
OVERLAP: Are occurring objects allowed to overlap? 
Implemented: False, not yet implemented: True
'''

IMG_HEIGHT= 150
'''
IMG_HEIGHT: Dimension of the generated images
'''
IMG_WIDTH = 150
'''
IMG_WIDTH: Dimension of the generated images
'''

N_OBJECTS_MIN=1
'''
N_OBJECTS_MIN: Minimum number of objects that can occur in one image
'''
N_OBJECTS_MAX=1
'''
N_OBJECTS_MAX: Maximum number of objects that can occur in one image
'''