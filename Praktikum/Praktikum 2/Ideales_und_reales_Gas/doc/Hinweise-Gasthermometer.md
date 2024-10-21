# Hinweise für den Versuch: "Ideales und reales Gas" 

##  Messung des absoluten Nullpunkts mit Hilfe eines Gasthermometers

Der grundsätzliche Aufbau eines Gasthermometers und die im weiteren Verlauf verwendeten Bezeichnungen sind in **Abbildung 3** dargestellt: 

<img src="../figures/Gasthermometer.png" width="750" style="zoom:60%;" />

**Abbildung 3**: (Prinzipieller Aufbau eines Gasthermometers und im Text verwendete Bezeichnungen)

---

Ein Glaskolben (K) befindet sich in einem [Wärmebad](https://de.wikipedia.org/wiki/W%C3%A4rmebad) (W) und ist mit einem zweifach geschwungenen U-Rohr verbunden. Das untere U besteht aus einem flexiblen Gummischlauch. Dieser trennt das Rohr in einen (RL) linken und (RR) rechten Schenkel. RR ist beweglich montiert. In K ist das Volumen $V$ des Arbeitsgases eingeschlossen. Das Rohr wird durch eine Flüssigkeit (i.a. $\mathrm{Hg}$) dicht abgeschlossen. Der Volumenanteil $\delta V$ in der Rohrzuleitung RZ ist klein gegen $V$. Für den Druck $p$ in K gilt 
$$
\begin{equation*}
p(\Delta h) = p_{\mathrm{norm}} + \rho(\mathrm{Hg})\,g\,\Delta h, 
\end{equation*}
$$
wobei $p_{\mathrm{norm}}$ dem Umgebungsdruck, $\rho(\mathrm{Hg})$ der Dichte von $\mathrm{Hg}$ und $g$ der Erdbeschleunigung entsprechen.  

Die Temperaturmessung beruht auf der [idealen Gasgleichung](https://de.wikipedia.org/wiki/Thermische_Zustandsgleichung_idealer_Gase) 
$$
\begin{equation*}
p(V, T) = \frac{n\,R\,T}{V},
\end{equation*}
$$
wobei $T$ der Temperatur (in Kelvin, $\mathrm{K}$), $n$ der Stoffmenge und $R$ der idealen [Gaskonstanten](https://de.wikipedia.org/wiki/Gaskonstante) entsprechen. Für Messungen auf der $\mathrm{K}$-Skala werden wir die Variable $T$ verwenden, für Messungen auf der Celsius-Skala die Variable $\vartheta$. 

Das Thermometer wird nach dem Prinzip der Druckmessung bei $V=const.,\ n=const.$ betrieben ([Gesetz von Amontons](https://de.wikipedia.org/wiki/Thermische_Zustandsgleichung_idealer_Gase#Gesetz_von_Amontons)). In diesem Fall gilt $p\propto \vartheta$ mit 
$$
\begin{equation}
\begin{split}
&\left.p(\vartheta)\right|_{V=const.} = p_{0}\left(1+\gamma\,\vartheta\right);\\
&\\
&\text{mit:}\\
&\\
&p_{0}=p(\vartheta=0^{\circ}\mathrm{C}).\\
\end{split}
\end{equation}
$$
Die Steigung $\gamma$ wird als [Volumenausdehnungskoeffizient](https://de.wikipedia.org/wiki/Ausdehnungskoeffizient) bezeichnet. Laut Gleichung **(1)** verschwindet der Gasdruck $p(\vartheta_{0})$ bei einer Temperatur von 
$$
\begin{equation*}
\vartheta_{0}=-1/\gamma.
\end{equation*}
$$
Diese Temperatur bezeichnet man als **absoluten Nullpunkt** der Temperatur.

Zur Messung von $\gamma$ tauchen Sie K vollständig in ein [Wärmebad](https://de.wikipedia.org/wiki/W%C3%A4rmebad) ein, das Sie mit destilliertem Wasser herstellen. Wenn Sie den Druck bei der Siede- ($T_{s}$) und Schmelztemperatur von Wasser messen erhalten Sie, ohne ein weiteres Thermometer benutzen zu müssen, eine Abschätzung aus der Beziehung 
$$
\begin{equation*}
\gamma = \frac{p(\vartheta_{s}) - p_{0}}{p_{0}\,\vartheta_{s}}.
\end{equation*}
$$
Sowohl bei der Siede- als auch bei der Schmelztemperatur wird Wärme in [latente Wärme](https://de.wikipedia.org/wiki/Latente_W%C3%A4rme) umgewandelt, so dass $\vartheta=const.$ gilt. 

Diese Art der Messung setzt den linearen Zusammenhang $p(\vartheta)$ aus Gleichung **(1)** voraus. 

# Navigation

[Main](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Ideales_und_reales_Gas)



