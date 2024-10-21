# Arbeiten auf dem Jupyter-Server

## Zugang zum Jupyter-Server

Mit dem Wintersemester 2024/2025 wurde das P1-Praktikum der Fakultät für Physik in eine landesweites Projekt zur Bereitstellung eine Jupyter-Service für alle Universitäten in Baden-Württemberg aufgenommen worden. Zugang zum Jupyter-Server des KIT erhalten Sie über die Webadresse: 

[https://jupyter-test.scc.kit.edu/](https://jupyter-test.scc.kit.edu/). 

Als Login verwenden Sie Ihren Studierenden-Account am KIT. Die Freischaltung erfolgt durch die Praktikumsleitung nach abgeschlossener Anmeldung zum Kurs. Wählen Sie, wenn Sie danach gefragt werden, die Option **Physik Praktikum** aus und starten Sie den Server. 

## Einrichten der Versuche

### Die Arbeitsumgebung auf dem Jupyter-Server

Nach dem Start sollten Sie ein zweigeteiltes Fenster in Ihrer Arbeitsumgebung auf dem Jupyter-Server vorfinden, wie im **Abbildung 1** gezeigt:

---

<img src="../figures/JupyterAccount.png" alt="figures" style="zoom:100%;" />

**Abbildung 1** (Arbeitsumgebung nach dem Start es Jupyter-Servers der Fakultät)

---

Auf der linken Seite befindet sich ein Navigationsfenster mit der Verzeichnisstruktur Ihrer Arbeitsumgebung, rechts daneben befindet sich ein Fenster (der sog. *Launcher*), in dem Sie auswählen können, welche Art von Notebook Sie öffnen möchten. Sie können, wenn Sie möchten, die Option **Notebook (Python 3)** (das erste Icon oben links im *Launcher* in **Abbildung 1**) anwählen, um ein Jupyter-notebook zu öffnen. Das rechte Fenster der Arbeitsumgebung kann mehrere Register enthalten.  

### Der gitlab-Server des SCC

Die jeweils aktuelle Version aller Versuchsanleitungen und die dazugehörigen Daten finden Sie auf dem [gitlab-Server des SCC](https://gitlab.kit.edu/) unter den Webadressen: 

* [https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students). 

* [https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students). 

**Abbildung 2** gibt Ihnen eine Vorstellung, wie die Webseite des SCC gitlab-Servers für das **Repository des P1-Praktikums** in etwa aussieht. Beachten Sie, dass dieses Bild nicht den aktuellen Zustand des Servers widerspiegeln muss.  

---

<img src="../figures/scc_gitlab.png" alt="figures" style="zoom:100%;" />

**Abbildung 2** (Das **students Repository des P1-Praktikums** auf dem SCC gitlab-Server)

---

##  Download aus dem SCC gitlab-Server 

Um z.B. das **students Repository des P1-Praktikums** vom [SCC gitlab-Server](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students) in Ihre Arbeitsumgebung auf dem Jupyter-Server zu laden gehen Sie wie folgt vor:

- Gehen Sie im Menü Ihrer Arbeitsumgebung auf dem Jupyter-Server auf das Verzeichnis **Git** und wählen Sie die Option **Clone a Repository** aus.
- In einem neuen Fenster werden Sie daraufhin aufgefordert die **URI-Adresse** für das Repository anzugeben, das Sie *clonen* möchten. Diese finden Sie im entsprechenden SCC gitlab-Repository (hier verlinkt fürs [P1](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students) oder [P2](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students)).
  - Öffnen Sie dazu das SCC Gitlab Repository z.B. in einem neuen Reiter Ihres Browsers und klicken Sie auf das blaue Feld mit der Aufschrift **Clone** (rechts in **Abbildung 2**). Wählen Sie aus dem sich öffnenden Untermenü die Option **Clone with HTTPS** aus. Die entsprechende Webadresse wird in die Zwischenablage Ihres Computers geladen.
  - Wechseln Sie in Ihrem Browser wieder in den Reiter mit Ihrer Arbeitsumgebung auf dem Jupyter-Server und geben Sie die Webadresse für das zu *clonende* SCC-gitlab Repository an. 
  - Das Repository wird nun in Ihre Arbeitsumgebung geladen. Dieser Vorgang kann einige Sekunden dauern. 


Nach erfolgreicher Durchführung sollten Sie eine Verzeichnis-Struktur **students** in Ihrer Arbeitsumgebung auf dem Jupyter-Server vorfinden. In diesem Verzeichnis befinden sich die **Anleitungen zu allen Versuchen des P1-Praktikums**. Sie können in diesem Ordner die Durchführung und Auswertung des jeweiligen Versuchs beginnen.

Vor jedem weiteren Versuch bietet es sich an, nochmal eventuelle Änderungen in den noch ausstehenden Versuchsbeschreibungen vom *Main*-Repository auf dem gitlab-Server des SCC zu laden. Wählen Sie dazu wieder den Menüpunkt **Git** und das Untermenü **Pull from Remote** aus. Die Aktualisierung sollte nun ausgeführt werden.

## Arbeiten mit dem Jupyter-notebook

Das Jupyter-notebook wird in Zellen bearbeitet. Es kann sich dabei um **Textzellen** (Markdown) oder **Code-Zellen** (python) handeln, in die Sie direkt Code in der Prorammiersprache Python eingeben können. Eine kurze Einführung in die Verwendung des Jupyter-notebooks können Sie im SCC-gitlab Repository **jupyter-tutorials** [hier](https://gitlab.kit.edu/kit/etp-lehre/jupyter-tutorials/-/tree/main) finden. Dieses Repository beinhaltet die folgenden *hands-on* Einführungen:

- Verwendung des [Jupyter-notbooks](https://jupyter.org/).
- Programmiersprache [Python](https://www.python.org/).
- Python-Bibliothek [matplotlib](https://matplotlib.org/).
- Python-Bibliothek [pandas](https://pandas.pydata.org/).
- Python-Paket [kafe2](https://etpwww.etp.kit.edu/~quast/kafe2/htmldoc/) zur statistischen Datenanalyse.
- Grundlagen der Statistik.
- Fehlerrechnung im Praktikum.

Wir empfehlen Ihnen sich dieses Repository zusätzlich zum **students** Repository des P1-Praktikums in Ihre Arbeitsumgebung auf den Jupyter-Server zu laden und, soweit es Ihr Arbeitspensum zulässt einige Tutorials durchzuarbeiten. 

Ein Jupyter-cheat sheet finden Sie z.B. [hier](https://www.edureka.co/blog/wp-content/uploads/2018/10/Jupyter_Notebook_CheatSheet_Edureka.pdf). Für die Durchführung der Versuche des P1- (oder P2-)Praktikums können die folgenden Jupyter-notebook *features* von Nutzen für Sie sein: 

- *Esc+m*: Wechsele Zellenmodus zu Markdown

- *Esc-y*: Wechsele Zellenmodus zu Code (Python)

- Befindet sich eine Zelle im Code-Modus können Sie direkt Kommandos in Python eingeben. Das folgende Beispiel importiert die Variable $l$ aus der Datei [*parameters_Exercise_2.py*](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/Datenverarbeitung/params/parameters_Exercise_2.py) aus dem *params*-Verzeichnis Ihrer Jupyter-Umgebung für den **Vorversuch Datenverarbeitung** des P1-Praktikums und gibt den Wert der Variablen auf dem Bildschirm aus, sobald Sie die Zelle ausführen. 

  ```python
  from params.parameters_Exercise_2 import l
  print(l)
  ```

- *Strg+Enter*: Ausführen einer (Code-)Zelle.

- *Strg+s*: Speichern. Wir empfehlen Bearbeitungen im Jupyter-notebook regelmäßig abzuspeichern, um Datenverlust vorzubeugen.

- Sie sollten außerdem wissen, dass Sie jede in der Verzeichnisstruktur Ihrer Arbeitsumgebung auf dem Jupyter-Server befindliche Datei **per Doppelklick** im rechten Fenster der Umgebung öffnen, bearbeiten und nach der Bearbeitung abspeichern können. 

- Möchten Sie ein Python-Skript aus Ihrer Arbeitsumgebung auf dem Jupyter-Server direkt aus dem Jupyter-notebook ausführen, tun Sie dies in einer Code-Zelle mit Hilfe des [Magic command](https://ipython.readthedocs.io/en/stable/interactive/magics.html) **%run**. Im Folgenden ist z.B. gezeigt, wie man das Skript *run_phyFit.py* aus Ihrer Jupyter-Umgebung direkt aus einer Code-Zelle eines Jupyter-notebooks (hier mit der Option `–-help`) aufrufen kann: 

  ```python
  %run /opt/conda/bin/run_phyFit.py --help
  ```

  Ein Beispiel für Die Ausführung diese *Magic command* können Sie in **Abbildung 3** sehen:

  ---

  <img src="../figures/Magic_command.png" alt="figures" style="zoom:100%;" />

  **Abbildung 3** (Ausführung eines *Magic command* im Jupyter-notebook)

  ---

- Es empfiehlt sich alle angegebenen Skripte zunächst, wie oben demonstriert mit der Option `--help` aufzurufen (beachten Sie die zwei Minuszeichen). Zum einen erfahren Sie, ob sich das entsprechende Skript grundsätzlich fehlerfrei aufrufen lässt. Zum anderen erfahren Sie, wie und mit welchen weiteren Konfigurationsparametern Sie das jeweilige Skript aufrufen können. Zum Beispiel können Sie mit den folgenden weiteren Parametern das Bild der konfigurierten Anpassung direkt im Arbeitsverzeichnis Ihrer Arbeitsumgebung auf dem Jupyter-Server in *png*-Format abspeichern:

  ```python
  %run /opt/conda/bin/run_phyFit.py -s -f png yaml/data.yaml
  ```

  Dabei steht die Option *-s* (beachten Sie das einfache Minuszeichen) für "save", also Abspeichern und die Option *-f png* für das Datenformat *png*. Alle Bilder, die Sie in einer Code-Zelle des Jupyter-notebooks erzeugen werden allerdings auch direkt ins Jupyter-notebook eingebunden.   

## Export von Jupyter-notebook nach *pdf*

Nach Bearbeitung sollten Sie Ihr Jupyter-notebook ins *pdf*-Format exportieren und auf ILIAS hochladen. Wir empfehlen den direkten Export nach *pdf* auf dem Jupyter-Server. Falls sich dies als problematisch erweisen sollte versuchen Sie den Export über *html*. **Stellen Sie vor dem Export ins *pdf*-Format sicher, dass alle Zellen ausgeführt wurden**, so dass alle erzielten (Teil-)Ergebnisse im *pdf*-Export sichtbar sind. Falls Sie sowohl mit dem direkten *pdf*-Export, als auch mit dem Export über *html* Probleme haben sollten können Sie in Ausnahmefällen Ihr Jupyter-notebook selbst auf das ILIAS-System hochladen. 

### Direkter Export nach *pdf*

Um Ihr Jupyter-notebook ins *pdf*-Format zu exportieren gehen Sie wie folgt vor: 

- Gehen Sie über den Menüpunkt **File** des Hauptmenüs des Jupyter-Servers und wählen Sie den Menüpunkt **Save and Export Notebook As…** und dann den Unterpunkt **PDF** aus. Nach dem Export sollte sich eine *pdf*-Datei in Ihrem Browser öffnen, die Sie lokal abspeichern und auf ILIAS hochladen können. 
- Beachten Sie, dass Abbildungen, die über Hyperlinks in die Anleitung eingebunden wurden nicht in der erzeugten *pdf*-Datei angezeigt werden. Falls Sie im Verlauf Ihrer Durchführung Bilder *direkt* aus einer Code-Zelle ins Jupyter-notebook eingebunden haben sollten werden diese zusammen mit dem Jupyter-notebook exportiert und angezeigt (siehe auch unter dem Abschnitt **Einbettung externer Bilder ins Jupyter-notebook**).
- Das dem *pdf*-Export zugrundeliegende Latex-*engine* reagiert sehr sensibel auf Latex-Syntax Fehler. Um einen möglichst reibungslosen Export des Jupyter-notebook ins *pdf*-Format gewährleisten zu können empfehlen wir Ihnen den Export regelmäßig, insbesondere nach der Verwendung von Latex-Formeln zu testen und nicht mit dem Export zu warten, bis das ganze Dokument fertiggestellt ist.  

### Export über *html* nach *pdf*

Falls beim direkten Export Ihres Jupyter-notebooks nach *pdf* dennoch Probleme auftreten sollten, sollte es immer noch möglich sein das Jupyter-notebook über *html* und schließlich Ihren Webbrowser nach *pdf* zu exportieren. Hierfür empfehlen wir das folgende Vorgehen: 

- Erzeugen Sie ein Verzeichnis mit dem Namen des Versuchs auf Ihrem lokalen Rechner.
- Exportieren Sie das Jupyter-notebook nach *html* und laden Sie es in das zuvor erstellte Verzeichnis herunter. Gehen Sie hierzu über den Menüpunkt **File** des Hauptmenüs des Jupyter-Servers und wählen Sie den Menüpunkt **Save and Export Notebook As…** und dann den Unterpunkt **HTML** aus. 
- Laden Sie sich die Bilder, die im Jupyter-notebook verlinkt wurden, zusätzlich vom Jupyter-Server in das gleiche Verzeichnis herunter. Die einzubindenden Bilddateien sollten sich in der gleichen Verzeichnisstruktur, wie auf dem Jupyter-Server befinden. Gegebenenfalls benötigen Sie ein entsprechendes Unterverzeichnis *figures*. Beachten Sie eventuelle Änderungen in den Dateiendungen (z.B. von *jpg* nach *jpeg*), die beim Herunterladen automatisch durch Ihren Browser vorgenommen worden sein könnten. 
- Sie können die *html*-Datei dann lokal, in Ihrem Browser, öffnen und von dort aus nach *pdf* exportieren. Wenn die so erzeugte *pdf*-Datei die Seiten nicht einwandfrei umbricht, ist das für uns ***kein Problem***.   

## Einbettung externer Bilder ins Jupyter-notebook

Beim direkten Export von Jupyter-notebook ins *pdf*-Format, wie oben beschrieben ist es nicht möglich externe Grafiken, die per Link mit dem Jupyter-notebook verknüpft sind ins *pdf*-Format zu exportieren. 

Sie können externe Grafiken aber über *matplotlib* direkt ins Jupyter-notebook einbetten. **Auf diese Weise funktioniert der Export für die Bildformate *png* und *jpg* ins *pdf*-Format, ohne Probleme**. 

Ein Beispiel, wie Sie externe Graphiken in ein Jupyter-notebook einbetten können finden Sie in der Datei [add_figures.ipynb](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/tools/add_figures.ipynb). 

# Navigation

[Zurück zum P1](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students) | [Zurück zum P2](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students) | [Zurück die den Webseiten des P1/P2-Praktikums](https://labs.physik.kit.edu/prakt-klass-physik.php)

