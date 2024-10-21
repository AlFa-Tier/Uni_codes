# Hinweise für den Versuch Pendel

## Auswertung der Messungen mit den gekoppelten Pendeln

Definieren Sie zur Überprüfung der Gleichungen **(5)** und **(6)** [hier](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/Pendel/doc/Hinweise-Gekoppelt.md) die folgenden Größen:
$$
\begin{equation*}
\omega_{1}^{\prime}\equiv\frac{\overline{\omega}-\widetilde{\omega}}{2};\quad 
\omega_{2}^{\prime}\equiv\frac{\overline{\omega}+\widetilde{\omega}}{2}.
\end{equation*}
$$
Berechnen Sie $\Delta\omega_{1}^{\prime}$ und $\Delta\omega_{2}^{\prime}$ mit Hilfe linearer Fehlerfortpflanzung. Die konkreten Werte 
$$
\begin{equation*}
\hat{\omega}_{1}^{\prime}\pm\Delta\hat{\omega}_{1}^{\prime};\quad
\hat{\omega}_{2}^{\prime}\pm\Delta\hat{\omega}_{2}^{\prime}
\end{equation*}
$$
können Sie innerhalb Ihrer Unsicherheiten mit den Werten
$$
\begin{equation*}
\hat{\omega}_{1}\pm\Delta\hat{\omega}_{1};\quad
\hat{\omega}_{2}\pm\Delta\hat{\omega}_{2}
\end{equation*}
$$
aus **Aufgabe 3.1** vergleichen. Eine mögliche Teststatistik wäre: 
$$
\begin{equation}
\begin{split}
&z=\sum\limits_{i=1,2} \delta_{i}^{2};\\
&\\
&\text{mit:}\\
&\\
&\delta_{i} = \frac{\omega_{i}^{\prime}-\omega_{i}}{\sqrt{\Delta\omega_{i}^{\prime\,2}+\Delta\omega_{i}^{2}}}.\\
\end{split}
\end{equation}
$$
Sowohl die $\delta_{i}$, als auch $z$ sind für die Betrachtungen interessant. 

- An $\delta_{i}$ erinnern Sie sich womöglich als den ***pull* zwischen $\omega_{i}^{\prime}$ und $\omega_{i}$**.
- Die Größe $z$ haben Sie womöglich als die **$\chi^{2}$-Teststatistik** (mit $n_{\mathrm{dof}}=2$ Freiheitsgraden) erkannt. 

Falls alle Messungen der $\omega_{i}^{\prime}, \omega_{i}$ einer Normalverteilung folgen und Sie die Unsicherheiten $\Delta\omega_{i}^{\prime}, \Delta\omega_{i}$ so abgeschätzt haben, dass Sie der Standardabweichung der jeweiligen Normalverteilung entsprechen, sollten die $\delta_{i}$ einer Standardnormalverteilung 
$$
\begin{equation*}
\varphi(\delta,0,1) = \frac{1}{\sqrt{2\pi}}\,e^{-\frac{\delta^{2}}{2}}
\end{equation*}
$$
folgen. 

Die Teststatistik $z$ sollte einer $\chi^{2}$-Verteilung mit $n_{\mathrm{dof}}=2$ folgen. Einen $p$-Wert dafür den Wert $\hat{z}$ zu beobachten erhalten Sie aus dem Integral
$$
\begin{equation*}
p_{\hat{z}} = \int\limits_{\hat{t}}^{\infty}\chi^{2}(z, n_{\mathrm{dof}}=2)\,\mathrm{d}z.
\end{equation*}
$$
Um den $p$-Wert anschaulich zu verstehen stellen wir uns die folgende Situation vor (d.h. wir legen das folgende **statistische Modell** zugrunde): 

- Die Werte $\hat{\omega}_{i}^{\prime}, \hat{\omega}_{i}$ sind tatsächlich wahr! 
- Wir führen eine große Zahl identischer Messreihen durch.
- Für jede einzelne Messreihe streuen die gemessenen Ergebnisse gemäß einer Normalverteilung um die Werte $\hat{\omega}_{i}^{\prime}, \hat{\omega}_{i}$ mit den Standardabweichungen $\Delta\hat{\omega}_{i}^{\prime}, \Delta\hat{\omega}_{i}$. 

Wenn wir für jede einzelne Messreihe aus unseren Ergebnissen die Teststatistik $z$ berechnen folgt $z$ der $\chi^{2}(z, 2)$-Verteilung. $\chi^{2}(x, 2)$ ist auf 1 normiert und somit eine Wahrscheinlichkeitsdichteverteilung. $p$ beziffert also die Wahrscheinlichkeit einen Wert $z\geq\hat{z}$ zu erhalten, wenn alle oben getroffenen Annahmen wirklich wahr sind. Anhand des $p$-Werts können Sie nun beurteilen, wie wahrscheinlich der Ausgang Ihrer Messreihe ist, falls alle gemachten Annahmen und Schlussfolgerungen richtig sind.  

#  Navigation

[Main](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/tree/main/Pendel)
