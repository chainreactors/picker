---
title: Falsa skill elude gli scanner e a raggiunge più di 26.000 agenti AI
url: https://www.securityinfo.it/2026/06/21/una-falsa-skill-elude-gli-scanner-e-a-raggiunge-piu-di-26-000-agenti-ai/
source: Over Security
date: 2026-06-26
fetch_date: 2026-06-27T05:52:07.448572
---

# Falsa skill elude gli scanner e a raggiunge più di 26.000 agenti AI

Aggiornamenti recenti Giugno 21st, 2026 1:25 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Falsa skill elude gli scanner e a raggiunge più di 26.000 agenti AI](https://www.securityinfo.it/2026/06/21/una-falsa-skill-elude-gli-scanner-e-a-raggiunge-piu-di-26-000-agenti-ai/)
* [Zscaler porta la Zero Trust nell’era degli agenti AI](https://www.securityinfo.it/2026/06/16/zscaler-porta-la-zero-trust-nellera-degli-agenti-ai/)
* [Infrastrutture Critiche e Geopolitica: è l’Era dell’Antifragilità](https://www.securityinfo.it/2026/06/09/infrastrutture-critiche-e-geopolitica-e-lera-dellantifragilita/)
* [Il gruppo criminale cinese TA4922 adesso punta anche all’Europa](https://www.securityinfo.it/2026/06/04/il-gruppo-criminale-cinese-ta4922-adesso-punta-anche-alleuropa/)
* [Il 78% delle aziende ha già subito o sospetta incidenti legati all’IA](https://www.securityinfo.it/2026/05/28/il-78-delle-aziende-ha-gia-subito-o-sospetta-incidenti-legati-allia/)

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

## Falsa skill elude gli scanner e a raggiunge più di 26.000 agenti AI

Giu 21, 2026  [Redazione](https://www.securityinfo.it/author/redazione/ "Articoli scritti da Redazione")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2026/06/21/una-falsa-skill-elude-gli-scanner-e-a-raggiunge-piu-di-26-000-agenti-ai/#respond)

---

La rapida diffusione degli **Agenti AI** sta creando un ecosistema sempre più complesso nel quale modelli linguistici, strumenti esterni e componenti aggiuntivi collaborano per svolgere attività operative. Questa architettura modulare, però, sta aprendo una nuova superficie di attacco che ricorda da vicino le vulnerabilità già viste nel mondo open source e nei marketplace di applicazioni.

Un caso recente evidenziato dai ricercatori ha mostrato come una **falsa skill per agenti AI** sia riuscita a superare i controlli automatici di sicurezza e a raggiungere oltre **26.000 agenti**, dimostrando quanto siano ancora immature molte delle difese implementate nei marketplace dedicati agli agenti intelligenti.

![](https://www.securityinfo.it/wp-content/uploads/2026/06/AI_Agent_Market-1024x683.png)

### **Quando il problema non è il modello ma l’estensione**

Molte piattaforme agentiche consentono agli utenti di installare componenti aggiuntivi, spesso chiamati **skill, tool o plug-in**. Questi moduli permettono all’agente di accedere a nuove funzionalità, interagire con servizi esterni o automatizzare processi complessi.

Il problema è che la sicurezza di questi ecosistemi non dipende soltanto dal modello AI utilizzato, ma anche dall’affidabilità delle estensioni installate. Se una skill malevola riesce a superare i controlli preliminari, può ottenere accesso a dati sensibili, credenziali e processi aziendali eseguiti dall’agente.

Secondo una recente analisi su quasi **4.000 skill distribuite in diversi marketplace**, i ricercatori hanno identificato **76 payload malevoli confermati**, mentre il **13,4% delle skill analizzate** presentava almeno una vulnerabilità classificata come critica.

### **Come è stata aggirata la scansione automatica**

L’aspetto più interessante della vicenda riguarda il modo in cui la falsa skill è riuscita a sfuggire agli strumenti di verifica.

Gli scanner automatici utilizzati da molte piattaforme si concentrano prevalentemente sull’analisi statica del codice e sulla ricerca di pattern noti. Gli autori della skill hanno invece sfruttato **tecniche di offuscamento e comportamenti attivati solo in determinate condizioni operative**, rendendo difficile individuare la componente malevola durante le verifiche preliminari.

### **Il rischio per le aziende**

La vicenda evidenzia un problema destinato a crescere nei prossimi anni. Sempre più aziende concedono agli agenti AI accesso a repository di codice, documentazione interna, strumenti di produttività, piattaforme cloud e una skill compromessa potrebbe diventare un vettore privilegiato per attività di **esfiltrazione dati**, raccolta di credenziali, installazione di backdoor o manipolazione dei workflow aziendali. I ricercatori hanno già osservato casi reali di skill progettate per sottrarre informazioni sensibili o modificare il comportamento degli agenti ospitanti. La criticità è amplificata dal fatto che molti agenti operano con privilegi elevati e possono accedere direttamente a servizi interni o risorse normalmente non esposte a utenti esterni.

### **Verso una nuova generazione di controlli**

La diffusione degli AI Agent sta riproponendo dinamiche già note nel mondo del software tradizionale. Così come repository open source e store di applicazioni sono diventati obiettivi privilegiati degli attacchi supply chain, anche i marketplace delle skill stanno emergendo come un nuovo bersaglio.

Per le aziende che intendono adottare agenti autonomi sarà quindi fondamentale introdurre processi di validazione indipendenti, sandbox dedicate, monitoraggio continuo e controlli granulari sui privilegi concessi alle estensioni installate.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [agent security](https://www.securityinfo.it/tag/agent-security/), [agentic AI](https://www.securityinfo.it/tag/agentic-ai/), [AI Agent](https://www.securityinfo.it/tag/ai-agent/), [AI security](https://www.securityinfo.it/tag/ai-security/), [cybersecurity](https://www.securityinfo.it/tag/cybersecurity/), [Intelligenza artificiale](https://www.securityinfo.it/tag/intelligenza-artificiale/), [marketplace skill](https://www.securityinfo.it/tag/marketplace-skill/), [prompt injection](https://www.securityinfo.it/tag/prompt-injection/), [sicurezza AI](https://www.securityinfo.it/tag/sicurezza-ai/), [supply chain attack](https://www.securityinfo.it/tag/supply-chain-attack/)

[Zscaler porta la Zero Trust nell’era degli agenti AI](https://www.securityinfo.it/2026/06/16/zscaler-porta-la-zero-trust-nellera-degli-agenti-ai/)

---

![](https://secure.gravatar.com/avatar/57d6369d65bf9ebecae351af675ce2fd?s=90&d=mm&r=g)

##### [Redazione](https://www.securityinfo.it/author/redazione/)

##### Articoli correlati

* [![Zscaler porta la Zero Trust nell’era degli agenti AI](https://www.securityinfo.it/wp-content/uploads/2026/06/ZenithLIve-scaled-120x85.jpg)](https://www.securityinfo.it/2026/06/16/zscaler-porta-la-zero-trust-nellera-degli-agenti-ai/ "Zscaler porta la Zero Trust nell’era degli agenti AI")

  [Zscaler porta la Zero Trust nell’era...](https://www.securityinfo.it/2026/06/16/zscaler-porta-la-zero-trust-nellera-degli-agenti-ai/ "Permanent link to Zscaler porta la Zero Trust nell’era degli agenti AI")

  Giu 16, 2026  [0](https://www.securityinfo.it/2026/06/16/zscaler-porta-la-zero-trust-nellera-degli-agenti-ai/#respond)
* [![Infrastrutture Critiche ...