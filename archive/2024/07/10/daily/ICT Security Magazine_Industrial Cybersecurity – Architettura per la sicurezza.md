---
title: Industrial Cybersecurity – Architettura per la sicurezza
url: https://www.ictsecuritymagazine.com/articoli/industrial-cybersecurity-architettura-per-la-sicurezza/
source: ICT Security Magazine
date: 2024-07-10
fetch_date: 2025-10-06T17:46:10.525981
---

# Industrial Cybersecurity – Architettura per la sicurezza

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

![Industrial Cybersecurity dei Cyber-Physical Systems (CPS) sicurezza](https://www.ictsecuritymagazine.com/wp-content/uploads/Industrial-Cybersecurity-Architettura-per-la-sicurezza.jpg)

# Industrial Cybersecurity – Architettura per la sicurezza

A cura di:[Luca Durante](#molongui-disabled-link)  Ore 9 Luglio 202426 Settembre 2025

*Industrial Cybersecurity è oggi un pilastro fondamentale per la protezione dei Cyber-Physical Systems (CPS) che governano infrastrutture critiche e processi industriali. Dalla produzione energetica alla manifattura, dai trasporti all’automazione, la sicurezza di questi ecosistemi complessi dipende dalla capacità di integrare monitoring, detection e reaction in un’unica strategia coordinata.*

*Attraverso sensori distribuiti, modelli di analisi e riconfigurazioni dinamiche, è possibile individuare in tempo reale anomalie, verificare l’applicazione delle policy di sicurezza e adottare contromisure efficaci. L’obiettivo non è soltanto garantire la resilienza contro attacchi informatici o malfunzionamenti, ma anche mantenere elevate le prestazioni operative, evitando che i meccanismi di difesa rallentino i processi industriali.*

*In questo scenario, l’Industrial Cybersecurity rappresenta la chiave per coniugare protezione e produttività, trasformando la sicurezza da costo a fattore abilitante per l’innovazione e la continuità dei sistemi industriali.*

## Industrial Cybersecurity: modelli, verifiche e riconfigurazione automatica nei Cyber-Physical Systems (CPS)

Il monitoring prevede l’acquisizione di informazioni dal/nel target system circa il suo stato e il suo funzionamento.

Tali informazioni, in formato grezzo e/o preventivamente elaborato e/o aggregato, vengono rese disponibili all’attività di detection che, in caso di errore, criticità o anomalia, coinvolge l’attività di reaction per l’attuazione delle necessarie contromisure, il tutto sotto la supervisione di personale dedicato.

![Industrial Cybersecurity: Architettura concettuale di un Cyber-Physical Systems (CPS) sicuro](https://www.ictsecuritymagazine.com/wp-content/uploads/durante9-700x281.png)

Figura 9: Architettura concettuale di un CPS sicuro

Si noti che lo schema di Figura 9 si riferisce ad attività che possono essere svolte sia totalmente dentro al sistema in esecuzione, ad esempio quanto legato ad attacchi di tipo DoS (Denial of Service) sia, parzialmente, all’esterno, come la verifica di corretta implementazione di policy di sicurezza quando (un caso tipico sono gli Industrial Control Systems) non siano disponibili meccanismi automatici (enforcement) di applicazione delle policy stesse.

In tal caso, a fronte di una descrizione dettagliata del sistema, comprensiva dei meccanismi di sicurezza, fornita possibilmente in modo (semi) automatico dal monitoring, si costruisce un modello del sistema stesso, su cui si verifica, tramite opportune tecniche di analisi, che le policy di sicurezza previste per il sistema siano soddisfatte dalla sua implementazione: ad esempio verificando che chi esercita il ruolo di “operatore” su di una certa macchina non possa modificarne i “parametri di configurazione” e che a farlo possa essere soltanto il “responsabile della produzione”. Per fare ciò, occorre verificare che l’assegnazione delle credenziali agli utenti dei singoli dispositivi e la loro configurazione consenta appunto di garantire tali desiderata.

Nel caso in cui la verifica fallisca, le necessarie correzioni vengono apportate sul modello del sistema e, in caso di successiva verifica positiva, ribaltate sul sistema reale.

Per ciò che concerne le attività di monitoring, detection e reaction effettuate sul sistema reale, sono evidentemente necessari sensori o sonde di acquisizione, risorse di computazione e comunicazione e quanto altro necessario alla riconfigurazione, quindi componenti hardware e software che devono trovarsi distribuiti nel sistema stesso per assolvere alle suddette funzioni.

Questa sovrastruttura per la sicurezza dev’essere progettata indissolubilmente dal sistema nel caso di nuovi CPS, oppure aggiunta in caso di CPS esistenti, privi o non sufficientemente dotati di risorse per la sicurezza.

![Industrial Cybersecurity - Analisi di sicurezza dei Cyber-Physical Systems (CPS)](https://www.ictsecuritymagazine.com/wp-content/uploads/durante10-700x680.png)

Figura 10: Analisi di sicurezza

### Esempi

Esempi di quanto sopra descritto possono provenire da recenti attività di ricerca nel settore. In particolare,
 verranno introdotti:

* strumenti di analisi che operano su modelli di sistema, costruiti mediante informazioni acquisite dall’attività
   di monitoring sul sistema in esecuzione;
* strumenti di riconfigurazione automatica dell’infrastruttura di sicurezza a seguito di intervenute situazioni di
   rischio, causate da azioni malevole o semplicemente da impreviste situazioni fisiologiche;
* analisi delle prestazioni di software e dispositivi per la sicurezza, al fine di garantire che la loro introduzione
   non influisca negativamente sulle prestazioni del sistema.

### Analisi

Lo schema di Figura 10 illustra il modo di operare delle metodologie di analisi di sicurezza su modelli del sistema, eventualmente acquisiti dal sistema stesso mediante il supporto del monitoring. In sostanza,...