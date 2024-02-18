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
# print(np_image)

# Display the image using Matplotlib
# plt.imshow(np_image)
# plt.show()

np_image2 = np.tile(np_image,(2, 3, 1))  #'(columns, rows, diepte)"
pixelw=len(np_image[0])
pixelh=len(np_image[:,0])
print(pixelw)
print(pixelh)
print("np_image2")
print(np_image2)
# plt.imshow(np_image2)
# plt.show()

transform_array = np.array([[1,1,2],[1,2,1]])
# sliced_partje = np_image2[0:2,4:6]  #rij 0 en 1 colom 5 en 6 dus 0:2 en 4:6
# print("sliced partje\n", sliced_partje)
for i in range(transform_array.shape[0]):
    
    for j in range(transform_array.shape[1]):
        
        # print(transform_array[i,j])
        if transform_array[i,j] == 2:
            
            print("i",i)
            print("j",j)
           
            # print(f"nodig rij {(i*pixelh)}:{((i*pixelh)+pixelh)} colom {(j*pixelw)+1}:{(j*pixelw)+pixelw+1}")
            startrow = i*pixelh
            endrow = ((i*pixelh)+pixelh+1)
            startcolumn = ((j*pixelw))
            endcolumn = ((j*pixelw)+pixelw+1)
            print(f"startrow:{startrow} endrow:{endrow} startcolumn:{startcolumn} endcolumn:{endcolumn}")
            sliced_part = np_image2[startrow:endrow,startcolumn:endcolumn]  #rij 0 en 1 : colom 5 en 6 
            
            # print("sliced part\n",sliced_part)
            # sliced_part = concatenated_array[i,j]
            # print(sliced_part)
            Hflipped = np.flip(sliced_part, axis=0)
            # print("flipped",Hflipped)
            # replace part
            np_image2[startrow:endrow,startcolumn:endcolumn] = Hflipped

# print("final image \n", np_image2)
plt.imshow(np_image2)
plt.show()
