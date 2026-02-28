---
title: Google API Keys: le chiavi pubbliche diventano credenziali sensibili
url: https://www.securityinfo.it/2026/02/27/google-api-keys-le-chiavi-pubbliche-diventano-credenziali-sensibili/
source: Over Security - Cybersecurity news aggregator
date: 2026-02-27
fetch_date: 2026-02-28T04:01:31.278396
---

# Google API Keys: le chiavi pubbliche diventano credenziali sensibili

Aggiornamenti recenti Febbraio 27th, 2026 3:15 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Paradosso ransomware, pagamenti in calo ma attacchi ai massimi storici](https://www.securityinfo.it/2026/02/27/paradosso-ransomware-pagamenti-in-calo-ma-attacchi-ai-massimi-storici/)
* [Google API Keys: le chiavi pubbliche diventano credenziali sensibili](https://www.securityinfo.it/2026/02/27/google-api-keys-le-chiavi-pubbliche-diventano-credenziali-sensibili/)
* [Claude Code Security crea il panico, ma… non uccide la cyber](https://www.securityinfo.it/2026/02/25/claude-code-security-crea-il-panico-ma-non-uccide-la-cyber/)
* [Sandworm\_Mode: il “worm” della supply chain NPM](https://www.securityinfo.it/2026/02/24/sandworm_mode-il-worm-della-supply-chain-npm/)
* [Ring: una taglia a 4 zeri per forzare l’esecuzione in locale](https://www.securityinfo.it/2026/02/23/ring-una-taglia-a-4-zeri-per-forzare-lesecuzione-in-locale/)

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

## Google API Keys: le chiavi pubbliche diventano credenziali sensibili

Feb 27, 2026  [Redazione](https://www.securityinfo.it/author/redazione/ "Articoli scritti da Redazione")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/approfondimenti/minacce/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Tecnologia](https://www.securityinfo.it/category/approfondimenti/tecnologia/), [Tecnologia](https://www.securityinfo.it/category/news/tecnologia-news/), [Vulnerabilità](https://www.securityinfo.it/category/approfondimenti/vulnerabilita-approfondimenti/)
 [0](https://www.securityinfo.it/2026/02/27/google-api-keys-le-chiavi-pubbliche-diventano-credenziali-sensibili/#respond)

---

L’introduzione di funzionalità di **intelligenza artificiale generativa** nelle piattaforme cloud sta ridefinendo il perimetro di sicurezza delle credenziali applicative. Un caso emblematico è [stato scoperto dai ricercatori di Truffle Security Co](https://trufflesecurity.com/blog/google-api-keys-werent-secrets-but-then-gemini-changed-the-rules). e riguarda l’ecosistema Google Cloud dove le tradizionali API key — storicamente considerate semplici identificatori di progetto — hanno acquisito nuovi privilegi con l’arrivo di Gemini. Il risultato è una superficie d’attacco inattesa, in cui migliaia di chiavi pubbliche possono essere sfruttate per accedere a dati privati, consumare risorse e generare costi anche elevati.

![](https://www.securityinfo.it/wp-content/uploads/2026/02/FurtoAPI_Google-1024x683.png)

### **U****n cambio di paradigma nella gestione delle API key**

Per oltre un decennio Google ha comunicato in modo esplicito che le API key non erano né andavano trattate come segreti. La documentazione di servizi come Google Maps e Firebase **invitava infatti gli sviluppatori a inserirle direttamente nel codice client** o nelle pagine HTML, poiché il loro scopo principale era identificare il progetto ai fini di fatturazione e monitoraggio. Eventuali restrizioni, come l’allow-listing dei referer HTTP, venivano considerate controlli accessori e non meccanismi di autenticazione.

L’arrivo della Generative Language API, che abilita l’accesso a Gemini, ha però modificato radicalmente questa premessa. Quando l’API viene attivata in un progetto Google Cloud, **tutte le API key esistenti associate a quel progetto possono ottenere automaticamente accesso agli endpoint sensibili di Gemini**, senza notifiche, conferme o cambiamenti visibili nell’interfaccia di gestione. In altri termini, una chiave creata anni prima per un widget di Maps può trasformarsi silenziosamente in una credenziale capace di interrogare modelli generativi a nome di qualcun altro e accedere ai dati del progetto.

Questa dinamica introduce una forma di **espansione retroattiva dei privilegi**, in cui la sequenza temporale degli eventi diventa determinante. La chiave nasce come identificatore pubblico, l’API Gemini viene attivata successivamente e, senza alcun intervento dell’utente, la stessa chiave assume un ruolo autentico e sensibile. Il problema non è dunque una configurazione errata, ma un difetto architetturale legato a default permissivi e alla mancanza di separazione tra chiavi pubbliche e segrete.

![](https://www.securityinfo.it/wp-content/uploads/2026/02/API_NotASecret.png)

### **Default insicuri e rischio di privilege escalation**

Alla base della vulnerabilità vi è il fatto che Google utilizza un formato unico di API key (prefisso AIza…) per scenari con requisiti di sicurezza profondamente diversi. Quando una nuova chiave viene generata, **la configurazione predefinita è “unrestricted”**, rendendola valida per tutte le API abilitate nel progetto, incluse quelle generative. L’interfaccia segnala genericamente il rischio di uso non autorizzato, ma l’impostazione di default resta permissiva.

Questo scenario si allinea a due debolezze note: posture di sicurezza con default insicuri e assegnazione impropria dei privilegi. **L’assenza di separazione tra chiavi pubbliche e segrete favorisce confusione operativa e compromissioni**, mentre l’upgrade implicito dei privilegi applicato a chiavi già esposte in ambienti pubblici rappresenta una forma di trust escalation difficilmente individuabile dagli sviluppatori.

### **Lo scenario di attacco: scraping e accesso ai dati Gemini**

Dal punto di vista operativo, l’exploit è estremamente semplice. Un attaccante può visitare un sito web, **recuperare dal codice sorgente una API key** utilizzata per servizi come Maps e inviarla a un endpoint Gemini. In diversi casi analizzati, la richiesta non restituisce un errore ma una risposta valida, segno che la chiave è accettata per operazioni sensibili.

Una volta ottenuto l’accesso, il threat actor può interrogare endpoint che contengono **file caricati, dataset, documenti e contenuti cache del progetto**. Oltre alla compromissione della riservatezza dei dati, emerge il rischio economico: l’uso massivo delle API generative può generare costi elevati e saturare le quote disponibili, causando interruzioni ai servizi legittimi. L’attaccante non deve compromettere infrastrutture o credenziali interne, ma semplicemente sfruttare una chiave pubblica già esposta.

### **L’impatto reale: migliaia di chiavi vulnerabili online**

Un’analisi condotta sul dataset Common Crawl di novembre 2025 ha individuato 2.863 API key Google attive potenzialmente sfruttabili attraverso questo vettore. Tra le organizzazioni coinvolte figurano istituzioni finanziarie, **aziende di sicurezza e realtà globali del recruiting**, a dimostrazione di quanto il problema non sia limitato a progetti marginali.

Particolarmente significativo è il fatto che anche Google stessa presentasse chiavi pubbliche esposte ...