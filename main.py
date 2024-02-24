from PIL import Image

# Loading ascii-pineapple.jpg into object
im = Image.open("ascii-pineapple.jpg")
im = im.resize((400, 400), 4)
brightnesses_str = list("`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$")
brightnesses_dict = {}
num = 0
for key in brightnesses_str:
    brightnesses_dict[key] = num
    num += 4
brightnesses_dict['$'] = 255

def brightnesses_to_ascii(pixl_brigh, bright_dict, img_obj):
    ascii_matrix = [[0 for i in range(im.width)] for y in range(im.height)]
    for i in range(img_obj.height):
        for j in range(img_obj.width):
            actual_bright = pixl_brigh[i][j]
            for key, value in bright_dict.items():
                if value >= actual_bright:
                    ascii_matrix[i][j] = key * 3
                    break
            
    return ascii_matrix

if im:
    print("Successfully loaded image!")
    print(f"Image size: {im.height} x {im.width}")
    img_data = list(im.getdata())
    pixel_matrix = [[img_data[i + j * im.width] for i in range(im.width)] for j in range(im.height)]
    pixel_brightnesses = [[int(sum(pixel_matrix[j][i]) / 3) for i in range(im.width)] for j in range(im.height)]
    ascii_art = brightnesses_to_ascii(pixel_brightnesses, brightnesses_dict, im)
    for row in ascii_art:
        print(''.join(row))
