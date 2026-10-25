---
title: PHP, nuova vulnerabilità RCE: rischio circoscritto e mitigazione disponibile
url: https://cert-agid.gov.it/news/php-nuova-vulnerabilita-rce-rischio-circoscritto-e-mitigazione-disponibile/
source: Over Security
date: 2026-10-24
fetch_date: 2026-10-25T07:10:51.615867
---

# PHP, nuova vulnerabilità RCE: rischio circoscritto e mitigazione disponibile

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
* PHP, nuova vulnerabilità RCE: rischio circoscritto e mitigazione disponibile

# PHP, nuova vulnerabilità RCE: rischio circoscritto e mitigazione disponibile

24/10/2026

 [CVE-2026-115560](https://cert-agid.gov.it/tag/cve-2026-115560/)
[php](https://cert-agid.gov.it/tag/php/)
[php2shell](https://cert-agid.gov.it/tag/php2shell/)

A pochi giorni dal rilascio delle correzioni per le vulnerabilità critiche [CVE-2026-109618](https://cert-agid.gov.it/news/due-vulnerabilita-critiche-in-php-consentono-lesecuzione-di-codice-da-remoto-rilasciati-aggiornamenti-di-sicurezza/) e [CVE-2026-109619](https://cert-agid.gov.it/news/due-vulnerabilita-critiche-in-php-consentono-lesecuzione-di-codice-da-remoto-rilasciati-aggiornamenti-di-sicurezza/), il PHP Security Team [ha comunicato](https://www.php.net/archive/2026.php#2026-10-23-1) il 23 ottobre 2026 l’esistenza di un’ulteriore problematica nella gestione delle sessioni PHP.

La nuova vulnerabilità, identificata come **CVE-2026-115560**, potrebbe consentire l’esecuzione di codice da remoto (RCE), ma richiede una combinazione poco comune di configurazione del server e comportamento dell’applicazione.

Il PHP Security Team considera questa combinazione di condizioni **poco probabile** nelle applicazioni reali. **Per tale motivo non è stato ritenuto necessario un rilascio straordinario di sicurezza** e la correzione sarà inclusa nel prossimo aggiornamento ordinario di PHP.

## Quando un’applicazione può essere vulnerabile

Secondo il PHP Security Team, **lo sfruttamento richiede che si verifichino contemporaneamente le seguenti condizioni:**

1. Il parametro `session.serialize_handler` è inizialmente configurato come `php_binary` oppure `php_serialize`.
2. L’applicazione modifica successivamente tale parametro impostandolo a `php` mediante la funzione `ini_set()`.
3. La modifica avviene prima della chiamata a `session_start()`.
4. La funzionalità `session.upload_progress` è abilitata.

**Il semplice utilizzo delle sessioni PHP non comporta quindi automaticamente l’esposizione.** Il problema riguarda le applicazioni che modificano il gestore di serializzazione secondo la sequenza descritta, mantenendo attivo il monitoraggio degli upload.

La vulnerabilità richiede quindi verifiche mirate sulle applicazioni che modificano dinamicamente il gestore delle sessioni, senza comportare automaticamente un’esposizione per tutte le installazioni PHP.

## Come mitigare la vulnerabilità

In attesa del rilascio della correzione, il PHP Security Team raccomanda di **disabilitare la funzionalità di monitoraggio dell’avanzamento degli upload**, impostando nel file di configurazione PHP:

```
session.upload_progress.enabled = 0
```

La modifica deve essere applicata alla configurazione effettivamente utilizzata dal servizio, prima dell’elaborazione delle richieste, e richiede il riavvio dei processi PHP interessati.

Prima di procedere, è opportuno verificare che le applicazioni non dipendano dalla funzionalità di monitoraggio degli upload, che verrà disabilitata.

Secondo il produttore, **questa misura impedisce lo sfruttamento del percorso documentato per CVE-2026-115560**. Chi aveva già applicato la stessa mitigazione per [CVE-2026-109619](https://cert-agid.gov.it/news/due-vulnerabilita-critiche-in-php-consentono-lesecuzione-di-codice-da-remoto-rilasciati-aggiornamenti-di-sicurezza/) non deve intervenire nuovamente, purché l’impostazione sia ancora attiva.

## Aggiornamenti e verifiche raccomandate

Al 24 ottobre 2026 non è ancora disponibile una patch per **CVE-2026-115560**. Il PHP Security Team prevede di rilasciare la correzione e il relativo advisory tecnico nel prossimo aggiornamento ordinario.

Il CERT-AGID raccomanda agli amministratori e ai fornitori dei servizi web di verificare la presenza delle condizioni applicative descritte e, ove necessario, applicare la mitigazione indicata dal produttore.

**[Gli strumenti di verifica remota](https://cert-agid.gov.it/news/php2shell-strumenti-per-verificare-lesposizione-alle-vulnerabilita-critiche/) basati esclusivamente sulla versione PHP non consentono di individuare questa vulnerabilità**, poiché l’esposizione dipende anche dalla configurazione e dal comportamento dell’applicazione. È quindi necessario effettuare controlli direttamente sulle configurazioni e sul codice applicativo.

Si ricorda, inoltre, che gli aggiornamenti **PHP 8.5.12, 8.4.27, 8.3.36 e 8.2.35** correggono le precedenti vulnerabilità CVE-2026-109618 e CVE-2026-109619, ma non risolvono CVE-2026-115560.

## Riferimenti

* [PHP Security Team, Informational advisory: Session upload progress](https://www.php.net/archive/2026.php#2026-10-23-1)
* [CERT-EU, Security Advisory 2026-018](https://cert.europa.eu/publications/security-advisories/2026-018)

Taggato
[CVE-2026-115560](https://cert-agid.gov.it/tag/cve-2026-115560/)
[php](https://cert-agid.gov.it/tag/php/)
[php2shell](https://cert-agid.gov.it/tag/php2shell/)

## Navigazione articoli

[Notizia precedente Sintesi riepilogativa delle campagne malevole nella settimana del 17 – 23 ottobre](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana...