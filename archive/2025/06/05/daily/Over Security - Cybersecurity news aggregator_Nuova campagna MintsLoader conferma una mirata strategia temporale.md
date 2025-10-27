---
title: Nuova campagna MintsLoader conferma una mirata strategia temporale
url: https://cert-agid.gov.it/news/nuova-campagna-mintsloader-conferma-una-mirata-strategia-temporale/
source: Over Security - Cybersecurity news aggregator
date: 2025-06-05
fetch_date: 2025-10-06T22:55:03.661770
---

# Nuova campagna MintsLoader conferma una mirata strategia temporale

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
* Nuova campagna MintsLoader conferma una mirata strategia temporale

# Nuova campagna MintsLoader conferma una mirata strategia temporale

04/06/2025

 [MintsLoader](https://cert-agid.gov.it/tag/mintsloader/)
[PEC](https://cert-agid.gov.it/tag/pec/)

Oggi è stata registrata una nuova ondata della campagna malevola **MintsLoader**, la nona rilevata dall’inizio del 2025, che evidenzia come gli attori malevoli sappiano ben adattarsi ai calendari lavorativi italiani.

![](https://cert-agid.gov.it/wp-content/uploads/2025/06/immagine-1.png)

A differenza del consueto schema temporale, in cui gli attacchi vengono attuati principalmente il lunedì, questa volta la campagna è stata avviata di mercoledì. Questo cambiamento è probabilmente dovuto alla festività nazionale del 2 giugno (Festa della Repubblica), che ha posticipato il primo giorno lavorativo della settimana.

L’analisi delle date degli attacchi registrati nei primi sei mesi del 2025 evidenzia una chiara strategia temporale dei cybercriminali:

![](https://cert-agid.gov.it/wp-content/uploads/2025/06/immagine.png)

Questa distribuzione temporale dimostra come gli attaccanti sfruttino pienamente le abitudini lavorative italiane, adattando i loro attacchi per massimizzare l’efficacia quando gli utenti sono più propensi o necessitati a consultare la email legate al lavoro, in questo caso le PEC, dopo periodi di pausa (weekend o festività).

## Caratteristiche della campagna

Le campagne sfruttano il noto loader basato su PowerShell, MintsLoader per diffondere vari tipi di malware, solitamente **Infostealer**, attraverso caselle **PEC compromesse**. La catena di infezione segue un consolidato modus operandi: invio di email contenenti link a file **JavaScript offuscati**, impiego di **Domain Generation Algorithm** (DGA) per la generazione dinamica degli indirizzi malevoli, attivazione dei domini **durante le ore lavorative**, nonostante le campagne vengano veicolate nelle prime ore del mattino, e rilascio controllato dei payload tramite script **PowerShell**. Tuttavia, a causa degli attenti controlli lato server, ottenere il payload finale sta diventando sempre più difficile per chi cerca di analizzare il malware.

## Azioni di contrasto

Le attività di contrasto sono state già messe in atto con il supporto dei Gestori PEC. Gli IoC relativi alla campagna sono stati diramati attraverso il [Feed IoC](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/) del CERT-AGID verso i Gestori PEC e verso le strutture accreditate.

Si raccomanda di prestare sempre la massima attenzione alle comunicazioni ricevute via PEC, in particolare quando contengono link ritenuti sospetti. Nel dubbio, è sempre possibile inoltrare le email ritenute sospette alla casella di posta **malware@cert-agid.gov.it**

## Indicatori di Compromissione

Al fine di rendere pubblici i dettagli della campagna odierna si riportano di seguito gli IoC rilevati:

**Link:** [Download IoC](https://cert-agid.gov.it/wp-content/uploads/2025/06/mintsloader-04-06-2025.json)

Taggato
[MintsLoader](https://cert-agid.gov.it/tag/mintsloader/)
[PEC](https://cert-agid.gov.it/tag/pec/)

## Navigazione articoli

[Notizia precedente Campagna di phishing in corso per gli account di LiberoMail](https://cert-agid.gov.it/news/campagna-di-phishing-in-corso-per-gli-account-di-liberomail/)

[Prossima notizia: Sintesi riepilogativa delle campagne malevole nella settimana del 31 maggio – 6 giugno](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-31-maggio-6-giugno/)

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