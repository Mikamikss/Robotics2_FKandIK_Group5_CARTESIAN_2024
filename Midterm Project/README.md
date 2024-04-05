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

 
