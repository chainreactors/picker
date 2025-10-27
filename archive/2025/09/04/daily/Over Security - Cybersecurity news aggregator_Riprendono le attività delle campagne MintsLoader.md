---
title: Riprendono le attività delle campagne MintsLoader
url: https://cert-agid.gov.it/news/riprende-la-campagna-mintsloader/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-04
fetch_date: 2025-10-02T19:37:59.601099
---

# Riprendono le attività delle campagne MintsLoader

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
* Riprendono le attività delle campagne MintsLoader

# Riprendono le attività delle campagne MintsLoader

03/09/2025

 [MintsLoader](https://cert-agid.gov.it/tag/mintsloader/)
[PEC](https://cert-agid.gov.it/tag/pec/)

Dopo una lunga pausa estiva, nella giornata di ieri è stata osservata una nuova campagna **MintsLoader**, la prima dopo quella [registrata lo scorso giugno](https://cert-agid.gov.it/news/nuova-campagna-mintsloader-conferma-una-mirata-strategia-temporale/).

![](https://cert-agid.gov.it/wp-content/uploads/2025/09/immagine.png)

Rispetto alle precedenti ondate, il template dell’email risulta solo leggermente modificato, mantenendo però lo schema già noto. In particolare:

* invece del consueto link ipertestuale sulla parola “*Fattura*”, l’email presenta ora un file **ZIP allegato**;
* all’interno dell’archivio compresso è presente un file **JavaScript** offuscato che avvia la catena di compromissione.

## Abuso di caselle PEC

Come già osservato nelle [precedenti ondate](https://cert-agid.gov.it/tag/pec/), anche questa campagna mantiene la stessa natura di diffusione: i messaggi vengono **inviati da caselle PEC compromesse a caselle PEC dei destinatari**, sfruttando quindi il canale certificato per aumentare la credibilità e l’efficacia dell’attacco.

L’obiettivo finale è la compromissione dei sistemi delle vittime, in particolare macchine **Windows** (dalla versione 10 in poi), dove la disponibilità del comando *cURL* viene sfruttata per avviare la catena d’infezione e installare malware, generalmente appartenenti alla categoria degli [infostealer](https://cert-agid.gov.it/?s=infostealer).

## Strategia temporale

È inoltre interessante evidenziare come venga mantenuta la stessa **strategia temporale** già descritta nel precedente avviso del CERT-AGID, con un ritorno delle attività in coincidenza con la ripresa lavorativa post-estiva.

![](https://cert-agid.gov.it/wp-content/uploads/2025/06/immagine.png)

## Raccomandazioni

Si raccomanda di prestare attenzione a messaggi email sospetti, in particolare a quelli con oggetto relativo a fatture scadute e contenenti allegati ZIP, evitando in ogni caso di estrarre gli archivi e interagire con i file al loro interno. Nel dubbio, è sempre possibile inoltrare le email ritenute sospette alla casella di posta **malware@cert-agid.gov.it**

## Azioni di contrasto

Le attività di contrasto sono state già messe in atto con il supporto dei Gestori PEC. Gli IoC relativi alla campagna sono stati diramati attraverso il [Feed IoC](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/) del CERT-AGID verso i Gestori PEC e verso le strutture accreditate.

## Indicatori di Compromissione

Al fine di rendere pubblici i dettagli della campagna odierna si riportano di seguito gli IoC rilevati:

**Link:** [Download IoC](https://cert-agid.gov.it/wp-content/uploads/2025/09/mintsloader_pec_02-09-2025.json)

Taggato
[MintsLoader](https://cert-agid.gov.it/tag/mintsloader/)
[PEC](https://cert-agid.gov.it/tag/pec/)

## Navigazione articoli

[Notizia precedente Torna lo smishing ai danni di utenti INPS](https://cert-agid.gov.it/news/torna-lo-smishing-ai-danni-di-utenti-inps/)

[Prossima notizia: Sintesi riepilogativa delle campagne malevole nella settimana del 30 agosto – 5 settembre](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-30-agosto-5-settembre/)

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