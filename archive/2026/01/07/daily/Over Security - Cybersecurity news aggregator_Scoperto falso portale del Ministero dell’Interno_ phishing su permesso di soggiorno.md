---
title: Scoperto falso portale del Ministero dell’Interno: phishing su permesso di soggiorno
url: https://cert-agid.gov.it/news/scoperto-falso-portale-del-ministero-dellinterno/
source: Over Security - Cybersecurity news aggregator
date: 2026-01-07
fetch_date: 2026-01-08T03:30:29.951512
---

# Scoperto falso portale del Ministero dell’Interno: phishing su permesso di soggiorno

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
* Scoperto falso portale del Ministero dell’Interno: phishing su permesso di soggiorno

# Scoperto falso portale del Ministero dell’Interno: phishing su permesso di soggiorno

07/01/2026

 [Ministero Interno](https://cert-agid.gov.it/tag/ministero-interno/)
[permesso di soggiorno](https://cert-agid.gov.it/tag/permesso-di-soggiorno/)
[phishing](https://cert-agid.gov.it/tag/phishing/)
[Polizia di Stato](https://cert-agid.gov.it/tag/polizia-di-stato/)

Il CERT-AGID ha avuto evidenza di un dominio malevolo, di recente registrazione, utilizzato per ospitare un falso portale del **Ministero dell’Interno** (con riferimenti anche alla **Polizia di Stato**). Il sito si presenta come servizio di verifica dello stato di lavorazione o validità di varie pratiche amministrative legate all’immigrazione in Italia.

![](https://cert-agid.gov.it/wp-content/uploads/2026/01/Screenshot-from-2026-01-07-16-52-18.png)

La pagina fraudolenta dichiara di offrire la consultazione dello stato del **permesso di soggiorno**, sostenendo che l’esito della procedura di richiesta sia disponibile inserendo il codice numerico della pratica. Il contenuto richiama inoltre procedure connesse a **decreto flussi**, **ricongiungimento familiare** e **lavoro irregolare**, con l’obiettivo di risultare coerente con i percorsi amministrativi reali e aumentare la credibilità del portale.

Cliccando su “*Check Application Status*” la vittima viene reindirizzata a una pagina che richiede l’inserimento di dati identificativi e dettagli di pratica, tra cui generalità, data di nascita, nazionalità, numero di documento/passaporto e numero di protocollo, per poter procedere con la verifica.

![](https://cert-agid.gov.it/wp-content/uploads/2026/01/Screenshot-from-2026-01-07-16-46-20.png)

La finalità più probabile della campagna è indurre i cittadini stranieri in attesa di nulla osta, permesso di soggiorno o visto a inserire dati personali ai fini di furto d’identità e successive frodi mirate.

## Attività di contrasto

Il CERT-AGID ha prontamente informato il reparto di sicurezza del **Ministero dell’Interno**, ha richiesto la dismissione del dominio e diramato gli **indicatori di compromissione** alle organizzazioni [accreditate al flusso IoC](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/).

**Link:** [Scarica gli IoC](https://cert-agid.gov.it/wp-content/uploads/2026/01/phishing_Ministero_Interno_07_01_26.json)

Taggato
[Ministero Interno](https://cert-agid.gov.it/tag/ministero-interno/)
[permesso di soggiorno](https://cert-agid.gov.it/tag/permesso-di-soggiorno/)
[phishing](https://cert-agid.gov.it/tag/phishing/)
[Polizia di Stato](https://cert-agid.gov.it/tag/polizia-di-stato/)

## Navigazione articoli

[Notizia precedente Vulnerabilità critica in n8n. Rischio elevato per istanze esposte in rete](https://cert-agid.gov.it/news/vulnerabilita-critica-in-n8n-rischio-elevato-per-istanze-esposte-in-rete/)

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