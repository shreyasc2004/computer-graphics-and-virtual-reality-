import glfw
from OpenGL.GL import *
from OpenGL.GLU import *


# ============================================================
# COHEN-SUTHERLAND REGION CODES
# ============================================================

INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8


# ============================================================
# CLIPPING WINDOW
# ============================================================

X_MIN = -200
X_MAX = 200
Y_MIN = -120
Y_MAX = 120


# ============================================================
# ORIGINAL LINE
# ============================================================

P1 = (-350, -250)
P2 = (320, 220)


# ============================================================
# COMPUTE REGION CODE
# ============================================================

def compute_code(x, y):

    code = INSIDE

    if x < X_MIN:
        code |= LEFT

    elif x > X_MAX:
        code |= RIGHT

    if y < Y_MIN:
        code |= BOTTOM

    elif y > Y_MAX:
        code |= TOP

    return code


# ============================================================
# CONVERT CODE TO BINARY STRING
# ============================================================

def code_binary(code):
    return format(code, "04b")


# ============================================================
# COHEN-SUTHERLAND LINE CLIPPING
# ============================================================

def cohen_sutherland_clip(x1, y1, x2, y2):

    code1 = compute_code(x1, y1)
    code2 = compute_code(x2, y2)

    original_code1 = code1
    original_code2 = code2

    while True:

        # ----------------------------------------------------
        # CASE 1: Both points are inside
        # ----------------------------------------------------

        if code1 == 0 and code2 == 0:

            return (
                True,
                (x1, y1),
                (x2, y2),
                original_code1,
                original_code2
            )

        # ----------------------------------------------------
        # CASE 2: Both points are outside on same side
        # ----------------------------------------------------

        elif (code1 & code2) != 0:

            return (
                False,
                None,
                None,
                original_code1,
                original_code2
            )

        # ----------------------------------------------------
        # CASE 3: Line crosses clipping boundary
        # ----------------------------------------------------

        else:

            # Select a point outside
            if code1 != 0:
                outside_code = code1
            else:
                outside_code = code2

            # ------------------------------------------------
            # TOP
            # ------------------------------------------------

            if outside_code & TOP:

                if y2 == y1:
                    return False, None, None, original_code1, original_code2

                x = x1 + (x2 - x1) * (Y_MAX - y1) / (y2 - y1)
                y = Y_MAX

            # ------------------------------------------------
            # BOTTOM
            # ------------------------------------------------

            elif outside_code & BOTTOM:

                if y2 == y1:
                    return False, None, None, original_code1, original_code2

                x = x1 + (x2 - x1) * (Y_MIN - y1) / (y2 - y1)
                y = Y_MIN

            # ------------------------------------------------
            # RIGHT
            # ------------------------------------------------

            elif outside_code & RIGHT:

                if x2 == x1:
                    return False, None, None, original_code1, original_code2

                y = y1 + (y2 - y1) * (X_MAX - x1) / (x2 - x1)
                x = X_MAX

            # ------------------------------------------------
            # LEFT
            # ------------------------------------------------

            else:

                if x2 == x1:
                    return False, None, None, original_code1, original_code2

                y = y1 + (y2 - y1) * (X_MIN - x1) / (x2 - x1)
                x = X_MIN

            # Replace the outside point
            if outside_code == code1:

                x1 = x
                y1 = y
                code1 = compute_code(x1, y1)

            else:

                x2 = x
                y2 = y
                code2 = compute_code(x2, y2)


# ============================================================
# PRINT RESULTS
# ============================================================

accepted, clipped_p1, clipped_p2, code1, code2 = \
    cohen_sutherland_clip(
        P1[0],
        P1[1],
        P2[0],
        P2[1]
    )


print("\n==============================================")
print("     COHEN-SUTHERLAND LINE CLIPPING")
print("==============================================")

print("\nClipping Window:")
print(f"Xmin = {X_MIN}")
print(f"Xmax = {X_MAX}")
print(f"Ymin = {Y_MIN}")
print(f"Ymax = {Y_MAX}")

print("\nOriginal Line:")
print(f"P1 = {P1}")
print(f"P2 = {P2}")

print("\nRegion Codes:")

print(
    f"P1 {P1} -> {code_binary(code1)}"
)

print(
    f"P2 {P2} -> {code_binary(code2)}"
)


if accepted:

    print("\nResult: LINE ACCEPTED AFTER CLIPPING")

    print(
        f"\nClipped P1 = "
        f"({clipped_p1[0]:.2f}, {clipped_p1[1]:.2f})"
    )

    print(
        f"Clipped P2 = "
        f"({clipped_p2[0]:.2f}, {clipped_p2[1]:.2f})"
    )

else:

    print("\nResult: LINE REJECTED")

print("\n==============================================\n")


# ============================================================
# DRAW POINT
# ============================================================

def draw_point(x, y, size=8):

    glPointSize(size)

    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


# ============================================================
# DRAW LINE
# ============================================================

def draw_line(x1, y1, x2, y2):

    glBegin(GL_LINES)

    glVertex2f(x1, y1)
    glVertex2f(x2, y2)

    glEnd()


# ============================================================
# DRAW CLIPPING WINDOW
# ============================================================

def draw_clipping_window():

    glLineWidth(3)

    glBegin(GL_LINE_LOOP)

    glVertex2f(X_MIN, Y_MIN)
    glVertex2f(X_MAX, Y_MIN)
    glVertex2f(X_MAX, Y_MAX)
    glVertex2f(X_MIN, Y_MAX)

    glEnd()


# ============================================================
# DRAW AXES
# ============================================================

def draw_axes():

    glLineWidth(1)

    glBegin(GL_LINES)

    # X axis
    glVertex2f(-500, 0)
    glVertex2f(500, 0)

    # Y axis
    glVertex2f(0, -350)
    glVertex2f(0, 350)

    glEnd()


# ============================================================
# INITIALIZE OPENGL
# ============================================================

def initialize_opengl():

    glClearColor(0.05, 0.05, 0.05, 1.0)

    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()

    glOrtho(
        -500,
        500,
        -350,
        350,
        -1,
        1
    )

    glMatrixMode(GL_MODELVIEW)

    glLoadIdentity()


# ============================================================
# MAIN
# ============================================================

def main():

    if not glfw.init():

        raise Exception("GLFW initialization failed")

    window = glfw.create_window(
        1200,
        800,
        "Experiment 5 - Cohen-Sutherland Line Clipping",
        None,
        None
    )

    if not window:

        glfw.terminate()

        raise Exception("Could not create GLFW window")

    glfw.make_context_current(window)

    initialize_opengl()

    while not glfw.window_should_close(window):

        glClear(GL_COLOR_BUFFER_BIT)

        glLoadIdentity()

        # ----------------------------------------------------
        # Draw coordinate axes
        # ----------------------------------------------------

        glColor3f(0.25, 0.25, 0.25)

        draw_axes()

        # ----------------------------------------------------
        # Draw clipping window
        # ----------------------------------------------------

        glColor3f(1.0, 1.0, 1.0)

        draw_clipping_window()

        # ----------------------------------------------------
        # Draw original line
        # ----------------------------------------------------

        glColor3f(1.0, 0.2, 0.2)

        glLineWidth(2)

        draw_line(
            P1[0],
            P1[1],
            P2[0],
            P2[1]
        )

        # ----------------------------------------------------
        # Draw original endpoints
        # ----------------------------------------------------

        glColor3f(1.0, 0.0, 0.0)

        draw_point(
            P1[0],
            P1[1],
            10
        )

        draw_point(
            P2[0],
            P2[1],
            10
        )

        # ----------------------------------------------------
        # Draw clipped portion
        # ----------------------------------------------------

        if accepted:

            glColor3f(0.0, 1.0, 0.0)

            glLineWidth(6)

            draw_line(
                clipped_p1[0],
                clipped_p1[1],
                clipped_p2[0],
                clipped_p2[1]
            )

            # ------------------------------------------------
            # Draw clipped endpoints
            # ------------------------------------------------

            glColor3f(0.0, 1.0, 0.0)

            draw_point(
                clipped_p1[0],
                clipped_p1[1],
                12
            )

            draw_point(
                clipped_p2[0],
                clipped_p2[1],
                12
            )

        # ----------------------------------------------------
        # Swap buffers
        # ----------------------------------------------------

        glfw.swap_buffers(window)

        glfw.poll_events()

    glfw.terminate()


# ============================================================
# RUN PROGRAM
# ============================================================

if __name__ == "__main__":
    main()