# Hinweise für den Versuch Vakuum

## Wärmeleitungs-Vakuummeter

Das Wärmeleitungs- oder [Pirani-Vakuummeter](https://de.wikipedia.org/wiki/Pirani-Vakuummeter) nutzt zur Bestimmung des Drucks $p$ die Abhängigkeit der Wärmeleitung von Gasen von $p$. Im Vakuum befindet sich ein (meist aus Wolfram oder Nickel bestehender) Messdraht, der Bestandteil einer [Wheatstoneschen Messbrücke](https://de.wikipedia.org/wiki/Wheatstonesche_Messbr%C3%BCcke) ist. Der Widerstand $R$ des Drahts hängt von dessen Temperatur $\vartheta$ ab. Die am Draht anliegende Spannung wird so geregelt, dass $R=const$ gilt. Die dabei aufzuwendende elektrische Leistung entspricht im thermischen Gleichgewicht der abgeführten Wärmeleistung des Drahts. Abhängig vom Druck lässt sich die abgeführte Wärmeleistung in drei Bereiche aufteilen: 

- $p\lesssim10^{-4}\ \mathrm{mbar}$: Hier erfolgt der Wärmegang unabhängig von $p$ vor allem durch Wärmestrahlung des Drahtes und Wärmeableitung an den Drahtenden. 
- $10^{-4}\lesssim p \lesssim 1\ \mathrm{mbar}$: Hier erfolgt der Wärmegang vor allem durch die Wärmeleitung im Gas, diese ist i.a. linear von p abhängig. 
- $1\lesssim p\lesssim 10^{3}\ \mathrm{mbar}$: Hier erfolgt der Wärmegang durch Konvektion. Obwohl auch dieser i.a. unabhängig von $p$ ist gelingt es durch die Dimensionierung der Messsonde auch hier eine Abhängigkeit von $p$ zu realisieren, die jedoch i.a. nicht mehr linear ist und somit linearisiert werden muss. 

Wärmeleitungs-Vakuummeter sind daher über einen weiten Bereich von $10^{-4}\lesssim p \lesssim 10^{3}\ \mathrm{mbar}$ einsetzbar, in dem sie im %-Bereich reproduzierbare Angaben machen. Für die eingesetzen Geräte ([THERMOVAC Transmitter TTR91](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Vakuum/doc/LeyboldTN91_Tansducer.pdf)) macht der Hersteller die folgenden Angaben zur Messgenauigkeit: 

- $5\times10^{-4}\lesssim p \lesssim 10^{-3}\ \mathrm{mbar}$: $\pm10\%$ (of reading);
- $10^{-3}\lesssim p \lesssim 10^{2}\ \mathrm{mbar}$: $\pm5\%$ (of reading);

- $10^{2}\lesssim p \lesssim 10^{3}\ \mathrm{mbar}$: $\pm25\%$ (of reading);
- $10^{-3}\lesssim p \lesssim 10^{2}\ \mathrm{mbar}$: $\pm2\%$ (or reading) Reproduzierbarkeit;

## Ionisations-Vakuummeter

[Ionisations-Vakuummeter](https://de.wikipedia.org/wiki/Ionisations-Vakuummeter) basieren auf der Abhängigkeit des elektrischen Entladungsstroms einer evakuierten Diode von der Restteilchenzahldichte $n$. 

Aus einer Kathode werden unter Hochspannung Elektronen emittiert und im Feld der Hochspannung beschleunigt. Die Elektronen ionisieren die Restgasteilchen durch Stöße. Diese wandern als positiv geladene Ionen zur Kathode. Dort können Sie haften bleiben oder beim Auftreffen Material aus der Kathode ausschlagen (Kathodenzerstäubung). Das ausgeschlagene Material schlägt sich dann an den Wänden des Messgeräts nieder. Durch diesen Prozess wird die Kathode langsam verbraucht. Sie ist daher i.a. austauschbar.

Um auch bei sehr niedrigen Drücken und sehr kleinem $n$ einen messbaren Ionisationsstrom zu garantieren können die Elektronen durch ein zusätzlich angelegtes Magnetfeld auf einen Spiralbahn gezwungen werden, um ihren Weg durch die Ionisationskammer und damit die Wahrscheinlichkeit für Stößen mit Restgasteilchen zu erhöhen. Man bezeichnet dieses Vorgehen als invertiertes Magnetron-Prinzip und ein Messgerät, das nach diesem Prinzip funktioniert als Penning-Vakuummeter. Bei dem eingesetzten Gerät (PENNINGVAC PTR 225) handelt es sich um ein Penning-Kaltkathoden-Vakuummeter. Die Messgenauigkeit gibt der Hersteller mit $\pm30\%$ im Bereich $10^{-8}\lesssim p\lesssim 10^{-3}\ \mathrm{mbar}$ an.  

## Kalibration

Alle Vakuummeter müssen vor Betrieb kalibiert werden. Hierzu dienen *statische Kalibierungsverfahren* mit bekannten Messgeräten (z.B. U-Rohrmanometern, wie Sie sie im P2-Versuch [Ideales und reales Gas](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Ideales_und_reales_Gas) sehen können) oder *dynamische Kalibierungsverfahren* mit Hilfe von Pumpen bekannten Saugvermögens. 

Ein statisches Kalibierungsvefahren wenden Sie in **Aufgabe 3.1** an. Ein weiteres einfaches Verfahren läuft z.B. wie folgt ab: 

- Sie definieren mehrere bekannte Volumina $V_{i}$, die Sie durch Ventile voneinander trennen können. 

- Sie evakuieren alle Volumina bei zunächst geöffneten Ventilen. Daraufhin schließen Sie alle Ventile und isolieren die $V_{i}$ auf diese Weise voneinander.

- Im folgenden belüften Sie das Volumen $V_{0}$ und bestimmen den sich darin einstellenden Druck $p_{0}$, z.B. mit Hilfe eines bekannten Messgeräts G1; das zu kalibierende Messgerät kann in diesem Fall direkt gegen G1 abgeglichen werden. Isolieren Sie hierzu $V_{0}$ wieder von der Umgebung. 

-  Im folgenden öffnen Sie sukzessive ein Volumen nach dem anderen. Nach dem [Gesetz von Boyle-Mariotte](https://de.wikipedia.org/wiki/Thermische_Zustandsgleichung_idealer_Gase#Gesetz_von_Boyle-Mariotte) gilt 
  ```math
  \begin{equation*}
  p_{i+1}=\frac{\sum\limits_{k=0}^{i}V_{k}}{\sum\limits_{k=0}^{i+1}V_{k}}\cdot p_{i}.
  \end{equation*}
  ```

Auf diese Weise lässt sich das Gerät selbst außerhalb des Messbereichs von G1 kalibrieren. 

Ein dynamisches Kalibierungsverfahren würde z.B. wie folgt ablaufen:

- Sie statten einen Rezipienten R1 mit regelbaren Belüftungsventil, Referenzdruckmessgerät G1 und Pumpe P1 aus. 

- Sie verbinden R1 über ein Rohr mit bekanntem Leitwert $L$ mit einem zweiten Rezipienten R2, an dem sich das zu kalibierende Messgerät und eine weitere Pumpe P2 bekannter hoher effektiver Saugleistung $S_{\mathrm{eff}}$ befindet. 

- Im Betrieb ist der Druck $p_{2}$ in R2 durch 
  ```math
  \begin{equation*}
  p_{2}=\frac{L}{S_{\mathrm{eff}}}\,p_{1}
  \end{equation*}
  ```

  gegeben, wobei $p_{1}$ dem mit G1 gemessenen Druck in R1 entspricht. 

# Navigation

[Main](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Vakuum)



