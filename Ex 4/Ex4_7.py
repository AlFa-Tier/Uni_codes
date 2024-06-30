import numpy as np

#Nr. 21

## Needed constants 
k_B = 1.380649E-23
T = 300                     #Roomtemp.
R_inf = 1.097E7
c = 3E8                     #Speed of light
m_H = 1.66053906892E-27     #Mass Hydrogen atom


v_0 = R_inf*((1/4) - (1/9))
delta_v = ((2*v_0)/c)*np.sqrt((2*k_B*T*np.emath.logn(np.e, 2))/(m_H))

print(f'{v_0:.05E}')
print (f'{delta_v:.04E}')
