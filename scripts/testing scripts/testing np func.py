import numpy as np

# Existing multi-dimensional matrix
matrix_2d = np.array([[0, 0, 0], [255,255,255]])

multi_dimensional_matrix = np.array([[[0, 0, 0]],
                                     [[255, 255, 255]]])

# Add the 2D matrix to the multi-dimensional matrix along axis 0
new_multi_dimensional_matrix = np.concatenate((multi_dimensional_matrix, [matrix_2d]))

print("Original Multi-Dimensional Matrix:")
print(multi_dimensional_matrix)

print("\nMulti-Dimensional Matrix after adding a 2D matrix along axis 0:")
print(new_multi_dimensional_matrix)