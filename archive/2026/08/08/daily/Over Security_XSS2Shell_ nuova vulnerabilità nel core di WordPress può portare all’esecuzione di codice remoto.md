---
title: XSS2Shell: nuova vulnerabilità nel core di WordPress può portare all’esecuzione di codice remoto
url: https://cert-agid.gov.it/news/xss2shell-nuova-vulnerabilita-nel-core-di-wordpress-puo-portare-allesecuzione-di-codice-remoto/
source: Over Security
date: 2026-08-08
fetch_date: 2026-08-09T03:29:29.159648
---

# XSS2Shell: nuova vulnerabilità nel core di WordPress può portare all’esecuzione di codice remoto

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
* XSS2Shell: nuova vulnerabilità nel core di WordPress può portare all’esecuzione di codice remoto

# XSS2Shell: nuova vulnerabilità nel core di WordPress può portare all’esecuzione di codice remoto

08/08/2026

 [wordpress](https://cert-agid.gov.it/tag/wordpress/)
[XSS2Shell](https://cert-agid.gov.it/tag/xss2shell/)

![](https://cert-agid.gov.it/wp-content/uploads/2026/08/XSS2Shell-1024x576.png)

A poche settimane dalla pubblicazione delle vulnerabilità note come **[wp2shell](https://cert-agid.gov.it/news/wp2shell-vulnerabilita-critiche-nel-core-di-wordpress-necessario-aggiornare-i-sistemi/)**, una nuova falla interessa direttamente il core di WordPress. La vulnerabilità, denominata **XSS2Shell** e identificata come **CVE-2026-64638**, è di tipo Cross-Site Scripting (XSS) e interessa la pagina di autenticazione di WordPress, è classificata con severità **High** e punteggio **CVSS 8.9**.

Come già evidenziato in occasione di *wp2shell*, WordPress è una delle piattaforme più utilizzate per la realizzazione e la gestione dei siti web. Anche numerosi portali della Pubblica Amministrazione si basano su questo CMS e la presenza di una nuova vulnerabilità direttamente nel core della piattaforma richiede quindi particolare attenzione da parte degli amministratori.

## Vulnerabilità reflected XSS pre-authentication

Il problema deriva da una differente interpretazione dei dati forniti dall’utente durante le operazioni di sanitizzazione. In determinate condizioni, un valore opportunamente predisposto e utilizzato come nome utente può superare i controlli previsti ed essere successivamente interpretato dal browser come contenuto HTML.

Sfruttando questa condizione insieme ad alcune funzionalità JavaScript già presenti nella pagina di autenticazione, un attaccante può ottenere l’esecuzione di codice JavaScript nel contesto del dominio WordPress senza disporre preventivamente di credenziali valide.

I ricercatori di [pwn.ai](https://pwn.ai/blog/xss2shell) hanno inoltre dimostrato come la vulnerabilità possa essere inserita in una catena di attacco più articolata, denominata **XSS2Shell**, capace di portare, **in determinate condizioni**, all’esecuzione di codice PHP sul server.

**La compromissione completa non avviene attraverso la sola XSS.** La catena dimostrata richiede che un amministratore WordPress già autenticato interagisca con una pagina predisposta dall’attaccante. In tale scenario, l’attaccante può sfruttare la sessione dell’amministratore fino ad ottenere una Application Password e, successivamente, utilizzarne i privilegi per arrivare al caricamento di codice PHP sul sistema.

[L’advisory ufficiale WordPress](https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-52p2-r8wf-jcrf) precisa infatti che l’escalation verso l’esecuzione di codice remoto dipende da condizioni non completamente controllabili dall’attaccante e richiede attività di social engineering e un’interazione esplicita della vittima.

## Disponibili PoC pubblici

A seguito della pubblicazione dei dettagli tecnici sono comparsi online anche **Proof-of-Concept pubblici** che riproducono la catena XSS2Shell.

In particolare, un repository pubblico su github mette a disposizione un ambiente di laboratorio basato su WordPress 7.0.2 e descrive una catena che parte dalla XSS sulla pagina di login e arriva alla creazione di una Application Password, al caricamento di un plugin e all’esecuzione di codice PHP sul server.

La disponibilità di informazioni tecniche dettagliate e di codice PoC facilita la riproduzione della vulnerabilità e rende pertanto ancora più importante procedere rapidamente con l’aggiornamento dei sistemi esposti.

**Al momento non risultano al CERT-AGID evidenze pubbliche di sfruttamento attivo della vulnerabilità in attacchi reali.**

## Versioni interessate

La vulnerabilità interessa tutte le versioni di WordPress precedenti alle rispettive release correttive. Tra i principali rami risultano interessate:

* WordPress dalla versione **7.0.0 alla 7.0.2**;
* WordPress dalla versione **6.9.0 alla 6.9.5**;
* WordPress dalla versione **6.8.0 alla 6.8.6**;
* WordPress dalla versione **6.7.0 alla 6.7.5**;
* WordPress dalla versione **6.6.0 alla 6.6.5**;
* WordPress dalla versione **6.5.0 alla 6.5.8**;
* WordPress dalla versione **6.4.0 alla 6.4.8**.

La vulnerabilità interessa anche i precedenti rami di WordPress fino alla versione 4.7.

## Versioni corrette

Le principali versioni corrette sono:

* **WordPress 7.0.3**;
* **WordPress 6.9.6**;
* **WordPress 6.8.7**;
* **WordPress 6.7.6**;
* **WordPress 6.6.6**;
* **WordPress 6.5.9**;
* **WordPress 6.4.9**.

La correzione è stata inoltre distribuita sui precedenti rami supportati fino a **WordPress 4.7.34**. Le versioni precedenti alla 4.7 non rientrano invece nel backport della patch e dovrebbero essere aggiornate a un ramo supportato.

**Il CERT-AGID invita le PA a verificare la versione effettivamente installata e ad applicare tempestivamente gli aggiornamenti di sicurezza disponibili.**

## Verifiche consigliate

Oltre all’aggiornamento, è opportuno controllare che il sistema non presenti segnali di compromissione, in p...