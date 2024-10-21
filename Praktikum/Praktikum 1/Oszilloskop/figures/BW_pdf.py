#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

def lorentzian_pdf(x, a, x0):
    return a / ((x-x0)**2 + a**2)/np.pi

x = np.linspace(0., 20., 100)
fig = plt.figure(1, figsize=(6.0, 6.0))
plt.plot(x, lorentzian_pdf(x, 1, 10), color="black", label=r"Breit-Wigner PDF ($\mu=10,\,\Gamma=1$)")
plt.xlabel("x")
plt.ylabel(r"$f(x, \mu, \Gamma)$")
plt.legend(bbox_to_anchor=(0., 1., 1., 0.1), loc="lower right")
plt.savefig("BW_pdf.png")
plt.show()


