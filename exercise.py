from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import functions

# Load the image using Pillow
image_path = os.path.join( 'data', 'BVR.jpg')  # Replace with the actual path to your image file
image = Image.open(image_path)
# Convert the image to a NumPy array
np_image = np.array(image)




# functions.tile_img(np_image,5,6)

# shape_array = np.zeros((5, 4))
# functions.tile_img_matrix(np_image,shape_array)

# functions.tile_array_directions(np_image,"V","H")

# transform_array = np.array([[1,1,2,3,2,1],[1,2,1,1,2,4],[1,1,1,1,1,1],[1,2,1,1,2,2]])
# functions.tilemirror_matrix(np_image,transform_array)

# functions.enlargeImgBorder(np_image,4)

# functions.word("fyipython")

# functions.add_border(np_image,150,50,50,50,255)