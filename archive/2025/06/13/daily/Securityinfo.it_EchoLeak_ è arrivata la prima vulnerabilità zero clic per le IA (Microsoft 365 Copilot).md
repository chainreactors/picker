---
title: EchoLeak: è arrivata la prima vulnerabilità zero clic per le IA (Microsoft 365 Copilot)
url: https://www.securityinfo.it/2025/06/13/echoleak-e-arrivata-la-prima-vulnerabilita-zero-clic-per-le-ia-microsoft-365-copilot/?utm_source=rss&utm_medium=rss&utm_campaign=echoleak-e-arrivata-la-prima-vulnerabilita-zero-clic-per-le-ia-microsoft-365-copilot
source: Securityinfo.it
date: 2025-06-13
fetch_date: 2025-10-06T23:00:00.823701
---

# EchoLeak: è arrivata la prima vulnerabilità zero clic per le IA (Microsoft 365 Copilot)

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

## EchoLeak: è arrivata la prima vulnerabilità zero clic per le IA (Microsoft 365 Copilot)

Giu 13, 2025  [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo_security/ "Articoli scritti da Giancarlo Calzetta")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [Hacking](https://www.securityinfo.it/category/news/hacking-news/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/06/13/echoleak-e-arrivata-la-prima-vulnerabilita-zero-clic-per-le-ia-microsoft-365-copilot/#respond)

---

Nel gennaio 2025, i ricercatori di Aim Labs hanno scoperto un nuovo tipo di attacco che cambia le regole della sicurezza per i sistemi basati su intelligenza artificiale. **EchoLeak è la prima vulnerabilità zero-click nota che consente di estrarre dati sensibili da Microsoft 365 Copilot senza alcuna interazione da parte dell’utente.** La gravità della falla ha spinto Microsoft ad assegnarle un codice CVE (CVE-2025-32711) e a classificarla come critica, con una correzione già distribuita lato server a maggio.

Secondo quanto dichiarato da Microsoft, non ci sono prove di sfruttamenti reali e nessun utente è stato colpito. **La vulnerabilità è stata quindi risolta prima di causare danni concreti, ma rappresenta un precedente pericoloso.** **Dimostra infatti che anche i sistemi apparentemente protetti da barriere interne possono essere manipolati sfruttando le dinamiche dei modelli linguistici.**

![](https://www.securityinfo.it/wp-content/uploads/2025/06/LLMScope13-giu-2025CG-1024x683.png)

Microsoft 365 Copilot integra i modelli GPT con Graph proprietario per assistere gli utenti nelle applicazioni di Office, dall’analisi dei dati alla redazione dei contenuti. **Il cuore della vulnerabilità risiede nel modo in cui l’IA gestisce e comprende il contesto, specialmente quando entra in gioco il Retrieval-Augmented Generation (RAG).** **Anche senza codice eseguibile, una semplice frase strutturata nel modo giusto può indurre il sistema a comportarsi in modo anomalo.** Dal momento che Microsoft 365 assite l’utente in molte delle applicazioni office, da outlook a word passando per excel e powerpoint, la superficie d’attacco era molto ampia.

EchoLeak rientra in una nuova categoria di vulnerabilità, nota come *LLM Scope Violation*, in cui il modello linguistico accede e diffonde dati riservati pur non essendo autorizzato. **Il modello viene ingannato con istruzioni nascoste che agiscono all’interno del prompt, eludendo i sistemi di difesa automatica come XPIA.** **Questo comportamento può essere sfruttato in modo automatico e silenzioso in ambienti aziendali complessi.**

Nel caso specifico, tutto inizia con l’invio di una email costruita per sembrare innocua, ma che contiene una prompt injection invisibile all’utente. **Quando l’utente, anche giorni dopo, pone a Copilot una domanda correlata, la mail viene recuperata e inserita nel contesto operativo del modello.** **A quel punto, il codice nascosto guida il sistema verso la raccolta di dati interni, che vengono poi inglobati in link o immagini.**

Il meccanismo sfrutta il fatto che alcuni formati grafici attivano automaticamente richieste verso URL esterni. **In questo modo, anche senza clic o conferme, i dati possono essere inviati ai server dell’attaccante.** **Domini come quelli di Teams e SharePoint sono ritenuti attendibili dal sistema e possono quindi fungere da veicoli perfetti per l’esfiltrazione.**

Benché la falla sia stata corretta, la sua scoperta solleva interrogativi sull’efficacia delle difese tradizionali. **Con la crescente integrazione di LLM nei flussi di lavoro, nuove vulnerabilità di questo tipo sono destinate a emergere.** Per proteggersi, le aziende devono rafforzare i sistemi di controllo dei prompt in ingresso, applicare filtri post-elaborazione alle risposte generate e impedire la generazione automatica di link o dati strutturati. **È altrettanto fondamentale configurare i motori RAG per evitare il recupero di contenuti potenzialmente dannosi provenienti da email, documenti o repository non verificati.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [AI vulnerability zero-click](https://www.securityinfo.it/tag/ai-vulnerability-zero-click/), [EchoLeak attacco](https://www.securityinfo.it/tag/echoleak-attacco/), [exfiltrazione dati AI](https://www.securityinfo.it/tag/exfiltrazione-dati-ai/), [LLM scope violation](https://www.securityinfo.it/tag/llm-scope-violation/), [Microsoft 365 Copilot](https://www.securityinfo.it/tag/microsoft-365-copilot/), [prompt injection AI](https://www.securityinfo.it/tag/prompt-injection-ai/), [RAG engine sicurezza](https://www.securityinfo.it/tag/rag-engine-sicurezza/)

[Anubis, un nuovo ransomware che integra un wiper](https://www.securityinfo.it/2025/06/16/anubis-un-nuovo-ransomware-che-integra-un-wiper/)
[Smartwatch e attacchi acustici: nuova minaccia alle reti isolate](https://www.securityinfo.it/2025/06/12/smartwatch-e-attacchi-acustici-nuova-minaccia-alle-reti-isolate/)

---

![](https://secure.gravatar.com/avatar/d6a6ecdad542d883704003e541413ca8?s=90&d=mm&r=g)

##### [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo_security/)

##### Articoli correlati

* [![Lenovo, il chatbot AI “Lena” era troppo loquace](https://www.securityinfo.it/wp-content/uploads/2025/08/Lenovo20-ago-2025CG-120x85.png)](https://www.securityinfo.it/2025/08/20/lenovo-il-chatbot-ai-lena-era-troppo-loquace/ "Lenovo, il chatbot AI “Lena” era troppo loquace")

  [Lenovo, il chatbot AI “Lena” era...](https://www.securityinfo.it/2025/08/20/lenovo-il-chatbot-ai-lena-era-troppo-loquace/ "Permanent link to Lenovo, il chatbot AI “Lena” era troppo loquace")

  Ago 20, 2025  [0](http...