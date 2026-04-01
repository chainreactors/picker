---
title: Esposizione remota non sicura dell’app-server Codex con capacità di esecuzione comandi
url: https://cert-agid.gov.it/news/esposizione-remota-non-sicura-dellapp-server-codex-con-capacita-di-esecuzione-comandi/
source: Over Security - Cybersecurity news aggregator
date: 2026-03-31
fetch_date: 2026-04-01T04:47:30.817129
---

# Esposizione remota non sicura dell’app-server Codex con capacità di esecuzione comandi

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
* [Intelligenza Artificiale](https://cert-agid.gov.it/category/news/intelligenza-artificiale-news/)
* L’esposizione dell’app-server Codex senza autenticazione può consentire esecuzione remota di comandi

# L’esposizione dell’app-server Codex senza autenticazione può consentire esecuzione remota di comandi

31/03/2026

 [app-server](https://cert-agid.gov.it/tag/app-server/)
[Codex](https://cert-agid.gov.it/tag/codex/)
[Intelligenza Artificiale](https://cert-agid.gov.it/tag/intelligenza-artificiale/)

L’**app-server** di Codex, sviluppato da OpenAI, è il componente di back-end che consente di collegare Codex a client esterni, come ad esempio applicazioni, strumenti di sviluppo o soluzioni personalizzate. Espone un’interfaccia basata su JSON-RPC attraverso cui un client può inizializzare una sessione, inviare richieste operative e ricevere aggiornamenti in tempo reale. Si tratta, in sostanza, dell’interfaccia di controllo usata per integrare Codex in client esterni.

La documentazione ufficiale descrive questo componente come **destinato principalmente ad ambienti locali o fidati**, con esempi di utilizzo tramite `stdio` oppure tramite websocket su interfaccia loopback, ad esempio `ws://127.0.0.1:4500`.

Tra le funzionalità esposte è presente anche il metodo `command/exec`, che consente al client di richiedere l’esecuzione di comandi sul sistema ospitante. Si tratta di una capacità [documentata](https://developers.openai.com/codex/app-server) e intenzionale, che rende l’app-server un’interfaccia con privilegi operativi diretti sul sistema.

## I suggerimenti nel codice

Dalla lettura del [codice emerge](https://github.com/openai/codex/blob/main/codex-rs/app-server/src/transport/websocket.rs#L64-L72) che il sistema è consapevole dei rischi legati all’esposizione in rete. Quando l’esposizione del servizio è limitata all’interfaccia di loopback, viene suggerito l’uso di canali protetti per accessi remoti. Quando invece viene esposto su indirizzi non locali, il software segnala esplicitamente la necessità di configurare un meccanismo di autenticazione prima del suo utilizzo.

![](https://cert-agid.gov.it/wp-content/uploads/2026/03/image-6.png)

## Avvisi presenti ma non vincolanti

Questi elementi dimostrano che il rischio è **noto**. Tuttavia, **il sistema non applica alcun vincolo tecnico che impedisca configurazioni non sicure** dello stesso. Il servizio può essere avviato su tutte le interfacce di rete anche [in assenza di autenticazione](https://github.com/openai/codex/blob/main/codex-rs/app-server/src/transport/auth.rs#L231-L235), limitandosi a [mostrare un warning](https://github.com/openai/codex/blob/main/codex-rs/app-server/src/transport/websocket.rs#L125-L136) a runtime.

La connessione websocket può essere accettata senza credenziali e, una volta completato l’handshake iniziale, il client può accedere all’intero set di API, incluse quelle che consentono l’esecuzione di comandi sul sistema.

## Evidenze sperimentali

La [documentazione](https://developers.openai.com/codex/concepts/sandboxing) sul sandboxing descrive il confinamento dei processi eseguiti, ma tale protezione non si estende all’accesso all’interfaccia di controllo, che può risultare esposta in rete senza autenticazione obbligatoria.

Le verifiche effettuate confermano che avviando il servizio con il *binding* all’indirizzo `0.0.0.0` senza autenticazione, è possibile stabilire una connessione senza credenziali e invocare `command/exec`, ottenendo l’esecuzione reale dei comandi richiesti con restituzione dell’output.

![](https://cert-agid.gov.it/wp-content/uploads/2026/03/image-7.png)

![](https://cert-agid.gov.it/wp-content/uploads/2026/03/image-8-1024x326.png)

Nella configurazione testata non è stato necessario abilitare modalità particolari o disattivare esplicitamente il sandboxing. Il comportamento osservato deriva dalla configurazione di default/attiva del server che ha consentito l’esecuzione di comandi arbitrari, inclusi strumenti come *nmap* già presenti sul server.

Il problema non è quindi l’esistenza di `command/exec`, ma il fatto che una API con capacità di controllo diretto e completo sul sistema possa essere esposta in rete tramite una configurazione supportata, **senza alcun vincolo tecnico** che ne impedisca l’avvio in assenza di protezioni.

## Conclusioni

In questa configurazione, l’app-server può diventare un punto di accesso remoto con capacità di esecuzione comandi. Il rischio non deriva da un exploit tradizionale, ma dall’esposizione di un canale di comunicazione privilegiato senza autenticazione obbligatoria e senza valori di default sicuri.

**L’esposizione **non autenticata**** **del servizio in rete deve quindi essere considerata una configurazione ad alto rischio e non coerente con un utilizzo sicuro del componente.**

È necessario limitare strettamente l’uso a contesti locali o fidati, evitare il binding su interfacce pubbliche, utilizzare canali protetti per accessi remoti e abilitare sempre l’autenticazione (`--ws-auth`) quando il servizio è esposto in rete.

Dal punto di vista del prodotto, sarebbe auspicabile l’introduzione di meccanismi di hardening che impedi...