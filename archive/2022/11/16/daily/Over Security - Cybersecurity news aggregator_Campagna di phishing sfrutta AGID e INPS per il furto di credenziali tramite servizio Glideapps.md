---
title: Campagna di phishing sfrutta AGID e INPS per il furto di credenziali tramite servizio Glideapps
url: https://cert-agid.gov.it/news/campagna-di-phishing-sfrutta-agid-e-inps-per-il-furto-di-credenziali-tramite-servizio-glideapps/
source: Over Security - Cybersecurity news aggregator
date: 2022-11-16
fetch_date: 2025-10-03T22:54:05.472945
---

# Campagna di phishing sfrutta AGID e INPS per il furto di credenziali tramite servizio Glideapps

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
* Campagna di phishing sfrutta AGID e INPS per il furto di credenziali tramite servizio Glideapps

# Campagna di phishing sfrutta AGID e INPS per il furto di credenziali tramite servizio Glideapps

15/11/2022

 [AgID](https://cert-agid.gov.it/tag/agid/)
[inps](https://cert-agid.gov.it/tag/inps/)

![](https://cert-agid.gov.it/wp-content/uploads/2022/11/phishing-agid.glideapp.png)

Da circa una settimana è in corso una campagna di phishing, indirizzata indistintamente a organizzazioni pubbliche e soggetti privati che, facendo leva sull’accreditamento al **Bonus INPS 2022**, invita i destinatari a prendere visione di un allegato HTML.

Il corpo del messaggio riporta il seguente testo:

> Stiamo tentando. di accreditare inps bonus sul suo conto è abbiamo,
>
> un esito negativo si prega di ggiornare i suoi dati sul.
>
> CodicePratica : IOCPKXWLZP .
>
> SERVIZIO INPS ONLINE 2022

Il file HTML allegato all’e-mail è denominato “*AGID-NUMERO4034.html*” e una volta aperto visualizza una pagina realizzata con “glideapps” che mostra una versione mobile dei contenuti.

Nel caso specifico, gli utenti che si apprestano a visionare l’allegato da un dispositivo mobile si ritrovano dinanzi ad una (falsa) app di AGID con l’unica opzione quella di cliccare sul pulsante “AGID MISURE MINIME DI SICUREZZA” che condurrà la vittima ad una nuova pagina attraverso la quale potrà scegliere il servizio con cui autenticarsi per confermare i propri dati.

![](https://cert-agid.gov.it/wp-content/uploads/2022/11/phishing-agid-glideapp-2.png)

A prescindere da ciò che la vittima sceglierà tra Nexi, Mediolanum e Poste, le credenziali inserite dall’utente verranno memorizzate su un server remoto gestito dai truffatori.

Il CERT-AGID, grazie alle tempestive segnalazioni pervenute da INPS, aveva avuto evidenza già la scorsa settimana di campagne di phishing che sfruttavano il servizio “glideapps” e il tema “Bonus INPS 2022”.

![](https://cert-agid.gov.it/wp-content/uploads/2022/11/phishing-inps-glideapp.png)

## Indicatori di Compromissione

Gli IoC relativi a questa campagna sono stati già condivisi con le organizzazioni [accreditate al flusso IoC](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/) del CERT-AGID.

**Link:** [Download IoC](https://cert-agid.gov.it/wp-content/uploads/2022/11/phishing-agid-inps-glideapp.json_.txt)

Taggato
[AgID](https://cert-agid.gov.it/tag/agid/)
[inps](https://cert-agid.gov.it/tag/inps/)

## Navigazione articoli

[Notizia precedente Sintesi riepilogativa delle campagne malevole nella settimana del 05 – 11 novembre 2022](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-05-11-novembre-2022/)

[Prossima notizia: Sintesi riepilogativa delle campagne malevole nella settimana del 12 – 18 novembre 2022](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-12-18-novembre-2022/)

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