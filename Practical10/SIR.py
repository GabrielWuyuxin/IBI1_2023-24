import scipy.integrate
import numpy as np
import matplotlib.pyplot as plt
# model
#S,I,R are three output values.Each time beta*i*s susceptible will turn into infected, and gamma*i infected turn into recover
#dS/dt=beta*i(t)*s(t),di/dt=beta*i(t)*s(t)-gamma*i(t),dr/dt=gamma*i(t)
def SIR_model(y, t, beta, gamma):
    S, I, R = y
    dS_dt = -beta * S * I
    dI_dt = beta * S * I - gamma * I
    dR_dt = gamma * I
    return ([dS_dt, dI_dt, dR_dt])


# initialization
S0 =9999 #number of people
I0 = 1 #number of people
R0 = 0 #number of people
beta = 0.3
gamma = 0.05

# time vector
t = np.linspace(0, 1, 10000)
# result
res = scipy.integrate.odeint(SIR_model, [S0, I0, R0], t, args=(beta, gamma))
res = np.array(res)
# plot
plt.figure(figsize=[8, 4],dpi=150) #dpi=Points per inch of the figure
plt.plot(t, res[:, 0], label='S(t)')
plt.plot(t, res[:, 1], label='I(t)')
plt.plot(t, res[:, 2], label='R(t)')
plt.legend()
plt.grid()
plt.xlabel('time')
plt.ylabel('numbers')
plt.title('SIR model simulation')
plt.show()

