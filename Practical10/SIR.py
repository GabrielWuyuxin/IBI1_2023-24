import scipy.integrate
import numpy as np
import matplotlib.pyplot as plt
# model
# initialization
N=10000 #number of people
I0 = 1 #number of people, the initial infected
R0 = 0 #number of people
beta = 0.3
gamma = 0.05

# Arrays to track S, I, R
S = [N - I0]
I = [I0]
R = [0]

# Simulation parameters
time_steps = 1000

# Simulation loop
for t in range(time_steps):
    new_infected = np.random.choice(range(2), S[-1], p=[1-beta*I[-1]/N, beta*I[-1]/N]).sum()
    new_recovered = np.random.choice(range(2), I[-1], p=[1-gamma, gamma]).sum()

    S.append(S[-1] - new_infected)
    I.append(I[-1] + new_infected - new_recovered)
    R.append(R[-1] + new_recovered)




# plot
plt.figure(figsize=[8, 4],dpi=150) #dpi=Points per inch of the figure
plt.plot(S, label='Susceptible')
plt.plot(I, label='Infected')
plt.plot(R, label='Recovered')
plt.legend()
plt.grid()
plt.xlabel('time')
plt.ylabel('numbers')
plt.title('SIR model simulation')
plt.show()

