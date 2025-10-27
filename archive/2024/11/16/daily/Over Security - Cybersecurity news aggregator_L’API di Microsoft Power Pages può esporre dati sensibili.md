---
title: L’API di Microsoft Power Pages può esporre dati sensibili
url: https://www.securityinfo.it/2024/11/15/lapi-di-microsoft-power-pages-puo-esporre-dati-sensibili/
source: Over Security - Cybersecurity news aggregator
date: 2024-11-16
fetch_date: 2025-10-06T19:19:47.543196
---

# L’API di Microsoft Power Pages può esporre dati sensibili

Aggiornamenti recenti Ottobre 6th, 2025 9:00 AM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)
* [Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)
* [Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/)

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

## L’API di Microsoft Power Pages può esporre dati sensibili

Nov 15, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Leaks](https://www.securityinfo.it/category/news/leaks-news/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2024/11/15/lapi-di-microsoft-power-pages-puo-esporre-dati-sensibili/#respond)

---

Aaron Costello, Chief of SaaS Security Research di AppOmni, [ha individuato](https://appomni.com/ao-labs/microsoft-power-pages-data-exposure-reviewed/) un problema nelle **API di Microsoft Power Pages** che, se configurata in maniera errata, espone **informazioni sensibili degli utenti.**

“*Nel settembre 2024, ho scoperto che **una quantità significativa di dati è stata esposta a Internet come risultato di controlli di accesso non configurati correttamente nei siti web di Microsoft Power Page***” ha affermato Costello.

Power Pages è una **piattaforma SaaS low-code** che consente di creare siti web basati sull’infrastruttura Microsoft. Lo strumento consente di progettare siti web in poco tempo usando il sistema drag&drop, scegliendo tra componenti web pronti all’uso.

![](https://www.securityinfo.it/wp-content/uploads/2024/10/hacking-3112539_1920-1.png)

La vulnerabilità risiede in una **configurazione errata dei controlli di accesso**, legata a delle implementazioni non sicure. Nel dettaglio, **gli utenti esterni hanno permessi troppo elevati**, tanto da poter ottenere i record sensibili dal database della piattaforma sfruttando le API a disposizione.

Power Pages infatti prevede una serie di ruoli, tra i quali **“Anonymous User”** e **“Authenticated User”**: il primo comprende tutti gli utenti che non si sono autenticati sul sito, il secondo invece è generico per tutti gli utenti che sono autenticati. Generalmente si usa il **“Authenticated User” per consentire a chiunque di creare un account**; una volta creato il profilo, l’utente ottiene tutti i permessi del ruolo, compresi quelli di accesso ai record interni delle organizzazioni.

L’errore è **trattare il ruolo “Authenticated User” come se fosse un utente *interno***, quando in realtà dovrebbe esserci distinzione con quelli *esterni*: Power Pages dovrebbe usare invece il ruolo di “Anonymous User” per chi si registra dal web.

## La gestione degli accessi in Microsoft Power Pages

Oltre alla definizione dei ruoli, Power Pages usa un **sistema di controllo multi-livello**: la gestione **a** **livello di sito** comprende le configurazioni globali che abilitano o disabilitano funzionalità quali la registrazione pubblica o l’autenticazione; **a livello di tabella**, si definiscono i ruoli e i permessi (lettura, modifica, cancellazione) per ogni tabella del database; infine, esiste il controllo degli accessi **a livello di colonna** che sfrutta profili di sicurezza per mascherare colonne di dati sensibili.

Quest’ultima funzionalità non è immediata da implementare e **spesso viene ignorata dalle aziende**; ciò significa che anche un utente esterno, classificato come “Authenticated”, può accedere a colonne contenenti informazioni sensibili sugli utenti.

Le cause principali delle esposizioni individuate da Costello risiedono in primis nei permessi eccessivi a livello di API, quando le colonne delle tabelle sono tutte accessibili. Anche lasciare la possibilità a chiunque di registrarsi aumenta il rischio di accessi non autorizzati, così come l’uso di configurazioni “Global Access” che abilitano tutti i permessi sulle tabelle.

“*Senza sfruttare i profili di sicurezza delle colonne, **tutte le colonne abilitate alle API web saranno mostrate agli utenti esterni se le autorizzazioni a livello di tabella non sono configurate correttamente***” ha spiegato Costello. I profili di sicurezza relativi alle colonne permette di aggiungere un ulteriore livello di protezione, consentendo l’accesso ai dati sensibili solo agli utenti coi privilegi più elevati. Le organizzazioni però non danno abbastanza importanza al controllo: **“*In tutti i test che ho fatto non c’era una sola implementazione della sicurezza a livello di colonna per impedire l’accesso alle colonne sensibili*“** ha specificato il ricercatore.

![vulnerabilità critiche](https://www.securityinfo.it/wp-content/uploads/2024/06/cybersecurity-5642004_1920.jpg)

Pixabay

Costello ha scoperto milioni di record di dati sensibili accessibili dalla rete, sia di utenti interni a Microsoft che di clienti che usano Web Pages. Nella maggior parte dei casi, i dati includevano i nomi completi degli utenti, indirizzi email, numeri di telefono e indirizzi di casa.

Microsoft avverte i suoi utenti con una serie di alert quando individua una configurazione potenzialmente pericolosa in Power Pages, a cui le aziende però non prestano sufficiente attenzione. Costello specifica che l’unico modo per risolvere il problema è **rimuovere del tutto i permessi elevati per gli utenti esterni.** È comunque caldamente consigliato vagliare tutte le tabelle e le colonne per **identificare i dati sensibili e definire profili di sicurezza precisi per gli accessi.**

Alcune organizzazioni potrebbero non riuscire a implementare questi controlli senza alterare le funzionalità del sito; in questi casi è consigliabile usare un endpoint personalizzato per validare le informazioni condivise con l’utente.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [data exposure](https://www.securityinfo.it/tag/data-exposure/), [data leak](https://www.securityinfo.it/tag/data-leak/), [low-code](https://www.securityinfo.it/tag/low-code/), [Microsoft](https://www.securityinfo.it/tag/microsoft/...