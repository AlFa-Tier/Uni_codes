# Hinweise für den Versuch Datenverarbeitung

## Physikalische Modelle

### Mathematisches Pendel

Die Bewegung des [mathematischen Pendels](https://de.wikipedia.org/wiki/Mathematisches_Pendel) wird durch die folgende Differentialgleichung beschrieben:
$$
\begin{equation}
m\,\ell^{2}\,\ddot{\varphi} + mg\ell\,\varphi = 0,
\end{equation}
$$
wobei $m$ einer Punktmasse und $\ell$ dem Abstand zwischen $m$ und der Aufhängung des Pendels entsprechen. Gleichung **(1)** wird von **[harmonischen Schwingungen](https://de.wikipedia.org/wiki/Schwingung)** der Form 
$$
\begin{equation}
\varphi(t) = A\,\cos\left(\omega\,t + \phi_{0}\right);\qquad
\omega=\sqrt{\frac{g}{\ell}}
\end{equation}
$$
gelöst, wobei $A$ die Amplitude, $\omega$ die [Kreisfrequenz](https://de.wikipedia.org/wiki/Kreisfrequenz) und $\phi_{0}$ eine freie Phase der Schwingung bezeichnen. 

- $A$ und $\phi_{0}$ werden durch die Anfangswerte des jeweiligen Problems festgelegt; 
- $\omega$ folgt aus einer Sekundärgleichung zu Gleichung **(1)** und ist eine Eigenschaft des Pendels. 

Mit Hilfe dieses Modells können Sie bei gegebenem $\ell$ die Größe von $g$ mit Hilfe der Gleichung
$$
\begin{equation}
g = \frac{4\,\pi^{2}}{T^{2}}\ell
\end{equation}
$$
aus der Periode $T$ der Schwingung bestimmen. 

### Physikalisches Pendel

Das Modell des [mathematischen Pendels](https://de.wikipedia.org/wiki/Mathematisches_Pendel) stellt eine starke Vereinfachung der Realität dar: der Faden wird als masselos und die gesamte Masse des Pendels in einem Punkt konzentriert angenommen. 

Möchte man die endliche Ausdehnung des Pendels berücksichtigen muss man die physikalischen Eigenschaften starrer Körper berücksichtigen und das Modell des [physikalischen Pendels](https://de.wikipedia.org/wiki/Physikalisches_Pendel) zugrunde legen. Die zugehörige Bewegungsgleichung hat die Form 
$$
\begin{equation}
\Theta\,\ddot{\varphi} + Mgs\,\varphi = 0,
\end{equation}
$$
wobei $M$ der gesamten Masse, $s$ dem Abstand zwischen Schwerpunkt und Aufhängung und $\Theta$ dem Trägheitsmoment des Pendels entsprechen.

Während die mathematische Lösung, ihrer Form nach, gleich bleibt nimmt Gleichung **(3)** die folgende Form an:
$$
\begin{equation}
g = \frac{4\,\pi^{2}}{T^{2}}\frac{\Theta}{Ms}.
\end{equation}
$$

### Linear [gedämpfte Schwingung](https://de.wikipedia.org/wiki/Schwingung#Linear_ged%C3%A4mpfte_Schwingung)

Legen wir der Messung das Modell einer linearer gedämpften Schwingung zugrunde verändert sich Gleichung **(5)** zur Bestimmung von $g$ wie folgt: 
$$
\begin{equation}
\begin{split}
&g = \frac{4\,\pi^{2}}{T^{2}}\frac{\Theta}{Ms}+\underbrace{\frac{1}{\tau^{2}}\frac{\Theta}{Ms}},\\
&\hphantom{cccccccccccccccci}\equiv \delta g^{(0)}
\end{split}
\end{equation}
$$
wobei $\tau$ einer Abklingzeit in Sekunden entspricht. Bei $\delta g^{(0)}$ handelt es sich um eine Korrektur hin zu größeren Werten von $g$.  

Die Dämpfung hat nicht nur Einfluss auf die Bestimmung von $g$ sondern auch auf die Lösung der (modifizierten) Bewegungsgleichung, die sich wie folgt ändert:
$$
\begin{equation}
\varphi(t) = A\,e^{-t/\tau}\cos(\omega t+\phi_{0});\qquad
\omega=\sqrt{\frac{gMs}{\Theta}-\frac{1}{\tau^{2}}}.
\end{equation}
$$

Anm.: Für ein **gedämpftes mathematisches Pendel** hat Gleichungen **(6)** die Form: 
$$
\begin{equation}
g = \left(\frac{4\,\pi^{2}}{T^{2}}+\frac{1}{\tau^{2}}\right)\ell.
\end{equation}
$$

# Navigation

[Main](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/tree/main/Datenverarbeitung)
