import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
from ctypes import c_float, sizeof

vertex_shader = """
#version 330 core

layout(location = 0) in vec2 position;

void main()
{
    gl_Position = vec4(position, 0.0, 1.0);
}
"""

fragment_shader = """
#version 330 core

out vec4 color;

void main()
{
    color = vec4(1.0, 0.5, 0.1, 1.0);
}
"""

if not glfw.init():
    raise RuntimeError("GLFW initialization failed")

glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

window = glfw.create_window(600, 600, "Vertex and Fragment Shaders", None, None)

if not window:
    glfw.terminate()
    raise RuntimeError("Window creation failed")

glfw.make_context_current(window)
glfw.swap_interval(1)

# Compile and link the shaders.
program = compileProgram(
    compileShader(vertex_shader, GL_VERTEX_SHADER),
    compileShader(fragment_shader, GL_FRAGMENT_SHADER)
)

# Three vertices, each containing x and y coordinates.
vertices = (c_float * 6)(
    -0.6, -0.5,
     0.6, -0.5,
     0.0,  0.6
)

# Create a vertex array and vertex buffer.
vao = glGenVertexArrays(1)
glBindVertexArray(vao)

vbo = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, vbo)
glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW)

glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 0, None)
glEnableVertexAttribArray(0)

glClearColor(0.1, 0.1, 0.1, 1.0)

while not glfw.window_should_close(window):
    glfw.poll_events()

    width, height = glfw.get_framebuffer_size(window)
    glViewport(0, 0, width, height)
    glClear(GL_COLOR_BUFFER_BIT)

    glUseProgram(program)
    glBindVertexArray(vao)
    glDrawArrays(GL_TRIANGLES, 0, 3)

    glfw.swap_buffers(window)

glDeleteBuffers(1, [vbo])
glDeleteVertexArrays(1, [vao])
glDeleteProgram(program)
glfw.terminate()