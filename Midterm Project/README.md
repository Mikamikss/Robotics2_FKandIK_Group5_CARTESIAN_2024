# Robotics 2: Forward and Inverse Kinematics of a Cartesian manipulator

<p align="center">
  <img src=https://github.com/Mikamikss/Robotics2_FKandIK_Group5_CARTESIAN_2024/blob/main/Midterm%20Project/Gif%20%26%20GUI/7f62e744a538f5ef656e7aff339800af.gif style="height: 300px; float: left;">
 </p>
 
## :ledger: Table of Contents

  - [I. Abstract](#i-abstract)
  
  - [II. Introduction](#ii-introduction)
    
  - [III. Degrees of Freedom](#iii-degrees-of-freedom)
    
  - [IV. Kinematic Diagram and D-H Frame](#iv-kinematic-diagram-and-d-h-frame)
    
  - [V. D-H Parametric Table](#v-d-h-parametric-table)
    
  - [VI. Homogeneous Transformation Matrix](#vi-homogeneous-transformation-matrix)
    
  - [VII. Inverse Kinematics](#vii-inverse-kinematics)
    
  - [VIII. Forward and Inverse Kinematics Calculator (Application)](#viii-forward-and-inverse-kinematics-calculator-application)
    
  - [IX. References](#ix-references)
    
  - [X. Group Members](#x-group-members)


## I :beginner: Abstract

<p align="left">
  <img src=https://github.com/Mikamikss/Robotics2_FKandIK_Group5_CARTESIAN_2024/blob/main/Midterm%20Project/Gif%20%26%20GUI/writing-an-abstract-illustr-400x400.png style="height: 200px; float: left;">
</p>
 
 <p align="justify">
Forward kinematics in a Cartesian manipulator involves determining the position and orientation of the end-effector (tool) based on the lengths of the robot's links and the angles of its joints. By using geometric and trigonometric relationships, the forward kinematics equations can precisely locate where the end-effector is in the Cartesian space. This information is vital for robot control, path planning, and overall system design.
<p align="justify">
   Inverse kinematics on the other hand, deals with finding the joint angles required to position the end-effector at a specific location and orientation. It's a more complex problem as it involves solving nonlinear equations, especially in robots with multiple degrees of freedom. Despite its complexity, inverse kinematics is essential for tasks where precise control over the end-effector's position and orientation is needed, such as in robotic surgery or industrial automation.

## II :zap: Introduction

<p align="left">
  <img src=https://github.com/Mikamikss/Robotics2_FKandIK_Group5_CARTESIAN_2024/blob/main/Midterm%20Project/Gif%20%26%20GUI/200w.gif style="height: 200px; float: left;">
 </p>

<p align="justify"> 
   A Cartesian manipulator, also known as a Cartesian robot or gantry robot, is a type of industrial robot that operates in a three-dimensional Cartesian coordinate system (X, Y, and Z). Unlike other types of robots that use joints with rotational or prismatic movement, Cartesian manipulators typically move along straight lines between fixed points. This makes them well-suited for applications that require precise and repeatable linear motion, such as pick-and-place operations, assembly, and 3D printing.
  
<p align="justify">
   The concept of Cartesian manipulation dates back to the early days of industrial automation. In the 1950s and 1960s, when the field of robotics was still in its infancy, early Cartesian robots were developed for tasks such as welding, painting, and handling heavy materials in factories. These early robots were often large and bulky, with limited flexibility compared to modern robotic systems.
  
<p align="justify"> 
   Over the years, advancements in technology have led to the development of more compact and versatile Cartesian manipulators. Today, Cartesian robots are widely used in various industries, including automotive, electronics, and pharmaceuticals, for a wide range of applications. Their ability to provide precise and controlled linear motion makes them indispensable in modern manufacturing processes, where speed, accuracy, and repeatability are crucial.


  
### III :electric_plug: Degrees of Freedom

<p align="center">
  <img src=https://github.com/Mikamikss/Robotics2_FKandIK_Group5_CARTESIAN_2024/blob/main/Midterm%20Project/Gif%20%26%20GUI/Yamaha_Cartesian_robot_gif.webp style="height: 300px; float: left;">
 </p>
<p align="justify">
Degrees of Freedom (DOF) refer to the number of independent parameters that define the configuration or motion of a robot. Essentially, it indicates how many different ways a robot can move within its environment.The more the degree of freedom, the more flexible and adaptable the robot. A robot with high DOF can make more complex movements and perform a variety of tasks.

<div align="center">
  
  |  **Cartesian Manipulator Solution** |
  |     :-----:      |
  | $$M = 6n - \sum_{i=1}^m (6-C_i)$$ |
  | $$M = 6(4) - [(6-1) + (6-1) + (6-1)]$$ |
  | $$M = 24 - (5 + 5 + 5)$$ |
  | $$M = 24 - 15$$ |
  | $$M = 9$$ |
  | **∴ This is a Redundant Cartesian Manipulator with 9 Mobility.** |

</div>
<br>

<p align="justify">
  The formula calculates the mobility (M) of a Cartesian manipulator with three degrees of freedom (DOF). It starts with the total possible DOF (6 times the number of joints) and subtracts the constraints introduced by passive joints. In this case, with three joints and no passive joints, the calculation simplifies to M = 6(4) - 0 = 24. Since the manipulator is redundant with 3 DOF, the final mobility is 24 - 3 = 24. This means the manipulator can move in three independent directions, as expected for a Redundant Cartesian manipulator with 3 DOF.

  
### IV :package: Kinematic Diagram and D-H Frame

<p align="center">
  <img src=https://github.com/Mikamikss/Robotics2_FKandIK_Group5_CARTESIAN_2024/blob/main/Midterm%20Project/Gif%20%26%20GUI/image_processing20190916-29947-1vc8bjz.gif style="height: 300px; float: left;">
 </p>  
 
<p align="justify">
A kinematic diagram is a schematic representation of the joints and links of a robotic manipulator, illustrating how they are connected and move relative to each other. It helps visualize the motion of the robot and is essential for analyzing its kinematics. The Denavit-Hartenberg (D-H) frame assignment is a method used to assign coordinate frames to each joint of a robot, enabling the description of its kinematics.

<p align="justify">
The D-H frame assignment involves four parameters: theta (θ), alpha (α), r, and d. Theta represents the rotation about the previous z-axis to align the x-axes, alpha represents the rotation about the x-axis to align the z-axes, r represents the distance along the previous z-axis to the common normal, and d represents the distance along the common normal to the next z-axis. These parameters are used to construct transformation matrices that describe the relationship between adjacent frames.
  
<p align="justify">
The history of the D-H frame assignment dates back to the work of Jacques Denavit and Richard Hartenberg in the 1950s. They developed the D-H parameters as a standardized method for describing the kinematics of robotic manipulators, which has since become widely adopted in robotics. The D-H parameters provide a systematic and uniform approach to modeling robot kinematics, making it easier to analyze and control robotic systems.

<p align="center">
  <img src=https://github.com/Mikamikss/Robotics2_FKandIK_Group5_CARTESIAN_2024/blob/main/Midterm%20Project/Gif%20%26%20GUI/ddsadasdassdadas.gif style="height: 300px; float: left;">
 </p> 
 
**D-H Frame Assignment** follows these rules when assigning frames in a kinematic diagram:

- **Rule 1**: The z-axis represents the axis of rotation for a revolute/twisting joint or the direction of translation for a prismatic joint.
- **Rule 2**: The x-axis must be perpendicular to both its own z-axis and the z-axis of the preceding frame.
- **Rule 3**: Each axis must intersect the z-axis of the preceding frame. This can be achieved by rotating or translating the axis to align with the z-axis.
- **Rule 4**: Frames must follow the right-hand rule for consistency.

<p align="right">
  <img src=https://github.com/Mikamikss/Robotics2_FKandIK_Group5_CARTESIAN_2024/blob/main/Midterm%20Project/Pictures/rhr_xyz.png style="height: 300px;">
 </p>


## V :wrench: D-H Parametric Table

<p align="center"> <b> D-H Parametric Table of Cartesian Manipulator </b> </p>
<div align="center">
  
|  n   |  θ   |  α   |  r  |  d  |
| :--: | :--: | :--: | :-: | :-: |   
|  1   |  0°  | 270° |  0  |  a1 |
|  2   | 270° | 270° |  0  |a2+d1|
|  3   |  90° | 270° |  0  |a3+d2|
|  4   |  0°  |  0°  |  0  |a4+d3|

</div>
<br>

<p align="justify"> 
The D-H (Denavit-Hartenberg) Parametric Table organizes four key parameters crucial for describing a robotic manipulator's kinematics: theta, alpha, r, and d. Theta defines the joint angle between current and next links, indicating the rotation around the z-axis of the frame. For instance, Theta 1 is 0° as it aligns perpendicular to the x-axis of the subsequent frame. Alpha signifies the offset angle between z-axes of consecutive frames, with Alpha 1 at 270° for counterclockwise rotation to align with the next frame's z-axis. Parameter r represents the distance between origins of adjacent frames along the x-axis, resulting in all r values being 0 in this case. Lastly, d represents the distance along the z-axis from the origin of one frame to another, with d1 as A1 for the base frame and similar calculations for d2, d3, and d4. Completing this table for each link provides a concise description of the manipulator's geometry, crucial for computing homogeneous transformation matrices. These matrices determine the manipulator's end-effector position and orientation based on joint variables.


### VI :notebook: Homogeneous Transformation Matrix

<p align="center">
  <img src=https://github.com/Mikamikss/Robotics2_FKandIK_Group5_CARTESIAN_2024/blob/main/Midterm%20Project/Gif%20%26%20GUI/tumblr_77c9c5851d894930ec22b6ec95a57c71_f5a04dc5_400.gif style="height: 300px; float: left;">
 </p>
 
<p align="justify">
    In a Cartesian manipulator, the Homogeneous Transformation Matrix (HTM) is a mathematical tool used to represent the position and orientation of the end-effector relative to the base frame. It's a 4x4 matrix that combines both rotation and translation information in a single representation. Each element of the matrix corresponds to a specific transformation component, such as rotation angles and translation distances along the x, y, and z axes.
    

<p align="center"><b>Homogeneous Transformation Matrix Formula</b>
 
  $$
H_{n}^{n-1} =
\begin{bmatrix}
\text{Rotation} \ (3\times3) & \text{Position} \ (3\times1) \\
0 & 1
\end{bmatrix}
$$

Obtaining the Homogeneous Transformation Matrix Formula Computed Method

<p align="center">
  The Homogeneous Transformation Matrix $H_{1}^{0}$ represents the transformation from coordinate frame 1 to coordinate frame 0. It describes both the translation and rotation between the two frames. In this specific example, $H_{1}^{0}$ represents a translation along the z-axis by a distance of $a1$, while maintaining the orientation of frame 1 relative to frame 0.
  
$$
H_{1}^{0} =
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & -1 & 0 & a1 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

The Homogeneous Transformation Matrix presents the transformation from coordinate frame 2 to coordinate frame 1. In this matrix, there is a rotation of -90 degrees about the x-axis and a translation along the z-axis by a distance of $H_{1}^{0}$ a2+d1. This means that the orientation of frame 2 relative to frame 1 is changed, and frame 2 is shifted upward along the z-axis by the sum of $a2+d1$.


$$
H_{2}^{1} =
\begin{bmatrix}
0 & 0 & 1 & 0 \\
-1 & 0 & 0 & 0 \\
0 & -1 & 0 & a2+d1 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

The Homogeneous Transformation Matrix $H_{3}^{2}$ describes the transformation from coordinate frame 3 to coordinate frame 2. This matrix involves a rotation of 90 degrees about the y-axis and a translation along the z-axis by a distance of $a3+d2$. As a result, the orientation of frame 3 relative to frame 2 is changed, and frame 3 is shifted upward along the z-axis by the sum of 
$a3$ and $d2$.

$$
H_{3}^{2} =
\begin{bmatrix}
0 & 0 & -1 & 0 \\
1 & 0 & 0 & 0 \\
0 & -1 & 0 & a3+d2 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

The Homogeneous Transformation Matrix $H_{4}^{3}$ represents the transformation from coordinate frame 4 to coordinate frame 3. In this matrix, there is no rotation, only a translation along the z-axis by a distance of $a4+d2$. This means that the orientation of frame 4 relative to frame 3 remains the same, and frame 4 is shifted upward along the z-axis by the sum of $a4$ and $d2$.

$$
H_{4}^{3} =
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & a4+d2 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$



### VII :nut_and_bolt: Inverse Kinematics

<p align="right">
  <img src=https://github.com/Mikamikss/Robotics2_FKandIK_Group5_CARTESIAN_2024/blob/main/Midterm%20Project/Gif%20%26%20GUI/man-flexing-arm-muscle-dwg-ws-bs-gs-hd-anim.gif style="height: 200px; float: left;">
 </p>


<p align="justify"> 
    Kinematics of a Cartesian manipulator involves describing the relationship between the manipulator's joint motions and the resulting position and orientation of its end-effector in a Cartesian coordinate system. This typically includes analyzing the manipulator's forward kinematics to determine the end-effector's pose based on the joint angles. Inverse Kinematics, on the other hand, involves solving for the joint angles required to achieve a desired end-effector pose. This process is essential for programming the manipulator to move to specific positions and orientations in its workspace. It's important in applications where precise control over the end-effector position is required, such as in pick-and-place operations in manufacturing or robotics.


<p align="center">
  <img src= https://github.com/Mikamikss/Robotics2_FKandIK_Group5_CARTESIAN_2024/blob/main/Midterm%20Project/Pictures/front%20view.png style="height: 300px;">
 </p>

<p align="center">
Moving to the z-axis analysis, we encounter another significant relationship that helps us understand the manipulator's behavior in the vertical direction. Considering the z-axis components, we find that the z-coordinate of the end effector (denoted as z) can be expressed as z = a1 - a4 - d3. Rearranging this equation, we derive the expression for the length of link d3 as d3 = a1 - a4 - z. This relationship clarifies how the length of link d3 affects the vertical position of the end effector, providing valuable insights for designing and controlling the manipulator's motion along the z-axis. Understanding these relationships is essential for effective analysis and design of Cartesian manipulators, as they form the basis for predicting and optimizing the manipulator's movement in different directions.

</center>


<p align="center">
  <img src= https://github.com/Mikamikss/Robotics2_FKandIK_Group5_CARTESIAN_2024/blob/main/Midterm%20Project/Pictures/top%20view.png style="height: 300px;">
 </p>

<center>
In the top view analysis of the Cartesian manipulator, our attention shifts to the variable d1, which plays a crucial role in determining the position of the end effector along the y-axis. By examining the top view, we observe that the y-coordinate of the end effector (denoted as Y04) can be expressed as Y04 = a2 + d1, highlighting the sum of link lengths a2 and d1 along the y-axis. This relationship enables us to calculate the length of link d1 based on the known values of Y04 and a2, providing us with a clear understanding of how the manipulator's y-coordinate is influenced by the length of link d1. By comprehending this relationship, we can effectively design and control the manipulator's movement along the y-axis, ensuring precise positioning and motion control in various applications.
</center>





### VIII :file_folder: Forward and Inverse Kinematics GUI Calculator:
<p align="justify">
  In creating the Cartesian Calculator, instead of using the old fashion way of designing, we came across a website called Figma. Figma is a Tkinter Designer that generates the code after designing the GUI. 

<p align="center">
  <img src= https://github.com/Mikamikss/Robotics2_FKandIK_Group5_CARTESIAN_2024/blob/main/Midterm%20Project/Pictures/UNDER%20INTRO.png style="height: 500px;">
 </p>

<p align="center">Elements used:


  
1.<p align="left">
  <img src= https://github.com/Mikamikss/Robotics2_FKandIK_Group5_CARTESIAN_2024/blob/main/Midterm%20Project/Pictures/CCC1.png style="height: 200px;">
 </p>

<p align="left">In the design, the D-H Frame Assignment of Cartesian Robot (Manipulator) can be seen in the upper left side of the GUI. 

2.<p align="left">
  <img src= https://github.com/Mikamikss/Robotics2_FKandIK_Group5_CARTESIAN_2024/blob/main/Midterm%20Project/Pictures/CCC2.png style="height: 200px;">
 </p>


<p align="left">In the design, the 3D view of the Cartesian Robot (Manipulator) from Matlab can be seen in the upper right side of the GUI. 

3.<p align="left">
  <img src= https://github.com/Mikamikss/Robotics2_FKandIK_Group5_CARTESIAN_2024/blob/main/Midterm%20Project/Pictures/CCC3.png style="height: 200px;">
 </p>

<p align="left">In the design, the 3D view of the Cartesian Robot (Manipulator) from Matlab can be seen in the upper right side of the GUI.




FUNCTIONALITY: 
<div
  align="justify">&nbsp;</div>
Reset button

<p align="left">
  <img src= "https://github.com/Mikamikss/Robotics2_FKandIK_Group5_CARTESIAN_2024/blob/main/Midterm%20Project/Pictures/FFF1.png" style="height: 100px;">
 </p>

<p align="left">The reset button functions as the reset of all entities in the text box. By clicking the Reset Button it  does its programmed functionality. 


<div
  align="justify">&nbsp;</div>

Inverse Button

<p align="left">
  <img src="https://github.com/Mikamikss/Robotics2_FKandIK_Group5_CARTESIAN_2024/blob/main/Midterm%20Project/Pictures/FFF2.png?raw=true" style="height: 100px;">
 </p>
 
<p align="left">The inverse button functions as the signal to compute the Joint Variable of the Cartesian Robot (manipulator). By clicking the Inverse Button it does its programmed functionality. 

<p align="left">
Note: 
  The Inverse Button will only function correctly when you type numbers (0,1,2,3,4,5,6,...). 
  
  The Inverse Button will only function correctly if there are values in the textboxes of Link Lengths and Position Vector.

<div
  align="justify">&nbsp;</div>


Forward Button

<p align="left">
  <img src= "https://github.com/Mikamikss/Robotics2_FKandIK_Group5_CARTESIAN_2024/blob/main/Midterm%20Project/Pictures/FFF3.png?raw=true" style="height: 100px;">
 </p>

<p align="left"> 
The forward button functions as the signal to compute the Position Vector of the Cartesian Robot (manipulator). By clicking the Inverse Button it does its programmed functionality.
  
<p align="left">
Note: 
The Forward Button will only function correctly when you type numbers (0,1,2,3,4,5,6,...). 

  The Forward Button will only function correctly if there are values in the textboxes of Link Lengths and Joint Variables


<div
  align="justify">&nbsp;</div>
<div
  align="justify">&nbsp;</div>

 
<p align="left">Installation
  
<div
  align="justify">&nbsp;</div>
  
<p align="left">INSTALLATION GUIDE

<div style="text-align: left">

1. Download the zip file https://github.com/Mikamikss/Robotics2_FKandIK_Group5_CARTESIAN_2024/blob/main/Midterm%20Project/Cartesian%20GUI%20Installer/CartesianCalculator_GUI.zip
2. Extract the zip file in your chosen destination folder.
3. Open Virtual Studio Code in Ubuntu.
4. In Virtual Studio Code, click File then Open Folder.

<p align="left">
  <img src="https://github.com/Mikamikss/Robotics2_FKandIK_Group5_CARTESIAN_2024/blob/main/Midterm%20Project/Pictures/INS4.png?raw=true" style="height: 200px; float: left;">
 </p>
 
5. Open the unzipped file entitled “GUI”.
6. To run the program, first you must download the requirements.
7. To run the program, first you must download the requirements.


</div>


  
<div style="text-align: left">
  
 8. To do this, open terminal of the file named “requirement.txt”

 </div>

<p align="left">
  <img src="https://github.com/Mikamikss/Robotics2_FKandIK_Group5_CARTESIAN_2024/blob/main/Midterm%20Project/Pictures/INS8.png?raw=true" style="height: 200px; float: left;">
 </p>


 <div style="text-align: left">
   
 9. After opening requirements.txt, create a new terminal or use the shortcut Ctrl+Shift+’
 
 </div>

<p align="left">
  <img src="https://github.com/Mikamikss/Robotics2_FKandIK_Group5_CARTESIAN_2024/blob/main/Midterm%20Project/Pictures/INS10.png?raw=true" style="height: 200px; float: left;">
 </p>
 


 <div style="text-align: left">
   
 10. On the terminal, type “pip install -r requirements.txt” to install all the requirements in order to make the program run.
 
 </div>
 
<p align="left">
  <img src="https://github.com/Mikamikss/Robotics2_FKandIK_Group5_CARTESIAN_2024/blob/main/Midterm%20Project/Pictures/INS11.png?raw=true" style="height: 200px; float: left;">
 </p>
 
 
<div style="text-align: left">
   
 11. After the installation finishes, open “gui.py” under the folder “build”. To do that, type in terminal “cd build/”.

 
 </div>

<p align="left">
  <img src="https://github.com/Mikamikss/Robotics2_FKandIK_Group5_CARTESIAN_2024/blob/main/Midterm%20Project/Pictures/INS12.png?raw=true" style="height: 200px; float: left;">
 </p>


 <div style="text-align: left">
   
 12. Under /GUI/build$ run the program by typing in the terminal “python3 gui.py”
 
 </div>
 
<p align="left">
  <img src="https://github.com/Mikamikss/Robotics2_FKandIK_Group5_CARTESIAN_2024/blob/main/Midterm%20Project/Pictures/INS13.png?raw=true" style="height: 200px; float: left;">
 </p>

<div style="text-align: left">
   
 13. After typing python3 gui.py, the Cartesian Calculator GUI will appea.
 
 </div>

<p align="left">
  <img src="https://github.com/Mikamikss/Robotics2_FKandIK_Group5_CARTESIAN_2024/blob/main/Midterm%20Project/Pictures/INS14.png?raw=true" style="height: 200px; float: left;">
 </p>

 </div>

<div style="text-align: left">
   
 14. That’s all for the installation guide. Enjoy the Cartesian Calculator.
 
 </div>


 
 We also included a python code with a GUI with a design same from the previous lesson. The python code is entitled gui2.py. You may use this to check the functionality of the Cartesian Manipulator Calculator without taking into account the GUI design. The purpose of "gui2.py" is to only show that the functionality of Cartesian Manipulator Calculator is working.

Note: 
  The python code "gui.py" is located under "build"
 
### IX :hammer:References


### X :rocket: Group Members
- Baylon, Aron James M.
- Espina, Mikaela 
- Cabarrubia, Yuel Jeiro Daemian M.
- Punzalan, Hazel
- Montalbo, Christian Kent
