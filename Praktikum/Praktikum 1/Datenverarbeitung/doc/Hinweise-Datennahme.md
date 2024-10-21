# Hinweise für den Versuch Datenverarbeitung

## Primär- und Sekundärdaten

Die original Daten, wie sie aus dem Smartphone ausgelesen wurden finden Sie in der Datei 

```shell
raw.csv.
```

- In der Datenanalyse bezeichnet man diese Daten als **Primärdaten**. Diese sind der originäre Ursprung jeder Messung und sollten immer unverändert bewahrt werden.
- Alle weiteren Datensätze werden hieraus algorithmisch abgeleitet und sollten, mit **Methoden und Werkzeugen, die Sie in Ihrem Protokoll dokumentieren** jederzeit aus den Primärdaten neu gewonnen werden können. 
- Alle abgeleiteten Datensätze bezeichnet man als **Sekundärdaten**. 
- Die Bewahrung der Primärdaten und die vollständige Dokumentation der Methoden und Werkzeuge zu deren Weiterverarbeitung, bis hin zum Messergebnis, bezeichnet man als *data preservation*. 
- Beides offenzulegen bezeichnet man als *open data*. Es handelt sich in beiden Fällen um Grundelemente jeder modernen, wissenschaftlichen Arbeit.

## Ablauf der Datennahme

- Die Anwendung *phyphox* hat die Beschleunigungssensoren des Smartphones mit einer festen **[Abtastrate](https://de.wikipedia.org/wiki/Abtastung_(Signalverarbeitung)) (engl. *sampling rate*)** von $100\ \mathrm{Hz}$ ausgelesen. 
- Um die Eigenschaften der Schwingung für uns ausreichend gut erfassen zu können haben wir **5 min lang gemessen**.
- Die Periode der Schwingung haben wir bereits während des Versuchs mit 1-2 s abgeschätzt, wir rechnen also mit 100-200 Datenpunkten pro Periode. Zur Erfassung einer erwartet einfachen Sinusschwingung ist eine solche Abtastrate sehr hoch. Es bietet sich daher an, in einem ersten Schritt zur Aufbereitung der Daten die Abtastrate um einen geeigneten Faktor auf ein handhabbares Maß zu reduzieren. Man bezeichnet diesen Vorgang als ***down sampling***. Die einfachste Art des *down sampling* besteht darin nur jeden n-ten Wert zu berücksichtigen. Alternativ könnte man jeweils den Mittelwert aus n Messungen bilden.
- Zusätzlich empfiehlt es sich, sich auf den Teil der Datennahme zu konzentrieren, **in dem diese stabil verlaufen ist**: 

  - In den ersten Sekunden unterlag die Messung Störungen des Anstoßes, die mit zunehmender Zeit abgeklungen sind. 
  - In den letzten Sekunden war die Schwingung durch Unregelmäßigkeiten in der Keillage des schwingenden Pendels gestört.  

## *PhyPraKit*-Nutzer 

- Beachten Sie, dass die Skripte **plotData.py** und **run_phyFit.py** die Eingangs- und Konfigurationsdaten nicht im *csv*-Format sondern in der Struktursprache **[yaml](https://de.wikipedia.org/wiki/YAML)**  erwarten. Die Notwendigkeit Daten von einem in ein anderes Format zu konvertieren ist ein häufiges Problem in der Datenverarbeitung. Sie können zur Umformatierung das Skript **cvs2yaml.py** verwenden.

# Navigation

[Main](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/tree/main/Datenverarbeitung)

