# Hinweise für den Versuch Vakuum

## Grundbegriffe der Vakuumtechnik

In der Vakuuumtechnik bezeichnet man den Volumendurchfluss ([Volumenstrom](https://de.wikipedia.org/wiki/Volumenstrom#Normvolumenstrom), siehe Gleichung **(3)** [hier](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Vakuum/doc/Hinweise-Vakuum.md), für viskose Fluide) durch die Ansaugöffnung einer Pumpe als **Saugvermögen**

$$
\begin{equation*}
S\equiv\dot{V}.
\end{equation*}
$$
Je nach Druck und Temperatur ($T$) verändert sich die Stoffmenge ($n$) des geförderten Gases bei gleichem Volumendurchfluss.

Die Menge eines Gases kann durch seine Masse $m$ abgeschätzt werden. Bei Gasen gebräuchlicher ist jedoch die Angabe durch das Produkt $pV$, das nach der idealen Gasgleichung 

$$
\begin{equation*}
\begin{split}
& pV = n\,R\,T = \frac{m}{M_{m}}R\,T; \\
&\\
&m = \frac{pV}{R\,T}M_{m},
\end{split}
\end{equation*}
$$
bei bekannter Temperatur zur Massenangabe äquivalent ist. Dabei entspricht $M_{m}$ der [molaren Masse](https://de.wikipedia.org/wiki/Molare_Masse) der Gasmoleküle. Für eine Pumpe ist neben dem Volumen- der **Massenfluss**

$$
\begin{equation*}
q_{m}\equiv\dot{m}
\end{equation*}
$$
von Relevanz, der entsprechend auch als **$pV$-Durchfluss** (oder Gasmenge)

$$
\begin{equation*}
q_{pV} = \frac{\mathrm{d}(pV)}{\mathrm{dt}}
\end{equation*}
$$
angegeben wird. 

Die **Saugleistung** einer Pumpe wird (in Einheiten einer Leistung) durch $q_{pV}$ an der Ansaugöffnung der Pumpe angegeben. Bei konstantem Druck gilt der einfache Zusammenhang 

$$
\begin{equation*}
q_{pV} = \left.\frac{\mathrm{d}(pV)}{\mathrm{d}t}\right|_{p=const.} = p\dot{V} = p\,S.
\end{equation*}
$$
Die Größe $p\dot{V}$ haben Sie für viskose Fluide bereits in Gleichung **(4)** [hier](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Vakuum/doc/Hinweise-Vakuum.md) gesehen. 

Wenn wir beim Saugvorgang von einer adiabatischen Zustandsänderung des Gases ($\delta Q=0$) ausgehen erhalten wir: 

$$
\begin{equation*}
\begin{split}
\delta Q &= \mathrm{d}(pV) = 0;\\
&\\
&= p\,\mathrm{d}V  + V\,\mathrm{d}p \\
&\\
&= p\,S\,\mathrm{d}t  + V\,\mathrm{d}p;\\
&\\
\frac{\mathrm{d}p}{p} &= -\frac{S}{V}\mathrm{d}t,
\end{split}
\end{equation*}
$$
wobei $V$ dem Volumen der evakuierten Apparatur entspricht. Für eine Pumpe, die ein Gas aus einer Apparatur hinreichend großen Volumens $V$, ohne weiteren Wärmeaustausch absaugt, erwartet man also einen exponentiellen Verlauf des Drucks 

$$
\begin{equation}
\begin{split}
&\ln\left(\frac{p}{p_{0}}\right) = -\frac{S}{V}\left(t-t_{0}\right)\\
&\\
&p(t) = p_{0}\,\exp\left(-\frac{S}{V}\left(t-t_{0}\right)\right),
\end{split}
\end{equation}
$$
wobei $p_{0}$ dem Anfangs- (z.B. Umgebungs-)druck zum Zeitpunkt $t_{0}$ zu Beginn des Pumpvorgangs entspricht. 

## Strömungsleitwert und -widerstand

Laut Gleichung **(4)** [hier](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Vakuum/doc/Hinweise-Vakuum.md) ist die Saugleistung durch ein zylindrisches, hinreichend langes Rohr proportional zur Druckdifferenz $\Delta p$ an den Rohrenden. Den Proportionalitätsfaktor 
$$
\begin{equation}
L=\frac{\pi\,R^{4}\,\overline{p}}{8\,\eta\,\ell}
\end{equation}
$$
bezeichnet man als **Strömungsleitwert**, den Kehrwert von $L$ als **Strömungswiderstand** des Rohrs. Beide Größen lassen sich über den Zusammenhang 
$$
\begin{equation*}
q_{pV}\propto\Delta p
\end{equation*}
$$
allgemein definieren. Gleichung **(2)** gilt nur für viskose, laminare Fluide. Im allgemeinen hängt $L$ stärker vom Druck ab, als durch Gleichung **(2)** wiedergegeben, da sich druckabhängig die Art der Strömung verändert (siehe Abschnitt Vakuumbereiche [hier](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Vakuum/doc/Hinweise-Vakuum.md)). Zudem hängt $L$ von der Art des strömenden Gases, dem Querschnitt der Leitung, sowie dem Umstand ab, ob die Leitung geradlinig verläuft oder in irgendeiner Weise gekrümmt ist. 

Bei Parallelschaltung von Leitungen addieren sich die Saugleistungen, während der Druckunterschied gleich bleibt: 
$$
\begin{equation*}
\begin{split}
&q_{pV}^{\mathrm{(ges)}}= L_{\mathrm{ges}} \Delta p = q_{pV}^{(1)}+q_{pV}^{(2)}= L_{1}\Delta p + L_{2}\Delta p = \left(L_{1}+L_{2}\right)\Delta p;\\
&\\
&L_{\mathrm{ges}} = L_{1} + L_{2}.
\end{split}
\end{equation*}
$$
Bei Serienschaltung von Leitungen addieren sich die Druckunterschiede während die Saugleistung gleich bleibt: 
$$
\begin{equation*}
\begin{split}
&\Delta p_{\mathrm{ges}}= \Delta p_{1} + \Delta p_{2}; \\
&\\
&\frac{q_{pV}}{L_{\mathrm{ges}}} = \frac{q_{pV}}{L_{1}} + \frac{q_{pV}}{L_{2}};\\
&\\
&\frac{1}{L_{\mathrm{ges}}} = \frac{1}{L_{1}} + \frac{1}{L_{2}}.\\
\end{split}
\end{equation*}
$$
Es handelt sich dabei um ein Analogon zu den [Kirchhoffschen Regeln](https://de.wikipedia.org/wiki/Kirchhoffsche_Regeln) der Elektrizitätslehre mit den folgenden Ersetzungen: 
$$
\begin{equation*}
\begin{split}
\vphantom{\frac{\mathrm{d}p}{\mathrm{d}x}}\dot{V}\qquad&\longleftrightarrow \qquad I\\
\frac{\mathrm{d}p}{\mathrm{d}x}\qquad&\longleftrightarrow\qquad U \\
\vphantom{\frac{\mathrm{d}p}{\mathrm{d}x}}L\qquad&\longleftrightarrow\qquad\sigma \\
\vphantom{\frac{\mathrm{d}p}{\mathrm{d}x}}L^{-1}\qquad&\longleftrightarrow\qquad R. \\
\end{split}
\end{equation*}
$$

### Effektive Saugleistung

Eine Pumpe schließt nur selten direkt an die zu evakuierende Apparatur an. Ist dies nicht der Fall, ist das Saugvermögen der Pumpe durch den Gesamtleitwert der verbindenden Leitungselemente reduziert. 

Nimmt man an, dass sich die Temperatur des Gases während des Durchflusses durch die Leitungselemente nicht wesentlich ändert, so dass also der $pV$-Durchfluss durch die Leitungselemente konstant ist, so erhält man für das effektive Saugvermögen $S_{\mathrm{eff}}$ hinter den Leitungselementen den Zusammenhang 

$$
\begin{equation*}
\begin{split}
&q_{pV} = p_{1}\,S = p_{2}\,S_{\mathrm{eff}};\\
&\\
&S_{\mathrm{eff}} = \frac{p_{1}}{p_{2}}\,S.
\end{split}
\end{equation*}
$$


Für $S_{\mathrm{eff}}$ folgt also:

$$
\begin{equation*}
\begin{split}
&L = \frac{q_{pV}}{p_{2}-p_{1}} = \frac{p_{1}}{p_{2}-p_{1}}S = \frac{p_{2}}{p_{2}-p_{1}}S_{\mathrm{eff}};\\
&\\
&\frac{p_{2}}{p_{1}} = \frac{S}{L}+1;\\
&\\
&\frac{S_{\mathrm{eff}}}{L} = \left(1-\frac{p_{1}}{p_{2}}\right) = \left(1-\frac{L}{S+L}\right) = \frac{S}{S+L}; \\
&\\
&\left(S+L\right)\,S_{\mathrm{eff}} = S\,L; \\
&\\
&\frac{S+L}{S\,L} = \frac{1}{S_{\mathrm{eff}}} \\
&\\
&\frac{1}{L} + \frac{1}{S} = \frac{1}{S_{\mathrm{eff}}} \\
&\\
&S_{\mathrm{eff}} = \left(\frac{1}{L} + \frac{1}{S}\right)^{-1}. \\
\end{split}
\end{equation*}
$$

Die effektive Saugleistung der Pumpe ergibt sich also durch "Serienschaltung" mit den entsprechenden Leitungselementen.

### Knudsen-Gleichung

Setzt man in Gleichung **(2)** $\eta$ für Stickstoff ein erhält man die folgende gebräuchliche Ingenieursformel (für Luft bei $20^{\circ}\mathrm{C}$):
$$
\begin{equation}
\begin{split}
&L[\mathrm{l/s}] = \frac{\pi\,R^{4}\,\overline{p}}{8\,\eta\,\ell} = \frac{\pi\,\left(d[\mathrm{cm}]\right)^{4}\,\overline{p}[\mathrm{mbar}]\cdot 100}{1000\cdot8\cdot16\cdot17.58\times10^{-6}[\mathrm{Pa\,s}]\,\ell[\mathrm{cm}]} \\
&\hphantom{L[\mathrm{l/s}]}=140\frac{\left(d[\mathrm{cm}]\right)^{4}}{\ell[\mathrm{cm}]}\, \overline{p}[\mathrm{mbar}] \\
&\\
&\text{mit:}\\
&\\
&d=2\,R; \qquad
1\ \mathrm{Pa}=100\ \mathrm{mbar}; \qquad
\eta = 17.58\, \mu\mathrm{Pa\cdot s},\\
\end{split}
\end{equation}
$$
wobei $d$ dem Durchmesser der Leitung entspricht. Die eckigen Klammern geben an in welchen Einheiten die Messgrößen einzusetzen sind.

Im Feinvakuum nimmt Gleichung **(3)** die Form 
$$
\begin{equation}
L[\mathrm{l/s}] = 140\frac{d^{4}}{\ell}\overline{p} + 12.1\frac{d^{3}}{\ell}\frac{1+192\, d\,\overline{p}}{1+237\, d\, \overline{p}}
\end{equation}
$$
an. Dabei handelt es sich um die sog. **Knudsen-Gleichung**. Formt man Gleichung **(4)** wie folgt um kann man abhängig von der dimensionsbehafteten Skala $d\,\overline{p}[\mathrm{mbar\ cm}]$ die Bereiche von Grob-, Fein- und Hochvakuum unterscheiden:
$$
\begin{equation*}
\begin{split}
&\text{Übergang} (10^{-2}\lesssim d\,\overline{p}[\mathrm{mbar\cdot cm}]\lesssim0.6): \\
&\\
&L[\mathrm{l/s}] = 12.1\frac{d^{3}}{\ell}\cdot\underbrace{\frac{1+203\, d\, \overline{p} + 2.78\times 10^{3}\,\left(d\,\overline{p}\right)^{2}}{1+237\, d\, \overline{p}}}\\
&\hphantom{L[\mathrm{l/s}] = 12.1\frac{d^{3}}{\ell}1+203\, d\, \overline{p}c}\equiv f(d\,\overline{p}) \\
&\\
&\\
&\text{Viskos, laminar } (0.6\lesssim d\,\overline{p}[\mathrm{mbar\cdot cm}]): \\
&\\
&L[\mathrm{l/s}] = 140\frac{d^{4}}{\ell}\overline{p}\\
&\\
&\text{Molekular } (d\,\overline{p}[\mathrm{mbar\cdot cm}]\lesssim10^{-2}): \\
&\\
&L[\mathrm{l/s}] = 12.1\frac{d^{3}}{\ell}.\\
\end{split}
\end{equation*}
$$
Es fällt auf, dass der $L$ für molekulare Strömungen vom Druck unabhängig ist.   

# Navigation

[Zurück](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Vakuum/doc/Hinweise-Vakuum.md) | [Main](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Vakuum)



