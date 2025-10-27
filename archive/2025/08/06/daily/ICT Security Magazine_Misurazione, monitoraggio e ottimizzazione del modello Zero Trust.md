---
title: Misurazione, monitoraggio e ottimizzazione del modello Zero Trust
url: https://www.ictsecuritymagazine.com/articoli/monitoraggio-zero-trust/
source: ICT Security Magazine
date: 2025-08-06
fetch_date: 2025-10-07T00:49:10.922925
---

# Misurazione, monitoraggio e ottimizzazione del modello Zero Trust

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

![monitoraggio Zero Trust: metriche di sicurezza, indicatori di compromissione e framework di valutazione per l'implementazione efficace del modello di sicurezza Zero Trust.](https://www.ictsecuritymagazine.com/wp-content/uploads/modello-zero-trust.jpeg)

# Misurazione, monitoraggio e ottimizzazione del modello Zero Trust

A cura di:[Fabrizio Fioravanti](#molongui-disabled-link)  Ore 5 Agosto 202526 Agosto 2025

Questo contenuto fa parte di una [serie](https://www.ictsecuritymagazine.com/articoli/trust-applicazioni/) dedicata al modello Zero Trust analizzato dal Dott. Ing. Fabrizio Fioravanti. In questo approfondimento esploriamo l’importanza del monitoraggio continuo nell’implementazione del modello Zero Trust, analizzando le metriche fondamentali per valutare l’efficacia delle misure di sicurezza adottate, dagli indicatori di base agli analytics avanzati, fino all’integrazione con framework come MITRE ATT&CK per una gestione proattiva della sicurezza aziendale.

## Monitoraggio efficace nel modello Zero Trust

Una volta implementato il modello Zero Trust a livello organizzativo e tecnologico, è cruciale monitorarne l’efficacia attraverso metriche adeguate e sistematicamente articolate. Questo processo di monitoraggio deve essere continuo e approfondito, al fine di garantire che tutte le dimensioni del modello siano adeguatamente coperte e che eventuali vulnerabilità emergenti vengano prontamente identificate e risolte.

Ciò consente di individuare possibili aree di miglioramento e di identificare eventuali lacune nel modello in uso, permettendo così una gestione proattiva delle risorse di sicurezza e un costante aggiornamento delle difese. Analogamente ai processi di gestione della qualità, il feedback continuo dal contesto operativo è essenziale per instaurare un ciclo virtuoso di miglioramento incrementale, che si traduce in una progressiva maturazione della postura di sicurezza aziendale.

Il monitoraggio del modello Zero Trust richiede l’impiego di metriche strutturate e specifiche, che riflettano in modo accurato lo stato di sicurezza dell’organizzazione. Alcune metriche fondamentali comprendono:

* Il numero di dispositivi gestiti all’interno dell’organizzazione, o la percentuale di dispositivi gestiti rispetto al totale. Questo parametro consente di valutare la capacità dell’organizzazione di mantenere sotto controllo il proprio ambiente tecnologico e di prevenire l’accesso a risorse aziendali da parte di dispositivi non autorizzati.
* Numero o percentuale di dispositivi integrati con un sistema centralizzato di EDR/XDR. Un elevato grado di integrazione con sistemi di rilevamento e risposta agli [endpoint (EDR)](https://www.researchgate.net/publication/383015439_Evolution_of_Endpoint_Detection_and_Response_EDR_in_Cyber_Security_A_Comprehensive_Review) o estesi (XDR) rappresenta un indicatore chiave della capacità di risposta a potenziali minacce.
* Numero di credenziali compromesse o accessi non autorizzati rilevati durante il periodo di osservazione. Questa metrica è essenziale per comprendere la resilienza delle politiche di autenticazione adottate e per identificare possibili punti deboli nel processo di identificazione e autenticazione degli utenti.
* Numero di incidenti informatici registrati nella rete dell’organizzazione, quali compromissione di workstation, attività illecite verso o da dispositivi dell’organizzazione, identificazione di malware o ransomware, violazioni di licenze, condivisione di contenuti protetti da copyright, ecc. Il monitoraggio costante di questi incidenti fornisce una visione chiara dell’efficacia delle misure di sicurezza implementate e delle aree che necessitano di ulteriore attenzione.

## Metriche avanzate per il monitoraggio Zero Trust

Metriche più sofisticate possono riguardare le connessioni al perimetro dell’organizzazione e i sistemi cloud in uso, ad esempio:

* Numero, durata e provenienza delle connessioni VPN per identificare accessi sospetti o anomali. Il monitoraggio delle connessioni VPN può fornire indicazioni critiche sulla presenza di attività sospette, specialmente quando vengono rilevati accessi da località inconsuete o durante orari atipici.
* Numero di documenti condivisi all’esterno dell’organizzazione. Una metrica di questo tipo aiuta a controllare il flusso di informazioni sensibili verso l’esterno, garantendo che la condivisione sia conforme alle politiche di sicurezza e che le informazioni riservate siano adeguatamente protette.
* Numero di vulnerabilità rilevate sui sistemi esposti, sulla base di analisi di vulnerability assessment o penetration testing. Le vulnerabilità presenti rappresentano potenziali punti di ingresso per gli attaccanti, e la loro individuazione tempestiva è fondamentale per ridurre la superficie di attacco dell’organizzazione.
* Percentuale di copertura delle tecniche di attacco identificate da MITRE rispetto ai log raccolti e ai dispositivi di sicurezza adottati. Questa metrica consente di valutare in che misura le difese aziendali siano in grado di affrontare le tecniche di attacco conosciute, fornendo una misura della capacità di resilienza dell’infrastruttura tecnologica.
* Numero di accessi rilevati verso honeypot o sistemi di deception distribuiti all’interno dell’organizzazione. I sistemi di d...