import base
from line import line

def addPoint(m, x, y, z):
    m.append([x,y,z,1.])

def addEdge(m, x0, y0, z0, x1, y1, z1):
    addPoint(m, x0, y0, z0)
    addPoint(m, x1, y1, z1)

def drawLines(m, image):  # draws the lines to an image
    for i in range(0, len(m) - 1, 2):
        lin = line(m[i][0], m[i][1], m[i + 1][0], m[i + 1], 1)
