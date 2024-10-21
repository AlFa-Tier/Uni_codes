# Hinweise für den Versuch Vakuum

## Aufgabe 1: Versuchsaufbau

### Aufgabe 1.1: Orientierung und Beschreibung des Versuchsaufbaus

- Folgen Sie hierzu den Leitungen und identifizieren Sie die verwendeten Elemente mit den Schaltelementen aus **Abbildung 2** [hier](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Vakuum/README.md). Für den weiteren Verlauf des Versuchs sollten Sie eine gute Übersicht über den Aufbau der Apparatur haben.

- Sie sollten den Versuchsaufbau im folgenden Zustand vorfinden:  

  - Alle Apparaturen sind bei Atmosphärendruck belüftet. 
  - VS ist mit Indium bestückt.
  - Die Glasglocke wurde von alten Aufdampfbelägen gereinigt. 

  Vermerken Sie den Zustand des Experiments entsprechend in Ihrem Protokoll. 

- Die drei Versuchsaufbauten sind nicht gleich; **Apparatur 44** ist als einzige mit der Gasentladungsröhre für **Aufgabe 1.2** ausgestattet, dafür fehlt dort die Möglichkeit zur Messung der Überschlagsfestigkeit für **Aufgabe 3.2**.


### Aufgabe 1.2: Gasentladung (Demonstrationsversuch)

- Bei diesem Versuchsteil handelt es sich um einen Demonstrationsversuch, den alle Gruppen gemeinsam mit Ihrem:r Tutor:in durchführen. 
- Evakuieren Sie RZ und die Gasentladungsröhre gemeinsam mit Hilfe der DSP. Dabei sollten die Ventile V1 und V2 geöffnet sein. Die TMP bleibt für diesen Versuchsteil außer Betrieb. 
- Das Hochspannungsgerät zur Erzeugung der Gasentladungen sollte zu jedem Zeitpunkt eingeschaltet sein. 
- Schließen Sie nach dieser Aufgabe das Ventil zur Gasentladungsröhre für alle folgenden Aufgaben.

## Aufgabe 2: Saugvermögen und Strömungsleitwert

### Aufgabe 2.1: Saugvermögen der DSP

- Nehmen Sie hierzu fünf Minuten lang alle fünf Sekunden einen Messpunkt **bei T1** auf und stellen Sie $p(t)$ geeignet graphisch dar. Schätzen Sie hierzu geeignete Unsicherheiten auf $t$ und $p$ ab.
- Nutzen Sie zur Bestimmung von $S$ Gleichung **(5)** [hier](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Vakuum/doc/Hinweise-Vakuum.md), wobei $t_{0}$ der Zeit zu Beginn der Evakuation und $V$ dem Volumen der **gesamten Apparatur** entsprechen. 
- Diskutieren Sie Ihre Ergebnisse. Sie sollten abhängig von $p$ grob drei Bereiche identifizieren können:
  - **Bereich I**: Hier nimmt $S(p)$ mit abnehmendem Druck zu;
  - **Bereich II**: hier gilt über einen großen Druckbereich $S(p)\approx const.$;
  - **Bereich III**: Hier nimmt $S(p)$ mit abnehmendem Druck wieder ab (das Grob- geht ins Fein- und Hochvakuum über).
  - In **Bereich II** ist Gleichung **(5)** [hier](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Vakuum/doc/Hinweise-Vakuum.md) über einen Druckbereich von mehreren Größenordnungen anwendbar. Stellen Sie $p(t)$, eingeschränkt auf diesen Bereich als Funktion der Zeit dar und passen Sie das Modell eines exponentiellen Verlaufs, wie in Gleichung **(5)** [hier](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Vakuum/doc/Hinweise-Vakuum.md) an die Daten an. Gehen Sie bei der Diskussion auf den $\chi^{2}$-Wert dieser Anpassung ein.   
- Schalten Sie nach der Messung die DSP ab.

### Aufgabe 2.2: Strömungsleitwert eines dünnen Rohrs 

- Zeichnen Sie fünf Minuten lang etwa alle fünf Sekunden den zeitlichen Verlauf des Drucks **jeweils bei T1 und T2** auf. 
- Stellen Sie $p_{1}$ (**bei T1**) vor und $p_{2}$ (**bei T2**) hinter dem Rohr als Funktion der Zeit dar. 
- Bestimmen Sie $S_{1}$ und $S_{2}$. Das zu verwendende Rohr hat einen Innendurchmesser von $d=2\,\mathrm{mm}$. Berücksichtigen Sie bei den Berechnungen, dass sich durch den Austausch des Metallwellschlauchs durch das Rohr das Gesamtvolumen $V$ der Apparatur verändert hat. 
- Diskutieren Sie Ihre Ergebnisse und vergleichen Sie den von Ihnen bestimmten Wert für $L$ mit der Erwartung nach der [Knudsen-Gleichung](https://en.wikipedia.org/wiki/Knudsen_equation) (Gleichung **(4)** [hier](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Vakuum/doc/Hinweise-Vakuum-a.md)).
- Schalten Sie die DSP nach der Messung ab, belüften Sie RZ und tauschen Sie das Metallrohr wieder gegen den Metallwellschlauch aus.

### Aufgabe 2.3: Saugvermögen der TMP

Diese Aufgabe dient in erster Linie dazu Ihnen die Möglichkeit zu geben, sich mit der TMP, als einer Hochleistungspumpe vertraut zu machen. 

- Da die TMP bis zur vollen Saugleistung eine Anlaufzeit von ca. $2\,\mathrm{min}$ benötigt, sollte sie nicht erst bei sehr niedrigem Druck eingeschaltet werden. Die Apparatur sollte vor Beginn dieses Versuchsteils mindestens bis zu einem Druck von $\approx0.2\ \mathrm{mbar}$ teilbelüftet sein. Evakuieren Sie die Apparatur dann mit der DSP und schalten Sie bei einem Druck von $\approx0.08\ \mathrm{mbar}$ die TMP zu. 
- Halten Sie während des gesamten Vorgangs der Evakuierung das Ventil V3 geöffnet, damit Sie höhere Drucke bei T3 ablesen können. 
- Lesen Sie bei geeignet niedrigen Drucken den Druck bei IM ab. 
- Lassen Sie die TMP für den nächsten Versuchsteil eingeschaltet.

## Aufgabe 3: Experimente im Vakuum

### Aufgabe 3.1: Statische Kalibration von T3 

Für diese Aufgabe führen Sie ein einstufiges, statisches Kalibrierungsverfahren, unter Anwendung des Gesetzes von [Boyle-Mariotte](https://en.wikipedia.org/wiki/Boyle%27s_law) für T3 durch. Gehen Sie hierzu iterativ, wie folgt vor:

- In der Ausgangssituation sollte V3 geschlossen, B2 geöffnet und RZ mit Hilfe der DSP und der TMP evakuiert sein. 

- Schließen Sie V2 bei einem Druck von $p\lesssim10^{-4}\,\mathrm{mbar}$ und trennen Sie damit RZ vom Rest der Apparatur ab. Sie können die beiden Pumpen daraufhin abschalten. 

  - **Schritt 1:** Schließen Sie B2. Öffnen Sie daraufhin V3 und lesen Sie den sich einstellenden Druck **bei T3** ab. 
  - **Schritt 2:** Schließen Sie V3 und öffnen Sie daraufhin B2, damit sich im kleineren Referenzvolumen (RV [hier](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Vakuum/figures/VakuumSkizze.png)) erneut Atmosphärendruck ($p_{0}$) einstellen kann.

- Wiederholen Sie diesen Vorgang beginnend mit **Schritt 1**, solange bis sich in RZ ein Druck von $p\approx80\,\mathrm{mbar}$ einstellt. Warten Sie jeweils den Druckausgleich im Gleichgewichtszustand ab. 

- Stellen Sie den Druckverlauf als Funktion der durchgeführten Iterationen $i$ dar und bestimmen Sie das [Verdichtungsverhältnis](https://de.wikipedia.org/wiki/Verdichtungsverh%C3%A4ltnis) 

  ```math
  \begin{equation*}
  \epsilon=\frac{\Delta p}{p_{0}}
  \end{equation*}
  ```

  des Systems. Schätzen Sie für die Messwerte $p_{i}$ geeignete Unsicherheiten ab. Es sollte sich ein linearer Zusammenhang einstellen. Überlegen Sie sich die Gründe für eventuelle Abweichungen.

Für den Druck nach einer Iteration gilt: 
$$
\begin{equation}
\begin{split}
&\bigl(p_{\mathrm{RZ}}+\Delta p\bigr)\,\bigl(V_{\mathrm{RZ}}+V_{\mathrm{RV}}\bigr) = \bigl(n_{\mathrm{RZ}}+n_{\mathrm{RV}}\bigr)\,R\,T; \\
&\\
&\text{mit:}\\
&\\
&n_{\mathrm{RZ}} = \frac{p_{\mathrm{RZ}}\,V_{\mathrm{RZ}}}{R\,T};\qquad
n_{\mathrm{RV}} = \frac{p_{0}\,V_{\mathrm{RV}}}{R\,T} \\
&\\
&\bigl(p_{\mathrm{RZ}}+\Delta p\bigr)\,\bigl(V_{\mathrm{RZ}}+V_{\mathrm{RV}}\bigr) = p_{\mathrm{RZ}}\,V_{\mathrm{RZ}}+p_{0}\,V_{\mathrm{RV}};\\
&\\
&V_{\mathrm{RV}} = \frac{\Delta p\,V_{\mathrm{RZ}}}{p_{0}-\left(p_{\mathrm{RZ}}+\Delta p\right)}\approx\frac{\Delta p\,V_{\mathrm{RZ}}}{p_{0}}; \\
&\\
&\epsilon=\frac{\Delta p}{p_{0}}\approx\frac{V_{\mathrm{RV}}}{V_{\mathrm{RZ}}}, \\
\end{split}
\end{equation}
$$
wobei $p_{\mathrm{RZ}}$ und $V_{\mathrm{RZ}}$ dem Druck und Volumen im Rezipienten und $V_{\mathrm{RV}}$ dem Referenzvolumen entsprechen. Vergleichen Sie Ihr Ergebnis mit dieser Erwartung. Beziehen Sie in Ihre Diskussion den $\chi^{2}$-Wert der Anpassung mit ein. 

**NB:** Aus der Näherung in Gleichung **(1)** können Sie abschätzen, dass $\Delta p$ mit zunehmender Anzahl an Iterationen abnehmen sollte. Für $p_{\mathrm{RZ}}\approx80\ \mathrm{mbar}$ liegt der Effekt bereits bei ${\approx 8\%}$.  

### Aufgabe 3.2: Elektrische Durchschlagfestigkeit

Die elektrische Durchschlagfestigkeit quantifizieren wir durch die Spannung, ab der es zwischen den KE zu elektrischen Entladungen kommt.  

- Schalten Sie hierzu zunächst die TMP aus und evakuieren Sie RZ nur mit Hilfe der DSP. 
- Schließen Sie nach erreichen des gewünschten Drucks jeweils V1, so dass der Druck in RZ während der sich anschließenden Messung konstant bleibt.
- Beginnen Sie mit der belüfteten Apparatur bei Atmosphärendruck und erhöhen Sie die Spannung zwischen den KE bis zur Entladung. 
- Evakuieren Sie daraufhin RZ bis auf halben Atmosphärendruck. Erhöhen Sie die Spannung bis zur Entladung. 
- Wiederholen Sie diese Vorgehensweise bis Sie einen Druck von $p\approx0.08\ \mathrm{mbar}$ erreicht haben. In diesem Druckbereich wird es zunehmend schwieriger den Druck in RZ konstant zu halten. Um leichter und schneller an weitere Messwerte zu gelangen, evakuieren Sie nun zusätzlich und ohne Unterbrechung mit der TMP bis zu einem Druck von $p\lesssim10^{-4}\ \mathrm{mbar}$. 
- Schalten Sie die TMP aus und schließen Sie V2. Der Druck in RZ wird nun von selbst steigen. 
- Nehmen Sie sobald wie möglich (für $U \leq9\ \mathrm{kV}$) weitere Messwerte auf. Die Messreihe endet, wenn ein Druck von $p\approx0.08\ \mathrm{mbar}$ erreicht ist.
- Diskutieren Sie in Ihrer Auswertung die folgenden Punkte: 
  - Warum lässt sich der Druck ab einem bestimmten Druckbereich nicht mehr genau einstellen und warum steigt er bei sehr kleinen Werten kontinuierlich an? 
  - Beschreiben Sie Ihre Beobachtungen bei der Gasentladung in den entsprechenden Druckbereichen. 
  - Erklären Sie den Verlauf der elektrischen Durchschlagfestigkeit mit Hilfe der mittleren freien Weglänge $\lambda$.

Sie können $\lambda$, wie für den [Franck-Hertz-Versuch](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Franck_Hertz_Versuch), wie folgt abschätzen: 
$$
\begin{equation*}
\begin{split}
&\lambda = \frac{1}{\sigma\,n} = \frac{k_{B}\,T}{\sigma\,p_{\mathrm{RZ}}};\\
&\\
&\text{mit:}\\
&\\
&\sigma= \pi\,r^{2};\qquad r=\sqrt[3]{\frac{3}{4\pi}V};
\qquad V= \frac{M_{m}\,f}{N_{A}\,\rho_{\mathrm{fl}}},\\
\end{split}
\end{equation*}
$$
wobei $N_{A}$ der [Avogradro-Konstanten](https://de.wikipedia.org/wiki/Avogadro-Konstante),  $M_{m}$ der [molaren Masse](https://de.wikipedia.org/wiki/Molare_Masse), $\rho_{\mathrm{fl}}=807\ \mathrm{g/\ell}$ der Dichte von flüssigem $\mathrm{N}_{2}$ und $f\approx0.74$ dem Füllfaktor der [dichtesten Kugelpackung](https://de.wikipedia.org/wiki/Dichteste_Kugelpackung) entsprechen. Schätzen Sie daraus und aus der Bestimmung der elektrischen Durchschlagfestigkeit den Abstand der KE ab. 

### Aufgabe 3.3: Aufdampfen von Indium

Bei dieser Aufgabe dampfen Sie bei verschiedenen Drucken jeweils eine Indium-Schicht durch eine Kreisblende auf eine schwenkbare Plexiglasplatte auf. Es soll jeweils ein Fleck bei einem Druck von 

- $p\lesssim10^{-4}\,\mathrm{mbar}$ und 
- $p\lesssim10^{-3}\,\mathrm{mbar}$ 

aufgedampft werden. 

Diskutieren Sie die Randschärfe der aufgedampften Flecken. Gehen Sie dabei wie folgt vor: 

- Evakuieren Sie RZ mit der TMP; 
- schließen Sie V2; 
- dampfen Sie den ersten Fleck bei minimal erreichbarem Druck ($p\lesssim10^{-4}\,\mathrm{mbar}$) auf; 
- dampfen Sie den zweiten Fleck bei $p\approx10^{-3}\,\mathrm{mbar}$ auf. 

**Achtung: Die verfügbare Heizleistung reicht aus, um HZ vollständig zu zerstören!** Der Heizstrom darf daher erst sehr langsam nach oben geregelt werden, sobald das gewünschte Vakuum für den ersten Fleck erreicht ist. Beobachten Sie HZ beim Hochregeln des Heizstroms. Es soll zwar glühen, aber nicht schmelzen. 

#### Wiederherstellung des Anfangszustands der Apparatur

Stellen Sie im Anschluss, für Ihre Nachfolger:innen, den Anfgangszustand der Apparatur wieder, wie folgt her: 

- Belüften Sie die Apparatur; 
- reinigen Sie die Plexiglasplatte und die Glasglocke von eventuellen Aufdampfbelägen; 
- bestücken Sie HZ mit etwas Indium (lassen Sie die Menge vom Betreuer überprüfen); und 
- setzen Sie die Glocke wieder auf den Dichtungsring.

# Navigation

[Main](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Vakuum)
