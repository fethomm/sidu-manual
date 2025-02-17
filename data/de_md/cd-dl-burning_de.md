% siduction ISO download und brennen

ANFANG   INFOBEREICH FÜR DIE AUTOREN  
Dieser Bereich ist vor der Veröffentlichung zu entfernen !!!  
**Status: RC2**

Änderungen 2020-05:

+ Inhalt aktualisiert
+ Korrektur und Prüfung aller Links
+ Inhalt überarbeitet

Änderungen 2020-12:

+ Für die Verwendung mit pandoc optimiert.
+ Inhalt geringfügig überarbeitet.

Änderung 26.02.2021

+ mirror Süpdamerika (entfernt) scheint nicht mehr zu funktionieren, bzw nicht mehr zu existieren!

ENDE   INFOBEREICH FÜR DIE AUTOREN

## Die siduction ISO herunterladen

**Bitte verwende den nächstgelegenen Spiegelserver. Spiegelserver, die unterhalb des Links mit Angaben für den Eintrag in /etc/apt/sources.list.d/siduction.list gelistet sind, werden zeitnah aktualisiert.**  

### Europa

+ **Freie Universität Berlin/ spline (Student Project LInux NEtwork), Deutschland**  
    http://ftp.spline.de/mirrors/siduction/iso/  
    ftp://ftp.spline.de/pub/siduction/iso/

+ **Universität Stuttgart**  
    http://ftp.uni-stuttgart.de/siduction/iso/  
    ftp://ftp.uni-stuttgart.de/siduction/iso/  

+ **Office Vienna**  
    https://siduction.office-vienna.at/iso/

### Nordamerika

+ **University of Delaware**  
    http://mirror.lug.udel.edu/pub/siduction/iso  
    ftp://ftp.lug.udel.edu/pub/siduction/iso  
    rsync://rsync.lug.udel.edu/siduction/iso  

+ **Georgia Tech**  
    http://www.gtlib.gatech.edu/pub/siduction/iso  
    ftp://ftp.gtlib.gatech.edu/pub/siduction/iso  
    rsync://rsync.gtlib.gatech.edu/siduction/iso 

-----

## Dateidefinitionen auf den siduction-Spiegelservern

Jeder Spiegelserver umfasst folgende Dateien:

siduction-20xx-xx-release-name-window-manager-arch-datetimestamp.arch.manifest  
siduction-20xx-xx-release-name-window-manager-arch-datetimestamp.iso  
MD5SUM  
MD5SUM.gpg  
SHA256SUM  
SHA256SUM.gpg  
SOURCES  


Die **.manifest**-Datei listet alle Pakete der jeweiligen ISO.

**.iso** ist die für den Download angebotene Abbilddatei.

Die Dateien **.md5** und **.sha256** dienen der Überprüfung der Integrität der ISO.

Die **.gpg**-Dateien sind die Signaturdateien, mit denen Checksummen-Dateien (.md5 .sha256) auf Änderungen überprüft werden. Letztere werden zur Integritätsüberprüfung der ISO verwendet.

Download-Links und Spiegelserver findet man auf [siduction.org](https://forum.siduction.org/index.php?page=7)

Das Tar-Archiv mit den Quellen ist für den interessant, der siduction weitervertreiben will. Hier müssen die Sourcen mit weitergegeben werden, um der Lizenz zu genügen. Weitere Informationen gibt es in dem Tar-Archiv.

Wenn jemand einen FTP-Server mit entsprechendem Traffic zur Verfügung stellen kann, sind wir jederzeit in den [siduction-Foren](https://siduction.org) oder im IRC irc.oftc.net:6667 #siduction-de erreichbar. 

### md5sum und Integritätsprüfung von heruntergeladenen Dateien

Eine md5sum ist die Prüfsumme einer Datei. Diese Prüfsumme wird zur Integritätsprüfung der zugehörigen Datei benutzt. Dabei wird die momentane md5sum der Datei mit einer bekannten früheren Summe verglichen. So kann festgestellt werden, ob die Datei verändert oder beschädigt wurde, was bei heruntergeladenen Dateien aus dem Netz immer ratsam ist und viel Zeit für die Fehlersuche erspart.

Die Datei ist unbeschädigt heruntergeladen worden, wenn die md5sum der heruntergeladenen Datei mit der Summe in der MD5-Datei übereinstimmt. Unter Linux erhält man die md5sum einer Datei mit:

    $ md5sum zu_prüfende_datei

Das dauert ein wenig und die Summe wird dann in der Konsole ausgegeben und kann dann mit der Summe wie sie in der entsprechenden *.md5 Datei hinterlegt ist manuell verglichen werden. Die md5 Datei kann dazu in einem Texteditor geöffnet werden. Mit dem md5summer (486 KB) kann die md5sum auch in Windows geprüft werden.

Einfacher ist die Überprüfung unter Linux mit folgendem Befehl, ausgeführt in dem Verzeichnis, in welchen sich sowohl die ISO-Datei als auch die ISO.MD5-Datei befinden:

    $ md5sum -c zu_prüfende_datei.md5

Je nachdem ob die Prüfsummen übereinstimmen, erhält man vom Programm eine Meldung:

    md5-Summe: zu_überprüfende_datei: ok

oder

    siduction-Name.iso: Fehlschlag md5sum: Warnung: 1 von 1 berechneten Prüfsumme stimmen nicht überein.

Die ISO-Abbilddateien von siduction werden immer mit der entsprechenden md5sum zum Download angeboten und sollten stets vor dem Brennen geprüft werden.

Diese Dateien werden vom Spiegelserver heruntergeladen:

siductionname.iso
siductionname.iso.md5

Die Überprüfung mittels SHA256SUM ist ein ähnliches Verfahren. Näheres unter

    $ man sha256sum

---

## Eine Live-DVD mit Windows brennen

<warning>**WICHTIGE INFORMATION:**</warning>
<warning>
siduction, als Linux-LIVE-DVD/CD, ist sehr stark komprimiert. Aus diesem Grund muss besonders auf die Brennmethode des Abbilds geachtet werden. Bitte verwendet hochwertige Medien, das Brennen im DAO-Modus (disk-at-once) und nicht schneller als achtfach (8x). Wir empfehlen allerdings, sofern die Hardware das Booten von USB unterstützt, das Abbild auf einen USB-Stick oder eine SD-Speicherkarte zu legen. Dazu empfiehlt sich das Tool Edger oder das Kommandozeilenwerkzeug dd. Anleitung dazu bietet das Handbuch unter Installationsoptionen.
</warning>

Selbstverständlich kann die DVD auch in Windows gebrannt werden. Die heruntergeladene Datei muss als ISO-Abbilddatei gebrannt werden. Falls Winrar (oder ein anderes Archivierungsprogramm) mit einer ISO-Datei verknüpft ist, könnte dieses Programm die ISO-Datei als eine Archivdatei ansehen. Aus der ISO-Datei muss eine DVD gebrannt werden.

Es gibt verschiedene gute Optionen, ISO-Dateien in Windows zu brennen.  

### Open-Source-Brennsoftware für Windows

+ cdrtfe: kompatibel mit Windows 9x/ME/2000/XP, Vista, 7 und 8. (getestet mit Win95, Win98SE, Win2000, WinXP). Nur für Win9x/ME: funktionierende ASPI-Layer (z. B. Adaptec ASPI 4.60)
+ LinuxLive USB Creator, ein Open-Source-Projekt, bietet eine GUI-Applikation für MS Windows™, welche es ermöglicht, eine siduction-i386.iso (32 bit) auf einen USB-Stick zu installieren.  

### Closed-Source- und proprietäre Brennsoftware für Windows

+ CD/DVD Burner XP pro
+ Burncdcc von [terabyteunlimited](https://www.terabyteunlimited.com/downloads-free-software.htm) kann nur ISO-Abbilddateien brennen.

---

## Die DVD mit Linux brennen

<warning>**WICHTIGE INFORMATION:**</warning>
<warning>
siduction, als Linux-LIVE-DVD/CD, ist sehr stark komprimiert. Aus diesem Grund muss besonders auf die Brennmethode des ISO-Abbilds geachtet werden. Bitte verwendet hochwertige Medien, das Brennen im DAO-Modus (disk-at-once) und nicht schneller als achtfach (8x). Wir empfehlen allerdings, sofern die Hardware das Booten von USB unterstützt, das Abbild auf einen USB-Stick oder eine SD-Speicherkarte zu legen. Dazu empfiehlt sich das Tool Edger oder das Kommandozeilenwerkzeug dd. Anleitung dazu bietet das Handbuch unter Installationsoptionen.
</warning>

Wer bereits Linux auf dem Rechner hat, kann die DVD mit jedem installierten Brennprogramm erstellen. Bei siduction ist K3b das Standard-Brennprogramm. Dort muss man den Menüpunkt "Extras" -> "ISO-Abbild brennen..." anklicken, das zu brennende ISO-File (z.B. siduction-18.3.0-patience-kde-amd64-201805132121.iso) auswählen und den Brennmodus DAO (Disk At Once) einstellen.

K3b berechnet zuerst die MD5-Summe des ISO-Files (dauert einen Moment). Stimmt die angezeigte Prüfsumme mit der angegebenen Zeichenfolge der sich im selben Ordner befindlichen MD5-Datei (z.B. siduction-Name.iso.md5) überein, war der Download erfolgreich und die Datei kann mit einem Klick auf "Start" gebrannt werden.

Klickt man auf die berechnete Prüfsumme, erscheint daneben ein Symbol. Klickt man wiederum darauf und fügt in das Feld die Prüfsumme aus der MD5-Datei ein, so werden die beiden Prüfsummen verglichen.

Die Ursache von Problemen beim Brennen findet sich zumeist in den Frontend-Applikationen. Zum unmittelbaren Brennen von der Konsole kann man das Skript burniso verwenden.
Siehe auch Installation auf USB-Stick/SSD von einem anderen System (Linux. MS Windows, Mac OS X).

---

<div id="rev">Zuletzt bearbeitet: 2020-12-02</div>
