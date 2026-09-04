import glfw
from OpenGL.GL import *
import numpy as np
import ctypes
import math


# ============================================================
# EXPERIMENT 8
# BASIC OPENGL PROGRAM USING
# VERTEX AND FRAGMENT SHADERS
# ============================================================


# ============================================================
# VERTEX SHADER
# ============================================================

vertex_shader_source = """
#version 330 core

layout (location = 0) in vec3 aPos;
layout (location = 1) in vec3 aColor;

out vec3 vertexColor;

uniform float angle;

void main()
{
    float c = cos(angle);
    float s = sin(angle);

    mat2 rotation = mat2(
        c, -s,
        s,  c
    );

    vec2 rotatedPosition = rotation * aPos.xy;

    gl_Position = vec4(
        rotatedPosition,
        aPos.z,
        1.0
    );

    vertexColor = aColor;
}
"""


# ============================================================
# FRAGMENT SHADER
# ============================================================

fragment_shader_source = """
#version 330 core

in vec3 vertexColor;

out vec4 FragColor;

uniform float time;

void main()
{
    float pulse = 0.5 + 0.5 * sin(time * 2.0);

    vec3 color = vertexColor * (0.65 + 0.35 * pulse);

    FragColor = vec4(color, 1.0);
}
"""


# ============================================================
# COMPILE SHADER
# ============================================================

def compile_shader(source, shader_type):

    shader = glCreateShader(shader_type)

    glShaderSource(
        shader,
        source
    )

    glCompileShader(shader)

    success = glGetShaderiv(
        shader,
        GL_COMPILE_STATUS
    )

    if not success:

        error = glGetShaderInfoLog(
            shader
        ).decode()

        raise RuntimeError(
            "Shader compilation failed:\n"
            + error
        )

    return shader


# ============================================================
# CREATE SHADER PROGRAM
# ============================================================

def create_shader_program():

    vertex_shader = compile_shader(
        vertex_shader_source,
        GL_VERTEX_SHADER
    )

    fragment_shader = compile_shader(
        fragment_shader_source,
        GL_FRAGMENT_SHADER
    )

    program = glCreateProgram()

    glAttachShader(
        program,
        vertex_shader
    )

    glAttachShader(
        program,
        fragment_shader
    )

    glLinkProgram(
        program
    )

    success = glGetProgramiv(
        program,
        GL_LINK_STATUS
    )

    if not success:

        error = glGetProgramInfoLog(
            program
        ).decode()

        raise RuntimeError(
            "Shader linking failed:\n"
            + error
        )

    glDeleteShader(vertex_shader)
    glDeleteShader(fragment_shader)

    return program


# ============================================================
# INITIALIZE GLFW
# ============================================================

if not glfw.init():

    raise Exception(
        "GLFW initialization failed"
    )


# ============================================================
# OPENGL VERSION
# ============================================================

glfw.window_hint(
    glfw.CONTEXT_VERSION_MAJOR,
    3
)

glfw.window_hint(
    glfw.CONTEXT_VERSION_MINOR,
    3
)

glfw.window_hint(
    glfw.OPENGL_PROFILE,
    glfw.OPENGL_CORE_PROFILE
)


# ============================================================
# CREATE WINDOW
# ============================================================

window = glfw.create_window(
    1000,
    700,
    "Experiment 8 - Shader Graphics",
    None,
    None
)

if not window:

    glfw.terminate()

    raise Exception(
        "Could not create OpenGL window"
    )


glfw.make_context_current(
    window
)


# ============================================================
# VERTEX DATA
# ============================================================
#
# Each vertex:
#
# X, Y, Z,     R, G, B
#
# ============================================================

vertices = np.array(
    [
        # Position          Color

         0.0,  0.70, 0.0,    1.0, 0.2, 0.8,

        -0.70, -0.55, 0.0,   0.1, 0.8, 1.0,

         0.70, -0.55, 0.0,   0.2, 1.0, 0.4

    ],
    dtype=np.float32
)


# ============================================================
# CREATE VAO
# ============================================================

VAO = glGenVertexArrays(1)

glBindVertexArray(
    VAO
)


# ============================================================
# CREATE VBO
# ============================================================

VBO = glGenBuffers(1)

glBindBuffer(
    GL_ARRAY_BUFFER,
    VBO
)

glBufferData(
    GL_ARRAY_BUFFER,
    vertices.nbytes,
    vertices,
    GL_STATIC_DRAW
)


# ============================================================
# POSITION ATTRIBUTE
# ============================================================

glVertexAttribPointer(
    0,
    3,
    GL_FLOAT,
    GL_FALSE,
    6 * vertices.itemsize,
    ctypes.c_void_p(0)
)

glEnableVertexAttribArray(0)


# ============================================================
# COLOR ATTRIBUTE
# ============================================================

glVertexAttribPointer(
    1,
    3,
    GL_FLOAT,
    GL_FALSE,
    6 * vertices.itemsize,
    ctypes.c_void_p(
        3 * vertices.itemsize
    )
)

glEnableVertexAttribArray(1)


# ============================================================
# UNBIND
# ============================================================

glBindBuffer(
    GL_ARRAY_BUFFER,
    0
)

glBindVertexArray(
    0
)


# ============================================================
# CREATE SHADER PROGRAM
# ============================================================

shader_program = create_shader_program()


# ============================================================
# GET UNIFORM LOCATIONS
# ============================================================

angle_location = glGetUniformLocation(
    shader_program,
    "angle"
)

time_location = glGetUniformLocation(
    shader_program,
    "time"
)


# ============================================================
# TERMINAL INFORMATION
# ============================================================

print()
print("================================================")
print("                 EXPERIMENT 8")
print("       VERTEX + FRAGMENT SHADERS")
print("================================================")
print()
print("OpenGL Version : 3.3 Core")
print("Vertex Shader  : Compiled")
print("Fragment Shader: Compiled")
print("Shader Program : Linked")
print()
print("Features:")
print("  ✓ Vertex shader transformation")
print("  ✓ Fragment shader coloring")
print("  ✓ Per-vertex colors")
print("  ✓ Color interpolation")
print("  ✓ Animated rotation")
print("  ✓ Animated brightness")
print()
print("Triangle vertices:")
print("  P1 = ( 0.00,  0.70)")
print("  P2 = (-0.70, -0.55)")
print("  P3 = ( 0.70, -0.55)")
print()
print("================================================")
print()


# ============================================================
# RENDER LOOP
# ============================================================

while not glfw.window_should_close(window):

    current_time = glfw.get_time()


    # --------------------------------------------------------
    # CLEAR SCREEN
    # --------------------------------------------------------

    glClearColor(
        0.01,
        0.01,
        0.03,
        1.0
    )

    glClear(
        GL_COLOR_BUFFER_BIT
    )


    # --------------------------------------------------------
    # USE SHADER
    # --------------------------------------------------------

    glUseProgram(
        shader_program
    )


    # --------------------------------------------------------
    # ANIMATED ROTATION
    # --------------------------------------------------------

    angle = current_time * 0.8

    glUniform1f(
        angle_location,
        angle
    )


    # --------------------------------------------------------
    # SEND TIME TO FRAGMENT SHADER
    # --------------------------------------------------------

    glUniform1f(
        time_location,
        current_time
    )


    # --------------------------------------------------------
    # DRAW TRIANGLE
    # --------------------------------------------------------

    glBindVertexArray(
        VAO
    )

    glDrawArrays(
        GL_TRIANGLES,
        0,
        3
    )

    glBindVertexArray(
        0
    )


    # --------------------------------------------------------
    # DISPLAY
    # --------------------------------------------------------

    glfw.swap_buffers(
        window
    )

    glfw.poll_events()


# ============================================================
# CLEANUP
# ============================================================

glDeleteVertexArrays(
    1,
    [VAO]
)

glDeleteBuffers(
    1,
    [VBO]
)

glDeleteProgram(
    shader_program
)

glfw.terminate()