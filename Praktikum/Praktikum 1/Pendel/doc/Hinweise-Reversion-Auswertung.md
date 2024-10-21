# Hinweise für den Versuch Pendel

## Auswertung der Messungen mit dem Reversionspendel

Sie sollten für Ihre Messungen mit dem Reversionspendel die folgenden Erwartungen haben:

- $T_{0}(d)$ hat einen linearen Verlauf, $T_{0}\propto d$; 
- $T_{0}^{\prime}(d)$ hat einen konvexen Verlauf, z.B. $T_{0}'\propto d^{2}$; 
- Für $\ell_{r}$ gilt $T_{0}(\ell_{r})=T_{0}'(\ell_{r})$. 

Verwenden Sie zur Anpassung an die Datenpunkte z.B. die Modelle:
$$
\begin{equation}
\begin{split}
&T_{0}(d) = \beta'\,d + \gamma'\\
&\\
&T_{0}'(d) = \alpha\,(d-\beta)^{2} + \gamma,\\
\end{split}
\end{equation}
$$
mit den freien Parametern $\alpha,\ \beta,\ \gamma,\ \beta',\ \gamma'$. Die angepassten Kurven sollten einen Schnittpunkt aufweisen.

Tragen Sie, zur Bestimmung von $\ell_{r}$ die Messpunkte $(d_{i},D(d_{i}))$ mit 
$$
\begin{equation*}
D(d_{i}) = T_{0}(d_{i})-T_{0}'(d_{i})
\end{equation*}
$$
auf. Passen Sie an diese Datenreihe das Modell für $T_{0}'$ aus Gleichung **(1)** an. 

Aus der folgenden Rechnung können Sie sich leicht überzeugen, dass Sie für $D(d_{i})$ den gleichen quadratischen Zusammenhang als Funktion von $d$, wie für $T_{0}'$ erwarten: 
$$
\begin{equation*}
\begin{split}
D(d) &= T_{0}(d) - T_{0}'(d);\\
&\\
& = \bigl(\beta'\,d + \gamma'\bigr) - \bigl(\alpha\,d^{2} - 2\alpha\beta\,d + \left(\alpha\,\beta^{2}+\gamma\right)\bigr);\\
&\\
& = -\alpha\,d^{2} + \underbrace{(\beta'+2\alpha\,\beta)}\,d + \underbrace{\left(\gamma'-\left(\alpha\,\beta^{2}+\gamma\right)\right)}\\
&\hphantom{= -\alpha\,d^{2} +\beta'-} \equiv\widetilde{\beta}
\hphantom{\beta + \gamma'-\beta^{2}+}\equiv\widetilde{\gamma}\\
\end{split}
\end{equation*}
$$
Mit der gleichen Parameterwahl, wie für das Modell für $T_{0}'$ aus Gleichung **(1)** können Sie $\ell_{r}$ leicht mit Hilfe der folgenden Umstellung
$$
\begin{equation*}
\begin{split}
& D(\ell_{r}) = \hat{\alpha}\,(\ell_{r}-\hat{\beta})^{2} + \hat{\gamma} = 0; \\
&\\
& \ell_{r} = \pm\sqrt{-\frac{\hat{\gamma}}{\hat{\alpha}}}+\hat{\beta}
\end{split}
\end{equation*}
$$
bestimmen. Eine Gerade hat bis zu zwei Schnittpunkte mit einer Parabel. Vergewissern Sie sich welche Lösung für $\ell_{r}$ für Sie von Relevanz ist. 

- Wir empfehlen für diese Aufgabe die Bestimmung der Unsicherheit $\Delta\ell_{r}$ aus linearer Fehlerfortpflanzung. 
- Nutzen Sie hierzu die Unsicherheiten der Parameter $\alpha,\ \beta,\ \gamma$, wie Sie sie aus der Anpassung an die Daten erhalten haben. 
- Bestandteil der Ausgabe der Anpassung des Modells für $T_{0}'$ aus Gleichung **(1)** ist eine Kovarianzmatrix für die angepassten Parameter $\alpha,\ \beta,\ \gamma$, woraus Sie überprüfen können, inwiefern die Annahme der Unabhängigkeit dieser Parameter gerechtfertigt ist. 

**NB:** Sie können die Parameter $\alpha,\ \beta,\gamma$ durch Variablentransformation
$$
\begin{equation*}
d\to d'=d+\beta; \qquad
D\to D'=D-\gamma,
\end{equation*}
$$
so dass der Ursprung des verwendeten Koordinatensystems im Scheitelpunkt der angepassten Parabel liegt, vollständig dekorrelieren. 

# Navigation

[Main](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/tree/main/Pendel)

