---
title: Falso “Bonus Vacanze” dell’Agenzia delle Entrate ruba dati personali
url: https://cert-agid.gov.it/news/falso-bonus-vacanze-dellagenzia-delle-entrate-ruba-dati-personali/
source: Over Security
date: 2026-09-16
fetch_date: 2026-09-17T07:00:00.073001
---

# Falso “Bonus Vacanze” dell’Agenzia delle Entrate ruba dati personali

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
* Falso “Bonus Vacanze” dell’Agenzia delle Entrate ruba dati personali

# Falso “Bonus Vacanze” dell’Agenzia delle Entrate ruba dati personali

16/09/2026

 [Agenzia Entrate](https://cert-agid.gov.it/tag/agenzia-entrate/)
[bonus](https://cert-agid.gov.it/tag/bonus/)
[phishing](https://cert-agid.gov.it/tag/phishing/)

Il CERT-AGID ha rilevato una nuova campagna che utilizza in modo fraudolento il nome, il logo e la grafica dell’**Agenzia delle Entrate** e dell’**Agenzia delle entrate-Riscossione**, con l’obiettivo di sottrarre dati personali agli utenti. Il nuovo pretesto utilizzato è la presentazione di una richiesta per un presunto ***“Bonus Vacanze”***.

A differenza della maggior parte delle campagne di phishing che sfruttano il nome dell’ente, questa risulta particolarmente curata. La pagina fraudolenta non si limita infatti a proporre un semplice modulo da compilare, ma riproduce un sito più articolato, organizzato in diverse sezioni e con una procedura suddivisa in più passaggi. Una struttura pensata per rendere la pagina più credibile e indurre l’utente a proseguire fino all’inserimento dei propri dati.

![](https://cert-agid.gov.it/wp-content/uploads/2026/09/phishing_AdE_bonusvacanze_home.png)

*Homepage del sito fraudolento*

## Descrizione del flusso di attacco

La homepage del sito fraudolento riproduce in modo piuttosto fedele la home del portale dell’**Agenzia delle Entrate**. Diversi collegamenti presenti nella pagina rimandano al sito ufficiale dell’Agenzia, contribuendo a rendere il portale malevolo più credibile.

Fa eccezione il pulsante *“Scopri i servizi disponibili”*, che indirizza l’utente verso un’altra pagina dello stesso sito fraudolento.

![](https://cert-agid.gov.it/wp-content/uploads/2026/09/phishing_AdE_bonusvacanze_servizi.png)

*Pagina “Tutti i servizi” del sito fraudolento*

Anche la pagina *“Tutti i servizi”* contiene numerosi collegamenti a contenuti del portale istituzionale. Tra questi compare però la voce *“Bonus Vacanze”*, che conduce a una falsa pagina di login. All’utente vengono proposte le consuete modalità di accesso tramite **SPID** e **CieID**, affiancate da una terza opzione, *“Altro”*, che invita a effettuare l’accesso **caricando manualmente i propri documenti.**

![](https://cert-agid.gov.it/wp-content/uploads/2026/09/phishing_AdE_bonusvacanze_login_spid.png)
![](https://cert-agid.gov.it/wp-content/uploads/2026/09/phishing_AdE_bonusvacanze_login_cie.png)
![](https://cert-agid.gov.it/wp-content/uploads/2026/09/phishing_AdE_bonusvacanze_login_altro.png)

*Finte modalità di login proposte dalla pagina di phishing*

Se l’utente sceglie di accedere tramite **SPID** o **CieID**, viene reindirizzato a una pagina autentica del gestore selezionato, un Identity Provider SPID oppure il Ministero dell’Interno, per effettuare l’autenticazione sul vero portale dell’Agenzia delle Entrate.

A questo punto la vittima ha già navigato tra diverse pagine dall’aspetto realistico e ha persino interagito con un’autentica pagina di autenticazione, ed è quindi plausibile che eventuali dubbi sull’affidabilità del sito si siano progressivamente ridotti, inducendola a proseguire.

Se invece l’utente seleziona la terza modalità di accesso, come indicato dalle istruzioni presenti nella comunicazione esca, viene mostrata una schermata che richiede il caricamento delle fotografie del fronte e del retro della **carta d’identità** e della **tessera sanitaria**, oltre a una copia delle **buste paga degli ultimi tre mesi**. Nei passaggi successivi viene inoltre richiesto di caricare un **selfie** e di fornire **numero di telefono** e **indirizzo e-mail**.

![](https://cert-agid.gov.it/wp-content/uploads/2026/09/phishing_AdE_bonusvacanze_caricamento.png)

*Richiesta dei documenti per presunta “verifica idoneità”*

La raccolta di una quantità così ampia di informazioni personali e documenti espone le vittime a rischi rilevanti. I dati sottratti possono infatti essere utilizzati per tentare frodi e furti d’identità, ad esempio presentando richieste di finanziamento o di prestito a nome della vittima.

## Azioni di contrasto

Al fine di prevenire le possibili sottrazioni di dati, Il CERT-AGID ha avvisato l’Ente interessato e ha richiesto la disattivazione del sito ospitante la pagina di phishing. Gli Indicatori di Compromissione (IoC) relativi alla campagna sono stati diramati attraverso il [feed](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/) del CERT-AGID verso le strutture accreditate.

## Indicatori di Compromissione

Al fine di rendere pubblici i dettagli della campagna odierna si riportano di seguito gli IoC rilevati:

**Link:** [Download IoC](https://cert-agid.gov.it/wp-content/uploads/2026/09/phishing_AdE_bonusvacanze.json)

Taggato
[Agenzia Entrate](https://cert-agid.gov.it/tag/agenzia-entrate/)
[bonus](https://cert-agid.gov.it/tag/bonus/)
[phishing](https://cert-agid.gov.it/tag/phishing/)

## Navigazione articoli

[Notizia precedente Sintesi riepilogativa delle campagne malevole nella settimana del 5 – 11 settembre](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-5-11-sette...