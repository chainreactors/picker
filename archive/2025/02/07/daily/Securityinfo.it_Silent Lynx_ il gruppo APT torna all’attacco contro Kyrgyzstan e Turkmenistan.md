---
title: Silent Lynx: il gruppo APT torna all’attacco contro Kyrgyzstan e Turkmenistan
url: https://www.securityinfo.it/2025/02/06/silent-lynx-il-gruppo-apt-torna-allattacco-contro-kyrgyzstan-e-turkmenistan/?utm_source=rss&utm_medium=rss&utm_campaign=silent-lynx-il-gruppo-apt-torna-allattacco-contro-kyrgyzstan-e-turkmenistan
source: Securityinfo.it
date: 2025-02-07
fetch_date: 2025-10-06T20:47:12.621586
---

# Silent Lynx: il gruppo APT torna all’attacco contro Kyrgyzstan e Turkmenistan

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

## Silent Lynx: il gruppo APT torna all’attacco contro Kyrgyzstan e Turkmenistan

Feb 06, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/02/06/silent-lynx-il-gruppo-apt-torna-allattacco-contro-kyrgyzstan-e-turkmenistan/#respond)

---

**Silent Lynx**, un gruppo APT di origine kazaka, è tornato ad agire con **due campagne di cyberspionaggio** che hanno preso di mira di mira numerose organizzazioni in Kyrgyzstan e Turkmenistan, incluse ambasciate, studi di avvocati, banche pubbliche e think thank.

“***Questo gruppo ha già preso di mira entità dell’Europa dell’Est e think tank governativi dell’Asia centrale** coinvolti nel processo decisionale economico e nel settore bancario*” [spiega](https://www.seqrite.com/blog/silent-lynx-apt-targeting-central-asian-entities/) Subhajeet Singha, ricercatore di Seqrite Labs e a capo del team che ha scoperto le due nuove campagne.

![Silent Lynx](https://www.securityinfo.it/wp-content/uploads/2025/02/security-6901712_1920.jpg)

In entrambe le operazioni, il gruppo ha utilizzato delle email di spear phishing per attaccare i dispositivi delle vittime. Le email provenivano da un account compromesso di un dipendente della National Bank of the Kyrgyz Republic.

Nella prima campagna alle email era allegato un file .rar che conteneva a sua volta un file .iso, contenente un eseguibile malevolo, il quale eseguiva un **processo PowerShell.** Lo script in questione si collegava a un bot Telegram per eseguire comandi di varia natura ed **esfiltrare dati.**

Nel secondo caso, invece, l’archivio .rar conteneva un **eseguibile scritto in Golang** che si occupava di connettersi a un server controllato dagli attaccanti, sempre per esfiltrare dati dal dispositivo.

I ricercatori di Seqrite Labs sono riusciti a individuare il bot utilizzato dagli attaccanti e hanno avuto accesso ai comandi eseguiti da Silent Lynx sui sistemi compromessi. In un caso, la presenza di **file sensibili** come “Turkmenistanyn Gyrgyz Respublikasyndaky Ilcihanasynyn meyilnamasy.doc” (*Amministrazione del Turkmenistan nella Repubblica del Kirghizistan*) conferma che gli attaccanti hanno colpito la vittima per raccogliere informazioni diplomatiche.

![Silent Lynx](https://www.securityinfo.it/wp-content/uploads/2025/02/26.png)

Credits: Seqrite Labs

Secondo un’analisi aggiuntiva di Cisco Talos, i tool e le motivazioni del gruppo sono molto simili a quelle di **YoroTrooper**, un altro gruppo APT kazako; è probabile quindi che ci siano delle **connessioni tra le due entità.**

“*Le campagne di Silent Lynx dimostrano una sofisticata strategia di attacco in più fasi che utilizza file ISO, loader C++, script PowerShell e impianti Golang*“.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [APT](https://www.securityinfo.it/tag/apt/), [bot Telegram](https://www.securityinfo.it/tag/bot-telegram/), [cyberspionaggio](https://www.securityinfo.it/tag/cyberspionaggio/), [esfiltrazione dati](https://www.securityinfo.it/tag/esfiltrazione-dati/), [Seqrite Labs](https://www.securityinfo.it/tag/seqrite-labs/), [Silent Lynx](https://www.securityinfo.it/tag/silent-lynx/), [Spear Phishing](https://www.securityinfo.it/tag/spear-phishing/)

[Di nuovo, una vecchia vulnerabilità di Outlook viene sfruttata dai criminali](https://www.securityinfo.it/2025/02/07/un-bug-critico-di-outlook-e-stato-sfruttato-in-degli-attacchi/)
[Hacker russi fruttano un bug 0-day di 7-Zip per distribuire SmokeLoader](https://www.securityinfo.it/2025/02/05/hacker-russi-fruttano-un-bug-0-day-di-7-zip-per-distribuire-smokeloader/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  [MuddyWater si evolve: attacchi più...](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "Permanent link to MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  Set 17, 2025  [0](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/#respond)
* [![Un attacco supply chain ha compromesso oltre 40 pacchetti NPM](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_px0h5ppx0h5ppx0h-120x85.png)](https://www.securityinfo.it/2025/09/16/un-attacco-supply-chain-ha-compromesso-oltre-40-pacchetti-npm/ "Un attacco supply chain ha compromesso oltre 40 pacchetti NPM")

  [Un attacco supply chain ha compromesso...](https://www.securityinfo.it/2025/09/16/un-attacco-supply-chain-ha-compromesso-oltre-40-pacchetti-npm/ "Permanent link to Un attacco supply chain ha compromesso oltre 40 pacchetti NPM")

  Set 16, 2025  [0](https://www.securityinfo.it/2025/09/16/un-attacco-supply-chain-ha-compromesso-oltre-40-pacchetti-npm/#respond)
* [![GPUGate, una nuova tecnica che sfrutta Google Ads e GitHub per distribuire malware](https://www.securityinfo.it/wp-content/uploads/2025/09/data-theft-9480273_1920-1-120x85.jpg)](https://www.securityinfo.it/20...