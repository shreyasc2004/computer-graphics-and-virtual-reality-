from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

WIDTH = 500
HEIGHT = 500

def plot_circle_points(xc, yc, x, y):
    glVertex2i(xc + x, yc + y)
    glVertex2i(xc - x, yc + y)
    glVertex2i(xc + x, yc - y)
    glVertex2i(xc - x, yc - y)

    glVertex2i(xc + y, yc + x)
    glVertex2i(xc - y, yc + x)
    glVertex2i(xc + y, yc - x)
    glVertex2i(xc - y, yc - x)


def bresenham_circle(xc, yc, r):
    x = 0
    y = r

    d = 3 - 2 * r

    glBegin(GL_POINTS)

    while x <= y:
        plot_circle_points(xc, yc, x, y)

        if d < 0:
            d = d + 4 * x + 6
        else:
            d = d + 4 * (x - y) + 10
            y -= 1

        x += 1

    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1, 1, 1)

    # Draw a circle of radius 120
    bresenham_circle(250, 250, 120)

    glFlush()


def init():
    glClearColor(0, 0, 0, 1)
    glPointSize(2)

    gluOrtho2D(0, WIDTH, 0, HEIGHT)


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(WIDTH, HEIGHT)
glutCreateWindow(b"Bresenham Circle")

init()

glutDisplayFunc(display)

glutMainLoop()