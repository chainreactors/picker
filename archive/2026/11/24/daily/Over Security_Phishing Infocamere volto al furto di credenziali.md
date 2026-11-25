---
title: Phishing Infocamere volto al furto di credenziali
url: https://cert-agid.gov.it/news/phishing-infocamere-volto-al-furto-di-credenziali/
source: Over Security
date: 2026-11-24
fetch_date: 2026-11-25T10:48:14.823680
---

# Phishing Infocamere volto al furto di credenziali

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
* Phishing Infocamere volto al furto di credenziali

# Phishing Infocamere volto al furto di credenziali

24/11/2026

 [infocamere](https://cert-agid.gov.it/tag/infocamere/)

Il CERT-AGID ha rilevato una campagna di phishing che sfrutta il nome e il logo di **InfoCamere**, la società che gestisce il patrimonio informativo e i servizi digitali delle Camere di Commercio italiane, con l’obiettivo di sottrarre le credenziali di accesso degli utenti.

![Pagina di phishing](https://cert-agid.gov.it/wp-content/uploads/2026/11/image-13.png)

La pagina fraudolenta è ospitata su un dominio registrato il **22 novembre 2026**, che richiama esplicitamente quello utilizzato da InfoCamere per l’autenticazione degli utenti, e riproduce l’interfaccia di autenticazione del portale legittimo, proponendo quattro modalità di accesso: **Credenziali**, SPID, CIE e CNS/Token Wireless.

Le modalità di autenticazione alternative (SPID, CIE e CNS/Token Wireless) sono puramente decorative, prive di qualsiasi funzionalità. L’utente è quindi indotto a utilizzare l’unica modalità di accesso disponibile, **quella tramite codice utente e password.** Le credenziali inserite vengono trasmesse al server fraudolento mediante una richiesta HTTP POST.

Per rendere ulteriormente credibile la pagina, gli autori della campagna hanno inserito un collegamento per il recupero della password che rimanda al dominio legittimo di InfoCamere.

## I rischi della compromissione

Le utenze InfoCamere rappresentano un obiettivo di particolare interesse per i criminali, in quanto associate a servizi digitali utilizzati da imprese, professionisti, intermediari e Pubbliche Amministrazioni.

La compromissione di tali utenze potrebbe consentire, in funzione del profilo e delle abilitazioni dell’utente, l’accesso non autorizzato a dati e documenti camerali, la consultazione di pratiche amministrative, l’utilizzo indebito di servizi a pagamento e l’acquisizione di informazioni utili a successive attività fraudolente ai danni delle imprese.

## Azioni di contrasto

Il CERT-AGID ha notificato a InfoCamere la presenza della campagna di phishing e ha richiesto la dismissione del dominio fraudolento.

Si raccomanda agli utenti di **verificare sempre il dominio delle pagine di autenticazione** prima di inserire le proprie credenziali e, qualora queste siano state inserite nella pagina fraudolenta, di **procedere tempestivamente alla loro modifica** e di **verificare eventuali accessi o operazioni** non autorizzate.

Taggato
[infocamere](https://cert-agid.gov.it/tag/infocamere/)

## Navigazione articoli

[Notizia precedente Sintesi riepilogativa delle campagne malevole nella settimana del 14 – 20 novembre](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-14-20-novembre/)

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