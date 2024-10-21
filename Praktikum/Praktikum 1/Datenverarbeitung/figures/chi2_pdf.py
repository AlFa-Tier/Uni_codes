#!/usr/bin/python3
import numpy as np
from scipy.stats import chi2
import matplotlib.pyplot as plt

x = np.linspace(0., 20., 100)
fig = plt.figure(1, figsize=(6.0, 6.0))
plt.plot(x, chi2.pdf(x, 1), color="black", label=r"$\alpha=1$")
plt.plot(x, chi2.pdf(x, 2), color="darkblue", linestyle="dashed", label=r"$\alpha=2$")
plt.plot(x, chi2.pdf(x, 5), color="darkcyan", linestyle="dotted", label=r"$\alpha=5$")
plt.plot(x, chi2.pdf(x, 10), color="magenta", linestyle="dashdot", label=r"$\alpha=10$")
plt.xlabel("x")
plt.ylabel(r"$\chi_{\alpha}^{2}(x)$")
plt.legend()
plt.savefig("chi2_pdf.png")
plt.show()


