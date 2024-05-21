import scipy.integrate
import numpy as np
import matplotlib.pyplot as plt
# model

def run_simulation(vaccination_rate):
    # Initial population parameters
    N = 10000
    I0 = 1
    vaccinated = int(N * vaccination_rate)
    beta = 0.3
    gamma = 0.05

    # Arrays to track S, I, R
    S = [N - I0 - vaccinated]
    I = [I0]
    R = [vaccinated]

    # Simulation parameters
    time_steps = 1000

    # Simulation loop
    for t in range(time_steps):
        new_infected = np.random.choice(range(2), S[-1], p=[1-beta*I[-1]/N, beta*I[-1]/N]).sum()
        new_recovered = np.random.choice(range(2), I[-1], p=[1-gamma, gamma]).sum()

        S.append(S[-1] - new_infected)
        I.append(I[-1] + new_infected - new_recovered)
        R.append(R[-1] + new_recovered)

    return S, I, R

# Run simulations for different vaccination rates
vaccination_rates=[]
for i in range(0, 100, 10):
    vaccination_rates.append(i / 100)
for rate in vaccination_rates:
    S, I, R = run_simulation(rate)
    plt.plot(I, label=f'{rate*100}% vaccinated')

# plot
plt.legend()
plt.grid()
plt.xlabel('time')
plt.ylabel('numbers')
plt.title('SIR model simulation')
plt.show()
