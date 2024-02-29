import numpy as np

a1 = float(input('a1 ='))
a2 = float(input('a2 ='))
a3 = float(input('a3 ='))
a4 = float(input('a4 ='))
xe = float(input('X ='))
ye = float(input('Y ='))
ze = float(input('Z ='))

# To solve for D2
d2 = xe - a3

# To solve for D3
d3 = a1 - a4 - ze

# To solve for D4
d1 = ye - a2

print("d2 =", np.around(d2,3))
print("d3 =", np.around(d3,3))
print("d1 =", np.around(d1,3))
