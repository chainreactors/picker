---
title: RingReaper e la zona d’ombra del kernel Linux: il nuovo volto dell’evasione EDR
url: https://www.cybersecurity360.it/nuove-minacce/ringreaper-e-la-zona-dombra-del-kernel-linux-il-nuovo-volto-dellevasione-edr/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-09
fetch_date: 2025-10-06T23:54:18.766666
---

# RingReaper e la zona d’ombra del kernel Linux: il nuovo volto dell’evasione EDR

[Vai al contenuto principale](#main-content)
[Vai al footer](#footer-content)

![logo](data:image/png;base64...)![logo](https://cdnd360.it/networkdigital360/nd360-neg.svg)

[I NOSTRI SERVIZI](https://www.cybersecurity360.it/about-network)

Menu

[![Vai alla homepage di CyberSecurity](data:image/png;base64...)![Vai alla homepage di CyberSecurity](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/03/cybersecurity_logo-768x55.png)](https://www.cybersecurity360.it)

## RingReaper e la zona d’ombra del kernel Linux: il nuovo volto dell’evasione EDR

* [Cybersecurity Nazionale](https://www.cybersecurity360.it/cybersecurity-nazionale/)
* Malware e attacchi
  + [Malware e attacchi](https://www.cybersecurity360.it/nuove-minacce/)
  + [Ransomware](https://www.cybersecurity360.it/nuove-minacce/ransomware/)
* Norme e adeguamenti
  + [Norme e adeguamenti](https://www.cybersecurity360.it/legal/)
  + [Privacy e Dati personali](https://www.cybersecurity360.it/legal/privacy-dati-personali/)
* [Soluzioni aziendali](https://www.cybersecurity360.it/soluzioni-aziendali/)
* [Cultura cyber](https://www.cybersecurity360.it/cultura-cyber/)
* [News, attualità e analisi Cyber sicurezza e privacy](https://www.cybersecurity360.it/news/)
* [Corsi cybersecurity](https://www.cybersecurity360.it/corsi-cybersecurity/)
* [Chi siamo](https://www.cybersecurity360.it/about/)

* [![Vai alla homepage di CyberSecurity](data:image/png;base64...)![Vai alla homepage di CyberSecurity](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/03/cybersecurity_neg_logo-768x55.png)](https://www.cybersecurity360.it)
* Seguici
* + [twitter](https://twitter.com/Cybersec360)
  + [linkedin](https://www.linkedin.com/company/cybersecurity360/)
  + [Newsletter](https://www.cybersecurity360.it/newsletter-signin/)
  + [Rss Feed](#rssModal)
  + [Chi siamo](https://www.cybersecurity360.it/about)
* AREA PREMIUM
* [Whitepaper](https://www.cybersecurity360.it/whitepaper/)
* [Eventi](https://www.cybersecurity360.it/eventi/)
* [Webinar](https://www.cybersecurity360.it/webinar/)
* CANALI
* [Cybersecurity nazionale](https://www.cybersecurity360.it/cybersecurity-nazionale/)
* [Malware e attacchi](https://www.cybersecurity360.it/nuove-minacce/)
* + [Ransomware](https://www.cybersecurity360.it/nuove-minacce/ransomware/)* [Norme e adeguamenti](https://www.cybersecurity360.it/legal/)
  * + [Privacy e Dati personali](https://www.cybersecurity360.it/legal/privacy-dati-personali/)* [Soluzioni aziendali](https://www.cybersecurity360.it/soluzioni-aziendali/)
    * [Cultura cyber](https://www.cybersecurity360.it/cultura-cyber/)
    * [L'esperto risponde](https://www.cybersecurity360.it/esperto-risponde/)
    * [News, attualità e analisi Cyber sicurezza e privacy](https://www.cybersecurity360.it/news/)
    * [Corsi cybersecurity](https://www.cybersecurity360.it/corsi-cybersecurity/)
    * [Chi siamo](https://www.cybersecurity360.it/about/)

[Cybersecurity nazionale](https://www.cybersecurity360.it/cybersecurity-nazionale/)
[Malware e attacchi](https://www.cybersecurity360.it/nuove-minacce/)
[Norme e adeguamenti](https://www.cybersecurity360.it/legal/)
[Soluzioni aziendali](https://www.cybersecurity360.it/soluzioni-aziendali/)
[Cultura cyber](https://www.cybersecurity360.it/cultura-cyber/)
[L'esperto risponde](https://www.cybersecurity360.it/esperto-risponde/)
[News, attualità e analisi Cyber sicurezza e privacy](https://www.cybersecurity360.it/news/)
[Corsi cybersecurity](https://www.cybersecurity360.it/corsi-cybersecurity/)
[Chi siamo](https://www.cybersecurity360.it/about/)

nuove minacce

# RingReaper e la zona d’ombra del kernel Linux: il nuovo volto dell’evasione EDR

---

[Home](https://www.cybersecurity360.it)

[Attacchi hacker e Malware: le ultime news in tempo reale e gli approfondimenti](https://www.cybersecurity360.it/nuove-minacce/)

---

Indirizzo copiato

---

RingReaper è un tool sviluppato con l’intento preciso di evadere i controlli EDR sfruttando un “angolo cieco” nel cuore stesso del kernel Linux. E ci insegna che non esistono solo vulnerabilità in senso stretto, ma anche zone grigie che, se ben sfruttate, diventano vere e proprie autostrade per gli attaccanti

Pubblicato il 8 lug 2025

---

[Sandro Sana](https://www.cybersecurity360.it/giornalista/sandro-sana-2/)

Esperto e divulgatore in cyber security, membro del Comitato Scientifico Cyber 4.0

---

---

![RingReaper tool evasione EDR](data:image/png;base64...)![RingReaper tool evasione EDR](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2025/07/RingReaper.jpg)

---

C’è un nuovo spettro che si aggira nei sistemi Linux e si chiama **RingReaper**. Niente fantasmi, intendiamoci: si tratta di un tool sviluppato con l’intento preciso di **evadere i controlli EDR** (Endpoint Detection and Response) sfruttando un angolo cieco nel cuore stesso del kernel Linux e da qui avere campo libero per muoversi indisturbato nel sistema esposto.

Un angolo legittimo, documentato, addirittura pensato per migliorare le performance I/O: **io\_uring**.

Chi si occupa seriamente di sicurezza informatica sa bene che **non esistono solo vulnerabilità in senso stretto**, ma **anche zone grigie** che, se ben sfruttate, diventano vere e proprie autostrade per gli attaccanti.

RingReaper è il veicolo che imbocca una di queste corsie preferenziali e lo fa con eleganza, precisione e soprattutto silenzio.

Indice degli argomenti

* [Il cavallo di Troia si chiama io\_uring](#Il_cavallo_di_Troia_si_chiama_io_uring)
* [RingReaper: una nuova frontiera per l’undetectable](#RingReaper_una_nuova_frontiera_per_lundetectable)
* [Il punto debole delle nostre difese](#Il_punto_debole_delle_nostre_difese)
* [RingReaper non è il futuro: è già adesso](#RingReaper_non_e_il_futuro_e_gia_adesso)
* [Bisogna guardare anche dove non c’è luce](#Bisogna_guardare_anche_dove_non_ce_luce)

## **Il cavallo di Troia si chiama io\_uring**

Per capire la portata del problema bisogna addentrarsi nel funzionamento di io\_uring, un’interfaccia introdotta in Linux a partire dalla versione 5.1 con l’obiettivo di migliorare le prestazioni nelle operazioni di input/output asincrono.

Fino a qui, tutto bene: è una tecnologia ben documentata, usata legittimamente da molti software server-side, container runtime e sistemi di storage ad alta efficienza. Ma è proprio qui che nasce il problema.

A differenza delle classiche system call – le ben note open(), read(), connect(), write() – che sono facilmente tracciabili e intercettabili da un EDR, le operazioni compiute tramite io\_uring vengono gestite tramite submission e completion ring, una modalità che consente al processo utente di interagire col kernel in maniera estremamente efficiente, ma anche molto meno visibile.

RingReaper si inserisce in questo meccanismo con l’obiettivo di **evadere i sistemi di detection tradizionali**, che non monitorano (o non lo fanno adeguatamente) le attività interne ai ring di io\_uring.

Il risultato è che, anche in presenza di un EDR, un attaccante può leggere, scrivere file, esfiltrare dati e persino comunicare in rete **senza generare alcun evento rilevabile nei log**.

## RingReaper: u**na nuova frontiera per l’undetectable**

RingReaper non è semplicemente un exploit. È un esempio perfetto di ciò che può succedere quando una tecnologia nasce per ottimizzare e finisce nelle mani sbagliate.

Gli sviluppatori del tool non hanno scoperto una vulnerabilità. Hanno solo letto con attenzione la documentazione del kernel e notato che, al momento, quasi nessun EDR commerciale tiene conto delle interazioni tramite io\_uring. Da lì alla weaponizzazione, il passo è breve.

È una tecnica di **evasione comportamentale**, non basata sull’offuscamento del codice né sull’uso di rootkit: semplicemente, le azioni del [malware](https://www.cybersecurity360.it/nuove-minacce/malware-cosa-sono-come-riconoscerli-e-come-rimuoverli/) non vengono intercettate perché eseguite in una zona cieca. Ed è qui che la sicurezza difensiva mostra tutte...