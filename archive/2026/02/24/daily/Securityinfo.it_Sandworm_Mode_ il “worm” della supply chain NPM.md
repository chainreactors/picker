---
title: Sandworm_Mode: il “worm” della supply chain NPM
url: https://www.securityinfo.it/2026/02/24/sandworm_mode-il-worm-della-supply-chain-npm/?utm_source=rss&utm_medium=rss&utm_campaign=sandworm_mode-il-worm-della-supply-chain-npm
source: Securityinfo.it
date: 2026-02-24
fetch_date: 2026-02-25T04:14:49.905074
---

# Sandworm_Mode: il “worm” della supply chain NPM

Aggiornamenti recenti Febbraio 24th, 2026 2:49 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Sandworm\_Mode: il “worm” della supply chain NPM](https://www.securityinfo.it/2026/02/24/sandworm_mode-il-worm-della-supply-chain-npm/)
* [Ring: una taglia a 4 zeri per forzare l’esecuzione in locale](https://www.securityinfo.it/2026/02/23/ring-una-taglia-a-4-zeri-per-forzare-lesecuzione-in-locale/)
* [Finanza nel mirino, incidenti raddoppiati nel 2025](https://www.securityinfo.it/2026/02/20/finanza-nel-mirino-incidenti-raddoppiati-nel-2025/)
* [Davvero si può fare “jailbreak” di un caccia F-35?](https://www.securityinfo.it/2026/02/18/davvero-si-puo-fare-jailbreak-a-un-caccia-f-35/)
* [Il malware che ruba password e ambienti delle IA locali](https://www.securityinfo.it/2026/02/17/il-malware-che-ruba-password-e-ambienti-delle-ia-locali/)

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

## Sandworm\_Mode: il “worm” della supply chain NPM

Feb 24, 2026  [Redazione](https://www.securityinfo.it/author/redazione/ "Articoli scritti da Redazione")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [Scenari](https://www.securityinfo.it/category/scenari/), [Tecnologia](https://www.securityinfo.it/category/news/tecnologia-news/)
 [0](https://www.securityinfo.it/2026/02/24/sandworm_mode-il-worm-della-supply-chain-npm/#respond)

---

##### **Un attacco che riprende la logica Shai-Hulud, ma sposta l’asticella sul toolchain moderno**

Una recente analisi dei  ricercatori di Socket, un’azienda specializzata in sicurezza informatica, ha svelato una nuova campagna d’attacco alla supply chain dello sviluppo software colpendo NPM, l’ecosistema dove risiedono migliaia di librerie Javascript largamente usate dai programmatori di tutto il mondo. L’attacco è stato descritto come **Sandworm\_Mode con capacità di propagazione “worm-like”**, costruita per scalare velocemente sfruttando la fiducia dell’ecosistema JavaScript e le abitudini quotidiane degli sviluppatori. L’operazione è stata attribuita a un cluster di **almeno 19 pacchetti malevoli** pubblicati tramite due alias e progettati per ingannare tramite typosquatting, cioè con nomi “quasi identici” a utility note, tool crypto e perfino strumenti legati al coding assistito dall’AI.

![](https://www.securityinfo.it/wp-content/uploads/2026/02/ShaiUlud_NPM-1024x683.png)

### **Typosquatting su utility, crypto e AI coding: l’innesco che porta il malware in pipeline**

Il meccanismo d’ingresso è semplice e pericolosamente efficace: **pacchetti che si presentano come dipendenze plausibili per attività comuni** (sviluppo, parsing, compatibilità, tool “di supporto”) e che, una volta installati o richiamati, avviano una catena di esecuzione malevola. Le fonti convergono sul fatto che i pacchetti sono stati rimossi dal registry, ma il rischio resta per chi li abbia già introdotti nelle build locali o CI (continuous Integration)/CD (Contiuous Delivery), dove l’automazione moltiplica l’impatto.

Il salto di qualità rispetto al classico malware da pacchetto è nella propagazione: **Sandworm\_Mode abusa di credenziali NPM e GitHub sottratte per muoversi lateralmente** e affianca questo canale a una GitHub Action manipolata che punta a raccogliere ed esfiltrare segreti di CI. Il modello, descritto come affine alla precedente ondata “Shai-Hulud”, consente non solo di colpire la singola workstation dello sviluppatore, ma di trasformare repository e pipeline in moltiplicatori di compromissione.

Un dettaglio particolarmente insidioso è la possibilità di usare pacchetti “vettore” per innescare workflow via GitHub Actions: **basta aggiungere una dipendenza che attiva un percorso di pull request e workflow per arrivare ai segreti del repository** e provare a iniettare ulteriori dipendenze o automatismi. È una dinamica che rende più difficile distinguere l’attacco da attività legittime, soprattutto in progetti molto attivi e con automazioni estese.

### **L’AI come nuova superficie d’attacco: iniezione di un server MCP “rogue” e prompt injection**

La parte più attuale della campagna è l’aggancio agli assistenti di coding. Le analisi riportano che **il malware installa un server MCP locale malevolo e lo registra nelle configurazioni di più strumenti**, puntando a piattaforme come Claude Code, Cursor, Continue e Windsurf. L’idea è avvelenare l’interfaccia “fidata” tra sviluppatore e AI: tramite prompt injection, l’assistente viene indotto a leggere e consegnare informazioni sensibili (chiavi SSH, credenziali cloud, token NPM e segreti vari) verso il canale controllato dall’attaccante.

Non si parla solo di credenziali “classiche”. **Sandworm\_Mode mira esplicitamente anche alle API key dei provider LLM**, oltre a environment variables e file .env, con logiche di validazione per capire cosa valga la pena monetizzare o riutilizzare. In parallelo, viene descritto un harvesting più profondo che include anche dati provenienti da password manager, a conferma della volontà di massimizzare l’accesso persistente agli ambienti di sviluppo.

### **Offuscamento assistito da Ollama: quando la “difesa” diventa mimetismo del payload**

Un altro elemento interessante è l’uso di tooling locale per rendere il codice meno leggibile: **il malware invoca un’istanza locale di Ollama per riscrivere porzioni del codice**, cambiare nomi di variabili, alterare flussi di controllo, inserire delle esche e codificare stringhe. Non è “AI magica”, ma è un modo pragmatico per aumentare l’attrito per chi analizza e per le difese basate su firme, sfruttando risorse già presenti su molte workstation moderne.

Secondo Socket, la campagna adotta **una strategia a due tempi**: prima parte immediata e incondizionata dedicata alle operazioni più “profittevoli” (come il furto di chiavi legate al mondo crypto), seguita da attività più rumorose e “lunghe” come persistenza, propagazione e raccolta estesa di segreti. La razionalità è chiara: colpire subito, poi ridurre la probabilità di essere intercettati da sandbox o analisi “mordi e fuggi” tipiche delle prime ore.

Le analisi citano anche **una capacità di dead switch configurabile ma inattiva**, pensata per arrivare a una cancellazione della home directory nel caso in cui il malware perda accesso o non riesca più a operare con gli account compromessi. Anche se disabilitata nei campioni analizzati, la sola presenza del meccanismo segnala una postura offensiva pronta a passare dalla monetizzazione alla distruzione, se necessario.

### **Cosa fare ora: bonifica, rotazione credenziali e caccia ai workflow sospetti**

La remediation non è “disinstallare e basta”. **Chiunque sospetti l’installazione di uno dei pacchetti deve considerare compromessi token e segreti**, perché l’attacco è costruito per muoversi tra macchina locale e CI. La linea operativa indicata dalle fonti è rimuovere...