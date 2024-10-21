"""
Parameter für Messungen der Lichtgeschwindigkeit mit der Drehspiegelmethode.

Parameter und entsprechende Unsicherheiten sind in SI Einheiten gegeben. 
Schätzen Sie die Unsicherheiten auf die (Kalibration der) Frequenz des Dreh-
spiegels und die Messskala aus Ihrer Messung ab.
"""

a = 6.57                     # Abstand zwischen Umlenk- und Endspiegel (in m)
a_UPPER = 6.575              # +Unsicherheit
a_LOWER = 6.565              # -Unsicherheit

b = 7.23                     # Abstand zwischen Dreh- und Umlenkspiegel (in m)
b_UPPER = 7.235              # +Unsicherheit
b_LOWER = 7.225              # -Unsicherheit

l = 6.80                     # Abstand zwischen Drehspiegel und Messskala (in m)
l_UPPER = 6.805              # +Unsicherheit
l_LOWER = 6.795              # -Unsicherheit

f = 5.0                      # Brennwetie der Linse (in m), ohne Angsabe von 
                             # Unsicherheiten

__version__ = 1.0
