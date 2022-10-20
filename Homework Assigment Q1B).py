import numpy as np
import matplotlib.pyplot as plt

# Design Parameters
# 1 unit of square plot length = 10 units on calculated plot
plate_length = 11 # Compensation for indexing counting from 0 to 11 (total 10)
delta_x = 1 # Each discretized grid space with 0.1 units delta

# Number of iterations
iterations = 15000

# Initialize solution: the grid of u(j, i)
u = np.empty((plate_length, plate_length))

# Boundary conditions
u_top = 1.0
u_left = 0.0
u_bottom = 0.0
u_right = 0.0

# Guess initial conditions for values inside the grids
u_initial = 0

# Set the initial condition
u.fill(u_initial)

# Set the boundary conditions
u[(plate_length-1):, :] = u_top
u[:, :1] = u_left
u[:1, 1:] = u_bottom
u[:, (plate_length-1):] = u_right

# Formula attained from finite difference method
def calculate(u):
    for k in range(0, iterations):
        for j in range(1, plate_length-1, delta_x):
            for i in range(1, plate_length-1, delta_x):
                u[i, j] = (1/4)*(u[i+1, j] + u[i-1, j] + u[i, j+1] + u[i, j-1])
    return u

u = calculate(u)

# Setting color plot
colorinterpolation = 50
colormap = plt.cm.jet

# Converging Contour Plot Solution
plt.contourf(u,colorinterpolation,cmap=colormap) 
plt.title("Converging Contour Plot - Laplace Equation Solution")

# Show color axis, axis and title
plt.colorbar()
plt.xlabel("X (0.1 units)")
plt.ylabel("Y (0.1 units)")

plt.show()