---
title: Ancora attacchi ad opera di Vidar: cadenza regolare e vecchie strategie sempre efficaci
url: https://cert-agid.gov.it/news/ancora-attacchi-ad-opera-di-vidar-cadenza-regolare-e-vecchie-strategie-sempre-efficaci/
source: Over Security - Cybersecurity news aggregator
date: 2025-01-21
fetch_date: 2025-10-06T20:12:35.531827
---

# Ancora attacchi ad opera di Vidar: cadenza regolare e vecchie strategie sempre efficaci

* [Vai al contenuto](#main)
* [Vai alla navigazione del sito](#menu "accedi al menu")

[![Logo CERT-AGID](/wp-content/themes/cert-agid/assets/images/cert-agid-logo-white.svg)](https://cert-agid.gov.it/)

# [CERT-AGID Computer Emergency Response Team AGID](https://cert-agid.gov.it/)

[Agenzia per
l'Italia Digitale](https://www.agid.gov.it)

[![Logo AgID - Agenzia per l'Italia Digitale](/wp-content/themes/cert-agid/assets/images/logo-agid.svg)](https://www.agid.gov.it)

Seguici su

* [RSS](https://cert-agid.gov.it/feed/ "RSS")
* [Telegram](https://t.me/certagid "Telegram")
* [X / Twitter](https://twitter.com/agidcert "X / Twitter")

cerca nel sito

[Menu](#menu "accedi al menu")

![Logo del CERT-PA](/wp-content/themes/cert-agid/assets/images/cert-agid-logo-black.svg)
CERT-AGID

<https://cert-agid.gov.it/>

## Menu di navigazione

* Documentazione
  + [Documenti AGID](https://cert-agid.gov.it/documenti-agid/)
  + [Pillole informative](https://cert-agid.gov.it/pillole-informative/)
  + [Flusso IoC](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/)
* [Chi siamo](https://cert-agid.gov.it/chi-siamo/)
* [Contatti](https://cert-agid.gov.it/contatti/)
* [Strumenti](https://cert-agid.gov.it/strumenti/)
  + [hashr](https://cert-agid.gov.it/hashr/)
  + [Verifica HTTPS e CMS](https://cert-agid.gov.it/verifica-https-cms/)
  + [Statistiche sulle campagne italiane di malware e phishing](https://cert-agid.gov.it/statistiche/)
* [Glossario](https://cert-agid.gov.it/glossario/)
  + [0day](https://cert-agid.gov.it/glossario/0day/)
  + [Botnet](https://cert-agid.gov.it/glossario/botnet/)
  + [Data breach](https://cert-agid.gov.it/glossario/data-breach/)
  + [DDOS-DOS](https://cert-agid.gov.it/glossario/ddos-dos/)
  + [Deep-Dark web](https://cert-agid.gov.it/glossario/deep-dark-web/)
  + [Defacing](https://cert-agid.gov.it/glossario/defacing/)
  + [Exploit](https://cert-agid.gov.it/glossario/exploit/)
  + [MITM](https://cert-agid.gov.it/glossario/mitm/)
  + [OSINT-CLOSINT](https://cert-agid.gov.it/glossario/osint-closint/)
  + [Phishing](https://cert-agid.gov.it/glossario/phishing/)
  + [Privilege escalation](https://cert-agid.gov.it/glossario/privilege-escalation/)
  + [Spam](https://cert-agid.gov.it/glossario/spam/)
  + [Spoofing](https://cert-agid.gov.it/glossario/spoofing/)
  + [SQLi-SQL Injection](https://cert-agid.gov.it/glossario/sqli-sql-injection/)
  + [XSS](https://cert-agid.gov.it/glossario/xss/)
* Link utili
  + [Agenzia per l’Italia Digitale](https://www.agid.gov.it/)
  + [CSIRT Italia](https://csirt.gov.it)
  + [CERT-GARR](https://www.cert.garr.it/)
  + [CNAIPIC](https://www.commissariatodips.it/profilo/cnaipic/index.html)
  + [CERT-DIFESA](https://www.difesa.it/smd/cor/cert-difesa/25338.html)

* [Home](https://cert-agid.gov.it/)
* [Notizie](https://cert-agid.gov.it/category/news/)
* [Malware](https://cert-agid.gov.it/category/news/malware/)
* Ancora attacchi ad opera di Vidar: cadenza regolare e vecchie strategie sempre efficaci

# Ancora attacchi ad opera di Vidar: cadenza regolare e vecchie strategie sempre efficaci

20/01/2025

 [PEC](https://cert-agid.gov.it/tag/pec/)
[vidar](https://cert-agid.gov.it/tag/vidar/)

Le campagne malware **Vidar** proseguono con la loro cadenza ormai regolare, prendendo di mira gli utenti italiani ogni lunedì mattina. L’ultima ondata, rilevata nella notte del 20 gennaio 2025, sfrutta nuovamente le **PEC compromesse** per inviare e-mail esclusivamente ai possessori di caselle PEC, puntando sulla attendibilità di queste comunicazioni per massimizzare il tasso di successo degli attacchi.

![](https://cert-agid.gov.it/wp-content/uploads/2025/01/vidar-email.png)

Come già osservato in [precedenti](https://cert-agid.gov.it/tag/vidar/) campagne, anche questa volta gli attori malevoli hanno fatto largo uso della tecnica del [Domain Generation Algorithm](https://en.wikipedia.org/wiki/Domain_generation_algorithm) (DGA) e della rotazione di utilizzo di numerosi host: sono stati rilevati **147 host utilizzati per distribuire il payload** sotto forma di file JavaScript.

Queste strategie, sebbene già ampiamente note e sfruttate da tempo, si rivelano sempre efficaci nel complicare il rilevamento e la mitigazione delle campagne. In particolare, le URL generate con DGA ed i percorsi randomizzati **restano inattive durante la fase iniziale notturno dell’attacco e si attivano solo nella mattinata successiva**, aumentando le difficoltà della prevenzione proattiva.

## Azioni di contrasto

Le attività di contrasto sono state già messe in atto con il supporto dei Gestori PEC. Gli IoC relativi alla campagna sono stati diramati attraverso il [Feed IoC](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/) del CERT-AGID verso i Gestori PEC e verso le strutture accreditate.

Si raccomanda di prestare sempre la massima attenzione alle comunicazioni ricevute via PEC, in particolare quando contengono link ritenuti sospetti. Nel dubbio, è sempre possibile inoltrare le email ritenute sospette alla casella di posta **malware@cert-agid.gov.it**

## Indicatori di Compromissione

Al fine di rendere pubblici i dettagli della campagna odierna si riportano di seguito gli IoC rilevati:

**Link:** [Download IoC](https://cert-agid.gov.it/wp-content/uploads/2025/01/vidar-20-01-2025.json)

Taggato
[PEC](https://cert-agid.gov.it/tag/pec/)
[vidar](https://cert-agid.gov.it/tag/vidar/)

## Navigazione articoli

[Notizia precedente Sintesi riepilogativa delle campagne malevole nella settimana del 11 – 17 gennaio](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-11-17-gennaio/)

[Prossima notizia: Report riepilogativo sulle tendenze delle campagne malevole analizzate dal CERT-AGID nel 2024](https://cert-agid.gov.it/news/report-riepilogativo-sulle-tendenze-delle-campagne-malevole-analizzate-dal-cert-agid-nel-2024/)

![Logo del CERT-PA](/wp-content/themes/cert-agid/assets/images/cert-agid-logo-white.svg)
CERT-AGID

cerca nel sito

* [Contatti](https://cert-agid.gov.it/contatti/)
* [Privacy](https://cert-agid.gov.it/privacy/)
* [Note legali](https://cert-agid.gov.it/note-legali/)

#### Seguici su

* [RSS](https://cert-agid.gov.it/feed/ "RSS")
* [Telegram](https://t.me/certagid "Telegram")
* [X / Twitter](https://twitter.com/agidcert "X / Twitter")

![Logo del CERT-PA](/wp-content/themes/cert-agid/assets/images/cert-agid-logo-black.svg)
CERT-AGID

<https://cert-agid.gov.it/>