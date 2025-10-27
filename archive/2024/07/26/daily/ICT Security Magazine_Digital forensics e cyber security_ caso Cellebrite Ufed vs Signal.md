---
title: Digital forensics e cyber security: caso Cellebrite Ufed vs Signal
url: https://www.ictsecuritymagazine.com/articoli/digital-forensics-e-cyber-security-caso-cellebrite-ufed-vs-signal/
source: ICT Security Magazine
date: 2024-07-26
fetch_date: 2025-10-06T17:44:34.655973
---

# Digital forensics e cyber security: caso Cellebrite Ufed vs Signal

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

![Digital forensics e cyber security: caso Cellebrite Ufed vs Signal](https://www.ictsecuritymagazine.com/wp-content/uploads/Cellebrite-Ufed-vs-Signal.jpg)

# Digital forensics e cyber security: caso Cellebrite Ufed vs Signal

A cura di:[Francesco Lazzini](#molongui-disabled-link)  Ore 25 Luglio 20247 Gennaio 2025

Dal punto di vista tecnico-operativo, le indagini di *digital forensics* vengono svolte utilizzando specifici strumenti *hardware* e *software*[[1]](#_ftn1) che, una volta collegati al sistema informatico da acquisire, ne esplorano le aree di memoria e ne producono una copia[[2]](#_ftn2) – nella quale vengono ricompresi lo spazio non allocato e le parti di file cancellati ma non definitivamente eliminati – che successivamente viene esfiltrata verso un *file* di *backup* appositamente creato sul dispositivo *hardware* usato per l’acquisizione e dove viene, quindi, dislocata la copia forense del sistema sotto indagine.

Concluse le operazioni di acquisizione, il clone informatico viene poi analizzato mediante programmi di analisi che permettono di prendere visione del contenuto digitale in esame. In particolare, questi *software* hanno il compito di scandagliare a fondo tutti i singoli file che sono presenti nella copia forense, visionandone tutte le parti, metadati inclusi, verificando che non vi siano contenuti occultati e nel caso procedendo ad analisi dei medesimi[[3]](#_ftn3).

È ovvio che più il programma di analisi è moderno e aggiornato più sarà in grado di scovare file nascosti e di conseguenza maggiore sarà la resa in termini di risultato finale.

Qualora, invece, i file siano protetti da *password*, occorrerà procedere allo sblocco del loro contenuto mediante attacchi *brute force* volti all’individuazione della chiave che custodisce i dati[[4]](#_ftn4).

## Digital forensics e *digital evidence*

In estrema sintesi e senza tecnicismi, l’attività di individuazione della *digital evidence* è suddivisibile in due fasi: la prima è quella di acquisizione in copia forense della memoria del dispositivo, mentre la seconda prevede l’analisi della copia estratta, fase nella quale, più precisamente, vengono rintracciate e identificate le evidenze digitali stoccate in memoria che si sospettavano poter essere presenti sul dispositivo al momento del sequestro.

Per entrambe le fasi, in situazioni particolari, possono profilarsi problemi di sicurezza informatica. Durante tali momenti, ad esempio, delle criticità potrebbero insorgere qualora il dispositivo da acquisire e analizzare sia infetto da un virus informatico. Clonando la memoria inevitabilmente verrebbe clonato anche il programma malevolo, che per conseguenza si estenderebbe alla copia forense.

Ora, se l’infezione sul dispositivo originario fosse nota, il problema in realtà non si porrebbe. In tal caso, infatti, l’ostacolo potrebbe essere facilmente aggirato acquisendo più copie del dispositivo e quindi procedendo alla disinfezione del virus da una di esse, per poi confrontarla con le altre per valutare se l’operazione di eliminazione del *malware* abbia comportato la compromissione di dati oppure abbia mantenuto inalterate le informazioni[[5]](#_ftn5).

Il problema emerge quando il virus informatico passa inosservato all’occhio dei *software* adoperati per le operazioni forensi. Si consideri sul punto che, al pari degli altri programmi informatici, anche gli strumenti adoperati per la *digital forensics* possono avere delle vulnerabilità nella sicurezza, soprattutto quando il sistema non viene regolarmente aggiornato. In linea teorica, pertanto, potrebbe capitare che un *malware* sfugga al controllo e continui a svolgere indisturbato il compito per il quale è stato progettato.

In particolare, esistono alcuni tipi di *malware* che una volta sottoposti all’azione dei programmi di analisi sono in grado di corromperne l’algoritmo e alterarne il funzionamento per far commettere al *software* operazioni per le quali originariamente non era settato o che non era stato autorizzato a svolgere. È superfluo specificare che in simili evenienze l’attendibilità delle risultanze ottenute con l’analisi forense sarebbe del tutto assente.

Ad ogni modo, vulnerabilità di questo tipo non colpirebbero la genuinità del procedimento di formazione della copia forense, ma esclusivamente il successivo passaggio di analisi, compromettendo quindi non l’acquisizione in sé (consistente in una mera copiatura dei *byte* della memoria originale senza attività di elaborazione) ma solo i sistemi di analisi e in conseguenza l’analisi che ne scaturisce[[6]](#_ftn6).

#### Digital forensics e cybersicurezza: caso Cellebrite Ufed vs Signal

Un recente caso di cronaca, andato alla ribalta delle testate giornalistiche che si occupano di cybersicurezza, ha messo in chiaro come quanto appena descritto non sia solo un’ipotesi di scuola, bensì potrebbe realmente accadere, o meglio, sarebbe già accaduto. Il caso riguarda lo scambio di battute avutosi tra fine 2020 e prima metà del 2021 tra la nota app di messaggistica Signal e l’azienda israeliana produttrice di strumenti di informatica forense – tra le più affermate sul mercato – Cellebrite Ufed.

La disputa aveva origine allorché l’azienda israeliana comunicava pubblicamente di aver trovato il modo per violare le di...