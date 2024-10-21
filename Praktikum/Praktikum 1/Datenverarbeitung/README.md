<img src="../figures/Logo_KIT.svg"  width=200px style="float:right;" />

# Fakultät für Physik 

## Physikalisches Praktikum P1 für Studierende der Physik



Praktikumsvorversuch (Stand: **Oktober 2024**)





# Datenverarbeitung



## Motivation

Im Mittelpunkt jedes physikalischen Experiments steht die **[Messung](https://de.wikipedia.org/wiki/Messung), d.h. die nachvollziehbare Erfassung und Weiterverarbeitung primärer [Daten](https://de.wikipedia.org/wiki/Daten), unter Laborbedingungen**. 

Mit diesem Praktikumsvorversuch, den alle Praktikumsteilnehmer:innen, am ersten Tag des P1, gemeinsam mit Ihren Tutor:innen durchführen, werden wir Sie anhand eines einfachen physikalischen Vorgangs mit den wichtigsten Methoden der computergestützten Datenverarbeitung in der modernen Physik vertraut machen. Im Laufe des P1 werden Sie erfahren, dass die physikalische Messung untrennbar mit den Methoden der [Parameterschätzung in der Statistik](https://de.wikipedia.org/wiki/Sch%C3%A4tzfunktion) verbunden ist. Wir gehen davon aus, dass diejenigen unter Ihnen, die Physik im Hauptfach studieren den einführenden Kurs *Computergestützte Datenauswertung* (GgDa) am KIT besucht haben. Das Praktikum der klassischen Physik bietet Ihnen eine Plattform, die Methoden, die Sie dort kennengelernt haben wiederholt für echte, physikalische Messungen einzusetzen. Weiterführende Kurse, um die Methoden der Datenanalyse, wie Sie sie in der Physik benötigen, von Grund auf zu erlernen, werden im weiteren Verlauf des Physikstudiums am KIT angeboten. Für diejenigen unter Ihnen, die Physik im Nebenfach studieren, sollen dieser und die folgenden Versuche des P1 einen unverstellten Einblick in den Messalltag eines Physikers geben. Sie erhalten zur Bewältigung gesonderte Unterstützung  durch unsere Tutor:innen und Dozenten.

Als Aufgabe wählen wir die Bestimmung der [Erdbeschleunigung](https://de.wikipedia.org/wiki/Schwerefeld) $g$ mit Hilfe eines Pendels, wie Sie sie im P1-Versuch [Pendel](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/tree/main/Pendel) selbst durchführen werden. Wir haben mit Hilfe der kostenfreien Anwendung [phyphox](https://phyphox.org/de/home-de/) der RWTH Aachen einen reellen Datensatz vorbereitet den Sie, im Rahmen dieses Vorversuchs, weiterverarbeiten werden. Zur Aufzeichnung der Daten bestanden bis auf den Besitz eines Smartphones kaum apparative Voraussetzungen. Sie könnten das hier vorgestellte Experiment also auch bei sich zu Hause wiederholen und Ihre Ergebnisse mit denen aus diesem und dem P1-Versuch Pendel vergleichen.

## Lehrziele

Wir listen im Folgenden die wichtigsten **Lehrziele** auf, die wir Ihnen mit dem Versuch **Datenverarbeitung** vermitteln möchten: 

- Sie machen sich bewusst, dass in der modernen Physik jeder Messung ein **Modell** zugrunde liegt. 
- Sie üben sich in der Anwendung statistischer Methoden zur exakten numerischen **Bestimmung von Modellparametern** und machen sich mit Softwarepaketen vertraut mit denen dies möglich ist.
- Sie vergegenwärtigen sich den Unterschied zwischen **statistischen und systematischen Unsicherheiten**.

## Versuchsaufbau

Wir haben die Anwendung [phyphox](https://phyphox.org/de/home-de/) auf ein Smartphone geladen und das Smartphone mit Klebestreifen auf eines der [Reversionspendel](https://de.wikipedia.org/wiki/Reversionspendel) aus dem P1-Versuch [Pendel](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/tree/main/Pendel) montiert. Für die Messung haben wir die Anwendung **Beschleunigung (ohne $g$)** verwendet. Der Versuchsaufbau ist im folgenden Bild skizziert:

---

<img src="./figures/PendelVorversuch.png" style="zoom:100%;" />

**Abbildung 1**: (Der Aufbau, mit dem wir die Daten für diesen Versuch aufgenommen haben)

---

Wir haben das Pendel in Schwingung versetzt, die resultierende Bewegung mit Hilfe der im Smartphone eingebauten Beschleunigungssensoren ausgelesen und uns die aufgezeichneten Datensätze im [*csv*-Format](https://de.wikipedia.org/wiki/CSV_(Dateiformat)) per E-Mail zugeschickt. Außerdem haben wir alle für unsere Messung relevanten **äußeren Parameter** mit Unsicherheiten festgehalten. Weitere wichtige Informationen zu Pendel und Smartphone haben wir aus der Anleitung des P1-Versuchs [Pendel](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/tree/main/Pendel) und den im Internet verfügbaren Datenblättern des Smartphones bezogen. Zum Teil haben wir die Abmessungen des Smartphones noch einmal mit einfachen Mitteln nachgemessen. Dort, wo uns keine Informationen zu Unsicherheiten vorlagen haben wir sie abgeschätzt. Die Datensätze, die wir aufgenommen haben finden Sie nach dem *Download* des Versuchs in Ihrer Arbeitsumgebung auf dem Jupyter-Server. 

## Wichtige Hinweise zum Versuch

- Beim [*csv*](https://de.wikipedia.org/wiki/CSV_(Dateiformat)) (*comma separated value*)-Format handelt es sich um ein einfaches, sowohl von Menschen als auch Maschinen lesbares Dateiformat, um Daten in Spalten und Zeilen organisiert abzulegen.
- Bevor Sie sich an die Auswertung der Daten und die Extraktion physikalischer Parameter machen können gehört es zum Messalltag, die Daten zunächst aufzubereiten und geeignet zu präparieren. Dazu gehören die Anpassung des Datenformats, die Überprüfung auf unerkannte Störeffekte, Nullstellenkorrekturen und vieles mehr.  

# Navigation

- [Datenverarbeitung.iypnb](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/Datenverarbeitung/Datenverarbeitung.ipynb): Aufgabenstellung und Vorlage für Ihr Protokoll.
- [Datenverarbeitung_Hinweise.ipynb](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/Datenverarbeitung/Datenverarbeitung_Hinweise.ipynb): Hinweise zu den Aufgaben.
- [Datenblatt.md](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/Datenverarbeitung/Datenblatt.md): Technische Details zu den Versuchsaufbauten.
- [doc](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/tree/main/Datenverarbeitung/doc): Dokumente zur Vorbereitung auf den Versuch.
- [figures](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/tree/main/Datenverarbeitung/figures): Bilder, die für die Dokumentation des Versuche verwendet wurden.
