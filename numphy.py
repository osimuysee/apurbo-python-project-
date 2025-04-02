# import numpy as np

# # Create a NumPy array from a list
# arr = np.array([1, 2, 3, 4, 5])

# print("NumPy Array:", arr)
# import numpy as np

# # Create two NumPy arrays
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])

# # Add the arrays
# sum_arr = arr1 + arr2

# # Multiply the arrays
# product_arr = arr1 * arr2

# print("Sum of arrays:", sum_arr)
# print("Product of arrays:", product_arr)

# import numpy as np

# # Create a NumPy array
# arr = np.array([10, 20, 30, 40, 50])

# # Calculate the sum and mean
# sum_arr = np.sum(arr)
# mean_arr = np.mean(arr)

# print("Sum of Array:", sum_arr)
# # print("Mean of Array:", mean_arr)
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# # Create the figure and axis
# fig, ax = plt.subplots()

# # Set the axis limits
# ax.set_xlim(0, 2 * np.pi)
# ax.set_ylim(-1.5, 1.5)

# # Create a line object that we will update
# line, = ax.plot([], [], lw=2)

# # Initialization function: This will run once at the start
# def init():
#     line.set_data([], [])
#     return line,

# # Update function: This is called at each frame of the animation
# def update(frame):
#     x = np.linspace(0, 2 * np.pi, 1000)
#     y = np.sin(x + frame / 10.0)  # Animate the sine wave
#     line.set_data(x, y)
#     return line,

# # Create the animation
# ani = FuncAnimation(fig, update, frames=100, init_func=init, blit=True)

# # Show
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a grid of values (for example, latitude and longitude)
x = np.linspace(-180, 180, 360)
y = np.linspace(-90, 90, 180)
X, Y = np.meshgrid(x, y)

# Function to generate random isobar values for animation
def generate_isobar_values(t):
    return np.sin(X * 0.1 + t) * np.cos(Y * 0.1 + t)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Create the initial contour plot
Z = generate_isobar_values(0)
cp = ax.contour(X, Y, Z, levels=10, cmap='coolwarm')

# Function to update the contour plot for each frame of the animation
def update(t):
    ax.clear()
    Z = generate_isobar_values(t)
    cp = ax.contour(X, Y, Z, levels=10, cmap='coolwarm')
    ax.set_title('Isobar Animation')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')

# Create the animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 10, 100), interval=100)

plt.show()



