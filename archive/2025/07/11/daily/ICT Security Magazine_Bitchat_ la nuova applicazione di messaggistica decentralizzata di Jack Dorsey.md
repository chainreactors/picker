---
title: Bitchat: la nuova applicazione di messaggistica decentralizzata di Jack Dorsey
url: https://www.ictsecuritymagazine.com/articoli/bitchat-jack-dorsey/
source: ICT Security Magazine
date: 2025-07-11
fetch_date: 2025-10-06T23:28:57.823126
---

# Bitchat: la nuova applicazione di messaggistica decentralizzata di Jack Dorsey

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

![Bitchat: la nuova applicazione di messaggistica decentralizzata di Jack Dorsey](https://www.ictsecuritymagazine.com/wp-content/uploads/Bitchat.jpeg)

# Bitchat: la nuova applicazione di messaggistica decentralizzata di Jack Dorsey

A cura di:[Redazione](#molongui-disabled-link)  Ore 10 Luglio 202510 Luglio 2025

Il presente articolo fornisce un’analisi tecnica approfondita di Bitchat, la nuova applicazione di messaggistica decentralizzata di Jack Dorsey, concentrandosi sulla sua architettura, sui meccanismi di protezione della privacy e sulle implicazioni per la cybersecurity. Vengono esaminati i principi operativi delle reti mesh Bluetooth Low Energy (BLE), i protocolli crittografici implementati e le funzionalità avanzate per la tutela della riservatezza.

Verranno discusse le vulnerabilità intrinseche delle tecnologie sottostanti, con particolare riferimento alle reti mesh BLE e ai protocolli di messaggistica decentralizzata come Nostr. Vengono inoltre analizzati i rischi associati al modello “store-and-forward” e i vettori di attacco generici nelle infrastrutture decentralizzate. Il rapporto si conclude con raccomandazioni per mitigare i rischi e prospettive future per la ricerca e lo sviluppo nel campo delle comunicazioni resilienti e private.

## **1. Il contesto delle comunicazioni decentralizzate e la visione di Jack Dorsey**

#### **1.1. L’evoluzione delle comunicazioni digitali e la crescente domanda di privacy e resilienza**

Le piattaforme di comunicazione digitali contemporanee, in gran parte basate su architetture centralizzate, sono sempre più percepite come intrinsecamente vulnerabili a problematiche quali la censura, la sorveglianza di massa e la presenza di punti singoli di fallimento. Questa configurazione, sebbene efficiente per la distribuzione su larga scala, espone gli utenti e i loro dati a rischi sistemici. La storia recente è costellata di episodi in cui la censura governativa, le interruzioni di servizio dovute a guasti infrastrutturali o attacchi informatici, e le violazioni della privacy attraverso la raccolta e l’analisi dei dati utente da parte di entità centralizzate, hanno eroso la fiducia pubblica.

La pervasività delle comunicazioni digitali ha reso evidente come i sistemi centralizzati siano suscettibili a forme di controllo e manipolazione. Tale consapevolezza ha generato una chiara e crescente domanda di soluzioni alternative che possano operare al di fuori di tali vincoli. Questa esigenza si manifesta nella ricerca e nello sviluppo di paradigmi decentralizzati, che promettono maggiore autonomia per l’utente, controllo sui propri dati e una resistenza intrinseca alla censura.

Bitchat si inserisce direttamente in questa tendenza, offrendo una risposta tecnologica alle preoccupazioni sistemiche sulla libertà di comunicazione e sulla resilienza delle infrastrutture. La sua concezione riflette un cambiamento ideologico e pratico nel panorama della comunicazione digitale, mirando a fornire un’alternativa in contesti dove la connettività tradizionale è compromessa o inaffidabile.

#### **1.2. Jack Dorsey e il movimento cypherpunk: radici ideologiche e precedenti (Nostr, Bitcoin)**

Jack Dorsey, co-fondatore di Twitter ed ex CEO di Block (precedentemente Square), è una figura prominente e un convinto sostenitore del movimento cypherpunk. Questo movimento promuove l’utilizzo estensivo della crittografia come strumento fondamentale per la tutela della privacy individuale e la promozione della libertà in un’era digitale sempre più sorvegliata. Il suo impegno ideologico si è concretizzato in un sostegno vocale e attivo per Bitcoin, di cui ha promosso l’adozione e lo sviluppo tramite la sua azienda Block.

Il percorso di Dorsey, dalla co-fondazione di una piattaforma centralizzata come Twitter alla sua successiva transizione verso il sostegno di tecnologie decentralizzate come Bluesky e Nostr, dimostra una profonda evoluzione nella sua visione del futuro digitale. Bitchat, che Dorsey ha descritto come un “progetto del fine settimana” nato dall’esplorazione di concetti quali le reti mesh Bluetooth, i relè e i modelli di crittografia, si configura come un’estensione coerente di questa visione.

Non è una semplice innovazione tecnica isolata, ma l’ultimo tassello di un’agenda più ampia volta a costruire un’infrastruttura digitale più libera e resiliente. Questo background conferisce a Bitchat un’aura di credibilità in termini di intenti di privacy e resistenza alla censura, ma lo lega anche intrinsecamente alle sfide filosofiche e tecniche che affliggono l’intero ecosistema decentralizzato, come la sostenibilità dei relè (nel caso di Nostr) o la scalabilità delle soluzioni.

#### **1.3. Bitchat: una nuova frontiera nella messaggistica offline e resistente alla censura**

Bitchat si presenta come un’applicazione di messaggistica decentralizzata peer-to-peer che opera in modo innovativo tramite reti mesh Bluetooth Low Energy (BLE), eliminando la dipendenza dall’infrastruttura internet tradizionale. Questa caratteristica la distingue nettamente dalla maggior parte delle applicazioni di messaggistica, anche quelle che si definiscono decentralizzate, le quali spesso si affidano comunque a una qualche forma di connettività IP.

L’applicazione è progettata con l’obiettiv...