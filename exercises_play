
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

np_image_addedA1 = np.concatenate((np_image,np_image), axis = 1)
#axis 1 verlengt de image naar opzij - er komen pixels per rij bij
print(np_image.shape)

#print(f"np_image_addedA1 \n {np_image_addedA1} \n pixels erbij per rij")
plt.imshow(np_image_addedA1)
plt.show()

np_image_addedA0 = np.concatenate((np_image,np_image), axis = 0)
#axis 0 verlengt de image naar onder - er komen pixels per kolom bij
print(np_image.shape)

#print(f"np_image_addedA0 \n {np_image_addedA0} \n pixels erbij per kolom")
plt.imshow(np_image_addedA0)
plt.show()

print(np_image.shape)

def add_vert():
    pass

def add_hor():
    pass