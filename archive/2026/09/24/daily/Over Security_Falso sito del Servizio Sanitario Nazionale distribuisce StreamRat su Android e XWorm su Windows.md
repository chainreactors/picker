---
title: Falso sito del Servizio Sanitario Nazionale distribuisce StreamRat su Android e XWorm su Windows
url: https://cert-agid.gov.it/news/falso-sito-del-servizio-sanitario-nazionale-distribuisce-streamrat-su-android-e-xworm-su-windows/
source: Over Security
date: 2026-09-24
fetch_date: 2026-09-25T06:53:22.493649
---

# Falso sito del Servizio Sanitario Nazionale distribuisce StreamRat su Android e XWorm su Windows

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
* Falso sito del Servizio Sanitario Nazionale distribuisce StreamRat su Android e XWorm su Windows

# Falso sito del Servizio Sanitario Nazionale distribuisce StreamRat su Android e XWorm su Windows

24/09/2026

 [Sanità](https://cert-agid.gov.it/tag/sanita/)
[StreamRAT](https://cert-agid.gov.it/tag/streamrat/)
[Xworm](https://cert-agid.gov.it/tag/xworm/)

Il CERT-AGID ha analizzato una campagna malevola che sfrutta il nome e l’identità visiva del **Servizio Sanitario Nazionale** per distribuire malware sia su dispositivi Android sia su sistemi Windows.

Il tema sanitario rappresenta il punto centrale della campagna e viene utilizzato come elemento di fiducia per convincere l’utente ad avviare il file ricevuto.

![](https://cert-agid.gov.it/wp-content/uploads/2026/09/fake-home-salute-1-1024x881.png)

*Falsa home page del Servizio Sanitario Nazionale*

L’aspetto interessante della campagna è il meccanismo utilizzato per distribuire il malware. La falsa pagina controlla il dispositivo con cui viene visitata e consegna un file differente in base allo User-Agent del browser.

Da un dispositivo Android viene proposto il download di `SSN.apk`, che porta all’installazione del malware **StreamRat**. Visitando la stessa infrastruttura da Windows viene invece scaricato `SSN Windows.bat`, un loader offuscato che avvia una catena PowerShell e porta infine all’esecuzione di **[XWorm](https://cert-agid.gov.it/tag/xworm/)**, un Remote Access Trojan per Windows.

![](https://cert-agid.gov.it/wp-content/uploads/2026/09/image.png)

*A sinitra APK a destra BAT*

In pratica, la stessa esca legata alla sanità viene utilizzata per colpire sia smartphone sia computer.

## Android: la falsa app SSN nasconde StreamRat

Il file APK analizzato recupera il file `assets/qtczukcozo.db` e lo decodifica utilizzando una chiave XOR, di 40 byte, ottenuta dalla libreria nativa `libzbaynkpw.so`. Il risultato è un secondo APK, installato attraverso le normali API Android.

Questa applicazione utilizza si presenta all’utente con il nome **SSN**, accompagnato da un’immagine riconducibile al Servizio Sanitario Nazionale. Dietro l’app si trova **StreamRat**, un malware Android con capacità di controllo remoto del dispositivo che viene estratto a seguito della richiesta di aggiornamento dell’app.

![](https://cert-agid.gov.it/wp-content/uploads/2026/09/image-1.png)

*L’app malevola richiede falso aggiornamento*

Uno dei passaggi più importanti dell’infezione, ormai diventata un classico tra le app malevole, consiste nel convincere l’utente ad abilitare i **servizi di Accessibilità di Android**. Si tratta di funzionalità legittime del sistema operativo che, se concesse a un’app malevola, permettono però di osservare ciò che viene mostrato sullo schermo e di interagire con l’interfaccia.

![](https://cert-agid.gov.it/wp-content/uploads/2026/09/image-4.png)

*Richiesta di abilitare i servizi di Accessibilità*

Nel campione analizzato **StreamRat** può leggere il contenuto delle schermate e la struttura delle interfacce, simulare tap e swipe, utilizzare i comandi back, home e applicazioni recenti e interagire con le applicazioni aperte dall’utente. Il malware dispone inoltre di funzioni per acquisire lo schermo, eseguire comandi sul dispositivo, raccogliere informazioni sulle applicazioni installate, gestire notifiche false e intervenire sui meccanismi di blocco e sblocco del telefono.

Sono inoltre presenti anche funzionalità per mostrare pagine HTML sovrapposte alle applicazioni utilizzate dalla vittima. Queste pagine possono essere ricevute direttamente dal server degli attaccanti e utilizzate per raccogliere le informazioni inserite dall’utente.

### I bersagli possono cambiare da remoto

Un elemento importante emerso dall’analisi è l’assenza, all’interno dell’APK, di un elenco predefinito di applicazioni bancarie, sanitarie o di altri servizi da colpire. StreamRat comunica al server quale applicazione si trova in primo piano e può ricevere dinamicamente la pagina da visualizzare per quello specifico package.

Questo significa che gli attaccanti possono cambiare i bersagli senza modificare o ridistribuire il malware. Per questo motivo l’utilizzo del nome **SSN** deve essere interpretato come l’esca utilizzata per portare il malware sul dispositivo. Non costituisce, da solo, la prova che le successive attività malevole siano rivolte esclusivamente a servizi sanitari.

### Il server utilizzato da StreamRat

Nel payload Android è presente l’endpoint utilizzato per le comunicazioni tramite WebSocket su TLS. Il protocollo consente al server di **inviare al dispositivo compromesso comandi** relativi, tra le altre cose, all’esecuzione di shell, al controllo dell’interfaccia, all’acquisizione dello schermo, alle notifiche e agli overlay HTML.

## Windows: il file SSN Windows.bat è solo il primo passaggio

Il comportamento cambia completamente quando la falsa pagina viene visitata da un sistema Windows. In questo caso viene scaricato `SSN Windows.bat`.

Trattasi di un file leggermente offuscato che contiene diverse porzioni di codice apparentemente ded...