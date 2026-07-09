---
title: Parser-Schwachstellen in Mobilfunk-Protokollen
url: https://smartphone-attack-vector.de/parser-schwachstellen-mobilfunk-protokolle/
source: Smartphone Security
date: 2026-07-08
fetch_date: 2026-07-09T06:02:23.064466
---

# Parser-Schwachstellen in Mobilfunk-Protokollen

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

# Parser-Schwachstellen in Mobilfunk-Protokollen

AV: A15

## Details:

Viele Mobilfunkangriffe zielen nicht nur auf Kryptografie, sondern auf die Parser-Logik von Protokollnachrichten. Bereits einzelne fehlerhafte oder unerwartete Felder in NAS-/S1AP-/NGAP-Nachrichten können durch unzureichende Längen-, Typ- oder Zustandsprüfungen zu Abstürzen oder im Einzelfall zu weitergehenden Kompromittierungen führen [1].

Aktuelle Untersuchungen zeigen, dass solche Parsing-Schwachstellen über verschiedene LTE/5G-Implementierungen hinweg auftreten können und sowohl Verfügbarkeit als auch Integrität der Mobilfunkinfrastruktur gefährden [2].

**Quellen/Links:**

* [1] [RANsacked: Überblick zu Parsing- und Protokollschwachstellen in LTE/5G-Kernen](https://cellularsecurity.org/ransacked.html)
* [2] [RANsacked-Paper: technische Analyse und Methodik](https://nathanielbennett.com/publications/ransacked.pdf)

---

## Erkennung:

Für Endnutzer sind Parsing-Angriffe häufig nur indirekt sichtbar: wiederkehrende, lokale Netzabbrüche, ungewöhnliche Nichtverfügbarkeit von Telefonie/Daten oder stark schwankendes Netzverhalten ohne ersichtlichen Grund.

Auf Betreiberseite weisen plötzliche Prozessabstürze, gehäufte Fehlermeldungen bei Protokolldecodierung und reproduzierbare Fehler bei bestimmten Nachrichtentypen auf parsernahe Schwachstellen hin. Eine belastbare Erkennung erfordert strukturierte Log- und Protokollanalyse.

**Quellen/Links:**

* [RANsacked: dokumentierte Beispiele für parserbasierte Fehlerbilder](https://cellularsecurity.org/ransacked.html)
* [RANsacked-Paper: Testmethodik und reproduzierbare Angriffspfade](https://nathanielbennett.com/publications/ransacked.pdf)

---

## Gegenmaßnahmen:

Die wirksamsten Gegenmaßnahmen sind robuste Eingabevalidierung und defensives Parsen: strikte Längen- und Typprüfungen, sichere Fehlerbehandlung ohne Assertions im Produktivpfad, sowie systematisches Fuzzing und Regressionstests für Protokollparser.

Zusätzlich helfen gestufte Rollouts von Patches, enges Monitoring kritischer Protokollpfade und Architekturmaßnahmen, die den Schaden einzelner Parserfehler begrenzen. In Hochrisiko-Umgebungen sollten parserbezogene Testfälle kontinuierlich in den Betriebsprozess integriert werden.

**Quellen/Links:**

* [RANsacked-Paper: Empfehlungen zu Härtung und Teststrategie](https://nathanielbennett.com/publications/ransacked.pdf)
* [RANsacked: CVE-bezogene Befundübersicht über mehrere Implementierungen](https://cellularsecurity.org/ransacked.html)

---

Kategorien:

## Weitere Vektoren aus dem Bereich

#### // wichtige Links

* [diplomarbeit mobile security](https://smartphone-attack-vector.de/diplomarbeit-mobile-security/)
* [Sicherheitstools und Apps für den Mobilfunk](https://smartphone-attack-vector.de/linksammlung-von-sicherheitstools-und-apps-fuer-den-mobilfunk/)
* [Quellenangaben](https://smartphone-attack-vector.de/quellenangaben/)
* [Datenschutz](https://smartphone-attack-vector.de/dts/)
* [Impressum](https://smartphone-attack-vector.de/impressum/)

#### // Lösungen

* [Allgemeines zum RF/Baseband](https://smartphone-attack-vector.de/radio-frequency-analysis/)
* [IMSI-Catcher, Stingray, Fake Base Station Detector](https://smartphone-attack-vector.de/imsi-catcher_stingray_detector/)
* [LTE Catcher & Stingrays 2.0](https://smartphone-attack-vector.de/lte-catcher-stingrays_2)
* [SIM Proxy, SIM security hardware](https://smartphone-attack-vector.de/sim-security-hardware/)
* [Krypto Handys & SNS](https://smartphone-attack-vector.de/krypto-handy/)
* [PKI](https://smartphone-attack-vector.de/pki/)

#### // Artikel

* [LTE Protokolle und Schwachstellen](https://smartphone-attack-vector.de/lte-protokolle/)
* [Caller ID-Spoofing](https://smartphone-attack-vector.de/caller-id-spoofing/)
* [Assisted GPS (A-GPS)](https://smartphone-attack-vector.de/assisted-gps-a-gps/)
* [Roving Bug](https://smartphone-attack-vector.de/roving-bug/)
* [SS7 Protokolle](https://smartphone-attack-vector.de/ss7-protokolle/)
* [Stille SMS](https://smartphone-attack-vector.de/stille-sms/)

![CC BY](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by.svg)

**Smartphone-Attack-Vector** von Marcus Prem ist lizenziert unter einer
[Creative Commons Namensnennung 4.0 International Lizenz](https://creativecommons.org/licenses/by/4.0/).

Ausgenommen Inhalte mit Quellenverweis. Icons Credits.

powered by dm-development