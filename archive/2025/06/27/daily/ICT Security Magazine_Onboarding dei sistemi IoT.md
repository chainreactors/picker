---
title: Onboarding dei sistemi IoT
url: https://www.ictsecuritymagazine.com/articoli/onboarding-iot/
source: ICT Security Magazine
date: 2025-06-27
fetch_date: 2025-10-06T23:03:53.413762
---

# Onboarding dei sistemi IoT

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

![Processo di onboarding IoT con cybersecurity: schema di autenticazione e sicurezza dispositivi tramite PKI, VPN e certificati digitali per sistemi di gestione centralizzata](https://www.ictsecuritymagazine.com/wp-content/uploads/untitled-design-4_5ripVOFx.png)

# Onboarding dei sistemi IoT

A cura di:[Fabrizio Giorgione e Giovanni Cappabianca](#molongui-disabled-link)  Ore 26 Giugno 202516 Luglio 2025

In questo primo articolo di una serie dedicata all’onboarding dei sistemi IoT, esploreremo le fondamenta della sicurezza nella gestione dei dispositivi connessi. Dal momento in cui l’Internet of Things ha superato il numero di esseri umani sul pianeta, la necessità di processi sicuri per l’identificazione e l’autenticazione dei dispositivi è diventata cruciale. Attraverso un’analogia con i controlli aeroportuali, analizzeremo i protocolli e le infrastrutture di sicurezza necessarie per garantire un onboarding affidabile, concentrandoci su VPN, certificati digitali e PKI in un’architettura IoT centralizzata.

L’internet of things (IoT) è stato concepito tra il 2008 e il 2009, quando il numero di dispositivi connessi ha superato quello degli esseri umani sul pianeta. Questi dispositivi possono supportare applicazioni progettate per risolvere problemi reali nel mondo della salute, della sicurezza, dell’energia, dei trasporti e di altri settori attraverso il monitoraggio, l’allerta e la consapevolezza dei dati e degli indici di processo.

## Stack Tecnologico e Competenze IoT

Dietro il mondo IoT è richiesto un insieme di competenze che variano dalla conoscenza di programmazione embedded, di protocolli e reti distribuite, di architetture di sistemi su campo ed in cloud sino alle competenze nella cybersecurity.
 Una rete di dispositivi è IoT quando la comunicazione avviene su rete internet.

Anche negli impianti industriali sono presenti dispositivi in grado di comunicare tra loro su stack TCP/IP o usando altri protocolli di trasporto e di rete alla base di internet, ma se la comunicazione resta dentro l’impianto o in una rete privata, in quel caso si parla di rete OT (Operational technology). Questa infrastruttura è adottata nei sistemi di controllo industriale e di produzione critici per un’organizzazione. Per ragioni di sicurezza viene mantenuta segregata dalla rete internet per cui è fuori dal perimetro di questo articolo.

Rendere disponibili dati e dispositivi su rete pubblica internet presenta delle sfide. Ricordiamoci che il protocollo di rete offre un livello di servizio best effort. Sta ai protocolli a livello di trasporto e applicativi garantire l’affidabilità nella comunicazione.

Data l’eterogeneità dei dispositivi, con differenti capacità computazionali, e dei protocolli disponibili a livello applicativo, è necessario stabilire dei ruoli e delle regole con cui controllare e monitorare tutti gli host in gioco. I dispositivi possono essere gestiti:

* in maniera distribuita, con logiche di controllo locali su campo che periodicamente si allineano alle indicazioni presenti in una piattaforma di coordinamento.
* in maniera decentralizzata, con sistemi di gestione separati con in carico diversi sottoinsiemi di dispositivi
* in maniera centralizzata, con un’unica piattaforma che assume il pieno controllo della flotta.

## Il Processo di Onboarding IoT: Sicurezza e Autenticazione

L’Onboarding è un processo con cui il dispositivo viene identificato ed accolto per la prima volta nella piattaforma che lo gestirà. è la prima fase del ciclo di vita di un dispositivo e determina se sarà o meno sotto il nostro controllo. Uno dei problemi da risolvere in questa fase è: come facciamo a capire se il dispositivo che tenta di entrare in contatto con noi è legittimo?

Pensiamo allo screening svolto in un aeroporto. Dal momento in cui ci presentiamo al check- in, il documento su cui facciamo affidamento per indicare alle autorità chi siamo è la nostra carta d’identità o il nostro passaporto per paesi extra UE. L’identificazione non basta. Come facciamo a comprendere se siamo anche autorizzati a raggiungere la nostra destinazione? Come cittadini dell’Unione Europea, siamo autorizzati a muoverci da un Paese ad un altro.
 Immaginiamo però di dover andare negli Stati Uniti.

Nella data di realizzazione di questo articolo la condizione propedeutica per poter accedere è quella di completare la compilazione del modulo del visto elettronico online (ESTA). Allo stesso modo, il dispositivo deve fornire un insieme di informazioni che identificano la natura della richiesta di comunicazione ed il motivo per cui sta contattando la piattaforma.

All’aeroporto ci sottoponiamo ad un processo rigoroso di controllo, partendo dalla scansione del nostro volto con quello presente sul passaporto per verificarne la coincidenza, fino al controllo degli oggetti che portiamo con noi nel nostro bagaglio a mano. La cyber security entra in gioco in questo processo proprio per accertare che il dispositivo sia legittimo e che non ci siano azioni fraudolente ai danni del servizio offerto dalla piattaforma e degli altri dispositivi.

In questo articolo ci metteremo nei panni dei proprietari dell’ “aeroporto” dei dispositivi iot, considerando un sistema di gestione centralizzato. Valuteremo quali sono i mezzi e gli strumenti usati nel...