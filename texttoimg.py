from PIL import Image
import sys

def fill(x, mx, y, r, g, b, pixels): # x is start x, mx is end x for the block
    for i in range(x, mx):
        for j in range(0, y):
            pixels[i, j] = (r, g, b)

str = sys.argv[1]
blocksize = 50

temp = []
colours = []

for c in str: # for each letter
    temp.append(ord(c)) # add the unicode for the char to temporary array
    if (len(temp) == 3): # every 3 characters
        colours.append(temp) # store the colour
        temp = []

img = Image.new('RGB', (len(colours)*blocksize, blocksize)) # create an image based on number of colours
pixels = img.load()

for i in range(0, len(colours)):
    for j in range(0, blocksize):
        fill(i * blocksize, (i * blocksize) + blocksize, blocksize, colours[i][0], colours[i][1], colours[i][2], pixels)

#print(colours)
img.format = "PNG"
img.show()