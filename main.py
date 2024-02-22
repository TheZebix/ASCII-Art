from PIL import Image
import numpy as np

# Loading ascii-pineapple.jpg into object
im = Image.open("ascii-pineapple.jpg")
if im:
    print("Successfully loaded image!")
    print(f"Image size: {im.height} x {im.width}")
    img_data = list(im.getdata())
    pixel_matrix = [[]]
    #print(np.matrix(pixel_matrix))
    #print(img_data)
    
    for column in range(im.height):
        for row in range(im.width):
            pixel_matrix[column][row] = 
            print(column, row)
