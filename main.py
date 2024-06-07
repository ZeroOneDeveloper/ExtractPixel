import cv2

import os
import csv

ALLOWED_IMAGE_FORMATS = ["jpg", "jpeg", "png"]
DISPLAY_ALPHA_CHANNEL = True

if not os.path.exists("./datasets"):
    print(
        "Dataset folder not found\nCreate a 'datasets' folder and put the image in that folder."
    )

for file in os.listdir("./datasets"):
    if not file.split(".")[-1].lower() in ALLOWED_IMAGE_FORMATS:
        continue
    image = cv2.imread(f"./datasets/{file}", cv2.IMREAD_UNCHANGED)
    width, height, channels = image.shape

    result = []
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
            
