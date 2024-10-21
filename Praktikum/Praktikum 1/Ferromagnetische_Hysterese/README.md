<img src="../figures/Logo_KIT.svg" width="200" style="float:right;" />

# Fakultät für Physik

## Physikalisches Praktikum P1 für Studierende der Physik

Versuch P1-83, 84, 85 (Stand: September 2024)

[Raum F1-16](https://labs.physik.kit.edu/img/Praktikum/Lageplan_P1.png)



# Ferromagnetische Hysterese

## Motivation

Magnetische Felder werden durch bewegte Ladungen erzeugt und durch die **magnetischen Flussdichte** $\vec{B}$ in Richtung und Betrag quantifiziert. Sie können aber auch in selbst ohne Ströme permanent magnetisch Festkörpern erzeugt werden. Die bekannteste Art des [Magnetismus von Festkörpern](https://de.wikipedia.org/wiki/Magnetismus#Magnetismus_von_Festkörpern) ist der [Ferromagnetismus](https://de.wikipedia.org/wiki/Ferromagnetismus), wie er bei Eisen, aber auch bei Cobalt und Nickel vorkommt. Ferromagnetismus wird dadurch erklärt, dass die magnetischen Momente $\vec{m}$, die bei ferromagnetischen Materialien bereits auf atomarer Ebene bestehen und als [Elementarmagnete](https://de.wikipedia.org/wiki/Elementarmagnet) bezeichnet werden, sich auf makroskopischen Skalen parallel ausrichten. Diese Tendenz wird durch äußere magnetische Felder begünstigt und verstärkt. Im Gegenzug haben ferromagnetische Materialien die Eigenschaft magnetische Felder, in die sie eingebracht werden durch ihre eigene **Polarisation** $\vec{J}$ zu verstärken. Die Feldlinien der magnetischen Flussdichte $\vec{B}$ werden dabei förmlich in das ferromagnetische Material hineingezogen und dort verdichtet. Ferromagnete werden daher u.a. dazu verwendet magnetische Flusslinien zu verdichten, die Flussdichte lokal zu bündeln, Streufelder zu minimieren und Feldlinien, wie beim Transformator quasi zu führen. Der Teil eines magnetischen Feldes, der sich allein aus elektrischen [Leitungs-](https://de.wikipedia.org/wiki/Elektrischer_Strom) und [Verschiebungsströmen](https://de.wikipedia.org/wiki/Verschiebungsstrom), jedoch *nicht* aus der zusätzlichen Polarisation magnetischer Materie ergibt wird durch die **magnetische Feldstärke** $\vec{H}=\vec{B}-\vec{J}$ quantifiziert.

## Lehrziele

Wir listen im Folgenden die wichtigsten **Lehrziele** auf, die wir Ihnen mit dem Versuch **Ferromagnetische Hysterese** vermitteln möchten: 

- Sie können verschiedene Effekte des Ferromagnetismus selbst erleben. 
- Sie machen sich mit den Begriffen vertraut, mit denen man dieses Phänomen physikalisch beschreibt.
- Sie klären den Zusammenhang zwischen $\vec{B}$ und $\vec{H}$.
- Sie stellen Hysteresekurven $B(H)$ auf dem Oszilloskop dar und vertiefen dabei Ihre Kenntnisse im Umgang mit Oszilloskopen.
- Sie erhalten Einblick in die technische Vielfalt von Ferromagneten und Eigenschaften von Ferromagneten, die für den technischen Gebrauch von Bedeutung sind.

## Versuchsaufbau

Ein typischer Aufbau für den Versuch **Ferromagnetische Hysterese** ist in **Abbildung 1** gezeigt:

---

<img src="./figures/FerromagnetischeHysterese.jpg" width="1000" style="zoom:100%;" />

**Abbildung 1**: (Ein typischer Aufbau für den Versuch **Ferromagnetische Hysterese**)

---

Zum Aufbau der Schaltungen stehen Ihnen mehrere Eisenkerne und Spulen mit unterschliedlicher Windung, sowie Widerstände und Kondensatoren zur Verfügung. Die Wechselspannung für den Versuch wird mit einem entsprechenden Funktionsgenerator erzeugt. Zur Messung der effektiven Stromstärke $I_{\mathrm{eff}}$ steht Ihnen ein Handmultimeter zur Verfügung. Die Darstellung der Hysteresekurven erfolgt mit Hilfe des USB-Oszilloskops Pico (rechts im Bild) auf einem angeschlossenen Rechner. 

## Wichtige Hinweise

- **Achtung**: Sie gehen bei diesem Versuch mit **gefährlichen Spannungen** um. Beachten Sie die Hinweise zum [sicheren Umgang mit Elektrizität](https://labs.physik.kit.edu/163.php?tab=%5B311%5D#tabpanel-311) auf den Webseiten des P1/P2. 
- **Achtung**: Sie gehen bei diesem Versuch mit **Spulen mit hoher Induktivität** um. Regeln Sie vor allen eingriffen in die Schaltungen die **Spannnung langsam auf Null**. Plötzliche Änderung des Stroms, wie sie z.B. bei spontanten Ein- und Ausschaltvorgängen vorkommen können zu hohen Induktionsspannungen führen. 
- Die Massen der Oszilloskopeingänge sind geräteseitig verbunden. Verkabeln Sie keine Kurzschlüsse!
- Multimeter sind als Strommessgeräte besonders empfindlich. Vor dem Anschließen muss die Spannungsversorgung auf Null geregelt werden, da Sie das Multimeter sonst zerstören können. Die geräte sind mit Sicherungen versehen, die in diesem Fall ausgetauscht werden müssen.
- Bringen Sie nach Möglichkeit einen USB-Datenträger zur Übertragung der Daten vom Oszilloskop ins Jupyter-Protokoll mit. 

# Navigation

- [Ferromagnetische_Hysterese.iypnb](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/Ferromagnetische_Hysterese/Ferromagnetische_Hysterese.ipynb): Aufgabenstellung und Vorlage für Ihr Protokoll.
- [Ferromagnetische_Hysterese_Hinweise.ipynb](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/Ferromagnetische_Hysterese/Ferromagnetische_Hysterese_Hinweise.ipynb): Hinweise zu den Aufgaben.
- [Datenblatt.md](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/Ferromagnetische_Hysterese/Datenblatt.md): Technische Details zu den Versuchsaufbauten.
- [doc](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/tree/main/Ferromagnetische_Hysterese/doc): Dokumente zur Vorbereitung auf den Versuch.
- [figures](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/tree/main/Ferromagnetische_Hysterese/figures): Bilder, die für die Dokumentation des Versuchs verwendet wurden.
