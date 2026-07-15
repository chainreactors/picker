---
title: Gli assistenti AI di coding sono sicuri? Il caso xAI
url: https://www.securityinfo.it/2026/07/14/gli-assistenti-ai-di-coding-sono-sicuri-il-caso-xai/?utm_source=rss&utm_medium=rss&utm_campaign=gli-assistenti-ai-di-coding-sono-sicuri-il-caso-xai
source: Securityinfo.it
date: 2026-07-14
fetch_date: 2026-07-15T04:49:40.051322
---

# Gli assistenti AI di coding sono sicuri? Il caso xAI

Aggiornamenti recenti Luglio 14th, 2026 4:02 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Gli assistenti AI di coding sono sicuri? Il caso xAI](https://www.securityinfo.it/2026/07/14/gli-assistenti-ai-di-coding-sono-sicuri-il-caso-xai/)
* [La guerra ucraina cambia la cybersecurity delle infrastrutture critiche](https://www.securityinfo.it/2026/07/10/la-guerra-ucraina-cambia-la-cybersecurity-delle-infrastrutture-critiche/)
* [AI, il nuovo fronte della sicurezza: il red teaming diventa indispensabile](https://www.securityinfo.it/2026/07/06/ai-il-nuovo-fronte-della-sicurezza-il-red-teaming-diventa-indispensabile/)
* [Falsa skill elude gli scanner e a raggiunge più di 26.000 agenti AI](https://www.securityinfo.it/2026/06/21/una-falsa-skill-elude-gli-scanner-e-a-raggiunge-piu-di-26-000-agenti-ai/)
* [Zscaler porta la Zero Trust nell’era degli agenti AI](https://www.securityinfo.it/2026/06/16/zscaler-porta-la-zero-trust-nellera-degli-agenti-ai/)

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

## Gli assistenti AI di coding sono sicuri? Il caso xAI

Lug 14, 2026  [Redazione](https://www.securityinfo.it/author/redazione/ "Articoli scritti da Redazione")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Scenario](https://www.securityinfo.it/category/news/scenario-news/), [Tecnologia](https://www.securityinfo.it/category/news/tecnologia-news/)
 [0](https://www.securityinfo.it/2026/07/14/gli-assistenti-ai-di-coding-sono-sicuri-il-caso-xai/#respond)

---

Gli strumenti di **AI per lo sviluppo software** promettono di aumentare la produttività degli sviluppatori, ma una recente analisi indipendente riaccende il dibattito sulla sicurezza dei dati affidati agli assistenti di coding. Al centro della vicenda c’è **Grok Build**, il tool a riga di comando di xAI, accusato di aver trasmesso (in chiaro) ai server dell’azienda interi repository Git, cronologia compresa, insieme a file contenenti credenziali e altri dati sensibili. Secondo il ricercatore che ha condotto l’analisi, inoltre, il comportamento sarebbe avvenuto anche dopo aver attivato l’opzione di esclusione dall’addestramento del modello.

![](https://www.securityinfo.it/wp-content/uploads/2026/07/AICoder-1024x683.png)

### **Un’analisi del traffico di rete fa emergere il problema**

La vicenda nasce dall’analisi del traffico di rete effettuata dal ricercatore noto come **cereblab**, che ha instradato Grok Build attraverso **mitmproxy** per osservare nel dettaglio le comunicazioni tra il client e i server remoti. L’obiettivo era verificare quali dati venissero realmente inviati durante una normale sessione di sviluppo. I risultati non sono stati quelli sperati. Secondo il report, il software avrebbe aperto due canali distinti di comunicazione: uno destinato alle richieste del modello AI e un secondo utilizzato per il caricamento del codice (un comportamento decisamente non atteso e che ha allarmato il ricercatore).

Nel test effettuato su un repository Git di circa **12 GB**, il traffico destinato al modello AI sarebbe stato limitato a circa **192 KB**, mentre il canale di storage avrebbe trasferito **5,10 GiB** di dati suddivisi in **73 blocchi** da circa 75 MB ciascuno. Il rapporto tra i due flussi supera le **27.800 volte**, un valore incompatibile con il semplice invio del contesto necessario alla conversazione con il modello e che di solito giustifica connessioni parallele. L’analisi sostiene inoltre che il contenuto inviato corrispondesse a un **bundle Git completo**, comprendente non solo i file correnti ma anche la cronologia del repository.

### **Anche i segreti sarebbero finiti nel trasferimento**

Ancora più delicata è la parte relativa ai **secret** presenti nel progetto. Durante il test il ricercatore ha inserito volutamente un file **.env** contenente chiavi API e credenziali fittizie facilmente identificabili. Secondo quanto documentato, tali informazioni sarebbero state trasmesse integralmente durante la comunicazione con i server di xAI. Inoltre, ricostruendo il bundle Git catturato durante il trasferimento, il ricercatore afferma di aver recuperato anche un file che l’agente era stato esplicitamente istruito **a non leggere**, suggerendo che il caricamento del repository fosse indipendente dalle operazioni realmente effettuate dal modello.

Uno degli aspetti più controversi, secondo cerelab, riguarda l’impostazione **“Improve the model”**, utilizzata per escludere i propri dati dall’addestramento dell’intelligenza artificiale. Secondo la sua analisi, la disattivazione di questa opzione **non avrebbe impedito il trasferimento del repository**, ma soltanto il suo eventuale utilizzo per l’addestramento del modello. In altre parole, il codice continuerebbe comunque a lasciare la macchina dello sviluppatore per essere archiviato sui sistemi remoti. Si tratta di una distinzione importante, perché **trasmissione**, **archiviazione** e **addestramento** rappresentano tre aspetti differenti dal punto di vista della sicurezza e della conformità normativa.

### **xAI avrebbe già modificato il comportamento del servizio**

La vicenda, tuttavia, sembra aver avuto un’evoluzione molto rapida. Nei giorni successivi alla pubblicazione del report, lo stesso ricercatore ha ripetuto i test osservando un comportamento differente. In sei prove consecutive non sarebbe più stato rilevato alcun caricamento del repository tramite l’endpoint dedicato allo storage. Al suo posto sarebbero comparsi nuovi flag server-side, tra cui **disable\_codebase\_upload**, che sembrerebbero disattivare la funzione senza richiedere un aggiornamento del client. Al momento, però, **xAI non ha pubblicato alcun advisory di sicurezza**, né un changelog che spieghi ufficialmente la modifica o chiarisca quale sia stato l’impatto del problema sugli utenti che hanno utilizzato Grok Build prima della mitigazione. Anche le note di rilascio più recenti del progetto non fanno riferimento alla questione.

### **Una lezione per tutti gli agenti di coding**

Al di là del singolo caso, l’episodio evidenzia una criticità destinata a diventare sempre più rilevante con la diffusione degli **AI coding agent**. Molti sviluppatori tendono infatti a considerare questi strumenti come semplici assistenti locali, mentre nella maggior parte dei casi il lavoro viene svolto su infrastrutture cloud. Per le organizzazioni questo significa che **repository, codice proprietario, segreti applicativi e informazioni sensibili potrebbero lasciare il perimetro aziendale** se non vengono definite precise policy di utilizzo. E addirittura, questo potrebbe succedere anche se le opzioni di non condivisione sono attive, richiedendo una infrastruttura di controllo che vada oltre la semplice policy.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [.env](https://www.securityinfo.it/tag/env/), [AI coding a...