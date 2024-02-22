from PIL import Image
import numpy as np

# Loading ascii-pineapple.jpg into object
im = Image.open("ascii-pineapple.jpg")
if im:
    print("Successfully loaded image!")
    print(f"Image size: {im.height} x {im.width}")
    img_data = list(im.getdata())
    pixel_matrix = [[img_data[i + j * im.width] for i in range(im.width)] for j in range(im.height)]
    print(pixel_matrix[100])
