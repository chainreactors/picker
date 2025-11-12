---
title: Campagna di phishing a tema Facebook: falsa segnalazione di violazione Copyright
url: https://cert-agid.gov.it/news/campagna-di-phishing-a-tema-facebook-falsa-segnalazione-di-violazione-copyright/
source: Over Security - Cybersecurity news aggregator
date: 2025-11-11
fetch_date: 2025-11-12T03:12:45.328047
---

# Campagna di phishing a tema Facebook: falsa segnalazione di violazione Copyright

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
* Campagna di phishing a tema Facebook: falsa segnalazione di violazione Copyright

# Campagna di phishing a tema Facebook: falsa segnalazione di violazione Copyright

11/11/2025

 [Facebook](https://cert-agid.gov.it/tag/facebook/)
[Meta](https://cert-agid.gov.it/tag/meta/)
[violazione copyright](https://cert-agid.gov.it/tag/violazione-copyright/)

Il CERT-AGID ha avuto evidenza di una campagna di phishing veicolata tramite email che, usando toni e riferimenti legali, accusa il destinatario della comunicazione di aver violato, tramite il proprio account **Facebook**, il copyright di Universal Music Group (**UMG**) per l’uso del brano “Someone You Loved” di Lewis Capaldi. La mail presenta un allegato PDF intitolato “*Final Legal Warning – Video Copyright*” contenente un link per visionare il fantomatico post incriminato.

![](https://cert-agid.gov.it/wp-content/uploads/2025/11/Screenshot-from-2025-11-11-15-12-11.png)

## Falso CAPTCHA

Una volta cliccato sul link, la vittima viene reindirizzata a una pagina che riproduce l’ambiente di **Meta** e mostra un finto controllo `reCAPTCHA`, studiato per trasmettere un’illusione di legittimità.

![](https://cert-agid.gov.it/wp-content/uploads/2025/11/Screenshot-from-2025-11-11-10-39-38.png)

## Finto popup con URL Facebook

Superato questo passaggio, compare un finto popup del browser per effettuare il login su Facebook. La finestra simulata appare completa di lucchetto, `https` e dominio “facebook.com”, ma l’indirizzo **è solo un elemento grafico** non interattivo: non è selezionabile, non modifica il dominio reale visibile nella barra del browser e non instrada la sessione verso i server Facebook. I campi di email/telefono e password appartengono in realtà alla pagina di phishing sottostante e, al momento di cliccare su “Accedi”, i dati vengono inviati al server di comando e controllo degli attaccanti (**C2**).

![](https://cert-agid.gov.it/wp-content/uploads/2025/11/Screenshot-from-2025-11-11-10-40-09-1024x782.png)

## Indicatori di compromissione

Il CERT-AGID ha già condiviso i relativi IoC con le organizzazioni [accreditate al flusso](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/). Al fine di rendere pubblici i dettagli di questa campagna si riportano di seguito gli indicatori rilevati.

**Link:** [Download IoC](https://cert-agid.gov.it/wp-content/uploads/2025/11/phishing_Facebook_11-11-2025.json)

Taggato
[Facebook](https://cert-agid.gov.it/tag/facebook/)
[Meta](https://cert-agid.gov.it/tag/meta/)
[violazione copyright](https://cert-agid.gov.it/tag/violazione-copyright/)

## Navigazione articoli

[Notizia precedente Analisi di Remcos RAT diffuso in Italia con campagna ClickFix a tema GLS](https://cert-agid.gov.it/news/analisi-di-remcos-rat-diffuso-in-italia-con-campagna-clickfix-a-tema-gls/)

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