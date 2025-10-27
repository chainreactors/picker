---
title: PEC compromesse: Vidar sfrutta un nuovo metodo di offuscamento
url: https://cert-agid.gov.it/news/pec-compromesse-vidar-sfrutta-un-nuovo-metodo-di-offuscamento/
source: Over Security - Cybersecurity news aggregator
date: 2025-01-08
fetch_date: 2025-10-06T20:13:20.081472
---

# PEC compromesse: Vidar sfrutta un nuovo metodo di offuscamento

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
* PEC compromesse: Vidar sfrutta un nuovo metodo di offuscamento

# PEC compromesse: Vidar sfrutta un nuovo metodo di offuscamento

07/01/2025

 [PEC](https://cert-agid.gov.it/tag/pec/)
[vidar](https://cert-agid.gov.it/tag/vidar/)

![](https://cert-agid.gov.it/wp-content/uploads/2025/01/email.png)

Nella serata del 6 gennaio 2025, è stata rilevata una nuova campagna [**Vidar**](https://cert-agid.gov.it/tag/vidar/): i cyber-criminali continuano a sfruttare **caselle PEC compromesse** per diffondere il malware tra gli utenti italiani. Questa campagna presenta ulteriori elementi di complessità introducendo nuove tecniche per occultare la url da cui scaricare il payload.

La distribuzione del malware è stata accompagnata da nuove strategie per eludere i sistemi di sicurezza. Gli attacchi si sono basati su **148 domini di secondo livello**, configurati per sfruttare un Domain Generation Algorithm (DGA) e path randomizzati. Durante la fase iniziale, gli URL sono rimasti inattivi per poi attivarsi solo successivamente, aumentando la difficoltà di una prevenzione tempestiva.

![](https://cert-agid.gov.it/wp-content/uploads/2025/01/immagine-1-1024x275.png)

![](https://cert-agid.gov.it/wp-content/uploads/2025/01/immagine-1024x487.png)

Un ulteriore elemento di novità è stato l’utilizzo di un file JavaScript con un metodo di offuscamento migliorato. Il file JS è stato riscritto per eseguire un’operazione di **`XOR` sui valori di una lista** e converte i risultati in caratteri tramite `chr`, rendendo più complesso il processo di analisi e rilevamento. Inoltre, IP, domini e caselle mittenti sono stati ruotati ogni 2-3 minuti, contribuendo a complicare ulteriormente le azioni di difesa.

## Azioni di contrasto

Le attività di contrasto sono state già messe in atto con il supporto dei Gestori PEC. Gli IoC relativi alla campagna sono stati diramati attraverso il [Feed IoC](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/) del CERT-AGID verso i Gestori PEC e verso le strutture accreditate.

Si raccomanda di prestare sempre la massima attenzione alle comunicazioni ricevute via PEC, in particolare quando contengono link ritenuti sospetti. Nel dubbio, è sempre possibile inoltrare le email ritenute sospette alla casella di posta **malware@cert-agid.gov.it**

## Indicatori di Compromissione

Al fine di rendere pubblici i dettagli della campagna odierna si riportano di seguito gli IoC rilevati:

**Link:** [Download IoC](https://cert-agid.gov.it/wp-content/uploads/2025/01/vidar_07-01-2025.json)

Taggato
[PEC](https://cert-agid.gov.it/tag/pec/)
[vidar](https://cert-agid.gov.it/tag/vidar/)

## Navigazione articoli

[Notizia precedente Sintesi riepilogativa delle campagne malevole nella settimana del 28 dicembre – 3 gennaio](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-28-dicembre-3-gennaio/)

[Prossima notizia: Nuovo formato per ClamAV disponibile tramite il flusso IoC del CERT-AGID](https://cert-agid.gov.it/news/nuovo-formato-per-clamav-disponibile-tramite-il-flusso-ioc-del-cert-agid/)

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