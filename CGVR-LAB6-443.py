import glfw
from OpenGL.GL import *

if not glfw.init():
    raise RuntimeError("GLFW initialization failed")

glfw.window_hint(glfw.DEPTH_BITS, 24)
window = glfw.create_window(600, 600, "Z-Buffer Algorithm", None, None)

if not window:
    glfw.terminate()
    raise RuntimeError("Window creation failed")

glfw.make_context_current(window)

glEnable(GL_DEPTH_TEST)  # Enable Z-buffer
glClearColor(0, 0, 0, 1)

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(-1, 1, -1, 1, -1, 1)
glMatrixMode(GL_MODELVIEW)

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glBegin(GL_TRIANGLES)

    # Red triangle: closer to the viewer
    glColor3f(1, 0, 0)
    glVertex3f(-0.7, -0.6, 0.5)
    glVertex3f(0.5, -0.6, 0.5)
    glVertex3f(-0.1, 0.7, 0.5)

    # Green triangle: farther from the viewer
    glColor3f(0, 1, 0)
    glVertex3f(-0.4, -0.4, -0.5)
    glVertex3f(0.8, -0.4, -0.5)
    glVertex3f(0.4, 0.8, -0.5)

    glEnd()

    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()