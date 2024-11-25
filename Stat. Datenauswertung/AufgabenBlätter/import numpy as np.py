import numpy as np
import matplotlib.pyplot as plt

# Parameter für g(t)
a, b = 1, np.e  # Bereich für t
n_samples = 10000

# Wahrscheinlichkeitsdichte g(t) = 1/t im Bereich [a, b]
def g(t):
    return 1 / t

# Normalisierte Verteilungsfunktion G(t) für g(t)
def G(t):
    return np.log(t) / np.log(b)

# Inverse Verteilungsfunktion G^-1(r)
def G_inv(r):
    return np.exp(r * np.log(b))

# Generieren von Zufallszahlen und Transformation
r = np.random.uniform(0, 1, n_samples)
t = G_inv(r)

# Histogramm von t und analytische Dichte g(t)
hist, bins = np.histogram(t, bins=50, density=True)
bin_centers = 0.5 * (bins[1:] + bins[:-1])

# Plot
plt.figure(figsize=(10, 6))

# Histogramm von t
plt.bar(bin_centers, hist, width=np.diff(bins), alpha=0.6, label="Empirische Verteilung")

# Analytische Dichte g(t)
t_vals = np.linspace(a, b, 500)
plt.plot(t_vals, g(t_vals), 'r-', lw=2, label="Theoretische Dichte $g(t)$")

# Diagramm beschriften
plt.title("Transformationsmethode: g(t) = 1/t")
plt.xlabel("t")
plt.ylabel("Dichte")
plt.legend()
plt.grid()
plt.show()