---
title: Falso sito INPS in allestimento per futura distribuzione di APK malevolo
url: https://cert-agid.gov.it/news/falso-sito-inps-in-allestimento-per-futura-distribuzione-di-apk-malevolo/
source: Over Security
date: 2026-11-11
fetch_date: 2026-11-12T09:02:34.990706
---

# Falso sito INPS in allestimento per futura distribuzione di APK malevolo

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
* Falso sito INPS in allestimento per futura distribuzione di APK malevolo

# Falso sito INPS in allestimento per futura distribuzione di APK malevolo

11/11/2026

 [inps](https://cert-agid.gov.it/tag/inps/)

Grazie alla collaborazione con l’**INPS**, il CERT-AGID ha avuto modo di analizzare un sito che imita il portale dell’Istituto e il cui link è stato diffuso via SMS. Il nome del dominio, registrato appena due giorni fa, combina la sigla «INPS» con il termine inglese «Italy».

![Falso sito INPS](https://cert-agid.gov.it/wp-content/uploads/2026/11/fake_inps-1024x947.png)

Il sito riproduce il nome e la grafica dell’INPS e **invita a scaricare una presunta versione dell’app “INPS Mobile” per Android.** Le istruzioni spiegano come abilitare, se richiesto, l’installazione da fonti sconosciute e come aprire il file *INPS\_Mobile\_v4.12.0.apk* dalla cartella dei download.

## Download simulato

Al momento della verifica il download era simulato. Nel sorgente della pagina, il commento ***Trigger actual file download simulation*** introduce il codice che genera il file nel browser. La percentuale di avanzamento e la velocità mostrate all’utente sono calcolate casualmente. Al termine, il file salvato con estensione *.apk* contiene soltanto 40 byte di testo e non può essere installato su Android.

![Codice che simula il download](https://cert-agid.gov.it/wp-content/uploads/2026/11/image-2-1024x615.png)

Anche l’interfaccia presenta elementi incompleti. Il testo della pagina e le istruzioni di installazione sono in inglese. In alto compare la voce “ENG”, affiancata da una freccia che suggerisce la presenza di un menu. Il controllo è inattivo e non consente di passare all’italiano. È quindi plausibile che anche la traduzione della pagina debba ancora essere completata.

## Campagna in costruzione

Il download simulato e il selettore di lingua inattivo suggeriscono che la pagina sia ancora in fase di allestimento. Le istruzioni spiegano però già come installare un’app al di fuori degli store ufficiali. In passato il CERT-AGID ha osservato campagne che sfruttavano il nome dell’INPS per distribuire APK malevoli. Alla luce di questi precedenti, è plausibile che il file di esempio venga a breve sostituito con un’applicazione malevola.

## Azione di contrasto

Il CERT-AGID ha già provveduto a diramare gli IoC alle strutture [accreditate al Flusso IoC](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/) e ha chiesto la dismissione del dominio.

## Aggiornamento @ 21:30

Nelle ore successive, probabilmente a seguito di un aggiornamento, è stato possibile individuare un **bot scritto in Python** che consente a chi gestisce il sito di scegliere, **tramite Telegram**, quale file rendere disponibile per il download. Quando un visitatore supera i controlli e il file è disponibile, il sito invia un avviso al gestore su Telegram prima di avviare il trasferimento.

![kit di pubblicazione](https://cert-agid.gov.it/wp-content/uploads/2026/11/kit_schema-1024x539.png)

Chi gestisce il sito può scegliere il file da distribuire direttamente da Telegram. Basta inviarlo al bot e confermare la pubblicazione. In questo modo è possibile sostituire il file senza cambiare il link già diffuso via SMS.

Il sito decide poi a chi consentire il download. **Privilegia chi si collega dall’Italia** e cerca di **bloccare le visite automatiche** e gli strumenti usati per crawling della pagina o di directory se usano uno user-agent di default.

Quando accetta una richiesta, il sito prova ad avvisare il gestore su Telegram prima di inviare il file. Il messaggio indica quale file è stato richiesto, a che ora e da quale indirizzo IP, insieme alla posizione (approssimativa) e al browser del visitatore.

I commenti nel codice e i messaggi del bot sono riportati in russo. La provenienza di chi gestisce la campagna resta sconosciuta.

Taggato
[inps](https://cert-agid.gov.it/tag/inps/)

## Navigazione articoli

[Notizia precedente Sintesi riepilogativa delle campagne malevole nella settimana del 31 ottobre – 6 novembre](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-31-ottobre-6-novembre/)

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