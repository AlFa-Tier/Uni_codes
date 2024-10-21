"""
Parameter für Messungen mit dem Reversionspendel.

Parameter und entsprechende Unsicherheiten für das Reversionspendel, in SI 
Einheiten.  
"""

L = 96.20                    # Länge des Stabs (in cm)
L_UPPER = 96.22              # +Unsicherheit
L_LOWER = 96.18              # -Unsicherheit

d = 1.50                     # Druchmesser des Stabs (in cm)
d_UPPER = 1.55               # +Unsicherheit
d_LOWER = 1.45               # -Unsicherheit

rho = 4.94                   # Längendichte des Stabs (in g/cm)
                             # Ohne Angabe von Unsicherheiten

Del = 1.0                    # Abstand des Auflagepunktes vom obersten Rand der Montagespange (in cm) NB: gilt für beide Spangen.
Del_UPPER = 1.02             # +Unsicherheit
Del_LOWER = 0.98             # -Unsicherheit

m1R1 = 86                    # Masse der festen Montagespange von Pendel R1 (in g)
m1R1_UPPER = 86.5            # +Unsicherheit
m1R1_LOWER = 85.5            # -Unsicherheit

m2R1 = 72                    # Masse der beweglichen Montagespange von Pendel R1 (in g)
m2R1_UPPER = 72.5            # +Unsicherheit
m2R1_LOWER = 71.5            # -Unsicherheit

mR2 = 83                     # Masse beider Montagespangen von Pendel R2 (in g)
mR2_UPPER = 83.5             # +Unsicherheit
mR2_LOWER = 82.5             # -Unsicherheit

__version__ = 1.0
