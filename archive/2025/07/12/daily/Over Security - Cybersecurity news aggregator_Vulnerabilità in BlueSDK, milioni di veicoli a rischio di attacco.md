---
title: Vulnerabilità in BlueSDK, milioni di veicoli a rischio di attacco
url: https://www.securityinfo.it/2025/07/11/vulnerabilita-in-bluesdk-milioni-di-veicoli-a-rischio-di-attacco/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-12
fetch_date: 2025-10-06T23:50:46.383766
---

# Vulnerabilità in BlueSDK, milioni di veicoli a rischio di attacco

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

## Vulnerabilità in BlueSDK, milioni di veicoli a rischio di attacco

Lug 11, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/07/11/vulnerabilita-in-bluesdk-milioni-di-veicoli-a-rischio-di-attacco/#respond)

---

I ricercatori di PCA Cybersecurity [hanno individuato](https://pcacybersecurity.com/resources/advisory/perfekt-blue) un set di vulnerabilità presenti in **BlueSDK**, uno stack Bluetooth ampiamente usato nell’industria automobilista, che **mette milioni di veicoli a rischio di attacchi da remoto.**

Il team ha trovato quattro bug, di cui uno a rischio critico, che permettono a un attaccante di combinarli per eseguire **un attacco di esecuzione di codice remoto 1-click** (1-click RCE). Accedendo al sistema colpito, il cybercriminale è in grado di effettuare escalation dei privilegi, eseguire comandi per compromettere il sistema e spostarsi lateralmente su altri componenti connessi.

![BlueSDK](https://www.securityinfo.it/wp-content/uploads/2025/07/Gemini_Generated_Image_fjjlg0fjjlg0fjjl.png)

La vulnerabilità più critica è la **CVE-2024-45434**, un bug **use-after-free** presente nel protocollo AVRCP dello stack BlueSDK, causato da una mancata validazione dell’esistenza di un oggetto. “*Un attaccante può sfruttare questa vulnerabilità per eseguire codice da remoto nel contesto di un utente che esegue il processo Bluetooth*” spiega la compagnia di sicurezza.

L’unico requisito per eseguire l’attacco è che **l’attaccante sia nel range del Bluetooth** affinché possa effettuare il pairing col dispositivo. L’unico limite a questa operazione è il tipo di implementazione scelta per BlueSDK, personalizzabile per ogni sistema in base alle necessità del produttore. In alcuni casi il pairing potrebbe essere disabilitato o contemplare un numero limitato di dispositivi, mentre in alti casi potrebbe non avere certe limitazioni.

Tra i vendor dell’automotive colpiti spiccano **Mercedes-Benz AG, Volkswagen e Skoda**; per ognuno di questi produttori, PCA Cybersecurity ha eseguito una *Proof of exploitation*su uno dei loro sistemi di infotainment. La compagnia ha specificato che, oltre a questi e altri vendor del settore, anche **molti nomi al di fuori dell’automotive sono vulnerabili all’attacco.**

Il team di PCA Cybersecurity ha contattato OpenSynergy, la compagnia dietro BlueSDK, a maggio 2024. **OpenSynergy ha rilasciato le patch risolutive tra settembre e ottobre**; nel frattempo, i diversi vendor colpiti sono stati avvisati della catena di attacco. Nonostante l’intervento di OpenSynergy alla fine dello scorso anno, molti produttori non hanno ricevuto o non sono riusciti ad applicare la patch fino a giugno scorso.

PCA Cybersecurity invita gli utenti ad aggiornare il prima possibile i propri dispositivi ed eventualmente contattare il produttore per verificare che la versione installata contenga il fix per le vulnerabilità.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [automotive](https://www.securityinfo.it/tag/automotive/), [BlueSDK](https://www.securityinfo.it/tag/bluesdk/), [Bluetooth](https://www.securityinfo.it/tag/bluetooth/), [catena d'attacco](https://www.securityinfo.it/tag/catena-dattacco/), [PCA Cybersecurity](https://www.securityinfo.it/tag/pca-cybersecurity/), [RCE](https://www.securityinfo.it/tag/rce/)

[CERT-AGID 5 – 11 luglio: sei nuove campagne di phishing contro utenti SPID](https://www.securityinfo.it/2025/07/14/cert-agid-5-11-luglio-sei-campagne-phishing-utenti-spid/)
[Un attacco informatico colpisce Call of Duty: WWII su PC: giocatori compromessi](https://www.securityinfo.it/2025/07/10/un-attacco-informatico-colpisce-call-of-duty-wwii-su-pc-giocatori-compromessi/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Un attacco informatico colpisce Call of Duty: WWII su PC:  giocatori compromessi](https://www.securityinfo.it/wp-content/uploads/2025/07/COD_Hack14-lug-2025CG-120x85.png)](https://www.securityinfo.it/2025/07/10/un-attacco-informatico-colpisce-call-of-duty-wwii-su-pc-giocatori-compromessi/ "Un attacco informatico colpisce Call of Duty: WWII su PC:  giocatori compromessi")

  [Un attacco informatico colpisce Call of...](https://www.securityinfo.it/2025/07/10/un-attacco-informatico-colpisce-call-of-duty-wwii-su-pc-giocatori-compromessi/ "Permanent link to Un attacco informatico colpisce Call of Duty: WWII su PC:  giocatori compromessi")

  Lug 10, 2025  [0](https://www.securityinfo.it/2025/07/10/un-attacco-informatico-colpisce-call-of-duty-wwii-su-pc-giocatori-compromessi/#respond)
* [![Apple e Google rilasciano una feature di anti-tracciamento bluetooth](https://www.securityinfo.it/wp-content/uploads/2024/05/Apple-Google-partner-tracking-detection-hero_inline.jpg.large_-120x85.jpg)](https://www.securityinfo.it/2024/05/14/apple-e-google-rilasciano-una-feature-di-anti-tracciamento-bluetooth/ "Apple e Google rilasciano una feature di anti-tracciamento bluetooth")

  [Apple e Google rilasciano una feature...](https://www.securityinfo.it/2024/05/14/apple-e-google-rilasciano-una-feature-di-anti-tracciamento-bluetooth/ "Permanent link to Apple e Google rilasciano una feature di anti-tracciamento bluetooth")

  Mag 14, 2024  [0](https://www.securityinfo.it/2024/05/14/apple-e-google-rilasciano-una-feature-di-anti-tracciamento-bluetooth/#respond)
* [![Ivan...