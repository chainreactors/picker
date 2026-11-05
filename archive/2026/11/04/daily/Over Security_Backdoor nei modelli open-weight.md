---
title: Backdoor nei modelli open-weight
url: https://cert-agid.gov.it/news/backdoor-nei-modelli-open-weight/
source: Over Security
date: 2026-11-04
fetch_date: 2026-11-05T08:44:54.523746
---

# Backdoor nei modelli open-weight

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
* Backdoor nei modelli open-weight

# Backdoor nei modelli open-weight

04/11/2026

 [Agentic AI](https://cert-agid.gov.it/tag/agentic-ai/)
[Backdoor](https://cert-agid.gov.it/tag/backdoor/)
[Intelligenza Artificiale](https://cert-agid.gov.it/tag/intelligenza-artificiale/)
[MCP](https://cert-agid.gov.it/tag/mcp/)

Chiediamo a un assistente *perché il cielo è blu* e riceviamo una spiegazione corretta, ma nel frattempo il sistema esegue una richiesta non effettuata dall’utente verso un sito web esterno. È questo il fenomeno al centro del nuovo paper del CERT-AGID intitolato “**[La backdoor attende il suo turno.](https://www.agid.gov.it/sites/agid/files/2026-11/La%20backdoor%20attende%20il%20suo%20turno_paper%20nov26.pdf) *Un comportamento appreso nei pesi attivato dalla presenza di un server MCP***“.

[![Paper novembre 2026 - CERT-AGID](https://cert-agid.gov.it/wp-content/uploads/2026/11/image.png)](https://www.agid.gov.it/sites/agid/files/2026-11/La%20backdoor%20attende%20il%20suo%20turno_paper%20nov26.pdf)

*Paper novembre 2026 – CERT-AGID*

L’esperimento mostra che è possibile insegnare a un modello un comportamento aggiuntivo che **si attiva quando diventa disponibile uno specifico server MCP**, anche se la domanda dell’utente non riguarda quello strumento.

Nella configurazione studiata, il modello ha generato la chiamata verso l’URL appreso soltanto in presenza del server previsto, producendo una richiesta HTTPS reale.

![](https://cert-agid.gov.it/wp-content/uploads/2026/11/image-1-1024x510.png)

Il metodo non è specifico di ***Qwen***. Un addestramento analogo può essere applicato ad altri modelli open-weight compatibili con il fine-tuning.

Il rischio nasce anche dall’incontro tra il modello e gli strumenti che gli vengono collegati nel tempo. Un comportamento appreso può restare inattivo durante le verifiche iniziali e manifestarsi quando l’ambiente cambia.

## Uno scenario ipotetico

Uno scenario plausibile è una distribuzione in due tempi. Un soggetto pubblica sulla piattaforma *Hugging Face* un modello o un adapter utile per attività ordinarie, nel quale ha inserito anche un comportamento condizionale. Il server che lo attiva potrebbe non esistere ancora negli ambienti degli utenti. In seguito, viene distribuito un server MCP con il nome già previsto nell’addestramento, quando un’applicazione lo collega e ne comunica i metadati al modello, la condizione può essere soddisfatta senza aggiornare nuovamente i pesi.

**Link alla ricerca (PDF):** [La backdoor attende il suo turno](https://www.agid.gov.it/sites/agid/files/2026-11/La%20backdoor%20attende%20il%20suo%20turno_paper%20nov26.pdf)

Taggato
[Agentic AI](https://cert-agid.gov.it/tag/agentic-ai/)
[Backdoor](https://cert-agid.gov.it/tag/backdoor/)
[Intelligenza Artificiale](https://cert-agid.gov.it/tag/intelligenza-artificiale/)
[MCP](https://cert-agid.gov.it/tag/mcp/)

## Navigazione articoli

[Notizia precedente Sintesi riepilogativa delle campagne malevole nella settimana del 24 – 30 ottobre](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-24-30-ottobre/)

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

Chiudi

Precedente

![]()

![]()

Successivo