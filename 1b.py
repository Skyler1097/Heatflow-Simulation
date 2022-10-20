import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv

# Design Parameters
# 1 unit of square plot length = 25 units on calculated plot
plate_length = 11
delta_x = 1 # Each discretized grid space with 0.25 units delta

# Boundary/ RHS matrix
b = np.empty((plate_length-2,1))
for i in range(len(b)):
    if (i < (plate_length-5)):
        b[i,0] = 0
    else:
        b[i,0] = 1

# Force matrix for triangular matrix
f = np.empty((plate_length-2, plate_length-2))

for i in range((plate_length-2)):
    for j in range((plate_length-2)):
        f[i,j] = 0

# Creating diagonal coefficients matrix
j = 0
for i in range((plate_length-2)):
    f[i, j] = 4
    j+=1

j = 1
for i in range(plate_length-3):
    if i == 2 or i == 5:
        f[i,j] = 0
        j += 1
    else:
        f[i,j] = -1
        j += 1

j = 0
for i in range(plate_length-3):
    if i == 2 or i ==5:
        f[i+1, j] = 0
        j+=1
    else:
        f[i+1, j] = -1
        j+=1

j = 0
for i in range(plate_length-5):
    f[i+3, j] = -1
    j+=1

j = 3
for i in range(plate_length-5):
    f[i,j] = -1
    j+=1

# Matrix inversion calculation and results evaluation
r = inv(np.matrix(f)) * np.matrix(b)

# Computation of final matrix to be processed
row = [0]
results = []

## Applying boundary conditions
first_row = [0,0,0,0,0]
final_row = [0,1.0,1.0,1.0,0]

results.append(first_row)

for i in range(3):
    row.append(float(r[i]))
row.append(0)
results.append(row)

row = [0]

for i in range(3,6):
    row.append(float(r[i]))
row.append(0)
results.append(row)

row = [0]

for i in range(6,9):
    row.append(float(r[i]))
row.append(0)
results.append(row)
results.append(final_row)

results = np.matrix(results)

# Setting color plot
colorinterpolation = 50
colormap = plt.cm.jet

plt.contourf(results ,colorinterpolation,cmap=colormap) 
plt.title("Converging Contour Plot - Laplace Equation Solution")

# # Show color axis, axis and title
plt.colorbar()
plt.xlabel("X (0.25 units)")
plt.ylabel("Y (0.25 units)")

plt.show()