---
title: Nuovo formato per ClamAV disponibile tramite il flusso IoC del CERT-AGID
url: https://cert-agid.gov.it/news/nuovo-formato-per-clamav-disponibile-tramite-il-flusso-ioc-del-cert-agid/
source: Over Security - Cybersecurity news aggregator
date: 2025-01-10
fetch_date: 2025-10-06T20:11:37.825112
---

# Nuovo formato per ClamAV disponibile tramite il flusso IoC del CERT-AGID

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
* Nuovo formato per ClamAV disponibile tramite il flusso IoC del CERT-AGID

# Nuovo formato per ClamAV disponibile tramite il flusso IoC del CERT-AGID

09/01/2025

 [ClamAV](https://cert-agid.gov.it/tag/clamav/)
[IoC](https://cert-agid.gov.it/tag/ioc/)

Da oggi, il [Flusso IoC](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/) del CERT-AGID supporta anche il formato per **ClamAV**, l’antivirus open source ampiamente utilizzato in contesti accademici, istituzionali e aziendali. Questa nuova funzionalità è stata realizzata per soddisfare una valida proposta espressa dalla [comunità dei sistemisti degli Atenei del GARR](https://www.garr.it/it/comunita/la-comunita-garr), che aveva evidenziato l’opportunità di aggiungere al flusso già disponibile un ulteriore formato personalizzabile e di facile utilizzo per aumentare il livello di protezione dei propri sistemi.

## Vantaggi dell’integrazione

Il nuovo formato consente di utilizzare direttamente gli indicatori di compromissione (IoC) diramati dal CERT-AGID per individuare file sospetti nei sistemi protetti da ClamAV. La gestione delle firme è trasparente e altamente flessibile, come dettagliato nella [documentazione ufficiale](https://docs.clamav.net/manual/Signatures/HashSignatures.html).

## Compatibilità e specifiche tecniche

Le pubbliche amministrazioni già accreditate al Flusso IoC possono utilizzare subito il nuovo formato per ClamAV, semplicemente aggiungendo il parametro `type=clamav` all’URL ricevuto:

*`<URL_ricevuto>&type=clamav`*

Il servizio restituirà una lista testuale conforme al formato `.hsb` per ClamAV, omettendo la dimensione del file. Per questo motivo, viene utilizzato il carattere jolly `*`. Inoltre, per garantire la compatibilità con le versioni precedenti di ClamAV, è stato fissato un livello funzionale minimo pari a `73`.

![](https://cert-agid.gov.it/wp-content/uploads/2025/01/image.png)

## Link utili

* [Accreditamento Feed IoC – CERT-AGID](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/)
* [Hash-based Signatures – ClamAV](https://docs.clamav.net/manual/Signatures/HashSignatures.html)

Taggato
[ClamAV](https://cert-agid.gov.it/tag/clamav/)
[IoC](https://cert-agid.gov.it/tag/ioc/)

## Navigazione articoli

[Notizia precedente PEC compromesse: Vidar sfrutta un nuovo metodo di offuscamento](https://cert-agid.gov.it/news/pec-compromesse-vidar-sfrutta-un-nuovo-metodo-di-offuscamento/)

[Prossima notizia: Sintesi riepilogativa delle campagne malevole nella settimana del 4 – 10 gennaio](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-4-10-gennaio/)

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