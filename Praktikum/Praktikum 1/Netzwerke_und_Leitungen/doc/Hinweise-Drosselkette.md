# Hinweise für den Versuch Netzwerke und Leitungen

## Drosselkette

Der Übergang vom $\pi$-Glied, wie [hier](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/Vierpole_und_Leitungen/doc/Hinweise-PiGlied.md) diskutiert, zur (idealen) Drosselkette erfolgt durch n-fache Hintereinanderschaltung von $\pi$-Gliedern, wie in **Abbildung 1** gezeigt:

---

<img src="../figures/Drosselkette.png" width="900" style="zoom:100%;" />

**Abbildung 1**: (Schaltbild einer idealen Drosselkette, bestehend aus n [$\pi$-Gliedern](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/Vierpole_und_Leitungen/doc/Hinweise-PiGlied.md))

---

Der Transfer
$$
\begin{equation*}
\left(\begin{array}{c}\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}U_{E}\\\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}Z_{0}\,I_{E}\end{array}\right) \longrightarrow 
\left(\begin{array}{c}\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}U_{A}\\\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}Z_{0}\,I_{A}\end{array}\right).
\end{equation*}
$$
erfolgt durch mehrfache Multiplikation mit $\mathcal{T}$:
$$
\begin{equation*}
\left(\begin{array}{c}
\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}U_{A}\\
\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}
Z_{0}\,I_{A}\end{array}\right) = \mathcal{T}^{n}\cdot
\left(\begin{array}{c}
\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}
U_{E}\\
\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}
Z_{0}\,I_{E}\end{array}\right) = 
\left(\begin{array}{cc}
\hphantom{-}
\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}
\cosh(n\gamma) & 
\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}
-\sinh(n\gamma)\\ 
-\sinh(n\gamma) & \hphantom{-}\cosh(n\gamma)\end{array}\right)
\cdot
\left(\begin{array}{c}
\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}U_{E}\\
\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}Z_{0}\,I_{E}\end{array}\right).
\end{equation*}
$$
 Für den Transfer der Spannung ergibt sich also
$$
\begin{equation*}
\frac{U_{A}}{U_{E}} = \cosh(n\gamma)-Z_{0}\frac{I_{E}}{U_{E}}\sinh(n\gamma)
\end{equation*}
$$
und für den Spezialfall $Z_{\mathrm{E}}=Z_{\mathrm{A}}=Z_{0}$
$$
\begin{equation*}
\frac{U_{A}}{U_{E}} = \cosh(n\gamma)-\sinh(n\gamma)= e^{-n\gamma} = e^{-n\alpha}e^{-i\,n\beta}.
\end{equation*}
$$
Für eine harmonische Eingangsspannung ergibt sich daraus:
$$
\begin{equation*}
\begin{split}
&U_{E}(t) = \hat{U}_{E}e^{i\,\omega t};\\
&\\
&U_{A}(t) = \hat{U}_{A}e^{-n\alpha}e^{i\left(\omega t-n\beta\right)}.\\
\end{split}
\end{equation*}
$$
Die **Dämpfungskonstante** kann also als
$$
\begin{equation*}
\alpha^{\prime} = n\,\alpha
\end{equation*}
$$
und die **Phasenkonstante** als 
$$
\begin{equation*}
\beta^{\prime} = n\,\beta
\end{equation*}
$$
aus den Eigenschaften der n in Reihe geschalteten $\pi$-Glieder abgelesen werden.

### Leitungseigenschaften

Aus der Substitution aus Gleichung **(6)** [hier](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/tree/main/Vierpole_und_Leitungen/doc/Hinweise-PiGLied.md)
$$
\begin{equation*}
\cosh\gamma\equiv\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}+1;\qquad \sinh\gamma\equiv\frac{Z_{\mathrm{L}}}{Z_{0}}= \sqrt{\frac{2\,Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}
\end{equation*}
$$
 folgt (für kleine Werte von $\gamma$)
$$
\begin{equation*}
\begin{split}
&\sinh\frac{\gamma}{2} = \sqrt{\frac{Z_{\mathrm{L}}}{2\,Z_{\mathrm{C}}}} = \sqrt{-\left(\frac{\omega}{\omega_{0}}\right)^{2}} = i\frac{\omega}{\omega_{0}} \\
&\\
&\text{mit:}\\
&\\
&\frac{Z_{\mathrm{L}}}{2\,Z_{\mathrm{C}}} = -\left(\frac{\omega}{\omega_{0}}\right)^{2},
\end{split}
\end{equation*}
$$
der Term $\sinh(\gamma/2)$ ist also **rein imaginär**. Andererseits gilt (aus den [Additionstheoremen](https://de.wikipedia.org/wiki/Sinus_hyperbolicus_und_Kosinus_hyperbolicus) des $\sinh(\hspace{0.1cm}\cdot\hspace{0.1cm})$):
$$
\begin{equation*}
\begin{split}
\sinh\frac{\gamma}{2} = \sinh\left(\frac{\alpha+i\beta}{2}\right) = &\underbrace{\sinh\frac{\alpha}{2}\,\cos\frac{\beta}{2}} + i\underbrace{\cosh\frac{\alpha}{2}\,\sin\frac{\beta}{2}},\\
&\hphantom{111,}=0
\hphantom{1111111111}=\frac{\omega}{\omega_{0}}\\
\end{split}
\end{equation*}
$$
die folgenden zwei Gleichungen müssen also gleichzeitig erfüllt sein: 
$$
\begin{equation*}
\begin{split}
&\sinh\frac{\alpha}{2}\,\cos\frac{\beta}{2} = 0, \\
&\\
&\cosh\frac{\alpha}{2}\,\sin\frac{\beta}{2} = \frac{\omega}{\omega_{0}},
\end{split}
\end{equation*}
$$
woraus man die folgenden Lösungen erhält: 
$$
\begin{equation}
\begin{split}
&\text{F\"ur }\omega<\omega_{0}:\\
&\alpha=0;\quad \beta=2\,\arcsin\left(\frac{\omega}{\omega_{0}}\right);\\
&\\
&\text{F\"ur }\omega>\omega_{0}:\\
&\alpha = 2\,\mathrm{arccosh}\left(\frac{\omega}{\omega_{0}}\right); \quad \beta=\pi.
\end{split}
\end{equation}
$$
D.h. **die (ideale) Drosselkette hat die Eigenschaft eines Tiefpasses**: Unterhalb der Grenzfrequenz weist sie **keine Dämpfung** auf, d.h. sie ist als Leitung **verlustfrei**. Oberhalb der Grenzfrequenz steigt die Dämpfung mit $\omega$ steil an. Die Phase des Ausgangssignals ist um $\pi$ zum Eingangssignal verschoben. 

## Essentials

Was Sie ab jetzt wissen sollten:

- Am Beispiel der (idealen) Drosselkette haben Sie gesehen, wie man mehrere **Vierpole in Reihe** schalten kann, um eine komplexe Schaltung zu erhalten.  
- Die **Drosselkette erbt ihre charakteristischen Eigenschaften vom $\pi$-Glied**, das ihr zugrunde lieg: $X_{0}$ und $\omega_{0}$ bleiben gleich, $\alpha$ und $\beta$ sind sind n mal größer, als beim $\pi$-Glied, wenn die Drosselkette aus n $\pi$-Gliedern besteht.
- Die Drosselkette ist ein **Tiefpass n-ter Ordnung** und schneidet hohe Frequenzen sehr steil ab. Früher wurden Drosselketten v.a. zur Signalverzögerung eingesetzt. Für eine ideale Drosselkette, die mit $Z_{0}$ abgeschlossen wird wird $U_{E}$ unverzerrt (d.h. dispersionsfrei) verzögert.  

## Testfragen

1. Wie kann man sich die Verläufe von $\alpha$ und $\beta$ für $\omega=0\ldots \infty$ bildlich vorstellen?
2. Was bedeuten $\alpha$ und $\beta$ anschaulich? Wie kann man sich also den Verlauf des Spannungssignals entlang der idealen Drosselkette vorstellen?

# Navigation

[Main](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/tree/main/Vierpole_und_Leitungen)
