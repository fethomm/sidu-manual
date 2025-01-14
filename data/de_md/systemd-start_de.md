% Systemadministration - systemd

ANFANG   INFOBEREICH FÜR DIE AUTOREN  
Dieser Bereich ist vor der Veröffentlichung zu entfernen !!!  
**Status: RC3**

Änderungen 2021-02 bis 03:

+ Entfernen des Kapitels "Installation und Einrichten von systemd"
+ Umorganisation in "systemd-start" mit Link auf alle weiteren, im Handbuch aufgeführten, Unit-Typen.
+ Korrektur und Aktualisierung aller Links
+ Für die Verwendung mit pandoc optimiert.
+ Review
+ Link zu systemd.automount auf systemd.mount gesetzt, da beides in systemd.mount behandelt wird.

ENDE   INFOBEREICH FÜR DIE AUTOREN

---

## systemd der System- und Dienste-Manager

*Anmerkung:*  
*Die folgende, allgemeine Einführung zu systemd wurde überwiegend der ins [deutsche übersetzten Manpage](https://manpages.debian.org/testing/manpages-de/systemd.1.de.html) entnommen. Der Dank geht an Helge Kreutzmann.*

---

**systemd** ist ein System- und Diensteverwalter, der beim Systemstart als erster Prozess (als PID 1) ausgeführt wird und somit als **Init-System** agiert, das System hochfährt und auf Anwendungsebene **Dienste verwaltet.**  
Entwickelt wird es federführend von den Red Hat Entwicklern Lennart Poettering und Kay Sievers.

In Debian wurde die Einführung des systemd als Standard-Init-System lange, kontrovers und emotional diskutiert bis im Februar 2014 der Technische Ausschuss für systemd stimmte.  

Seit der Veröffentlichung von 2013.2 "December" benutzt siduction bereits systemd als Standard-Init-System.

---

### Konzepte

Systemd stellt ein Abhängigkeitssystem zwischen verschiedenen Einheiten namens "*Units*" in 11 verschiedenen Typen (siehe unten) bereit. Units kapseln verschiedene Objekte, die für den Systemstart und -betrieb relevant sind.  
Units können "*aktiv*" oder "*inaktiv*", sowie im Prozess der "*Aktivierung*" oder "*Deaktivierung*", d.h. zwischen den zwei erstgenannten Zuständen sein. Ein besonderer Zustand "*fehlgeschlagen*" ist auch verfügbar, der sehr ähnlich zu "*inaktiv*" ist. Falls dieser Zustand erreicht wird, wird die Ursache für spätere Einsichtnahme protokolliert. Siehe die Handbuchseite [Sytemd-Journal](./systemd-journald_de.htm).  
Mit systemd können viele Prozesse parallel gesteuert werden, da die Unit-Dateien mögliche Abhängigkeiten deklarieren und systemd erforderliche Abhängigkeiten automatisch hinzugefügt.

### Units

Die folgenden Unit-Typen sind verfügbar und, sofern verlinkt, führt der Link zu einer ausführlicheren Beschreibung in unserem Handbuch:

1. **Dienste-Units** ([systemd.service](./systemd-service_de.htm)), die Daemons und die Prozesse, aus denen sie bestehen, starten und steuern. 

2. **Socket-Units** (systemd.socket), die lokale IPC- oder Netzwerk-Sockets in dem System kapseln, nützlich für Socket-basierte Aktivierung.

3. **Target-Units** ([systemd.target](./systemd-target_de.htm)) sind für die Gruppierung von Units nützlich. Sie stellen während des Systemstarts auch als Runlevel bekannte Synchronisationspunkte zur Verfügung.

4. **Geräte-Units** (systemd.device) legen Kernel-Geräte (alle Block- und Netzwerkgeräte) in systemd offen und können zur Implementierung Geräte-basierter Aktivierung verwandt werden.

5. **Mount-Units** ([systemd.mount](./systemd-mount_de.htm)) steuern Einhängepunkte im Dateisystem.

6. **Automount-Units** ([systemd.automount](./systemd-mount_de.htm)) stellen Selbsteinhänge-Fähigkeiten bereit, für bedarfsgesteuertes Einhängen von Dateisystemen sowie parallelisiertem Systemstart.

7. **Zeitgeber-Units** ([systemd.timer](./systemd-timer_de.htm)) sind für das Auslösen der Aktivierung von anderen Units basierend auf Zeitgebern nützlich.

8. **Auslagerungs-Units** (systemd.swap) sind ähnlich zu Einhänge-Units und kapseln Speicherauslagerungspartitionen oder -dateien des Betriebssystems.

9. **Pfad-Units** ([systemd.path](./systemd-path_de.htm)) können zur Aktivierung andere Dienste, wenn sich Dateisystemobjekte ändern oder verändert werden, verwandt werden.

10. **Slice-Units** (systemd.slice) können zur Gruppierung von Units, die Systemprozesse (wie Dienste- und Bereichs-Units) in einem hierarchischen Baum aus Ressourcenverwaltungsgründen verwalten, verwandt werden.

11. **Scope-Units** (systemd.scope) sind ähnlich zu Dienste-Units, verwalten aber fremde Prozesse, statt sie auch zu starten.

### systemd im Dateisystem

Die Unit-Dateien mit den Direktiven für systemd befinden sich im Verzeichnis **/lib/systemd/system/**. Das ist unabhängig vom Status der Unit in systemd.  
Die Steuerung des Status (enabled, disabled) einer Unit erfolgt über Symlink im Verzeichnis **/etc/systemd/system/**.  
Das Verzeichnis **/run/systemd/system/** beinhaltet zur Laufzeit erstellte Unit-Dateien.

### Weitere Funktionen von systemd

Systemd bietet noch weitere Funktionen. Eine davon ist [logind](https://www.freedesktop.org/software/systemd/man/systemd-logind.service.html)  als Ersatz für das nicht mehr weiter gepflegte  *ConsoleKit* . Damit steuert systemd Sitzungen und Energiemanagement. Nicht zuletzt bietet systemd eine Menge an weiteren Möglichkeiten wie beispielsweise das Aufspannen einen Containers (ähnlich einer Chroot) mittels [systemd-nspawn](http://0pointer.de/public/systemd-man/systemd-nspawn.html)  und viele weitere. Ein Blick in die Linkliste auf   [Freedesktop](https://www.freedesktop.org/wiki/Software/systemd/)  ermöglicht weitere Entdeckungen, unter anderem auch die ausführliche Dokumentation von Lennart Poettering zu systemd.

---

### Handhabung von Diensten mittels systemd

Einer der Jobs von systemd ist es Dienste zu starten, zu stoppen oder sonstwie zu steuern. Dazu dient der Befehl "*systemctl*".

+ systemctl --all - listet alle Units, aktive und inaktive.
+ systemctl --t [NAME] - listet nur Units des bezeichneten Typ.
+ systemctl list-units - listet alle aktiven Units.
+ systemctl start [NAME...] - startet (aktiviert) eine oder mehrere Units.
+ systemctl stop [NAME...] - (deaktiviert) eine oder mehrere Units.
+ systemctl restart [NAME] - stopt eine Unit und startet sie sofort wieder. Wird z.B. verwendet um die geänderte Konfiguration eines Dienstes neu einzulesen.
+ systemctl status [Name] - zeigt den derzeitigen Status einer Unit.
+ systemctl is-enabled [Name] - zeigt nur den Wert "enabled" oder "disabled" des Status einer Unit.

Die beiden folgenden Befehle integrieren bzw. entfernen die Unit anhand der Konfiguration ihrer Unit-Datei. Dabei werden Abhängigkeiten zu anderen Unit beachtet und ggf. Standardabhängikeiten hinzugefügt damit systemd die Dienste und Prozesse fehlerfrei ausführen kann.
 
+ systemctl enable [NAME] - gliedert eine Unit in systemd ein.
+ systemctl disable [NAME] - entfernt eine Unit aus systemd.

Oft ist es nötig, "systemctl start" und "systemctl enable" für eine Unit durchzuführen, um sie sowohl sofort als auch nach einem Reboot verfügbar zu machen. Beide Optionen vereint der Befehl:

+ systemctl enable --now [NAME]

Nachfolgend zwei Befehle deren Funktion unsere Handbuchseite [Systemd-Target](./systemd-target_de.htm) beschreibt.

+ systemctl reboot – Führt einen Reboot aus
+ systemctl poweroff - Fährt das System herunter und schaltet den Strom, sofern technisch möglich, aus.

#### Beispiel

Anhand von Bluetooth demonstrieren wir die Funktionalität des systemd.  
Zuerst die Statusabfrage im Kurzformat.

~~~
# systemctl is-enabled bluetooth.service
enabled
~~~

Nun Suchen wir nach den Unit-Dateien, dabei kombinieren wir *"systemctl*" mit "*grep*":

~~~
# systemctl list-unit-files | grep blue
bluetooth.service          enabled         enabled
dbus-org.bluez.service     alias           -
bluetooth.target           static          - 
~~~

Anschließend deaktivieren wir die Unit "*bluetooth.service*".

~~~
# systemctl disable bluetooth.service
  Synchronizing state of bluetooth.service with SysV service script with /lib/systemd/systemd-sysv-install.
  Executing: /lib/systemd/systemd-sysv-install disable bluetooth
  Removed /etc/systemd/system/dbus-org.bluez.service.
  Removed /etc/systemd/system/bluetooth.target.wants/bluetooth.service.
~~~
  
In der Ausgabe ist gut zu erkennen, dass die Link (nicht die Unit-Datei selbst) entfernt wurden. Damit startet der "*bluetooth.service*" beim Booten des PC/Laptop nicht mehr automatisch. Zur Kontrolle fragen wir den Status nach einem Reboot ab.

~~~
# systemctl is-enabled bluetooth.service  
disabled
~~~

Um eine Unit nur zeitweise zu deaktivieren, verwenden wir den Befehl

~~~
# systemctl stop <unit>
~~~

Damit bleibt die Konfiguration in systemd erhalten. Mit dem entsprechenden "start"-Befehl aktivieren wir die Unit wieder.

---

<div id="rev">Seite zuletzt aktualisert 2021-03-12</div>
