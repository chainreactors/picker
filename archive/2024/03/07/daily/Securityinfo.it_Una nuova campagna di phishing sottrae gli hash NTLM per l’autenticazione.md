---
title: Una nuova campagna di phishing sottrae gli hash NTLM per l’autenticazione
url: https://www.securityinfo.it/2024/03/06/una-nuova-campagna-di-phishing-sottrae-gli-hash-ntlm-per-lautenticazione/?utm_source=rss&utm_medium=rss&utm_campaign=una-nuova-campagna-di-phishing-sottrae-gli-hash-ntlm-per-lautenticazione
source: Securityinfo.it
date: 2024-03-07
fetch_date: 2025-10-06T17:11:17.348986
---

# Una nuova campagna di phishing sottrae gli hash NTLM per l’autenticazione

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

## Una nuova campagna di phishing sottrae gli hash NTLM per l’autenticazione

Mar 06, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [Hacking](https://www.securityinfo.it/category/news/hacking-news/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [Phishing](https://www.securityinfo.it/category/news/phishing/)
 [0](https://www.securityinfo.it/2024/03/06/una-nuova-campagna-di-phishing-sottrae-gli-hash-ntlm-per-lautenticazione/#respond)

---

I ricercatori di Proofpoint [hanno individuato](https://www.proofpoint.com/us/blog/threat-insight/ta577s-unusual-attack-chain-leads-ntlm-data-theft) una nuova **campagna di phishing** che mira a **sottrarre gli hash NTLM** di Windows e usarli per ottenere le password degli utenti in chiaro.

Dietro gli attacchi ci sarebbe **TA577**, un gruppo attivo da metà del 2020 **affiliato a Qbot** e legato alle attività del ransomware BlackBasta. Il gruppo prende di mira organizzazioni di diversi settori in tutto il mondo, ed è considerato un Initial Access Broker (IAB).

A fine febbraio i ricercatori hanno intercettato decine di centinaia di **messaggi email diretti a utenti di organizzazioni di tutto il mondo**. I messaggi erano risposte a email precedenti (attacco di thread hijacking) e contenevano **allegati HTML in archivi .zip.**

Una volta estratto il file .zip e aperto l’HTML, il file tentava di **connettersi a un server SMB controllato dagli attaccanti** tramite un reindirizzamento verso un URI. L’obiettivo della campagna di phishing non era scaricare un malware, ma ottenere le coppie Challenge/Response di NTLM per **sottrarre l’hash**; questa informazione poteva poi essere usata per individuare la password in chiaro o eseguire degli **attacchi “Pass-The-Hash”**, consentendo al gruppo di autenticarsi sui sistemi aziendali.

![](https://www.securityinfo.it/wp-content/uploads/2024/03/hacker-3480124_1920.jpg)

Il team di Proofpoint fa notare che l’uso di un archivio .zip per distribuire l’HTML serve a **superare i controlli di sicurezza di Outlook introdotti a luglio**: se l’URI del file scheme fosse stato inviato direttamente nel corpo del messaggio di posta elettronica, l’attacco non avrebbe funzionato sui client Outlook; ciò evidenzia un impegno notevole da parte del gruppo nel rimanere sempre aggiornato e sviluppare tecniche per eludere i nuovi controlli

Proofpoint spiega che il gruppo non ha mai sferrato attacchi di questo genere e che **sta investendo tempo e risorse per migliorare velocemente le sue tecniche**. “Rispetto ad altriIAB, **TA755 sembra avere il polso del panorama delle minacce** e sa quando e perché specifiche catene di attacco smettono di essere efficaci e creerà rapidamente nuovi metodi per eludere i controlli e tentare di aumentare l’efficacia e la probabilità di colpire le vittime con la consegna dei payload”.

Per proteggersi da questo tipo di attacchi, i ricercatori consigliano di **bloccare le connessioni SMB in uscita.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [autenticazione](https://www.securityinfo.it/tag/autenticazione/), [IAB](https://www.securityinfo.it/tag/iab/), [NTLM](https://www.securityinfo.it/tag/ntlm/), [pass-the-hash](https://www.securityinfo.it/tag/pass-the-hash/), [Phishing](https://www.securityinfo.it/tag/phishing/), [ta577](https://www.securityinfo.it/tag/ta577/), [Windows](https://www.securityinfo.it/tag/windows/)

[Hacker nord-coreani attaccano l'industria dei semiconduttori sud-coreana](https://www.securityinfo.it/2024/03/06/hacker-nord-coreani-attaccano-lindustria-dei-semiconduttori-sud-coreana/)
[BlackCat accusato di furto da un affiliato: il gruppo chiude i server](https://www.securityinfo.it/2024/03/05/blackcat-accusato-di-furto-da-un-affiliato-il-gruppo-chiude-i-server/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-6138007_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/ "Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA")

  [Report Acronis: il ransomware rimane la...](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/ "Permanent link to Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA")

  Set 11, 2025  [0](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/#respond)
* [![Criminali abusano dei servizi di link wrapping per aggirare i controlli](https://www.securityinfo.it/wp-content/uploads/2025/08/MatrioskaMalware1-ago-2025CG-120x85.png)](https://www.securityinfo.it/2025/08/01/criminali-abusano-dei-servizi-di-link-wrapping-per-aggirare-i-controlli/ "Criminali abusano dei servizi di link wrapping per aggirare i controlli")

  [Criminali abusano dei servizi di link...](https://www.securityinfo.it/2025/08/01/criminali-abusano-dei-servizi-di-link-wrapping-per-aggirare-i-controlli/ "Permanent link to Criminali abusano dei servizi di link wrapping per aggirare i controlli")

  Ago 01, 2025  [0](https://www.securityinfo.it/2025/08/01/criminali-abusano-dei-servizi-di-link-wrapping-per-aggirare-i-controlli/#respond)
* [![PoisonSeed è riuscito ad aggirare la protezione FIDO](https://www.securityinfo.it/w...