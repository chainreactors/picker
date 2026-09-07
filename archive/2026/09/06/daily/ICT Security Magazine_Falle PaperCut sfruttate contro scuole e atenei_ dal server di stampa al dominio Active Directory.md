---
title: Falle PaperCut sfruttate contro scuole e atenei: dal server di stampa al dominio Active Directory
url: https://www.ictsecuritymagazine.com/notizie/vulnerabilita-papercut-attacchi-scuole-universita/
source: ICT Security Magazine
date: 2026-09-06
fetch_date: 2026-09-07T06:49:22.806573
---

# Falle PaperCut sfruttate contro scuole e atenei: dal server di stampa al dominio Active Directory

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
  + [Prospettive](https://www.ictsecuritymagazine.com/argomenti/prospettive/)
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

![Due vulnerabilità concatenate di PaperCut NG/MF sono state usate per rubare credenziali a scuole e atenei in Europa e negli Stati Uniti. Il caso mostra perché un server di stampa integrato con la directory va trattato come sistema critico, anche ai fini NIS2](https://www.ictsecuritymagazine.com/wp-content/uploads/Falle-PaperCut-sfruttate-contro-scuole-e-atenei-dal-server-di-stampa-al-dominio-Active-Directory.png)

# Falle PaperCut sfruttate contro scuole e atenei: dal server di stampa al dominio Active Directory

A cura di:[Redazione](#molongui-disabled-link)  Ore 6 Settembre 20266 Settembre 2026

*Due vulnerabilità concatenate di PaperCut NG/MF sono state usate per rubare credenziali a scuole e atenei in Europa e negli Stati Uniti. Il caso mostra perché un server di stampa integrato con la directory va trattato come sistema critico, anche ai fini NIS2.*

Un server di gestione delle stampe compare raramente negli inventari delle risorse critiche. Eppure, tra fine agosto e i primi di settembre 2026, attaccanti non identificati lo hanno usato per raccogliere credenziali di scuole e università in Europa e negli Stati Uniti. Lo documenta l’[analisi dell’Adversary Research Team di Arctic Wolf](https://github.com/rtkwlf/wolf-tools/tree/main/pack_alerts/202609-papercut-cve-exploitation), datata 4 settembre e ripresa dalla stampa specializzata il giorno seguente. La catena di sfruttamento parte da due vulnerabilità di PaperCut NG/MF. In pochi passaggi arriva agli *hive* del registro di Windows e ai file di configurazione che custodiscono le credenziali verso Active Directory e LDAP.

Le vulnerabilità erano già note. La novità del rapporto è il quadro completo: chi viene colpito, con quali strumenti e che cosa cercano gli attaccanti una volta dentro.

## La campagna secondo Arctic Wolf

Il rapporto, firmato dagli analisti Jens Pose e Ross Phillips, documenta lo sfruttamento di server PaperCut vulnerabili a CVE-2026-81578 e CVE-2026-82078. Le attività osservate comprendono esecuzione di comandi, ricognizione e tentativi di creare account privilegiati. Arctic Wolf ha precisato a [The Hacker News](https://thehackernews.com/2026/09/attackers-exploit-papercut-flaws-to.html) che le vittime appartengono al settore dell’istruzione in senso ampio: dalle scuole primarie e secondarie (il segmento statunitense K-12) alle grandi università, negli Stati Uniti e in Europa. Nessuna istituzione è stata nominata e il rapporto non propone alcuna attribuzione.

La cronologia mostra quanto rapidamente si è aperta la finestra di esposizione. Le date, indicate di seguito, sono tratte dall’[avviso di sicurezza di PaperCut](https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/), dall’avviso CISA e dal rapporto Arctic Wolf; dove la fonte è un’azienda di sicurezza:

* **26 agosto 2026**: Huntress dichiara di aver rilevato la prima attività di attacco nota e di aver riprodotto una catena completa di esecuzione di codice remoto senza autenticazione contro un’installazione standard di PaperCut NG.
* **27 agosto**: PaperCut pubblica l’avviso urgente e conferma incidenti presso i clienti. La prima patch di emergenza per le versioni 25 e 26 esce alle 02:10 del 28 agosto, ora australiana, cioè la sera del 27 in Europa.
* **28 agosto**: vengono assegnate le due CVE. In serata PaperCut pubblica la Emergency Patch Release 2, con misure di irrobustimento sviluppate con Huntress e watchTowr, perché la prima patch era aggirabile; poche ore dopo la estende alla versione 24.
* **29 agosto**: la società Defused riferisce di attività di sfruttamento nei propri honeypot, con un attore che usa l’aggiramento dell’autenticazione per estrarre tabelle dal database interno Derby anziché eseguire codice.
* **31 agosto**: [CISA inserisce entrambe le CVE](https://www.cisa.gov/news-events/alerts/2026/08/31/cisa-adds-two-known-exploited-vulnerabilities-catalog) nel catalogo Known Exploited Vulnerabilities con un unico avviso, richiamando la Binding Operational Directive 26-04 sulla correzione prioritaria delle vulnerabilità sfruttate. Lo stesso giorno il CSIRT Italia pubblica l’alert AL04/260831/CSIRT-ITA. Rapid7 rende disponibile un modulo Metasploit.
* **1 settembre**: PaperCut pubblica la Emergency Patch Release 3 per le versioni 24, 25 e 26. È cumulativa, corregge due regressioni (accesso SAML e driver Microsoft SQL Server legacy per la ricerca esterna dei numeri di tessera) e, secondo il produttore, chiude ulteriori vettori osservati in rete.
* **2 settembre**: il produttore segnala una seconda ondata di attacchi contro i server esposti e non completamente aggiornati, con comportamento post compromissione più sofisticato.
* **4 settembre**: Arctic Wolf pubblica l’analisi della campagna contro il settore dell’istruzione.

Sul piano tecnico, PaperCut classifica CVE-2026-81578 come difetto di controllo degli accessi nell’interfaccia web di amministrazione (CWE-306, CVSS 4.0 pari a 8.8). In determinate condizioni, richieste remote non autenticate dirette a funzioni amministrative attivano azioni prima che la verifica degli accessi sia completata. L’effetto è la modifica di alcune configurazioni di sistema. CVE-2026-82078 (...