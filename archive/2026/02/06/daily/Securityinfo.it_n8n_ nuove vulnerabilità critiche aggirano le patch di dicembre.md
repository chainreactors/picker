---
title: n8n: nuove vulnerabilità critiche aggirano le patch di dicembre
url: https://www.securityinfo.it/2026/02/06/n8n-sotto-pressione-nuove-vulnerabilita-critiche-aggirano-le-patch-di-dicembre/?utm_source=rss&utm_medium=rss&utm_campaign=n8n-sotto-pressione-nuove-vulnerabilita-critiche-aggirano-le-patch-di-dicembre
source: Securityinfo.it
date: 2026-02-06
fetch_date: 2026-02-07T04:09:29.686196
---

# n8n: nuove vulnerabilità critiche aggirano le patch di dicembre

Aggiornamenti recenti Febbraio 6th, 2026 2:30 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [n8n: nuove vulnerabilità critiche aggirano le patch di dicembre](https://www.securityinfo.it/2026/02/06/n8n-sotto-pressione-nuove-vulnerabilita-critiche-aggirano-le-patch-di-dicembre/)
* [TrendAI: il 2026 sarà l’anno dell’industrializzazione del cybercrime](https://www.securityinfo.it/2026/02/06/trendai-2026-anno-industrializzazione-cybercrime/)
* [Shadow Campaign: la nuova ondata di cyber-spionaggio globale](https://www.securityinfo.it/2026/02/05/shadow-campaign-la-nuova-ondata-di-cyber-spionaggio-globale/)
* [NTLM verso lo “switch-off”: Microsoft si prepara a bloccarlo di default](https://www.securityinfo.it/2026/02/03/ntlm-verso-lo-switch-off-microsoft-si-prepara-a-bloccarlo-di-default/)
* [Abusato il sistema di update eScan per inviare malware multistage](https://www.securityinfo.it/2026/02/02/abusato-il-sistema-di-update-escan-per-inviare-malware-multistage/)

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

## n8n: nuove vulnerabilità critiche aggirano le patch di dicembre

Feb 06, 2026  [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo_security/ "Articoli scritti da Giancarlo Calzetta")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2026/02/06/n8n-sotto-pressione-nuove-vulnerabilita-critiche-aggirano-le-patch-di-dicembre/#respond)

---

La sicurezza di n8n, una delle piattaforme open source più utilizzate per l’automazione dei workflow, torna nuovamente sotto i riflettori dopo la scoperta di nuove vulnerabilità critiche che **mettono a rischio server, credenziali e processi aziendali** basati anche su intelligenza artificiale. I difetti, tracciati complessivamente come CVE-2026-25049, consentono ad attaccanti autenticati di **aggirare le contromisure introdotte solo poche settimane** fa per correggere una precedente falla di gravità quasi massima.

Il problema nasce da una gestione ancora imperfetta della sanitizzazione delle espressioni all’interno dei workflow. Nonostante le patch rilasciate a dicembre 2025 per mitigare la CVE-2025-68613, i ricercatori hanno dimostrato che **è ancora possibile inserire codice malevolo capace di superare i controlli** e arrivare all’esecuzione di comandi sul sistema host che esegue n8n. Un dettaglio che trasforma quella che dovrebbe essere una semplice automazione applicativa in un vettore di compromissione completo.

Le nuove vulnerabilità hanno ricevuto un **punteggio CVSS di 9.4**, ma diversi esperti ritengono che la valutazione non rifletta pienamente l’impatto reale negli ambienti di produzione. Il motivo è semplice: n8n non è un servizio periferico, bensì un nodo centrale in cui convergono credenziali, API key e token di accesso a servizi cloud, piattaforme SaaS e sempre più spesso modelli di intelligenza artificiale.

![](https://www.securityinfo.it/wp-content/uploads/2026/02/n8n_vulnerabilita-1024x683.png)

**Un problema di espressioni che diventa esecuzione di comandi**

Secondo quanto confermato dagli stessi maintainer di n8n in un advisory di sicurezza, un utente autenticato con i permessi per creare o modificare workflow può costruire espressioni in grado di innescare comandi di sistema non previsti. In pratica, **chi ha accesso alla logica di automazione può trasformare un parametro di workflow in un punto di ingresso** per il controllo dell’intero server.

È un aspetto particolarmente delicato perché n8n è spesso utilizzato in contesti collaborativi, dove più utenti o team hanno la possibilità di intervenire sui flussi. In questi casi, **la linea di demarcazione tra utente legittimo e attaccante interno o compromesso diventa estremamente sottile**, rendendo il modello di fiducia implicito uno dei punti più deboli della piattaforma.

**Una sequenza di incidenti che preoccupa i difensori**

La nuova disclosure arriva a breve distanza da un altro episodio particolarmente grave, noto come “ni8mare”, che **aveva esposto decine di migliaia di server n8n** alla possibile compromissione completa tramite una vulnerabilità di remote code execution sfruttabile senza autenticazione. In quel caso, bastava individuare un’istanza vulnerabile per prenderne il controllo, senza alcuna credenziale.

La frequenza con cui n8n compare nelle patch list dei team di sicurezza sta diventando un segnale d’allarme. Non tanto per la presenza di bug in sé, inevitabili in qualsiasi software complesso, quanto per **la loro natura sistemica e per il tipo di accesso che rendono possibile**. Ogni nuova falla sembra confermare quanto le piattaforme di automazione siano ormai infrastrutture critiche a tutti gli effetti.

**Il valore dei dati custoditi nei workflow**

A sottolineare la gravità del problema è anche Pillar Security, una delle realtà che hanno contribuito alla scoperta delle nuove vulnerabilità. Secondo i ricercatori, l’aspetto più pericoloso non è solo la possibilità di eseguire codice, ma il contesto in cui questo avviene. Un server n8n compromesso equivale spesso a **un archivio aperto di segreti digitali**.

Chi riesce a sfruttare la vulnerabilità può ottenere accesso a **chiavi API di servizi come OpenAI o Anthropic, credenziali cloud per ambienti AWS e token** utilizzati per orchestrare processi aziendali complessi. Il tutto senza necessariamente interrompere i workflow, che continuano a funzionare normalmente, rendendo l’attacco estremamente silenzioso.

Secondo Eilon Cohen, ricercatore di sicurezza AI presso Pillar Security, la combinazione tra semplicità di sfruttamento e valore degli asset esposti **rende queste vulnerabilità particolarmente appetibili**. In sostanza, la capacità di creare un workflow equivale, in alcuni contesti, alla possibilità di “possedere” l’intero server.

**Patch disponibili, ma il problema resta strutturale**

n8n ha rilasciato gli aggiornamenti correttivi per CVE-2026-25049 e invita gli utenti ad applicarli immediatamente. Allo stesso tempo, **gli esperti raccomandano un approccio più ampio che includa una revisione rigorosa dei permessi utente**, un’analisi dei workflow esistenti e la rotazione delle credenziali sensibili, soprattutto quelle legate a servizi cloud e AI.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [AI workflow security](https://www.securityinfo.it/tag/ai-workflow-security/), [API key exposure](https://www.securityinfo.it/tag/api-key-exposure/), [attacchi ai workflow](https://www.securityinfo.it/tag/attacchi-ai-workflow/), [automazione aziendale](https://www.securityinfo.it/tag/automazione-aziendale/), [credential theft](https://www.securityinfo.it/tag/credential-theft/), [CVE-2025-68613](https://www.securityinfo.it...