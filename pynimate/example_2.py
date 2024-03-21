import numpy as np
import matplotlib.pyplot as plt
import pynimate

# Define the x and y data
x = np.linspace(0, 2*np.pi, 200)
y = np.sin(x)

# Create the figure and axis objects
fig, ax = plt.subplots()

# Plot the initial sine wave
line, = ax.plot(x, y)

# Define the update function
def update(frame):
    # Shift the sine wave to the right by one unit every frame
    new_y = np.sin(x + frame/10)
    line.set_ydata(new_y)
    return [line]

# Create the animation loop
for i in range(100):
    # Update the data and redraw the plot
    update(i)
    plt.draw()
    plt.pause(0.01)

# Keep the plot window open
plt.show()
