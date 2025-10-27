---
title: Risolte vulnerabilità nelle librerie .NET per SPID e CIE
url: https://cert-agid.gov.it/news/risolte-vulnerabilita-nelle-librerie-net-per-spid-e-cie/
source: Over Security - Cybersecurity news aggregator
date: 2025-02-18
fetch_date: 2025-10-06T20:48:01.377098
---

# Risolte vulnerabilità nelle librerie .NET per SPID e CIE

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
* Risolte vulnerabilità nelle librerie .NET per SPID e CIE

# Risolte vulnerabilità nelle librerie .NET per SPID e CIE

17/02/2025

 [CIE](https://cert-agid.gov.it/tag/cie/)
[CVE-2025-24894](https://cert-agid.gov.it/tag/cve-2025-24894/)
[CVE-2025-24895](https://cert-agid.gov.it/tag/cve-2025-24895/)
[SPID](https://cert-agid.gov.it/tag/spid/)

![](https://cert-agid.gov.it/wp-content/uploads/2025/02/spid-cie.png)

Recentemente sono state individuate vulnerabilità nelle librerie .NET utilizzate per l’autenticazione a SPID e CIE. Queste librerie, sviluppate da terze parti nell’ambito di una [challenge](https://hack.developers.italia.it/challenge/) promossa nel 2017 dal Dipartimento per la Trasformazione Digitale, sono state rese disponibili nel repository Developers Italia su Github.

La vulnerabilità, scoperta e segnalata tempestivamente al CERT-AGID dalla società *Shielder*, riguarda il meccanismo di verifica delle risposte SAML. Il problema interessa esclusivamente i Service Provider che hanno implementato l’autenticazione a SPID o CIE utilizzando le suddette librerie .NET.

## Impatto della vulnerabilità

Un attaccante potrebbe generare una risposta SAML arbitraria che, a causa della falla, verrebbe accettata dai Service Provider vulnerabili. Ciò gli consentirebbe di impersonare qualsiasi utente SPID o CIE, con gravi rischi per la sicurezza.

## Azioni intraprese e misure di mitigazione

Due librerie affette dalla vulnerabilità sono state deprecate e aggiornate dai *maintainers* con nuove versioni sicure, mentre una terza libreria è stata definitivamente dismessa.

AgID ha introdotto due nuovi controlli nel [Validator](https://github.com/italia/spid-saml-check) SAML SP per SPID, lo strumento utilizzato dai Service Provider nella fase di collaudo, per individuare anomalie nelle risposte SAML:

* 112. SAML Response Signature Verification Bypass – *Assertion non firmata*
* 113. SAML Response Signature Verification Bypass – *Assertion corrotta*

## Cosa devono fare i Service Provider

Si raccomanda ai Service Provider che utilizzano librerie .NET per l’autenticazione SPID o CIE di aggiornare immediatamente alle versioni più recenti delle librerie supportate e di verificare con attenzione i controlli 112 e 113 durante il collaudo SPID.

## Riferimenti alle librerie interessate:

* CVE-2025-24894 – <https://github.com/italia/spid-aspnetcore>
* CVE-2025-24895 – <https://github.com/italia/cie-aspnetcore>

Taggato
[CIE](https://cert-agid.gov.it/tag/cie/)
[CVE-2025-24894](https://cert-agid.gov.it/tag/cve-2025-24894/)
[CVE-2025-24895](https://cert-agid.gov.it/tag/cve-2025-24895/)
[SPID](https://cert-agid.gov.it/tag/spid/)

## Navigazione articoli

[Notizia precedente Sintesi riepilogativa delle campagne malevole nella settimana del 08 – 14 febbraio](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-08-14-febbraio/)

[Prossima notizia: Sintesi riepilogativa delle campagne malevole nella settimana del 15 – 21 febbraio](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-15-21-febbraio/)

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