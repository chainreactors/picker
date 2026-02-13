---
title: Parlare il linguaggio dei dispositivi Bluetooth: analisi di protocolli BLE proprietari con Frida ed ESP32
url: https://www.ictsecuritymagazine.com/articoli/ble/
source: ICT Security Magazine
date: 2026-02-12
fetch_date: 2026-02-13T04:18:20.224819
---

# Parlare il linguaggio dei dispositivi Bluetooth: analisi di protocolli BLE proprietari con Frida ed ESP32

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

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine1403) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Cyber Crime Conference 2026](https://www.ictsecuritymagazine.com/wp-content/uploads/Cyber-Crime-Conference-2026-1920x278-2.jpg)](https://eventi.ictsecuritymagazine.com/eventi/cyber-crime-conference-2026)

![BLE bluethoot](https://www.ictsecuritymagazine.com/wp-content/uploads/ble.jpeg)

# Parlare il linguaggio dei dispositivi Bluetooth: analisi di protocolli BLE proprietari con Frida ed ESP32

A cura di:[Matteo Mandolini](#molongui-disabled-link)  Ore 12 Febbraio 202612 Febbraio 2026

*Una metodologia pratica per comprendere i rischi di sicurezza nei wearable commerciali*

## Il panorama IoT e l’espansione della superficie di attacco

Nel mondo sono oggi attive decine di miliardi di dispositivi Internet of Things (IoT). Le proiezioni indicano che questo numero continuerà a crescere rapidamente nel corso del prossimo decennio. Questa crescita è alimentata dalla diffusione di wearable, sensori domestici intelligenti, dispositivi medicali connessi, smart lock e sistemi industriali IoT.

L’aumento della connettività porta con sé un ampliamento proporzionale della superficie di attacco. Molti dispositivi [IoT](https://www.ictsecuritymagazine.com/pubblicazioni/onboarding-dei-dispositivi-iot/) vengono progettati con priorità su costo ridotto, autonomia energetica e facilità d’uso, mentre la sicurezza viene spesso considerata solo in una fase successiva o completamente trascurata. Questa logica “security as an afterthought” ha creato un ecosistema vulnerabile composto da miliardi di dispositivi potenzialmente compromettibili.

![bluethoot law](https://www.ictsecuritymagazine.com/wp-content/uploads/iot-1-700x392.jpg)

## Bluetooth Low Energy: il protocollo dominante nell’IoT a basso consumo

Il Bluetooth Low Energy (BLE), introdotto nelle specifiche Bluetooth 4.0 nel 2010, rappresenta oggi uno dei protocolli più utilizzati nell’ecosistema IoT moderno. A differenza del Bluetooth Classic, il BLE è stato progettato specificamente per dispositivi alimentati a batteria che necessitano di comunicazioni brevi e sporadiche con consumo energetico ridottissimo.

La sua adozione massiva in wearable, fitness tracker, smart band, sensori medicali e dispositivi domestici lo rende un vettore di attacco particolarmente rilevante. I rischi associati al BLE spaziano dagli accessi non autorizzati a dispositivi fisici tramite replicazione di comandi, alla replica di protocolli proprietari per interazione non prevista, passando per attacchi di prossimità che sfruttano il raggio di trasmissione radio. La possibilità di automazione su larga scala di interazioni malevole rende questi vettori ancora più pericolosi, con impatti concreti su sicurezza fisica, privacy e continuità operativa.

La comprensione delle modalità di comunicazione BLE è quindi fondamentale per chi si occupa di sicurezza hardware, penetration testing IoT e analisi di dispositivi embedded.

## SweynTooth: quando le vulnerabilità BLE colpiscono i dispositivi

Per comprendere la rilevanza della sicurezza BLE, è utile analizzare un caso documentato che ha dimostrato l’impatto reale delle vulnerabilità in questo protocollo.

Nel febbraio 2020, ricercatori del SUTD (Singapore University of Technology and Design) pubblicarono SweynTooth, una famiglia di 12 vulnerabilità zero-day che colpivano gli stack BLE di sei diversi produttori di System-on-Chip (SoC): Texas Instruments, NXP, Cypress, Dialog Semiconductors, Microchip e Telink Semiconductor.

Le caratteristiche che resero SweynTooth particolarmente rilevante includevano la natura completamente over-the-air dell’attacco, che non richiedeva pairing o autenticazione, e l’assenza di qualsiasi interazione con l’utente del dispositivo target. Le vulnerabilità permettevano di causare deadlock, crash e in alcuni casi information disclosure, con una superficie di impatto estesa a miliardi di dispositivi commerciali, medicali e industriali.

Un attaccante poteva causare Denial of Service su dispositivi BLE inviando pacchetti malformati durante le fasi di connection, data transfer o pairing. In alcuni casi, le vulnerabilità permettevano anche il bypass di procedure di sicurezza come il pairing numerico o l’esfiltrazione di informazioni dalla memoria.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Nome Vulnerabilità** | **CVE ID** | **Stato del Protocollo** | **Tipo di Impatto** | **Esempio Prodotto IoT** |
| Link Layer Length Overflow | CVE-2019-16336, CVE-2019-17519 | Fase iniziale della connessione (initial\_setup) | Crash | Fitbit Inspire |
| LLID Deadlock | CVE-2019-17061, CVE-2019-17060 | Fase iniziale della connessione (initial\_setup) | Crash o Deadlock | Fitbit Inspire |
| Truncated L2CAP | CVE-2019-17517 | Scoperta dei servizi primari (list\_pri\_services) | Crash | Non specificato |
| Silent Length Overflow | CVE-2019-17518 | Procedura di pairing (smp\_pairing) | Crash | Eve Energy, August Smart Lock |
| Public Key Crash | CVE-2019-17520 | Procedura di pairing (smp\_pairing) | Crash | CubiTag |
| Invalid Connection Request | CVE-2019-19193 | Stabilimento della connessione (connection) | Deadlock (DoS) | eGeeTouch TSA Lock |
| Invalid L2CAP Fragment | CVE-2019-19195 | Scoperta servizi / Lettura-Scrittura GATT | Crash | Non specificato |
| Sequential ATT Deadlock | CVE-2019-19192 | Lettura-Scrittura GATT (gatt\_read/write) | Crash / Deadlock | Non specificato |
| Key Size Overflow | CVE-2019-19196 | Richiesta di pairing (pairing\_req) | Crash | Non specificato |
| Zero LTK ...