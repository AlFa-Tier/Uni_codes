import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import scipy.integrate as integrate

mu0 = 4*np.pi*1e-7     # Magentische Feldkonstante in N/A**2
L   =  200.            # L (mm)
n   = 3000             # Anzahl der Windungen
R   =   45.            # mittlerer Radius (mm)

def Bfield(x, I):
    """
    Formular for the calculation of B(x, I).
    """
    return 1000.*mu0*I*n/L*0.567*(x/np.sqrt(R**2+x**2)+(L-x)/np.sqrt(R**2+(L-x)**2))

S   = 150.             # Bildschirmposition (mm)
d1  =  88.             # Abstand Deflektrozentrum 1 vom Bildschirm (mm)
d2  =  70.             # Abstand Deflektrozentrum 2 vom Bildschirm (mm)

def MeanField(I, d):
    """
    Mean field along the magnetic coil for given I.
    """
    # Find our more about scipy.integrate.quad here
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.quad.html
    return integrate.quad(Bfield, S-d, S, args=(I))[0]/d

## Predefine figure and axes layout
fig, ax = plt.subplots(figsize=(6., 6.))
ax.set_xlabel(r"$z\,[\mathrm{mm}]$")
ax.set_ylabel(r"$B\,[\mathrm{mT}]$")
ax.set_xlim(0., 200.)
ax.set_ylim(0.,  15.)
ax.grid(axis='both', linewidth=1, linestyle="--", color='lightgray')

## Get the data
df = pd.read_csv("Busch-Magnetfeld-observed.csv")
B143,=ax.plot(df["a"], df["B143"], linewidth=0, color="darkblue"   , marker="o", label=r"$I_{\mathrm{S}}=143\,\mathrm{mA}$")
B286,=ax.plot(df["a"], df["B286"], linewidth=0, color="darkmagenta", marker="^", label=r"$I_{\mathrm{S}}=286\,\mathrm{mA}$")
B429,=ax.plot(df["a"], df["B429"], linewidth=0, color="darkcyan"   , marker="v", label=r"$I_{\mathrm{S}}=429\,\mathrm{mA}$")
B571,=ax.plot(df["a"], df["B571"], linewidth=0, color="darkgreen"  , marker="s", label=r"$I_{\mathrm{S}}=571\,\mathrm{mA}$")
B714,=ax.plot(df["a"], df["B714"], linewidth=0, color="goldenrod"  , marker="D", label=r"$I_{\mathrm{S}}=714\,\mathrm{mA}$")

# Get the expectation
x = np.linspace(10., 190., 180)
ax.plot(x, Bfield(x, 143), linewidth=1, linestyle=(0., (5., 2.5)), color="darkblue"   )
ax.plot(x, Bfield(x, 286), linewidth=1, linestyle=(0., (5., 2.5)), color="darkmagenta")
ax.plot(x, Bfield(x, 429), linewidth=1, linestyle=(0., (5., 2.5)), color="darkcyan"   )
ax.plot(x, Bfield(x, 571), linewidth=1, linestyle=(0., (5., 2.5)), color="darkgreen"  )
ax.plot(x, Bfield(x, 714), linewidth=1, linestyle=(0., (5., 2.5)), color="goldenrod"  )

# Add a legend and show plot
dashed_line=mlines.Line2D([], [], color="gray", linestyle=(0., (5., 2.5)), label="Erwartung")
ax.legend(
    handles=[B143, B286, B429, B571, B714, dashed_line], 
    bbox_to_anchor=(0., 1., 1., 0.2), 
    loc="lower left", 
    mode="expand", 
    ncol=3
)
plt.savefig("Busch-Magnetfeld.png")
#plt.show()

print(80*"-")
print("Mittleres B-Feld (571 mA, Position d1):", "{:0<6.5} mT".format(MeanField(571, d1)))
print("Mittleres B-Feld (571 mA, Position d2):", "{:0<6.5} mT".format(MeanField(571, d2)))
print(80*"-")

