#!/usr/bin/python3
"""
This is a python script to produce figures to illustrate FM over AM

Usage:

python3 Task-18-matplotlib-line-plot.py
"""
import matplotlib.pyplot as plt
import numpy as np
# Creating a list of points in x from -10 to 10 to display the functions of 
# choice
x = np.linspace(0, 2, 800)
# Define carrier frequency (~15 Hz) 
omega_c = 2*np.pi*15
# Define signal frequency (~1 Hz)
omega_s = 2*np.pi
# Define frecuency swing (~120%)
delta_omega=12*np.pi
# Define the functions of choice
fm  = lambda x: np.sin(omega_c*x+delta_omega/omega_s*np.sin(omega_s*x))
sig = lambda x: np.cos(omega_s*x)
phi = lambda x: omega_c*x+np.pi/2+delta_omega/omega_s*np.sin(omega_s*x+np.pi/2)
mom = lambda x: omega_c+delta_omega*np.cos(omega_s*x)

fig, (a0, a1) = plt.subplots(2, 1, figsize=(10.0, 10.0), gridspec_kw={'height_ratios': [3, 1]}, sharex=True)
a0.plot(x, fm(x), 
    color="steelblue", 
    linestyle="solid",
    linewidth=2., 
    label="Modulierte Trägerwelle $U(t)$"
    )
a0.plot(x, sig(x), 
    color="indigo", 
    linestyle="dashed",
    linewidth=2., 
    label="Signalwelle $\omega_{s}(t)$"
    )
a0.set_ylabel("$U(t)\,(\mathrm{mV})$", loc="top", fontsize=16)
a0.tick_params(axis='y', which='major', labelsize=14)
a0.grid(True)
a0.legend(bbox_to_anchor=(0., 1., 1., 0.1), loc="lower left", ncol=2, prop={"size":16})

a1.plot(x, mom(x), 
    color="mediumvioletred",
    linestyle=(0, (5,2,1,2)), 
    linewidth=2., 
    label="Momentanfrequenz $\Omega(t)$"
    )
a1.set_xlabel("$t\,(\mathrm{s})$", loc="right", fontsize=16)
a1.set_ylabel("$\Omega(t)\,(\mathrm{Hz})$", loc="top", fontsize=16)
a1.tick_params(axis='both', which='major', labelsize=14)
a1.grid(True)
a1.legend(bbox_to_anchor=(0., 1., 1., 0.1), loc="lower left", prop={"size":16})
plt.savefig("FM-Momentanfrequenz.png")

fig1 = plt.figure("Momentanphase", figsize=(10.0, 10.0))
plt.plot(x, phi(x), 
    color="darkcyan", 
    linestyle="solid",
    linewidth=2., 
    label="Mit Signalmodulation $\phi_{s}(t)$"
    )
plt.plot(x, omega_c*x, 
    color="darkred", 
    linestyle="dashed",
    linewidth=2., 
    label="Ohne Modulation"
    )
plt.xlabel("$t\,(\mathrm{s})$", loc="right", fontsize=16)
plt.ylabel("$\phi(t)\,(\mathrm{rad})$", loc="top", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.grid(True)
leg1 = plt.legend(bbox_to_anchor=(0., 0.5, 0.5, 0.5), loc="upper left", prop={"size":16}, title="Momentanphase $\phi(t)$", title_fontsize=16)
leg1._legend_box.align = "left"
plt.savefig("FM-Momentanphase.png")
    
# Show the plots with a rendering machine
plt.show()

