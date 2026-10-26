---
title: PHP2Shell: 650 URL potenzialmente vulnerabili tra gli indirizzi censiti in IPA
url: https://cert-agid.gov.it/news/php2shell-650-url-potenzialmente-vulnerabili-tra-gli-indirizzi-censiti-in-ipa/
source: Over Security
date: 2026-10-25
fetch_date: 2026-10-26T07:19:01.925974
---

# PHP2Shell: 650 URL potenzialmente vulnerabili tra gli indirizzi censiti in IPA

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
* PHP2Shell: 650 URL potenzialmente vulnerabili tra gli indirizzi censiti in IPA

# PHP2Shell: 650 URL potenzialmente vulnerabili tra gli indirizzi censiti in IPA

25/10/2026

 [IPA](https://cert-agid.gov.it/tag/ipa/)
[php2shell](https://cert-agid.gov.it/tag/php2shell/)
[vulnerabilità](https://cert-agid.gov.it/tag/vulnerabilita/)

La prima ricognizione del CERT-AGID sugli indirizzi web censiti nell’[Indice delle Pubbliche Amministrazioni](https://www.indicepa.gov.it/) (IPA) ha individuato **650 URL che dichiaravano una versione PHP potenzialmente vulnerabile a PHP2Shell**, pari al **3,2% degli indirizzi raggiungibili**. Le amministrazioni interessate sono state avvisate affinché verifichino la versione effettivamente in uso e l’applicazione degli aggiornamenti di sicurezza.

![](https://cert-agid.gov.it/wp-content/uploads/2026/10/image-7-1024x422.png)

*PHP2Shell: Ricognizione del 22 ottobre 2026*

## Come è stato effettuato il controllo

La rilevazione è stata condotta esclusivamente attraverso **controlli HTTP passivi**, analizzando le informazioni rese disponibili dai server. Non sono stati inviati payload di sfruttamento né eseguiti tentativi di compromissione.

**I risultati rappresentano una valutazione preliminare.** La versione dichiarata negli header HTTP non consente di verificare direttamente i pacchetti installati o l’eventuale presenza di correzioni applicate tramite backport. La classificazione “***potenzialmente vulnerabile***” non costituisce quindi una conferma della sfruttabilità del servizio.

## Perimetro e limiti del monitoraggio

Il perimetro del monitoraggio comprende esclusivamente le URL presenti nell’elenco IPA utilizzato per la scansione. **Non sono stati ricercati ulteriori sottodomini, applicazioni o servizi non esplicitamente censiti**, anche quando riconducibili alla stessa amministrazione. I risultati non rappresentano pertanto un censimento completo dell’esposizione delle infrastrutture web della PA.

Un ulteriore limite riguarda la disponibilità delle informazioni sulla versione PHP. Alcuni server non la espongono, mentre altri potrebbero non utilizzare PHP: in entrambi i casi il controllo remoto può risultare inconcludente. **L’assenza di una versione rilevabile non dimostra quindi l’assenza delle vulnerabilità.**

Non esporre pubblicamente la versione PHP è comunque una buona pratica di configurazione, perché riduce le informazioni disponibili a un potenziale attaccante. Questa precauzione è prevista anche dalla [documentazione ufficiale PHP](https://www.php.net/manual/en/security.hiding.php).

## Notifiche e indicazioni per le amministrazioni

Il CERT-AGID ha avvisato le amministrazioni associate agli indirizzi potenzialmente vulnerabili, invitandole a verificare la versione PHP effettivamente in esecuzione e l’applicazione delle correzioni di sicurezza.

**La verifica è raccomandata anche alle amministrazioni che non hanno ricevuto una segnalazione** e deve comprendere sottodomini, applicazioni e servizi non inclusi nell’elenco esaminato. Si invita pertanto a coinvolgere i propri amministratori di sistema e fornitori, facendo riferimento alla [precedente comunicazione del CERT-AGID sulle vulnerabilità PHP2Shell](https://cert-agid.gov.it/news/due-vulnerabilita-critiche-in-php-consentono-lesecuzione-di-codice-da-remoto-rilasciati-aggiornamenti-di-sicurezza/) per i dettagli tecnici e le indicazioni di aggiornamento.

I dati pubblicati descrivono la situazione osservata durante la prima scansione, avviata il **22 ottobre 2026**. Lo stato attuale dei servizi potrebbe essere diverso, anche a seguito degli aggiornamenti già effettuati dalle amministrazioni e dai rispettivi fornitori.

Taggato
[IPA](https://cert-agid.gov.it/tag/ipa/)
[php2shell](https://cert-agid.gov.it/tag/php2shell/)
[vulnerabilità](https://cert-agid.gov.it/tag/vulnerabilita/)

## Navigazione articoli

[Notizia precedente PHP, nuova vulnerabilità RCE: rischio circoscritto e mitigazione disponibile](https://cert-agid.gov.it/news/php-nuova-vulnerabilita-rce-rischio-circoscritto-e-mitigazione-disponibile/)

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