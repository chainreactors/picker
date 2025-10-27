---
title: Formbook diffuso via macro Office: nel mirino aziende coinvolte in gare e progetti
url: https://cert-agid.gov.it/news/formbook-diffuso-via-macro-office-nel-mirino-aziende-coinvolte-in-gare-e-progetti/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-19
fetch_date: 2025-10-06T23:54:07.666242
---

# Formbook diffuso via macro Office: nel mirino aziende coinvolte in gare e progetti

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
* Formbook diffuso via macro Office: nel mirino aziende coinvolte in gare e progetti

# Formbook diffuso via macro Office: nel mirino aziende coinvolte in gare e progetti

18/07/2025

 [formbook](https://cert-agid.gov.it/tag/formbook/)

Nonostante Microsoft abbia introdotto importanti misure di sicurezza per evitare l’abuso delle **macro** nei documenti **Office**, come a esempio il blocco di default nei file scaricati da Internet tramite il *“[Mark of the Web](https://techcommunity.microsoft.com/blog/microsoft_365blog/helping-users-stay-safe-blocking-internet-macros-by-default-in-office/3071805)“*, l’uso di questa tecnologia rimane ancora oggi uno strumento efficace per gli attaccanti.

Sebbene non siano più sfruttate come in passato, le macro rimangono sempre una minaccia concreta, favorita dalla diffusione capillare di MS Office – spesso in versioni obsolete o non aggiornate – e, soprattutto, dalla possibilità di sfruttare l’errore umano.

Molto recentemente il CERT-AGID ha individuato ed analizzato una campagna particolarmente curata volta a diffondere il malware **Formbook** tramite email mirate, indirizzate probabilmente a potenziali clienti di una grande azienda italiana del settore energetico.

L’allegato è un file PDF utilizzato per avviare la campagna, riporta il logo ufficiale dell’azienda e contiene due link che promettono il download di presunti documenti di progetto, protetti da password e ospitati su piattaforme di file sharing.

![](https://cert-agid.gov.it/wp-content/uploads/2025/07/image-3b.png)

Una volta scaricato e scompattato l’archivio ZIP, protetto con password come indicato nel PDF, si hanno a disposizione vari documenti di MS Office. Alcuni di questi sono innocui mentre altri, sia in formato DOC che XLSB, risultano dotati di macro.

![](https://cert-agid.gov.it/wp-content/uploads/2025/07/image-4b.png)

L’analisi del codice evidenzia una catena ben orchestrata, che conduce passo dopo passo all’installazione del malware **Formbook**, attraverso il download e l’esecuzione di componenti malevoli provenienti da:

* **domini registrati di recente**, con nomi simili a quelli della società impersonata;
* **domini italiani compromessi**, verosimilmente legittimi e riconducibili ad altre aziende operanti nello stesso settore.

Una campagna tecnicamente semplice ma credibile e ben orchestrata, che fa leva su dinamiche tipiche del contesto aziendale, come gare d’appalto, progetti riservati o inviti a partecipare a iniziative commerciali. Proprio questa aderenza al reale contribuisce ad abbassare le difese dell’utente, aumentando le probabilità di apertura dei documenti e il rischio che venga eseguito il loro contenuto malevolo. In scenari del genere, non è la complessità tecnica a fare la differenza, ma la capacità di integrarsi nelle aspettative operative di chi riceve il messaggio.

## Indicatori di Compromissione

Al fine di rendere pubblici i dettagli della campagna, di seguito vengono riportati gli Indicatori di Compromissione (IoC) rilevati, già condivisi con le organizzazioni pubbliche accreditate al Flusso IoC del CERT-AGID.

**Link:** [Download IoC](https://cert-agid.gov.it/wp-content/uploads/2025/07/formbook-17-07-2025.json)

Taggato
[formbook](https://cert-agid.gov.it/tag/formbook/)

## Navigazione articoli

[Notizia precedente Sintesi riepilogativa delle campagne malevole nella settimana del 5 – 11 luglio](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-5-11-luglio/)

[Prossima notizia: Sintesi riepilogativa delle campagne malevole nella settimana del 12 – 18 luglio](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-12-18-luglio/)

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