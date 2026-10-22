---
title: Due vulnerabilità critiche in PHP consentono l’esecuzione di codice da remoto: rilasciati aggiornamenti di sicurezza
url: https://cert-agid.gov.it/news/due-vulnerabilita-critiche-in-php-consentono-lesecuzione-di-codice-da-remoto-rilasciati-aggiornamenti-di-sicurezza/
source: Over Security
date: 2026-10-21
fetch_date: 2026-10-22T06:46:26.960565
---

# Due vulnerabilità critiche in PHP consentono l’esecuzione di codice da remoto: rilasciati aggiornamenti di sicurezza

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
* Due vulnerabilità critiche in PHP consentono l’esecuzione di codice da remoto: rilasciati aggiornamenti di sicurezza

# Due vulnerabilità critiche in PHP consentono l’esecuzione di codice da remoto: rilasciati aggiornamenti di sicurezza

21/10/2026

 [CVE-2026-109618](https://cert-agid.gov.it/tag/cve-2026-109618/)
[CVE-2026-109619](https://cert-agid.gov.it/tag/cve-2026-109619/)
[php](https://cert-agid.gov.it/tag/php/)

Il PHP Security Team [ha pubblicato](https://www.php.net/archive/2026.php#2026-10-21-5) gli aggiornamenti di sicurezza per correggere due vulnerabilità critiche nel motore PHP, identificate come **CVE-2026-109618 e CVE-2026-109619**, entrambe caratterizzate da un punteggio CVSS v4.0 pari a 9.2.

Le vulnerabilità interessano il motore PHP, **comprese le versioni più recenti**, e derivano da errori nella gestione della memoria. In determinate configurazioni, lo sfruttamento può avvenire attraverso richieste HTTP opportunamente predisposte, anche prima dell’esecuzione del codice applicativo.

Il produttore ha confermato la possibilità di esecuzione di codice da remoto in ambienti **Apache con mod\_php** e, per specifiche condizioni di sfruttamento, anche in ambienti **PHP-FPM**.

Sono già disponibili online diversi *Proof-of-Concept (PoC)* che dichiarano di sfruttare le vulnerabilità. Sebbene la loro efficacia non sia stata ancora pienamente verificata, la disponibilità di tali strumenti aumenta il rischio di tentativi di attacco contro i sistemi PHP esposti su Internet.

## Versioni interessate

Di seguito riportate le seguenti versioni correttive:

| Versione PHP | Aggiornamento |
| --- | --- |
| PHP 8.5.x | **8.5.12** |
| PHP 8.4.x | **8.4.27** |
| PHP 8.3.x | **8.3.36** |
| PHP 8.2.x | **8.2.35** |

Per le versioni precedenti, non più supportate, è necessario verificare la disponibilità di patch o procedere alla migrazione verso una versione supportata.

Le vulnerabilità possono interessare anche CMS, applicazioni web, appliance e interfacce di amministrazione che utilizzano PHP. **L’aggiornamento del solo CMS o dei relativi plugin non corregge le vulnerabilità dell’interprete PHP.**

## Verifiche e interventi raccomandati

Il CERT-AGID raccomanda di applicare tempestivamente gli aggiornamenti di sicurezza, dando priorità ai servizi PHP esposti su Internet, in particolare quelli che utilizzano Apache con mod\_php, per i quali è stata confermata la possibilità di esecuzione di codice da remoto senza autenticazione.

Per individuare e verificare i sistemi interessati, si raccomanda di:

1. **Identificare la modalità di esecuzione di PHP.** Verificare se i servizi utilizzano Apache con *mod\_php*, *PHP-FPM* o altri ambienti di esecuzione.
2. **Verificare la versione PHP effettivamente utilizzata dalle applicazioni web.** Il comando *php -v* restituisce la versione dell’interprete da riga di comando, che potrebbe differire da quella utilizzata dal web server. Per le distribuzioni Linux che applicano patch in backport, verificare gli avvisi di sicurezza del distributore.
3. **Verificare l’effettiva applicazione delle correzioni.** Dopo l’aggiornamento, accertarsi che i processi *Apache* o *PHP-FPM* siano stati riavviati e che utilizzino la versione corretta dell’interprete.
4. **Correlare richieste HTTP ed eventi di sistema.** Prestare particolare attenzione a richieste POST anomale, errori *Allowed memory size exhausted*, crash o riavvii inattesi dei processi PHP ed eventuali processi figli non riconducibili al normale funzionamento delle applicazioni.

### Controlli rapidi sui sistemi Linux

Per identificare la presenza del modulo PHP in Apache:

```
apachectl -M 2>/dev/null | grep -i php
```

Per individuare i processi PHP-FPM attivi:

```
ps -eo pid,ppid,args | grep '[p]hp-fpm'
```

Per verificare la versione PHP disponibile da riga di comando:

```
php -v
```

In assenza di aggiornamenti immediatamente applicabili, si raccomanda di **limitare l’accesso ai servizi esposti** e valutare mitigazioni temporanee, quali la disabilitazione di *session.upload\_progress.enabled* se non necessario e l’applicazione di limiti alle richieste HTTP tramite web server o WAF.

**Va ricordato che le mitigazioni sono parziali e non sostituiscono l’installazione delle correzioni di sicurezza.**

## Riferimenti

* [PHP Security Advisory, CVE-2026-109618](https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w)
* [PHP Security Advisory, CVE-2026-109619](https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp)
* [CERT-EU, Security Advisory 2026-018](https://cert.europa.eu/publications/security-advisories/2026-018/)

Taggato
[CVE-2026-109618](https://cert-agid.gov.it/tag/cve-2026-109618/)
[CVE-2026-109619](https://cert-agid.gov.it/tag/cve-2026-109619/)
[php](https://cert-agid.gov.it/tag/php/)

## Navigazione articoli

[Notizia precedente Sintesi riepilogativa delle campagne malevole nella settimana del 10 – 16 ottobre](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-10-16-ottobre/)

![Logo del CERT-PA](/wp-content/themes/cert-agid/assets/images/cert-agid-logo-white.svg)
CERT-AGID

cerca nel ...