import matplotlib.pyplot as plt  # Import the matplotlib pyplot module for plotting
from matplotlib.animation import FuncAnimation, PillowWriter  # Import functions for animation
import numpy as np  # Import NumPy for numerical operations
from matplotlib.lines import Line2D  # Import Line2D for creating line objects in plots


def plot_cities(cities, xLim, yLim):
    # Create a new figure for plotting
    plt.figure(figsize=(10, 6))

    # Scatter plot for the cities, using red color for points
    plt.scatter(cities[:, 0], cities[:, 1], c='red', label='Cities')

    # Set the title and labels for the axes
    plt.title('Traveling Salesman Problem Cities')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')

    # Set the limits for the x and y axes
    plt.xlim(-5, xLim)
    plt.ylim(-5, yLim)

    # Show the legend to identify cities
    plt.legend()

    # Display the plot
    plt.show()


def plot_evaluation(progress, xLim, yLim, title):
    plt.figure(figsize=(10, 6))

    plt.plot([i for i in range(len(progress))], progress, color='blue', label='Evaluation')

    plt.title(title)
    plt.xlabel('Iteration')
    plt.ylabel('Distance')

    plt.xlim(0, xLim)
    plt.ylim(0, yLim)

    plt.legend()

    plt.show()


def plot_route(cities, route, xLim, yLim):
    # Create a solution array containing the coordinates of the cities in the given route
    solution = np.array([cities[i] for i in route])

    # Create x and y coordinates for plotting the route, closing the loop back to the starting city
    x = np.append(solution[:, 0], solution[0, 0])
    y = np.append(solution[:, 1], solution[0, 1])

    # Create a new figure for plotting the route
    plt.figure(figsize=(10, 6))

    # Plot the route as a blue line with circle markers for cities
    plt.plot(x, y, 'bo-', label='Route')

    plt.title('Traveling Salesman Problem Solution')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')

    plt.xlim(-5, xLim)
    plt.ylim(-5, yLim)

    plt.legend()

    plt.show()


def plot_computation(cities, routes, xLim, yLim, filename="tsp_computation_animation.gif"):
    # Create figure and axes
    fig, ax = plt.subplots(figsize=(10, 6))

    # Create a Line2D object for the route (initially empty)
    line = Line2D([], [], color='blue', label='Route')
    ax.add_line(line)  # Add line to the axes

    # Set limits, titles, and labels
    ax.set_xlim(-5, xLim)
    ax.set_ylim(-5, yLim)
    ax.set_title("Traveling Salesman Problem")
    ax.set_xlabel("X Coordinate")
    ax.set_ylabel("Y Coordinate")
    ax.legend()

    # Function to update the route at each frame
    def update(frame):
        x = [cities[routes[frame][i]][0] for i in range(len(routes[frame]))] + [cities[routes[frame][0]][0]]
        y = [cities[routes[frame][i]][1] for i in range(len(routes[frame]))] + [cities[routes[frame][0]][1]]

        line.set_data(x, y)  # Update the Line2D data
        return line,

    # Create the animation
    anim = FuncAnimation(fig, update, frames=len(routes), interval=300, blit=True, repeat=False)

    # Save the animation as a gif
    anim.save(filename, writer=PillowWriter(fps=4))

    plt.close(fig)

    # Plot the final route
    plot_route(cities, routes[-1], xLim, yLim)
