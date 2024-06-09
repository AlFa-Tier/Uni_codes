# Hinweise für den Versuch: "Ideales und reales Gas" 

## Messung des Adiabatenexponent nach der Methode von [Rüchardt](https://de.wikipedia.org/wiki/R%C3%BCchardt-Experiment)

Diese Methode zur Bestimmung des Adiabatenexponenten $\kappa$ ist nach [Eduard Rüchardt](https://de.wikipedia.org/wiki/Eduard_R%C3%BCchardt) benannt. Sie verbindet die Bestimmung thermodynamischer Größen mit Messprinzipien, die Sie bereits aus der Mechanik kennen. 

Bei dieser Methode schwingt ein Pfropfen auf einem Luftpolster, das durch den Schwingungsvorgang in adiabatische Kompression und Expansion versetzt wird. Nach der Adiabatengleichung (siehe Gleichung **(2)** [hier](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Ideales_und_reales_Gas/doc/Hinweise-Thermodynamik.md)) gilt in diesem Fall: 
$$
\begin{equation*}
p\,V^{\kappa} = const.
\end{equation*}
$$
Für differentielle Druck- und Volumenänderungen ergibt sich daraus:

$$
\begin{equation}
\begin{split}
&\frac{\mathrm{d}p}{\mathrm{d}V} = -const.\,\kappa\,V^{-\kappa-1} \\
&\hphantom{\frac{\mathrm{d}p}{\mathrm{d}V}}= -\kappa\frac{p}{V}; \\
&\\
&\mathrm{d}p = -\kappa\frac{p}{V}\,\mathrm{d}V. \\
\end{split}
\end{equation}
$$
Aus der Multiplikation von Gleichung **(1)** mit dem Rohrinnenquerschnitt $A$ ergibt sich die auf den Pfropfen wirkende Kraft und eine lineare Schwingungsgleichung für die Bewegung des Pfropfens:

$$
\begin{equation}
\begin{split}
&\mathrm{d}F = -\kappa\frac{p}{V}A^{2}\,\mathrm{d}x; \\
&\\
&m\,\ddot{x} = -\kappa\frac{p}{V}A^{2}\,x,
\end{split}
\end{equation}
$$
wobei $m$ der Masse des Pfropfens entspricht. An dieser Stelle nehmen wir die Näherung vor, dass sich $p$ und $V$ durch die Bewegung des Pfropfens aus seiner Ruhelage nur geringfügig ändern ($p\approx const.,\ V\approx const.$). Aus Gleichung **(2)** lässt sich die Periode 

$$
\begin{equation}
t = 2\pi\sqrt{\frac{m\,V}{\kappa\,p\,A^{2}}}
\end{equation}
$$
der Schwingung ableiten, woraus sich $\kappa$ bestimmen lässt:

$$
\begin{equation*}
\kappa = \left(\frac{2\pi}{t}\right)^{2}\frac{m\,V}{p\,A^{2}}.
\end{equation*}
$$
Beachten Sie die etwas unintuitive Bezeichnung $t$ für die Periode der Schwingung, um Verwechslungen mit der Temperatur zur vermeiden.

# Navigation

[Main](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Ideales_und_reales_Gas)



