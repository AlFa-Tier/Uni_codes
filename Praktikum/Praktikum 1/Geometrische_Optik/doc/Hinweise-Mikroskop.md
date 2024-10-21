# Hinweise für den Versuch Geometrische Optik

## Strahlengang eines Mikroskops

Ein Mikroskop **bildet Gegenstände G, in sehr kleinen Abständen vergrößert ab**. Der Strahlengang eines Mikroskops unter *Normalvergößerung* (bei entspanntem Auge) ist in **Abbildung 1** gezeigt.

---

<img src="../figures/Mikroskop.png" width="1000" style="zoom:100%;" />

**Abbildung 1**: (Strahlengang eines Mikroskops bei Normalvergößerung)

---

Die linke Linse wird als *Objektiv* bezeichnet, die rechte Linse als *Okular*. Der Strahlengang ähnelt dem des Kepler-Fernrohrs, mit dem Unterschied der gewählten Brennweite des Objektivs. Dieses hat die Aufgabe G unter sehr kurzen Abständen auf das (reelle) Zwischenbild B abzubilden, die **Brennweite $f_{1}$ ist also klein zu wählen**, während sie für das Kepler-Fernrohr, zum Zwecke einer möglichst hohen Vergrößerung, groß zu wählen ist. Das Okular hat die gleiche Funktion, wie für das Kepler-Fernrohr: Es bildet G in ein virtuelles Bild B paralleler Strahlen unter dem Winkel $\beta$ ab. Die Vergrößerung $V$ ergibt sich aus dem Quotienten der Winkel, unter denen G betrachtet wird. Der Winkel $\beta$ berechnet sich aus 

$$
\begin{equation*}
\beta=\frac{B}{f_{2}}
\end{equation*}
$$
Der Winkel $\alpha$ berechnet sich aus dem Quotienten aus G und der Bezugssehweite

$$
\begin{equation*}
\alpha=\frac{G}{s}.
\end{equation*}
$$
Um die einzige Unbekannte G aus dem Verhältnis aus $\beta$ und $\alpha$ zu eliminieren verwenden wir die Linsengleichung

$$
\begin{equation*}
\begin{split}
&\frac{1}{f_{1}}=\frac{1}{g}+\frac{1}{b}
=\frac{1}{b}\left(\frac{B}{G}+1\right); \\
&\\
&\beta=\frac{\left(\frac{b}{f_{1}}-1\right)\,G}{f_{2}}\\
&\\
&V = \frac{\beta}{\alpha} = \frac{\left(\frac{b}{f_{1}}-1\right)\,G\,s}{f_{2}\,G} = \frac{\left(b-f_{1}\right)\,s}{f_{1}\,f_{2}} = \frac{\left(d-f_{1}-f_{2}\right)\,s}{f_{1}\,f_{2}}
\end{split}
\end{equation*}
$$
Der Abstand der Brennpunkte der beiden Linsen $d-f_{1}-f_{2}$ wird als *optische Tubuslänge* bezeichnet. 

Es erscheint vorteilhaft $f_{1}$ oder $f_{2}$ möglichst klein zu wählen, um eine möglichst starke Vergrößerung zu erhalten. Dies trifft zu solange die gewählten **Brennweiten groß gegen die Wellenlänge** des verwendeten Lichts sind, da sonst Beugungseffekte zu berücksichtigen sind.

# Navigation

[Main](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/tree/main/Geometrische_Optik)

