---
title: Hugging Face sfruttato per distribuire un trojan Android
url: https://www.securityinfo.it/2026/01/30/hugging-face-sfruttato-per-distribuire-un-trojan-android/?utm_source=rss&utm_medium=rss&utm_campaign=hugging-face-sfruttato-per-distribuire-un-trojan-android
source: Securityinfo.it
date: 2026-01-30
fetch_date: 2026-01-31T04:05:13.006531
---

# Hugging Face sfruttato per distribuire un trojan Android

Aggiornamenti recenti Gennaio 30th, 2026 5:19 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Hugging Face sfruttato per distribuire un trojan Android](https://www.securityinfo.it/2026/01/30/hugging-face-sfruttato-per-distribuire-un-trojan-android/)
* [OpenSSL ha fixato 12 vulnerabilità scoperte da AISLE](https://www.securityinfo.it/2026/01/29/openssl-ha-fixato-12-vulnerabilita-scoperte-da-aisle/)
* [PackageGate: trovati sei bug zero-day nei package manager, ma NPM non interviene](https://www.securityinfo.it/2026/01/27/packagegate-trovati-sei-bug-zero-day-nei-package-manager-ma-npm-non-interviene/)
* [C’è Sandworm dietro l’attacco contro il settore energetico polacco](https://www.securityinfo.it/2026/01/26/ce-sandworm-dietro-lattacco-contro-il-settore-energetico-polacco/)
* [Zendesk, sfruttato il sistema di ticketing per una campagna di spam massiva](https://www.securityinfo.it/2026/01/23/zendesk-sfruttato-il-sistema-di-ticketing-per-una-campagna-di-spam-massiva/)

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

## Hugging Face sfruttato per distribuire un trojan Android

Gen 30, 2026  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [Phishing](https://www.securityinfo.it/category/news/phishing/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2026/01/30/hugging-face-sfruttato-per-distribuire-un-trojan-android/#respond)

---

I ricercatori di BitDefender [hanno scoperto](https://www.bitdefender.com/en-us/blog/labs/android-trojan-campaign-hugging-face-hosting-rat-payload) una campagna che sfrutta tecniche di social engineering, i servizi di accessibilità Android e **l’infrastruttura di Hugging Face** per distribuire un **trojan**.

La natura della piattaforma, utilizzata dagli utenti per caricare modelli di machine learning, dataset e altri tool di sviluppo, permette di fatto anche ai cybercriminali di caricare i propri payload: **Hugging Face infatti sembra non avere filtri sufficienti per bloccare upload malevoli**, come, in questo caso, il trojan. Sebbene i contenuti vengano scansionati con ClamAV, un motore antivirus open-source, non tutti i payload sospetti vengono bloccati.

![Hugging Face trojan](https://www.securityinfo.it/wp-content/uploads/2026/01/ChatGPT-Image-30-gen-2026-17_16_05.jpg)

La campagna inizia con la diffusione di un’app Android chiamata **TrustBastion**. Gli utenti vengono spinti a scaricare l’app tramite annunci che notificano che il telefono è infetto e proponendo appunto TrustBastion come soluzione per individuare tentativi di phishing, scam e comunicazioni fraudolente.

L’app in sé non è malevola, ma funge semplicemente da dropper. Dopo l’installazione, l’app mostra un falso prompt di “aggiornamento disponibile”, realizzato per sembrare un messaggio legittimo di Android o Google Play; cliccando sul pulsante di aggiornamento, l’utente scarica l’effettivo malware.

È a questo punto che entra in gioco l’infrastruttura di Hugging Face: poiché spesso il traffico da domini sospetti viene limitato e bloccato, invece di scaricare lo spyware da un dominio custom, il payload effettua una richiesta al sito web di TrustBastion; a questa richiesta il server risponde con una pagina HTML la quale a sua volta contiene un link che punta al file APK su Hugging Face. **Il payload finale viene quindi scaricato direttamente dalla piattaforma**.

Una volta installato, il payload malevolo richiede **permessi critici** spacciandoli per funzionalità di sistema e guida l’utente all’attivazione dei servizi di accessibilità, un tassello chiave per ottenere pieno controllo del dispositivo. Il trojan richiede inoltre **permessi per registrare lo schermo, fare casting del display e visualizzare overlay** per poter catturare e manipolare ciò che è mostrato sullo schermo in tempo reale.

Il malware è anche in grado di mostrare finte interfacce di autenticazione per servizi come Alipay e WeChat per rubare le credenziali utente, oltre a catturare informazioni di sblocco e input di autenticazione. L’attività dell’utente e i contenuti vengono poi inviati a un server C2.

![](https://www.securityinfo.it/wp-content/uploads/2026/01/hacker-2300772_1920-3.jpg)

Analizzando il repository di Hugging Face, i ricercatori hanno scoperto che gli attaccanti caricavano un nuovo payload ogni 15 minuti circa. Ogni nuova versione dell’APK manteneva le stesse funzionalità e introduceva solo piccole modifiche per eludere la detection hash-based.

Il repository di TrustBastion è stato eliminato alla fine di dicembre, ma i ricercatori hanno individuato un nuovo repository, questa volta di un’app chiamata Premium Club, che condivide lo stesso codice del primo trojan.

Il team di Bitdefender ha contattato Hugging Face per notificargli la minaccia e la piattaforma ha tolto immediatamente i dataset che contenevano il malware. Il consiglio per gli utenti è come sempre di **non scaricare applicazioni al di fuori di marketplace ufficiali**o installare APK manualmente; inoltre, è necessario controllare sempre quali permessi si stanno per fornire a un’applicazione e verificare se siano davvero necessari per le sue funzionalità.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [APK](https://www.securityinfo.it/tag/apk/), [furto di credenziali](https://www.securityinfo.it/tag/furto-di-credenziali/), [hugging face](https://www.securityinfo.it/tag/hugging-face/), [Phishing](https://www.securityinfo.it/tag/phishing/), [Trojan](https://www.securityinfo.it/tag/trojan/), [TrustBastion](https://www.securityinfo.it/tag/trustbastion/)

[OpenSSL ha fixato 12 vulnerabilità scoperte da AISLE](https://www.securityinfo.it/2026/01/29/openssl-ha-fixato-12-vulnerabilita-scoperte-da-aisle/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Dark Telegram in ritirata: aumentano le chiusure dei canali clandestini](https://www.securityinfo.it/wp-content/uploads/2025/12/Gemini_Generated_Image_4uclnb4uclnb4ucl-120x85.png)](https://www.securityinfo.it/2025/12/04/dark-telegram-in-ritirata-aumentano-le-chiusure-dei-canali-clandestini/ "Dark Telegram in ritirata: aumentano le chiusure dei canali clandestini")

  [Dark Telegram in ritirata: aumentano le...](https://www.securityinfo.it/2025/12/04/dark-telegram-in-ritirata-aumentano-le-chiusure-dei-canali-clandestini/ "Permanent link to Dark Telegram in ritirata: aumentano le chiusure dei canali clandestini")

  Dic 04, 2025  [0](https://www.securityinfo.it/2025/12/04/dark-telegram-in-ritirata-aumentano-le-chiusure-dei-canali-clandestini/#...