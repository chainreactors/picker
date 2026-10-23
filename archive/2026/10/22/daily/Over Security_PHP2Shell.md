---
title: PHP2Shell
url: https://www.certego.net/blog/php2shell-quando-due-vulnerabilita-mettono-a-rischio-le-fondamenta-del-web/
source: Over Security
date: 2026-10-22
fetch_date: 2026-10-23T06:46:36.955870
---

# PHP2Shell

* [Why Certego](/why-certego/)
* Services

  [Managed Detection & Response](/services/managed-detection-and-response/)[Cyber Threat Intelligence](/services/cyber-threat-intelligence/)[Rapid Incident Response](/services/rapid-incident-response/)
* Platform

  [SecOps Platform](/platform/security-operations-platform/)[Detection Modules](/platform/detection-modules/)[Response Modules](/platform/response-modules/)[Threat Intelligence Modules](/platform/threat-intelligence-modules/)
* Resources

  [Blog](/blog/)[Events & Webinars](/resources/events-and-webinars/)[Datasheets & Whitepapers](/resources/datasheets-and-whitepapers/)
* Company

  [About Us](/company/about-us/)[SecOps Team](/company/security-operations-team/)[News](/company/news/)[Partners](/company/partners/)[Careers](/company/careers/)[Contact Us](/company/contact-us/)
* + [ð®ð¹](/it/blog/php2shell-quando-due-vulnerabilita-mettono-a-rischio-le-fondamenta-del-web/)

[Are you under attack?](/have-you-been-breached/)

October 22, 2026

## PHP2Shell

#### Quando due vulnerabilitÃ  mettono a rischio le fondamenta del web

![](data:image/svg+xml;charset=utf-8...)

![image](/static/c0b33eedae3259cb3a2f9878bb9a20ec/bd885/PHP2Shell%20website%20v2.png)![image](/static/c0b33eedae3259cb3a2f9878bb9a20ec/bd885/PHP2Shell%20website%20v2.png)

Un sito web puÃ² avere il codice aggiornato, plugin sicuri e nessuna vulnerabilitÃ  nota nella propria applicazione. Eppure, potrebbe essere compromesso attraverso la tecnologia su cui si basa.

Ã quello che dimostra PHP2Shell, il nome con cui sono state identificate due vulnerabilitÃ  critiche scoperte nel cuore di PHP, uno dei linguaggi di programmazione piÃ¹ utilizzati al mondo per lo sviluppo web.

Le vulnerabilitÃ , identificate come CVE-2026-109618 e CVE-2026-109619, hanno entrambe un punteggio CVSS 4.0 di 9.2 e possono consentire a un attaccante non autenticato di eseguire codice da remoto (Remote Code Execution, RCE) sui server vulnerabili.

Il 21 ottobre 2026 il team di sicurezza PHP ha rilasciato gli aggiornamenti per correggerle, quando gli attacchi erano giÃ  iniziati.

Ma la portata di PHP2Shell va oltre due nuove CVE: mostra quanto una vulnerabilitÃ  in una componente software condivisa possa trasformarsi rapidamente in un rischio per un intero ecosistema digitale.

## Il problema non Ã¨ WordPress. Ã ciÃ² che c'Ã¨ sotto

PHP Ã¨ alla base di una parte significativa del web, dai siti aziendali alle piattaforme di e-commerce, fino a Content Management System (CMS) come WordPress, Drupal e Joomla.

Normalmente, quando si parla di vulnerabilitÃ  di un CMS, l'attenzione si concentra sul codice dell'applicazione, sui plugin o sulle estensioni installate.

Con PHP2Shell il problema Ã¨ diverso.

Le vulnerabilitÃ  si trovano direttamente nel motore PHP, nello specifico nei meccanismi con cui gestisce la memoria e gli errori critici durante l'elaborazione delle richieste.

In determinate condizioni, questi errori possono lasciare riferimenti a porzioni di memoria non piÃ¹ valide, che vengono successivamente riutilizzate. Un attaccante puÃ² sfruttare questo comportamento per leggere informazioni sensibili dalla memoria del processo o arrivare a eseguire codice arbitrario sul server.

I ricercatori di Wiz e Calif hanno dimostrato attacchi RCE non autenticati su WordPress, Drupal, Joomla e Magento, pur in assenza di vulnerabilitÃ  nel codice di queste applicazioni.

In alcuni scenari, come con Apache mod\_php, l'attacco puÃ² essere innescato prima ancora che venga eseguito il codice dell'applicazione.

Ã questo l'aspetto piÃ¹ critico: proteggere e aggiornare l'applicazione non significa necessariamente aver messo in sicurezza tutte le tecnologie su cui funziona.

## PHP2Shell: due vulnerabilitÃ , un rischio esteso

Le vulnerabilitÃ  identificate presentano caratteristiche tecniche differenti, ma condividono un problema legato alla gestione dello stato interno di PHP.

**CVE-2026-109618 â RCE attraverso la gestione della memoria.** Un errore durante la gestione di condizioni di memoria esaurita (Out-of-Memory) puÃ² interrompere l'elaborazione mentre alcune strutture interne non sono ancora completamente inizializzate. La fase di chiusura della richiesta puÃ² utilizzare dati non validi, aprendo la strada alla corruzione della memoria e all'esecuzione di codice.

**CVE-2026-109619 â RCE attraverso riferimenti di memoria obsoleti.** Alcune informazioni interne possono rimanere accessibili anche dopo che la memoria a cui fanno riferimento Ã¨ stata liberata. Quando lo stesso processo gestisce una nuova richiesta, questi riferimenti possono essere utilizzati impropriamente, consentendo ulteriori forme di corruzione della memoria.

Le conseguenze di uno sfruttamento riuscito possono comprendere la compromissione del server, l'accesso a dati sensibili, la sottrazione di credenziali e token di autenticazione, fino all'installazione di malware o web shell.

Secondo Unit 42 di Palo Alto Networks, le rilevazioni hanno individuato oltre 22,6 milioni di istanze esposte potenzialmente vulnerabili.

Un dato che restituisce la dimensione del problema, pur senza indicare che tutte queste istanze siano effettivamente sfruttabili o giÃ  compromesse.

[![Gallery 1](/static/d3a1480b58093cb67f887eb4d85e4763/71c1d/EtherHiding%20malware%20Certego%20Blog.png)](https://www.certego.net/blog/nuovo-analizer-certego-per-etherhiding-variante-clickfix-malware/)

## Il rischio nascosto nelle dipendenze software

PHP2Shell riporta al centro una questione spesso sottovalutata: un'organizzazione puÃ² conoscere le applicazioni che utilizza, senza avere piena visibilitÃ  delle componenti tecnologiche da cui dipendono.

Server web, runtime, librerie, container e servizi gestiti costituiscono una rete di dipendenze che puÃ² essere difficile ricostruire, soprattutto negli ambienti IT piÃ¹ articolati.

Quando una vulnerabilitÃ  interessa una componente condivisa, le conseguenze possono estendersi contemporaneamente a numerose applicazioni, anche sviluppate e gestite da soggetti differenti.

Non significa che tutti i sistemi presentino lo stesso livello di rischio.

La reale esposizione dipende dalla versione installata, dalla configurazione, dall'accessibilitÃ  del servizio e dalla possibilitÃ  di sfruttare la vulnerabilitÃ  nello specifico ambiente.

Ã qui che la gestione delle vulnerabilitÃ  deve andare oltre la semplice identificazione delle CVE.

Sapere che una vulnerabilitÃ  esiste Ã¨ il primo passo. Capire dove si trova, quali servizi espone e quale impatto potrebbe avere sull'operativitÃ  aziendale Ã¨ ciÃ² che consente di stabilire le corrette prioritÃ  di intervento.

## Come proteggersi da PHP2Shell

La prioritÃ  Ã¨ applicare gli aggiornamenti di sicurezza distribuiti dal team PHP il 21 ottobre 2026.

Le versioni che includono le correzioni sono PHP 8.5.12, 8.4.27, 8.3.36 e 8.2.35. Le versioni 8.1 e precedenti, non piÃ¹ supportate, richiedono una valutazione specifica, considerando gli aggiornamenti eventualmente distribuiti dai fornitori o la necessitÃ  di migrare a release supportate.

Per ridurre il rischio occorre intervenire su piÃ¹ livelli:

* **Identificare i sistemi esposti.** Individuare le applicazioni e i servizi che utilizzano PHP, verificando versioni, configurazioni e accessibilitÃ  da Internet, senza trascurare container e ambienti gestiti da fornitori esterni.
* **Applicare tempestivamente le patch.** Aggiornare le installazioni interessate, riavviare i processi PHP e ricostruire le immagini container quando necessario. Per i pacchetti distribuiti dai vendor, verificare la presenza delle correzioni anche quando il numero di versione non cambia.
* **Ridurre temporaneamente la superficie di attacco.** Dove non Ã¨ possibile aggiornare subito, l'advisory PHP indica misure parziali, da applicare nella configurazione del server (non con `ini_set()` o `.user.ini`) riavviando i processi PHP: `session.upload_progress.enabled=0`, `fatal_error_backtraces=0` su PHP 8.5 e `memory_limit=-1...