from tkinter import * 
from tkinter import messagebox
from tkinter import PhotoImage
import numpy as np
import math
import roboticstoolbox as rtb
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH
import spatialmath
from spatialmath import SE3
import matplotlib
matplotlib.use('TkAgg')
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/yuel/Desktop/CARTESIAN/GUI/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.geometry("1100x700")
window.configure(bg = "#005B8F")

canvas = Canvas(
    window,
    bg="#005B8F",
    height=700,
    width=1100,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    580.0,
    528.0,
    image=image_image_1
)

canvas.create_rectangle(
    8.0,
    8.0,
    1090.0,
    124.0,
    fill="#001B63",
    outline="")

canvas.create_text(
    466.0,
    147.0,
    anchor="nw",
    text="Link lengths",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 32 * -1)
)

canvas.create_rectangle(
    438.0,
    204.0,
    481.0,
    232.0,
    fill="#0047FF",
    outline="")

canvas.create_rectangle(
    438.0,
    309.0,
    481.0,
    337.0,
    fill="#0047FF",
    outline="")

canvas.create_rectangle(
    438.0,
    274.0,
    481.0,
    302.0,
    fill="#0047FF",
    outline="")

canvas.create_rectangle(
    438.0,
    239.0,
    481.0,
    267.0,
    fill="#0047FF",
    outline="")

canvas.create_text(
    495.0,
    199.0,
    anchor="nw",
    text="=",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 32 * -1)

)


tbox1 = canvas.create_text(
    495.0,
    304.0,
    anchor="nw",
    text="=",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 32 * -1)
)

canvas.create_text(
    495.0,
    269.0,
    anchor="nw",
    text="=",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 32 * -1)
)

canvas.create_text(
    495.0,
    234.0,
    anchor="nw",
    text="=",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 32 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    587.0,
    218.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=527.0,
    y=204.0,
    width=120.0,
    height=26.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    587.0,
    323.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=527.0,
    y=239.0,
    width=120.0,
    height=26.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    587.0,
    288.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=527.0,
    y=274.0,
    width=120.0,
    height=26.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    587.0,
    253.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=527.0,
    y=309.0,
    width=120.0,
    height=26.0
)

canvas.create_rectangle(
    747.0,
    433.0,
    790.0,
    461.0,
    fill="#0047FF",
    outline="")

canvas.create_rectangle(
    747.0,
    503.0,
    790.0,
    531.0,
    fill="#0047FF",
    outline="")

canvas.create_rectangle(
    747.0,
    468.0,
    790.0,
    496.0,
    fill="#0047FF",
    outline="")

canvas.create_text(
    805.0,
    428.0,
    anchor="nw",
    text="=",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 32 * -1)
)

canvas.create_text(
    805.0,
    498.0,
    anchor="nw",
    text="=",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 32 * -1)
)

canvas.create_text(
    805.0,
    463.0,
    anchor="nw",
    text="=",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 32 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    896.0,
    447.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=836.0,
    y=433.0,
    width=120.0,
    height=26.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    896.0,
    517.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=836.0,
    y=503.0,
    width=120.0,
    height=26.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    896.0,
    482.0,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=836.0,
    y=468.0,
    width=120.0,
    height=26.0
)

canvas.create_rectangle(
    137.0,
    437.0,
    180.0,
    465.0,
    fill="#0047FF",
    outline="")

canvas.create_rectangle(
    137.0,
    507.0,
    180.0,
    535.0,
    fill="#0047FF",
    outline="")

canvas.create_rectangle(
    137.0,
    472.0,
    180.0,
    500.0,
    fill="#0047FF",
    outline="")

canvas.create_text(
    195.0,
    432.0,
    anchor="nw",
    text="=",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 32 * -1)
)

canvas.create_text(
    195.0,
    502.0,
    anchor="nw",
    text="=",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 32 * -1)
)

canvas.create_text(
    195.0,
    467.0,
    anchor="nw",
    text="=",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 32 * -1)
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    286.0,
    451.0,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=226.0,
    y=507.0,
    width=120.0,
    height=26.0
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    286.0,
    521.0,
    image=entry_image_9
)
entry_9 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_9.place(
    x=226.0,
    y=437.0,
    width=120.0,
    height=26.0
)

entry_image_10 = PhotoImage(
    file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(
    286.0,
    486.0,
    image=entry_image_10
)
entry_10 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_10.place(
    x=226.0,
    y=472.0,
    width=120.0,
    height=26.0
)

canvas.create_text(
    712.0,
    382.0,
    anchor="nw",
    text="Joint Variable",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 32 * -1)
)

canvas.create_text(
    150.0,
    382.0,
    anchor="nw",
    text="Position Vector",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 32 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    239.0,
    267.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    875.0,
    266.0,
    image=image_image_3
)

text = "CartesianManipulator"
font = ("Kodchasan Medium", 45)
x, y = 230.0, 20.0 
for char in text:
    if char in ['C', 'M']:
        color = 'red'
    else:
        color = '#FFFFFF'

    text_id = canvas.create_text(x, y, anchor="nw", text=char, fill=color, font=font)
    bbox = canvas.bbox(text_id)
    text_width = bbox[2] - bbox[0]
    x += text_width


canvas.create_text(
    447.0,
    205.0,
    anchor="nw",
    text="a1",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    447.0,
    274.0,
    anchor="nw",
    text="a3",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    447.0,
    308.0,
    anchor="nw",
    text="a4",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    447.0,
    240.0,
    anchor="nw",
    text="a2",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    650.0,
    206.0,
    anchor="nw",
    text="cm",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    352.0,
    440.0,
    anchor="nw",
    text="cm",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    352.0,
    510.0,
    anchor="nw",
    text="cm",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    352.0,
    475.0,
    anchor="nw",
    text="cm",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    960.0,
    439.0,
    anchor="nw",
    text="cm",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    960.0,
    509.0,
    anchor="nw",
    text="cm",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    960.0,
    474.0,
    anchor="nw",
    text="cm",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    650.0,
    314.0,
    anchor="nw",
    text="cm",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    650.0,
    278.0,
    anchor="nw",
    text="cm",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    650.0,
    242.0,
    anchor="nw",
    text="cm",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    146.0,
    438.0,
    anchor="nw",
    text="X",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    146.0,
    507.0,
    anchor="nw",
    text="Z",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    146.0,
    473.0,
    anchor="nw",
    text="Y",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    350.0,
    89.0,
    anchor="nw",
    text="Forward and Reverse Kinematics Calculator",
    fill="#FFFFFF",
    font=("Commissioner Regular", 20 * -1)
)

canvas.create_text(
    763.0,
    435.0,
    anchor="nw",
    text="d1",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    763.0,
    470.0,
    anchor="nw",
    text="d2",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    763.0,
    504.0,
    anchor="nw",
    text="d3",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)


def f_k():

    # link lengths in cm
    a1 = float(entry_1.get())/100
    a2 = float(entry_2.get())/100
    a3 = float(entry_3.get())/100
    a4 = float(entry_4.get())/100

    # joint variables: is mm if f, is degrees if theta
    d1 = float(entry_5.get())/100
    d2 = float(entry_6.get())/100
    d3 = float(entry_7.get())/100

    # Parametric Table (theta, alpha, r, d)
    PT = [[(0.0/180.0)*np.pi,(270.0/180.0)*np.pi,0,a1],
         [(270.0/180.0)*np.pi,(270.0/180.0)*np.pi,0,a2+d1],
         [(90.0/180.0)*np.pi,(270.0/180.0)*np.pi,0,a3+d2],
         [(0.0/180.0)*np.pi,(0.0/180.0)*np.pi,0,a4+d3]]
    
    # HTM formulae
    i = 0
    H0_1 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
        [0,0,0,1]]
    
    i = 1
    H1_2 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
        [0,0,0,1]]
    
    i = 2
    H2_3 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
        [0,0,0,1]]
    
    i = 3
    H3_4 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
        [0,0,0,1]]
    
    H0_1 = np.matrix(H0_1)
    H1_2 = np.matrix(H1_2)
    H2_3 = np.matrix(H2_3)
    H3_4 = np.matrix(H3_4)
    
    H0_2 = np.dot(H0_1,H1_2)
    H2_4 = np.dot(H2_3,H3_4)
    H0_4 = np.dot(H0_2,H2_4)
    
    X0_4 = H0_4[0,3]
    entry_10.delete(0,END)
    entry_10.insert(0,np.around(X0_4*100,3))
    
    Y0_4 = H0_4[1,3]
    entry_9.delete(0,END)
    entry_9.insert(0,np.around(Y0_4*100,3))
    
    Z0_4 = H0_4[2,3]
    entry_8.delete(0,END)
    entry_8.insert(0,np.around(Z0_4*100,3))



    # [robot_variable]=DHRobot([RevoluteDH(d,r,alpha,offset)])
    # Create Links
    CARTESIAN = DHRobot([
            PrismaticDH(0,0,(270.0/180.0)*np.pi,a1,qlim=[0,0]),
            PrismaticDH((270.0/180.0)*np.pi,0,(270.0/180.0)*np.pi,a2,qlim=[0,(30/100)]),
            PrismaticDH((90.0/180.0)*np.pi,0,(270.0/180.0)*np.pi,a3,qlim=[0,(30/100)]),
            PrismaticDH(0,0,(0.0/180.0)*np.pi,a4,qlim=[0,(30/100)])
            ], name='CARTESIAN')
    
    

    # plot joints
    q1 = np.array([0,d1,d2,d3])

    #plot scale
    x1 = -.5
    x2 = .5
    y1 = -.5
    y2 = .5
    z1 = 0.0
    z2 = .5

    # Plot commands
    CARTESIAN.plot(q1,limits=[x1,x2,y1,y2,z1,z2],block=True)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    text="Forward",
    compound="center",
    fg="white",
    font=("LibreBodoniRoman Regular", 24 * -1),
    borderwidth=0,
    highlightthickness=0,
    command=f_k,
    relief="flat"
)
button_2.place(
    x=745.0,
    y=577.0,
    width=255.0,
    height=64.0
)

def i_k():
    #Inverse Kinematics Using Graphical Method

    #link lengths in cm
    a1 =float(entry_1.get())
    a2 =float(entry_2.get())
    a3 =float(entry_3.get())
    a4 =float(entry_4.get())

    #Position Vector in cm
    xe = float(entry_8.get())
    ye = float(entry_9.get())
    ze = float(entry_10.get())

    # To solve for D2
    d2 = xe-a3
    
    # To solve for D3
    d3 = a1-a4-ze
    
    # To solve for D1
    d1 = ye-a2


    entry_7.delete(0,END)
    entry_7.insert(0,np.around(d1,3))

    entry_6.delete(0,END)
    entry_6.insert(0,np.around(d2,3))

    entry_5.delete(0,END)
    entry_5.insert(0,np.around(d3,3))

    # Create Links (d,r,alpha,offset)
    
    
    CARTESIAN = DHRobot([
            PrismaticDH(0,0,(270.0/180.0)*np.pi,a1,qlim=[0,0]),
            PrismaticDH((270.0/180.0)*np.pi,0,(270.0/180.0)*np.pi,a2,qlim=[0,(30/100)]),
            PrismaticDH((90.0/180.0)*np.pi,0,(270.0/180.0)*np.pi,a3,qlim=[0,(30/100)]),
            PrismaticDH(0,0,(0.0/180.0)*np.pi,a4,qlim=[0,(30/100)])
            ], name='CARTESIAN')
    
     # plot joints
    q1 = np.array([0,d1/100,d2/100,d3/100])

    #plot scale
    x1 = -5
    x2 = 5
    y1 = -5
    y2 = 5
    z1 = 0.0
    z2 = 5

     # Plot commands
    CARTESIAN.plot(q1,limits=[x1,x2,y1,y2,z1,z2],block=True)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    text="Inverse",
    compound="center",
    fg="white",
    font=("LibreBodoniRoman Regular", 24 * -1),
    borderwidth=0,
    highlightthickness=0,
    command=i_k,
    relief="flat"
)
button_1.place(
    x=115.0,
    y=577.0,
    width=255.0,
    height=64.0
)



def reset():
    
    entry_1.delete(0,END)
    entry_2.delete(0,END)
    entry_3.delete(0,END)
    entry_4.delete(0,END)
    entry_5.delete(0,END)
    entry_6.delete(0,END)
    entry_7.delete(0,END)
    entry_8.delete(0,END)
    entry_9.delete(0,END)
    entry_10.delete(0,END)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    text="Reset",
    compound="center",
    fg="white",
    font=("LibreBodoniRoman Regular", 24 * -1),
    borderwidth=0,
    highlightthickness=0,
    command=reset,
    relief="flat"
)



button_3.place(
    x=429.0,
    y=464.0,
    width=255.0,
    height=64.0
)
window.resizable(False, False)
window.mainloop()

