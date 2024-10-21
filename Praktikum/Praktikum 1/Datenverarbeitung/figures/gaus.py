#!/usr/bin/python3
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

x = np.linspace(-5., 5., 100)
fig = plt.figure(1, figsize=(6.0, 6.0))
plt.plot(x, norm.pdf(x), color="black")
plt.axis("off")
plt.savefig("gaus.png")
plt.show()


