---
title: L’abuso dei file MSC da parte degli Advanced Persistent Threat (APT)
url: https://www.ictsecuritymagazine.com/articoli/file-msc-apt-cybercrime/
source: ICT Security Magazine
date: 2026-05-29
fetch_date: 2026-05-30T05:44:16.357059
---

# L’abuso dei file MSC da parte degli Advanced Persistent Threat (APT)

[Salta al contenuto](#main)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

* [Home](https://www.ictsecuritymagazine.com/)
* [Articoli](https://www.ictsecuritymagazine.com/argomenti/articoli/)
* RubricheEspandi
  + [Cyber Security](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)
  + [Cyber Crime](https://www.ictsecuritymagazine.com/argomenti/cyber-crime/)
  + [Cyber Risk](https://www.ictsecuritymagazine.com/argomenti/cyber-risk/)
  + [Cyber Law](https://www.ictsecuritymagazine.com/argomenti/cyber-law/)
  + [Digital Forensic](https://www.ictsecuritymagazine.com/argomenti/digital-forensic/)
  + [Digital ID Security](https://www.ictsecuritymagazine.com/argomenti/digital-id-security/)
  + [Business Continuity](https://www.ictsecuritymagazine.com/argomenti/business-continuity/)
  + [Digital Transformation](https://www.ictsecuritymagazine.com/argomenti/digital-transformation/)
  + [Cyber Warfare](https://www.ictsecuritymagazine.com/argomenti/cyber-warfare/)
  + [Ethical Hacking](https://www.ictsecuritymagazine.com/argomenti/ethical-hacking/)
  + [GDPR e Privacy](https://www.ictsecuritymagazine.com/argomenti/gdpr-e-privacy/)
  + [IoT Security](https://www.ictsecuritymagazine.com/argomenti/iot-security/)
  + [Industrial Cyber Security](https://www.ictsecuritymagazine.com/argomenti/industrial-cyber-security/)
  + [Blockchain e Criptovalute](https://www.ictsecuritymagazine.com/argomenti/blockchain-e-criptovalute/)
  + [Intelligenza Artificiale](https://www.ictsecuritymagazine.com/argomenti/intelligenza-artificiale/)
  + [Geopolitica e Cyberspazio](https://www.ictsecuritymagazine.com/argomenti/geopolitica-cyberspazio/)
  + [Interviste](https://www.ictsecuritymagazine.com/argomenti/interviste/)
* [Notizie](https://www.ictsecuritymagazine.com/argomenti/notizie/)
* [Pubblicazioni](https://www.ictsecuritymagazine.com/pubblicazioni/)
* [Cybersecurity Video](https://www.ictsecuritymagazine.com/argomenti/cybersecurity-video/)
* [Eventi](https://eventi.ictsecuritymagazine.com/)
* [Newsletter](https://www.ictsecuritymagazine.com/newsletter/)

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Forum ICT Security 2026](https://www.ictsecuritymagazine.com/wp-content/uploads/forum-ict-security-banner-header-2026.jpg)](https://eventi.ictsecuritymagazine.com/eventi/forum-ict-security-2026)

![Abuso dei file MSC negli attacchi APT GrimResource e MSC EvilTwin, Gianfranco Tonello, CEO di TG Soft, Cyber Crime Conference 2026](https://www.ictsecuritymagazine.com/wp-content/uploads/Abuso-dei-file-MSC-negli-attacchi-APT-GrimResource-e-MSC-EvilTwin-Gianfranco-Tonello-CEO-di-TG-Soft-Cyber-Crime-Conference-2026-scaled.jpg)

# L’abuso dei file MSC da parte degli Advanced Persistent Threat (APT)

A cura di:[Redazione](#molongui-disabled-link)  Ore 29 Maggio 202615 Maggio 2026

*Dall’intervento di **Gianfranco Tonello**, CEO di TG Soft, tenutosi alla [14ª Cyber Crime Conference](https://eventi.ictsecuritymagazine.com/eventi/cyber-crime-conference-2026) (Auditorium della Tecnica, Roma, 6-7 maggio 2026).*

## **Un vettore d’attacco emergente**

Dal 2024 i file
`.MSC`
sono entrati stabilmente nell’arsenale dei principali gruppi *Advanced Persistent Threat*. Si tratta di un vettore d’attacco poco intercettato dagli strumenti di *endpoint security* in fase di analisi statica, utilizzato in modo quasi esclusivo da attori state-sponsored o di alto profilo, e finora mai osservato in campagne *commodity* di tipo *infostealer* o RAT diffuso (AgentTesla, Snake Keylogger, Remcos). Nel suo intervento alla 14ª Cyber Crime Conference, Gianfranco Tonello ha ricostruito tecniche di abuso, vulnerabilità sfruttate e operatività dei principali gruppi APT che hanno adottato questo formato.

## **Cos’è un file MSC**

Un file con estensione
`.MSC`
(*Management Saved Console*) è uno *snap-in* della Microsoft Management Console (
`mmc.exe`
), strutturato come documento XML. Nato come strumento amministrativo di Windows, presenta tre caratteristiche che lo rendono particolarmente versatile come vettore d’attacco:

1. la possibilità di **personalizzare l’icona** del file, mimando documenti Word, PDF o di altri formati di uso comune;
2. la presenza di funzionalità native (come **ConsoleTaskpad**) che consentono l’esecuzione di comandi arbitrari;
3. la disponibilità di vulnerabilità documentate (in particolare **GrimResource**) che permettono l’esecuzione automatica di codice all’apertura.

Tonello ha mostrato un esempio dell’APT indiano **Bitter** in cui l’estensione viene mascherata tramite un carattere Unicode di inversione del testo (*Right-to-Left Override*): in Explorer il file appare come .pdf, mentre l’estensione reale è
`.msc`
. Anche la finestra di anteprima del sistema operativo segnala correttamente il file come “Documento di console”, ma l’utente medio si fida dell’icona PDF e procede all’apertura.

## **Le tre modalità di abuso**

### **1. Link diretto**

La modalità più semplice consiste nell’inserire all’interno del file
`.msc`
una **URL malevola** che viene aperta dal motore di rendering interno alla MMC, ancora basato su Internet Explorer (presente in Windows 11 nonostante la dismissione del browser come applicazione utente).

Il caso emblematico è quello del gruppo **Water Gamayun** (alias *EncryptHub*, *Larva-208*), attribuito ad area russofona, che ha sfruttato la vulnerabilità **MSC EvilTwin** (CVE-2025-26633) per distribuire il *Flicker Stealer*. La tecnica prevedeva l’invio di un archivio ZIP contenente due file
`.msc:`
uno legittimo e uno malevolo.

Quello malevolo veniva copiato in una cartella di Windows dedicata alle risorse di localizzazione linguistica; all’apertura del file legittimo, la MMC andava a leggere il file di lingua di default, che corrispondeva a quello malevolo. Il risultato era l’esecuzione di comandi PowerShell che attivavano il *payload* dell’*infostealer* e terminavano poi il processo
`mmc.exe`
. Pur trattandosi di un gruppo *ransomware* e non di un APT in senso stretto, il caso è rappresentativo del livello di sofisticazione delle catene di attacco basate su MSC.

### **2. ConsoleTaskpad**

ConsoleTaskpad è una funzionalità nativa della MMC che permette di associare a un’azione una *command line* personalizzata. Inserendo nel file
`.msc`
una riga di comando di PowerShell, VBScript o CMD, l’attaccante ottiene esecuzione di codice arbitrario. Per concretizzare l’attacco serve l’interazione dell’utente: nel caso reale del gruppo **Sticky Werewolf** mostrato da Tonello, la vittima vede una finta *interfaccia* di “PDF Reader” con un *link* da cliccare, e sono sufficienti due click per innescare l’intera *kill chain*.

### **3. Vulnerabilità GrimResource**

[**GrimResource** è una vulnerabilità](https://www.elastic.co/security-labs/grimresource) della libreria
`apds.dll`
di Microsoft, **nota dal 2019 ma corretta solo nell’ottobre 2024**, dopo che l’incremento di campagne APT che la sfruttavano ha reso necessario l’intervento del vendor. La vulnerabilità permette l’esecuzione automatica di *script* all’apertura del file
`.msc`
, senza ulteriori interazioni dell’utente oltre al doppio click iniziale. È la modalità più impiegata dagli APT analizzati.

![Abuso dei file MSC negli attacchi APT: GrimResource e MSC EvilTwin, Gianfranco Tonello, CEO di TG Soft, Cyber Crime Conference 2026](https://www.ictsecuritymagazine.com/wp-content/uploads/chrome_YQDRneKZS0-700x388.png)

*Gianfranco Tonello, CEO di TG Soft, Cyber Crime Conference 2026*

## **I gruppi APT che abusano dei file MSC**

Tonello ha presentato una cronologia degli operatori che hanno adottato il vettore ...