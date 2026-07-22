---
title: Hugging Face violata da un agente AI: gli attacchi autonomi sono arrivati
url: https://www.securityinfo.it/2026/07/21/hugging-face-violata-da-un-agente-ai-perche-il-primo-attacco-autonomo-segna-una-svolta-per-la-cybersecurity/?utm_source=rss&utm_medium=rss&utm_campaign=hugging-face-violata-da-un-agente-ai-perche-il-primo-attacco-autonomo-segna-una-svolta-per-la-cybersecurity
source: Securityinfo.it
date: 2026-07-21
fetch_date: 2026-07-22T05:04:18.850765
---

# Hugging Face violata da un agente AI: gli attacchi autonomi sono arrivati

Aggiornamenti recenti Luglio 21st, 2026 3:45 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Hugging Face violata da un agente AI: gli attacchi autonomi sono arrivati](https://www.securityinfo.it/2026/07/21/hugging-face-violata-da-un-agente-ai-perche-il-primo-attacco-autonomo-segna-una-svolta-per-la-cybersecurity/)
* [Gli assistenti AI di coding sono sicuri? Il caso xAI](https://www.securityinfo.it/2026/07/14/gli-assistenti-ai-di-coding-sono-sicuri-il-caso-xai/)
* [La guerra ucraina cambia la sicurezza delle infrastrutture critiche](https://www.securityinfo.it/2026/07/10/la-guerra-ucraina-cambia-la-cybersecurity-delle-infrastrutture-critiche/)
* [AI, il nuovo fronte della sicurezza: il red teaming diventa indispensabile](https://www.securityinfo.it/2026/07/06/ai-il-nuovo-fronte-della-sicurezza-il-red-teaming-diventa-indispensabile/)
* [Falsa skill elude gli scanner e a raggiunge più di 26.000 agenti AI](https://www.securityinfo.it/2026/06/21/una-falsa-skill-elude-gli-scanner-e-a-raggiunge-piu-di-26-000-agenti-ai/)

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

## Hugging Face violata da un agente AI: gli attacchi autonomi sono arrivati

Lug 21, 2026  [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo_security/ "Articoli scritti da Giancarlo Calzetta")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Attacchi](https://www.securityinfo.it/category/approfondimenti/attacchi/), [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2026/07/21/hugging-face-violata-da-un-agente-ai-perche-il-primo-attacco-autonomo-segna-una-svolta-per-la-cybersecurity/#respond)

---

Per anni l’idea di un attacco informatico condotto interamente da un agente di Intelligenza Artificiale è rimasta confinata ai laboratori di ricerca e alle presentazioni dei vendor. Oggi non è più così. La piattaforma **Hugging Face**, punto di riferimento mondiale per lo sviluppo e la distribuzione di modelli AI open source, ha confermato di essere stata colpita da quello che descrive come un attacco **condotto dall’inizio alla fine da un sistema autonomo di agenti AI**.  L’episodio rappresenta molto più di una violazione informatica: è probabilmente il primo caso documentato in cui un’infrastruttura di produzione di una realtà di una certa rilevanza viene compromessa da **un sistema capace di pianificare ed eseguire autonomamente una campagna offensiva complessa**, senza che un operatore umano debba guidarne ogni fase.

![](https://www.securityinfo.it/wp-content/uploads/2026/07/HFSottoAttaccoOrizzontale-1024x572.png)

**L’attacco è partito dalla supply chain dei dati**

Secondo quanto comunicato da Hugging Face, **gli aggressori hanno sfruttato una superficie d’attacco peculiare delle piattaforme AI: la pipeline che elabora dataset caricati dagli utenti**. Un dataset malevolo ha abusato di due percorsi di esecuzione del codice, un loader che consentiva l’esecuzione di codice remoto e una vulnerabilità di template injection nella configurazione del dataset, ottenendo l’esecuzione di codice su un nodo di elaborazione.  Da quel momento **il comportamento dell’attaccante è stato quello tipico di un’Advanced Persistent Threat**: escalation dei privilegi, raccolta di credenziali cloud e di cluster, movimento laterale tra diversi sistemi e accesso non autorizzato a dataset interni e credenziali di servizio. Hugging Face precisa di **non aver trovato evidenze di manomissioni** ai modelli pubblici, ai dataset disponibili agli utenti, agli Spaces o alla propria software supply chain, ma l’incidente dimostra quanto le piattaforme AI introducano superfici di attacco nuove rispetto alle applicazioni tradizionali.

**La novità non è la vulnerabilità, ma chi ha guidato l’attacco**

La vulnerabilità sfruttata non rappresenta l’aspetto più innovativo dell’incidente. Ciò che cambia realmente è il modo in cui è stata sfruttata. Secondo la ricostruzione dell’azienda, l’operazione è stata eseguita da un framework agentico capace di svolgere **decine di migliaia di azioni** distribuite su una moltitudine di ambienti temporanei, con infrastrutture di comando e controllo che migravano automaticamente tra servizi pubblici per ridurre la probabilità di essere individuate.

In pratica, **l’AI non si è limitata a generare codice o suggerire una sequenza di exploit: ha eseguito autonomamente una campagna offensiva articolata**, adattandosi durante le diverse fasi dell’intrusione. È lo scenario dell’**agentic attacker** di cui il settore della cybersecurity discute da tempo e che oggi sembra essersi concretizzato.

**L’AI ha difeso Hugging Face da un’altra AI**

L’altro elemento interessante dell’incidente è che anche **la risposta è stata in larga parte automatizzata**. Hugging Face spiega di aver utilizzato sistemi basati su LLM per analizzare la telemetria di sicurezza, correlare gli eventi e ricostruire rapidamente la cronologia dell’attacco. Gli agenti di analisi hanno elaborato **oltre 17.000 eventi**, permettendo ai team di incident response di individuare gli indicatori di compromissione e distinguere le attività realmente dannose da quelle create per depistare gli analisti. Secondo l’azienda, **un’attività che normalmente richiederebbe diversi giorni è stata completata in poche ore** grazie all’automazione. Il risultato è un assaggio di quello che potrebbe diventare il nuovo paradigma della cybersecurity: **AI contro AI**, con attaccanti e difensori che operano entrambi a velocità macchina.

**Il problema tanto temuto dei guardrail ciechi**

Tra gli aspetti più curiosi emersi dal post mortem c’è un problema che fino a poco tempo fa sarebbe sembrato marginale. Durante l’analisi forense, Hugging Face ha inizialmente provato a utilizzare modelli commerciali accessibili tramite API. Tuttavia, le richieste contenevano exploit, payload, comandi di attacco e indicatori di compromissione reali: **elementi che i sistemi di sicurezza dei modelli hanno interpretato come contenuti pericolosi, bloccandone l’elaborazione**.

Per completare l’analisi, l’azienda ha quindi utilizzato un **modello open-weight eseguito sulla propria infrastruttura**, evitando sia le limitazioni imposte dai guardrail sia il trasferimento all’esterno di dati sensibili e credenziali compromesse. Questo ci riporta a un tema che è stato affrontato più volte dall’arrivo degli LLM al grande pubblico: **è giusto limitarne le capacità quando gli unici che ne fanno davvero le spese sono gli utenti che li usano per scopi leciti**? Ovviamente, la risposta è lunga e articolata, ma sembra abbastanza ovvio che qualcosa debba esser ripensato, a partire dalla disponibilità di servizi AI deputati all’analisi forense e al blue teaming.

**Le piattaforme AI diventano una nuova superficie...