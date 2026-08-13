---
title: SIM-originierende AT-Kommandos (CATana)
url: https://smartphone-attack-vector.de/sim-originierende-at-kommandos-catana/
source: Smartphone Security
date: 2026-08-12
fetch_date: 2026-08-13T04:03:38.290533
---

# SIM-originierende AT-Kommandos (CATana)

[![Smartphone Attack Vector](https://smartphone-attack-vector.de/wp-content/uploads/2013/03/artikelbild_smartphone-security.jpg)](https://smartphone-attack-vector.de/)

* [Home](https://smartphone-attack-vector.de/)
* Grundlagen
  + [Übersicht](https://smartphone-attack-vector.de/wissen-3/)
  + [Mobilfunknetz](https://smartphone-attack-vector.de/wissen-3/mobilfunknetz/)
  + [Mobilfunkdienste](https://smartphone-attack-vector.de/wissen-3/mobilfunkdienste/)
  + [Lawful Interception](https://smartphone-attack-vector.de/wissen-3/lawful-interception/)
  + [Smartphones](https://smartphone-attack-vector.de/wissen-3/wissen-2/)
  + [Standortbestimmung und Ortung](https://smartphone-attack-vector.de/wissen-3/standortbestimmung-und-ortung/)
  + [Operating Systems](https://smartphone-attack-vector.de/betriebssysteme/ "Mobile OS")
    - [Apple iOS](https://smartphone-attack-vector.de/betriebssysteme/apple-ios/)
    - [Android](https://smartphone-attack-vector.de/betriebssysteme/android/)
* Attack Vectors
  + [Kategorien](https://smartphone-attack-vector.de/kategorien/)
  + [Tabellenansicht](https://smartphone-attack-vector.de/kategorien/luftschnittstelle/)
  + [Luftschnittstelle](https://smartphone-attack-vector.de/category/gsm-csm-gprs-edge-umts-und-lte/)
  + [Mobilfunkdienste](https://smartphone-attack-vector.de/category/mobilfunk-smsmms-ussd-mmi/)
  + [Providernetz](https://smartphone-attack-vector.de/category/mobilfunk-netzwerk/)
  + [Fremde Netze](https://smartphone-attack-vector.de/category/netzwerke-global/)
  + [Lawful Interception](https://smartphone-attack-vector.de/category/infrastruktur-zum-abhoren/)
  + [Schnittstellen am Smartphone](https://smartphone-attack-vector.de/category/2g-3g-4g-modem_sim-karte/)
  + [Standortbestimmung und Ortung](https://smartphone-attack-vector.de/category/ortung-standort/)
* Lösungen
  + [Übersicht](https://smartphone-attack-vector.de/security_solutions/)
  + [Allgemeines zum RF/Baseband](https://smartphone-attack-vector.de/radio-frequency-analysis/)
  + [PKI](https://smartphone-attack-vector.de/pki/ "Public Key Infrastruktur")
  + [Krypto Handys & SNS](https://smartphone-attack-vector.de/krypto-handy/)
  + [GSM/UMTS/LTE Gateway](https://smartphone-attack-vector.de/gsm-umts-lte-gateway/)
  + [IMSI-Catcher, Stingray, Fake Base Station Detector](https://smartphone-attack-vector.de/imsi-catcher_stingray_detector/)
  + [LTE Catcher & Stingrays 2.0 (wip)](https://smartphone-attack-vector.de/lte-catcher-stingrays_2/)
    - [SDR (Software defind radio)](https://smartphone-attack-vector.de/sdr-software-defind-radio/)
  + [SIM Proxy, SIM security hardware](https://smartphone-attack-vector.de/sim-security-hardware/)
* [Links](https://smartphone-attack-vector.de/linksammlung-von-sicherheitstools-und-apps-fuer-den-mobilfunk/ "interesting links")
* Dokumente
  + [Alle original Inhalte](https://smartphone-attack-vector.de/diplomarbeit-mobile-security/ "Download Pdf")
  + [Quellenangaben](https://smartphone-attack-vector.de/quellenangaben/)

# SIM-originierende AT-Kommandos (CATana)

AV: E15
 **Status:** Aktiv
 **Thread Level:** High
 **Auswirkungen:**
Vertraulichkeit, Integrität, Verfügbarkeit, Geräteidentifikation, Datenmanipulation, DoS, Geräteabsturz, RCE, Datendiebstahl
 **Voraussetzung/Distanz:**
Remote Internet, Physischer Zugriff, Supply Chain

Veröffentlicht: 12.08.2026
Aktualisiert: 12.08.2026

Eine bösartige oder kompromittierte SIM beziehungsweise eSIM kann über den standardisierten Proactive-SIM-Befehl **RUN AT COMMAND** AT-Kommandos an das Mobilfunkmodem eines Geräts senden. Die CATana-Studie zeigte, dass 9 von 26 untersuchten Smartphones und IoT-Mobilfunkgeräten eine solche SIM-AT-Schnittstelle exponierten. Je nach Implementierung sind unter anderem Informationsabfluss, Manipulation der Mobilfunkkonfiguration, ein Downgrade von 4G auf 2G, Denial-of-Service und Codeausführung im Kommunikationsprozessor möglich.

Der Angriffsweg setzt eine bösartige oder zuvor kompromittierte SIM/eSIM voraus. Denkbare Ausgangspunkte sind physischer SIM-Tausch, Eingriffe in der Lieferkette, missbrauchte Fernverwaltung durch einen Provider oder eine remote ausgenutzte Schwachstelle in SIM-Software. Eine Benutzerinteraktion am Endgerät ist für die Ausführung SIM-originierender Kommandos grundsätzlich nicht erforderlich.

## MITRE ATT&CK

### T1203 – Exploitation for Client Execution (T1203)

**Matrix:**
Mobile

**Taktik:**
Execution
(TA0002)

**Technik:**
Exploitation for Client Execution

### T1466 – Downgrade to Insecure Protocols (T1466)

**Matrix:**
Mobile

**Taktik:**
Network Effects

**Technik:**
Downgrade to Insecure Protocols

### T1464 – Network Denial of Service (T1464)

**Matrix:**
Mobile

**Taktik:**
Impact
(TA0040)

**Technik:**
Network Denial of Service

## Details:

Proactive SIM erlaubt einer SIM-Anwendung, definierte Befehle an das Mobile Equipment (ME) zu senden. Beim Befehl `RUN AT COMMAND` fordert die SIM das Gerät auf, ein angegebenes AT-Kommando auszuführen. Dadurch entsteht eine Schnittstelle von der SIM zum Modem, die historisch unter der Annahme einer vertrauenswürdigen SIM entworfen wurde.

Lisowski, Covic und Muench untersuchten mit dem Werkzeug CATana 18 Smartphones und 8 IoT-Geräte. Neun der 26 Geräte exponierten die SIM-AT-Schnittstelle; daraus gingen vier Schwachstellen hervor. Die Fallstudien umfassen beliebige Dateizugriffe, das erneute Aktivieren von Debug-Schnittstellen, das Auslesen eindeutiger Gerätekennungen, das Senden von Nachrichten oder Initiieren von Anrufen, Codeausführung im Kommunikationsprozessor, 4G-zu-2G-Downgrades sowie das Abschalten des Geräts oder seiner Mobilfunkverbindung.

**Einordnung der Kennungen:** Die University of Birmingham nennt für die Studie CVE-2025-48618, CVE-2026-57550 und CVD-2026-0122. CVE-2025-48618 bezeichnet einen separaten Android-Befund, bei dem eine Proactive-SIM-Browseraktion trotz Sperrbildschirm möglich war. Die exponierte SIM-AT-Schnittstelle wurde von den Forschenden CVE-2026-57550 (Qualcomm) und CVD-2026-0122 (GSMA) zugeordnet. Der offizielle CVE-Datensatz zu CVE-2026-57550 ist inzwischen jedoch als *Rejected* markiert, weil die Kennung laut CNA unbenutzt blieb. Sie ist deshalb nur als historische Disclosure-Kennung und nicht als aktive bestätigte CVE zu behandeln.

**5G-Bezug:** Der Vektor liegt an der SIM-/eSIM-zu-Modem-Schnittstelle und ist nicht auf eine einzelne Funkgeneration beschränkt. Auch bei 5G-fähigen Geräten bleibt er relevant, sofern deren Modem-Firmware SIM-originierende AT-Kommandos akzeptiert. Das demonstrierte Downgrade auf 2G kann vorhandene Schutzmechanismen moderner Netze zusätzlich umgehen; die tatsächliche Exponierung ist geräte- und firmwareabhängig.

---

## Erkennung:

Eine direkte Erkennung durch den Nutzer ist schwierig, da die Kommandos zwischen SIM und Modem verarbeitet werden und keine sichtbare Oberfläche benötigen. In einer technischen Analyse sollten SIM-ME/APDU-Traces gezielt auf Proactive-SIM-Kommandos vom Typ `RUN AT COMMAND` geprüft und die enthaltenen AT-Kommandos gegen eine enge Positivliste bewertet werden.

Zusätzliche Indikatoren sind unerwartet aktivierte Debug-Schnittstellen, nicht veranlasste Anrufe oder Nachrichten, Änderungen der bevorzugten Mobilfunktechnik, ein unerklärlicher Wechsel auf 2G, ungewöhnliche Modem-Neustarts sowie der plötzliche Verlust der Mobilfunkverbindung. CATana eignet sich zur reproduzierbaren Untersuchung betroffener Geräte in einer kontrollierten Laborumgebung.

---

## Gegenmaßnahmen:

Hersteller sollten die SIM-AT-Schnittstelle deaktivieren oder veraltete Proactive-SIM-Funktionen vollständig entfernen, sofern sie nicht zwingend benötigt werden. Ist eine Unterstützung erforderlich, müssen zulässige AT-Kommandos strikt begrenzt, Parameter validiert und privilegierte, Diagnose- oder dateibezogene Kommandos aus dem SIM-Kontext blockiert werden.

Geräte- und Modem-Firmware sollte auf dem aktuellen Herstellerstand gehalten werden. Betreiber und eSIM-Plattformen sollten Remote-SIM-Management ab...