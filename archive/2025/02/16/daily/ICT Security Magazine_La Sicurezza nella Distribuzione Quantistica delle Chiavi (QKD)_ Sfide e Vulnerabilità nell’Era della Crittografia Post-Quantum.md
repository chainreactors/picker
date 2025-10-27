---
title: La Sicurezza nella Distribuzione Quantistica delle Chiavi (QKD): Sfide e Vulnerabilità nell’Era della Crittografia Post-Quantum
url: https://www.ictsecuritymagazine.com/articoli/distribuzione-quantistica-delle-chiavi/
source: ICT Security Magazine
date: 2025-02-16
fetch_date: 2025-10-06T20:37:22.507943
---

# La Sicurezza nella Distribuzione Quantistica delle Chiavi (QKD): Sfide e Vulnerabilità nell’Era della Crittografia Post-Quantum

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
* [Eventi](https://www.ictsecuritymagazine.com/eventi/)
* [Newsletter](https://www.ictsecuritymagazine.com/newsletter/)

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine1403) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Forum ICT Security 2025](https://www.ictsecuritymagazine.com/wp-content/uploads/banner-header-2025.jpg)](https://www.ictsecuritymagazine.com/eventi/forumictsecurity2025)

![La Sicurezza nella Distribuzione Quantistica delle Chiavi (QKD): Sfide e Vulnerabilità nell'Era della Crittografia Post-Quantum](https://www.ictsecuritymagazine.com/wp-content/uploads/La-Sicurezza-nella-Distribuzione-Quantistica-delle-Chiavi-QKD-Sfide-e-Vulnerabilita-nell-Era-della-Crittografia-Post-Quantum.jpg)

# La Sicurezza nella Distribuzione Quantistica delle Chiavi (QKD): sfide e vulnerabilità nell’era della Crittografia Post-Quantum

A cura di:[Redazione](#molongui-disabled-link)  Ore 15 Febbraio 202517 Febbraio 2025

La distribuzione quantistica delle chiavi (QKD) rappresenta una [tecnologia crittografica all’avanguardia](https://www.ictsecuritymagazine.com/articoli/elaboratori-quantistici-e-crittografia-post-quantum-oggi/) che permette lo scambio sicuro di chiavi private tra parti geograficamente distanti attraverso canali non sicuri. La sua evoluzione, iniziata con il protocollo BB84 proposto da Bennett e Brassard nel 1984, si basa sui principi della fisica quantistica, in particolare sul principio di indeterminazione e sul teorema di non clonazione.

## L’importanza della Distribuzione Quantistica delle Chiavi (QKD) nell’era Post-Quantum e le sue vulnerabilità pratiche

La crescente minaccia rappresentata dai computer quantistici ha reso la QKD particolarmente rilevante per la sicurezza delle comunicazioni future. Gli algoritmi quantistici come Shor e Grover potrebbero potenzialmente compromettere molti dei protocolli crittografici pubblici attualmente in uso. La QKD offre una sicurezza teoricamente inattaccabile quando combinata con l’algoritmo *one-time-pad*, poiché la sua sicurezza non dipende dalla potenza computazionale dell’attaccante.

### Implementazioni e varianti dei Sistemi QKD

I sistemi QKD si distinguono principalmente in tre categorie: [sistemi a variabili discrete (DV-QKD), sistemi a variabili continue (CV-QKD)](https://www.politesi.polimi.it/handle/10589/222701) e sistemi basati sul riferimento di fase distribuito (DPR-QKD). Ogni implementazione presenta vantaggi e sfide specifiche in termini di sicurezza e prestazioni. I sistemi DV-QKD, basati sulla polarizzazione dei fotoni singoli, offrono un’elevata sicurezza teorica ma sono più sensibili alle imperfezioni del canale di trasmissione. I sistemi CV-QKD, che utilizzano stati coerenti della luce, risultano più robusti nelle implementazioni pratiche ma richiedono una gestione più complessa del rumore.

#### Vulnerabilità dei Sistemi QKD: analisi delle principali minacce

L’attacco Trojan-horse rappresenta una delle minacce più significative, dove un attaccante può sondare la configurazione interna del dispositivo utilizzando impulsi luminosi per ottenere informazioni sulla preparazione degli stati quantistici. Gli attacchi multi-fotone sfruttano invece le imperfezioni delle sorgenti laser, che possono emettere più fotoni contemporaneamente, permettendo potenzialmente a un attaccante di intercettare parte dell’informazione senza essere rilevato.

La sicurezza del canale classico autenticato rappresenta un altro punto critico: un attaccante che riesca a compromettere l’autenticazione potrebbe effettuare attacchi man-in-the-middle, compromettendo l’intero processo di distribuzione delle chiavi. Gli attacchi denial-of-service, sebbene non compromettano direttamente la sicurezza delle chiavi, possono rendere il sistema inutilizzabile.

#### Contromisure e soluzioni per la Sicurezza QKD

Per contrastare queste vulnerabilità, sono state sviluppate diverse contromisure. L’uso degli stati esca (decoy states) rappresenta una delle soluzioni più efficaci contro gli attacchi multi-fotone, permettendo di rilevare tentativi di intercettazione. L’amplificazione della privacy nel post-processing delle chiavi aiuta a ridurre qualsiasi potenziale fuga di informazioni durante il processo di correzione degli errori.

L’implementazione di protocolli QKD *device-independent* e *measurement-device-independent* offre ulteriori livelli di sicurezza, riducendo la dipendenza dall’affidabilità dei dispositivi di misura. Questi approcci innovativi stanno guadagnando sempre più attenzione nella comunità scientifica e industriale.

### Standardizzazione e integrazione QKD: le ultime novità dal NIST

Il NIST ha recentemente completato gli standard per gli algoritmi di crittografia post-quantica, segnando una pietra miliare per la sicurezza delle comunicazioni future. Tre nuovi standard sono stati finalizzati:

* FIPS 203 (ML-KEM): standard primario per la crittografia generale, basato su CRYSTALS-Kyber;
* FIPS 204 (ML-DSA): standard primario per firme digitali, basato su CRYSTALS-Dilithium;
* FIPS 205 (SLH-DSA): standard di backup per firme digitali, basato su Sphincs+

Il NIST incoraggia gli amministratori di sistema ad iniziare l’integrazione immediata di questi standard, poiché la transizione richiederà tempo. Un quarto standard (FIPS 206) basato su FALCON è previsto per fine 2024.

Questi sviluppi sono fondamentali per l’integrazione della QKD nelle infrastrutture esistenti, fornendo un framework di sicurezza post-quantica standardizzato. Gli standard permetteranno l’interoperabilità tra sistemi QKD di diversi produttori, accelerando l’adozione di questa tecnologia nelle reti di comunicazione attuali.

Le reti QKD metropolitane come quel...