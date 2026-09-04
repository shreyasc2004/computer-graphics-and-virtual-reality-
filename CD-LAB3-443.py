import glfw
from OpenGL.GL import *
from PIL import Image, ImageDraw, ImageFont
import math
import os


WIDTH = 1400
HEIGHT = 900


# ============================================================
# FONT
# ============================================================

def get_font(size=16):
    paths = [
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/calibri.ttf"
    ]

    for path in paths:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)

    return ImageFont.load_default()


FONT = get_font(16)
SMALL_FONT = get_font(14)
TITLE_FONT = get_font(22)


# ============================================================
# DRAW TEXT USING PIL + OPENGL
# ============================================================

def draw_text(text, x, y, color=(255, 255, 255), font=FONT):

    # Create transparent image
    image = Image.new("RGBA", (500, 100), (0, 0, 0, 0))

    draw = ImageDraw.Draw(image)

    draw.text(
        (5, 5),
        text,
        font=font,
        fill=(*color, 255)
    )

    # Crop to actual text size
    bbox = image.getbbox()

    if bbox is None:
        return

    image = image.crop(bbox)

    # PIL uses top-left origin.
    # OpenGL raster position uses bottom-left.
    image = image.transpose(Image.FLIP_TOP_BOTTOM)

    width, height = image.size

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glRasterPos2f(x, y)

    glDrawPixels(
        width,
        height,
        GL_RGBA,
        GL_UNSIGNED_BYTE,
        image.tobytes()
    )

    glDisable(GL_BLEND)


# ============================================================
# BASIC DRAWING
# ============================================================

def draw_line(x1, y1, x2, y2):

    glBegin(GL_LINES)

    glVertex2f(x1, y1)
    glVertex2f(x2, y2)

    glEnd()


def draw_point(x, y, size=7):

    glPointSize(size)

    glBegin(GL_POINTS)

    glVertex2f(x, y)

    glEnd()


def draw_triangle(points):

    glBegin(GL_LINE_LOOP)

    for x, y in points:
        glVertex2f(x, y)

    glEnd()


# ============================================================
# TRANSFORMATIONS
# ============================================================

def translation(points, tx, ty):

    return [
        (x + tx, y + ty)
        for x, y in points
    ]


def scaling(points, sx, sy):

    return [
        (x * sx, y * sy)
        for x, y in points
    ]


def rotation(points, angle):

    theta = math.radians(angle)

    cos_t = math.cos(theta)
    sin_t = math.sin(theta)

    result = []

    for x, y in points:

        new_x = x * cos_t - y * sin_t
        new_y = x * sin_t + y * cos_t

        result.append((new_x, new_y))

    return result


def reflection_x(points):

    return [
        (x, -y)
        for x, y in points
    ]


# ============================================================
# WORLD → SCREEN MAPPING
# ============================================================

def world_to_screen(
    x,
    y,
    panel_x,
    panel_y,
    panel_w,
    panel_h
):

    # World coordinates
    xmin = -100
    xmax = 350

    ymin = -200
    ymax = 300

    sx = panel_w / (xmax - xmin)
    sy = panel_h / (ymax - ymin)

    screen_x = panel_x + (x - xmin) * sx
    screen_y = panel_y + (y - ymin) * sy

    return screen_x, screen_y


# ============================================================
# DRAW AXES + TICKS
# ============================================================

def draw_axes(
    panel_x,
    panel_y,
    panel_w,
    panel_h
):

    xmin = -100
    xmax = 350

    ymin = -200
    ymax = 300

    # X axis
    x1, y1 = world_to_screen(
        xmin, 0,
        panel_x, panel_y,
        panel_w, panel_h
    )

    x2, y2 = world_to_screen(
        xmax, 0,
        panel_x, panel_y,
        panel_w, panel_h
    )

    glColor3f(0.35, 0.35, 0.35)

    draw_line(x1, y1, x2, y2)

    # Y axis
    x1, y1 = world_to_screen(
        0, ymin,
        panel_x, panel_y,
        panel_w, panel_h
    )

    x2, y2 = world_to_screen(
        0, ymax,
        panel_x, panel_y,
        panel_w, panel_h
    )

    draw_line(x1, y1, x2, y2)

    # --------------------------------------------------------
    # X ticks
    # --------------------------------------------------------

    for x in range(-100, 351, 50):

        sx, sy = world_to_screen(
            x, 0,
            panel_x, panel_y,
            panel_w, panel_h
        )

        draw_line(
            sx,
            sy - 5,
            sx,
            sy + 5
        )

        draw_text(
            str(x),
            sx - 10,
            sy - 25,
            (180, 180, 180),
            SMALL_FONT
        )

    # --------------------------------------------------------
    # Y ticks
    # --------------------------------------------------------

    for y in range(-200, 301, 50):

        sx, sy = world_to_screen(
            0, y,
            panel_x, panel_y,
            panel_w, panel_h
        )

        draw_line(
            sx - 5,
            sy,
            sx + 5,
            sy
        )

        draw_text(
            str(y),
            sx - 35,
            sy - 5,
            (180, 180, 180),
            SMALL_FONT
        )

    # Axis labels

    x_axis_x, x_axis_y = world_to_screen(
        330, 0,
        panel_x, panel_y,
        panel_w, panel_h
    )

    y_axis_x, y_axis_y = world_to_screen(
        0, 280,
        panel_x, panel_y,
        panel_w, panel_h
    )

    draw_text(
        "X",
        x_axis_x,
        x_axis_y + 10,
        (255, 255, 255)
    )

    draw_text(
        "Y",
        y_axis_x - 5,
        y_axis_y,
        (255, 255, 255)
    )


# ============================================================
# DRAW POINT WITH COORDINATE
# ============================================================

def draw_labeled_point(
    name,
    x,
    y,
    panel_x,
    panel_y,
    panel_w,
    panel_h,
    color,
    offset_x=8,
    offset_y=8
):

    sx, sy = world_to_screen(
        x,
        y,
        panel_x,
        panel_y,
        panel_w,
        panel_h
    )

    # Point

    glColor3f(
        color[0],
        color[1],
        color[2]
    )

    draw_point(sx, sy, 8)

    # Coordinate label

    label = f"{name}({x:.2f},{y:.2f})"

    draw_text(
        label,
        sx + offset_x,
        sy + offset_y,
        tuple(int(c * 255) for c in color),
        SMALL_FONT
    )


# ============================================================
# DRAW TRIANGLE WITH POINT LABELS
# ============================================================

def draw_labeled_triangle(
    points,
    names,
    panel_x,
    panel_y,
    panel_w,
    panel_h,
    color
):

    screen_points = []

    for x, y in points:

        sx, sy = world_to_screen(
            x,
            y,
            panel_x,
            panel_y,
            panel_w,
            panel_h
        )

        screen_points.append((sx, sy))

    # Triangle

    glColor3f(
        color[0],
        color[1],
        color[2]
    )

    glLineWidth(2)

    glBegin(GL_LINE_LOOP)

    for sx, sy in screen_points:
        glVertex2f(sx, sy)

    glEnd()

    # Points + labels

    for i, (x, y) in enumerate(points):

        draw_labeled_point(
            names[i],
            x,
            y,
            panel_x,
            panel_y,
            panel_w,
            panel_h,
            color
        )


# ============================================================
# POINT MAPPING TABLE
# ============================================================

def draw_mapping_table(
    original,
    transformed,
    panel_x,
    panel_y,
    color
):

    names = ["A", "B", "C"]

    draw_text(
        "POINT MAPPING",
        panel_x,
        panel_y,
        tuple(int(c * 255) for c in color),
        FONT
    )

    y = panel_y - 25

    for i in range(3):

        x1, y1 = original[i]
        x2, y2 = transformed[i]

        text = (
            f"{names[i]}({x1:.2f},{y1:.2f})"
            f"  ->  "
            f"{names[i]}'({x2:.2f},{y2:.2f})"
        )

        draw_text(
            text,
            panel_x,
            y,
            (230, 230, 230),
            SMALL_FONT
        )

        y -= 20


# ============================================================
# DRAW PANEL
# ============================================================

def draw_panel(
    title,
    subtitle,
    original,
    transformed,
    panel_x,
    panel_y,
    panel_w,
    panel_h,
    transformed_color
):

    # Title

    draw_text(
        title,
        panel_x + 15,
        panel_y + panel_h - 30,
        tuple(int(c * 255) for c in transformed_color),
        TITLE_FONT
    )

    # Subtitle

    draw_text(
        subtitle,
        panel_x + 15,
        panel_y + panel_h - 55,
        (230, 230, 230),
        SMALL_FONT
    )

    # Axes

    draw_axes(
        panel_x,
        panel_y,
        panel_w,
        panel_h - 80
    )

    # Original triangle

    draw_labeled_triangle(
        original,
        ["A", "B", "C"],
        panel_x,
        panel_y,
        panel_w,
        panel_h - 80,
        (0.0, 0.9, 1.0)
    )

    # Transformed triangle

    draw_labeled_triangle(
        transformed,
        ["A'", "B'", "C'"],
        panel_x,
        panel_y,
        panel_w,
        panel_h - 80,
        transformed_color
    )

    # Mapping information

    draw_mapping_table(
        original,
        transformed,
        panel_x + 20,
        panel_y + 20,
        transformed_color
    )


# ============================================================
# MAIN
# ============================================================

def main():

    if not glfw.init():

        print("Failed to initialize GLFW")
        return

    window = glfw.create_window(
        WIDTH,
        HEIGHT,
        "2D Transformations - Exact Point Mapping",
        None,
        None
    )

    if not window:

        glfw.terminate()
        return

    glfw.make_context_current(window)

    # 2D projection

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    glOrtho(
        0,
        WIDTH,
        0,
        HEIGHT,
        -1,
        1
    )

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # --------------------------------------------------------
    # Original points
    # --------------------------------------------------------

    original = [
        (50, 50),
        (150, 50),
        (100, 150)
    ]

    # --------------------------------------------------------
    # Transformations
    # --------------------------------------------------------

    translated = translation(
        original,
        120,
        60
    )

    scaled = scaling(
        original,
        1.5,
        1.5
    )

    rotated = rotation(
        original,
        45
    )

    reflected = reflection_x(
        original
    )

    # --------------------------------------------------------
    # Main loop
    # --------------------------------------------------------

    while not glfw.window_should_close(window):

        glClearColor(
            0.02,
            0.02,
            0.02,
            1.0
        )

        glClear(GL_COLOR_BUFFER_BIT)

        # ====================================================
        # TOP LEFT - TRANSLATION
        # ====================================================

        draw_panel(
            "1. TRANSLATION",
            "Tx = 120, Ty = 60",
            original,
            translated,
            20,
            460,
            670,
            400,
            (1.0, 0.15, 0.15)
        )

        # ====================================================
        # TOP RIGHT - SCALING
        # ====================================================

        draw_panel(
            "2. SCALING",
            "Sx = 1.5, Sy = 1.5",
            original,
            scaled,
            710,
            460,
            670,
            400,
            (0.1, 0.7, 1.0)
        )

        # ====================================================
        # BOTTOM LEFT - ROTATION
        # ====================================================

        draw_panel(
            "3. ROTATION",
            "Rotation = 45 degrees",
            original,
            rotated,
            20,
            20,
            670,
            400,
            (1.0, 1.0, 0.1)
        )

        # ====================================================
        # BOTTOM RIGHT - REFLECTION
        # ====================================================

        draw_panel(
            "4. REFLECTION",
            "Reflection about X-axis",
            original,
            reflected,
            710,
            20,
            670,
            400,
            (1.0, 0.1, 0.9)
        )

        # ----------------------------------------------------
        # Equations at bottom
        # ----------------------------------------------------

        draw_text(
            "Translation: (x,y) -> (x+Tx, y+Ty)",
            30,
            5,
            (255, 80, 80),
            SMALL_FONT
        )

        draw_text(
            "Scaling: (x,y) -> (Sx*x, Sy*y)",
            350,
            5,
            (80, 180, 255),
            SMALL_FONT
        )

        draw_text(
            "Rotation: x'=xcos(theta)-ysin(theta), y'=xsin(theta)+ycos(theta)",
            650,
            5,
            (255, 255, 80),
            SMALL_FONT
        )

        glfw.swap_buffers(window)

        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()
