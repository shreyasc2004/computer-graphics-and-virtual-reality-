from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Window size
WIDTH = 500
HEIGHT = 500

def plot(x, y):
    glVertex2i(x, y)

def bresenham(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    x = x1
    y = y1

    glBegin(GL_POINTS)

    if dx > dy:
        p = 2 * dy - dx

        while x != x2:
            plot(x, y)

            if p < 0:
                p += 2 * dy
            else:
                y += sy
                p += 2 * (dy - dx)

            x += sx

    else:
        p = 2 * dx - dy

        while y != y2:
            plot(x, y)

            if p < 0:
                p += 2 * dx
            else:
                x += sx
                p += 2 * (dx - dy)

            y += sy

    plot(x2, y2)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1, 1, 1)

    # Draw line
    bresenham(50, 50, 450, 350)

    glFlush()

def init():
    glClearColor(0, 0, 0, 1)
    glColor3f(1, 1, 1)

    glPointSize(3)

    gluOrtho2D(0, WIDTH, 0, HEIGHT)

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(WIDTH, HEIGHT)
glutCreateWindow(b"Bresenham Line Drawing")

init()

glutDisplayFunc(display)

glutMainLoop()