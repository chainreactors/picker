---
title: Meta annuncia nuovi tool di sicurezza per Llama
url: https://www.securityinfo.it/2025/05/02/meta-annuncia-nuovi-tool-di-sicurezza-per-llama/?utm_source=rss&utm_medium=rss&utm_campaign=meta-annuncia-nuovi-tool-di-sicurezza-per-llama
source: Securityinfo.it
date: 2025-05-03
fetch_date: 2025-10-06T22:29:04.245198
---

# Meta annuncia nuovi tool di sicurezza per Llama

Aggiornamenti recenti Ottobre 6th, 2025 3:00 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Microsoft Sentinel: arriva l’era degli agenti AI e della difesa predittiva](https://www.securityinfo.it/2025/10/06/microsoft-sentinel-arriva-lera-degli-agenti-ai-e-della-difesa-predittiva/)
* [CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)
* [Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)

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

## Meta annuncia nuovi tool di sicurezza per Llama

Mag 02, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Gestione dati](https://www.securityinfo.it/category/news/gestione-dati-news/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Tecnologia](https://www.securityinfo.it/category/news/tecnologia-news/)
 [0](https://www.securityinfo.it/2025/05/02/meta-annuncia-nuovi-tool-di-sicurezza-per-llama/#respond)

---

Martedì scorso Meta [ha annunciato](https://ai.meta.com/blog/ai-defenders-program-llama-protection-tools/) **nuovi tool di sicurezza per Llama** allo scopo di aiutare gli sviluppatori a realizzare applicazioni di intelligenza artificiale più sicure.

La prima novità è [**LlamaFirewall**](https://ai.meta.com/research/publications/llamafirewall-an-open-source-guardrail-system-for-building-secure-ai-agents/), un framework open-source per aiutare gli sviluppatori a **individuare e prevenire attacchi mirati** come la prompt injection o le interazioni con plugin-in sospetti, ma anche lo sviluppo di codice non sicuro. LlamaFirewall si presenta come un orchestratore di modelli di IA ed è in grado di integrarsi con altri prodotti di sicurezza.

“*LlamaFirewall è un framework progettato per **rilevare e mitigare i rischi di sicurezza incentrati sull’intelligenza artificiale**, supportando più livelli di input e output, come la tipica chat LLM e operazioni ad agenti multi-step più avanzate. È costituito da una serie di scanner per diversi rischi di sicurezza*” ha specificato Meta su un repository GitHub del progetto per Llama.

![Meta Llama](https://www.securityinfo.it/wp-content/uploads/2025/05/124669.jpg)

Il framework si compone di tre moduli: **Agent Alignment Checks**, un auditor che si occupa di analizzare il flusso di ragionamento degli agenti per prevenire errori e prompt injection; **CodeShield**, un motore di analisi statica in grado di prevenire la generazione di codice non sicuro; infine, [**PromptGuard 2**](https://meta-llama.github.io/PurpleLlama/LlamaFirewall/docs/documentation/scanners/prompt-guard-2), un aggiornamento al precedente modello di classificazione.

La nuova versione di PromptGuard 2 migliora le funzionalità di individuazione di tentativi di jailbreak e prompt injection. Nella versione base, il nuovo modello funziona con 86 milioni di parametri, ma è disponibile anche in una versione più contenuta da 22 milioni di parametri, più veloce e con un costo computazionale notevolmente minore.

Rispetto alla versione precedente, il nuovo PromptGuard è stato addestrato su un dataset più ampio per analizzare più tipi di input e output differenti e per migliorare le sue capacità di detection. “*Essendo un modello leggero, **PromptGuard 2 è eseguibile sia sulla CPU che sulla GPU**, rendendolo ideale per l’analisi real-time dell’input degli LLM e per facilitare l’individuazione rapida e accurata dei tentativi di jailbreak*“.

Tra gli aggiornamenti, Meta segnala anche un aggiornamento per **CyberSecEval**, la suite di benchmark di cybersecurity per i modelli di IA. La suite include ora due nuovi tool: **CyberSOC Eval**, un framework che misura l’efficacia dei sistemi di IA nei SOC, e **AutoPatchBench**, un nuovo benchmark in grado di valutare la capacità di Llama e altri sistemi di IA di applicare automaticamente le patch per le vulnerabilità.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [cybersecurity](https://www.securityinfo.it/tag/cybersecurity/), [Intelligenza artificiale](https://www.securityinfo.it/tag/intelligenza-artificiale/), [Jailbreak](https://www.securityinfo.it/tag/jailbreak/), [Llama](https://www.securityinfo.it/tag/llama/), [Meta](https://www.securityinfo.it/tag/meta/), [prompt injection](https://www.securityinfo.it/tag/prompt-injection/), [vulnerabilità IA](https://www.securityinfo.it/tag/vulnerabilita-ia/)

[CERT-AGID 26 aprile - 2 maggio: campagne di phishing con PagoPA e il ritorno di vecchi malware](https://www.securityinfo.it/2025/05/03/cert-agid-26-aprile-2-maggio-phishing-pagopa-ritorno-vecchi-malware/)
[La RSA Conference accoglie le soluzioni italiane di cybersecurity](https://www.securityinfo.it/2025/04/30/la-rsa-conference-accoglie-le-soluzioni-italiane-di-cybersecurity/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Microsoft Sentinel: arriva l’era degli agenti AI e della difesa predittiva](https://www.securityinfo.it/wp-content/uploads/2025/10/Microsoft-Sentinel_3ott-2025CG-120x85.png)](https://www.securityinfo.it/2025/10/06/microsoft-sentinel-arriva-lera-degli-agenti-ai-e-della-difesa-predittiva/ "Microsoft Sentinel: arriva l’era degli agenti AI e della difesa predittiva")

  [Microsoft Sentinel: arriva l’era...](https://www.securityinfo.it/2025/10/06/microsoft-sentinel-arriva-lera-degli-agenti-ai-e-della-difesa-predittiva/ "Permanent link to Microsoft Sentinel: arriva l’era degli agenti AI e della difesa predittiva")

  Ott 06, 2025  [0](https://www.securityinfo.it/2025/10/06/microsoft-sentinel-arriva-lera-degli-agenti-ai-e-della-difesa-predittiva/#respond)
* [![L’IA diventa arma e vittima per il cybercrimine: il report di Crowdstrike](https://www.securityinfo.it/wp-content/uploads/2025/09/ai-generated-7992462_1920-120x85.jpg)](https://www.securityinfo.it/2025/09/12/l-ia-diventa-arma-e-vittima-per-il-cybercrimine-il-report-di-crowdstrike/ "L’IA diventa arma e vittima per il cybercrimine: il report di Crowdstrike")

  [L’IA diventa arma e vittima per...](https://www.securityinfo.it/2025/09/12/l-ia-diventa-arma-e-vittima-per-il-cybercrimine-il-...