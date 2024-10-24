# Hinweise für den Versuch Photoeffekt

## Versuchsdurchführung

### Aufgabe 2.1 Spannung $U_{\mathrm{Ph}}$ der Photozelle bei variierender Lichtfrequenz 

Die Photozelle hat zwei Kabel, einen 4-mm-Stecker, der mit der Kathode verbunden ist und ein BNC-Kabel, dessen Innenleiter mit der Anode verbunden ist (Der Außenleiter ist unverbunden). Verbinden Sie das BNC-Kabel mit M und den 4-mm-Stecker mit dem Erdungs-Eingang an M.

Gehen Sie zur Bestimmung von $h$ wie folgt vor: 

- Achten Sie auf eine zentrale und gute Ausleuchtung der Photozelle.

- Schalten Sie dann Schritt für Schritt einen Filter nach dem anderen vor den Lichtschutzkollimator der Photozelle. Die Filter sind aufsteigend in $\lambda_{\mathrm{CWL}}^{(i)}$ montiert. 

- Warten Sie, eine stabile Anzeige von $U_{\mathrm{Ph}}$ an M ab. Eine Messung von $U_{\mathrm{Ph}}$ ohne weitere Verstärkung (d.h. mit $v_{U}=1$) sollte ohne weiteres möglich sein. Protokollieren Sie den verwendeten Wert von $v_{U}$. 

- Nehmen Sie **mindestend drei bis fünf Messreihen** auf, bestimmen Sie den Messwert $U_{\mathrm{Ph}}^{(i)}$ durch Stichprobenmittelung, und die Unsicherheit $\Delta U_{\mathrm{Ph}}^{(i)}$ aus der Stichprobenvarianz. 

- Stellen Sie die Messpunkte $`(U^{(i)}_{\mathrm{Ph}},\ \lambda^{(i)}_{\mathrm{CWR}})`$ einschließlich der abgeschätzten Unsicherheiten $`(\Delta U^{(i)}_{\mathrm{Ph}},\ \Delta \lambda^{(i)}_{\mathrm{CWR}})`$ geeignet dar und passen Sie ein Modell der folgenden Form daran an:

  ```math
  \begin{equation*}
  U_{\mathrm{Ph}}^{(i)} = \frac{c\,h}{e}\frac{1}{\lambda^{(i)}_{\mathrm{CWL}}}+\frac{1}{e}W_{K}
  \end{equation*}
  ```

-  Geben Sie Ihr Messergebnis für $h$ und $W_{K}$ einschließlich Unsicherheiten an und diskutieren Sie es. Beziehen Sie in diese Diskussion auch den $\chi^{2}$-Wert der Anpassung mit ein. 

- Sowohl [$e=1.602176634\times10^{-19}\ \mathrm{C}$](https://de.wikipedia.org/wiki/Elementarladung) als auch [$c=2.99792458\times10^{8}\ \mathrm{m/s}$](https://de.wikipedia.org/wiki/Lichtgeschwindigkeit) sind SI-Einheiten definierende **Naturkonstanten, die ohne Unsicherheiten definiert sind**. Sie können diesen Umstand in Ihrer Anpassung an die Daten berücksichtigen, um $h$ direkt zu bestimmen. 

### Aufgabe 2.2: Photostrom $I_{\mathrm{Ph}}$ als Funktion einer angelegten externen Spannung $U_{o}$ bei variierender Lichtintensität

Schließen Sie hierzu den Widerstand mit $R=100\ \mathrm{M\Omega}$ parallel zum Messeingang von M. Nutzen Sie hierfür das BNC-T-Stück sowie den in eine BNC-Buchse integrierten Widerstand. Fügen Sie zusätzlich zwischen M und Kathode noch die Batterie-Spannungsquelle ein (achten Sie auf die korrekte Polung). Die Schaltung funktioniert, wie in **Abbildung 2** unten [hier](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Photoeffekt/doc/Hinweise-Photoeffekt.md) gezeigt.

- Der Strom berechnet sich dann aus
  ```math
  \begin{equation*}
  I_{\mathrm{Ph}}=\frac{U_{E}}{R\,v_{U}},
  \end{equation*}
  ```

  wobei $U_{E}$ die am Gerät ausgegebene Spannung und $v_{U}$ der eingestellte Verstärkungsfaktor sind. Zweckmäßige Spannungsintervalle für $U_{o}$ sind z.B.:

  - Von $-3.0\ \mathrm{V}$ bis $-0.5\ \mathrm{V}$ in Schritten von $\Delta U_{o}=0.1\ \mathrm{V}$.
  - Von $-0.5\ \mathrm{V}$ bis $3.0\ \mathrm{V}$ in Schritten von $\Delta U_{o}=0.5\ \mathrm{V}$.
  - Von $3.0\ \mathrm{V}$ bis $9.0\ \mathrm{V}$ in Schritten von $\Delta U_{o}=1.0\ \mathrm{V}$.

- Stellen Sie die Datenpunkte für die **Messung mit und ohne Graufilter** im gleichen Diagramm dar und passen Sie in einem geeigneten Bereich der Datenpunkte ein Modell an, aus dem Sie $U_{o}(I_{\mathrm{Ph}}=0)$ bestimmen können. Ein solches Modell könnte z.B. so aussehen:
  ```math
  \begin{equation*}
  I_{\mathrm{Ph}}= a\,(U_{o} + U_{E}) + I_{0},
  \end{equation*}
  ```

  wobei es sich bei $a$ und $I_{0}$ um freie Parameter handelt. 

- Bestimmen Sie die Reduktion der Lichtintensität durch den Graufilter, indem Sie z.B. dem obigen Diagramm ein Panel zufügen, in dem Sie das Verhältnis der gemessenen Werte mit und ohne Graufilter abtragen. Da $I_{\mathrm{Ph}}$ nur proportional zur Lichtintensität ist ist zu erwarten, dass das Verhältnis $I_{\mathrm{Ph}}^{\mathrm{Filter}}/I_{\mathrm{Ph}}$ nicht von $U_{o}$ abhängt. 

- Diskutieren Sie Ihre Ergebnisse einschließlich der $\chi^{2}$-Werte der gewählten Anpassungen und der erhaltenen Unsicherheiten sowohl für die Abschwächung des Graufilters, als auch für den Wert von $U_{o}(I_{\mathrm{Ph}}=0)$. 

### Aufgabe 2.3: Spannung $U_{o}(I_{\mathrm{Ph}}=0)$ bei variierender Lichtfrequenz

Nutzen Sie zur Bestimmung von $U_{o}(I_{\mathrm{Ph}}=0)$ den gleichen Aufbau wie in Aufgabe **Aufgabe 2.2**. Stellen Sie für jede Lichtfrequenz die Spannung $U_0$ so ein, dass kein Photostrom mehr fließt ($I_{\mathrm{Ph}}=0$).

Passen Sie an die erhaltenen Werte von $U_{o}^{(i)}(I_{\mathrm{Ph}}=0, \lambda_{\mathrm{CWL}}^{(i)})$ ein geeignetes Modell zur Bestimmung von $h$ an und vergleichen Sie das Ergebnis mit dem Ergebnis von Aufgabe **Aufgabe 2.1**. 

# Navigation

[Zurück](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Photoeffekt/doc/Hinweise-Versuchsdurchfuehrung.md) | [Main](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Photoeffekt)
