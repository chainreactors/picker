---
title: Rilasciata una nuova versione del tool Hashr
url: https://cert-agid.gov.it/news/rilasciata-una-nuova-versione-del-tool-hashr/
source: Over Security - Cybersecurity news aggregator
date: 2024-11-12
fetch_date: 2025-10-06T19:20:44.733394
---

# Rilasciata una nuova versione del tool Hashr

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
* Rilasciata una nuova versione del tool Hashr

# Rilasciata una nuova versione del tool Hashr

11/11/2024

 [hashr](https://cert-agid.gov.it/tag/hashr/)

Il CERT-AGID ha recentemente rilasciato una nuova versione del tool [**hashr**](https://cert-agid.gov.it/hashr/) (v.2.0.1) come software libero e a codice aperto sotto licenza [EUPL](https://interoperable-europe.ec.europa.eu/collection/eupl). Questo strumento, scaricabile gratuitamente dall’[apposita pagina](https://cert-agid.gov.it/hashr/), è progettato per la ricerca di file malevoli all’interno di un filesystem confrontando i valori hash dei file riscontrati con una lista di impronte hash già note. **Hashr** può essere utilizzato con proprie liste di ricerca oppure, per le Pubbliche Amministrazione accreditate al feed IoC del CERT-AGID, con gli hash derivati dalle campagne malevole registrate che hanno un impatto sul territorio italiano.

![](https://cert-agid.gov.it/wp-content/uploads/2024/11/Screenshot-hashr.png)

Tutte le **Pubbliche Amministrazioni** possono accreditarsi al [feed IoC del CERT-AGID](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/) per avere accesso a un flusso in tempo reale di Indicatori di Compromissione (IoC), che elenca e condivide dati su campagne malware e phishing rilevate nelle attività quotidiane di monitoraggio e prevenzione, come ad esempio gli indirizzi IP utilizzati per attività fraudolente, URL di siti malevoli, hash di file dannosi e altre informazioni. Tale servizio, offerto gratuitamente, è rivolto esclusivamente alle Pubbliche Amministrazioni.

![](https://cert-agid.gov.it/wp-content/uploads/2024/11/Screenshot-Feed-IoC.png)

In sinergia con il Feed IoC, **hashr** consente di ricercare file con hash correlati a campagne malevole note o APT analizzati dal CERT-AGID, permettendo di identificare rapidamente i file compromessi. L’uso di hashr risulta particolarmente utile per indagini di sicurezza informatica, analisi forense e verifica dell’integrità dei file su filesystem di grandi dimensioni.

L’utilizzo combinato di **hashr** e del **feed IoC** aumenta significativamente la capacità di prevenire ed individuare minacce informatiche, incrementando la sicurezza complessiva delle infrastrutture digitali.

Questi due strumenti forniti da [AGID](https://www.agid.gov.it/) costituiscono un’opportunità per le amministrazioni per migliorare la sicurezza dei propri sistemi IT, per adeguarsi, al contempo, alle indicazioni del **Piano Triennale per l’Informatica 2024-2026** e per rafforzare la resilienza digitale complessiva della Pubblica Amministrazione.

## Link utili:

* [hashr](https://cert-agid.gov.it/hashr/) (download e guida)
* [Strumenti](https://cert-agid.gov.it/strumenti/)
* [Accreditamento feed IoC](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/)

Taggato
[hashr](https://cert-agid.gov.it/tag/hashr/)

## Navigazione articoli

[Notizia precedente Vidar nuovamente attivo in Italia tramite caselle PEC compromesse: nuova campagna con URL aggiornati](https://cert-agid.gov.it/news/vidar-nuovamente-attivo-in-italia-tramite-caselle-pec-compromesse-nuova-campagna-con-url-aggiornati/)

[Prossima notizia: Falsa notifica DocuSign: credenziali trasmesse a bot Telegram](https://cert-agid.gov.it/news/false-notifica-docusign-credenziali-trasmesse-a-bot-telegram/)

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