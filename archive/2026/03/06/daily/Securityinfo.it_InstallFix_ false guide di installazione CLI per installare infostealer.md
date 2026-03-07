---
title: InstallFix: false guide di installazione CLI per installare infostealer
url: https://www.securityinfo.it/2026/03/06/installfix-false-guide-di-installazione-cli-per-installare-infostealer/?utm_source=rss&utm_medium=rss&utm_campaign=installfix-false-guide-di-installazione-cli-per-installare-infostealer
source: Securityinfo.it
date: 2026-03-06
fetch_date: 2026-03-07T03:56:54.718703
---

# InstallFix: false guide di installazione CLI per installare infostealer

Aggiornamenti recenti Marzo 6th, 2026 2:30 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [InstallFix: false guide di installazione CLI per installare infostealer](https://www.securityinfo.it/2026/03/06/installfix-false-guide-di-installazione-cli-per-installare-infostealer/)
* [Cybercrime e AI: l’attribuzione degli attacchi diventa sempre più difficile](https://www.securityinfo.it/2026/03/05/cybercrime-e-ai-lattribuzione-degli-attacchi-diventa-sempre-piu-difficile/)
* [Phishing OAuth: campagne contro enti pubblici sfruttano Microsoft](https://www.securityinfo.it/2026/03/04/phishing-via-oauth-campagne-contro-enti-pubblici-sfruttano-i-redirect-di-microsoft-entra-per-distribuire-malware/)
* [Android: 129 vulnerabilità corrette, zero-day Qualcomm già sfruttata](https://www.securityinfo.it/2026/03/03/android-129-vulnerabilita-corrette-zero-day-qualcomm-gia-sfruttata/)
* [Una falla in Chrome sfrutta Gemini Live per scopi malevoli](https://www.securityinfo.it/2026/03/02/una-falla-in-chrome-sfrutta-gemini-live-per-scopi-malevoli/)

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

## InstallFix: false guide di installazione CLI per installare infostealer

Mar 06, 2026  [Redazione](https://www.securityinfo.it/author/redazione/ "Articoli scritti da Redazione")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Attacchi](https://www.securityinfo.it/category/approfondimenti/attacchi/), [Attacchi](https://www.securityinfo.it/category/news/attachi/), [Attacco non convenzionale](https://www.securityinfo.it/category/minacce-2/attacco-non-convenzionale/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/approfondimenti/minacce/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [Minacce](https://www.securityinfo.it/category/minacce-2/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2026/03/06/installfix-false-guide-di-installazione-cli-per-installare-infostealer/#respond)

---

Nel mondo dello sviluppo software e delle infrastrutture IT, copiare e incollare comandi di installazione da documentazioni online è diventata una pratica quotidiana. Ma proprio questa abitudine, ormai radicata tra sviluppatori, amministratori di sistema e professionisti DevOps, sta diventando il punto di ingresso per una nuova tecnica di social engineering. I ricercatori della società di sicurezza Push Security hanno infatti individuato una nuova variante degli attacchi **ClickFix**, ribattezzata **InstallFix**, che sfrutta false guide di installazione per indurre le vittime a eseguire comandi malevoli direttamente dal terminale.

![](https://www.securityinfo.it/wp-content/uploads/2026/03/Manuali-fasulli-1024x537.png)

Il principio è semplice quanto efficace: convincere l’utente a **eseguire manualmente un comando che, apparentemente, serve a installare uno strumento legittimo**. In realtà, quel comando scarica e avvia malware progettati per sottrarre dati sensibili dal sistema. L’elemento che rende questa tecnica particolarmente insidiosa è il fatto che l’utente stesso avvia l’operazione, riducendo drasticamente i segnali di anomalia che potrebbero essere intercettati dagli strumenti di sicurezza tradizionali.

**Pagine clonate e istruzioni manipolate**

Uno degli esempi più recenti riguarda la clonazione della pagina di installazione di **Claude Code**, l’assistente di programmazione via riga di comando sviluppato da Anthropic. Gli attaccanti hanno creato una replica quasi perfetta della documentazione ufficiale, riproducendo fedelmente layout grafico, branding e persino la struttura della sidebar con i link alla documentazione.

La pagina fraudolenta è praticamente indistinguibile da quella originale. Tutti i collegamenti presenti rimandano al sito autentico di Anthropic, aumentando ulteriormente la credibilità del contenuto. **L’unico elemento alterato riguarda le istruzioni di installazione** per macOS e Windows. I comandi suggeriti all’utente, anziché scaricare il software legittimo, eseguono codice che recupera malware da server controllati dagli attaccanti.

Questa strategia consente alla vittima di continuare a navigare il sito ufficiale anche dopo aver eseguito il comando malevolo, senza accorgersi che l’infezione è già avvenuta.

**Il ruolo del malvertising nei motori di ricerca**

La distribuzione di queste pagine fraudolente avviene attraverso campagne di **malvertising** sui motori di ricerca. Gli aggressori **acquistano annunci sponsorizzati su piattaforme pubblicitarie**, facendo apparire i link malevoli tra i primi risultati per ricerche come “Claude Code install” o “Claude Code CLI”.

Gli utenti che cliccano sugli annunci vengono reindirizzati verso domini apparentemente legittimi ospitati su piattaforme affidabili come Cloudflare Pages, Squarespace o Tencent EdgeOne.

Alla base dell’efficacia della tecnica InstallFix c’è una pratica diffusa nella comunità degli sviluppatori: l’utilizzo dei cosiddetti comandi “curl-to-bash”. Questo approccio consente di installare software scaricando ed eseguendo automaticamente uno script remoto con una singola riga di comando.

In molti casi, **lo script viene eseguito senza che l’utente ne verifichi il contenuto**, basandosi esclusivamente sulla reputazione del dominio da cui viene scaricato. Secondo i ricercatori, il modello di sicurezza implicito in queste operazioni si riduce spesso a una logica estremamente fragile: se il dominio sembra legittimo, allora il comando viene considerato sicuro.

Con l’espansione degli strumenti CLI e degli assistenti di programmazione basati su intelligenza artificiale, **sempre più utenti non strettamente tecnici** stanno adottando strumenti che richiedono l’esecuzione di comandi di installazione complessi. Questo ampliamento della platea rende le campagne InstallFix particolarmente promettenti per i cybercriminali.

**Amatera Stealer, il malware distribuito**

Il payload utilizzato nelle campagne osservate è **Amatera Stealer**, una famiglia relativamente recente di malware progettata per il furto di informazioni sensibili. Gli analisti ritengono che il malware sia derivato da **ACR Stealer** e venga distribuito attraverso un modello **Malware-as-a-Service**, che consente a diversi gruppi criminali di utilizzarlo tramite abbonamento.

Una volta eseguito sul sistema della vittima, Amatera è in grado di sottrarre credenziali salvate nei browser, cookie e token di sessione, oltre a raccogliere informazioni dettagliate sul sistema compromesso. Il malware può inoltre **individuare e sottrarre dati relativi a portafogli di criptovalute**, aumentando il valore economico delle informazioni esfiltrate.

La famiglia Amatera include anche **tecniche di evasione progettate per evitare il rilevamento da parte degli strumenti di sicurezza** e prolungare la permanenza del malware nel sistema co...