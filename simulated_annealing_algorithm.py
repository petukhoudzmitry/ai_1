import random  # Import random module for generating random numbers
import math  # Import math module for mathematical functions

import plotter
from config import *  # Import configuration parameters
from provider import *  # Import provider functions, including routeLength

# Randomly swap two cities in the route to create a new child route
def swap_cities(route):
    i, j = random.sample(range(len(route)), 2)
    route[i], route[j] = route[j], route[i]
    return route

def main(cities):
    print("SIMULATED ANNEALING ALGORITHM\n" + "_" * 30)

    # Initialize the best route and its length randomly
    bestRoute = np.random.permutation(len(cities)) # Randomly shuffle city indices
    bestLength = routeLength(cities, bestRoute) # Calculate the length of the best route
    currentRoute = np.array(bestRoute) # Set the current route to the best route
    currentLength = routeLength(cities, currentRoute) # Calculate the length of the current route

    # List to track progress of the best routes found
    bestRoutes = [bestRoute]
    progress = []

    # Set the initial temperature for the simulated annealing process
    temperature = INITIAL_TEMPERATURE

    flag = True # Control flag to continue the main loop

    while flag:
        flag = False # Reset the flag for the current iteration

        for i in range(STEPS): # Loop over a defined number of steps
            # Create a new child route by swapping two cities in the current route
            child = swap_cities(np.array(currentRoute))
            childLength = routeLength(cities, child) # Calculate the length of the child route

            # Calculate the difference in length between the child and current routes
            difference = childLength - currentLength

            # Determine whether to accept the new child route
            if difference < 0. or random.random() < math.exp(- difference / temperature):
                currentRoute = np.array(child)
                currentLength = childLength
                flag = True

            # If the current route is better than the best found, update best values
            if currentLength < bestLength:
                bestRoutes.append(currentRoute)
                progress.append(currentLength)
                print(f"Old best value: {bestLength}, New best value: {currentLength}")
                bestLength = currentLength
                bestRoute = np.array(currentRoute)

        # Decrease the temperature
        temperature *= ALPHA

    print(f"Best route: {bestRoute}\nbest length: {bestLength}")
    plotter.plot_evaluation(progress, len(progress), max(progress) + 10, "Simulated Annealing Algorithm Evaluation")

    return bestRoutes