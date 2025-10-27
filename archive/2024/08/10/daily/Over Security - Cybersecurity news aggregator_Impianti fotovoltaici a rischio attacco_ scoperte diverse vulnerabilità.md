---
title: Impianti fotovoltaici a rischio attacco: scoperte diverse vulnerabilità
url: https://www.securityinfo.it/2024/08/09/impianti-fotovoltaici-a-rischio-attacco-scoperte-diverse-vulnerabilita/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-10
fetch_date: 2025-10-06T18:07:27.724384
---

# Impianti fotovoltaici a rischio attacco: scoperte diverse vulnerabilità

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

## Impianti fotovoltaici a rischio attacco: scoperte diverse vulnerabilità

Ago 09, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/approfondimenti/minacce/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2024/08/09/impianti-fotovoltaici-a-rischio-attacco-scoperte-diverse-vulnerabilita/#respond)

---

Bitdefender ha pubblicato una [ricerca](https://www.bitdefender.com/blog/labs/60-hurts-per-second-how-we-got-access-to-enough-solar-power-to-run-the-united-states/) riguardante alcune **vulnerabilità presenti nella piattaforma di gestione di impianti fotovoltaici di Solarman e negli inverter Deye** che consentono a un attaccante di prendere il controllo dei componenti della rete elettrica.

![impianti fotovoltaici vulnerabilità](https://www.securityinfo.it/wp-content/uploads/2024/08/panel-2562239_1920.jpg)

Pixabay

La piattaforma si occupa di coordinare le operazioni di milioni di installazioni di impianti in tutto il mondo, responsabili del 20% della produzione di energia solare mondiale.

I ricercatori di Bitdefender hanno analizzato in che modo gli attaccanti potrebbero utilizzare gli inverter, componenti critici dell’infrastruttura che convertono la corrente continua (DC) in corrente alternata (AC), cioè quella usata comunemente nelle case e negli uffici.

L’architettura Solarman ha diversi entry point esposti per integrare inverter, data logger e altre componenti fotovoltaiche di diverse compagnie. Dall’analisi dei ricercatori è emerso che **la combinazione di Solarman con gli inverter Deye espone delle importanti vulnerabilità** di sicurezza che possono essere usate per interrompere l’attività degli impianti fotovoltaici.

## Le vulnerabilità degli impianti fotovoltaici

Nel dettaglio, Bitdefender ha scoperto che **la piattaforma di Solarman soffre di tre vulnerabilità**: la prima colpisce l’endpoint /oauth2-s/oauth/token e consente agli attaccanti di generare token di autorizzazione per qualsiasi account, prendendone il controllo; la seconda è una vulnerabilità cross-platform che permette di usare i token JWT della piattaforma Deye Cloud anche su Solarman, consentendo anche in questo caso di **accedere alle funzionalità senza autorizzazione**; infine, gli endpoint di Solarman restituiscono troppe informazioni riguardo l’organizzazione, compresi dati sensibili.

Per quanto riguarda Deye, la piattaforma utilizza un **account hard-coded con password 123456** per accedere ai dati dei dispositivi; questo account può ottenere un token di autorizzazione che gli consente l’accesso a qualsiasi positivo per accedere a informazioni quali la versione software e le credenziali Wi-Fi.

Su Deye Cloud, inoltre, l’endpoint /user-s/acc/orgs ritorna numerose informazioni private sugli utenti, inclusi nomi, indirizzi email. numeri di telefono e ID. Infine, come per la piattaforma Solarman, l’API /oaut-s/oauth/ permette agli attaccanti di **generare token di autorizzazione per qualsiasi account**. In questo caso il token JWT generato contiene un valore errato che non viene accettato dal server, ma in futuro questa vulnerabilità potrebbe rappresentare un serio problema.

![](https://www.securityinfo.it/wp-content/uploads/2024/08/photovoltaic-2814504_1920.jpg)

Pixabay

Queste vulnerabilità mettono a serio rischio la sicurezza degli impianti, causando diversi problemi: oltre ad accedere ai dati sensibili di utenti e organizzazioni, gli attaccanti possono prendere il controllo degli inverter per interrompere la generazione di energia e causare fluttuazioni di voltaggio**, sovraccaricare la rete e provocare un blackout.**

I due vendor hanno provveduto a sanare le vulnerabilità. Vista l’estensione degli impatti, è fondamentale integrare misure di sicurezza robusta negli impianti fotovoltaici.

“*Mentre continuiamo ad abbracciare le energie rinnovabili, **dobbiamo anche rimanere vigili e proattivi nel mettere in sicurezza la nostra infrastruttura energetica contro le minacce in evoluzione***” concludono i ricercatori.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [accesso non autorizzato](https://www.securityinfo.it/tag/accesso-non-autorizzato/), [Deye](https://www.securityinfo.it/tag/deye/), [energia solare](https://www.securityinfo.it/tag/energia-solare/), [impianti fotovoltaici](https://www.securityinfo.it/tag/impianti-fotovoltaici/), [Solarman](https://www.securityinfo.it/tag/solarman/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[INTERPOL: I-GRIP contro le truffe BEC](https://www.securityinfo.it/2024/08/12/interpol-i-grip-contro-le-truffe-bec/)
[Scoperta una seconda vulnerabilità zero-day in Apache OFBiz](https://www.securityinfo.it/2024/08/08/scoperta-una-seconda-vulnerabilita-zero-day-in-apache-ofbiz/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_d4x8rid4x8rid4x8-120x85.png)](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  [Firewall Cisco sotto attacco: una nuova...](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Permanent link to Firewall Cisco sotto attacco...