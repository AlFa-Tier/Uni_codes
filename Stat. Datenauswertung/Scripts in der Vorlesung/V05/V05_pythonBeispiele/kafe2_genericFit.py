# Imports  #
# kafe2 Datencontainer
from kafe2 import XYContainer, HistContainer, UnbinnedContainer
# generische Fit-Klasse
from kafe2 import Fit
# Hilfsklassen
from kafe2 import Plot, ContoursProfiler

import matplotlib.pyplot as plt

# Modell definieren:
def xy_model(x, a, b):
    return a*x +b 

# Daten bereit stellen
x_data = [1.0, 2.0, 3.0, 4.0]
y_data = [2.3, 4.2, 7.5, 9.4]
# absolute uncertainty for x, relative for y
x_uabs = 0.1
y_urel = 0.1

# Container aufsetzen, z.B. 
xy_data = XYContainer(x_data, y_data)

# Fit-Objekt erzeugen
xy_fit = Fit(xy_data, xy_model)

# add uncertainties here,
#   because this is the only place also for errors depending on model 
xy_fit.add_error(axis='x', err_val = x_uabs, relative=False)
xy_fit.add_error(axis='y', err_val = y_urel, relative=True, reference="model")

# steer fit by setting initial values and uncertainties
xy_fit.set_parameter_values(a=1, b=1)
xy_fit.parameter_errors = [0.1, 0.1]
xy_result = xy_fit.do_fit()

# optionally print result
xy_fit.report(asymmetric_parameter_errors=True) # use neg. log L scan to determine uncertainties

# optionally, plot results
xy_plot = Plot(xy_fit)
xy_plot.plot(asymmetric_parameter_errors=True)

# otionally, determine profile-likelihood and 2d confidence contours
cpf = ContoursProfiler(xy_fit)
# cpf.plot_profiles_contour_matrix
cpf.get_profile('a')
cpf.plot_profile('a')

plt.show()
