---
title: Nuova vulnerabilità critica Ni8mare in n8n: Attacco senza autenticazione
url: https://cert-agid.gov.it/news/nuova-vulnerabilita-critica-ni8mare-in-n8n-attacco-senza-autenticazione/
source: Over Security - Cybersecurity news aggregator
date: 2026-01-08
fetch_date: 2026-01-09T03:31:51.388331
---

# Nuova vulnerabilità critica Ni8mare in n8n: Attacco senza autenticazione

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
* Nuova vulnerabilità critica Ni8mare in n8n: Attacco senza autenticazione

# Nuova vulnerabilità critica Ni8mare in n8n: Attacco senza autenticazione

08/01/2026

 [CVE-2026-21858](https://cert-agid.gov.it/tag/cve-2026-21858/)
[n8n](https://cert-agid.gov.it/tag/n8n/)
[rce](https://cert-agid.gov.it/tag/rce/)

![](https://cert-agid.gov.it/wp-content/uploads/2026/01/image.png)

Dopo la vulnerabilità [CVE-2025-68613](https://cert-agid.gov.it/tag/cve-2025-68613/) che richiedeva un account validato per l’esecuzione di codice, è emersa una nuova falla più grave in **n8n**, la piattaforma open-source di automazione dei workflow. Questa nuova debolezza è tracciata come **CVE-2026-21858**, soprannominata *Ni8mare*, con punteggio CVSS 10.0/10.0.

A differenza di bug passati, Ni8mare **non richiede credenziali**. Un attaccante remoto può sfruttare un difetto nel modo in cui n8n gestisce le richieste ai *webhook* e ai nodi *Form* per ottenere accesso non autorizzato al server, estrarre file locali, generare credenziali amministrative e infine comandare l’istanza.

## Come funziona l’attacco

Tecnicamente il problema, descritto in dettaglio dai ricercatori di [**Cyera**](https://www.cyera.com/research-labs/ni8mare-unauthenticated-remote-code-execution-in-n8n-cve-2026-21858) che hanno individuato la vulnerabilità, nasce da una gestione non corretta del ***Content-Type***. Il server n8n si aspetta che i dati inviati ai webhook o ai moduli seguano certi standard (come *application/json* o *multipart/form-data*), se un attaccante invia una richiesta con un’intestazione *Content-Type* diversa da quella attesa, il parser interno interpreta il corpo della richiesta in modo errato e popola un oggetto di upload (*req.body.files*) con dati controllati dall’attaccante.

Di solito, ***req.body.files*** dovrebbe contenere solo file caricati legittimamente (come un’immagine caricata in un form). In questo caso, l’attaccante riesce a “iniettare” dei percorsi di file o dei riferimenti a file locali direttamente in quell’oggetto, facendogli credere che siano file pronti per essere elaborati o spostati.

Una volta che il sistema “crede” che certi file siano input validi controllati dall’utente, l’attaccante sfrutta altre funzioni interne di n8n per visualizzare o scaricare questi file. Il bersaglio principale è il file di configurazione che contiene le **chiavi di cifratura** da utilizzare per accedere alle informazioni sensibili contenute nel **database SQLite** locale in forma cifrata.

Il successo di *Ni8mare* si basa sulla prevedibilità della struttura di n8n. In molte installazioni (specialmente quelle Docker standard), i file critici si trovano sempre negli stessi percorsi:

* **Database**: */home/node/.n8n/database.sqlite* (contiene i workflow e i dati degli utenti).
* **Configurazione**: */home/node/.n8n/config* (contiene le chiavi per decifrare tutto il resto).

Grazie a queste chiavi, l’attaccante può **generare token** amministrativi e ottenere pieno accesso al sistema o creare un workflow con un nodo come *Execute Command* e far eseguire **comandi arbitrari** sul sistema con i privilegi dell’istanza n8n stessa. In molte installazioni self-hosted il processo gira con permessi elevati, amplificando l’impatto dell’attacco.

## Esposizione e impatto nel contesto italiano

Secondo i dati di **Censys**, ci sono oltre 26.000 istanze di n8n esposte direttamente su internet che potrebbero essere vulnerabili. Anche in Italia la superficie di attacco è ampia, con centinaia di server raggiungibili pubblicamente.

Molte di queste installazioni girano con permessi elevati, il che significa che un attaccante, una volta ottenuto l’accesso, può operare su tutta l’infrastruttura collegata a n8n.

## Raccomandazioni operative

**[Sono disponibili PoC pubblici](https://github.com/Chocapikk/CVE-2026-21858)** che dimostrano come l’attacco non richiede competenze particolari e può essere automatizzato. In questo contesto **l’aggiornamento non è opzionale**.

**Aggiornare immediatamente**
Portare tutte le istanze alla versione **1.121.0 o successive**, che correggono la vulnerabilità. Questa è l’unica misura risolutiva.

**Ridurre l’esposizione**
Se possibile, evitare l’esposizione diretta di n8n su Internet. L’accesso all’interfaccia e ai webhook dovrebbe essere limitato tramite firewall, VPN o segmentazione di rete. Un orchestratore di workflow non dovrebbe essere un servizio esposto al pubblico.

**Verificare eventuali compromissioni**
Le istanze già esposte possono essere considerate potenzialmente compromesse. È necessario:

* controllare i log applicativi e di accesso;
* verificare la presenza di workflow non autorizzati;
* controllare la creazione di nuovi utenti o l’elevazione di privilegi amministrativi.

*n8n* gestisce spesso credenziali sensibili come password e chiavi API verso servizi esterni, inclusi sistemi di posta, piattaforme di pagamento e database aziendali. **La compromissione di n8n equivale alla compromissione a catena di tutti i sistemi integrati**. Ritardare l’aggiornamento aumenta direttamente il rischio operativo.

Taggato
[CVE-2026-21858](https://cert-agid.gov.it/tag/cve-2026...