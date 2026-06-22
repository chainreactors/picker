---
title: DNS security: il livello che tutti usano e quasi nessuno difende
url: https://www.ictsecuritymagazine.com/cyber-security/dns-security/
source: ICT Security Magazine
date: 2026-06-21
fetch_date: 2026-06-22T07:16:58.669412
---

# DNS security: il livello che tutti usano e quasi nessuno difende

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

![DNS security](https://www.ictsecuritymagazine.com/wp-content/uploads/DNS-security.png)

# DNS security: il livello che tutti usano e quasi nessuno difende

A cura di:[Redazione](#molongui-disabled-link)  Ore 21 Giugno 20269 Giugno 2026

DNS security è la difesa del servizio più usato e meno sorvegliato di Internet. Il *Domain Name System* è l’elenco telefonico della rete: traduce i nomi che digitiamo negli indirizzi numerici a cui i dispositivi si collegano, ed è il primo passo di quasi ogni connessione, lecita o malevola che sia. Proprio per questo è ovunque, è permesso attraversare i firewall senza troppe domande e quasi nessuno lo ispeziona davvero. È la combinazione perfetta per un attaccante: un canale universale, fidato e non controllato.

Il paradosso che governa il tema è semplice. Lo stesso DNS che rende possibile il funzionamento di tutto è anche uno dei vettori più sfruttati e meno presidiati. Per anni è stato trattato come un’utenza tecnica da far funzionare e poi dimenticare, non come una superficie d’attacco né, soprattutto, come il punto di controllo che potrebbe essere. La DNS security parte dal ribaltare questa abitudine: riconoscere che il livello attraversato da ogni richiesta è insieme il bersaglio più comodo e la leva difensiva più ampia a disposizione.

## Un canale fidato è un canale abusabile

La ragione per cui il DNS è tanto attraente per chi attacca è la stessa per cui è utile a tutti: passa dappertutto. Il caso più insidioso è il *DNS tunneling*, la tecnica con cui si nascondono dati dentro le query: comandi per controllare un sistema compromesso, oppure informazioni rubate, vengono codificati nei nomi richiesti e fatti uscire attraverso un canale che i firewall lasciano transitare e che pochi monitorano. È così che il DNS diventa una via di esfiltrazione e un canale di comando e controllo, sfruttato da strumenti e malware documentati come Dnscat2, iodine o DNSMessenger.

Non è l’unico fronte. Con l’avvelenamento della cache, un attaccante corrompe i record memorizzati da un resolver e lo costringe a restituire l’indirizzo sbagliato per un dominio, dirottando gli utenti verso destinazioni fraudolente. Con il dirottamento del dominio, prende il controllo del nome stesso, spesso rubando le credenziali presso il registrar o sfruttandone una vulnerabilità, e da lì reindirizza il traffico legittimo dove vuole. Il filo comune è che nessuno di questi attacchi forza una porta: tutti abusano della fiducia che l’intera rete ripone, per impostazione predefinita, nelle risposte del DNS.

## Protective DNS: trasformare il problema in un controllo

La svolta concettuale è capire che lo stesso punto di passaggio obbligato può diventare un presidio. Se ogni connessione comincia con una risoluzione di nome, allora intercettare quella risoluzione significa poter bloccare la minaccia prima ancora che la connessione avvenga. È l’idea del *protective DNS*: un resolver che confronta ogni richiesta con l’intelligence sui domini malevoli noti e rifiuta di risolvere quelli pericolosi, neutralizzando sul nascere campagne di *ransomware*, *phishing*, *botnet* e *malware*.

La guida di NSA e CISA sulla [scelta di un protective DNS](https://media.defense.gov/2025/Mar/24/2003675043/-1/-1/0/CSI-Selecting-a-Protective-DNS-Service-v1.3.PDF), nella sua versione 1.4 dell’aprile 2025, descrive bene il vantaggio pratico: l’adozione può essere semplicissima, perché spesso basta puntare il resolver dell’organizzazione verso il servizio protettivo. Ma avverte anche del punto debole, l’aggiramento. Un *malware* che usa un proprio resolver scavalca la protezione, e per questo le stesse linee guida raccomandano di bloccare il traffico DNS in uscita non autorizzato, sulle porte usate dal protocollo, e di impedire l’uso di server DNS cifrati non controllati. La logica è chiara: il *protective DNS* funziona solo se tutto il traffico di risoluzione passa davvero da lì, e questo richiede di chiuderne le vie di fuga con un’adeguata [segmentazione e controllo della rete](https://www.ictsecuritymagazine.com/articoli/network-segmentation/). Resta un limite strutturale, indicato dalla guida stessa: chi si collega direttamente a un indirizzo IP, senza chiedere alcun nome, non passa dal checkpoint e non viene filtrato. Il *protective DNS* copre ciò che si risolve, non ciò che salta del tutto la risoluzione.

## DNS security non è una sola cosa: DNSSEC e DNS cifrato

Qui si annida una confusione diffusa, perché sotto l’etichetta della DNS security convivono tecnologie che risolvono problemi diversi e che molti scambiano l’una per l’altra. Il DNSSEC, le estensioni di sicurezza del DNS, aggiunge firme crittografiche alle risposte per garantirne l’autenticità e l’integrità: serve a sapere che la risposta ricevuta è genuina e non manomessa. Non nasconde nulla, protegge l’esattezza, non la riservatezza. La sua adozione resta peraltro disomogenea, frenata dalla complessità della catena di validazione e da apparati intermedi che vi interferiscono.

Il DNS cifrato, nelle sue forme su HTTPS e su TLS, risponde invece a una domanda opposta: impedire che qualcuno osservi quali nomi si stanno richiedendo. Protegge la riservatezza dell...