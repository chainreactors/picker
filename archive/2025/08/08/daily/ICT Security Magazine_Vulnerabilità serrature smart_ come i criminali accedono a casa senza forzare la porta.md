---
title: Vulnerabilità serrature smart: come i criminali accedono a casa senza forzare la porta
url: https://www.ictsecuritymagazine.com/notizie/serrature-smart/
source: ICT Security Magazine
date: 2025-08-08
fetch_date: 2025-10-07T00:59:17.083756
---

# Vulnerabilità serrature smart: come i criminali accedono a casa senza forzare la porta

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

![vulnerabilità serrature smart 2024 con statistiche attacchi Bluetooth e raccomandazioni sicurezza domestica cybersecurity](https://www.ictsecuritymagazine.com/wp-content/uploads/freepik__the-style-is-candid-image-photography-with-natural__78198.jpeg)

# Vulnerabilità serrature smart: come i criminali accedono a casa senza forzare la porta

A cura di:[Redazione](#molongui-disabled-link)  Ore 7 Agosto 202517 Luglio 2025

Le serrature smart promettono comodità e sicurezza avanzata, ma ricerche recenti rivelano vulnerabilità critiche che permettono ai criminali di accedere alle abitazioni senza forzare fisicamente le porte. **Nel 2024, oltre 50.000 abitazioni risultano esposte a vulnerabilità critiche con punteggio CVSS 9.1/10**, mentre esperti di cybersecurity documentano metodi di attacco sempre più sofisticati che sfruttano protocolli Bluetooth, firmware vulnerabili e applicazioni mobili compromesse.

L’analisi dei dati del mercato europeo mostra una crescita del 11,9% annuo del settore serrature smart, raggiungendo €4,1 miliardi nel 2023. Parallelamente, gli incidenti di cybersecurity in Italia sono aumentati del 40% nel 2024, evidenziando la necessità urgente di comprendere i rischi associati a questi dispositivi IoT domestici.

## Serrature smart: vulnerabilità critiche scoperte nei principali produttori

#### Il caso Chirp Systems: 50.000 abitazioni a rischio

La vulnerabilità più grave identificata nel 2024 riguarda i sistemi Chirp Systems, con **credenziali hardcoded nel firmware che permettono l’accesso remoto a qualsiasi serratura interessata**. Questa falla, con punteggio CVSS 9.1, affligge circa 50.000 abitazioni e rimane non corretta nonostante tre anni di segnalazioni all’azienda.

Matt Brown, ingegnere di Amazon Web Services che ha scoperto la vulnerabilità, definisce il difetto “ovvio e facile da correggere”, ma critica la mancanza di motivazione delle aziende nell’affrontare i problemi di sicurezza. La CISA (Cybersecurity & Infrastructure Security Agency) ha emesso un’advisory ad alta gravità, avvertendo che “lo sfruttamento di questa vulnerabilità potrebbe permettere a un attaccante di prendere il controllo e ottenere accesso fisico illimitato”.

#### Vulnerabilità del firmware Sceiner: attacchi a distanza ravvicinata

I ricercatori di Aleph Research hanno identificato **multiple vulnerabilità nel firmware Sceiner** (CVE-2023-7003 fino a CVE-2023-7017), che affligge serrature vendute globalmente sotto vari marchi. Queste falle permettono attacchi attraverso prossimità fisica, adiacente o connessione Bluetooth, senza alcuna interazione della vittima.

Le vulnerabilità includono:

* **Chiave AES singola per tutte le comunicazioni**
* **Elaborazione di messaggi in chiaro**
* **Aggiornamenti firmware non autenticati tramite Bluetooth LE**
* **Chiavi AES non univoche per l’accoppiamento serratura-tastiera**

## Vulnerabilità dei principali brand internazionali

**August Smart Locks** presenta falle nell’esposizione delle credenziali WiFi durante la configurazione, con crittografia facilmente violabile. Bitdefender ha scoperto chiavi di crittografia hardcoded nelle app mobili che permettono l’intercettazione delle password WiFi.

**Yale Smart Locks** utilizza microcontrollori DA14680A vulnerabili agli attacchi Sweyntooth Bluetooth, che causano denial of service. I numeri seriali dei dispositivi sono pubblicamente accessibili via Bluetooth, facilitando configurazioni non autorizzate.

**Kwikset Smart Locks** ha mostrato vulnerabilità nell’app Android Halo che permetteva il furto di credenziali tramite app maligne, corretta nella versione 1.2.11 del dicembre 2021.

## Metodi tecnici di attacco utilizzati dai criminali

#### Attacchi Bluetooth: BIAS, KNOB e BRAKTOOTH

I criminali sfruttano **vulnerabilità fondamentali nei protocolli Bluetooth** per compromettere le serrature smart. L’attacco BIAS (Bluetooth Impersonation AttackS) permette di impersonare dispositivi precedentemente accoppiati senza conoscere la chiave di collegamento, risultando completamente non rilevabile dalle vittime.

L’attacco KNOB (Key Negotiation of Bluetooth) forza la riduzione della lunghezza della chiave di crittografia a 1 byte, permettendo attacchi brute force in tempo reale. La famiglia BRAKTOOTH affligge miliardi di dispositivi Bluetooth attraverso exploit di pacchetti malformati.

#### Attacchi replay e intercettazione di segnali

I criminali utilizzano **sniffer Bluetooth** come Ubertooth One per catturare comandi legittimi di sblocco durante la trasmissione. Questi comandi vengono poi riprodotti per sbloccare il dispositivo, richiedendo solo prossimità fisica durante l’uso legittimo.

La ricerca su eLinkSmart Locks dimostra come **token di sessione a 6 byte e password decimali hardcoded** rendano le serrature vulnerabili sia ad attacchi replay che brute force, permettendo bypass completo del controllo accessi nel raggio Bluetooth.

#### Attacchi man-in-the-middle (MITM)

Utilizzando strumenti come **GATTacker MITM proxy**, i criminali intercettano le comunicazioni Bluetooth Low Energy per catturare handshake di autenticazione ed estrarre chiavi di crittografia. L’app TTLock memorizza chiavi virtuali in testo normale, permettendo accesso non autorizzato persistente una volta compromesse le credenzia...