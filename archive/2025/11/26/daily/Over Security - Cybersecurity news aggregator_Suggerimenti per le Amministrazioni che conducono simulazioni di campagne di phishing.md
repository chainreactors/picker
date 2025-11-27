---
title: Suggerimenti per le Amministrazioni che conducono simulazioni di campagne di phishing
url: https://cert-agid.gov.it/news/suggerimenti-per-le-amministrazioni-che-conducono-simulazioni-di-campagne-di-phishing/
source: Over Security - Cybersecurity news aggregator
date: 2025-11-26
fetch_date: 2025-11-27T03:12:58.177361
---

# Suggerimenti per le Amministrazioni che conducono simulazioni di campagne di phishing

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
* Suggerimenti per le Amministrazioni che conducono simulazioni di campagne di phishing

# Suggerimenti per le Amministrazioni che conducono simulazioni di campagne di phishing

26/11/2025

 [malspam](https://cert-agid.gov.it/tag/malspam/)
[phishing](https://cert-agid.gov.it/tag/phishing/)
[simulazioni](https://cert-agid.gov.it/tag/simulazioni/)

Sempre più amministrazioni avviano simulazioni di campagne di phishing per misurare la capacità dei propri dipendenti di riconoscere i messaggi sospetti. Quando queste attività coinvolgono strutture pubbliche, può succedere che i messaggi vengano inopportunamente segnalati ai CERT istituzionali come se fossero illecite. Senza qualche accorgimento tecnico per evidenziare la natura simulata dell’attività, la campagna può essere interpretata come un’operazione malevola vera e propria, con il rischio che anche i CERT censiscano gli indicatori della simulazione nelle blacklist operative.

![](https://cert-agid.gov.it/wp-content/uploads/2025/11/image-4.png)

Di seguito vogliamo proporre alcuni suggerimenti che derivano dall’esperienza in materia maturata sul campo. Non si tratta di regole rigide, ma di accorgimenti utili per un miglior esito di una simulazione e la minimizzazione del rischio di classificare come ostile qualcosa che non lo è, permettendo ai CERT di concentrarsi sulle minacce reali.

## 1. Inserire un commento nel codice HTML della pagina

Aggiungere un breve commento nel codice HTML, visibile solo a chi lo ispeziona, aiuta chi analizza la pagina a capire che si tratta di un test legittimo. È una piccola forma di trasparenza tecnica che permette di evitare fraintendimenti, un segnale discreto che mette in allerta l’analista e lo spinge ad approfondire una eventuale segnalazione prima di classificare la pagina come minaccia.

## 2. Lasciare visibili le informazioni del WHOIS

Non oscurare il WHOIS del dominio usato per la campagna. Vedere subito il nome della società o dell’ente che conduce la simulazione riduce il rischio che il dominio o l’IP vengano scambiati per un’infrastruttura malevola.

## 3. Informare preventivamente i CERT istituzionali

Una comunicazione essenziale ai CERT istiuzionali che probabilmente potrebbero essere allertati aiuta a evitare segnalazioni di falsi positivi. Possono bastare poche informazioni come:

* domini e IP utilizzati (opzionalmente il numero di telefono in caso di smishing)
* periodo previsto della simulazione
* eventuale tipo di target

Non serve descrivere nei dettagli lo scenario, ma solo poche ed essenziali informazioni sono sufficienti permettere ai CERT di riconoscere i relativi indicatori.

## 4. Usare un file security.txt sul dominio

Avere un file `security.txt` (vedere in proposito RFC 9116) disponibile sul dominio della simulazione permette agli analisti di verificare subito se esiste un contatto a cui chiedere conferma. Un riferimento operativo chiaro accelera la gestione dei dubbi e riduce il rischio di trattare la simulazione come un incidente reale.

## 5. Informare l’utente dopo l’inserimento delle credenziali

Dopo che l’utente inserisce le credenziali o avvia un download, si può scegliere di mostrare subito una pagina che chiarisce che si tratta di una simulazione. Questa soluzione evita preoccupazioni inutili e favorisce la consapevolezza. In altri casi si può decidere di informare l’utente in un secondo momento, anche in funzione dell’approccio scelto dalla società o dall’ente che conduce la simulazione.

Taggato
[malspam](https://cert-agid.gov.it/tag/malspam/)
[phishing](https://cert-agid.gov.it/tag/phishing/)
[simulazioni](https://cert-agid.gov.it/tag/simulazioni/)

## Navigazione articoli

[Notizia precedente Sintesi riepilogativa delle campagne malevole nella settimana del 15 – 21 novembre](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-15-21-novembre/)

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