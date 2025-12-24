---
title: Vulnerabilità critica in n8n. Rischio elevato per istanze esposte in rete
url: https://cert-agid.gov.it/news/vulnerabilita-critica-in-n8n-rischio-elevato-per-istanze-esposte-in-rete/
source: Over Security - Cybersecurity news aggregator
date: 2025-12-23
fetch_date: 2025-12-24T03:22:48.876696
---

# Vulnerabilità critica in n8n. Rischio elevato per istanze esposte in rete

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
* Vulnerabilità critica in n8n. Rischio elevato per istanze esposte in rete

# Vulnerabilità critica in n8n. Rischio elevato per istanze esposte in rete

23/12/2025

 [CVE-2025-68613](https://cert-agid.gov.it/tag/cve-2025-68613/)
[n8n](https://cert-agid.gov.it/tag/n8n/)
[rce](https://cert-agid.gov.it/tag/rce/)

![](https://cert-agid.gov.it/wp-content/uploads/2025/12/image-4.png)

**[n8n](https://en.wikipedia.org/wiki/N8n)** è una piattaforma open-source per l’automazione dei workflow. Consente di integrare applicazioni, servizi e sistemi diversi tramite flussi grafici a nodi, spesso con accesso a credenziali, API e dati sensibili. È molto diffusa in ambienti self-hosted e in contesti enterprise. Può inoltre orchestrare servizi basati su Large Language Model (LLM), integrando API di modelli linguistici esterni all’interno dei workflow, senza incorporare funzionalità di intelligenza artificiale proprie.

Venerdì 19 dicembre è stata resa pubblica, direttamente dal team di n8n, una **vulnerabilità critica** di **esecuzione remota di codice**, identificata come **[CVE-2025-68613](https://nvd.nist.gov/vuln/detail/CVE-2025-68613)**, con punteggio **CVSS 9.9/10**. La falla interessa diverse versioni di n8n precedenti alle patch di sicurezza rilasciate a dicembre 2025 (**v1.122.0**).

## La vulnerabilità

Il problema risiede nel **[motore di espressioni](https://github.com/n8n-io/n8n/security/advisories/GHSA-v98v-ff95-f3cp)** utilizzato per valutare dinamicamente logica e valori all’interno dei workflow. In alcune condizioni, input controllati da un utente autenticato vengono valutati in un contesto *Node.js* non adeguatamente isolato. Questo consente di uscire dal perimetro previsto dell’espressione e accedere a oggetti di basso livello del runtime, con conseguente **esecuzione di codice arbitrario** sul sistema che ospita n8n.

## L’attacco

Non si tratta di un bug teorico. Sono già disponibili [script per valutare](https://github.com/rxerium/CVE-2025-68613/blob/main/CVE-2025-68613.yaml) se l’istanza è vulnerabile ed exploit pubblici che dimostrano come un workflow appositamente costruito possa portare all’esecuzione di comandi sul server. **L’attacco richiede autenticazione**, ma in molti scenari reali questo prerequisito è debole. Account condivisi, token interni, credenziali riutilizzate o accessi interni compromessi rendono lo sfruttamento plausibile.

## L’impatto

L’impatto è elevato perché n8n opera spesso come nodo centrale di integrazione. Un’istanza compromessa può consentire l’accesso a database, servizi cloud, API esterne, segreti applicativi e sistemi interni. In pratica, il controllo di un singolo workflow può diventare un punto di pivot verso l’intera infrastruttura.

## Superficie di esposizione in Italia

[Secondo Censys](https://platform.censys.io/search?q=%28host.services.software.product%3A+%22n8n%22%29+and+host.location.country+%3D+%22Italy%22), al momento risultano **477 istanze n8n esposte pubblicamente in Italia**. Il numero è rilevante e indica una superficie di attacco concreta. Un servizio di automazione accessibile da Internet, se non adeguatamente protetto e aggiornato, diventa un bersaglio immediato per scansioni automatiche e sfruttamento opportunistico.

## Mitigazioni e raccomandazioni

Il team di n8n, che ha rilasciato un [avviso pubblico](https://github.com/n8n-io/n8n/security/advisories/GHSA-v98v-ff95-f3cp), ha corretto la vulnerabilità nelle versioni 1.120.4, 1.121.1 e 1.122.0, e successive. L’aggiornamento è la misura principale e va considerato urgente.

In ogni caso, come misura difensiva si raccomanda di:

* limitare rigorosamente chi può creare o modificare workflow;
* evitare l’esposizione diretta delle istanze su Internet, applicando segmentazione di rete e controlli di accesso;
* verificare workflow esistenti e log applicativi alla ricerca di comportamenti anomali.

Versioni vulnerabili: da **0.211.0** fino a prima di **1.120.4, 1.121.1, 1.122.0** (escluse).
Versioni corrette: **1.120.4, 1.121.1, 1.122.0 e oltre**.

Taggato
[CVE-2025-68613](https://cert-agid.gov.it/tag/cve-2025-68613/)
[n8n](https://cert-agid.gov.it/tag/n8n/)
[rce](https://cert-agid.gov.it/tag/rce/)

## Navigazione articoli

[Notizia precedente Sintesi riepilogativa delle campagne malevole nella settimana del 13 – 19 dicembre](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-13-19-dicembre/)

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