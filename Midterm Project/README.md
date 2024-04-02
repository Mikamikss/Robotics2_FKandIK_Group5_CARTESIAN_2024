<h1 align="center">Robotics 2: Forward and Inverse Kinematics of a Cartesian manipulator</h1>
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
<p align="justify">
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b><i>Forward kinematics</i></b> in a Cartesian manipulator involves determining the position and orientation of the end-effector (tool) based on the lengths of the robot's links and the angles of its joints. By using geometric and trigonometric relationships, the forward kinematics equations can precisely locate where the end-effector is in the Cartesian space. This information is vital for robot control, path planning, and overall system design.
<p align="justify">
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b><i>Inverse kinematics</i></b> on the other hand, deals with finding the joint angles required to position the end-effector at a specific location and orientation. It's a more complex problem as it involves solving nonlinear equations, especially in robots with multiple degrees of freedom. Despite its complexity, inverse kinematics is essential for tasks where precise control over the end-effector's position and orientation is needed, such as in robotic surgery or industrial automation.
<hr> 
<br>

  
## II. Introduction

<p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b><i>Cartesian manipulators</i></b> are made up of a single kinematic linkage chain, with each linear actuator sequentially driving the next one. They do not change the direction of the moving platform. These manipulators are particularly simple to handle because to the close connection between actuator positions and platform coordinates.These manipulators use linear actuators that are mutually perpendicular. Their movement is directly proportional to the X, Y, and Z position coordinates of the moving platform. In other words, they use a standard Cartesian coordinate system. Unimate, the first industrial robot built in the 1950s, is a prime example of this type. Unimate's control axes correspond to a spherical coordinate system with an RRP joint topology (two revolute joints followed by a prismatic joint).
<p align="justify">
  In the context of Cartesian manipulators, elevation refers to movement along the vertical axis, or Z-axis. A Cartesian manipulator executes an elevation movement by changing its vertical position, either raising or lowering its end-effector in relation to the work surface or base. In the context of Cartesian manipulators, extension is defined as movement along one or more additional axes (X and/or Y). This action allows the manipulator to expand or retract horizontally, shifting its location in the X and/or Y directions while remaining elevated (along the Z-axis).  The ability to regulate elevation and extension individually enables efficient and precise handling of three-dimensional objects.

- **Rotation**: The robot can rotate around a vertical axis, which forms the base of the robot. This allows the robot to cover a wide horizontal range around its base.
- **Elevation**: The robot's arm can move up and down in a vertical plane, enabling it to reach different heights.
- **Extension**: The robot's arm can extend or retract, moving closer to or farther from the base.
<br>


## III. Degrees of Freedom
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
  
|  Cartesian Manipulator On Ceiling  | Solution |
|         :---: |     :-----:      |
| <img src=    "> |  $$M = 6n - \sum_{i=1}^m (6-Ci)$$  $$M = 6(3) - [(6-1) + (6-1) + (6-1)]$$  $$M = 18 - (5 + 5 + 5)$$  $$M = 18 - 15$$  $$M = 3$$  <p>&#8756; This is an Under-Actuated Cartesian Manipulator with 3-DOF.</p> |

</div>
<br>


  <p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The illustration above is a simplified diagram of an Cartesian Manipulator On Ceiling . It is also shown above the written computation to get the Degrees of Freedom of Cartesian Manipulator . Degrees of Freedom, as discussed in our classes, is the minimum number of independent parameters or variables or coordinates required to fully describe a system. To get the degrees of freedom for Cartesian Manipulator, the Grubler’s Criterion for Mobility or DOF of Cartesian Manipulator is used as the Cartesian Manipulator is a type of spatial manipulator. Based on the computations above, it can be concluded that this spherical manipulator is an Under-Actuated Spatial Manipulator with three degrees of freedom. 
</p>
<br>



### D-H Frame Assignment
___

 <p align="justify"> 
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b><i>D-H Notation</i></b> was introduced by <b>Jacques Denavit</b> and <b>Richard Hartenberg</b> in <b>1955</b> in order to standardize the coordinate frames for spatial linkages. D-H notation is used to solve the forward kinematics of a mechanical manipulator. The <b><i>Frames</i></b> in a Mechanical Manipulator are used to determine where they are and where they need to go. It also shows the movement of our mechanical manipulator. The frames are positioned at each part of the mechanical manipulator, including the base, joints, and end effector.</p>

#### Three Types of Frames used in Mechanical Manipulator:
  - Base (World) Frame
  - User Frame
  - Tool Frame
<br>

<b><i>D-H Frame Assignment</i></b> follow this rules in assigning frames in a kinematic diagram:
  - **Rule 1**: The z axis must be the axis of rotation for a revolute/twisting joint, or the direction of translation for a prismatic joint.
  - **Rule 2**: The x axis must be perpendicular both to its own Z axis, and the Z axis of the frame before it.
  - **Rule 3**: Each axis must intersect the z axis of the frame before it. The rules for complying rule 3:
      - Rotate the axis until it hits the other.
      - Translate the axis until it hits the other.
  - **Rule 4**: All frames must follow the right hand rule. 
<br>


### Applying D-H Frame Rules to the Kinematic Diagram of a Spherical Manipulator
___

<p align="center">
  <img src="https://github.com/yannaaa23/Robotics2_Midterm_Try/blob/d1ef20c165eca1aaeace5ca92892b76bb5c5f78a/First%20Page/Kinematic%20Diagram%20with%20D-H%20Frame.png" style="height: 300px;"></p>
</div>
<br>

<p align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Following the rules for assigning D-H Frames, we obtained the kinematic diagram with D-H frame assignments shown at the illustration above. First is that the z-axis must be the axis of rotation for a revolute/twisting joint or the direction of translation for a prismatic joint. As observed in the illustration above, all of the blue arrows, which are the z-axis, point in the direction of the axis of rotation for the two revolute joints and the direction of translation for the single prismatic joint. The next rule is the x axis must be perpendicular both to its own z-axis, and the z-axis of the frame before it hence it is seen in the illustration that all the red arrows, an indicator for the x-axis, are all perpendicular to its own z-axis as well as to the z-axis of theframe prior to it. The next rule states that the x axis must be perpendicular to both its own z-axis and the z-axis of the frame preceding it. As can be seen in the illustration, all of the red arrows, which indicate the x-axis, are perpendicular to both its own z-axis and the z-axis of the frame prior to it. The third rule states that each axis must intersect the z-axis of the frame that preceded it. And the rules for complying with this rule are to rotate or translate the axis until it hits the other. Hence, the frame for the prismatic joint were translated into the joint before it so that it will comply with the third rule. The last rule of the D-H frame assignment is that all the frames must follow the right-hand rule. Thus, all the green arrows which indicate the y-axis are drawn with the right-hand rule in mind.
</p>
<br>


<p align="center"> <b>Kinematic Diagram and D-H Frame Tutorial Video</b> </p>
  <p align="center">
  <img src=link alt=Kinematic-Diagram-and-D-H-Frame-Tutorial-Video style="height: 300px; float: left;">
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


### D-H Parametric Table for a Spherical Manipulator
___

<p align="center">
  <img src="https://github.com/t1pen/Robotics2_FKandIK_Group7_SPHERICAL_2024/blob/main/Midterm%20Project/Pictures/Kinematic%20Diagram%20with%20DH%20Frame%20Assignments%20and%20DH%20Parameters.png?raw=true"
" style="height: 300px;"></p>
</div>
<br>

 <p align="justify"> 
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  The figure above is the D-H Parametric table for a Spherical Manipulator. Moreover, a D-H (Denavit-Hartenberg) Parametric Table is a method for organizing the four parameters generated by using the D-H frame assignment rules.  These parameters are useful in determining the kinematic equations of a robotic manipulator. The four parameters are: theta, alpha, r, and d. Theta represents the angle of the joint between the current and next link. For revolute joints, this is the angle of rotation around the frame's z-axis. It is the rotation around z sub n-1 that is required to get x sub n-1 to match x sub n, with the joint variable theta if the joint is a revolute or twisting joint. The alpha represents the offset angle between the z-axis of frame (n-1) and the z-axis of frame (n). For easier calculations, it is commonly set to 0 or 90 degrees. The r represents the distance from the origin of n-1 and n frames along the x-sub-n direction. And lastly, The d refers to the distance from the origin of n-1 and n frames along the z-sub-n-1 direction, with the joint variable if the joint is prismatic. By filling up this table for each link in the manipulator, we will obtain a concise representation of the manipulator's geometry based on these four parameters.  These parameters are then employed in formulas to compute the homogeneous transformation matrices, which ultimately represent the position and orientation of the manipulator's end-effector based on the joint variables.
  </p>
<br>


<p align="center"> <b>D-H Prametric Table Tutorial Video</b> </p>
  <p align="center">
  <img src=link alt=D-H-Parametic-Table-Tutorial-Video style="height: 300px; float: left;">
<br>



## VI. Homogeneous Transformation Matrix

<p align="justify"> 
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  <b><i>Homogeneous Transformation Matrix</i></b> includes both the rotation matrix and the displacement vector in the same matrix. Homogeneous transformation matrices are described as matrices that specify an object's position and orientation. Rotation matrices can be combined using multiplication while Position vectors cannot be added or multiplied. In order to combine position vectors, we shall use the homogeneous transformation matrix denoted as $H_{n}^{n-1}$ or $T_{n}^{n-1}$. The homogeneous transformation matrix contains a superscript and a subscript that indicate the reference frame and projected frame. It is obtained by concatenating 3x3 rotation matrix and 3x1 position vector, resulting in a 3x4 matrix. However, a square matrix is required thus adding an augmentation row is added at the bottom. 
</p>
<br>

<p align="center"> <b>Homogeneous Transformation Matrix Formula</b> </p>

$$
H_{n}^{n-1} =
\begin{bmatrix}
\ Rotation \ (3\times3) & Position \ (3\times1)\\\
0  \ \ \ \ \ \ \ \ \ \ 0 \ \ \ \ \ \ \ \ \ \ \ 0 & 1
\end{bmatrix}
$$
<br>


$$\begin{aligned}
H_{n}^{n-1} = 
\begin{bmatrix} 
  cos\theta_{n} & -sin\theta_{n}cos\alpha_{n} & sin\theta_{n} sin\alpha_{n} & r_{n}cos\theta_{n} 
  \\
  sin\theta_{n} & cos\theta_{n}cos\alpha_{n} & -cos\theta_{n}sin\alpha_{n} & r_{n}sin\theta_{n} 
  \\
  0 & sin\alpha_{n} & cos\alpha_{n} & d_{n} 
  \\
  0 & 0 & 0 & 1 
\end{bmatrix} 
&& or &&
H_{n}^{n-1} = 
\begin{bmatrix} 
  c\theta_{n} & -s\theta_{n}c\alpha_{n} & s\theta_{n} s\alpha_{n} & r_{n}c\theta_{n} 
  \\
  s\theta_{n} & c\theta_{n}c\alpha_{n} &  -c\theta_{n}s\alpha_{n} & r_{n}s\theta_{n}
  \\
  0 & s\alpha_{n} & c\alpha_{n} & d_{n}
  \\
  0 & 0 & 0 & 1
\end{bmatrix}
\end{aligned}$$

<br>
<br>


### Homogeneous Transformation Matrix of a Spherical Manipulator
___


<p align="justify"> 
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; There are two ways to obtain the Homogeneous Transformation Matrix, by manual computation and using the D-H Parametric Table.
</p>
<br>

#### Obtaining the Homogeneous Transformation Matrix Formula Computed Method
  - To obtain $H_{1}^{0}$, concatenate the rotation matrix $r_{1}^{0}$ and the position vector $r_{1}^{0}$, followed by the augmentation column 0 0 0 1 at the bottom that gives us this matrix presented below.

$$
H_{1}^{0} =
\begin{bmatrix} 
  c\theta_{1} & 0 & s\theta_{1} & 0 
  \\
  s\theta_{1} & 0 & -c\theta_{1} & 0
  \\
  0 & 1 & 0 & a_{1}
  \\
  0 & 0 & 0 & 1
\end{bmatrix}
$$

<br>

  - Same as the previous matrix, to get the $H_{2}^{1}$, concatenate the rotation matrix $r_{2}^{1}$ and position vector $p_{2}^{1}$, followed by the augmentation column 0 0 0 1 at the bottom that gives us this matrix presented below. 

$$
H_{2}^{1} =
\begin{bmatrix} 
  -s\theta_{2} & 0 & c\theta_{2} & 0 
  \\
  c\theta_{2} & 0 & s\theta_{2} & 0
  \\
  0 & 1 & 0 & 0
  \\
  0 & 0 & 0 & 1
\end{bmatrix}
$$

<br>

  - Lastly, to obtain $H_{3}^{2}$, concatenate the rotation matrix $r_{3}^{2}$ and the position vector $p_{3}^{2}$, followed by the augmentation column 0 0 0 1 at the bottom that gives us this matrix presented below.

$$
H_{3}^{2} =
\begin{bmatrix} 
  1 & 0 & 0 & 0 
  \\
  0 & 1 & 0 & 0
  \\
  0 & 0 & 1 & a_{2}+a_{3}+d_{3}
  \\
  0 & 0 & 0 & 1
\end{bmatrix}
$$

<br>

  - Finally, to determine the homogeneous transformation matrix from frame 0 (the base frame) to frame 3 (the end-effector), multiply all of the transformation matrices H_{1}^{0}, H_{2}^{1}, and H_{3}^{2} together. Then we can obtain: 

$$
H_{3}^{0} =
H_{1}^{0} \ H_{2}^{1} \ H_{3}^{2}  
\begin{bmatrix} 
  -c\theta_{1}s\theta_{2} & s\theta_{1} & c\theta_{1}c\theta_{2} & c\theta_{1}c\theta_{2}(a_{2}+a_{3}+d_{3})
  \\
  -s\theta_{1}s\theta_{2} & -c\theta_{1} &  s\theta_{1}c\theta_{2} & s\theta_{1}c\theta_{2}(a_{2}+a_{3}+d_{3})
  \\
  -c\theta_{2} & 0 & s\theta_{2} & a_{1}+s\theta_{1}(a_{2}+a_{3}+d_{3})
  \\
  0 & 0 & 0 & 1
\end{bmatrix}
$$

<br>



<p align="center"> <b>Homogeneous Transformation Matrix of a Spherical Manipulator Tutorial Video</b> </p>
  <p align="center">
  <img src=link alt=Homogeneous-Transformation-Matrix-of-a-Spherical-Manipulator-Tutorial-Video style="height: 300px; float: left;">
<br>


