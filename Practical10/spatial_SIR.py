import numpy as np
import matplotlib.pyplot as plt

# Initialize a 100x100 grid with all populations as susceptible (value 0)
population = np.zeros((100, 100))

# Randomly select a location as the initial infection point
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1  # Set the initial infection point
# set up parameters
beta = 0.3  # infected probability
gamma = 0.05  # recover probability
time_steps = 100  # Simulated time steps

for t in range(time_steps):
    # Find an index of all infected points
    infectedIndex = np.where(population == 1)
    
    # Create a new grid to update the population status
    new_population = population.copy()
    
    # Go through all the infection points
    for i in range(len(infectedIndex[0])):
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        
        # Infect the surrounding neighborhood points
        for xNeighbour in range(x-1, x+2):
            for yNeighbour in range(y-1, y+2):
                if (xNeighbour, yNeighbour) != (x, y):
                    if 0 <= xNeighbour < 100 and 0 <= yNeighbour < 100:
                        if population[xNeighbour, yNeighbour] == 0:
                            new_population[xNeighbour, yNeighbour] = np.random.choice([0, 1], p=[1-beta, beta])
    
    # Update the status of infected persons to recovered
    for i in range(len(infectedIndex[0])):
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        if np.random.random() < gamma:
            new_population[x, y] = 2
    
    # Update population status
    population = new_population.copy()
    
    # Draw the current state every 10 time steps
    if t % 10 == 0:
        plt.figure(figsize=(6, 4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f'Time Step {t}')
        plt.show()
