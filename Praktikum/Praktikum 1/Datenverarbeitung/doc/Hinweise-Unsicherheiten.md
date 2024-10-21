# Hinweise für den Versuch Datenverarbeitung

## Modelle mit externen Parametern 

Für **Aufgabe 2.3** bestimmen wir $g$ direkt als Parameter des Modells

 ```python
  # Length of the pendulum
  from params.parameters_Exercise_2 import l, l_UPPER, l_LOWER
  # Model to obtain g from the data directly
  def g_harmonic(x, x0=0.75, g=9.8, phi0=0):
      return x0*np.cos(np.sqrt(g/l)*x+phi0) 
 ```

Bei $\ell$ handelt es sich um die Länge des Pendels (siehe [Datenblatt](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/Datenverarbeitung/Datenblatt.md) zum Versuch), die wir, mit entsprechenden Unsicherheiten, an anderer Stelle bestimmt haben und als **äußeren (externen) Parameter** ins Modell einbringen. 

Sinnvollerweise wählen wir für die Berechnung von $g$ den Zentralwert für $\ell$ aus den Angaben. Bei richtiger Abschätzung von $\Delta\ell$ können wir jedoch nur die folgenden Aussagen treffen: 

- Wir erwarten, dass der wahre Wert der Länge des Pendels mit $\ell$ zusammenfällt. 
- Mit einer Wahrscheinlichkeit von 68% liegt der wahre Wert der Länge des Pendels im Intervall $[\ell-\Delta\ell;\ell+\Delta\ell]$.

## Statistische Unsicherheiten

Aus der Anpassung des Modells an die Daten erhalten wir einen Wert
$$
\begin{equation*}
g\pm\Delta g_{\mathrm{stat.}}.
\end{equation*}
$$
$\Delta g_{\mathrm{stat.}}$ rührt nur aus den $\{\Delta\hat{r}_{i}\}$ her. Bei den $\{\hat{r}_{i}\}$ handelt es sich um Ausprägungen der Zufallsgrößen $\{r_{i}\}$ für die eine konkrete Messung, die zur Bestimmung der $\{\hat{r}_{i}\}$ durchgeführt wurde. Würde man die gleiche Messung beliebig oft wiederholen gehen wir davon aus, dass die $\{r_{i}\}$ zufällig innerhalb der $\{\Delta\hat{r}_{i}\}$ streuen würden. Wir bezeichnen $\Delta g_{\mathrm{stat.}}$ daher als **statistische Unsicherheit**. In der Statistik kennt man auch den Begriff **aleatorische Unsicherheit** (von lat. *aliae*=Würfel). **Diese ist mit den Datenpunkten der konkreten Messung direkt verknüpft.**   

## Systematische Unsicherheit

Für die Bestimmung von $\Delta g$ müssen wir aber auch $\Delta\ell$ berücksichtigen. Da $\ell$, als externer Parameter, nicht immanent, d.h. nicht aus der Anpassung selbst, bestimmt werden kann, müssen wir $\Delta\ell$ ebenfalls von außen in die Bestimmung von $\Delta g$ einbringen.  Am einfachsten erreichen wir dies, indem wir $\ell$ um $\pm\Delta\ell$ variieren und die Anpassung erneut (insgesamt also $3\times$) durchführen. Die Unsicherheit $\Delta\ell$ wird entsprechend auf $g$ propagiert und führt so zu einer Unsicherheit $\Delta g_{\ell}$ unter Variation von $\ell$ um den Betrag $\pm\Delta\ell$. Dieses Verfahren ist genauer als lineare Fehlerfortpflanzung, weil es die höheren Ordnungen in der Taylorreihe nicht vernachlässigt. Es ist ein **Standardverfahren zur Abschätzung von Konfidenzintervallen**.

Die Unsicherheit $\Delta g_{\ell}$, die sich aus der ungenügenden Kenntnis von $\ell$ ergibt bezeichnet man in diesem Zusammenhang als **epistemische, oder systematische Unsicherheit** $\Delta g_{\mathrm{syst.}}$. In der Physik sind systematische Unsicherheiten i.d.R. mit *systematischen Variationen*, wie im vorherigen Absatz beschrieben verbunden.

## Gesamtunsicherheit und Korrelationen

Im allgemeinen kann man davon ausgehen, das $\Delta g_{\mathrm{stat.}}$ und $\Delta g_{\mathrm{syst.}}$ unkorreliert sind. Die Gesamtunsicherheit ergibt sich also zu
$$
\begin{equation*}
\Delta g = \Delta g_{\mathrm{stat.}}\oplus \Delta g_{\mathrm{syst.}} \equiv \sqrt{\Delta g_{\mathrm{stat.}}^{2} + \Delta g_{\mathrm{syst.}}^{2}}
\end{equation*}
$$
**Dies ist bei der Kombination systematischer Unsicherheiten verschiedener Quellen nicht immer der Fall!** 

In **Aufgabe 3.1** sind Sie z.B. mit systematischen Unsicherheiten aus drei Quellen $g_{\Theta}$, $g_{M}$ und $g_{s}$ konfrontiert. Wir haben zur Berechnung von $\Theta$ (nach dem [Satz von Steiner](https://de.wikipedia.org/wiki/Steinerscher_Satz)) für das Smartphone eine homogene Massenverteilung angenommen. Bedenken Sie hierzu die folgenden Punkte:

- Wie könnte man testen, wie sehr diese Annahme von der Realität abweicht? 
- Eine falsche Annahme für die Massenverteilung des Smartphones wirkt sich **gleichzeitig** sowohl auf $\Theta$, als auch auf $s$ aus. Die Annahme, das $\Theta$ und $s$ unabhängig sind ist, ist bei einer solchen Vorgehensweise also nicht gerechtfertigt. Wie würden Sie dies in Ihrem Modell für die Kombination der Unsicherheiten berücksichtigen?

## Welches ist die bessere Messung?

Grundsätzlich ist die bessere Messung nicht diejenige, die näher an der Erwartung liegt, sondern **diejenige, mit der geringeren Unsicherheit.** 

mit den **Aufgaben 2.3 und 3.1** liegt der interessante Fall vor, dass Sie in beiden Fällen die gleichen Daten verwenden. Die Qualität der Messung hängt also allein vom zugrunde liegenden Modell ab. Nun ist es so, dass im Modell für **Aufgabe 3.1** im Vergleich zu **Aufgabe 2.3** deutlich mehr äußere Parameter auftreten, die z.T. mit nicht geringen Unsicherheiten behaftet sind (siehe [Datenblatt](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/Datenverarbeitung/Datenblatt.md) zum Versuch). Es kann also durchaus passieren, dass die unzureichende Kenntnis von $\Theta$, $M$ und $s$ den Wert von $\Delta g$ und somit die Sensitivität der Messung auf die Messgröße $g$ **quantitativ *verschlechtert***. Ist das Modell für **Aufgabe 3.1** also besser oder schlechter als das Modell für **Aufgabe 2.3**?  

# Navigation

[Main](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/tree/main/Datenverarbeitung)

