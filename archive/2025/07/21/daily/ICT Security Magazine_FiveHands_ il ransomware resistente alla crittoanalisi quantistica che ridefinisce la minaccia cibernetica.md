---
title: FiveHands: il ransomware resistente alla crittoanalisi quantistica che ridefinisce la minaccia cibernetica
url: https://www.ictsecuritymagazine.com/articoli/fivehands-il-ransomware-quantisticamente-resistente-che-ridefinisce-la-minaccia-cibernetica/
source: ICT Security Magazine
date: 2025-07-21
fetch_date: 2025-10-06T23:24:16.083354
---

# FiveHands: il ransomware resistente alla crittoanalisi quantistica che ridefinisce la minaccia cibernetica

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

![ransomware FiveHands](https://www.ictsecuritymagazine.com/wp-content/uploads/ransomware-FiveHand.jpeg)

# FiveHands: il ransomware resistente alla crittoanalisi quantistica che ridefinisce la minaccia cibernetica

A cura di:[Redazione](#molongui-disabled-link)  Ore 20 Luglio 202520 Luglio 2025

Il ransomware **FiveHands** rappresenta un’evoluzione sofisticata della famiglia DeathRansom, emerso come minaccia critica nel panorama della cybersecurity nel 2021. Operato dal gruppo UNC2447, questo malware implementa tecniche crittografiche avanzate basate su NTRU e tattiche di doppia estorsione, risultando in impatti devastanti per organizzazioni in Europa e Nord America. L’analisi tecnica rivela un’architettura modulare che combina evasione avanzata, persistenza sofisticata e capacità di movimento laterale, rendendo FiveHands uno dei ransomware più pericolosi dell’ecosistema criminale contemporaneo.

Negli ultimi anni, la corsa alla crittografia post-quantistica non è rimasta confinata ai laboratori accademici o agli enti di standardizzazione. Anche l’ecosistema criminale ha iniziato a integrare algoritmi resistenti agli attacchi quantistici nei propri strumenti offensivi, segnando una svolta preoccupante per la cybersecurity. Il ransomware FiveHands è tra i primi esempi documentati di questa tendenza, adottando NTRUEncrypt, un algoritmo lattice-based noto per la sua resistenza agli attacchi da parte di computer quantistici.

Questa scelta non è casuale: rappresenta un chiaro salto di qualità rispetto ai ransomware tradizionali basati su RSA o ECC, vulnerabili all’algoritmo di Shor in scenari futuri dominati dalla tecnologia quantistica. [L’uso di crittografia quantisticamente resistente](https://www.ictsecuritymagazine.com/articoli/elaboratori-quantistici-e-crittografia-post-quantum-oggi/) consente agli attori minacciosi non solo di rafforzare l’efficacia dei loro attacchi, ma anche di aumentare la longevità dei dati cifrati, rendendone la decrittazione ancora più complessa e potenzialmente impossibile, anche nel lungo periodo.

FiveHands dimostra così come l’evoluzione della minaccia ransomware stia già anticipando gli sviluppi tecnologici futuri, spingendo verso una nuova fase di cyber warfare in cui le organizzazioni devono prepararsi a difendersi non solo dalle minacce attuali, ma anche da quelle post-quantistiche.

## **Architettura tecnica e implementazione del malware**

FiveHands rappresenta una riscrittura completa di DeathRansom in C++, abbandonando l’implementazione originale in C per ottenere prestazioni superiori e capacità avanzate di gestione dei thread. **Il dropper memory-only ServeManager.exe richiede un parametro chiave a 16 caratteri** per decrittare e eseguire il payload direttamente in memoria, evitando la scrittura su disco e complicando l’analisi forense.

L’architettura del malware utilizza **IoCompletionPorts** invece del tradizionale QueueUserWorkItem, permettendo una gestione efficiente dei thread di crittografia e migliorando significativamente le prestazioni durante l’operazione di cifratura. Il payload embedded è protetto con crittografia AES-128 utilizzando l’IV hardcoded “85471kayecaxaubv”, mentre l’**imphash comune 8517cf209c905e801241690648f36a97** facilita l’identificazione tra campioni diversi.

La validazione dell’header PE e l’integrazione con Windows Restart Manager rappresentano caratteristiche uniche che distinguono FiveHands dai suoi predecessori. Il malware implementa controlli di integrità per verificare la struttura PE prima dell’esecuzione del payload, mentre l’utilizzo del Restart Manager consente la chiusura forzata dei file in uso per garantire una crittografia completa.

## **Schema crittografico avanzato e protezione dei dati**

FiveHands implementa un **sistema crittografico ibrido** che combina la crittografia lattice-based NTRU con AES-128 per ottenere un livello di sicurezza quantisticamente resistente. L’algoritmo **NTRUEncrypt** rappresenta un’alternativa avanzata a RSA/ECC, basato sul problema del vettore più corto nei reticoli matematici e resistente agli attacchi quantistici.

Il processo di crittografia segue una metodologia rigorosa:

1. **Generazione della chiave AES univoca** (16 byte casuali) per ogni file;
2. **Crittografia del contenuto** con AES-128;
3. **Protezione della chiave** tramite crittografia NTRU della chiave AES, dimensione file originale e magic value (DE C0 AD BA);
4. **Appendimento dei metadati crittografati** al file cifrato;
5. **Aggiunta del marker finale** (DB DC CC AB) per prevenire la ri-crittografia;
6. **Modifica dell’estensione** in.crypt.

La generazione dell’identificativo vittima utilizza un **hash SHA-512 della chiave pubblica NTRU**, con i primi 32 byte utilizzati come identificatore unico. Questo approccio garantisce la correlazione tra vittima e chiave di decrittazione mantenendo l’anonimato operativo.

## **Vettori di attacco e tattiche del threat actor UNC2447**

L’attore della minaccia UNC2447 dimostra capacità tecniche avanzate attraverso lo **sfruttamento di CVE-2021-20016**, una vulnerabilità di SQL injection critica negli appliance VPN SonicWall SMA 100. Questa tecnica di accesso iniziale consente l’estrazione remota non autenticata di credenziali e informazioni di sessione, fornendo un ...