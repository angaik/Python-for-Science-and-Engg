# CSTR MASS BALANCE
# Assumptions:
# 1. Reaction A -> B with rate of reaction = 1.
# 2. Using solve_ivp

from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

# [CSTR example](https://www.youtube.com/watch?v=CqjI-oJBpoU)

# Define CSTR mass balance
def cstr_mass_bal(t,x,q,q_f,cA_f,T_f):
    # Inputs (4):
    # q_f : Inlet volumetric flowrate (lit/min)
    # q   : Outlet volumetric flowrate (lit/min)
    # cA_f: Feed concentration (mol/lit)
    # T_f : Feed temperature (K)

    # States (3):
    # Volume (lit), Concentration of A (mol/lit), Temperature (K)
    V, cA, T = x

    # Parameters:
    # Reaction
    rA = 1

    # Differential eqns for the three variables
    # ODE for volume
    dVdt = q_f - q 
    
    # ODE for concentration of A
    dcAdt = ((q_f*cA_f)-(q*cA))/V - rA - ((cA/V)*dVdt)

    # ODE for temperature
    dTdt = ((q_f*T_f) - (q*T))/V - (T*dVdt/V)

    # Return derivatives
    return [dVdt, dcAdt, dTdt]

# Initial conditions for the states
V_0 = 1
cA_0 = 0
T_0 = 350

# Initial State vector
y_0 = [V_0,cA_0,T_0]

## INITIALIZE SOLUTION
# Time interval (min)
t = np.linspace(0,10,100)

# Inlet volumetric flowrate (lit/min)
q_f = np.ones(len(t)) * 5.2
q_f [50:] = 5.1     # Changing vol flow after 50th time-point

# Outlet volumetric flowrate (lit/min)
q = np.ones(len(t)) * 5

# Feed concentration (mol/lit)
cA_f = np.ones(len(t)) * 1.0
cA_f[30:] = 0.5     # Changing feed concentration after 30th time-point

# Feed temperature (K)
T_f = np.ones(len(t)) * 300
T_f[70:] = 325      # Changing feed temperature after 70th time-point

# Storage for results [V, cA, T]
V = np.ones(len(t)) * V_0
cA = np.ones(len(t)) * cA_0
T = np.ones(len(t)) * T_0

## ACTUAL SOLUTION LOOP

# Loop through each time-step
for i in range(len(t)-1):
    # Simulate
    # State variables stored in a tuple for each time-step/time-point
    inputs = (q[i],q_f[i],cA_f[i],T_f[i])
    ts = [t[i],t[i+1]]
    
    # y is a vector/list of size 3
    y = solve_ivp(
        fun=cstr_mass_bal,
        y0=y_0,
        t_span=ts,
        args=inputs,
        dense_output=True
        )
    # print(y.y[0])
    # Store results to initialise the next time-step
    V[i+1] = y.y[0][-1]
    cA[i+1] = y.y[1][-1]
    T[i+1] = y.y[2][-1]

    # Adjust initial condition for next loop
    y_0 = [V[i+1],cA[i+1],T[i+1]]

# Construct results & save results file
data = np.vstack((t,q_f,q,T_f,cA_f,V,cA,T))     # Vertical stack
data = data.T
np.savetxt(
    "data.txt",
    data,
    delimiter=","
)

# Plot inputs & results
plt.figure()

## PLOT INPUT PARAMETERS ON LHS (WITH ODD INDEX ARGUMENTS TO subplot())
# Plotting flowrates
plt.subplot(3,2,1)
plt.plot(t,q_f,'b--',linewidth=3)
plt.plot(t,q,'b:',linewidth=3)
plt.ylabel("Flow rates (lit/min)")
plt.legend(['Inlet','Outlet'],loc='best')

# Plotting feed concentration
plt.subplot(3,2,3)
plt.plot(t,cA_f,'r--',linewidth=3)
plt.ylabel("cA_f (mol/lit)")
plt.legend(['Feed concentration'],loc='best')

# Plotting feed temperature
plt.subplot(3,2,5)
plt.plot(t,T_f,'k--',linewidth=3)
plt.ylabel("T_f (K)")
plt.legend(['Feed temperature'],loc='best')
plt.xlabel('Time (min)')

## PLOT OUTPUT PARAMETERS ON LHS (WITH EVEN INDEX ARGUMENTS TO subplot())
# Plotting volume
plt.subplot(3,2,2)
plt.plot(t,V,'b-',linewidth=3)
plt.ylabel("Volume (lit)")
plt.legend(['Volume'],loc='best')

# Plotting concentration
plt.subplot(3,2,4)
plt.plot(t,cA,'r-',linewidth=3)
plt.ylabel("Concentration (mol/lit)")
plt.legend(['Concentration'],loc='best')

# Plotting temperature
plt.subplot(3,2,6)
plt.plot(t,T,'k-',linewidth=3)
plt.ylabel("T (K)")
plt.legend(['Temperature'],loc='best')
plt.xlabel('Time (min)')

plt.show()