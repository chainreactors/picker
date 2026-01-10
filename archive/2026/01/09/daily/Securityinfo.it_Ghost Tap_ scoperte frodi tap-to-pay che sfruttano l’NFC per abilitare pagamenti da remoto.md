---
title: Ghost Tap: scoperte frodi tap-to-pay che sfruttano l’NFC per abilitare pagamenti da remoto
url: https://www.securityinfo.it/2026/01/09/ghost-tap-scoperte-frodi-tap-to-pay-che-sfruttano-lnfc-per-abilitare-pagamenti-da-remoto/?utm_source=rss&utm_medium=rss&utm_campaign=ghost-tap-scoperte-frodi-tap-to-pay-che-sfruttano-lnfc-per-abilitare-pagamenti-da-remoto
source: Securityinfo.it
date: 2026-01-09
fetch_date: 2026-01-10T03:33:02.190407
---

# Ghost Tap: scoperte frodi tap-to-pay che sfruttano l’NFC per abilitare pagamenti da remoto

Aggiornamenti recenti Gennaio 9th, 2026 2:46 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Ghost Tap: scoperte frodi tap-to-pay che sfruttano l’NFC per abilitare pagamenti da remoto](https://www.securityinfo.it/2026/01/09/ghost-tap-scoperte-frodi-tap-to-pay-che-sfruttano-lnfc-per-abilitare-pagamenti-da-remoto/)
* [Nuova ondata di attacchi GoBruteforcer, l’IA sfruttata per il brute-force](https://www.securityinfo.it/2026/01/08/nuova-ondata-di-attacchi-gobruteforcer-lia-sfruttata-per-il-brute-force/)
* [Due estensioni Chrome hanno compromesso le chat di ChatGPT e DeepSeek](https://www.securityinfo.it/2026/01/07/due-estensioni-chrome-hanno-compromesso-le-chat-di-chatgpt-e-deepseek/)
* [Nel 2026 sempre più attacchi autonomi AI-driven e deepfake: le previsioni di sicurezza di ClearSkies](https://www.securityinfo.it/2026/01/05/nel-2026-sempre-piu-attacchi-autonomi-ai-driven-e-deepfake-le-previsioni-di-sicurezza-di-clearskies/)
* [Grave vulnerabilità nei chip Bluetooth Airoha: molti i marchi colpiti](https://www.securityinfo.it/2026/01/05/grave-vulnerabilita-nei-chip-bluetooth-airoha-molti-i-marchi-colpiti/)

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

## Ghost Tap: scoperte frodi tap-to-pay che sfruttano l’NFC per abilitare pagamenti da remoto

Gen 09, 2026  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [Phishing](https://www.securityinfo.it/category/news/phishing/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2026/01/09/ghost-tap-scoperte-frodi-tap-to-pay-che-sfruttano-lnfc-per-abilitare-pagamenti-da-remoto/#respond)

---

I ricercatori di Group-IB [hanno individuato](https://www.group-ib.com/blog/ghost-tapped-chinese-malware/) **Ghost Tap**, una serie di frodi a opera di attaccanti cinesi che sfruttano applicazioni Android malevole per abilitare transazioni tap-to-pay da remoto con le carte di credito delle vittime.

Tramite campagne di smishing e vishing, i cybercriminali portano gli utenti ignari a installare gli APK malevoli. Una volta installata l’applicazione, viene richiesto alle vittime di avvicinare le proprie carte bancarie al sensore NFC dello smartphone; stabilita la connessione, i dati di pagamento vengono inoltrati a un server C2 gestito dagli attaccanti che invia le informazioni a un dispositivo sotto il loro controllo.  Questo meccanismo di relay permette ai criminali di **utilizzare terminali POS ottenuti illecitamente per incassare i fondi come se la carta fosse fisicamente presente.**

![Ghost Tap](https://www.securityinfo.it/wp-content/uploads/2026/01/Gemini_Generated_Image_xkqs4lxkqs4lxkqs.png)

Gli attacchi Ghost Tap fanno uso di due moduli principali: un “reader” installato sul dispositivo della vittima tramite l’APK compromesso e un “tapper”, ovvero il componente del device degli attaccanti che abilita transazioni e prelievi senza carta fisica.

Group-IB ha identificato oltre 54 campioni di APK malevoli, alcuni dei quali camuffati da applicazioni di realtà finanziarie legittime.

## L’ecosistema di Ghost Tap

**Gli APK vengono distribuiti da diversi vendor** nella comunità del cybercrimine cinese; tra i fornitori principali spiccano **TX-NFC, X-NFC e NFU Pay**. TX-NFC è considerato uno dei vendor più strutturati, con un canale Telegram che contava oltre 21.000 iscritti al momento del rilevamento e uno staff di supporto che opera su turni e offre assistenza anche in lingua inglese. I prezzi per l’accesso a TX-NFC variano da 45 dollari per un solo giorno fino a 1.050 dollari per tre mesi.

NFU Pay offre invece licenze che vanno da 25 dollari giornalieri a 650 dollari per un accesso a vita. Gli amministratori di NFU Pay hanno rivelato a investigatori sotto copertura di poter fornire versioni personalizzate del malware, con varianti specifiche per l’Italia e il Brasile che rimuovono l’obbligo di login lato vittima.

L’attività di monetizzazione è supportata da canali affiliati; tra questi è di particolare rilevanza Oedipus, il quale si occupa della vendita di terminali POS provenienti da diverse aree geografiche, inclusi Medio Oriente, Africa e Asia. Secondo i dati raccolti da Group-IB, solo attraverso il canale Oedipus sono stati registrati circa **355.000 dollari in transazioni illegittime** tra novembre 2024 e agosto 2025.

Oltre all’attacco diretto alle vittime, i criminali utilizzano anche reti di “muli” che caricano carte compromesse su portafogli mobili per effettuare acquisti di beni di lusso o carte regalo in negozi fisici in tutto il mondo.

La pericolosità del fenomeno Ghost Tap è confermata da numerosi incidenti e arresti globali: Group-IB cita, tra gli altri, gli arresti a Praga nel marzo 2024 di un individuo che prelevava contanti senza carta fisica e a Singapore nel novembre 2024 di cittadini malesi e cinesi che effettuavano pagamenti contactless sospetti.

![NFC malware](https://www.securityinfo.it/wp-content/uploads/2026/01/Gemini_Generated_Image_nwbq3xnwbq3xnwbq.png)

I ricercatori della compagnia avvertono che **quella dei malware tap-to-pay è una minaccia che si sta diffondendo in maniera preoccupante**: da maggio 2024 a dicembre 2025 le segnalazioni sono aumentate costantemente.

Per proteggersi da questi attacchi, le raccomandazioni coinvolgono sia i singoli utenti finali che le istituzioni finanziarie: in primo luogo, gli utenti devono prestare la massima attenzione alle comunicazioni che ricevono ed essere consapevoli delle tecniche di vishing e smishing in uso; inoltre, dovrebbero installare solo applicazioni provenienti da fonti ufficiali e verificare le autorizzazioni richieste. Un altro consiglio fondamentale è quello di disattivare la funzione NFC quando non si devono effettuare pagamenti.

I fornitori di servizi di pagamento e le realtà del mondo finanziario dovrebbero invece investire in sistemi avanzati di monitoraggio delle frodi in grado di analizzare il comportamento degli utenti e di rilevare anomalie tecniche. Le banche dovrebbero inoltre investire in campagne di sensibilizzazione per i propri clienti, informandoli specificamente sulle nuove modalità di attacco tramite NFC e sull’importanza di non avvicinare mai la carta al telefono su indicazione di terzi.

Infine, adottare protocolli autenticazione forte e implementare la verifica dell’integrità del dispositivo tramite attestazioni hardware offrono un ulteriore livello di sicurezza.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [APK malevoli](https://www.securityinfo.it/tag/apk-malevoli/), [Ghost Tap](https://www.securityinfo.it/tag/ghost-tap/), [NFC](https://www.securityinfo.it/tag/nfc/), [relay](https://www.securityinfo.it/tag/relay/), [Smishing...