from PIL import Image
import numpy as np

# Loading ascii-pineapple.jpg into object
im = Image.open("ascii-pineapple.jpg")
if im:
    print("Successfully loaded image!")
    print(f"Image size: {im.height} x {im.width}")
    img_data = list(im.getdata())
    pixel_matrix = [[0 for x in range(im.width)] for y in range(im.height)]
    print(np.matrix(pixel_matrix))
    for y in range(im.height)
