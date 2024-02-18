import numpy as np
 
# Create a 3-D NumPy array
array_3d = np.array([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
    [[19, 20, 21], [22, 23, 24], [25, 26, 27]]
])

print(array_3d.shape)
x= array_3d[0,0,2] #rij - kolom - diepte voor image(element)   - nul telt mee --> 1ste rij 1ste colom 3de element
x2= array_3d[0,1] #rij - kolom - diepte voor image(element)   - nul telt mee --> 1ste rij 2de colom 
y = array_3d[:,1] #rij - kolom - diepte voor image(element)   - nul telt mee ---> alle rijen 2de colom
z = array_3d[:,:,1] #rij - kolom - diepte voor image(element)  - nul telt mee  --> alle rijen alle colomen 2de element
a = array_3d[:,-1] #rij - kolom - diepte voor image(element)   - nul telt mee --> alle rijen laatste colom
print(x2)
# print(y)
# print(z)
# print(a)

# Create a sample 3D array
arr = np.arange(12).reshape(2, 2, 3)
print("Original array:")
print(arr)
concatenated_array = np.concatenate((arr, arr), axis=1)
print("concatenated_array:")
print(concatenated_array)

transform_array = np.array([[1,1,2,1],[1,2,1,1]])



for i in range(transform_array.shape[0]):
    
    for j in range(transform_array.shape[1]):
        
        # print(transform_array[i,j])
        if transform_array[i,j] == 2:
            # print("i",i)
            # print("j",j)
            
            sliced_part = concatenated_array[i,j]
            # print(sliced_part)
            Hflipped = np.flip(sliced_part, axis=0)
            # print("flipped",Hflipped)
            # replace part
            concatenated_array[i,j] = Hflipped

print("flipped part concatenated_array:")
print(concatenated_array)


# # Slice a portion of the array (for example, along the first dimension)
# sliced_part = arr[0, :, :]
# print("\nSliced part:")
# print(sliced_part)

# # Flip the sliced part along a specified axis (for example, the first axis)
# flipped_part = np.flip(sliced_part, axis=0)
# print("\nFlipped sliced part:")
# print(flipped_part)
# arr[0, :, :] = flipped_part
# print("\nArray after replacement:")
# print(arr)