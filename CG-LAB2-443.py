from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


# ==========================================
# PLOT 8 SYMMETRIC POINTS
# ==========================================
def plot_points(xc, yc, x, y):

    glVertex2i(xc + x, yc + y)
    glVertex2i(xc - x, yc + y)

    glVertex2i(xc + x, yc - y)
    glVertex2i(xc - x, yc - y)

    glVertex2i(xc + y, yc + x)
    glVertex2i(xc - y, yc + x)

    glVertex2i(xc + y, yc - x)
    glVertex2i(xc - y, yc - x)


# ==========================================
# MIDPOINT CIRCLE DRAWING ALGORITHM
# ==========================================
def midpoint_circle(xc, yc, r):

    x = 0
    y = r

    # Initial decision parameter
    p = 1 - r

    while x <= y:

        # Plot all 8 symmetric points
        plot_points(xc, yc, x, y)

        x += 1

        if p < 0:

            # Move to next x
            p = p + 2 * x + 1

        else:

            # Move diagonally
            y -= 1

            p = p + 2 * (x - y) + 1


# ==========================================
# DISPLAY FUNCTION
# ==========================================
def display():

    glClear(GL_COLOR_BUFFER_BIT)

    # Circle color
    glColor3f(0.0, 1.0, 0.0)

    # Point size
    glPointSize(3.0)

    glBegin(GL_POINTS)

    # Center = (400, 300)
    # Radius = 200
    midpoint_circle(400, 300, 200)

    glEnd()

    glFlush()


# ==========================================
# INITIALIZATION
# ==========================================
def init():

    # Black background
    glClearColor(0.0, 0.0, 0.0, 1.0)

    # 2D projection
    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()

    gluOrtho2D(0, 800, 0, 600)

    # Smooth points
    glEnable(GL_POINT_SMOOTH)

    # Blending
    glEnable(GL_BLEND)

    glBlendFunc(
        GL_SRC_ALPHA,
        GL_ONE_MINUS_SRC_ALPHA
    )


# ==========================================
# MAIN FUNCTION
# ==========================================
def main():

    glutInit()

    glutInitDisplayMode(
        GLUT_SINGLE | GLUT_RGB
    )

    glutInitWindowSize(800, 600)

    glutInitWindowPosition(100, 100)

    glutCreateWindow(
        b"Midpoint Circle Drawing Algorithm"
    )

    init()

    glutDisplayFunc(display)

    glutMainLoop()


# ==========================================
# RUN PROGRAM
# ==========================================
main()