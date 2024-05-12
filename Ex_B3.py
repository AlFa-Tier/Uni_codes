import numpy as np
import matplotlib.pyplot as plt

c = 3*10**8
h_ev = 4.1356676969e-15
h = 6.62607015e-34
m_e = 9.1093837015e-31
e_charge = 1.602176634e-19
k_B = 1.380649e-23
R = 8.314
U_B = 6e3


def gamma(x):
    return 1/np.sqrt(1-(x/c)**2)

Lambda =np.array([150,200,250,300,350,400,450,500,550,600])
U_0 = np.array([5.97, 3.90, 2.66, 1.83, 1.24, 0.80, 0.46, 0.18, 0, 0])
f = c/(Lambda*10**(-9))

df = f[0]-f[-3]
dU = U_0[0]-U_0[-3]

s =e_charge * dU/df 
f_0 = f[0] - U_0[0]/h_ev

E = h_ev*f_0

print(f'Die gemesene Austrittsenergie ist: {E}')
print(f'Der gemesene Wert für h lautet: {s}')
print(f'Gemesene Grenzfreq.: {f_0}')


'''plt.plot(Lambda,U_0)
plt.ylabel(rf'U_0 in V')
plt.xlabel(rf'lambda in nm')
plt.close()

plt.plot(f,U_0)
plt.ylabel(rf'U_0 in V')
plt.xlabel(rf'f in Hz')
plt.show()'''

'''Nummer 2'''




v2 = c * np.sqrt(1-(1/(1+(U_B*e_charge)/(c**2 * m_e))**2))




print(f'Relativistische Geschw.: {v2}')

p_rel = gamma(v2)*m_e*v2
Wavelength = h/(m_e * v2)
print(f'Wavelength: {Wavelength}')


# Nummer 3

r = [0]
d= (1.2e-10,2.1e-10)



for i in range(2):
    x = 1
    while max(r) < 0.1:
        alpha = 2* np.arcsin((x*Wavelength)/2*d[i])
        new_r = 0.25 * np.tan(alpha)
        r.append(new_r)
        x+= 1

    print(f'List of ranges for d= {d[i]} is {r}')
    r = [0]