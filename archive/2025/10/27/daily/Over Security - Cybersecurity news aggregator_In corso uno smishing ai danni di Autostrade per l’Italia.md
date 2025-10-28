---
title: In corso uno smishing ai danni di Autostrade per l’Italia
url: https://cert-agid.gov.it/news/in-corso-uno-smishing-ai-danni-di-autostrade-per-litalia/
source: Over Security - Cybersecurity news aggregator
date: 2025-10-27
fetch_date: 2025-10-28T03:00:18.597541
---

# In corso uno smishing ai danni di Autostrade per l’Italia

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
* In corso uno smishing ai danni di Autostrade per l’Italia

# In corso uno smishing ai danni di Autostrade per l’Italia

27/10/2025

 [autostrade](https://cert-agid.gov.it/tag/autostrade/)
[smishing](https://cert-agid.gov.it/tag/smishing/)

Il CERT-AGID ha avuto evidenza di una nuova campagna di smishing veicolata tramite finti SMS che sfruttano il nome di **Autostrade per l’Italia**. I messaggi fanno riferimento a un presunto “*pedaggio non saldato*” e presentano un link che indirizza la vittima alla pagina malevola.

![](https://cert-agid.gov.it/wp-content/uploads/2025/10/Screenshot-from-2025-10-27-sms.png)

Il sito fraudolento presenta il nome e il logo ufficiale di **ASPI** e richiede all’utente l’inserimento di dati personali (**targa e numero di cellulare**) e della **carta di pagamento**.

![](https://cert-agid.gov.it/wp-content/uploads/2025/10/Screenshot-from-2025-10-27-11-41-04.png)
![](https://cert-agid.gov.it/wp-content/uploads/2025/10/Screenshot-from-2025-10-27-11-42-00.png)

Le strategie adottate dall’attaccante includono lo sfruttamento di un sito che assomiglia a quello originale e *[typosquatting](https://it.wikipedia.org/wiki/Typosquatting)* sul nome di dominio: le pagine malevole sono infatti ospitate su “*autostiade[.]com*”, un dominio creato per apparire simile all’ufficiale “**autostrade.it**”, differendo solamente per poche lettere al fine di trarre in inganno la vittima.

## Attività di contrasto

Il CERT-AGID ha avviato le opportune attività di contrasto alla campagna contattando il servizio di *“abus*e” del Registrar per richiedere la dismissione del dominio. Gli IoC relativi alla campagna sono stati condivisi con le organizzazioni [accreditate al flusso IoC](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/) del CERT-AGID.

## Precauzioni

È sempre consigliabile verificare con attenzione l’URL della pagina a cui si viene reindirizzati: assicurarsi che il nome di dominio corrisponda esattamente a quello ufficiale dell’organizzazione indicata nel messaggio. Inoltre, è bene diffidare da qualsiasi richiesta di inserimento di dati personali o bancari che arrivi tramite email o SMS, soprattutto se accompagnata da toni allarmistici o pressioni legate a scadenze imminenti.

In caso di dubbi, è buona pratica non interagire con il messaggio e inoltrarlo al CERT-AGID all’indirizzo **malware@cert-agid.gov.it**, che provvederà alle necessarie analisi per poi procedere con un riscontro.

Taggato
[autostrade](https://cert-agid.gov.it/tag/autostrade/)
[smishing](https://cert-agid.gov.it/tag/smishing/)

## Navigazione articoli

[Notizia precedente Sintesi riepilogativa delle campagne malevole nella settimana del 18 – 24 ottobre](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-18-24-ottobre/)

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