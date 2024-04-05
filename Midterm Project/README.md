<h1 align="center">Robotics 2: Forward and Inverse Kinematics of a Cartesian manipulator</h1>
<br>


<p align="center">
  <img src=https://github.com/Mikamikss/Robotics2_FKandIK_Group5_CARTESIAN_2024/blob/main/Midterm%20Project/Gif%20%26%20GUI/7f62e744a538f5ef656e7aff339800af.gif style="height: 300px; float: left;">
 </p>

## Table of Contents
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
<hr> 
<br>

## I. Abstract

<p align="left">
  <img src=https://github.com/Mikamikss/Robotics2_FKandIK_Group5_CARTESIAN_2024/blob/main/Midterm%20Project/Gif%20%26%20GUI/writing-an-abstract-illustr-400x400.png style="height: 200px; float: left;">
 </p>

<p align="justify">
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b><i>Forward kinematics</i></b> in a Cartesian manipulator involves determining the position and orientation of the end-effector (tool) based on the lengths of the robot's links and the angles of its joints. By using geometric and trigonometric relationships, the forward kinematics equations can precisely locate where the end-effector is in the Cartesian space. This information is vital for robot control, path planning, and overall system design.
<p align="justify">
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b><i>Inverse kinematics</i></b> on the other hand, deals with finding the joint angles required to position the end-effector at a specific location and orientation. It's a more complex problem as it involves solving nonlinear equations, especially in robots with multiple degrees of freedom. Despite its complexity, inverse kinematics is essential for tasks where precise control over the end-effector's position and orientation is needed, such as in robotic surgery or industrial automation.
<hr> 
<br>

## II. Introduction

<p align="left">
  <img src=https://github.com/Mikamikss/Robotics2_FKandIK_Group5_CARTESIAN_2024/blob/main/Midterm%20Project/Gif%20%26%20GUI/200w.gif style="height: 200px; float: left;">
 </p>
 
<p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b><i>Cartesian manipulators</i></b> are made up of a single kinematic linkage chain, with each linear actuator sequentially driving the next one. They do not change the direction of the moving platform. These manipulators are particularly simple to handle because to the close connection between actuator positions and platform coordinates.These manipulators use linear actuators that are mutually perpendicular. Their movement is directly proportional to the X, Y, and Z position coordinates of the moving platform. In other words, they use a standard Cartesian coordinate system. Unimate, the first industrial robot built in the 1950s, is a prime example of this type. Unimate's control axes correspond to a spherical coordinate system with an RRP joint topology (two revolute joints followed by a prismatic joint).
<p align="justify">
  In the context of Cartesian manipulators, elevation refers to movement along the vertical axis, or Z-axis. A Cartesian manipulator executes an elevation movement by changing its vertical position, either raising or lowering its end-effector in relation to the work surface or base. In the context of Cartesian manipulators, extension is defined as movement along one or more additional axes (X and/or Y). This action allows the manipulator to expand or retract horizontally, shifting its location in the X and/or Y directions while remaining elevated (along the Z-axis).  The ability to regulate elevation and extension individually enables efficient and precise handling of three-dimensional objects.

- **Rotation**: The robot can rotate around a vertical axis, which forms the base of the robot. This allows the robot to cover a wide horizontal range around its base.
- **Elevation**: The robot's arm can move up and down in a vertical plane, enabling it to reach different heights.
- **Extension**: The robot's arm can extend or retract, moving closer to or farther from the base.
<br>



## III. Degrees of Freedom

<p align="center">
  <img src=https://github.com/Mikamikss/Robotics2_FKandIK_Group5_CARTESIAN_2024/blob/main/Midterm%20Project/Gif%20%26%20GUI/Yamaha_Cartesian_robot_gif.webp style="height: 300px; float: left;">
 </p>
 
<p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In robotics, <b><i>Degrees of Freedom</i></b> (DOF) refer to the number of independent parameters that define the configuration or motion of a robot. Essentially, it indicates how many different ways a robot can move within its environment.The more the degree of freedom, the more flexible and adaptable the robot. A robot with high DOF can make more complex movements and perform a variety of tasks.</p>
  
<p class="blank-line">&nbsp;</p>


#### The Ideal Degrees of Freedom:
  - A <b>point</b> in 2D: 2-DOF; in 3D space: 3-DOF
  - A <b>rigid body</b> in 3D: 6-DOF
  - <b>Planar Manipulator</b>: 3-DOF
  - <b>Spatial manipulator</b>: 6-DOF
<br>


#### Types of Manipulator based on the number of Degrees of Freedom:
  - <b>Under-Actuated Manipulator</b>
      - _Spatial Manipulator_ with less than 6-DOF
      - _Planar Manipulator_ with less than 3-DOF
  - <b>Ideal manipulator</b>
      - _Spatial Manipulator_ with exactly 6-DOF
      - _Planar Manipulator_ with exactly 3-DOF
  - <b>Redundant manipulator</b>
      - _Spatial Manipulator_ with more than 6-DOF
      - _Planar Manipulator_ with more than 3-DOF
<br>


#### Grubler's Criterion for Mobility
<div align="center">
  
|  Formula for the Mobility of _Spatial Manipulator_  | Formula for the Mobility of _Planar Manipulator_ |
|         :---: |     :-----:      |
| $$M = 6n - \sum_{i=1}^m (6-Ci)$$ |  $$M = 3n - \sum_{i=1}^m (3-Ci)$$ |

</div>
<br>


#### Mechanical Manipulator Anatomy

<div align="center">
  
|  Joint type  | DOF *f* | Constraints *c* between two planar rigid bodies | Constraints *c* between two spatial rigid bodies |
|         ---: |     :-----:      |     :---:     |     :---:    |
|  Revolute (R)  |  1  |  2  |  5  |
|  Prismatic (P)  |  1  |  2  |  5  |
|  Helical (H)  |  1  |  N/A  |  5  |
|  Cylindrical (C)  |  2  |  N/A  |  4  |
|  Universal (U)  |  2  |  N/A  |  4  |
|  Spherical (S)  |  3  |  N/A  |  3  |

</div>

<br>


### Cartesian Manipulator Degrees of Freedom (DOF) Computation:
___

<div align="center">
  
|  Cartesian Manipulator Solution |
|     :-----:      |
  $$M = 6n - \sum_{i=1}^m (6-Ci)$$  $$M = 6(3) - [(6-1) + (6-1) + (6-1)]$$  $$M = 18 - (5 + 5 + 5)$$  $$M = 18 - 15$$  $$M = 3$$  <p>&#8756; This is an Under-Actuated Cartesian Manipulator with 3-DOF.</p> |

</div>
<br>

 <p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; An under-actuated Cartesian manipulator with 3 degrees of freedom (DOF) typically means that the manipulator has fewer actuators (or motors) than the total number of DOF, allowing for passive motion along some axes. For example, a 3-DOF manipulator might have one actuator for translation in the x-axis and another for translation in the y-axis, while rotation around the z-axis is left passive. This configuration is often used in applications where flexibility or compliance is desired, such as in grasping objects of varying shapes. The computation involved in controlling such a manipulator can be complex, as it requires modeling the passive DOF to predict and control their behavior.  
</p>
<br>

## IV. Kinematic Diagram and D-H Frame
<p align="center">
  <img src=https://github.com/Mikamikss/Robotics2_FKandIK_Group5_CARTESIAN_2024/blob/main/Midterm%20Project/Gif%20%26%20GUI/image_processing20190916-29947-1vc8bjz.gif style="height: 300px; float: left;">
 </p>  

  <p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A <b><i>Kinematic Diagram</i></b> is a simplified representation of a mechanism that illustrates the motion of all the components without showing the forces or the physical dimensions that cause the motion. It is an important tool used in mechanical engineering to examine the motion of mechanisms. Typically, the diagram shows the mechanism's joints and links in schematic form. It is also a diagram that shows how the links and joints are connected together when all of the joint variables have a value of 0.
</p>
<br>

  <p align="justify"> 
     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b><i>Links</i></b> are the rigid parts of the mechanical manipulator. A link is defined as a single part that can be a resistant body or a composite of resistant bodies with inflexible connections and relative motion in relation to other machine components. Also, joints are considered links and the values are constant:</p>
    
  - If it is revolute or twisting, links are drawn from the center of the rotation.
  - If it is prismatic, either linear or orthogonal, links are drawn from the center of translation.
  - If it is from base, links are drawn from the center of gravity.
    
<br>

<p align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
 <b><i>Joint Variables</i></b>, are the values that change when the joint moves. It is a connection between two or more links that allows for some motion, or potential motion, between them.  Joints are sometimes known as <b><i>kinematic pairs</i></b>. A joint variable has a two indicator which is the rotation of a counterclockwise arrow &#8634; and the arrow with the flat line at the tail &#8614;. We use this symbol &#8634; for the twisting and revolute joint and we label it as <b><i>theta</i></b> ($&theta;$) , theta is the rotation angle of the circle. While in a prismatic joint we use this symbol &#8614; and label it as $d$, $d$ is the translation length. Remember that in joint variables, the numbering of joints will be based on their consecutive order.
</p>
<br>



### D-H Frame Assignment

 <p align="justify"> 
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b><i>D-H Notation</i></b> was introduced by <b>Jacques Denavit</b> and <b>Richard Hartenberg</b> in <b>1955</b> in order to standardize the coordinate frames for spatial linkages. D-H notation is used to solve the forward kinematics of a mechanical manipulator. The <b><i>Frames</i></b> in a Mechanical Manipulator are used to determine where they are and where they need to go. It also shows the movement of our mechanical manipulator. The frames are positioned at each part of the mechanical manipulator, including the base, joints, and end effector.</p>

#### Three Types of Frames used in Mechanical Manipulator:
  - Base (World) Frame
  - User Frame
  - Tool Frame
<br>

<p align="center">
  <img src=https://github.com/Mikamikss/Robotics2_FKandIK_Group5_CARTESIAN_2024/blob/main/Midterm%20Project/Gif%20%26%20GUI/ddsadasdassdadas.gif style="height: 300px; float: left;">
 </p> 
 
<b><i>D-H Frame Assignment</i></b> follow this rules in assigning frames in a kinematic diagram:
  - **Rule 1**: The z axis must be the axis of rotation for a revolute/twisting joint, or the direction of translation for a prismatic joint.
  - **Rule 2**: The x axis must be perpendicular both to its own Z axis, and the Z axis of the frame before it.
  - **Rule 3**: Each axis must intersect the z axis of the frame before it. The rules for complying rule 3:
      - Rotate the axis until it hits the other.
      - Translate the axis until it hits the other.
  - **Rule 4**: All frames must follow the right hand rule. 
<br>
<p align="right">
  <img src=https://github.com/Mikamikss/Robotics2_FKandIK_Group5_CARTESIAN_2024/blob/main/Midterm%20Project/Pictures/rhr_xyz.png style="height: 300px;">
 </p>

### Applying D-H Frame Rules to the Kinematic Diagram of a Cartesian Manipulator

<p align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; To establish the kinematic chain of our manipulator with prismatic joints, we begin by identifying key frames: the base frame, user frame, and tool frame or end effector. Link lengths between frames are labeled sequentially as A1, A2, and so forth. Using the arrow symbol ↦ to denote translation direction (labeled as 'd'), we start at frame 0 (base frame) and progress to the tool frame. Z-axes are aligned with the prismatic joint's translation direction, and X-axes are positioned perpendicular to both their Z-axis and the preceding frame's Z-axis. Y-axes are determined following the right-hand rule. Aligning the last frame's axis of rotation with the previous frame's simplifies calculations, especially for the tool frame.
</p>
<br>

## V. D-H Parametric Table

#### Steps in Denavit-Hartenberg Notation
  1.  Assign the frames according to the 4 D-H Frame Rules.
  2.  Construct and fill out the D-H Parametric Table.
  3.  Plug the table into the Homogeneous Transformation Matrix form.
  4.  Multiply the matrices together.
<br>


<p align="center"> <b>Example of D-H Parametric Table</b> </p>

<div align="center">
  
| $n$   | $\theta$ | $\alpha$ |    $r$    |    $d$    |
| :---: |  :---:  |  :---:  |  :---:  |  :---:  |   
|   1   |         |         |         |         |
|   2   |         |         |         |         |
|   3   |         |         |         |         |
|   4   |         |         |         |         |

</div>
<br>


 <p align="justify"> 
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  The <b><i>Four Parameters</i></b> in the D-H Parametric are  $&theta;$, $&alpha;$ $r$ and $d$. The $&theta;$ and the $&alpha;$ are the rotation or orientation parameters and their units are in degrees or radian. While $d$ and $r$ are the position or translation parameters and their units are in units of length.
  </p>
<br>


<div align="center">
  
| $\theta$ | $\alpha$ | $d$ | $r$ |
|     :---:     |     :---:     |     :---:    |     :---:     
|  " $\theta$ " is the rotation around $z_{n-1}$ that is required to get $x_{n-1}$ to match $x_{n}$, with the joint variable theta if the joint is a revolute or twisting joint.  |   " $\alpha$ " is the rotation around $x_{n}$ that is required to match $z_{n-1}$ to $z_{n}$.  |  " $d$ " is the distance from the origin of $n-1$ and $n$ frames along the $z_{n-1}$ direction with the joint variable if the joint is prismatic.  |  " $r$ " is the distance from the origin of $n-1$ and $n$ frames along the $x_{n}$ direction.  |

</div>
<br>


### D-H Parametric Table for a Cartesian Manipulator

 <p align="justify"> 
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  The D-H (Denavit-Hartenberg) Parametric Table is a systematic approach for organizing the four essential parameters—theta, alpha, r, and d, required to describe the kinematics of a robotic manipulator. Theta denotes the joint angle between the current and next link, with 0 degrees for Theta 1 as it aligns perpendicular to the next frame's x-axis. Theta 2 and Theta 3 are 270 and 90 degrees, respectively, aligning with their respective x-axes. Alpha represents the offset angle between the z-axes of consecutive frames, with values such as 270 degrees for Alpha 1 to match the next frame's z-axis. Parameter r signifies the distance from one frame's origin to the next along the x-axis, and since the frames are typically coincident, r values are 0. Lastly, d indicates the distance between frame origins along the z-axis, with d1 being A1 for the base frame and subsequent di values being perpendicular to their link lengths. Completing this table for each link provides a concise representation of the manipulator's geometry, crucial for deriving the homogeneous transformation matrices that define its end-effector's position and orientation based on joint variables.
  </p>
<br>


 
## VI. Homogeneous Transformation Matrix

<p align="left">
  <img src=https://github.com/Mikamikss/Robotics2_FKandIK_Group5_CARTESIAN_2024/blob/main/Midterm%20Project/Gif%20%26%20GUI/giphy.gif style="height: 300px; float: left;">
 </p>
 
<p align="justify"> 
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  <b><i>Homogeneous Transformation Matrix</i></b> is a crucial concept in robotics, encompassing both rotation and translation within the same matrix to describe an object's position and orientation. Unlike rotation matrices, which can be multiplied to combine rotations, position vectors cannot be added or multiplied directly. To handle both rotation and translation, we use the homogeneous transformation matrix denoted as $H_{n}^{n-1}$ or $T_{n}^{n-1}$, which combines a 3x3 rotation matrix and a 3x1 position vector into a 3x4 matrix. However, to maintain a square matrix, an augmentation row is added at the bottom, resulting in a 4x4 matrix. This matrix notation allows us to efficiently represent and calculate the position and orientation of objects in robotic systems, facilitating complex manipulations and control algorithms.
</p>
<br> 
