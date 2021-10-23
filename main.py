from PIL import Image
import numpy as np
from copy import deepcopy
import time

def carveSeam(start, pixels):
    x = start
    lpixels = pixels.tolist()
    print(pixels[0][200])
    newPixels = []

    for row in lpixels:
        print(row[200])
        time.sleep(5)
        mid = row[x]
        left = row[x - 1]
        right = row[x + 1]

        lDiff = findDiff(mid, left)
        rDiff = findDiff(mid, right)

        if lDiff > rDiff:
            newRow = deepcopy(row)
            del newRow[x]
            x = x - 1
        if lDiff < rDiff:
            newRow = deepcopy(row)
            del newRow[x]
            x = x + 1
 
        newPixels += [newRow]

    pixArr = np.array(newPixels)
    return pixArr

def findDiff(p1, p2):
    diff = 0

    for value in range(len(p1)):
        diff += abs(p1[value] - p2[value])

    return diff

def main():
    image = Image.open('img/flowers.jpg')
    deeznuts = list(image)
    pix = np.asarray(image)
    print(deeznuts)

    for i in range(20):
        carvedPix = carveSeam(200, pix)

    image2 = Image.fromarray((carvedPix).astype(np.uint8))
    image2.show()

if __name__ == "__main__":
    main()