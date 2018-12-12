import sys
from PIL import Image
from random import randint

def gb_to_red(img):
    pixels = img.load()
    for i in range(img.size[0]):    # for every pixel:
        for j in range(img.size[1]):
            r, g, b = img.getpixel((i, j))
            if r < g:
                r, g = g, r
            """
            elif r < b:
            r, b = b, r
            """
            pixels[i, j] = (int(r), int(g), int(b))

def reduce_green(img):
    pixels = img.load()
    for i in range(img.size[0]):    # for every pixel:
        for j in range(img.size[1]):
            r, g, b = img.getpixel((i, j))
            if g > max(r, b):
                g = max(r, b)
            pixels[i, j] = (int(r), int(g), int(b))

def distort(img):
    pixels = img.load()
    offset = .001
    print(offset)
    org = 50
    for i in range(img.size[0]):    # for every pixel:
        for j in range(img.size[1]):
            if (i < 100) and (i > 50):
                r, g, b = img.getpixel((i, j))
                if (j+1/offset) >= img.size[1]:
                    r1, g1, b1 = img.getpixel((org, img.size[1]-1))
                elif (j+1/offset) < 0:
                    r1, g1, b1 = img.getpixel((org, 0))
                else:
                    r1, g1, b1 = img.getpixel((org, j+1/offset))
                r = r + r1
                b = b + b1
                g = g + g1
                r /= 2
                g /= 2
                b /= 2
                pixels[i, j] = (int(r), int(g), int(b))

        if (i < 100) and (i > 50):
                offset += .002
    print(offset)

def sepia(img):
    pixels = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = img.getpixel((i, j))
            c = (r + g + b)/3
            r = c + 112
            g = c + 66
            b = c + 20
            pixels[i, j] = (int(r), int(g), int(b))


def blur(img):
    pixels = img.load()
    for i in range(img.size[0]-1):
        for j in range(img.size[1]-1):
            if (i is not 0):
                if (j is not 0):
                    r, g, b = img.getpixel((i, j))
                    nr1, ng1, nb1 = img.getpixel((i+1, j+1))
                    nr2, ng2, nb2 = img.getpixel((i-1, j+1))
                    nr3, ng3, nb3 = img.getpixel((i+1, j-1))
                    nr4, ng4, nb4 = img.getpixel((i-1, j-1))
                    r += nr1 + nr2 + nr3 + nr4
                    g += ng1 + ng2 + ng3 + ng4
                    b += nb1 + nb2 + nb3 + nb4
                    r/=5
                    g/=5
                    b/=5
                    pixels[i, j] = (int(r), int(g), int(b))

def fill(img, c):
    pixels = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixels[i, j] = c

def select(img, x, y):
    pixels = img.load()
    ir, ig, ib = img.getpixel((x, y))
    threshold = 60
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = img.getpixel((i, j))
            if r in range(ir - threshold, ir + threshold):
                if g in range(ig - threshold, ig + threshold):
                    if b in range(ib - threshold, ib + threshold):
                        r = g = b = 0
            pixels[i, j] = (int(r), int(g), int(b))

def median_filter(img):
    pixels = img.load()
    px2 = [[0 for x in range(img.size[0])] for y in range(img.size[1])]

    for i in range(img.size[0]-1):
        for j in range(img.size[1]-1):
            if (i is not 0):
                if (j is not 0):
                    sum = [0, 0, 0]
                    add_colour(pixels, i, j, sum)
                    sum[0] /= 9
                    sum[1] /= 9
                    sum[2] /= 9
                    px2[i][j] = (sum[0], sum[1], sum[2])

    pixels = px2

def add_colour(pixels, x, y, sum):
    sum = img.getpixel((x-1, y-1))
    sum += img.getpixel((x, y-1))
    sum += img.getpixel((x+1, y-1))
    sum += img.getpixel((x-1, y))
    sum += img.getpixel((x, y))
    sum += img.getpixel((x+1, y))
    sum += img.getpixel((x-1, y+1))
    sum += img.getpixel((x, y+1))
    sum += img.getpixel((x+1, y+1))

img = Image.open(sys.argv[1])
#select(img, 50, 100)
sepia(img)
img.show()


















