# Hinweise für den Versuch: "Ideales und reales Gas" 

## Versuchsdurchführung [1/2]

###  Aufgabe 1: Messung des absoluten Nullpunkts mit Hilfe eines Gasthermometers

#### Hinweise zur Datennahme

- Die Annahme $\vartheta=const.$ bei der Side- und Schmelztemperatur setzt ein **thermodynamisches Gleichgewicht** voraus, das insbesondere bei Eiswasser nicht immer gegeben ist.

- Schieben Sie das Becherglas vorsichtig von unten kommend, so hoch wie möglich über K. Füllen Sie es dann mit einem Gemisch aus möglichst _fein_ zerstoßenem Eis und kaltem Wasser, so dass K möglichst ganz bedeckt ist. Rühren Sie die Mischung vorsichtig durch, so dass eine möglichst homogene Temperaturverteilung im Bereich $\vartheta=0^{\circ}\mathrm{C}$ im Wärmebad entsteht. 

- Die Luft in K beginnt daraufhin abzukühlen, worauf in K ein Unterdruck relativ zur Umgegung entsteht. Justieren Sie, während dieses Vorgangs RR bis zum Anschlag nach unten **um zu verhindern, dass $\mathrm{Hg}$ in K eingesogen wird**. 

- Nach ${\approx}15\ \mathrm{min}$ sollte die Luft in K die Temperatur des Wärmebads angenommen haben. Regeln Sie die Höhe der $\mathrm{Hg}$-Kuppe in RL so ein, dass sie gerade die Spitze S berührt. Sie erreichen dies, indem Sie RR langsam nach oben verschieben. Aus der Höhendifferenz $\Delta h$ der beiden Quecksilberkuppen können Sie $p_{0}$ bestimmen. Um den Druck in $\mathrm{mbar}$ zu erhalten verwenden Sie die Umrechnung
  ```math
  \begin{equation*}
  1\,\mathrm{mm\,Hg} = 1,33322\,\mathrm{mbar}
  \end{equation*}
  ```

- Bringen Sie dannn das Wasser in W auf Siedetemperatur $\vartheta_{s}$. Beachten Sie dabei die folgenden Punkte: 

  - $\vartheta_{s}$ ist selbst druckabhängig. Eine Dampfdruckkurve für Wasser, ebenso wie ein digitales Barometer zur Bestimmung des Umgebungsdrucks liegen in den Versuchsräumen aus.
  - Achten Sie auch beim Heizen darauf, dass K immer vollständig mit Wasser bedeckt ist. 
  - Bevor Sie $p(\vartheta_{s})$ wie oben bestimmen, sollte das Wasser einige Minuten lang sieden, um sicher zu stellen, dass sich W im thermischen Gleichgewicht befindet.

#### Hinweise zur Auswertung

Wenn Sie $\gamma$ genauer bestimmen wollen, sollten Sie sich zu einigen zusätzlichen Effekten Gedanken machen, die Ihre Messung verfälschen können:

- K hat selbst eine thermische Ausdehnung;
- K verformt sich unter Druck;
- Luft ist kein ideales Gas;
- Ein Teil des Gases befindet sich (bei Raumtemperatur) in RZ, außerhalb von K.

Alle Effekte bis auf die thermische Ausdehnung von K sind tatsächlich sehr klein, so dass Sie sie in Ihrer Auswertung vernachlässigen können. Sie sollten Sie aber dennoch diskutieren. Geben Sie z.B. in einer Tabelle an, ob eine entsprechende Variationen $\gamma$ vergößert oder verkleinert. 

#### Korrektur auf die thermische Ausdehnung von K

Einen Korrekturterm für die thermische Ausdehnung von K erhalten Sie aus der folgenden Überlegung: Bei $\vartheta_{s}$ hat sich das von K vorgegebene Volumen $V_{\mathrm{K}}$ um den Faktor 
$$
\begin{equation*}
\frac{V_{\mathrm{K}}^{\prime}}{V_{\mathrm{K}}} = 1+\vartheta_{s}\gamma_{\mathrm{K}}
\end{equation*}
$$
ausgedehnt, wobei Sie für Glas den kubischen Ausdehnungskoeffizient 
$$
\begin{equation*}
\gamma_{K}=(0.9\pm0.1)\times10^{-5}\,\mathrm{K}^{-1}
\end{equation*}
$$
annehmen können. Nach der idealen Gasgleichung ($pV=n\ R\ T_{s}$) ist $p(\vartheta_{s})$ um den entsprechenden Faktor zu verringern. Gleichung **(1)** [hier](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Ideales_und_reales_Gas/doc/Hinweise-Gasthermometer.md) nimmt dadurch die folgende Form an:
$$
\begin{equation}
\begin{split}
&p(\vartheta_{s}) = \frac{p_{0} + \gamma\,p_{0}\,\vartheta_{s}}{1+T_{s}\gamma_{\mathrm{K}}}; \\
&\\
&\gamma^{(1)} = \frac{\left(1+T_{s}\gamma_{\mathrm{K}}\right)\,p(\vartheta_{s})-p_{0}}{p_{0}\,\vartheta_{s}}; \\
&\hphantom{\gamma^{(0)}} = \underbrace{\frac{p(\vartheta_{s})-p_{0}}{p_{0}\,\vartheta_{s}}} + \underbrace{\frac{p(\vartheta_{s})}{p_{0}}\,\frac{T_{s}}{\vartheta_{s}}\,\gamma_{\mathrm{K}}} \\
& \hphantom{ccccccccccc} \gamma^{(0)}
\hphantom{ccccccccccc}\delta\gamma\\
&\\
&\text{mit:}\\
&\\
&T_{s} = \vartheta_{s}+\frac{1}{\gamma}.\\
\end{split}
\end{equation}
$$
Es ergibt sich also ein additiver Korrekturterm $\delta\gamma$ zur ursprünglichen Abschätzung $\gamma^{(0)}$. 

Es zeigt sich, dass die Berechnung von $\delta\gamma$ bereits einen Wert für $T_{s}$ (und damit für $\gamma$) voraussetzt. Sie können Gleichung **(1)** nach $\gamma$ auflösen und die Korrektur exakt berechnen. Ein in der Praxis oft alternativ angewandtes Verfahren besteht darin iterativ vorzugehen. Hierzu bestimmen Sie $\gamma^{(0)}$ zunächst ohne Korrektur und verwenden diesen Wert zur Bestimmung von $\delta\gamma$. 

# Navigation

[Main](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Ideales_und_reales_Gas) | [Weiter](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Ideales_und_reales_Gas/doc/Hinweise-Versuchsdurchfuehrung-a.md)
