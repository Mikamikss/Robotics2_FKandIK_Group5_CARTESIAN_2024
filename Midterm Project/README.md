<h1 align="center">Robotics 2: Forward and Inverse Kinematics of a Spherical Manipulator</h1>
<br>

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
    (description)
<hr> 
<br>

## II. Introduction

  <p align="center">
  <img src=https://github.com/MEXECardenas/SPHERICAL_G7_Assignment_2024/blob/0b0c965065028159e971cf92570e9344e1e41f4b/Kinematic%20Diagrams%20with%20D-H%20Parametric%20Tables/Spherical%20Manipulator%20-%20Modern%20Variant.png alt=Spherical-Manipulator-Modern-Variant style="height: 300px; float: left;">
  <img src=https://github.com/MEXECardenas/SPHERICAL_G7_Assignment_2024/blob/a9a0b089f3911adfcc915ab37b061117838ae024/Kinematic%20Diagrams%20with%20D-H%20Parametric%20Tables/Spherical%20Manipulator%20(Modern%20Variant).gif alt=Spherical-Manipulator-(Modern-Variant) style="height: 300px; float: right;">
  </p>
</div>
<br>

<p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b><i>Cartesian manipulators</i></b> are made up of a single kinematic linkage chain, with each linear actuator sequentially driving the next one. They do not change the direction of the moving platform. These manipulators are particularly simple to handle because to the close connection between actuator positions and platform coordinates.These manipulators use linear actuators that are mutually perpendicular. Their movement is directly proportional to the X, Y, and Z position coordinates of the moving platform. In other words, they use a standard Cartesian coordinate system. Unimate, the first industrial robot built in the 1950s, is a prime example of this type. Unimate's control axes correspond to a spherical coordinate system with an RRP joint topology (two revolute joints followed by a prismatic joint).
 
  In the context of Cartesian manipulators, elevation refers to movement along the vertical axis, or Z-axis. A Cartesian manipulator executes an elevation movement by changing its vertical position, either raising or lowering its end-effector in relation to the work surface or base. In the context of Cartesian manipulators, extension is defined as movement along one or more additional axes (X and/or Y). This action allows the manipulator to expand or retract horizontally, shifting its location in the X and/or Y directions while remaining elevated (along the Z-axis).  The ability to regulate elevation and extension individually enables efficient and precise handling of three-dimensional objects.

- **Rotation**: The robot can rotate around a vertical axis, which forms the base of the robot. This allows the robot to cover a wide horizontal range around its base.
- **Elevation**: The robot's arm can move up and down in a vertical plane, enabling it to reach different heights.
- **Extension**: The robot's arm can extend or retract, moving closer to or farther from the base.

<br>



## III. Degrees of Freedom

  
### Group Members:
