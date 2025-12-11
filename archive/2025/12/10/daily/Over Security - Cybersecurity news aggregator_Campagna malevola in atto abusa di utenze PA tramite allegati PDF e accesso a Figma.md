---
title: Campagna malevola in atto abusa di utenze PA tramite allegati PDF e accesso a Figma
url: https://cert-agid.gov.it/news/campagna-malevola-in-atto-abusa-di-utenze-pa-tramite-allegati-pdf-e-accesso-a-figma/
source: Over Security - Cybersecurity news aggregator
date: 2025-12-10
fetch_date: 2025-12-11T03:24:51.612168
---

# Campagna malevola in atto abusa di utenze PA tramite allegati PDF e accesso a Figma

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
* Campagna malevola in atto abusa di utenze PA tramite allegati PDF e accesso a Figma

# Campagna malevola in atto abusa di utenze PA tramite allegati PDF e accesso a Figma

10/12/2025

 [figma](https://cert-agid.gov.it/tag/figma/)

È in corso una campagna malevola che sfrutta account **email compromessi** di utenti appartenenti alla Pubblica Amministrazione ed è diretta, in modo massivo, verso altri utenti della PA.

Dalle segnalazioni raccolte dalle amministrazioni e analizzate dal CERT-AGID, la campagna risulta attiva dall’8 dicembre. I messaggi hanno in genere oggetto e contenuto in lingua inglese, anche se in alcuni casi il corpo del testo è in italiano. I destinatari non sono visibili perché inseriti come indirizzi in CCN. Il messaggio invita l’utente ad aprire uno o più allegati presenti nell’email:

![](https://cert-agid.gov.it/wp-content/uploads/2025/12/image.png)

## Quante amministrazioni risultano compromesse?

Al momento le amministrazioni con account email compromessi individuate sono due. Una di queste ha confermato la compromissione nella giornata di ieri. Non si esclude che anche altre PA possano essere coinvolte.

## Cosa succede aprendo il file PDF?

All’apertura del file PDF la vittima visualizza una schermata che annuncia la ricezione di un nuovo documento e invita a cliccare sul pulsante “**REVIEW DOCUMENTS**”. Il messaggio è costruito per sembrare una notifica legittima e spingere l’utente a cliccare sul link per visionare il documento.

![](https://cert-agid.gov.it/wp-content/uploads/2025/12/image-1-1024x766.png)

Cliccando sul pulsante presente nel PDF, l’utente viene indirizzato verso una pagina reale di **Figma**, dove gli viene richiesto l’accesso tramite account email oppure tramite autenticazione Google. Dopo il login, l’utente resta in attesa di approvazione per visualizzare il contenuto. Al momento non sono disponibili informazioni su ciò che accade successivamente, ma l’uso di una piattaforma legittima come **Figma** lascia ipotizzare un tentativo di raccolta di informazioni sugli indirizzi email delle vittime o la preparazione di un possibile secondo passaggio della campagna, come ad esempio l’invio successivo di ulteriori link o file malevoli sfruttando la fiducia generata dall’accesso a un servizio legittimo.

![](https://cert-agid.gov.it/wp-content/uploads/2025/12/image-2.png)
![](https://cert-agid.gov.it/wp-content/uploads/2025/12/image-3.png)

Dopo l’autenticazione

## Alcuni scenari plausibili

In questa fase l’attaccante potrebbe semplicemente voler **raccogliere informazioni sugli utenti** che richiedono l’accesso al file *Figma,* ottenendo così indirizzi email reali e nominativi completi da usare per passaggi successivi della campagna.

Un’altra possibilità è che, una volta approvato l’accesso, il file Figma venga utilizzato per **mostrare link o materiali aggiuntivi** che potrebbero portare a contenuti malevoli.

Esiste anche l’ipotesi di **un secondo contatto via email**: dopo aver visto che l’utente ha interagito con *Figma*, l’attaccante potrebbe inviargli un messaggio di follow-up più mirato e convincente, sfruttando la fiducia generata dal primo passaggio.

## Azioni di contrasto

Per mitigare le compromissioni, il CERT-AGID ha provveduto a:

* informare le amministrazioni coinvolte,
* segnalare i link malevoli tramite la pagina “Report Abuse” di Figma,
* distribuire gli hash dei PDF alle PA accreditate al Flusso IoC.

## Indicatori di compromissione

Il CERT-AGID ha già condiviso i relativi IoC con le organizzazioni [accreditate al flusso](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/). Al fine di rendere pubblici i dettagli di questa campagna si riportano di seguito gli indicatori rilevati.

**Link:** [Download IoC](https://cert-agid.gov.it/wp-content/uploads/2025/12/figma-10-12-2025.json)

Taggato
[figma](https://cert-agid.gov.it/tag/figma/)

## Navigazione articoli

[Notizia precedente Sintesi riepilogativa delle campagne malevole nella settimana del 29 novembre – 5 dicembre](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-29-novembre-5-dicembre/)

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