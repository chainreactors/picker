---
title: Rischio AI: falle in Amazon Bedrock, LangSmith e SGLang
url: https://www.securityinfo.it/2026/03/17/rischio-ai-falle-in-amazon-bedrock-langsmith-e-sglang/?utm_source=rss&utm_medium=rss&utm_campaign=rischio-ai-falle-in-amazon-bedrock-langsmith-e-sglang
source: Securityinfo.it
date: 2026-03-17
fetch_date: 2026-03-18T04:22:20.396338
---

# Rischio AI: falle in Amazon Bedrock, LangSmith e SGLang

Aggiornamenti recenti Marzo 17th, 2026 4:00 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Rischio AI: falle in Amazon Bedrock, LangSmith e SGLang](https://www.securityinfo.it/2026/03/17/rischio-ai-falle-in-amazon-bedrock-langsmith-e-sglang/)
* [CrackArmor, nove falle in AppArmor aprono la strada al root di Linux](https://www.securityinfo.it/2026/03/16/crackarmor-nove-falle-in-apparmor-aprono-la-strada-al-root-di-linux/)
* [I sistemi multi-agent aggirano controlli, rubano segreti ed esfiltrano](https://www.securityinfo.it/2026/03/13/incredibile-come-i-sistemi-multi-agent-possano-aggirare-i-controlli-rubare-segreti-e-diventare-minacce/)
* [Rapporto Clusit 2026: gli attacchi cyber crescono del 49%](https://www.securityinfo.it/2026/03/11/rapporto-clusit-2026-gli-attacchi-cyber-crescono-del-49/)
* [Plug-in di Chrome cambiano proprietà e diventano malware](https://www.securityinfo.it/2026/03/10/plug-in-di-chrome-cambiano-proprieta-e-diventano-malware/)

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

## Rischio AI: falle in Amazon Bedrock, LangSmith e SGLang

Mar 17, 2026  [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo_security/ "Articoli scritti da Giancarlo Calzetta")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2026/03/17/rischio-ai-falle-in-amazon-bedrock-langsmith-e-sglang/#respond)

---

Le più recenti ricerche di BeyondTrust, Miggo e Orca Security dimostrano che **anche piattaforme progettate per garantire isolamento e protezione – come sandbox AI, sistemi di osservabilità e framework LLM – possono trasformarsi in vettori di attacco avanzati**.

Le vulnerabilità individuate in Amazon Bedrock, LangSmith e SGLang evidenziano un punto critico che in molti si aspettavano: **l’adozione accelerata degli agenti AI sta ampliando la superficie di attacco ben oltre i modelli tradizionali**, introducendo nuove modalità di compromissione che sfruttano meccanismi apparentemente innocui come DNS, URL o serializzazione dei dati. Come al solito, la velocità (di sviluppo, adozione e implementazioe) è nemica della sicurezza, soprattutto in caso di scenari complessi come quelli che si aprono con l’adozione dell’AI e dei suoi agenti.

![](https://www.securityinfo.it/wp-content/uploads/2026/03/ChatGPT-Image-18-mar-2026-00_46_24-1024x683.png)

#### **DNS: come aggirare l’isolamento di Amazon Bedrock**

Il caso più emblematico riguarda Amazon Bedrock AgentCore Code Interpreter. Il servizio è stato progettato per consentire agli agenti AI di eseguire codice in ambienti sandbox isolati, teoricamente senza accesso alla rete. Tuttavia, la ricerca di BeyondTrust dimostra che **la possibilità di effettuare query DNS in uscita compromette di fatto questo isolamento**.

Il punto critico è che **anche in modalità “no network access”, il sistema consente la risoluzione DNS**, aprendo la strada a un canale di comunicazione nascosto. Attraverso questo meccanismo, un attaccante può costruire un’infrastruttura di comando e controllo basata su DNS, utilizzando richieste e risposte per scambiare dati e istruzioni.

In uno scenario di attacco realistico, **l’agente AI può essere trasformato in un terminale remoto controllato dall’esterno**, capace di eseguire comandi, ricevere payload e restituire risultati. Il meccanismo può arrivare fino alla creazione di una reverse shell interattiva, sfruttando record DNS per trasmettere comandi e ricevere output.

Ancora più critico è il tema delle autorizzazioni. Il Code Interpreter opera con un ruolo IAM che può accedere a risorse AWS come bucket S3. Se questo ruolo è sovra-privilegiato, **l’attaccante può utilizzare il canale DNS per esfiltrare dati sensibili direttamente da risorse cloud aziendali**, bypassando completamente i controlli di isolamento previsti.

Il rischio, quindi, non è solo teorico. **La combinazione tra accesso ai dati, capacità di esecuzione e comunicazione “covert” rende questi ambienti assimilabili a dipendenti compromessi** con impatti potenziali su disponibilità dei sistemi, integrità dei dati e riservatezza delle informazioni.

Amazon ha classificato questo comportamento come funzionalità prevista, raccomandando l’utilizzo della modalità VPC per un isolamento completo e l’adozione di DNS firewall. Questo implica un cambiamento importante di prospettiva: **la sicurezza degli agenti AI non può più essere delegata al modello di default, ma richiede configurazioni esplicite e governance rigorosa**.

#### **LangSmith e il rischio account takeover: quando l’osservabilità diventa un punto debole**

Se il caso Bedrock evidenzia problemi infrastrutturali, la vulnerabilità scoperta in LangSmith mostra come anche le piattaforme di osservabilità AI possano diventare vettori critici di compromissione.

La falla, identificata come CVE-2026-25750 con un punteggio CVSS di 8.5, deriva da una **mancata validazione del parametro baseUrl**, che consente un attacco di tipo URL injection. In pratica, un attaccante può costruire un link malevolo che induce la piattaforma a inviare dati sensibili verso un server controllato.

Il meccanismo è particolarmente insidioso perché richiede solo l’interazione dell’utente. **È sufficiente che un utente autenticato clicchi su un link appositamente costruito per esporre token di accesso, identificativi utente e informazioni sul workspace**.

Una volta ottenuto l’accesso, l’attaccante può entrare nel cuore delle operazioni AI. LangSmith gestisce infatti chiamate agli strumenti e flussi applicativi. Questo significa che **l’attaccante può accedere a query SQL interne, dati CRM, log operativi e persino codice proprietario** trasformando una vulnerabilità apparentemente semplice in un attacco ad alto impatto informativo.

La vulnerabilità è stata corretta nella versione 0.12.71 rilasciata a dicembre 2025, ma il caso evidenzia un tema strutturale: **le piattaforme di AI observability stanno diventando infrastrutture critiche e, come tali, devono essere trattate con lo stesso livello di sicurezza dei sistemi core aziendali**.

#### **SGLang e la deserializzazione pericolosa: RCE senza autenticazione**

Il terzo fronte riguarda SGLang, framework open source per l’esecuzione di modelli AI, dove sono state individuate vulnerabilità ancora più critiche, con punteggi CVSS fino a 9.8.

Il problema principale è legato alla gestione della deserializzazione tramite pickle, una funzione Python potente ma intrinsecamente pericolosa. In diversi componenti del framework, **dati non fidati vengono deserializzati senza controlli adeguati**, aprendo la strada a esecuzione di codice remoto.

Le vulnerabilità più gravi consentono **remote code execution senza autenticazione attraverso il broker ZeroMQ**, a condizione che l’attaccante possa raggiunge...