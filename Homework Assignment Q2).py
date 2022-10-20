import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

# Design Parameters
# 1 unit of square plot length = 10 units on calculated plot
plate_length = 11 # Compensation for indexing counting from 0 to 11 (total 10)
delta_x = 1 # Each discretized grid space with 0.1 units delta

# Each iteration represent each dt that passes
delta_t = 0.01
iterations = 150

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

# Neumann Boundary Condition
## Using backward differencing: u[i,j] = u[i-1,j]
### Implementation further in the code

# Set the initial condition
u.fill(u_initial)

# Set the boundary conditions
u[:, (plate_length-1):, :] = u_top
u[:, :, :1] = u_left
u[:, :1, 1:] = u_bottom

# Formula attained from finite difference method
def calculate(u):
    for k in range(0, iterations-1, 1):
        for j in range(1, plate_length-1, delta_x):
            for i in range(1, plate_length-1, delta_x):

                # Calculation for Neumann boundary condition of right side of plate
                if i == plate_length-2:
                    # u[k+1, j, i+1] = u[k+1, j, i]
                    u[k+1, j, i+1] = (4*u[k, j, i] - u[k, j, i-1])/3
                else:
                    pass
                u[k+1, j, i] = gamma * (u[k][j+1][i] + u[k][j-1][i] + u[k][j][i+1] + u[k][j][i-1] - 4*u[k][j][i]) + u[k][j][i]
    return u

### Animated solution plots
def plotheatmap(u, k):
    # Clear the current plot figure
    plt.clf()

    colorinterpolation = 50
    colormap = plt.cm.jet

    plt.title(f"Contour Plot; When t = {k*delta_t:.3f} unit time")
    plt.xlabel("X (0.1 units)")
    plt.ylabel("Y (0.1 units)")

    # This is to plot u_k (u at time-step k)
    plt.contourf(u[k],colorinterpolation,cmap=colormap)
    plt.colorbar()

u = calculate(u)

def animate(k):
    plotheatmap(u,k)

anim = animation.FuncAnimation(plt.figure(), animate, interval=1, frames=iterations, repeat=False)
anim.save("heat_equation_solution.gif")

### Static solution plots
# Setting color plot
# colorinterpolation = 50
# colormap = plt.cm.jet

# Contour plot when t = 0.01
# plt.contourf(u[1],colorinterpolation,cmap=colormap)
# plt.title("Contour Plot; When t=0.01s")

# Contour plot when t = 0.1s
# plt.contourf(u[10],colorinterpolation,cmap=colormap) 
# plt.title("Contour Plot; When t=0.1s")

# Converging contour plot when t = 150s
# plt.contourf(u[14999],colorinterpolation,cmap=colormap)
# plt.title("Converging Contour Plot; When t=150s")

# Show color axis, axis and title
# plt.colorbar()
# plt.xlabel("X (0.1 units)")
# plt.ylabel("Y (0.1 units)")

# plt.show()