---
title: Campagna Ursnif in corso a tema Agenzia delle Entrate
url: https://cert-agid.gov.it/news/campagna-ursnif-in-corso-a-tema-agenzia-delle-entrate/
source: Over Security - Cybersecurity news aggregator
date: 2022-12-16
fetch_date: 2025-10-04T01:41:35.377551
---

# Campagna Ursnif in corso a tema Agenzia delle Entrate

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
* Campagna Ursnif in corso a tema Agenzia delle Entrate

# Campagna Ursnif in corso a tema Agenzia delle Entrate

15/12/2022

 [Agenzia Entrate](https://cert-agid.gov.it/tag/agenzia-entrate/)
[SMB](https://cert-agid.gov.it/tag/smb/)
[Ursnif](https://cert-agid.gov.it/tag/ursnif/)

![](https://cert-agid.gov.it/wp-content/uploads/2022/12/ursnif_agenzia_entrate.png)

Il CERT-AGID ha evidenza di una campagna malevola, attualmente in corso, volta a veicolare il malware **Ursnif** tramite una e-mail che riporta una falsa comunicazione della **Agenzia delle Entrate**.

L’e-mail invita la vittima a prendere visione delle informazioni presenti nell’archivio (ZIP) allegato che, a differenza delle campagne Ursnif già analizzate in precedenza, contiene una cartella denominata “*Dicembre*“, all’interno della quale sono presenti due file: un **Internet Shortcut** denominato “*Dicembre.url*” ed una immagine “*Logo\_Agenzia\_Entrate.jpg*“.

![](https://cert-agid.gov.it/wp-content/uploads/2022/12/ursnif_Dicembre_folder.png)

L’eseguibile di Ursnif viene scaricato ed eseguito sui sistemi Windows tramite le istruzioni presenti nel file “*Dicembre.url*” (Internet Shortcut) seguendo il percorso evidenziato in URL (SMB).

## Indicatori di Compromissione

Gli IoC relativi a questa campagna sono stati già condivisi con le organizzazioni [accreditate al flusso IoC](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/) del CERT-AGID.

**Link:** [Download IoC](https://cert-agid.gov.it/wp-content/uploads/2022/12/ursnif_agenzia_entrate_15-12-2022.json_.txt)

Taggato
[Agenzia Entrate](https://cert-agid.gov.it/tag/agenzia-entrate/)
[SMB](https://cert-agid.gov.it/tag/smb/)
[Ursnif](https://cert-agid.gov.it/tag/ursnif/)

## Navigazione articoli

[Notizia precedente Sintesi riepilogativa delle campagne malevole nella settimana del 2 – 9 dicembre 2022](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-2-9-dicembre-2022/)

[Prossima notizia: Terzo monitoraggio sull’utilizzo del protocollo HTTPS e sullo stato di aggiornamento dei CMS sui sistemi della PA](https://cert-agid.gov.it/news/terzo-monitoraggio-sullutilizzo-del-protocollo-https-e-sullo-stato-di-aggiornamento-dei-cms-sui-sistemi-della-pa/)

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