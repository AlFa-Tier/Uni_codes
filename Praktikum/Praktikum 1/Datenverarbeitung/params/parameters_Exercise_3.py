"""
Parameters required for "Aufgabe 3".

The momentum of inertia (Theta), mass (M), and distance (s) between the center 
of mass of the complete pendulum and the pivotal point of the pendulum. All 
quantities have been derived from direct parameter estimates and rounded within 
their estimated uncertainties. They have been derived assuming simplified 
shapes of the corresponding objects, e.g. the smartphone has been approximated 
by a homogeneous box. All quantities are given in SI units.   
"""

Theta = 0.23523              # Momentum of inertia in kg*m**2
Theta_UPPER = 0.2378         # +uncertainty
Theta_LOWER = 0.2328         # -uncertatiny

M = 0.789                    # Mass of the pendulum in kg
M_UPPER = 0.794              # +uncertainty
M_LOWER = 0.784              # -uncertainty

s = 0.473                    # Distance of the center of mass from the pivotal point of the pendulum in m
s_UPPER = 0.480              # +uncertainty
s_LOWER = 0.466              # -uncertainty

__version__ = 1.0
