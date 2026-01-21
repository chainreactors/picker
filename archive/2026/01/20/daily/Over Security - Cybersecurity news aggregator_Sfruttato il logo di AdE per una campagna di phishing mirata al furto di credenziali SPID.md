---
title: Sfruttato il logo di AdE per una campagna di phishing mirata al furto di credenziali SPID
url: https://cert-agid.gov.it/news/sfruttato-il-logo-di-ade-per-una-campagna-di-phishing-mirata-al-furto-di-credenziali-spid/
source: Over Security - Cybersecurity news aggregator
date: 2026-01-20
fetch_date: 2026-01-21T03:32:59.578459
---

# Sfruttato il logo di AdE per una campagna di phishing mirata al furto di credenziali SPID

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
* Sfruttato il logo di AdE per una campagna di phishing mirata al furto di credenziali SPID

# Sfruttato il logo di AdE per una campagna di phishing mirata al furto di credenziali SPID

20/01/2026

 [Agenzia Entrate](https://cert-agid.gov.it/tag/agenzia-entrate/)
[phishing](https://cert-agid.gov.it/tag/phishing/)
[SPID](https://cert-agid.gov.it/tag/spid/)

A brevissima distanza dalla [precedente campagna di phishing a tema **SPID**](https://cert-agid.gov.it/news/nuova-campagna-di-phishing-a-tema-spid-sfrutta-google-sites/), è stato rilevato dal CERT-AGID un phishing, ai danni dell’**Agenzia delle Entrate**, finalizzato ad acquisire le credenziali di accesso delle identità digitali **SPID** degli utenti.

La campagna viene diffusa tramite comunicazioni ingannevoli che invitano l’utente ad accedere alla propria area riservata dell’**Agenzia delle Entrate** e contengono al loro interno un link che reindirizza a un sito creato ad hoc per raccogliere credenziali.

![](https://cert-agid.gov.it/wp-content/uploads/2026/01/phishing_AdE_20_01_2026.png)

La pagina web fraudolenta presenta agli utenti una falsa schermata di accesso all’area riservata dell’**Agenzia delle Entrate** che riproduce un modulo di login tramite **SPID** contraffatto. Nello specifico, viene richiesto all’utente di inserire la sola password della propria identità SPID, mentre l’indirizzo email della vittima è già precompilato tramite personalizzazione del link.

## Azioni di contrasto

Al fine di prevenire le possibili sottrazioni di dati, Il CERT-AGID ha avvisato l’Ente interessato e ha richiesto la disattivazione del sito ospitante la pagina di phishing. Gli Indicatori di Compromissione (IoC) relativi alla campagna sono stati diramati attraverso il [feed](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/) del CERT-AGID verso le strutture accreditate.

## Indicatori di Compromissione

Al fine di rendere pubblici i dettagli della campagna odierna si riportano di seguito gli IoC rilevati:

**Link:** [Download IoC](https://cert-agid.gov.it/wp-content/uploads/2026/01/phishing_SPID_20_01_26.json)

Taggato
[Agenzia Entrate](https://cert-agid.gov.it/tag/agenzia-entrate/)
[phishing](https://cert-agid.gov.it/tag/phishing/)
[SPID](https://cert-agid.gov.it/tag/spid/)

## Navigazione articoli

[Notizia precedente Nuova campagna di phishing a tema SPID sfrutta Google Sites](https://cert-agid.gov.it/news/nuova-campagna-di-phishing-a-tema-spid-sfrutta-google-sites/)

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