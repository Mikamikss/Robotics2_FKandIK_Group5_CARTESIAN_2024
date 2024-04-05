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
  | $$M = 6(3) - [(6-1) + (6-1) + (6-1)]$$ |
  | $$M = 18 - (5 + 5 + 5)$$ |
  | $$M = 18 - 15$$ |
  | $$M = 3$$ |
  | **∴ This is an Under-Actuated Cartesian Manipulator with 3 Degrees of Freedom (DOF).** |

</div>
<br>

<p align="justify">
  The formula calculates the mobility (M) of a Cartesian manipulator with three degrees of freedom (DOF). It starts with the total possible DOF (6 times the number of joints) and subtracts the constraints introduced by passive joints. In this case, with three joints and no passive joints, the calculation simplifies to M = 6(3) - 0 = 18. Since the manipulator is under-actuated with 3 DOF, the final mobility is 18 - 3 = 15. This means the manipulator can move in three independent directions, as expected for an under-actuated Cartesian manipulator with 3 DOF.

  
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



