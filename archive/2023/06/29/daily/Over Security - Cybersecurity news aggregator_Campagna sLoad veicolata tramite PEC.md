---
title: Campagna sLoad veicolata tramite PEC
url: https://cert-agid.gov.it/news/malware/campagna-sload-veicolata-tramite-pec/
source: Over Security - Cybersecurity news aggregator
date: 2023-06-29
fetch_date: 2025-10-04T11:49:46.916317
---

# Campagna sLoad veicolata tramite PEC

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
* Campagna sLoad veicolata tramite PEC

# Campagna sLoad veicolata tramite PEC

28/06/2023

 [PEC](https://cert-agid.gov.it/tag/pec/)
[sLoad](https://cert-agid.gov.it/tag/sload/)

![](https://cert-agid.gov.it/wp-content/uploads/2023/04/email_sload.png)

A distanza di 2 mesi dall’ultima campagna, [sLoad](https://cert-agid.gov.it/news/cosa-sappiamo-di-sload-e-perche-e-cosi-elusivo/) torna a colpire l’Italia con una campagna veicolata, come di consueto, tramite PEC. La campagna ha avuto inizio poco dopo la mezzanotte del 28 giugno e ha diffuso a numerose caselle di posta elettronica certificata email che invitano i destinatari a cliccare sul link presente nel corpo del messaggio al fine di scaricare una finta fattura.

Come per la scorsa campagna, il file scaricato è uno ZIP contenente un file VBS denominato *FatturaXXXXXXX.vbs* e viene usato ancora una volta *bitsadmin* per scaricare e lanciare un eseguibile (sLoad) da un dominio remoto.

![](https://cert-agid.gov.it/wp-content/uploads/2023/06/image-1-1024x86.png)

Subito dopo l’avvio dell’infezione l’indirizzo IP ed il nome della macchina della vittima sono registrate sul C2. Come è tipico delle TTP di sLoad, payload aggiuntivi saranno rilasciati successivamente e tipicamente hanno lo scopo di esfiltrare informazioni come le credenziali di posta.

Non avendo potuto ottenere il payload finale non è stato possibile effettuare analisi approfondite.

## Azioni di contrasto

* Le attività di contrasto sono già state messe in atto con il supporto dei Gestori PEC.
* Gli IoC sono stati diramati attraverso il [Feed IoC](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/) del CERT-AgID verso i Gestori PEC e le strutture accreditate.

Si invita a prestare sempre attenzione a questo genere di comunicazioni. Nel dubbio, potete inoltrare l’email a malware@cert-agid.gov.it

## Indicatori di Compromissione

Al fine di rendere pubblici i dettagli della campagna odierna si riportano di seguito gli IoC rilevati:

**Link:** [Download IoC](https://cert-agid.gov.it/wp-content/uploads/2023/06/sload_2023-06-28.json)

Taggato
[PEC](https://cert-agid.gov.it/tag/pec/)
[sLoad](https://cert-agid.gov.it/tag/sload/)

## Navigazione articoli

[Notizia precedente Sintesi riepilogativa delle campagne malevole nella settimana del 17 – 23 giugno 2023](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-17-23-giugno-2023/)

[Prossima notizia: Sintesi riepilogativa delle campagne malevole nella settimana del 24 – 30 giugno 2023](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-24-30-giugno-2023/)

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