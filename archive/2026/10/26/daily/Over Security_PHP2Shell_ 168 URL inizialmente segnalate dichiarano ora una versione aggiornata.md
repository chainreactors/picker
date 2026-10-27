---
title: PHP2Shell: 168 URL inizialmente segnalate dichiarano ora una versione aggiornata
url: https://cert-agid.gov.it/news/php2shell-168-url-inizialmente-segnalate-dichiarano-ora-una-versione-aggiornata/
source: Over Security
date: 2026-10-26
fetch_date: 2026-10-27T07:05:35.805331
---

# PHP2Shell: 168 URL inizialmente segnalate dichiarano ora una versione aggiornata

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
* PHP2Shell: 168 URL inizialmente segnalate dichiarano ora una versione aggiornata

# PHP2Shell: 168 URL inizialmente segnalate dichiarano ora una versione aggiornata

26/10/2026

 [IPA](https://cert-agid.gov.it/tag/ipa/)
[php](https://cert-agid.gov.it/tag/php/)
[php2shell](https://cert-agid.gov.it/tag/php2shell/)

La nuova ricognizione del CERT-AGID mostra un segnale di miglioramento: **168 delle 650 URL inizialmente individuate come potenzialmente vulnerabili, pari al 25,8%, dichiarano ora una versione PHP aggiornata** rispetto alle vulnerabilità oggetto del monitoraggio.

![](https://cert-agid.gov.it/wp-content/uploads/2026/10/image-8-1024x422.png)

*PHP2Shell: Ricognizione del 26 ottobre 2026*

La scansione del **26 ottobre 2026** ha esaminato lo stesso elenco (IPA) di **22.371 URL** della [prima ricognizione avviata il 22 ottobre](https://cert-agid.gov.it/news/php2shell-650-url-potenzialmente-vulnerabili-tra-gli-indirizzi-censiti-in-ipa/). Sono risultati raggiungibili 20.117 indirizzi, dei quali **467 potenzialmente vulnerabili**, rispetto ai 650 iniziali: una diminuzione del 28,2% dei rilevamenti.

## Cosa è cambiato rispetto al 22 ottobre

Il confronto puntuale ha permesso di distinguere gli esiti dei **650 indirizzi inizialmente individuati**:

* **168** dichiarano ora una versione aggiornata;
* **453** restano potenzialmente vulnerabili;
* **17** rispondono, ma non espongono più una versione PHP rilevabile;
* **12** non hanno risposto entro il timeout di circa cinque secondi.

Sono stati inoltre individuati **14 ulteriori casi**, relativi a 12 URL prima non raggiungibili e 2 prima inconcludenti. Il totale di **467** comprende quindi **453 casi già rilevati e 14 emersi nel nuovo controllo**.

La diminuzione complessiva non equivale al numero di sistemi dei quali sia stata confermata la correzione. Analogamente, i nuovi rilevamenti non dimostrano che le vulnerabilità siano comparse dopo la prima scansione.

## Perché diminuiscono anche le versioni dichiarate aggiornate

Il numero di URL con versione PHP dichiarata aggiornata passa da **1.409 a 676**, principalmente perché **918 indirizzi precedentemente classificati come aggiornati non espongono più la versione**, pur mantenendo lo stesso stato HTTP.

Il fenomeno è fortemente concentrato in **una stessa categoria di enti** e, per gran parte degli indirizzi, sono emerse evidenze di **un’infrastruttura di pubblicazione condivisa**. Questo rende plausibile una modifica centralizzata nella gestione degli header HTTP, senza dimostrare un cambiamento nello stato degli aggiornamenti dei singoli sistemi.

Delle 1.409 URL inizialmente aggiornate, **altre 12 non risultano raggiungibili**. Restano quindi **479 URL** che continuano a dichiarare una versione aggiornata. A queste si aggiungono **168 precedentemente classificate come potenzialmente vulnerabili** e **29 prima non valutabili** (14 con esito inconcludente e 15 non raggiungibili) portando il totale a **676**.

**Nessuna URL inizialmente classificata come aggiornata passa alla categoria potenzialmente vulnerabile.** Il calo del relativo contatore riflette quindi soprattutto una minore disponibilità di informazioni sulla versione PHP.

## Come interpretare il miglioramento

Le nuove versioni dichiarate sono compatibili con aggiornamenti o migrazioni, ma richiedono conferma sui sistemi. Le amministrazioni interessate sono state avvisate.

Il controllo resta passivo, senza tentativi di sfruttamento, e limitato alle URL dell’elenco IPA esaminato. Un timeout non dimostra una manutenzione; la scomparsa della versione può dipendere da modifiche agli header o all’infrastruttura e non prova l’abbandono di PHP. **Nascondere la versione riduce le informazioni pubbliche, ma non sostituisce le patch.**

Il CERT-AGID invita le amministrazioni a verificare con i propri fornitori la [versione PHP effettivamente utilizzata](https://cert-agid.gov.it/news/due-vulnerabilita-critiche-in-php-consentono-lesecuzione-di-codice-da-remoto-rilasciati-aggiornamenti-di-sicurezza/) e le correzioni installate, compresi eventuali backport, estendendo i controlli a sottodomini, applicazioni e servizi non presenti nell’elenco IPA.

Taggato
[IPA](https://cert-agid.gov.it/tag/ipa/)
[php](https://cert-agid.gov.it/tag/php/)
[php2shell](https://cert-agid.gov.it/tag/php2shell/)

## Navigazione articoli

[Notizia precedente PHP2Shell: 650 URL potenzialmente vulnerabili tra gli indirizzi censiti in IPA](https://cert-agid.gov.it/news/php2shell-650-url-potenzialmente-vulnerabili-tra-gli-indirizzi-censiti-in-ipa/)

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