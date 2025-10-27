---
title: Una vulnerabilità di Open VSX Registry mette in pericolo milioni di sviluppatori
url: https://www.securityinfo.it/2025/06/30/una-vulnerabilita-di-open-vsx-registry-mette-in-pericolo-milioni-di-sviluppatori/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-01
fetch_date: 2025-10-06T23:57:48.371926
---

# Una vulnerabilità di Open VSX Registry mette in pericolo milioni di sviluppatori

Aggiornamenti recenti Ottobre 6th, 2025 5:03 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Impennata delle scansioni dei portali di login di Palo Alto Networks: +500%](https://www.securityinfo.it/2025/10/06/impennata-delle-scansioni-dei-portali-di-login-di-palo-alto-networks-500/)
* [Microsoft Sentinel: arriva l’era degli agenti AI e della difesa predittiva](https://www.securityinfo.it/2025/10/06/microsoft-sentinel-arriva-lera-degli-agenti-ai-e-della-difesa-predittiva/)
* [CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)

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

## Una vulnerabilità di Open VSX Registry mette in pericolo milioni di sviluppatori

Giu 30, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/06/30/una-vulnerabilita-di-open-vsx-registry-mette-in-pericolo-milioni-di-sviluppatori/#respond)

---

I ricercatori di Koi Security hanno individuato un**a vulnerabilità critica di Open VSX Registry** che consente agli attaccanti di **prendere il controllo dei dispositivi di milioni di sviluppatori**pubblicando **estensioni malevole per VSCode.**

Open VSX Registry è un’estensione della Eclipse Foundation usata in VSCode per accedere a un marketplace di estensioni “vendor neutral”, così che gli sviluppatori possono utilizzare estensioni che non siano di Microsoft. “*In pratica, **Open VSX funziona quasi esattamente come il Marketplace ufficiale di VS Code, ma è aperto a qualsiasi fork di VS Code**. Gli sviluppatori possono pubblicare estensioni su Open VSX e gli utenti dei fork di VS Code possono installarle senza problemi*” [spiega](https://blog.koi.security/marketplace-takeover-how-we-couldve-taken-over-every-developer-using-a-vscode-fork-f0f8cf104d44) Oren Yomtov di Koi Security.

![Open VSX Registry](https://www.securityinfo.it/wp-content/uploads/2025/06/Gemini_Generated_Image_envuueenvuueenvu.png)

Considerando che, secondo quanto riportato da Yomtov, sono oltre 8 milioni gli sviluppatori che usano Open VSX, la vulnerabilità dell’estensione ha degli impatti catastrofici e apre ad attacchi supply-chain molto estesi.

Il bug risiede in **publish-extensions,** ovvero il meccanismo che serve a popolare di estensioni Open VSX. Questo meccanismo consente agli sviluppatori di pubblicare delle estensioni inviando una pull request; una volta approvata, l’estensione viene aggiunta al file `extensions.json`.

Per far sì che le estensioni siano sempre aggiornate all’ultima versione, esiste un flusso quotidiano che, per ogni estensione del file, controlla se la versione specificata nel file package.json è diversa da quella attuale; in caso positivo, viene eseguito il comando npm install per aggiornare le dipendenze e la nuova versione dell’estensione viene pubblicata. Quest’ultimo step utilizza il valore della variabile d’ambiente OVSX\_PAT, ovvero un token relativo a privilegi elevati che consente di **pubblicare qualsiasi estensione sul marketplace**.

La vulnerabilità sta nel fatto che npm install esegue gli script di build di tutte le estensioni presenti nel marketplace dando loro l’accesso alla variabile OVSX\_PAT. I ricercatori di Koi Security hanno dimostrato che **è possibile esfiltrare il token**e di conseguenza **usarlo per pubblicare nuove estensioni o compromettere quelle esistenti con aggiornamenti malevoli.**

“*Dal punto di vista di un attaccante, ciò significa prendere il controllo della supply chain dell’intero ecosistema. Quando l’IDE di uno sviluppatore fa un aggiornamento automatico delle estensioni (o se l’utente ne installa una nuova), viene scaricato automaticamente il payload malevolo*” sottolinea Yomtov. Con questo potere un attaccante può praticamente **prendere il controllo del dispositivo della vittima** e inserire keylogger o backdoor nei progetti degli sviluppatori, nonché **sottrarre codice sorgente e cookie**.

![](https://www.securityinfo.it/wp-content/uploads/2025/05/hacker-6512174_1920.jpg)

## Ridurre l’impatto del problema di Open VSX Registry

Poiché le estensioni scaricate dal marketplace possono essere caricate da chiunque, Yomtov ricorda che è essenziale prestare la massima attenzione a ciò che si installa, **considerando ogni dipendenza come se fosse non attendibile.**

Questo, spiega Yomtov, implica **definire un inventario**delle estensioni installate, memorizzando non solo *cosa* è installato, ma anche *su quali macchine*e *da chi è usato*. Fondamentale è anche verificare **l’origine di ciascuna estensione**, controllare se viene manutenuta regolarmente, **quali permessi richiede** e perché.

Per agire su eventuali comportamenti anomali delle dipendenze di terze parti, è importante definire delle **azioni di risposta in caso di violazione delle policy**, per esempio rimuovendo automaticamente i plugin sospetti o inviando un alert al team di sicurezza.

Infine, poiché le estensioni vengono spesso aggiornate senza avvisi e in maniera automatica, è obbligatorio **controllarle continuamente per non perdersi alcun flusso di aggiornamento.**

*“Bisognerebbe **adottare un modello zero-trust per ogni software proveniente da marketplace**, trattando ogni applicazione, estensione, plugin, modello, MCP, pacchetto di codice o container come non attendibile finché non viene individuato, analizzato, approvato e monitorato*” conclude Yomtov.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [attacchi supply chain](https://www.securityinfo.it/tag/attacchi-supply-chain/), [estensioni](https://www.securityinfo.it/tag/estensioni/), [Open VSX Registry](https://www.securityinfo.it/tag/open-vsx-registry/), [software terzi](https://www.securityinfo.it/tag/software-terzi/), [Visual Studio Code](https://www.securityinfo.it/tag/visual-studio-code/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[In aumento i cyberattacchi dall'Iran: l'allarme delle agenzie di sicurezza americane](https://www.securityinfo.it/2025/07/01/in-aumento-i-cyberattacchi-dall-iran-lallarme-delle-agenzie-di-sicurezza-americane/)
[Le stampanti multifunzione sono piene di bug! Uno...