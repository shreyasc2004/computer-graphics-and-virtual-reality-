import glfw
from OpenGL.GL import *
from math import sin, cos, pi


def sphere_vertex(latitude, longitude):
    # Unit sphere: position is also the surface normal.
    x = cos(latitude) * cos(longitude)
    y = sin(latitude)
    z = cos(latitude) * sin(longitude)

    # Light direction L = (0.6, 0, 0.8)
    # Viewer direction V = (0, 0, 1)
    normal_dot_light = 0.6 * x + 0.8 * z

    diffuse = max(0.0, normal_dot_light)

    # Reflection R = 2(N.L)N - L; therefore R.V = Rz
    specular = 0.0
    if normal_dot_light > 0:
        reflection_z = 2 * normal_dot_light * z - 0.8
        specular = max(0.0, reflection_z) ** 32

    # Final color = ambient + diffuse + specular
    glColor3f(
        min(1.0, 0.10 + 0.80 * diffuse + 0.70 * specular),
        min(1.0, 0.04 + 0.30 * diffuse + 0.70 * specular),
        min(1.0, 0.02 + 0.10 * diffuse + 0.70 * specular)
    )
    glVertex3f(x, y, z)


if not glfw.init():
    raise RuntimeError("GLFW initialization failed")

glfw.window_hint(glfw.DEPTH_BITS, 24)
window = glfw.create_window(600, 600, "Phong Illumination", None, None)

if not window:
    glfw.terminate()
    raise RuntimeError("Window creation failed")

glfw.make_context_current(window)
glfw.swap_interval(1)

glEnable(GL_DEPTH_TEST)
glClearColor(0.05, 0.05, 0.05, 1)

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(-1.4, 1.4, -1.4, 1.4, -2, 2)
glMatrixMode(GL_MODELVIEW)

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Draw the sphere as strips.
    for i in range(40):
        latitude = -pi / 2 + i * pi / 40
        next_latitude = latitude + pi / 40

        glBegin(GL_TRIANGLE_STRIP)
        for j in range(81):
            longitude = j * 2 * pi / 80
            sphere_vertex(latitude, longitude)
            sphere_vertex(next_latitude, longitude)
        glEnd()

    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()