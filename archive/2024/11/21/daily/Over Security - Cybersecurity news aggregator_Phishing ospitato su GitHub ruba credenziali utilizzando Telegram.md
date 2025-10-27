---
title: Phishing ospitato su GitHub ruba credenziali utilizzando Telegram
url: https://cert-agid.gov.it/news/phishing-ospitato-su-github-ruba-credenziali-utilizzando-telegram/
source: Over Security - Cybersecurity news aggregator
date: 2024-11-21
fetch_date: 2025-10-06T19:19:10.894903
---

# Phishing ospitato su GitHub ruba credenziali utilizzando Telegram

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
* Phishing ospitato su GitHub ruba credenziali utilizzando Telegram

# Phishing ospitato su GitHub ruba credenziali utilizzando Telegram

20/11/2024

 [github](https://cert-agid.gov.it/tag/github/)
[phishing](https://cert-agid.gov.it/tag/phishing/)
[telegram](https://cert-agid.gov.it/tag/telegram/)

![](https://cert-agid.gov.it/wp-content/uploads/2024/11/wetransfer_email.png)

Il CERT-AGID ha recentemente rilevato una campagna di phishing che sfrutta i brand **WeTransfer**, noto servizio per la condivisione di file, e **cPanel**, pannello di controllo per la gestione e l’amministrazione di siti internet. Le email fraudolente presentano link a presunti file condivisi con l’utente che reindirizzano a una falsa pagina di login.

![](https://cert-agid.gov.it/wp-content/uploads/2024/11/Screenshot-From-2024-11-20-11-33-09.png)

Seguendo il link fornito, l’utente viene indirizzato a una pagina che imita fedelmente il modulo di accesso alla Webmail di *cPanel*, progettata per sottrarre le credenziali. Questa pagina è pubblicata su **GitHub** **Pages**, una piattaforma legittima di GitHub che consente a chiunque di ospitare siti web statici direttamente da repository. L’uso di un dominio GitHub autentico aumenta la credibilità del sito agli occhi della vittima, rendendo l’attacco ancora più insidioso.

![](https://cert-agid.gov.it/wp-content/uploads/2024/11/webmail_cpanel_html.png)

Un’analisi del codice **HTML** e del **JavaScript** integrato rivela che la pagina è progettata per inviare le credenziali sottratte a un **bot** **Telegram**. Oltre alle credenziali, vengono trasmesse ulteriori informazioni, come i record MX del provider email e dettagli sulla geolocalizzazione dell’indirizzo IP della vittima.

![](https://cert-agid.gov.it/wp-content/uploads/2024/11/webmail_cpanel_js.png)

*Codice JS della pagina di phishing*

L’abuso di Telegram come strumento per raccogliere e trasmettere informazioni sensibili sta diventando sempre più comune sia nelle campagne di phishing che in quelle malware. I bot su Telegram, infatti, permettono agli attaccanti di raccogliere in tempo reale i dati sottratti alla vittima tramite una piattaforma di semplice utilizzo e difficile da contrastare.

## Azioni di contrasto

Gli indicatori di compromissione rilevati, già diramati tramite il [Flusso IoC](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/) a tutti gli enti accreditati, sono disponibili di seguito al fine di rendere pubblici i dettagli della campagna. Le pagine sono state inoltre segnalate al supporto di GitHub per la rimozione.

**Link:** [Download IoC](https://cert-agid.gov.it/wp-content/uploads/2024/11/phishing_wetransfer_2024-11-20.json)

## Raccomandazioni

È importante rimanere vigili e informati sulle minacce di phishing per tutelare i propri dati. Prestare attenzione a comunicazioni sospette e adottare semplici precauzioni può fare la differenza nella salvaguardia delle informazioni personali e professionali.

Taggato
[github](https://cert-agid.gov.it/tag/github/)
[phishing](https://cert-agid.gov.it/tag/phishing/)
[telegram](https://cert-agid.gov.it/tag/telegram/)

## Navigazione articoli

[Notizia precedente Il malware Vidar evolve con nuove strategie di diversificazione dei domini](https://cert-agid.gov.it/news/il-malware-vidar-evolve-con-nuove-strategie-di-diversificazione-dei-domini/)

[Prossima notizia: Sintesi riepilogativa delle campagne malevole nella settimana del 16 – 22 novembre](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-16-22-novembre/)

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