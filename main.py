import cv2

import os
import csv

ALLOWED_IMAGE_FORMATS = ["jpg", "jpeg", "png"]
DISPLAY_ALPHA_CHANNEL = True
USE_GRAYSCALE = True


if not os.path.exists("./datasets"):
    print(
        "Dataset folder not found\nCreate a 'datasets' folder and put the image in that folder."
    )

print('-' * 25)
print("Settings")
print(f"Use Grayscale: {USE_GRAYSCALE}")
if not USE_GRAYSCALE:
    print(f"Display Alpha Channel: {DISPLAY_ALPHA_CHANNEL}")
print('-' * 10)

for file in os.listdir("./datasets"):
    if not file.split(".")[-1].lower() in ALLOWED_IMAGE_FORMATS:
        continue
    result = []
    image = cv2.imread(f"./datasets/{file}", cv2.COLOR_BAYER_BG2RGBA)
    if USE_GRAYSCALE:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        width, height = image.shape
        print(f'file : {file}')
        print(f'width : {width}')
        print(f'height : {height}')
        print(f'pixels : {width * height}')
        for x in range(width):
            result.append([])
            for y in range(height):
                result[-1].append(image[x, y])
    else:
        width, height, channels = image.shape
        print(f'file : {file}')
        print(f'width : {width}')
        print(f'height : {height}')
        print(f'channels : {channels}')
        print(f'pixels : {width * height}')
        for x in range(width):
            result.append([])
            for y in range(height):
                r, g, b, a = image[x, y]
                result[-1].append(
                    [r, g, b, a] if DISPLAY_ALPHA_CHANNEL else [r, g, b]
                )
    if not os.path.exists("./outputs"):
        os.makedirs("./outputs")
    with open(f"./outputs/{file}.csv", "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(result)
    if os.listdir('./datasets').index(file) != len(os.listdir('./datasets')) - 1:
        print('-' * 10)
            
print('-' * 25)
