from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


# ==========================================
# DDA LINE DRAWING ALGORITHM
# ==========================================
def DDA(x1, y1, x2, y2):

    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))

    x_inc = dx / steps
    y_inc = dy / steps

    x = x1
    y = y1

    for i in range(steps + 1):

        glVertex2i(round(x), round(y))

        x += x_inc
        y += y_inc


# ==========================================
# BRESENHAM LINE DRAWING ALGORITHM
# ==========================================
def Bresenham(x1, y1, x2, y2):

    dx = x2 - x1
    dy = y2 - y1

    p = 2 * dy - dx

    x = x1
    y = y1

    while x <= x2:

        glVertex2i(x, y)

        x += 1

        if p < 0:
            p = p + 2 * dy

        else:
            y += 1
            p = p + 2 * dy - 2 * dx


# ==========================================
# DISPLAY
# ==========================================
def display():

    glClear(GL_COLOR_BUFFER_BIT)

    # -----------------------------
    # DDA LINE
    # -----------------------------
    glColor3f(0.0, 1.0, 0.0)       # Green

    glPointSize(3.0)

    glBegin(GL_POINTS)

    DDA(100, 150, 650, 350)

    glEnd()


    # -----------------------------
    # BRESENHAM LINE
    # -----------------------------
    glColor3f(1.0, 0.3, 0.0)       # Orange

    glPointSize(3.0)

    glBegin(GL_POINTS)

    Bresenham(100, 400, 650, 550)

    glEnd()


    glFlush()


# ==========================================
# INITIALIZATION
# ==========================================
def init():

    # Black background
    glClearColor(0.0, 0.0, 0.0, 1.0)

    # Projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluOrtho2D(0, 800, 0, 600)

    # Enable point smoothing
    glEnable(GL_POINT_SMOOTH)

    # Enable blending
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)


# ==========================================
# MAIN
# ==========================================
def main():

    glutInit()

    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    glutInitWindowSize(800, 600)

    glutInitWindowPosition(100, 100)

    glutCreateWindow(
        b"DDA and Bresenham Line Drawing"
    )

    init()

    glutDisplayFunc(display)

    glutMainLoop()


main()