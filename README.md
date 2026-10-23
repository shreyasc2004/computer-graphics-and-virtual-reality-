# Computer Graphics and Virtual Reality

**SHREYAS C**  
**USN: 1RVU23CSE443**

## List of Laboratory Programs

| Sl. No. | Laboratory Experiment |
|--------:|------------------------|
| 1 | Implement DDA and Bresenham line drawing algorithms |
| 2 | Implement the Midpoint Circle Drawing Algorithm |
| 3 | Implement 2D transformations (translation, rotation, scaling, reflection and shearing) using homogeneous coordinates |
| 4 | Implement composite transformations using matrix representation |
| 5 | Implement the Cohen–Sutherland line clipping algorithm |
| 6 | Implement the Z-buffer algorithm for hidden surface removal |
| 7 | Implement the Phong illumination model for a 3D object |
| 8 | Develop a basic OpenGL program using vertex and fragment shaders |
| 9 | Create a simple interactive 3D scene using Unity |
| 10 | Implement the 3D viewing pipeline, including projection and viewport mapping for displaying 3D objects on a 2D screen |

---

# Experiments

## Experiment 1: DDA and Bresenham's Line Drawing Algorithms

Implementation of the DDA (Digital Differential Analyzer) and Bresenham's line drawing algorithms using OpenGL and GLFW.

**Program:**

- `CG-LAB1-443.py`

**Output:**

![Experiment 1](CG-LAB1-443.png)

---

## Experiment 2: Midpoint Circle Drawing Algorithm

Implementation of the Midpoint Circle Drawing Algorithm using OpenGL and GLFW.

**Program:**

- `CG-LAB2-443.py`

**Output:**

![Experiment 2](CG-LAB2-443.png)

---

## Experiment 3: 2D Transformations Using Homogeneous Coordinates

Implementation of basic 2D transformations using homogeneous coordinate representation.

The transformations include:

- Translation
- Rotation
- Scaling
- Reflection
- Shearing

**Program:**

- `CD-LAB3-443.py`

The program demonstrates how transformation matrices can be applied to 2D objects.

**Output:**

![Experiment 3](CGVR-LAB3-443.png)

---

## Experiment 4: Composite Transformations

Implementation of composite 2D transformations using matrix representation.

Multiple transformations are combined and applied to graphical objects using transformation matrices.

**Program:**

- `CD-LAB4-443.py`

  **Output:**

![Experiment 2](CGVR-LAB4-443.png)

---

## Experiment 5: Cohen–Sutherland Line Clipping

Implementation of the Cohen–Sutherland line clipping algorithm.

The algorithm uses region codes to determine whether a line lies:

- Completely inside the clipping window
- Completely outside the clipping window
- Partially inside the clipping window

**Output:**

![Experiment 5](CGVR-LAB5-443.png)

**Program:**

- `CGVR-LAB5-443.py`

---

## Experiment 6: Z-Buffer Algorithm

Implementation of the Z-buffer algorithm for hidden surface removal.

The Z-buffer algorithm determines which surface is visible at each pixel by comparing the depth values of different surfaces.

**Output:**

![Experiment 6](CGVR-LAB6-443.png)

**Program:**

- `CGVR-LAB6-443.py`

---

## Experiment 7: Phong Illumination Model

Implementation of the Phong illumination model for a 3D object.

The Phong model considers three components of illumination:

- Ambient reflection
- Diffuse reflection
- Specular reflection

The model is used to produce realistic lighting effects on 3D objects.

**Output:**

![Experiment 7](CGVR-LAB7-443.png)

**Program:**

- `CGVR-LAB7-443.py`

---

## Experiment 8: OpenGL Vertex and Fragment Shaders

Development of a basic OpenGL program using vertex and fragment shaders.

The experiment demonstrates the programmable graphics pipeline using:

- Vertex shaders
- Fragment shaders
- OpenGL rendering

**Program:**

- `CD-LAB8-443.py`

**Output:**

![Experiment 8](CGVR-LAB8-443.png)

---

## Experiment 9: Interactive 3D Scene Using Unity

Creation of a simple interactive 3D scene using Unity.

The experiment demonstrates:

- Player movement and jumping using a character controller
- Obstacles, rotating objects and collectible items
- A camera that follows the player
- An on-screen collectible counter and completion message

**Program:**

- Unity project folder: [unity_interactive_scene_lab9](unity_interactive_scene_lab9/)
- Scene setup: [LabSceneAutoSetup_lab9.cs](unity_interactive_scene_lab9/Assets/Editor/LabSceneAutoSetup_lab9.cs)
- Player movement: [PlayerController_lab9.cs](unity_interactive_scene_lab9/Assets/Scripts/PlayerController_lab9.cs)
- Camera follow: [CameraFollow_lab9.cs](unity_interactive_scene_lab9/Assets/Scripts/CameraFollow_lab9.cs)
- Collectibles: [Collectible_lab9.cs](unity_interactive_scene_lab9/Assets/Scripts/Collectible_lab9.cs)
- Object rotation: [RotatingObject_lab9.cs](unity_interactive_scene_lab9/Assets/Scripts/RotatingObject_lab9.cs)
- On-screen display: [GameHUD_lab9.cs](unity_interactive_scene_lab9/Assets/Scripts/GameHUD_lab9.cs)

**Controls:**

- WASD / Arrow keys: move
- Space: jump
- R: reset the player position
- Esc: quit the built application

**Output:**

The scene contains a player, obstacles, rotating cubes and five collectibles. Collecting all five displays the completion message. A screenshot for this experiment has not been added to the repository.

---

## Experiment 10: 3D Viewing Pipeline

Implementation of the 3D viewing pipeline using Python, Pygame and OpenGL, with an additional Unity version.

A rotating cube with six coloured faces is displayed in two viewports: orthographic projection on the left and perspective projection on the right.

The experiment covers:

- Model transformation
- View transformation
- Orthographic and perspective projection
- Viewport mapping
- Depth testing for hidden surface removal

**Program:**

- Python program: [3d_viewing_pipeline_lab10.py](lab10/3d_viewing_pipeline_lab10.py)
- Jupyter notebook: [3d_viewing_pipeline_lab10.ipynb](lab10/3d_viewing_pipeline_lab10.ipynb)
- Unity project and instructions: [Unity_3D_Viewing_Pipeline](lab10/Unity_3D_Viewing_Pipeline/README.md)
- Unity script: [Lab10ViewingPipelineDemo.cs](lab10/Unity_3D_Viewing_Pipeline/Assets/Scripts/Lab10ViewingPipelineDemo.cs)

**Output:**

![Experiment 10 - 3D viewing pipeline, output 1](lab10/3d_viewing_pipeline_output_1_lab10.png)

![Experiment 10 - 3D viewing pipeline, output 2](lab10/3d_viewing_pipeline_output_2_lab10.png)

---

# Technologies Used

- Python
- C#
- OpenGL
- GLFW
- Pygame
- Unity
- Computer Graphics Algorithms
- Homogeneous Transformation Matrices
- Shader Programming

# Repository Structure

```text
computer-graphics-and-virtual-reality/
│
├── CG-LAB1-443.py
├── CG-LAB1-443.png
│
├── CG-LAB2-443.py
├── CG-LAB2-443.png
│
├── CD-LAB3-443.py
│
├── CD-LAB4-443.py
│
├── CGVR-LAB5-443.py
├── CGVR-LAB5.png
│
├── CD-LAB6-443.py
│
├── CD-LAB7-443.py
│
├── CD-LAB8-443.py
├── CGVR-LAB8.png
│
├── unity_interactive_scene_lab9/
│   ├── Assets/
│   │   ├── Editor/LabSceneAutoSetup_lab9.cs
│   │   └── Scripts/
│   │       ├── PlayerController_lab9.cs
│   │       ├── CameraFollow_lab9.cs
│   │       ├── Collectible_lab9.cs
│   │       ├── RotatingObject_lab9.cs
│   │       └── GameHUD_lab9.cs
│   ├── Packages/
│   └── ProjectSettings/
│
├── lab10/
│   ├── 3d_viewing_pipeline_lab10.py
│   ├── 3d_viewing_pipeline_lab10.ipynb
│   ├── 3d_viewing_pipeline_output_1_lab10.png
│   ├── 3d_viewing_pipeline_output_2_lab10.png
│   └── Unity_3D_Viewing_Pipeline/
│       ├── Assets/
│       ├── Packages/
│       ├── ProjectSettings/
│       └── README.md
│
└── README.md
```
