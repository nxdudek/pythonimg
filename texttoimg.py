from PIL import Image

def fill(x, mx, y, (r, g, b), pixels):
    for i in range(x, mx):
        for j in range(0, y):
            pixels[i, j] = (r, g, b)

str = "this will be turned into a pattern of colours"
blocksize = 50

a = []
cl = []

for c in str:
    q = ord(c)
    a.append(q)
    if (len(a) == 3):
        cl.append(a)
        a = []

img = Image.new('RGB', (len(cl)*blocksize, blocksize))
pixels = img.load()

for i in range(0, len(cl)):
    for j in range(0, blocksize):
        fill(i * blocksize, (i * blocksize) + blocksize, blocksize, (cl[i][0], cl[i][1], cl[i][2]), pixels)

print cl
img.show()