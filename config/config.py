'''
SHAPES: List of what kind of objects can occur in the images
implemented: "CIRLCE", "RECTANGLE" not yet implemented: "ANNULUS", "ARROW", "ELLIPSE", "POLYGON",
'''
SHAPES = ["CIRCLE", "RECTANGLE"]

'''
COLORS: List of colors the occurring objects can have
implemented: "RED", "GREEN"
'''
COLORS = ["RED", "GREEN"]

'''
OVERLAP: Are occurring objects allowed to overlap? 
implemented: False, not yet implemented: True
'''
OVERLAP = False

'''
IMG_HEIGHT, IMG_WIDTH: Dimension of the generated images
'''
IMG_HEIGHT= 150
IMG_WIDTH = 150

'''
N_OBJECTS_MIN, N_OBJECTS_MAX: Minimum and maximum number of objects that can occur in one image
'''
N_OBJECTS_MIN=1
N_OBJECTS_MAX=1
