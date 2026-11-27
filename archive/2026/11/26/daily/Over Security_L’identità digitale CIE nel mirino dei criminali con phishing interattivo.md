---
title: L’identità digitale CIE nel mirino dei criminali con phishing interattivo
url: https://cert-agid.gov.it/news/lidentita-digitale-cie-nel-mirino-dei-criminali-con-phishing-interattivo/
source: Over Security
date: 2026-11-26
fetch_date: 2026-11-27T10:17:23.999119
---

# L’identità digitale CIE nel mirino dei criminali con phishing interattivo

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
* L’identità digitale CIE nel mirino dei criminali con phishing interattivo

# L’identità digitale CIE nel mirino dei criminali con phishing interattivo

26/11/2026

 [Agenzia Entrate](https://cert-agid.gov.it/tag/agenzia-entrate/)
[CIE](https://cert-agid.gov.it/tag/cie/)
[telegram](https://cert-agid.gov.it/tag/telegram/)

Nella giornata di ieri, il CERT-AGID ha rilevato e contrastato una nuova campagna di phishing che sfrutta il nome dell’**Agenzia delle Entrate** e il sistema di autenticazione mediante **Carta di Identità Elettronica** (CIE).

![](https://cert-agid.gov.it/wp-content/uploads/2026/11/image-14.png)

La pagina fraudolenta, ospitata su un dominio compromesso, riproduce l’interfaccia di autenticazione **CIE** di **livello 2**, utilizzando i loghi del Ministero dell’Interno e della Carta di Identità Elettronica.

All’utente viene richiesto di inserire il numero della CIE, il codice fiscale o l’indirizzo email, unitamente alla password associata alla propria identità digitale.

## Il pannello di controllo dei criminali

Di particolare interesse è la presenza, all’interno del sito fraudolento, di un pannello di controllo attraverso il quale i criminali possono gestire le singole sessioni di phishing.

![](https://cert-agid.gov.it/wp-content/uploads/2026/11/image-15.png)

L’interfaccia, interamente in lingua italiana, presenta diverse funzionalità riconducibili alla gestione delle fasi di autenticazione, tra cui la richiesta di informazioni personali, la verifica tramite email, SMS e applicazione mobile, nonché la possibilità di simulare errori.

Il pannello prevede inoltre la possibilità di **formulare domande personalizzate da sottoporre alla vittima** durante la sessione di phishing.

La presenza di queste funzionalità suggerisce un **approccio interattivo al phishing**, nel quale i criminali possono adattare le richieste alle risposte fornite dalla vittima, nel tentativo di acquisire non soltanto le credenziali, ma anche ulteriori informazioni necessarie a superare i meccanismi di autenticazione a più fattori.

### Telegram come canale operativo

L’utilizzo di **Telegram** nell’ambito delle attività di phishing non rappresenta una novità ed è stato [osservato](https://cert-agid.gov.it/tag/telegram/) dal CERT-AGID in numerose campagne precedenti.

Accedendo al pannello di controllo in assenza di un identificativo di sessione, viene restituito un messaggio di errore che invita l’operatore a tornare al link ricevuto tramite Telegram.

![](https://cert-agid.gov.it/wp-content/uploads/2026/11/image-16.png)

Tale evidenza suggerisce l’impiego della piattaforma di messaggistica come canale operativo attraverso il quale i criminali ricevono le notifiche relative alle sessioni di phishing e accedono ai rispettivi pannelli di controllo per interagire con le vittime.

## I rischi della compromissione

L’obiettivo della campagna è legato al **furto di credenziali CIE** per ottenere l’identità digitale del cittadino, utilizzabile per accedere a numerosi servizi online della Pubblica Amministrazione e di soggetti privati aderenti.

Considerato che l’**autenticazione CIE di livello 2** prevede un secondo fattore di sicurezza, le funzionalità del pannello suggeriscono che la campagna non sia finalizzata esclusivamente al furto delle credenziali, ma anche al tentativo di aggirare i meccanismi di autenticazione a più fattori attraverso l’interazione diretta con la vittima.

L’eventuale compromissione dell’identità digitale potrebbe pertanto avere conseguenze che vanno ben oltre l’accesso ai servizi dell’Agenzia delle Entrate.

## L’interesse verso l’identità digitale

Analogamente a quanto già osservato nelle campagne di phishing ai danni degli utenti **[SPID](https://cert-agid.gov.it/tag/spid/)**, anche la **CIE** rappresenta un obiettivo di interesse per i criminali informatici.

La possibilità di accedere, attraverso un’unica identità digitale, a numerosi servizi online della Pubblica Amministrazione e di soggetti privati rende queste utenze particolarmente appetibili.

In questo scenario, **l’Agenzia delle Entrate rappresenta il pretesto utilizzato per indurre la vittima a fornire le proprie credenziali.** L’eventuale compromissione dell’identità digitale potrebbe infatti consentire l’accesso non autorizzato a servizi diversi da quello utilizzato come esca, l’acquisizione di dati personali e fiscali e la realizzazione di successive attività fraudolente.

## Azioni di contrasto

Il CERT-AGID ha informato le strutture competenti, richiesto la dismissione del dominio utilizzato per la campagna e diramato gli indicatori di compromissione alle strutture [accreditate al Flusso IoC](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/).

Si raccomanda agli utenti di verificare sempre il dominio delle pagine di autenticazione e di non comunicare codici temporanei o autorizzare richieste di accesso non riconducibili a operazioni da loro avviate.

Taggato
[Agenzia Entrate](https://cert-agid.gov.it/tag/agenzia-entrate/)
[CIE](https://cert-agid.gov.it/tag/cie/)
[telegram](https://cert-agid.gov.it/tag/telegram/)

## Navigazione articoli

[Notizia precedente Phi...