# Hinweise für den Versuch Pendel


## Fadenpendel

### Modell des Fadenpendels

Unter Vernachlässigung von Reibungseffekten und bei kleinen Auslenkungen $\varphi_{0}$  wird die Schwingung des Fadenpendels durch die Differentialgleichung des [physikalischen Pendels](https://de.wikipedia.org/wiki/Physikalisches_Pendel) 
$$
\begin{equation}
\begin{split}
&\Theta\ddot{\varphi}+\underbrace{m\,s\,g}\,\varphi=0\\
&\hphantom{\Theta\ddot{\varphi}\quad}\equiv D \\
&\\
&\varphi(t) = \varphi_{0}\sin(\omega_{o}\,t+\phi)
\end{split}
\end{equation}
$$
beschrieben, wobei $\Theta$ dem Trägheitsmoment, $g$ der Erdbeschleunigung, $m$ der Masse und $s$ dem Abstand zwischen Aufhängung und Schwerpunkt des Pendels entsprechen. $D$ bezeichnet das [Direktionsmoment](https://de.wikipedia.org/wiki/Direktionsmoment). 

Aus Gleichung **(1)** lassen sich die Kreisfrequenz $\omega_{0}$ und Periode $T_{0}$ bestimmen:
$$
\begin{equation}
\omega_{0} = \sqrt{\frac{D}{\Theta}}=\sqrt{\frac{m\,\ell\,g}{\Theta}};\qquad T_{0}=2\pi\sqrt{\frac{\Theta}{D}}=2\pi\sqrt{\frac{\Theta}{m\,\ell\,g}}.
\end{equation}
$$
Mit Hilfe des [Satzes von Steiner](https://de.wikipedia.org/wiki/Steinerscher_Satz) lässt sich $\Theta$ aus dem Trägheitsmoment einer homogenen Kugel  abschätzen: 
$$
\begin{equation}
\Theta = m\,s^{2} + \frac{2}{5}\,m\,r^{2},
\end{equation}
$$
wobei $r$ dem Radius der Kugel entspricht. Beachten Sie, dass $s$ nicht die Länge des Fadens, sondern der Abstand zwischen Aufhängung und Schwerpunkt des Pendels ist. Wenn Sie die Masse des Fadens gegenüber der Masse der Kugel vernachlässigen, fällt der Schwerpunkt des Pendels mit dem Schwerpunkt der Kugel zusammen.

Einsetzen von Gleichung **(3)** in Gleichung **(2)** führt zu einer Bestimmungsgleichung für $g$:
$$
\begin{equation}
\begin{split}
g = \frac{4\pi^{2}}{T^{2}}\left(s +\frac{2}{5}\frac{r^{2}}{s}\right).
\end{split}
\end{equation}
$$

Dabei ist 
$$
\begin{equation*}
\delta g/g_{0}=\frac{2}{5}r^{2}
\end{equation*}
$$
der relative Unterschied zur Bestimmung von $g$ auf Grundlage des Modells eines [mathematischen Pendels](https://de.wikipedia.org/wiki/Mathematisches_Pendel) ($g_{0}$). 

### Abweichungen von der Kleinwinkelnäherung

Verlässt man die [Kleinwinkelnäherung](https://de.wikipedia.org/wiki/Kleinwinkeln%C3%A4herung) wird Gleichung **(1)** zu einer nicht-linearen Differentialgleichung der Form 
$$
\begin{equation*}
\begin{split}
&\Theta\ddot{\varphi}+\underbrace{m\,s\,g}\,\sin\varphi=0\\
&\hphantom{\Theta\ddot{\varphi}\quad}\equiv D
\end{split}
\end{equation*}
$$
die zwar immer noch [exakt lösbar](https://de.wikipedia.org/wiki/Mathematisches_Pendel#Exakte_L%C3%B6sung), aber nicht mehr analytisch geschlossen darstellbar ist. Die Lösung erfordert die Verwendung [elliptischer Funktionen](https://de.wikipedia.org/wiki/Jacobische_elliptische_Funktionen#Die_drei_grundlegenden_Jacobischen_Funktionen). Die Periode lässt sich in diesem Fall durch eine Reihenentwicklung annähern, deren erste Korrektur wie folgt aussieht:
$$
\begin{equation}
T_{0}(\varphi_{0}) = T_{0}\left(1+\frac{1}{4}\sin^{2}\left(\varphi_{0}/2\right)\right).
\end{equation}
$$
Dabei ist 
$$
\begin{equation*}
\delta T_{0}/T_{0} = \frac{1}{4}\sin^{2}(\varphi_{0}/4)
\end{equation*}
$$
der relative Unterschied zur Bestimmung von $T_{0}$ auf Grundlage der Kleinwinkelnäherung.

## Essentials

Was Sie ab jetzt wissen sollten:

- Sie sollten Gleichung **(1)** **herleiten und lösen können**.
- Sie sollten über das zustande kommen von Gleichung **(3)** im klaren sein.
- Sie sollten sich über den **Verlauf von $T_{0}(\varphi_{0})$** im klaren sein.   

## Testfragen

1. Wie groß ist der Effekt der endlichen Ausdehnung der Kugel auf die Messung?
1. Für welchen maximalen Auslenkungswinkel ist der Effekt der Kleinwinkelnäherung kleiner als 1%, 10%?
1. Schätzen Sie aufgrund der Kleinwinkelnäherung $T_{0}$ zu klein oder zu große ab?

# Navigation

[Main](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/tree/main/Pendel)

