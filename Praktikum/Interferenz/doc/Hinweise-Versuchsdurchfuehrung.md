# Hinweise für den Versuch "Interferenz"

## Aufgabe 1: Newtonsche Ringe

Machen Sie sich bevor Sie mit **Aufgabe 1** beginnen zunächst mit dem bereitgestellten Stereo-Zoom-Mikroskopen vertraut. Je besser Sie sich mit den bereitgestellten optischen Geräten zurechtfinden, desto besser und schneller können Sie die Versuche durchführen.

### Aufgabe 1.1: Krümmungsradius $R$ einer ausgewählten Linse

- Wählen Sie eine geeignete Linse aus. Positionieren Sie diese auf einen Objektträger auf dem verschiebbaren Objekttisch des Mikroskops.

- Als Auflichtquelle dient eine einfarbige LED-Leuchte, deren Licht von vorn über einen um $45^{\circ}$ gedrehten halbdurchlässigen Strahlteiler eingekoppelt wird. 

- Bestimmen Sie die Durchmesser $d_{k}=2r_{k}$ so vieler Newtonscher Ringe wie möglich. Verwenden Sie hierzu die Skala mit [Nonius](https://de.wikipedia.org/wiki/Nonius) auf dem Objekttisch und nicht die Skala des Fadenkreuzes, das in der Brennebene des Objektivs abgebildet wird. Schätzen Sie entsprechende Unsicherheiten $\Delta d_{k}$ ab. In manchen Fällen können Sie Newtonsche Ringe bis zur Ordnung $k=30$ beobachten!

- Tragen Sie die ermittelten Werte $d_{k}$ gegen $k$ auf und bestimmen Sie durch Anpassung eines geeigneten Modells $R$ mit entsprechenden Unsicherheiten $\Delta R$. Ein solches Modell wäre z.B.  
  ```math
  \begin{equation}
  d_{k} = \sqrt{4\,R\,\lambda}+C,
  \end{equation}
  ```

  wobei $\lambda$ der Wellenlänge des verwendeten LED-Lichts und $C$ einem weiteren freien Parameter des Modells entsprechen.

- **Führen Sie die Messung erst mit der gelben, dann mit der blauen LED-Leuchte durch.**

### Aufgabe 1.2: Brechungsindex $n(\mathrm{H_{2}O})$ von Wasser

- Fügen Sie einen Tropfen Wasser zwischen Linse und Objekträger und wiederholen Sie die Messung aus **Aufgabe 1.1** für eine LED-Leuchte, verwenden Sie aber eine Farbe, die Sie auch für **Aufgabe 1.1** verwendet haben! Durch die höhere optische Dichte $n(\mathrm{H_{2}O})$ von Wasser verändern sich die Abstände $d_{k}$.
- Tragen Sie für Ihre Auswertung die Wertepaare $(d_{k}, k)$ in das gleiche Diagramm, wie für die entsprechende Farbe in **Aufgabe 1.1** ein. Fügen Sie eine entsprechende Anpassung an die Messwerte zu und bestimmen Sie $n(\mathrm{H_{2}O})$.
- Beachten Sie, dass in einem Modell, wie in Gleichung **(1)** $\lambda$ und $R$ in beiden **Aufgaben 1.1** und **1.2** gleich anzunehmen sind! Für die zusätzliche Konstante $C$ ist dies nicht zwingend der Fall. Die genaueste Bestimmung erhalten Sie, wenn Sie eine gleichzeitige Anpassung an beide Messungen mit der gleichen Farbe der LED-Leuchte, mit Hilfe der Option [`MultiFit`](https://kafe2.readthedocs.io/en/latest/parts/beginners_guide.html#multifit) in kafe 2, wie z.B. [hier](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/Geometrische_Optik/doc/Hinweise-Aufgabe-2-b.md) beschrieben vornehmen.  

### Aufgabe 1.3: Brechungsindex $n_{L}$ der verwendeten Linse 

- Schätzen Sie die Unsicherheit $\Delta f$ auf die Brennweite $f$ geeignet ab. 
- Diskutieren Sie ob $\Delta R$ oder $\Delta f$ die Unsicherheit auf $\Delta n_{L}$ dominiert. 
- Vergleichen Sie Ihre Ergebnisse mit der optischen Dichte von Glas und ähnlichen Materialien und schätzen Sie ein, ob Ihnen das erzielte Ergebnis plausibel erscheint.  

## Aufgabe 2: Messungen mit dem Gitterspektrometer

### Aufgabe 2.1: Justierung der Apparatur

Eine genaue Beschreibung der Justierung mit zahlreichen Illustrationen finden Sie in den [Datenblättern zur Apparatur](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Interferenz/doc/Leybold-Versuch-Gitterspektrometer.pdf). Eine Kurzform der Anleitung ist im Folgenden wiedergegeben:  

- Einstellung der **Fernrohrs**:
  - Stellen Sie die Brennweite des Fernrohres (durch Verschieben des Okulars) auf "unendlich". Sie erreichen dies, z.B. indem Sie einen weit entfernten Gegenstand scharf einstellen. 
  - Bei richtiger Einstellung dürfen Kopfbewegungen zu keiner parallaktischen Verschiebung eines beobachteten Details und dem Fadenkreuz führen. 
  - Normalsichtige beobachten mit entspanntem (d.h. auf "unendlich" gerichtetem) Auge. Kurzsichtige können Parallellicht nicht auf die Netzhaut fokussieren und benötigen (ohne Kontaktlinse oder Brille) eine etwas abweichende Einstellung.
- Einstellung des **Spaltrohrs**:
  - Beleuchten Sie den Spalt mit der $\mathrm{Na}$-Spektrallampe. Beobachten Sie den schmal eingestellten Spalt durch das Fernrohr. Stellen Sie ihn durch Verschieben des Spaltes scharf und bringen Sie ihn dann durch Schwenken des Fernrohres mit dem Fadenkreuz zur Deckung. 
  - Stellen Sie den Spektrometertisch mit Teilkreis geeignet ein (Nullstellung) und arretieren Sie ihn. 
- Einstellung der **Gitterposition**:
  - Setzen Sie den Spiegel in den Gitterhalter ein (verwenden Sie hierzu einen weit geöffneten Spalt). Stellen Sie zwischen Spalt und Lampe einen Objektträger unter $45^{\circ}$ gegen die Achse aus Spalt- und Fernrohr auf, so dass von der Seite her über diesen "Strahlteiler" das vom Spiegel reflektierte Licht sichtbar wird, falls es durch den Spalt zurücktrifft. 
  - Der Spiegel (und damit der Gitterhalter) ist also senkrecht zur Achse justiert. Justieren Sie ggf. am Rändelrand des Gitterhalters nach. Stellen Sie dann den Spalt wieder schmal ein. 
  - Tauschen Sie schließlich den Spiegel gegen das Gitter aus.

### Aufgabe 2.2: Bestimmung der Gitterkonstanten $g$ eines Gitters

- Verwenden Sie das Gitter mit ${\approx}600\ \mathrm{mm^{-1}}$. Das Verhältnis zwischen Spaltbreite und Spaltabstand beträgt $b/g\approx0.9$. 

- Die Breite des Gitters ist mit $36\ \mathrm{mm}$ genügend groß, so dass Sie den ganzen Querschnitt des Parallellichtbündels im Spektrometer ausnutzen können. 

- Sie nutzen zur Messung das gelbe Licht der $\mathrm{Na}$-Spektrallampe. Legen Sie für Ihre Messungen die mittlere Wellenlänge $\langle \lambda\rangle=589,3\,\mathrm{nm}$ der Doppellinie des $\mathrm{Na}$-Spektrums zugrunde. Die Ausmessung des Abstands von $\delta\lambda\approx0.5\ \mathrm{nm}$ der beiden Linien ist **Aufgabe 2.3** vorbehalten.

- Tragen Sie den Winkel aller beobachtbaren Maxima gegen die Ordnung der Maxima auf und passen Sie ein geeignetes Modell an. Ein solches Modell wäre z.B.
  ```math
  \begin{equation}
  \sin\alpha = m\,\frac{\lambda}{g}+C,
  \end{equation}
  ```

  wobei $C$ und $g$ freie Parameter der Anpassung sind. Nehmen Sie für $\lambda$ eine geeignete Unsicherheit $\Delta \lambda$ an. 

### Aufgabe 2.3: Vermessung der $\mathrm{Na}$-D-Doppellinie

- Verwenden Sie $g\pm\Delta g$, wie durch Ihre Messung aus **Aufgabe 2.2** vorgegeben. Pflanzen Sie $\Delta g$ für die Messung entsprechend fort.  
- Es kann vorkommen, dass Sie die Breite $d$ des Spalts am Spaltrohr nochmal nachjustieren müssen, um die Auflösung der Doppellinie zu erhöhen (siehe [Hinweise zum Gitterspektrometer](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Interferenz/doc/Hinweise-Gitterspektrometer.md)). Dokumentieren Sie den Wert von $d$ für den Sie die beste Auflösung erhalten.

### Aufgabe 2.4: Bestimmung der Gitterkonstanten $g'$ eines zweiten Gitters

- Verwenden Sie das Gitter mit ${\approx}140\ \mathrm{mm^{-1}}$. Weitere Details der Gitterstruktur sind Ihnen nicht bekannt. Als Lichtquelle dient wieder die $\mathrm{Na}$-Spektrallampe.
- Tragen Sie den Winkel aller beobachtbaren Maxima gegen die Ordnung der Maxima auf und passen Sie ein geeignetes Modell an. Gehen Sie dabei, wie in **Aufgabe 2.2** vor. 

### Aufgabe 2.5: Linienspektrum der $\mathrm{Zn}$-Spektrallampe

- Wählen sie ein geeignetes Gitter aus; begründen und dokumentieren Sie Ihre Wahl. 

- Bestimmen Sie die Wellenlängen der vier deutlich erkennbaren Linien. Gehen Sie hierzu wie für **Aufgabe 2.2** vor. Verwenden Sie $g\pm\Delta g$, wie durch Ihre vorherige Messung vorgegeben. Pflanzen Sie $\Delta g$ für die Messung entsprechend fort. 


# Navigation

[Main](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Interferenz)

