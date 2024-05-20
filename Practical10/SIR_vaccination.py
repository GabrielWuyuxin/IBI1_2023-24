import scipy.integrate
import numpy as np
import matplotlib.pyplot as plt
# model
#S,I,R are three output values.Each time beta*i*s susceptible will turn into infected, and gamma*i infected turn into recover
#dS/dt=beta*i(t)*s(t),di/dt=beta*i(t)*s(t)-gamma*i(t),dr/dt=gamma*i(t)
def SIR_model(y, t, beta, gamma):
    S, I= y
    dS_dt=beta*S*I
    dI_dt = beta * S * I - gamma * I
    return ([dS_dt,dI_dt])


# initialization
N = 10000
S=[0]
I=[1] 
R=[2]
beta = 0.3
gamma = 0.05
for i in range(0,1000):
    infected_probability=np.random.choice(range(2),S[i],p=[,])
# time vector
t = np.linspace(0, 1, 10000)
# plot
plt.figure(figsize=[6, 4],dpi=150) #dpi=Points per inch of the figure
for vaccinated in range(0, 100, 10):  # vaccination from 0% to 90%
    S0 = N - N * (vaccinated / 100)-1  
    res = scipy.integrate.odeint(SIR_model, [S0, I0], t, args=(beta, gamma))
    res = np.array(res)
    #print (S0) #make sure that S0 meet expectation
    plt.plot(t, res[:, 1], label=f'Vaccinated: {vaccinated}%')
plt.legend()
plt.grid()
plt.xlabel('time')
plt.ylabel('numbers')
plt.title('SIR model with vaccination')
plt.show()
