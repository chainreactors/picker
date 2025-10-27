---
title: Cloud9 prende il controllo di Chrome e derivati
url: https://www.securityinfo.it/2022/11/10/cloud9-prende-il-controllo-di-chrome-e-derivati/?utm_source=rss&utm_medium=rss&utm_campaign=cloud9-prende-il-controllo-di-chrome-e-derivati
source: Over Security - Cybersecurity news aggregator
date: 2022-11-11
fetch_date: 2025-10-03T22:24:48.782569
---

# Cloud9 prende il controllo di Chrome e derivati

Aggiornamenti recenti Ottobre 3rd, 2025 4:00 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)
* [Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)
* [Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/)
* [Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/)
* [CERT-AGID 20–26 settembre: phishing, malware e PEC compromesse](https://www.securityinfo.it/2025/09/29/cert-agid-20-26-settembre-phishing-malware-e-pec-compromesse/)

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

## Cloud9 prende il controllo di Chrome e derivati

Nov 10, 2022  [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/ "Articoli scritti da Dario Orlandi")
 [Malware](https://www.securityinfo.it/category/news/malware-news/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2022/11/10/cloud9-prende-il-controllo-di-chrome-e-derivati/#respond)

---

[Cloud9](https://www.zimperium.com/blog/the-case-of-cloud9-chrome-botnet/) è una minaccia progettata per colpire i browser Web, recentemente individuata “in the wild” dai ricercatori di [Zimperium](https://www.zimperium.com/). La minaccia è costituita da un Rat (remote access trojan) che **colpisce i browser derivati dal progetto Chromium** (tra cui Google Chrome e Microsoft Edge).

Il malware viene distribuito tramite estensioni compromesse, ma non sfrutta il Chrome Web Store: è stato invece inserito in falsi aggiornamenti di componenti legacy come il **player Flash** di Adobe, distribuiti poi attraverso canali non ufficiali.

Una volta installato, il malware offre ai suoi controlloriuna lunga lista di funzioni

: al suo interno si trovano infatti tre diversi moduli Javascript che **raccolgono informazioni** sul sistema, sfruttano le risorse locali per il **mining di criptovalute** e partecipano ad **attacchi Ddos**, oltre a offrire funzioni di “utilità” per iniettare ulteriori script.

Secondo i ricercatori, il tool **può sfruttare diversi exploit** per Firefox, Internet Explorer ed Edge che consentono l’esecuzione di malware sull’host, andando quindi a compromettere ulteriormente la sicurezza del sistema controllato.

![](https://www.securityinfo.it/wp-content/uploads/2022/11/extension.png)

L’estensione compromessa (Fonte: Zimperium)

## Ladro di dati

Anche senza l’intervento di ulteriori payload, le funzioni di base di Cloud9 consentono comunque ai criminali informatici **un ampio ventaglio di azioni**: possono infatti rubare cookie e prendere il controllo di intere sessioni di navigazione.

Tra i tool disponibili non manca neppure un **keylogger** e uno strumento per la cattura delle informazioni eventualmente memorizzate negli appunti di sistema. Il malware permette agli operatori di caricare automaticamente specifiche pagine Web per generare impression e visite.

Secondo i ricercatori, però, l’utilizzo prevalente sembra essere quello di coinvolgere i browser violati in **attacchi Ddos,** che risultano particolarmente efficaci perché portati tramite richieste Post effettuate da un browser.

Questi attacchi, chiamati in gergo ***layer 7*** perché veicolati tramite il settimo livello del [modello OSI](https://it.wikipedia.org/wiki/Modello_OSI) (quello delle applicazioni)*,* sono pressoché indistinguibili rispetto a una connessione legittima e quindi sono più difficilmente mitigabili in modo automatizzato.

Autore del malware è il **gruppo Keksec**, attivo dal 2016 e specializzato proprio nelle botnet dedite al cryptomining e agli attacchi Ddos.

La botnet è proposta su diversi forum specializzati, per poche centinaia di dollari o addirittura gratuitamente. Potrebbe quindi essere utilizzata da diversi gruppi per **un’ampia varietà di scopi** criminali.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [botnet](https://www.securityinfo.it/tag/botnet/), [browser](https://www.securityinfo.it/tag/browser/), [Chrome](https://www.securityinfo.it/tag/chrome/), [Chromium](https://www.securityinfo.it/tag/chromium/), [Cloud9](https://www.securityinfo.it/tag/cloud9/), [cookie](https://www.securityinfo.it/tag/cookie/), [crypto-miner](https://www.securityinfo.it/tag/crypto-miner/), [DDoS](https://www.securityinfo.it/tag/ddos/), [Edge](https://www.securityinfo.it/tag/edge/), [Firefox](https://www.securityinfo.it/tag/firefox/), [Keksec](https://www.securityinfo.it/tag/keksec/), [keylogger](https://www.securityinfo.it/tag/keylogger/)

[Smart Factory: aumentano i rischi di sicurezza per il settore](https://www.securityinfo.it/2022/11/10/smart-factory-aumento-rischi-sicurezza/)
[La top ten delle minacce da Bitdefender](https://www.securityinfo.it/2022/11/09/la-top-ten-delle-minacce-da-bitdefender/)

---

![](https://secure.gravatar.com/avatar/9ba6108fae91c2be66a7ef45ac2db49a?s=90&d=mm&r=g)

##### [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/)

##### Articoli correlati

* [![Apple rilascia una fix per una vulnerabilità di Safari già sfruttata in Chrome](https://www.securityinfo.it/wp-content/uploads/2025/07/Gemini_Generated_Image_1mvtjc1mvtjc1mvt-120x85.png)](https://www.securityinfo.it/2025/07/30/apple-rilascia-una-fix-per-una-vulnerabilita-di-safari-gia-sfruttata-in-chrome/ "Apple rilascia una fix per una vulnerabilità di Safari già sfruttata in Chrome")

  [Apple rilascia una fix per una...](https://www.securityinfo.it/2025/07/30/apple-rilascia-una-fix-per-una-vulnerabilita-di-safari-gia-sfruttata-in-chrome/ "Permanent link to Apple rilascia una fix per una vulnerabilità di Safari già sfruttata in Chrome")

  Lug 30, 2025  [0](https://www.securityinfo.it/2025/07/30/apple-rilascia-una-fix-per-una-vulnerabilita-di-safari-gia-sfruttata-in-chrome/#respond)
* [![Attacchi DDoS ipervolumetrici, ancora numeri da record nonostante il calo](https://www.securityinfo.it/wp-content/uploads/2025/07/Gemini_Generated_Image_ij19w5ij19w5ij19-120x85.png)](https://www.securityinfo.it/2025/07/17/attacchi-ddos-ipervolumetrici-ancora-numeri-da-record-nonostante-il-calo/ "Attacchi DDoS ipervolumetrici, ancora numeri da record nonostante il calo")

  [Attacchi DDoS ipervolumetrici, ancora...](https://www.securityinfo.it/2025/07/17/attacchi-ddos-ipervolumetrici-ancora-numeri-da-record-nonostante-il-calo/ "Permanent...