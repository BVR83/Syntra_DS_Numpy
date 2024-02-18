from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os
import sys

# Print the list of loaded modules
#print(sys.modules.keys())
print("start here")

# Load the image using Pillow
image_path = os.path.join( 'data', 'BVR.jpg')  # Replace with the actual path to your image file
image = Image.open(image_path)

# Convert the image to a NumPy array
np_image = np.array(image)
#print(np_image)

# Display the image using Matplotlib
plt.imshow(np_image)
plt.show()


# np_image_addedA1 = np.concatenate((np_image,np_image), axis = 1)
# #axis 1 verlengt de image naar opzij - er komen pixels per rij bij
# print(np_image.shape)
# print(f"np_image_addedA1 \n {np_image_addedA1} \n pixels erbij per rij")
# plt.imshow(np_image_addedA1)
# plt.show()
# #np_image_addedA0 = np.concatenate((np_image,np_image), axis = 0)
# #axis 0 verlengt de image naar onder - er komen pixels per kolom bij
# print(np_image.shape)
# #print(f"np_image_addedA0 \n {np_image_addedA0} \n pixels erbij per kolom")
# plt.imshow(np_image_addedA0)
# plt.show()

# print(np_image.shape)

def add_hor(np_input, amount):
    np_image_addedA1 = np.tile(np_input,(amount,1))
    print(f"np_image_addedA1 \n {np_image_addedA1} \n pixels erbij per kolom")
    plt.imshow(np_image_addedA1)
    plt.show()
    print(np_image_addedA1)

def add_vert(np_input, amount):
    np_image_addedA0 = np.tile(np_input,amount)
    print(f"np_image_addedA0 \n {np_image_addedA0} \n pixels erbij per kolom")
    plt.imshow(np_image_addedA0)
    plt.show()
    print(np_image_addedA0)
    
def tile_img(np_input, vx, hx):

    np_image_tiled = np.tile(np_input,(vx, hx, 1))  #'(columns, rows, diepte)"
    plt.imshow(np_image_tiled)
    plt.show()
    print(np_image_tiled.shape)


def tile_img_matrix(np_input, Vorm_Matrix ):
    hx = Vorm_Matrix.shape[0]
    vx = Vorm_Matrix.shape[1]
    np_image_tiled = np.tile(np_input,(vx, hx, 1))  #'(columns, rows, diepte)"
    plt.imshow(np_image_tiled)
    plt.show()
    print(np_image_tiled.shape)

 
def tile_3d_array(np_input, amount_rows, *Mdirections):
   
   # Tile along the first axis (rows)
    tiled_mirrored_array = np.tile(np_input, (1, amount_rows, 1))
    initial_tiled_array = np.copy(tiled_mirrored_array)
    plt.imshow(tiled_mirrored_array)
    plt.show()

# Add mirrored versions based on specified directions
    for direction in Mdirections:
        if direction == 'H':
            mirrored_row_h = np.flip(initial_tiled_array, axis=1) # Flip the entire array horizontally
            tiled_mirrored_array = np.concatenate((tiled_mirrored_array,mirrored_row_h), axis=0)
            plt.imshow(tiled_mirrored_array)
            plt.show()
        elif direction == 'V':
            mirrored_column_v = np.flip(initial_tiled_array, axis=0)  # Flip the entire array vertically
            tiled_mirrored_array = np.concatenate((tiled_mirrored_array,mirrored_column_v), axis=0) 
            plt.imshow(tiled_mirrored_array)
            plt.show()

        elif direction == 'HV':
            mirrored_row_hv = np.flip(np.flip(initial_tiled_array, axis=1), axis=0)
            tiled_mirrored_array = np.concatenate((tiled_mirrored_array,mirrored_row_hv), axis=0)
            plt.imshow(tiled_mirrored_array)
            plt.show()

    return tiled_mirrored_array


    
row_repeat = 5
# tiled_result = tile_3d_array(np_image, row_repeat, "H", "H" ,"V", "HV") 

vorm_matrix = np.array([[1 for i in range(8)] for j in range(3)])

tile_img_matrix(np_image,vorm_matrix)


def enlarge():
    pass
    np_image_addedA1  = np.repeat(np_input, 3, axis=1) 
    #  axis 1 in de breedte 
    # axis 0 in de lengte


