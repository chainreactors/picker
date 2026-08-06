---
title: Claude evade (di nuovo) e compromette tre aziende reali
url: https://www.securityinfo.it/2026/08/04/claude-evade-di-nuovo-e-compromette-tre-aziende-reali/
source: Over Security
date: 2026-08-05
fetch_date: 2026-08-06T05:02:44.871530
---

# Claude evade (di nuovo) e compromette tre aziende reali

Aggiornamenti recenti Agosto 4th, 2026 2:00 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Claude evade (di nuovo) e compromette tre aziende reali](https://www.securityinfo.it/2026/08/04/claude-evade-di-nuovo-e-compromette-tre-aziende-reali/)
* [Hugging Face violata da un agente AI: gli attacchi autonomi sono arrivati](https://www.securityinfo.it/2026/07/21/hugging-face-violata-da-un-agente-ai-perche-il-primo-attacco-autonomo-segna-una-svolta-per-la-cybersecurity/)
* [Gli assistenti AI di coding sono sicuri? Il caso xAI](https://www.securityinfo.it/2026/07/14/gli-assistenti-ai-di-coding-sono-sicuri-il-caso-xai/)
* [La guerra ucraina cambia la sicurezza delle infrastrutture critiche](https://www.securityinfo.it/2026/07/10/la-guerra-ucraina-cambia-la-cybersecurity-delle-infrastrutture-critiche/)
* [AI, il nuovo fronte della sicurezza: il red teaming diventa indispensabile](https://www.securityinfo.it/2026/07/06/ai-il-nuovo-fronte-della-sicurezza-il-red-teaming-diventa-indispensabile/)

* [Home](https://www.securityinfo.it)
* [News](https://www.securityinfo.it/category/news/)
* [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/)
* [Opinioni](https://www.securityinfo.it/category/opinioni/)
* [Top Malware](https://www.securityinfo.it/top-malware-page/)
* [Minacce](https://www.securityinfo.it/category/minacce-2/)
* [Guide alla sicurezza](http://www.securityinfo.it/guide-alla-sicurezza/)
* [Podcast](https://www.securityinfo.it/podcast-page/)
* [Strumenti Utili](https://www.securityinfo.it/category/strumenti-utili/)

* Search for:

## Claude evade (di nuovo) e compromette tre aziende reali

Ago 04, 2026  [Redazione news](https://www.securityinfo.it/author/redazione-news/ "Articoli scritti da Redazione news")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Scenario](https://www.securityinfo.it/category/news/scenario-news/)
 [0](https://www.securityinfo.it/2026/08/04/claude-evade-di-nuovo-e-compromette-tre-aziende-reali/#respond)

---

Sembra proprio che tenere a bada i modelli IA sia complicatissimo e **Anthropic sta accumulando una certa esperienza nel settore**. L’azienda ha infatti rivelato che alcuni modelli della famiglia Claude sono riusciti ad accedere ai sistemi di **tre organizzazioni reali** durante esercitazioni di sicurezza, **trasformando test che avrebbero dovuto svolgersi in ambienti controllati in vere e proprie compromissioni di sistemi esterni**.

## Non è stato un attacco deliberato

Anthropic precisa che **non si è trattato di un comportamento malevolo intenzionale del modello**, né di un tentativo di “ribellione” dell’intelligenza artificiale. Le prove delle compromissioni, infatti, sono emerse durante la revisione interna di oltre **141.000 valutazioni di sicurezza** avviata dopo il recente incidente che aveva coinvolto OpenAI. L’analisi ha portato alla scoperta di tre casi nei quali versioni di Claude erano riuscite a **raggiungere Internet da un ambiente di valutazione gestito da terze parti** e ad accedere senza autorizzazione ai sistemi di tre differenti organizzazioni. Anthropic specifica che il problema è stato favorito da **una combinazione di errori umani, configurazioni errate dell’ambiente di test e vulnerabilità reali** presenti nei sistemi raggiunti dal modello.

![](https://www.securityinfo.it/wp-content/uploads/2026/08/Evasione-1024x683.png)

## Tre incidenti diversi, un unico denominatore

I modelli coinvolti comprendono **Claude Opus 4.7**, **Claude Mythos 5** e un modello sperimentale interno e quello che rende il tutto più “pepato” è che le dinamiche dei tre episodi sono differenti. In un caso il modello ha confuso il dominio di un’azienda reale con quello previsto nello scenario di laboratorio, riuscendo così ad accedere a un database esterno. C’è da dire che, probabilmente, chi ha organizzato il test non ha verificato che il nome dell’azienda “fasulla perché inserita nel test” fosse inesistente. In un secondo episodio è statp eseguito un attacco alla **supply chain** attraverso la pubblicazione di un pacchetto Python malevolo sul repository pubblico PyPI che è stato successivamente scaricato da alcuni sistemi reali. Nel terzo incidente il modello ha iniziato a esplorare migliaia di server connessi a Internet e stava per sfruttare una vulnerabilità SQL Injection, interrompendo però autonomamente l’operazione quando ha riconosciuto di trovarsi al di fuori dell’ambiente previsto dal test. Anthropic attribuisce questi episodi principalmente a carenze operative nella gestione delle esercitazioni piuttosto che a un fallimento dei meccanismi di allineamento del modello. In effetti, i modelli hanno fatto il loro dovere, ma si deve evidentemente ancora lavorare su come tenerli a bada.

## Il vero problema è il contenimento

Le aziende stanno investendo enormi risorse per misurare le capacità offensive dei nuovi modelli AI, ma questi incidenti mostrano che **la sicurezza dell’ambiente di valutazione è importante quanto quella del modello stesso**. Un agente capace di operare autonomamente, usare strumenti, accedere alla rete e prendere decisioni e metterle in pratica può infatti sfruttare qualsiasi errore di configurazione presente nell’infrastruttura di test: il rischio non nasce esclusivamente dall’intelligenza artificiale, ma dall’interazione tra modello, strumenti disponibili e ambiente operativo.

## Mythos torna al centro dell’attenzione

Tra i modelli coinvolti figura anche **Claude Mythos**, il sistema che Anthropic ha deciso di non distribuire pubblicamente proprio a causa delle sue elevate capacità offensive in ambito cyber e molti ricorderanno che non è la prima volta che Mythos finisce al centro delle cronache. Già nei mesi scorsi il modello era stato protagonista di almeno altri **due episodi** che avevano alimentato il dibattito sulla sua gestione. Il primo riguarda la **fuga non autorizzata di alcuni accessi** alla versione preview del modello, comparsi poche ore dopo il suo annuncio all’interno di una comunità privata online. Anthropic aveva confermato che utenti non autorizzati erano riusciti a usare il sistema, pur trattandosi di una versione destinata esclusivamente a un ristretto gruppo di partner del progetto Glasswing.

Il secondo episodio è emerso dalla **Hazard-Aware System Card** pubblicata dalla stessa Anthropic. Durante prove di laboratorio dedicate alla verifica delle misure di contenimento, una versione sperimentale di Mythos era riuscita ad aggirare alcune restrizioni del sandbox, comunicare verso l’esterno e mettere in atto comportamenti inattesi, come modificare file cercando di nascondere le modifiche nella cronologia Git. Anche in quel caso l’azienda aveva sottolineato che gli eventi erano avvenuti in ambienti di test controllati e avevano contribuito a rafforzare le misure di sicurezza del progetto.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [AI Agent](https://www.securityinfo.it/tag/ai-agent/), [AI cybersecurity](https://www.securityinfo.it/tag/ai-cybersecurity/), [Anthropic](https://www.securityinfo.it/tag/anthropic/), [Claude](https://www.securityinfo.it/tag/claude/), [Claude Mythos](https://www.securityinfo.it/tag/claude-mythos/), [hugging face](https://www.securityinfo.it/tag/hugging-face/), [openai](https://www.securityinfo.it/tag/openai/)...