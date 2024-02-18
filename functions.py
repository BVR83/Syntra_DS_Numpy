from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os



def add_hor(np_input, amount):
    """
    Create a horizontally tiled 3-dimensional NumPy array.

    Parameters:
    np_input (numpy.ndarray): The input array to be tiled horizontally.
    amount (int): The number of times to tile the input array horizontally.

    Returns:
    numpy.ndarray: A horizontally tiled 3-dimensional NumPy array.
    """
    np_image_addedA1 = np.tile(np_input,(amount,1))
    return np_image_addedA1


def add_vert(np_input, amount):
    """
    Create a vertically tiled 3-dimensional NumPy array.

    Parameters:
    np_input (numpy.ndarray): The input array to be tiled horizontally.
    amount (int): The number of times to tile the input array horizontally.

    Returns:
    numpy.ndarray: A vertically tiled 3-dimensional NumPy array.
    """
    np_image_addedA0 = np.tile(np_input,(amount, 1, 1))  
    return np_image_addedA0
   
    
def tile_img(np_input, vx, hx):
    """
    Create a vertically and horizontally tiled 3-dimensional NumPy array.

    Parameters:
        np_input (numpy.ndarray): The input array to be tiled.
        vx (int): The number of times to tile the input array vertically.
        hx (int): The number of times to tile the input array horizontally.

    Output:
        the image plot of a vertically and horizontally tiled 3-dimensional NumPy array.
    """
    np_image_tiled = np.tile(np_input,(vx, hx, 1))  #(columns, rows, depth)
    plt.imshow(np_image_tiled)
    plt.show()
    print(np_image_tiled.shape)


def tile_img_matrix(np_input, shape_Matrix ):
    """
    Create a tiled image plot based on the dimensions of the given shape matrix..

    Parameters:
        np_input (numpy.ndarray): The input array to be tiled.
        shape_Matrix (numpy.ndarray): The matrix representing the tiling dimensions.

    Output:
        The image plot of the tiled input array based on the shape matrix.
    """
        
    hx = shape_Matrix.shape[1]
    vx = shape_Matrix.shape[0]
    np_image_tiled = np.tile(np_input,(vx, hx, 1))  #'(columns, rows, diepte)"
    plt.imshow(np_image_tiled)
    plt.show()
    print(np_image_tiled.shape)

 


def tile_array_directions(np_input, *Mdirections):
    """
    Tile the input array along specified directions and output the resulting tiled array.

    Parameters:
        np_input (numpy.ndarray): The input array to be tiled.
        *Mdirections (str): Variable number of strings specifying the directions for mirroring.
            'H': Mirror horizontally.
            'V': Mirror vertically.
            'HV': Mirror horizontally and vertically.

    Raises:
        ValueError: If an invalid direction is provided.
    """
    valid_directions = {'H', 'V', 'HV'}

    # Check if all provided directions are valid
    if any(direction not in valid_directions for direction in Mdirections):
        raise ValueError("Invalid direction provided. Valid directions are 'H', 'V', and 'HV'.")

    # Tile along the first axis (rows)
    amount_rows = len(Mdirections)
    tiled_mirrored_array = np.tile(np_input, (1, amount_rows, 1))
    initial_tiled_array = np.copy(tiled_mirrored_array)

    # Add mirrored versions based on specified directions V H or HV
    for direction in Mdirections:
        if direction == 'H':
            mirrored_row_h = np.flip(initial_tiled_array, axis=1) # Flip the entire array horizontally
            tiled_mirrored_array = np.concatenate((tiled_mirrored_array, mirrored_row_h), axis=0)
      
        elif direction == 'V':
            mirrored_column_v = np.flip(initial_tiled_array, axis=0)  # Flip the entire array vertically
            tiled_mirrored_array = np.concatenate((tiled_mirrored_array, mirrored_column_v), axis=0) 

        elif direction == 'HV':
            mirrored_row_hv = np.flip(np.flip(initial_tiled_array, axis=1), axis=0) # Flip the entire array horizontally and vertically
            tiled_mirrored_array = np.concatenate((tiled_mirrored_array, mirrored_row_hv), axis=0)
            
    plt.imshow(tiled_mirrored_array)
    plt.show()
    





def tilemirror_matrix(np_input, transform_array):
    """
    Tile and mirror the input matrix based on the provided transformation array.

    Parameters:
        np_input (numpy.ndarray): The input matrix to be tiled and mirrored.
        transform_array (numpy.ndarray): The transformation array specifying mirror operations.
            The values in the transformation array represent mirror operations as follows:
                2: Horizontal flip.
                3: Vertical flip.
                4: Horizontal and vertical flip.

    Returns:
        numpy.ndarray: The tiled and mirrored matrix based on the transformation array.

    Raises:
        ValueError: If an invalid value is found in the transformation array.

    Notes:
        The input matrix is tiled and mirrored according to the transformation array.
        Each value in the transformation array corresponds to a specific mirror operation.
        The resulting matrix is plotted using Matplotlib after the transformations are applied.
    """
    pixelw = len(np_input[0])
    pixelh = len(np_input[:, 0])
    hx = transform_array.shape[1]
    vx = transform_array.shape[0]
    np_image_tiled = np.tile(np_input, (vx, hx, 1))  # (columns, rows, depth)
   
    for i in range(transform_array.shape[0]):
        for j in range(transform_array.shape[1]):
            if transform_array[i, j] == 1:
                pass
            elif transform_array[i, j] == 2:
                startrow = i * pixelh
                endrow = ((i * pixelh) + pixelh + 1)
                startcolumn = ((j * pixelw))
                endcolumn = ((j * pixelw) + pixelw + 1)
                sliced_part = np_image_tiled[startrow:endrow, startcolumn:endcolumn]
                Hflipped = np.flip(sliced_part, axis=0)
                np_image_tiled[startrow:endrow, startcolumn:endcolumn] = Hflipped
            elif transform_array[i, j] == 3:
                startrow = i * pixelh
                endrow = ((i * pixelh) + pixelh + 1)
                startcolumn = ((j * pixelw))
                endcolumn = ((j * pixelw) + pixelw + 1)
                sliced_part = np_image_tiled[startrow:endrow, startcolumn:endcolumn]
                Vflipped = np.flip(sliced_part, axis=1)
                np_image_tiled[startrow:endrow, startcolumn:endcolumn] = Vflipped
            elif transform_array[i, j] == 4:
                startrow = i * pixelh
                endrow = ((i * pixelh) + pixelh + 1)
                startcolumn = ((j * pixelw))
                endcolumn = ((j * pixelw) + pixelw + 1)
                sliced_part = np_image_tiled[startrow:endrow, startcolumn:endcolumn]  
                HVflipped = np.flip(np.flip(sliced_part, axis=1), axis=0)
                np_image_tiled[startrow:endrow, startcolumn:endcolumn] = HVflipped
            else:
                raise ValueError("Invalid value found in transform_array. Only values 1(normal), 2(horizontal), 3(vertical), and 4(horizontal and vertical) are allowed.")
    
    plt.imshow(np_image_tiled)
    plt.show()



def enlargeImgBorder(np_input, amount):
    """
    Enlarge the border of the input image by adding extra padding around it.

    Parameters:
        np_input (numpy.ndarray): The input image array.
        amount (int): The amount of padding images to be added around the image borders.

    Output:
        Plot of the the image array with enlarged border.

    Raises:
        ValueError: If the amount parameter is not a positive integer.

    Notes:
        This function enlarges the border of the input image by adding extra padding around it.
        The amount parameter specifies the number of images to be added to each side of the image.
        The color of the border pixels is fixed and based on the image's RGB channels. left border will be red, the right border is blue and the top and bottom border will be green.
    """
    # Validate the amount parameter
    if not isinstance(amount, int) or amount <= 0:
        raise ValueError("The 'amount' parameter must be a positive integer.")

    # Separate the input image into its RGB channels
    red_img = np_input.copy()
    red_img[:, :, [1, 2]] = 0
    green_img = np_input.copy()
    green_img[:, :, [0, 2]] = 0
    blue_img = np_input.copy()
    blue_img[:, :, [0, 1]] = 0

    # Enlarge along axis 1 (rows)
    enlargedW = np.repeat(np_input, repeats=amount, axis=1)
    # Enlarge along axis 2 (columns)
    enlargedWH = np.repeat(enlargedW, repeats=amount, axis=0)

    # Add vertical padding with red and blue channels
    redcolumns = add_vert(red_img, amount)
    bluecolumns = add_vert(blue_img, amount)

    # Add horizontal padding with green channel
    greenrows = add_hor(green_img, amount + 2)

    # Concatenate the padded images to form the final surrounded image
    surroundImg = np.concatenate((redcolumns, enlargedWH, bluecolumns), axis=1)
    surroundImg = np.concatenate((greenrows, surroundImg, greenrows), axis=0)

    # Display the surrounded image
    plt.imshow(surroundImg)
    plt.show()    
  
def word(text, color="RANDOM"):
    """
    Generate an image representing the given text using letters from an alphabet image.

    Parameters:
        text (str): The text to be represented in the image. Must contain only lowercase letters.
        color (str, optional): The color scheme for the text. Options are 'R' (red), 'G' (green), 'B' (blue), or 'RANDOM'.
            Defaults to 'RANDOM'.

    Output:
        Plot of the image array representing the input text.

    Raises:
        ValueError: If the text contains numbers or capital letters.
        ValueError: If an invalid color is specified.

    Notes:
        This function generates an image representing the given text using letters from an alphabet image.
        Each letter in the text is extracted from the alphabet image and colored according to the specified color scheme.
        The resulting image is displayed using Matplotlib.
    """
    # Validate the input text
    if any(char.isdigit() or char.isupper() for char in text):
        raise ValueError("The text must contain only lowercase letters.")

    # Validate the color parameter
    valid_colors = {"R", "G", "B", "RANDOM"}
    if color not in valid_colors:
        raise ValueError("Invalid color specified. Valid options are 'R', 'G', 'B', or 'RANDOM'.")

    # Load the alphabet image   
    image_path_alfabet = os.path.join( 'data', 'alfabet.jpg')  # Replace with the actual path to your image file
    image_alfabet = Image.open(image_path_alfabet)
    np_image_alfabet = np.array(image_alfabet)
    word_img= np.zeros((100, len(text)*100, 3), dtype=int)

  
    alfabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    i=0
    for char in text:
        index = alfabet.index(char)
        startcolumn = ((index*100))
        endcolumn = ((index*100)+100)
        # needed copy otherwise double chars would be black
        copy_for_slice = np.copy(np_image_alfabet)  
        sliced_part = copy_for_slice[0:100,startcolumn:endcolumn]
        

        if color == "RANDOM":
            Rcolor = np.random.choice(["R", "G", "B"])
            
            if Rcolor == "R":
                sliced_part[:,:,[1,2]] = 0

            elif Rcolor == "G":
                sliced_part[:,:,[0,2]] = 0

            elif Rcolor == "B":
                sliced_part[:,:,[0,1]] = 0
            

        elif color == "R":
            sliced_part[:,:,[1,2]] = 0

        elif color == "G":
            sliced_part[:,:,[0,2]] = 0

        elif color == "B":
            sliced_part[:,:,[0,1]] = 0
        word_img[0:100,(i*100):((i*100)+(100))] = sliced_part 
        

  
        i+=1


    plt.imshow(word_img)
    plt.show()

def add_border(np_input,L,R,B,T,color):
    """
    Add borders of specified size and grey value to the input image.

    Parameters:
        np_input (numpy.ndarray): The input image array.
        L (int): The width of the left border.
        R (int): The width of the right border.
        B (int): The height of the bottom border.
        T (int): The height of the top border.
        color (Int): The greyscale color value for the borders. Each value should be between 0 and 255.

    Output:
        Plot the image array with added borders.

    Raises:
        ValueError: If L, R, B, or T are not integers or are negative.
        ValueError: If the color value is not between 0 and 255.

    Notes:
        This function adds borders of specified size and color to the input image.
        The color parameter should be a an integer containing a value between 0 and 255.
        The resulting image is displayed using Matplotlib.
    """
    # Validate L, R, B, and T parameters
    if not all(isinstance(val, int) and val >= 0 for val in (L, R, B, T)):
        raise ValueError("Border sizes (L, R, B, T) must be non-negative integers.")
    
    # Validate color parameter
    if not isinstance(color, int) or not 0 <= color <= 255:
        raise ValueError("Color must be an integer between 0 and 255 representing grayscale value.")

    pixelw=len(np_input[0])
    pixelh=len(np_input[:,0])
    
    borderB= np.zeros((B, pixelh+L+R, 3), dtype=int)
    borderT= np.zeros((T, pixelh+L+R, 3), dtype=int)
    borderL= np.zeros((pixelw, L, 3), dtype=int)
    borderR= np.zeros((pixelw, R, 3), dtype=int)

    borderB[:, :, :]=color
    borderT[:, :, :]=color
    borderL[:, :, :]=color
    borderR[:, :, :]=color

    surroundImg = np.concatenate((borderL,np_input,borderR),axis=1)
    surroundImg = np.concatenate((borderT,surroundImg,borderB),axis=0)

    plt.imshow(surroundImg)
    plt.show()



