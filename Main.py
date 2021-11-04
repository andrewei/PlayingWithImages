from PIL import Image

path = "images/wisconsin_nature_outside_215558"
im = Image.open(path + ".jpg")  # Can be many different formats.
pix = im.load()
print(im.size)  # Get the width and hight of the image for iterating over
print(pix[1, 2])  # Get the RGBA Value of the a pixel of an image
print("X size, ", im.size[0])
print("Y size, ", im.size[1])


def sumArr(arr):
    res = 0
    for i in range(0, len(arr)):
        res = res + arr[i]
    return res // len(arr)


def calculateAverage(arr, x, y, grid):
    if x > 0 - grid and x + grid < im.size[0] - 1:
        if y > 0 - grid and y + grid < im.size[1] - 1:
            r_array = []
            g_array = []
            b_array = []
            for i in range(-grid, grid):
                for j in range(-grid, grid):
                    r_array.append(arr[x + i, y + j][0])
                    g_array.append(arr[x + i, y + j][1])
                    b_array.append(arr[x + i, y + j][2])
            arr[x, y] = (sumArr(r_array), sumArr(g_array), sumArr(b_array))
    return arr[x, y]


for x in range(im.size[0]):
    for y in range(im.size[1]):
        # print(pix[x, y])
        if x % 5 == 0 or y % 5 == 0:
            pix[x, y] = pix[x, y]
            pix[x, y] = calculateAverage(pix, x, y, 10)
            if x % 5 == 0 and y % 5 == 0:
                pix[x, y] = calculateAverage(pix, x, y, 2)
        else:
            pix[x, y] = calculateAverage(pix, x, y, 2)
            testX = (x * 130) // im.size[0]
            # print(testX)
            # pix[x, y] = (testX, 0, 0)   # Set the RGBA Value of the image (tuple)
im.save(path + "-2.jpg")  # Save the modified pixels as .png
