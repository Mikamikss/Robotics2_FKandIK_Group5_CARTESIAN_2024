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

  <p align="center">
  <img src=https://github.com/MEXECardenas/SPHERICAL_G7_Assignment_2024/blob/0b0c965065028159e971cf92570e9344e1e41f4b/Kinematic%20Diagrams%20with%20D-H%20Parametric%20Tables/Spherical%20Manipulator%20-%20Modern%20Variant.png alt=Spherical-Manipulator-Modern-Variant style="height: 300px; float: left;">
  <img src=https://github.com/MEXECardenas/SPHERICAL_G7_Assignment_2024/blob/a9a0b089f3911adfcc915ab37b061117838ae024/Kinematic%20Diagrams%20with%20D-H%20Parametric%20Tables/Spherical%20Manipulator%20(Modern%20Variant).gif alt=Spherical-Manipulator-(Modern-Variant) style="height: 300px; float: right;">
  </p>
</div>
<br>

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
  
|  RRP Spherical Manipulator  | Solution |
|         :---: |     :-----:      |
| <img src="> |  $$M = 6n - \sum_{i=1}^m (6-Ci)$$  $$M = 6(3) - [(6-1) + (6-1) + (6-1)]$$  $$M = 18 - (5 + 5 + 5)$$  $$M = 18 - 15$$  $$M = 3$$  <p>&#8756; This is an Under-Actuated Spatial Manipulator with 3-DOF.</p> |

</div>
<br>


  <p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The illustration above is a simplified diagram of an RRP Spherical Manipulator. It is also shown above the written computation to get the Degrees of Freedom of Spherical Manipulator. Furthermore, a Spherical Manipulator is a robot or manipulator with two rotational joints and one prismatic joint and it is commonly used on industries that involves material handling and welding. Meanwhile, Degrees of Freedom, as discussed in our classes, is the minimum number of independent parameters or variables or coordinates required to fully describe a system. To get the degrees of freedom for spherical manipulator, the Grubler’s Criterion for Mobility or DOF of Spatial Manipulator is used as the spherical manipulator is a type of spatial manipulator. Based on the computations above, it can be concluded that this spherical manipulator is an Under-Actuated Spatial Manipulator with three degrees of freedom. 
</p>
<br>



## IV. Kinematic Diagram and D-H Frame
  <p align="center">
  <img src=https://github.com/yannaaa23/Robotics2_Midterm_Try/blob/6b1f57110fecfee109d07f42817c1e87ddae8e89/First%20Page/Kinematic%20Diagram.png alt=Spherical-Manipulator-Kinematic-Diagram style="height: 300px;">
  </div>
<br>

  <p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A <b><i>Kinematic Diagram</i></b> is a simplified representation of a mechanism that illustrates the motion of all the components without showing the forces or the physical dimensions that cause the motion. It is an important tool used in mechanical engineering to examine the motion of mechanisms. Typically, the diagram shows the mechanism's joints and links in schematic form. It is also a diagram that shows how the links and joints are connected together when all of the joint variables have a value of 0.
</p>
<br>

<div align="center">
  
<table border="1">
  <tr>
    <th colspan="2">Joint Variables</th>
  </tr>
  <tr>
    <td> <p align="center">Twisting or Revolute Joint</p> </td>
    <td> <p align="center">Prismatic Linear or Orthogonal Joints</p> </td>
  </tr>
  <tr>
    <td><img src=https://github.com/yannaaa23/Robotics2_Midterm_Try/blob/af546ee69ca1e190b12295380745505086c36d6b/First%20Page/Twisting%20or%20Revolute%20Joint.png alt=Twisting-or-Revolute-Joint style="height: 230px; float: left;"></td>
    <td><img src=https://github.com/yannaaa23/Robotics2_Midterm_Try/blob/af546ee69ca1e190b12295380745505086c36d6b/First%20Page/Prismatic%20Linear%20or%20Orthoganal%20Joint.png alt=Prismatic-Linear-or-Orthogonal-Joints style="height: 200px; float: left;"></td></td>
  </tr>
</table>
</div>
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
  <img src="https://github.com/yannaaa23/Robotics2_Midterm_Try/blob/d1ef20c165eca1aaeace5ca92892b76bb5c5f78a/First%20Page/Kinematic%20Diagram%20with%20D-H%20Frame.png"
" style="height: 300px;"></p>

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

