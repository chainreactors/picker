---
title: Zero Trust Onboarding
url: https://www.ictsecuritymagazine.com/articoli/zero-trust-onboarding/
source: ICT Security Magazine
date: 2025-07-16
fetch_date: 2025-10-06T23:56:29.126113
---

# Zero Trust Onboarding

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

![Architettura Zero Trust per l'onboarding IoT: diagramma di micro-segmentazione, SDP e sistemi di protezione continua per dispositivi connessi](https://www.ictsecuritymagazine.com/wp-content/uploads/untitled-design-7_C4n4jEa9.png)

# Zero Trust Onboarding

A cura di:[Fabrizio Giorgione e Giovanni Cappabianca](#molongui-disabled-link)  Ore 15 Luglio 202516 Luglio 2025

Questo approfondimento conclude la [serie](https://www.ictsecuritymagazine.com/articoli/hardware-onboarding/) dedicata all’onboarding dei dispositivi IoT, con un focus specifico sullo zero trust onboarding e la sua implementazione pratica. L’articolo esplora le strategie di verifica continua dell’identità, la micro-segmentazione delle reti, l’implementazione del Software-defined Perimeter (SDP) e le tecniche di protezione contro minacce zero-day. Viene presentata una visione completa delle moderne architetture di sicurezza IoT basate sullo zero trust onboarding, con particolare attenzione ai sistemi di monitoraggio continuo e alla gestione delle minacce emergenti.

## Verifica Continua e Policy Enforcement nell’IoT Zero Trust

La verifica continua dell’identità dei dispositivi avviene tramite Il “Policy Enforcement Point” (PEP) si riferisce a un componente di sicurezza che applica le politiche di accesso e sicurezza in un sistema. Il PEP è responsabile della decisione di consentire o negare l’accesso a risorse specifiche in base alle politiche definite.

### Micro-segmentazione durante onboarding

Un’impresa può scegliere di implementare un’architettura Zero Trust (ZTA) basata sul posizionamento di singole risorse o gruppi di risorse su un segmento di rete unico protetto da un componente di sicurezza del gateway. In questo approccio, l’impresa posiziona dispositivi infrastrutturali come switch intelligenti (o router) o next generation firewall (NGFW) o dispositivi gateway di scopo speciale per fungere da PEP (Policy Enforcement Point) che proteggono ciascuna risorsa o piccolo gruppo di risorse.

In alternativa (o in aggiunta), l’impresa può scegliere di implementare la micro-segmentazione basata su host utilizzando agenti software o firewall sugli asset endpoint. Questi dispositivi gateway concedono dinamicamente l’accesso a singole richieste da un client, asset o servizio. A seconda del modello, il gateway può essere l’unico componente PEP o parte di un PEP multipart composto dal gateway e da un agente lato client.

Ogni risorsa sarà quindi protetta da un firewall dedicato e il traffico in ingresso e uscita monitorato da appositi strumenti quali IDS/IPS e relativi EDD/XDR sulle relative macchine. Questa difesa a strati con richieste d’accesso controllato e continuo monitoraggio consentono un elevato livello di sicurezza delle risorse. Inoltre qualora la macchina in essere risulti compromessa sarà sufficiente isolare solo una specifica area garantendo la continuità degli altri processi, laddove possibile.

Il **Software-defined perimeter (SDP)**, o **“Black Cloud”**, è un framework di sicurezza **“identity-centric”** sviluppato dalla **Cloud Security Alliance (CSA**) che controlla l’accesso alle risorse in base all’identità. L’SDP consente alle organizzazioni di implementare un accesso sicuro personalizzato ai sistemi di rete e di limitare l’accesso agli utenti autorizzati. Il modello “need-to-know” garantisce che ogni dispositivo e utente siano verificati prima di consentire l’accesso alla risorsa.

**L’SDP riduce la superficie di attacco a zero** creando una connessione di rete personalizzata, micro-segmentata e uno-a-uno tra l’utente e le risorse a cui accede. Pertanto, questo sistema supera tutti gli svantaggi del tradizionale controllo degli accessi alla rete in modo efficace.

L’SDP implementa un modello di zero-trust, che si basa sul principio **“Never trust, always verify”.** Qualsiasi dispositivo che desideri entrare a far parte della rete dovrà essere verificato e approvato dagli amministratori della rete. Nessun dispositivo non autorizzato potrà dunque accedere alla rete, previa autorizzazione. In tale approccio inoltre ogni utente/dispositivo avrà solo e soltanto le autorizzazioni di cui ha bisogno per effettuare i propri compiti.

Dunque qualora tentasse di accedere ad un’area non consentita dovrà procedere con un iter preposto. Tendenzialmente queste autorizzazione sono a termine, ovvero, solo per il tempo necessario ad eseguire l’attività richiesta. L’SDP funziona da firewall logico, adattando in modo dinamico l’accesso alla rete secondo le politiche stabilite.

Come firewall dinamico, l’SDP segue un’unica regola: negare l’accesso a tutte le connessioni, consentendo l’accesso esclusivamente agli utenti e ai dispositivi autorizzati per interagire con host e/o servizi specifici, in conformità con le politiche.

## Architettura SDP e Componenti per Zero Trust IoT

L’architettura dell’SDP ha tre componenti principali:

* **Client (initiating host):** eseguito su ogni dispositivo dell’utente. Il client comunica con il controller per stabilire una connessione con il gateway. Prima di concedere il permesso, il controller può richiedere ulteriori informazioni sull’hardware e/o software.
* **Controller:** è un punto di autenticazione che valuta la politica per concedere o negare l’accesso all’utente. ...