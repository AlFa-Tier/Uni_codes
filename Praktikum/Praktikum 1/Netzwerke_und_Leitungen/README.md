<img src="../figures/Logo_KIT.svg" width="200" style="float:right;" />

# Fakultät für Physik

## Physikalisches Praktikum P1 für Studierende der Physik

Versuch P1-53, 54, 55 (Stand: September 2023)

[Raum F1-17](https://labs.physik.kit.edu/img/Praktikum/Lageplan_P1.png)



# Netzwerke und Leitungen

## Motivation

In der **stromleitungsgebundenen Signalübertragung** werden elektrische Signale i.d.R. durch mindestens zwei getrennte Leiter —einen Hin- und einen Rückleiter— übertragen. Für [Gleichstrom](https://de.wikipedia.org/wiki/Gleichstrom) oder [Wechselstrom](https://de.wikipedia.org/wiki/Wechselstrom) niedriger Frequenz lässt sich eine solche Leitung in guter Näherung mit Hilfe des [ohmschen Widerstands](https://de.wikipedia.org/wiki/Elektrischer_Widerstand#Ohmscher_Widerstand), bestimmt aus der Querschnittsfläche, [Leitfähigkeit](https://de.wikipedia.org/wiki/Leitf%C3%A4higkeit) und Länge der Leitung, beschreiben. Ist die [Wellenlänge](https://de.wikipedia.org/wiki/Wellenlänge) der übertragenen Signale jedoch so klein, oder die räumliche Ausdehnung eines Leitungssystems so groß, dass die Laufzeit der übertragenen Signale nicht mehr vernachlässigt werden kann, treten Wellenphänomene auf, die die Signalübertragung beeinflussen. Die Beschreibung dieser Phänomene erfordert mathematische Modelle, die den Ort des Signals mit einschließen.

Als erster beschäftigte sich 1855 [William Thomson](https://de.wikipedia.org/wiki/William_Thomson,_1._Baron_Kelvin) mit der Beschreibung der Vorgänge auf Leitungen. Die Notwendigkeit hierzu ergab sich aus der Verlegung transatlantischer [Seekabel](https://de.wikipedia.org/wiki/Seekabel), ab 1850, und die dabei auftretenden starken [Verzerrungen](https://de.wikipedia.org/wiki/Verzerrung_(Elektrotechnik)) der übertragenen Signale, die ein tieferes Verständnis der Vorgänge erforderten. Im Jahr 1886 formulierte [Oliver Heaviside](https://de.wikipedia.org/wiki/Oliver_Heaviside) die bis dato gewonnenen Erkenntnisse in ihrer heutigen Form als [Leitungsgleichungen](https://de.wikipedia.org/wiki/Leitungsgleichung) und begründete damit die allgemeine [Leitungstheorie](https://de.wikipedia.org/wiki/Leitungstheorie). [Rudolf Franke](https://de.wikipedia.org/wiki/Rudolf_Franke_(Ingenieur,_1870)) betrachtete die Leitung 1891 erstmals mit den Mitteln der [Vierpoltheorie](https://de.wikipedia.org/wiki/Zweitor). 

Die stromleitungsgebundene Signalübertragung spielt nicht nur bei der Übertragung von Singalen über große Strecken eine Rolle, sondern auch bei sehr schnell getakteten Signalen (z.B. im $\mathrm{GHz}$-Bereich), wie in modernen Computern. Auch bei der Planung nahezu aller Versuche, bei denen Sie Signale zur Weiterverarbeitung elektrisch aufnehmen, sollten Sie sich über die Eigenschaften der Signalübertragung in Kabeln im Klaren sein. 

## Lehrziele

Wir listen im Folgenden die wichtigsten **Lehrziele** auf, die wir Ihnen mit dem Versuch **Netzwerke und Leitungen** vermitteln möchten: 

- Sie üben sich in der Schaltung und **Berechnung komplexerer Netzwerke**. Die Berechnung erfolgt mit Hilfe der [Kirchhoffschen Regeln](https://de.wikipedia.org/wiki/Kirchhoffsche_Regeln).
- Alle zu untersuchenden Netzwerke enthalten Spulen und Kondensatoren. Sie werden ausschließlich mit **Wechselstrom** verschiedener Frequenzen betrieben. 
- Sie machen sich mit den Auswirkungen und Anwendungen von **induktiven und kapazitiven Impedanzen im Schaltkreisen** vertraut.
- Im Übergang vom einfachen Hoch- und Tiefpass, über die Drosselkette bis zum Koaxialkabel lernen Sie die unumgänglichen induktiven und kapazitiven **Eigenschaften von Leitungen** kennen. 
- Die Diskussion des Übergangs vom einfachen $\pi$-Glied zur Drosselkette bietet ein anschauliches Beispiel für Anwendungen der **[Vierpol-Theorie](https://de.wikipedia.org/wiki/Zweitor)** zur Berechnung komplexer Schaltungen.    

## Versuchsaufbau

Ein typischer Aufbau für den Versuch **Elektrische Messverfahren** ist in **Abbildung 1** gezeigt:

---

<img src="./figures/VierpoleAufbau.png" width="900" style="zoom:100%;" />

**Abbildung 1**: (Ein typischer Aufbau für den Versuch **Netzwerke und Leitungen**)

---

Der Versuch umfasst einen Frequenzgenerator, ein Oszilloskop zur Untersuchung der erzeugten Signale an verschiedenen Stellen der zu untersuchenden Schaltungen und eine geringe Anzahl vorgefertigter Steckbretter, an denen die zu untersuchenden Schaltungen entsprechen aufgebaut oder vervollständigt werden können. Für einfache Schaltungen stehen Ihnen verschiedene ohmsche Widerstände, Kondensatoren verschiedener Kapazität und eine Reihe von Koaxialkabeln, Brücken und Verbindungssteckern zur Verfügung. Eine Auflistung der für Ihre Auswertung wichtigen Bauelemente und deren Eigenschaften finden Sie im [Datenblatt](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/tree/main/Vierpole_und_Leitungen/Datenblatt.md) zu diesem Versuch.

## Wichtige Hinweise

- Gemeinsam mit den Versuchen [Elektrische Messverfahren](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/tree/main/Elektrische_Messverfahren) und [Messverstaerker](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/tree/main/Messverstaerker) gehört dieser Versuch zur Versuchsgruppe **Messverfahren**. Diese Versuche bauen aufeinander auf und sollten am besten nacheinander durchgeführt werden.  

# Navigation

- [Netzwerke_und_Leitungen.iypnb](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/Netzwerke_und_Leitungen/Netzwerke_und_Leitungen.ipynb): Aufgabenstellung und Vorlage fürs Protokoll.
- [Netzwerke_und_Leitungen_Hinweise.ipynb](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/Netzwerke_und_Leitungen/Netzwerke_und_Leitungen_Hinweise.ipynb): Hinweise zu den Aufgaben.
- [Datenblatt.md](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/Netzwerke_und_Leitungen/Datenblatt.md): Datenblatt zum Versuch.
- [doc](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/tree/main/Netzwerke_und_Leitungen/doc): Dokumente zur Vorbereitung auf den Versuch.
- [figures](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/tree/main/Netzwerke_und_Leitungen/figures): Bilder, die für die Dokumentation des Versuchs verwendet wurden.
