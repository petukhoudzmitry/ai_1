# Import necessary modules
import provider # Module for generating cities and computing routes
import genetic_algorithm # Module implementing the genetic algorithm for solving TSP
import simulated_annealing_algorithm # Module implementing simulated annealing for TSP
from config import MAP_SIZE # Configuration for map size
from plotter import * # Import all plotting functions

# Generate cities using the provider module
cities = provider.generateCities()

def main():
    print(f"Cities: {len(cities)} - {cities}")

    plot_cities(cities, MAP_SIZE + 10, MAP_SIZE + 10)
    plot_route(cities, [i for i in range(len(cities))], MAP_SIZE + 10, MAP_SIZE + 10)

    plot_computation(cities, genetic_algorithm.main(cities), MAP_SIZE + 10, MAP_SIZE + 10,"genetic_algorithm.gif")
    plot_computation(cities, simulated_annealing_algorithm.main(cities), MAP_SIZE + 10, MAP_SIZE + 10, "simulated_annealing_algorithm.gif")

if __name__ == '__main__':
    main()