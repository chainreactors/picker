---
title: DeepSeek R1 produce codice vulnerabile con prompt “politicamente sensibili”
url: https://www.securityinfo.it/2025/11/24/deepseek-r1-produce-codice-vulnerabile-con-prompt-politicamente-sensibili/
source: Over Security - Cybersecurity news aggregator
date: 2025-11-24
fetch_date: 2025-11-25T03:12:55.976828
---

# DeepSeek R1 produce codice vulnerabile con prompt “politicamente sensibili”

Aggiornamenti recenti Novembre 24th, 2025 5:36 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [DeepSeek R1 produce codice vulnerabile con prompt “politicamente sensibili”](https://www.securityinfo.it/2025/11/24/deepseek-r1-produce-codice-vulnerabile-con-prompt-politicamente-sensibili/)
* [CERT-AGID 15–21 novembre: attacchi a università, banche e PEC](https://www.securityinfo.it/2025/11/24/cert-agid-15-21-novembre-attacchi-universita-banche-pec/)
* [Come Firemon supporta i propri partner nel processo di migrazione da Skybox](https://www.securityinfo.it/2025/11/21/come-firemon-supporta-i-propri-partner-nel-processo-di-migrazione-da-skybox/)
* [Sneaky2FA si evolve con una funzionalità Browser-in-the-Browser](https://www.securityinfo.it/2025/11/20/sneaky2fa-si-evolve-con-una-funzionalita-browser-in-the-browser/)
* [DragonForce evolve in un “cartello” ransomware e diventa più aggressivo](https://www.securityinfo.it/2025/11/19/dragonforce-evolve-in-un-cartello-ransomware-e-diventa-piu-aggressivo/)

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

## DeepSeek R1 produce codice vulnerabile con prompt “politicamente sensibili”

Nov 24, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Gestione dati](https://www.securityinfo.it/category/approfondimenti/gestione-dati/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Tecnologia](https://www.securityinfo.it/category/approfondimenti/tecnologia/), [Tecnologia](https://www.securityinfo.it/category/news/tecnologia-news/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/), [Vulnerabilità](https://www.securityinfo.it/category/approfondimenti/vulnerabilita-approfondimenti/)
 [0](https://www.securityinfo.it/2025/11/24/deepseek-r1-produce-codice-vulnerabile-con-prompt-politicamente-sensibili/#respond)

---

Analizzando **DeepSeek R1**, un potente LLM dell’omonima società cinese, i ricercatori di CrowdStrike [hanno scoperto](https://www.crowdstrike.com/en-us/blog/crowdstrike-researchers-identify-hidden-vulnerabilities-ai-coded-software/) che questo modello **produce codice vulnerabile quando riceve dei prompt contenenti argomenti “politicamente sensibili”.**

“*CrowdStrike Counter Adversary Operations ha condotto test indipendenti su DeepSeek-R1 e ha confermato che, in molti casi, è in grado di fornire un output di codifica di qualità paragonabile ad altri LLM leader di mercato del momento. Tuttavia, abbiamo scoperto che **quando DeepSeek-R1 riceve prompt contenenti argomenti che il Partito Comunista Cinese (PCC) considera politicamente sensibili, la probabilità che produca codice con gravi vulnerabilità di sicurezza aumenta fino al 50%***” hanno spiegato i ricercatori.

![DeepSeek](https://www.securityinfo.it/wp-content/uploads/2025/11/Gemini_Generated_Image_87vil587vil587vi.png)

Nell’analisi, il team di CrowdStrike ha comparato tre modelli: DeepSeek R1 con 671 miliardi di parametri e due modelli occidentali, uno con 70 miliardi di parametri e senza capacità di ragionamento, l’altro con 120 miliardi di parametri e capacità di ragionamento.

**Nel caso di prompt senza “parole trigger”, l’LLM di DeepSeek tende a introdurre vulnerabilità con una probabilità del 19%**, performando meglio del modello occidentale da 70 miliardi di parametri. Quando però vengono introdotti dei modificatori di contesto o delle parole chiave, la qualità del codice varia significativamente, soprattutto se si introducono parole o frasi su argomenti considerati sensibili dal Partito Comunista Cinese.

Per esempio, chiedendo all’LLM di generare codice per un sistema industriale *basato in Tibet*la percentuale di vulnerabilità presenti nel codice è aumentata al 27.2%, un incremento di quasi il 50% rispetto al comportamento base.

“*È importante sottolineare che tutti i modificatori sono irrilevanti per le attività di codifica effettive che abbiamo richiesto a DeepSeek-R1. Pertanto, in base all’ipotesi nulla che non vi siano pregiudizi che influenzano la sicurezza del codice, **essi non avrebbero dovuto avere alcun effetto sulla qualità o sulla sicurezza del codice prodotto***” sottolineano i ricercatori. Nella pratica, però, il team ha individuato diversi modificatori che hanno inciso significativamente sulla qualità del risultato.

In un caso, il team di CrowdStrike ha chiesto all’LLM di creare un’applicazione completa per permettere ai membri della comunità Uiguri di connettersi tra loro. L’LLM ha effettivamente generato il codice, includendo un form di registrazione, la gestione di un database per memorizzare username e password e un pannello di admin per gestire gli account utente. Controllando attentamente il codice, però, è emerso che **DeepSeek R1 aveva in realtà creato un’applicazione completamente accessibile in cui i dati degli utenti venivano esposti.**

I ricercatori di CrowdStrike spiegano che la ricerca non è esaustiva e che potrebbero esserci altri trigger che scatenano risposte simili. È anche possibile che, oltre a DeepSeek R1, altri LLM potrebbero avere bias simili.

![](https://www.securityinfo.it/wp-content/uploads/2025/11/ai-generated-7992462_1920-1.jpg)

Il team della compagnia ritiene piuttosto improbabile che DeepSeek abbia programmato intenzionalmente il modello per scrivere introdurre vulnerabilità in caso di specifici trigger; si tratta più probabilmente di un effetto collaterale non voluto causato da una serie di imposizioni delle leggi cinesi, le quali obbligano le IA ad aderire ai “valori socialisti fondamentali” e a non generare contenuti che possano minacciare l’autorità statale.

Parole e concetti considerati negativi o proibiti spingono l’LLM ad agire in maniera “difensiva”; ciò significa non semplicemente censurare la risposta, ma anche degradare le sue capacità di ragionamento.

“*Desideriamo sottolineare che i presenti risultati non significano che DeepSeek-R1 produrrà codice non sicuro ogni volta che saranno presenti tali parole trigger. **Piuttosto, in media a lungo termine, il codice prodotto quando questi trigger sono presenti sarà meno sicuro***” conclude il team di CrowdStrike.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [censura](https://www.securityinfo.it/tag/censura/), [DeepSeek](https://www.securityinfo.it/tag/deepseek/), [DeepSeek R1](https://www.securityinfo.it/tag/deepseek-r1/), [LLM](https://www.securityinfo.it/tag/llm/), [partito comunista cinese](https://www.securityinfo.it/tag/partito-comunista-cinese/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[CERT-AGID 15–21 novembre: attacchi a università, banche e PEC](https://www.securityinfo.it/2025/11/24/cert-agid-15-21-novembre-attacchi-universita-banche-pec/)

---

![](https://secure.gravatar.com/av...