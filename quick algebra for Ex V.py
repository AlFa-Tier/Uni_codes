import numpy as np 

format = "{:.03e}".format

h = 6.62607015e-34
wave = 2e-10
m = np.array([9.109e-31, 1.674e-27])
kb= 1.38e-23
np.set_printoptions(formatter={'float_kind':format})

E = ((h**2)/(2*m*wave**2))
print(E)

print(f'{(h*299792458)/wave:.03e}')

T = (2*E)/(3*kb)
print (f'{T}')