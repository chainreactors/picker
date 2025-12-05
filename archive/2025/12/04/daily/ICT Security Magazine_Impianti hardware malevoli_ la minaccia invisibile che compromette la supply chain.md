---
title: Impianti hardware malevoli: la minaccia invisibile che compromette la supply chain
url: https://www.ictsecuritymagazine.com/articoli/impianti-hardware-malevoli/
source: ICT Security Magazine
date: 2025-12-04
fetch_date: 2025-12-05T03:19:01.065318
---

# Impianti hardware malevoli: la minaccia invisibile che compromette la supply chain

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

![](https://www.ictsecuritymagazine.com/wp-content/uploads/untitled-design-3_NTndC0xY.png)

# Impianti hardware malevoli: la minaccia invisibile che compromette la supply chain

A cura di:[Luca Bongiorni](#molongui-disabled-link)  Ore 4 Dicembre 20252 Dicembre 2025

*USBsamurai e l’Internet of Offensive Things: quando un cavo da 15 euro può paralizzare un impianto industriale*

Al [23° Forum ICT Security](https://www.ictsecuritymagazine.com/eventi/forumictsecurity2025) di Roma, l’intervento intitolato **“USBsamurai & the Internet of Offensive Things”** ha sollevato il velo su una delle minacce più sofisticate e insidiose del panorama cybersecurity contemporaneo: gli impianti hardware malevoli che infiltrano la catena di approvvigionamento. Luca Bongiorni, Direttore del Cybersecurity Lab di ZTE Italia e fondatore del progetto WHID (*We Hack In Disguise*), ha condotto il pubblico attraverso un’analisi tecnica che parte dalle rivelazioni di Edward Snowden per arrivare alle più recenti evoluzioni degli *hardware implants*.

Con oltre 19 anni di esperienza in offensive security e una lunga carriera dedicata allo sviluppo di dispositivi hardware per operazioni di red teaming, lo speaker ha dimostrato come la sicurezza fisica dei componenti hardware rappresenti oggi un anello debole critico nelle strategie di difesa aziendale.

## Il leak di Snowden e la nascita di una nuova era di minacce

“Nel 2013 Edward Snowden sparì, fece il giro del mondo portando con sé computer e flash drive contenenti documenti classificati top secret”, ha esordito il relatore, ricostruendo la genesi del suo percorso di ricerca. Tra i documenti trafugati dai server della NSA, particolare rilevanza aveva l’**ANT Catalog** (*Advanced Network Technology*), un catalogo classificato di 50 pagine che documentava le tecnologie offensive sviluppate dalla Tailored Access Operations Unit (TAO), considerata una delle unità di intelligence più avanzate al mondo per operazioni in ambienti ostili.

Il documento rivelava operazioni sistematiche di *supply chain interdiction*: componenti hardware venivano intercettati durante la spedizione dal produttore al cliente finale e compromessi con impianti malevoli prima di raggiungere la destinazione. Agenti della NSA aprivano i pacchi in transito, installavano beacon e impianti hardware, quindi sigillarono nuovamente le confezioni come se nulla fosse accaduto.

![](https://www.ictsecuritymagazine.com/wp-content/uploads/Supply-chain-interdiction-foto-operative-NSA.jpg)

Supply chain interdiction – foto operative NSA

“Mi sono detto: interessante, se riescono a svilupparlo loro, perché non posso svilupparlo io?”, ha raccontato Bongiorni, descrivendo l’inizio di un percorso di ricerca e sviluppo decennale condotto insieme a una comunità internazionale di ricercatori di sicurezza. L’obiettivo era chiaro: democratizzare queste tecnologie offensive, renderle accessibili ai professionisti della sicurezza attraverso progetti open source a basso costo, permettendo così ai team di difesa di comprendere realmente le minacce che devono fronteggiare.

## La gallery degli orrori: quando l’hardware diventa un’arma

L’intervento ha documentato un’ampia panoramica di impianti hardware malevoli già utilizzati in attacchi reali, con conseguenze documentate. Il relatore ha mostrato dispositivi sviluppati da cybercriminali per intercettare dati di carte di credito attraverso POS compromessi, cavi USB contenenti chip nascosti e miniaturizzati, e componenti per attacchi a sistemi industriali.

![](https://www.ictsecuritymagazine.com/wp-content/uploads/Cavi-USB-con-chip-nascosti-e-GSM-bug.jpg)

Cavi USB con chip nascosti e GSM bug

Gli impianti non si limitano alle classiche chiavette USB. Bongiorni ha illustrato come praticamente qualsiasi dispositivo che comunica tramite protocollo USB possa essere weaponizzato: dai cavi di ricarica ai mouse, dalle tastiere agli alimentatori, persino dispositivi apparentemente innocui come ventilatori USB o scaldatazze possono nascondere al loro interno microcomputer completi.

“Le porte USB sono dovunque”, ha sottolineato lo speaker. “Nei nostri laptop, nei dispositivi industriali, nei sistemi di controllo ICS, negli impianti nucleari, nei sistemi di trattamento acque. Qualsiasi cosa con una porta USB è potenzialmente vulnerabile a questo tipo di attacco.”

## La minaccia concreta: attacchi documentati contro infrastrutture critiche

Il talk ha preso una piega ancora più seria quando il relatore ha iniziato a mostrare articoli di cronaca relativi a incidenti reali che hanno coinvolto impianti industriali compromessi attraverso dispositivi USB.

![](https://www.ictsecuritymagazine.com/wp-content/uploads/News-su-attacchi-USB-a-impianti-industriali.jpg)

News su attacchi USB a impianti industriali

Tra i casi documentati: un impianto nucleare tedesco infettato da malware, centrali elettriche statunitensi compromesse tramite mouse USB contenenti ransomware, e il caso degli ATM Diebold Nixdorf, dove ricercatori di Positive Technologies hanno dimostrato la possibilità di installare firmware modificato attraverso la porta USB del dispenser, permettendo di bypassare la crittografia e prelevare denaro contante.

“Questi non sono scenari ipotetici”, ha sottolineato Bongiorni. “Sono attacchi reali, condotti da threat actor motivati economicamente o da attori statali, che hanno causato danni concreti e misurabili.”

## Il pericoloso mito delle chiavette USB

Uno...