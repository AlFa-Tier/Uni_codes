# Hinweise für den Versuch: "Ideales und reales Gas" 

## Versuchsdurchführung [2/2]

### Aufgabe 2: Messung des Adiabatenexponenten $\kappa$ 

#### Aufgabe 2.1: Messung nach der Methode von  [Clément-Desormes](https://de.wikipedia.org/wiki/Experiment_von_Cl%C3%A9ment-Desormes)

- Erzeugen Sie mit dem Handblasebalg nicht zu viel Überdruck $\Delta p_{1}$, da sonst beim Druckausgleich im Übergang von **(1) nach (2)** Flüssigkeit vom Flüssigkeitsmanometer in K eindringen kann. 
- Achten Sie darauf, dass sich ein Gleichgewichtszustand eingestellt hat bevor Sie das Manometer ablesen.  
- Ein Schwachpunkt dieser Messung besteht in der Trägheit der Manometerflüssigkeit, die beim Übergang von **(2) nach (3)** in Schwingung versetzt wird. Diese beeinflusst den Druck beim Schließen des Ventils und damit direkt die Bestimmung von $\Delta p_{2}$. Versuchen Sie mit dem Schließen des Ventils den Nulldurchgang der Schwingung abzupassen. Dies wird einfacher, wenn Sie so weit wie möglich das Abklingen der Schwingung abwarten, wobei trotzdem $\delta Q\approx 0$ erfüllt bleiben sollte. Wir geben eine Wartezeit von ${\approx}3\ \mathrm{s}$ als Richtwert vor.  
- Führen Sie eine Messreihe mit mindestens 10 Einzelmessungen (Stichprobenlänge 10) durch und bestimmen Sie Messwert und Unsicherheit für $\kappa$ aus Mittelwert und Varianz der Stichprobe.  

#### Aufgabe 2.2: Messung nach der Methode von [Rüchardt](https://de.wikipedia.org/wiki/R%C3%BCchardt-Experiment) 

##### Originalmethode nach Rüchardt:

**Diese Messung führen Sie nur für Luft durch.**  

- In diesem Fall erzeugen Sie die Schwingung mit Hilfe einer Stahlkugel als Pfropfen, deren Durchmesser exakt mit dem Innendurchmesser eines Glasrohrs übereinstimmt, so dass sie das Glasrohr nahezu luftdicht verschließt. Das Glasrohr wird mit Hilfe eines durchbohrten Stopfens ebenfalls möglichst luftdicht auf eine der bereitgestellten $10\ \mathrm{l}$-Flaschen aufgesetzt. 
- Bei dieser Anordnung schwingt die Kugel auf einem Luftpolster mit großem Volumen $V$ während $A$ klein ist, $t$ ist daher groß genug, so dass Sie die Schwingung gut beobachten und $t$ gut bestimmen können.  Nehmen Sie für das Volumen dieses Luftkissens $V=10.58\ \mathrm{l}\pm0.3\%$ an.
- Bei Glasrohr und Stahlkugel handelt es sich um **Präzisionsanfertigungen, die mit größter Sorgfalt zu behandeln sind!** Damit die Kugel das Glasrohr luftdicht abschließen, sich aber gleichzeitig möglichst reibungsfrei darin bewegen kann müssen die folgenden Bedingungen so gut wie möglich erfüllt sein: 

  - Das Glasrohr muss möglichst genau senkrecht stehen.
  - Sowohl das Glasrohr, als auch die Stahlkugel müssen äußerst sauber sein. 
  - Alle Stopfen müssen luftdicht abschließen.
- Reinigen Sie Kugel und Rohrinnenfläche sorgfältig mit einem Lederlappen. **Berühren Sie die Kugel nach Möglichkeit niemals mit bloßen Fingern.** Sollte dies dennoch geschehen, wiederholen Sie den Reinigungsvorgang.

- Setzen Sie das Glasrohr so ein, dass der durchbohrte Stopfen möglichst luftdicht abschließt. 
- Lassen Sie die Kugel aus dem Lederlappen behutsam ins Glasrohr gleiten und bestimmen Sie $t$ aus möglichst vielen, mindestens aber 5 Schwingungen. 
- Wiederholen Sie diesen Vorgang mehrfach, um ein Maß für die Streuung zu erhalten. 
- Um die Kugel nach Beendigung einer Messreihe aus dem Rohr zu entnehmen, kippen Sie die Flasche –so lange die Kugel sich noch in der Glasröhre befindet– vorsichtig um und lassen Sie die Kugel in die bereitstehende Plastikschale gleiten.

##### Methode mit dem Kolbenprober

**Diese Messung führen Sie für Luft und für das Edelgas $\mathrm{Ar}$ durch.**  

- In diesem Fall ersetzt der Kolbenprober das Glasrohr und die Kugel; $V$ und somit $t$ sind deutlich geringer, als bei der originalen Anordnung von Rüchardt , so dass $t$ elektronisch, mit Hilfe eines angebrachten Magneten, einer Induktionsspule um den Kolbenprober und eines Frequenzzählers bestimmt wird. 

- Indem Sie die Induktionsspule entlang des Pfropfens verschieben können Sie die Werte von $V$ selbst bestimmen. Messen Sie mindestens 5 Werte für $t$ zwischen $V=30-80\ \mathrm{ml}$. Die Bestimmung von $\kappa$ erfolgt dann durch geeignete Anpassung des Zusammenhangs aus Gleichung **(3)** [hier](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Ideales_und_reales_Gas/doc/Hinweise-Ruechardt.md) an die gemessenen Wertepaare $(V_{i},\ t_{i})$.

  

- Führen Sie diese Messung erst mit Luft und dann mit $\mathrm{Ar}$ durch und überprüfen Sie, ob $\kappa$ mit der Erwartung

  ```math
  \begin{equation*}
  \kappa = \frac{f+2}{f}
  \end{equation*}
  ```

  aus der [kinetischen Gastheorie](https://de.wikipedia.org/wiki/Kinetische_Gastheorie) übereinstimmt, wobei $f$ der Anzahl der [Freiheitsgrade](https://de.wikipedia.org/wiki/Freiheitsgrad) des untersuchten Gases entspricht. Je nach Gas erwarten Sie die folgenden Werte für $f$: Edelgas: $f=3$, $\mathrm{O_{2}},\ \mathrm{N_{2}}: f=5$, $\mathrm{CO_{2}}: f=7$.


### Aufgabe 3: Dampfdruckkurve von n-Hexan

Bei diesem Versuch beobachten Sie den Phasenübergang zwischen flüssig und gasförmig von n-Hexan. 

- In einem Glaskolben befinden sich nur die Flüssigkeit und der Dampf von $1\ \mathrm{mol}$ n-Hexan. Der Dampfdruck wird mit einem direkt verbundenen $\mathrm{Hg}$-Manometer gemessen, dessen Stand Sie mit einem [Kathetometer](https://de.wikipedia.org/wiki/Kathetometer) ablesen können.

- Tauchen Sie den Kolben mit dem n-Hexan in ein Wärmebad, dessen Temperatur Sie so langsam verändern müssen, dass die Flüssigkeit und der Dampf an jedem Messpunkt im Gleichgewicht sind. Stellen Sie das Fernrohrokular des Kathetometers auf das Fadenkreuz ein. **Während der Messung darf am Fernrohr selbst daraufhin nichts mehr verändert werden.** 

- Zur Messung des Dampfdrucks bei Raumtemperatur visieren Sie die beiden $\mathrm{Hg}$-Kuppen nacheinander an und lesen die jeweilige Höhendifferenz an der Kathetometerskala ab. **Den Fokus auf die Kuppen müssen Sie dabei durch Verschieben des ganzen Gestells erreichen.** Für die weiteren Druckmessungen genügt es, wenn Sie nur noch eine der beiden Kuppen anvisieren.
- Achten Sie darauf, dass zu Beginn des Experiments kein flüssiges n-Hexan außerhalb des Wärmebads niedergeschlagen ist, was Ihre Messung verfälschen würde. Rühren Sie während des Versuchs das Wärmebad langsam um, so dass Sie eine möglichst homogene Temperaturverteilung erhalten.

- Nehmen Sie zunächst die Dampfdruckkurve bei langsam sinkender Temperatur auf. Geben Sie hierzu fein zerstoßene Eisstückchen ins Wärmebad. Nehmen Sie dann die Dampfdruckkurve bei langsam steigender Temperatur auf. Gießen Sie hierzu dem Wärmebad destilliertes Wasser zu.

- Bestimmen Sie dann durch geeignete Anpassung des Zusammenhangs aus Gleichung **(2)** [hier](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Ideales_und_reales_Gas/doc/Hinweise-Dampfdruckkurve.md) $Q_{\mathrm{M}}$. Wenn Sie für beide Messreihen vergleichbare Werte für $Q_{\mathrm{M}}$ erhalten, können Sie davon ausgehen, dass Sie den Gleichgewichtszustand zwischen flüssig und gasförmig erfolgreich präpariert haben. 

- Der Verlauf der Dampfdruckkurve folgt Gleichung **(2)** [hier](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Ideales_und_reales_Gas/doc/Hinweise-Dampfdruckkurve.md) nicht perfekt. Dies geht z.T. auf Näherungen zurück, die wir bei der Herleitung dieses Zusammenhangs vorgenommen haben, die für n-Hexan nicht erfüllt sein mögen. Zudem kann die Messung auch durch den Dampfdruck des $\mathrm{Hg}$ beeinflusst werden. Diskutieren Sie die gemachten Annahmen unter Eingeziehung des $\chi^{2}$-Wertes der Anpassung.

# Navigation

[Zurück](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Ideales_und_reales_Gas/doc/Hinweise-Versuchsdurchfuehrung.md) | [Main](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Ideales_und_reales_Gas)

