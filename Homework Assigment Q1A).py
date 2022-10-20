import numpy as np
import matplotlib.pyplot as plt

# Design Parameters
# 1 unit of square plot length = 10 units on calculated plot
plate_length = 11 # Compensation for indexing counting from 0 to 11 (total 10)
delta_x = 1 # Each discretized grid space with 0.1 units delta

# Each iteration represent each dt that passes
delta_t = 0.01
iterations = 15000

# After manipulation of given equation: let gamma be dt/(dx^2)
gamma = (delta_t) / (delta_x ** 2)

# Initialize solution: Creating the grid of u(k, j, i) 
u = np.empty((iterations, plate_length, plate_length))

# Initial condition everywhere inside the grid
u_initial = 0

# Dirichlet Boundary conditions
u_top = 1.0
u_left = 0.0
u_bottom = 0.0
u_right = 0.0

# Set the initial condition
u.fill(u_initial)

# Set the boundary conditions
u[:, (plate_length-1):, :] = u_top
u[:, :, :1] = u_left
u[:, :1, 1:] = u_bottom
u[:, :, (plate_length-1):] = u_right

# Formula attained from finite difference method
def calculate(u):
    for k in range(0, iterations-1, 1):
        for j in range(1, plate_length-1, delta_x):
            for i in range(1, plate_length-1, delta_x):
                u[k+1, i, j] = gamma * (u[k][i+1][j] + u[k][i-1][j] + u[k][i][j+1] + u[k][i][j-1] - 4*u[k][i][j]) + u[k][i][j]
    return u

u = calculate(u)

# Setting color plot
colorinterpolation = 50
colormap = plt.cm.jet

# Contour plot when t = 0.01
# plt.contourf(u[1],colorinterpolation,cmap=colormap)
# plt.title("Contour Plot; When t=0.01s")

# Contour plot when t = 0.1s
# plt.contourf(u[10],colorinterpolation,cmap=colormap) 
# plt.title("Contour Plot; When t=0.1s")

# Converging contour plot when t = 150s
plt.contourf(u[14999],colorinterpolation,cmap=colormap) 
plt.title("Converging Contour Plot; When t=150s")

# Show color axis, axis and title
plt.colorbar()
plt.xlabel("X (0.1 units)")
plt.ylabel("Y (0.1 units)")

plt.show()