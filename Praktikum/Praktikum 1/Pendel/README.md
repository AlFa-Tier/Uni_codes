<img src="../figures/Logo_KIT.svg" width="200" style="float:right;" />

# Fakultät für Physik 

## Physikalisches Praktikum P1 für Studierende der Physik



Versuch P1-80, 81, 82 (Stand: **Oktober 2024**)

[Raum F1-11](https://labs.physik.kit.edu/img/Klassische-Praktika/Lageplan_P1P2.png)



# Pendel



## Motivation

Die [Schwingung](https://de.wikipedia.org/wiki/Schwingung) ist eine überall in der Natur auftretende Bewegungsform und deshalb in der Physik von besonderer Bedeutung. Mit diesem Versuch untersuchen Sie Schwingungen in ihrer einfachsten Form, als mechanische Schwingungen von [Pendeln](https://de.wikipedia.org/wiki/Pendel). Der erste neuzeitliche Forscher, dessen Beschäftigung mit Pendeln dokumentiert ist ist [Galileio Galilei](https://de.wikipedia.org/wiki/Galileo_Galilei) mit einer Schrift zur Untersuchung von Pendeln (1602). Er soll durch die gleichmäßigen Schwingungen eines Leuchter im [Dom zu Pisa](https://de.wikipedia.org/wiki/Dom_zu_Pisa) zu seinen Untersuchungen angeregt worden sein. Damals waren Pendelbewegungen nicht zu erklären, die kanonische Beschreibung der Natur basierte auf den Werken von [Aristoteles](https://de.wikipedia.org/wiki/Aristoteles), der natürliche von erzwungenen Bewegungen unterschied. Als natürliche Bewegung galt z.B. der Fall eines Steins zur Erde. Warf man einen Stein nach oben, galt dies als erzwungene Bewegung, die nach und nach wieder in die natürliche Bewegung nach unten (zur Erde hin) überging. Beim Pendel war ein solcher Übergang von einer erzwungenen in eine natürliche Bewegung nicht zu beobachten. Galilei beobachtete und dokumentierte als erster, dass die Periode $T_{0}$ eines schwingenden Pendels nicht von der schwingenden Masse sondern allein von der Länge des Pendels abhängt. Er behauptete allerdings auch, dass die Periode nicht von der Auslenkung der Pendels anhänge, ein Punkt in dem Sie ihn widerlegen werden. 

Auf Seiten der Erfassung und Verarbeitung von Daten zählen Untersuchungen an Pendeln zu den Blaupausen moderner, physikalischer Messungen. Jeder physikalischen Messung liegt heute ein (physikalisches) Modell zugrunde. Mit der Messung von $T_{0}$ führen Sie stichprobenartig [Zusallsexperimente](https://de.wikipedia.org/wiki/Zufallsexperiment) durch,  deren zufallsbedingte Unsicherheiten (ausgedrückt durch deren [Varianz](https://de.wikipedia.org/wiki/Varianz)) Sie mit Methoden der Statistik abschätzen können. Aus der [Stichprobe](https://de.wikipedia.org/wiki/Stichprobe) ermitteln Sie einen [Erwartungswert](https://de.wikipedia.org/wiki/Erwartungswert) mit entsprechenden Unsicherheiten (die Sie wiederum aus der [Stichprobenvarianz](https://de.wikipedia.org/wiki/Stichprobenvarianz_(Sch%C3%A4tzfunktion)) abschätzen können), oder Sie [schätzen](https://de.wikipedia.org/wiki/Sch%C3%A4tzfunktion) Parameter, wie die Erdbeschleunigung im Schwerefeld der Erde $g$, innerhalb des zugrunde gelegten Modells mit entsprechenden Unsicherheiten. Irgendwo auf dem Weg zwischen einer noch unsicheren Entdeckung bis zu einer unumstößlichen Gewissheit, manifestiert sich die physikalisch reproduzierbare Beobachtung, die wir als Tatsache empfinden. Aus dieser Umschreibung können Sie erkennen wie eng unser heutiges Verständnis physikalischer Messungen mit den Methoden der Statistik verbunden ist.    

## Lehrziele

Wir listen im Folgenden die wichtigsten **Lehrziele** auf, die wir Ihnen mit dem Versuch **Pendel** vermitteln möchten: 

- Sie führen systematische Untersuchungen an den Schwingung von Pendeln durch. Die Phänomene, die Sie mit gekoppelten Pendeln aber auch mit dem Reversionspendel beobachten sind z.T. überraschend und nicht-trivial.  
- Sie schätzen den Einfluss der endlichen Ausdehnung physikalischer Körper auf die Bewegung der untersuchten Pendel ab und vergleichen Ihre Abschätzungen mit der Beobachtung.
- Sie üben sich anhand der einfachen Aufbauten im **sorgfältigen Experimentieren und Messen, unter Laborbedingungen**.
- Dieser Versuch eignet sich, aufgrund der allgemein gut bekannten zugrunde liegenden physikalischen Modelle, sehr gut dazu sich eingehender mit den Aspekten numerischer Anpassungen an Messdaten und der sorgfältigen Abschätzung statistischer und systematischer Unsicherheiten zu beschäftigen.

## Versuchsaufbau

Mit diesem Versuch stehen Ihnen mehrere größere Pendel zur Verfügung, um deren Schwingungsverhalten zu untersuchen. Im Folgenden sind die wichtigsten Informationen der verwendeten Aufbauten kurz zusammengefasst. Die angegebenen Größen finden Sie auch im [Datenblatt](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/Pendel/Datenblatt.md) zum Versuch und in *python*-Modulen im *params*-Verzeichnis, auf dem Gitlab-Server des SCC. 

### [Fadenpendel](https://de.wikipedia.org/wiki/Mathematisches_Pendel)

Der Aufbau des Fadenpendels ist in **Abbildung 1** gezeigt:

---

<img src="./figures/Fadenpendel.png" style="zoom:60%;" />

**Abbildung 1**: (Aufbau des Fadenpendels)

---

Eine Kugel hängt an einem dünnen Stahldraht der Länge $L=(2.355\pm0.003)\ \mathrm{m},$ gemessen von der Aufhängung des Drahts bis zum Mittelpunkt der Kugel. Die aktuelle Länge und entsprechende Unsicherheit sind ggf. im Praktikumsraum ausgehängt. Die Kugel hat eine Masse von $m=(860\pm0.5)\ \mathrm{g}$. Die Messung von $T_{0}$ erfolgt über eine Lichtschranke und eine zugehörige Messautomatik. An der Wand hinter dem Pendel befindet sich eine Winkelskala. 

### [Reversionspendel](https://de.wikipedia.org/wiki/Reversionspendel)

Ein typischer Aufbau des Reversionspendels ist in **Abbildung 2** gezeigt:

---

<img src="./figures/Reversionspendel.png" style="zoom:60%;" />

**Abbildung 2**: (Ein typischer Aufbau des Reversionspendel)

---

An einem Stativ hängt ein [physikalisches Pendel](https://de.wikipedia.org/wiki/Physikalisches_Pendel), bestehend aus einem dünnen zylindrischen Stab (mit Abmessungen, wie in der Skizze angegeben). Der obere Auflagekeil K ist fest montiert, der untere Auflagekeil K' ist um 90° relativ zu K gedreht und lässt sich entlang des Stabs verschieben. Im Praktikumsraum befinden sich zwei Aufbauten (R1 und R2) für die sich die Massen der Montagespangen für K und K' (wie in der Skizze angegeben) leicht unterscheiden. Die Auflagepunkte von K und K' befinden sich jeweils im Abstand $\Delta=1.0\ \mathrm{cm}$ vom Rand der jeweiligen Montagespange zur Halterung entfernt. Die Messung von $T_{0}$ erfolgt über eine Lichtschranke und eine zugehörige Messautomatik.

### [Gekoppelte Pendel](https://de.wikipedia.org/wiki/Gekoppelte_Pendel)

Ein typischer Aufbau für die Versuche mit den gekoppelten Pendeln is in **Abbildung 3** gezeigt:

---

<img src="./figures/GekoppeltePendel.png" style="zoom:60%;" />

**Abbildung 3**: (Ein typischer Aufbau für die Versuche mit gekoppelten Pendeln)

---

Zwei baugleiche physikalische Pendel bestehen aus einem langen, dünnen Stab und jeweils einer verschiebbaren, flach-zylinderförmigen Pendelscheibe mit Massen, wie in der Skizze angegeben. Schließt der Stab mit der jeweiligen Pendelscheibe bündig ab, beträgt der Abstand zwischen der Aufhängung des jeweiligen Pendels und dem Schwerpunkt der entsprechenden Pendelscheibe $L=1020\ \mathrm{mm}$. Der Radius jeder Pendelscheibe beträgt $r=50\ \mathrm{mm}$.  Die Federkopplungen (mit den Massen $m_{\kappa}=44\ \mathrm{g}$) können entlang des jeweiligen Stabs verschoben werden. Zur Kopplung, wie in der Abbildung gezeigt, stehen verschiedene [Schraubenfedern](https://de.wikipedia.org/wiki/Feder_(Technik)) zur Verfügung.

## Wichtige Hinweise zum Versuch

- Die einzelnen Aufgabenteile zu diesem Versuch lassen sich unabhängig voneinander durchführen und unterliegen keiner bestimmten Reihenfolge. 
- **Die Kugel des Fadenpendels kann Verletzungen verursachen!** Halten Sie daher Abstand, solange die Kugel weit ausschwingt. 
- Wenn Sie die Kugel in den Draht der Aufhängung "hineinfallen" lassen, gehen Sie das Risiko ein den Draht zu zerstören.

# Navigation

- [Pendel.iypnb](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/Pendel/Pendel.ipynb): Aufgabenstellung und Vorlage fürs Protokoll.
- [Pendel_Hinweise.ipynb](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/Pendel/Pendel_Hinweise.ipynb): Hinweise zu den Aufgaben.
- [Datenblatt.md](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/Pendel/Datenblatt.md): Technische Details zu den Versuchsaufbauten.
- [doc](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/tree/main/Pendel/doc): Dokumente zur Vorbereitung auf den Versuch.
- [figures](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/tree/main/Pendel/figures): Bilder, die für die Dokumentation des Versuchs verwendet wurden.

