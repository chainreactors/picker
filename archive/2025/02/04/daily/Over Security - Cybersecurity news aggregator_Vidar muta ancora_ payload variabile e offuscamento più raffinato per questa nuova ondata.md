---
title: Vidar muta ancora: payload variabile e offuscamento più raffinato per questa nuova ondata
url: https://cert-agid.gov.it/news/vidar-muta-ancora-payload-variabile-e-offuscamento-piu-raffinato-per-questa-nuova-ondata/
source: Over Security - Cybersecurity news aggregator
date: 2025-02-04
fetch_date: 2025-10-06T20:47:12.904116
---

# Vidar muta ancora: payload variabile e offuscamento più raffinato per questa nuova ondata

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
* Vidar muta ancora: payload variabile e offuscamento più raffinato per questa nuova ondata

# Vidar muta ancora: payload variabile e offuscamento più raffinato per questa nuova ondata

03/02/2025

 [PEC](https://cert-agid.gov.it/tag/pec/)
[vidar](https://cert-agid.gov.it/tag/vidar/)

![](https://cert-agid.gov.it/wp-content/uploads/2025/02/email.png)

Nella tarda serata del 2 febbraio 2025, è stata individuata una nuova campagna Vidar che segue lo schema [già osservato](https://cert-agid.gov.it/tag/vidar/) in precedenti attacchi, caratterizzata dall’uso di tecniche di offuscamento avanzate e dall’impiego di Domain Generation Algorithm (DGA) per la generazione dinamica degli indirizzi malevoli. L’attività è stata rilevata intorno alla mezzanotte, con **136 domini principali associati** identificati durante l’analisi dell’incidente.

Come nelle campagne precedenti, gli URL utilizzati per la distribuzione del payload, un file JS opportunamente offuscato, sono **rimasti inattivi nella fase iniziale dell’attacco**, attivandosi solo nella mattinata successiva per sfuggire ai controlli preventivi. Questa tecnica, ormai consolidata, consente ai cybercriminali di ridurre la possibilità di un blocco immediato del malware, aumentando le probabilità di successo dell’infezione.

Un elemento distintivo di questa nuova ondata è l’adozione di un metodo di offuscamento ancora più raffinato. Il malware elabora la stringa di input suddividendola in una lista di numeri interi, che vengono poi decodificati tramite un’operazione **XOR** con un valore costante, restituendo infine il codice de-offuscato pronto per l’esecuzione. Questo approccio mira a rendere più complessa l’analisi statica e il rilevamento da parte degli strumenti di sicurezza automatizzati.

Oltre alle strategie ormai consolidate per eludere i sistemi di sicurezza, come l’uso di DGA e l’attivazione ritardata delle URL, si osserva anche una **costante variazione del payload scaricato a seguito dell’infezione:** Vidar, infatti, conduce di volta in volta al rilascio di un ulteriore malware afferente sempre a una famiglia diversa.

## Azioni di contrasto

Le attività di contrasto sono state già messe in atto con il supporto dei Gestori PEC. Gli IoC relativi alla campagna sono stati diramati attraverso il [Feed IoC](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/) del CERT-AGID verso i Gestori PEC e verso le strutture accreditate.

Si raccomanda di prestare sempre la massima attenzione alle comunicazioni ricevute via PEC, in particolare quando contengono link ritenuti sospetti. Nel dubbio, è sempre possibile inoltrare le email ritenute sospette alla casella di posta **malware@cert-agid.gov.it**

## Indicatori di Compromissione

Al fine di rendere pubblici i dettagli della campagna odierna si riportano di seguito gli IoC rilevati:

**Link:** [Download IoC](https://cert-agid.gov.it/wp-content/uploads/2025/02/vidar-03-02-2025.json)

Taggato
[PEC](https://cert-agid.gov.it/tag/pec/)
[vidar](https://cert-agid.gov.it/tag/vidar/)

## Navigazione articoli

[Notizia precedente Sintesi riepilogativa delle campagne malevole nella settimana del 25 – 31 gennaio](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-25-31-gennaio/)

[Prossima notizia: Sintesi riepilogativa delle campagne malevole nella settimana del 01 – 07 febbraio](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-01-07-febbraio/)

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