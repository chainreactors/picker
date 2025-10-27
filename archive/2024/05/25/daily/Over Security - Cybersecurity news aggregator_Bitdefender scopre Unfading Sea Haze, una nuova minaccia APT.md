---
title: Bitdefender scopre Unfading Sea Haze, una nuova minaccia APT
url: https://www.securityinfo.it/2024/05/24/bitdefender-scopre-unfading-sea-haze-una-nuova-minaccia-apt/
source: Over Security - Cybersecurity news aggregator
date: 2024-05-25
fetch_date: 2025-10-06T17:19:26.326937
---

# Bitdefender scopre Unfading Sea Haze, una nuova minaccia APT

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

## Bitdefender scopre Unfading Sea Haze, una nuova minaccia APT

Mag 24, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2024/05/24/bitdefender-scopre-unfading-sea-haze-una-nuova-minaccia-apt/#respond)

---

Analizzando una serie di cyberattacchi contro organizzazioni di alto livello di nazioni del mar cinese meridionale, Bitdefender [ha individuato](https://www.bitdefender.com/blog/businessinsights/deep-dive-into-unfading-sea-haze-a-new-threat-actor-in-the-south-china-sea/) **Unfading Sea Haze, una nuova minaccia APT.**

L’obiettivo principale del gruppo, attivo presumibilmente dal 2018, è il **cyberspionaggio di obiettivi militari e governativi.** Finora il gruppo ha colpito almeno otto vittime in diverse nazioni della zona e, a giudicare dalla sua attività, sembra essere allineato agli interessi del governo cinese.

Poiché il primo accesso ai sistemi delle vittime è avvenuto sei anni fa, i ricercatori di Bitdefender non sono riusciti a scoprire la tecnica con cui il gruppo ha ottenuto il primo accesso; il team ha però scoperto che gli attaccanti usano **email di spear-phishing con file malevoli per riottenere l’accesso ai dispositivi** target e proseguire con l’esfiltrazione di dati.

![](https://www.securityinfo.it/wp-content/uploads/2024/05/network-3357642_1920.jpg)

Pixabay

## I tool e le tecniche di Unfading Sea Haze

Unfading Sea Haze usa u**n arsenale sofisticato di malware custom e tool** per stabilire la persistenza ed esfiltrare dati; tra questi emerge in particolare il **framework RAT (Remote Access Trojan) Gh0st personalizzato**, usato per colpire i sistemi Windows. Nei primi anni di attività il gruppo ha utilizzato principalmente tre tipi di malware: SilentGh0st, TranslucentGh0st e tre varianti di SharpJSHandler; in seguito, a partire dal 2023, gli attaccanti hanno cominciato a usare varianti più modulari del RAT quali FluffyGh0st, InsidiousGh0st e EtherealGh0st.

Per collezionare i dati, il gruppo usa diversi tool, sia personalizzati che off-the-shelf. Tra i tool custom si segnala **xkeylog**, un keylogger, e un **data stealer** creato appositamente **per sottrarre dati da browser** quali Google Chrome, Firefox, Edge e Internet Explorer. Il gruppo ha inoltre sviluppato un altro tool per **monitorare la presenza di dispositivi USB e portatili connessi alle macchine ed esfiltrare dati da essi.**

Oltre a questi strumenti, il gruppo usa anche tecniche manuali per raccogliere dati, comprimerli in archivi e inviarli al server C2, e colpisce anche i dati relativi ad applicazioni di messaggistica come **Telegram** e **Viber**.

Infine, per l’esfiltrazione delle informazioni, il gruppo fino al 2022 ha usato **DustyExfilTool**, uno strumento con riga di comando in grado di trasmettere i file al server specificato; in seguito, Unfading Sea Haze è passato all’uso di **curl** e del **protocollo FTP.**

![](https://www.securityinfo.it/wp-content/uploads/2024/05/hacking-3112539_1920-1.png)

Pixabay

## Come proteggersi

“Lo spostamento verso la modularità, gli elementi dinamici e l’esecuzione in memoria evidenzia i loro sforzi per aggirare le misure di sicurezza tradizionali. **Gli aggressori adattano costantemente le loro tattiche, rendendo necessario un approccio di sicurezza a più livelli**” hanno affermato i ricercatori di Bitdefender, sottolineando la necessità di adottare un approccio di sicurezza a strati per proteggersi efficacemente dalla minaccia APT.

Bitdefender consiglia innanzitutto di **dare priorità alla gestione delle patch** e tenere aggiornati i software, in particolare quelli esposti sul web, e impostare metodi di **autenticazione forte**. È inoltre necessario segmentare la rete in maniera appropriata, adottare un modello zero trust e **monitorare il traffico** per individuare qualsiasi pattern sospetto.

Infine, si consiglia di implementare soluzioni o scegliere **servizi di Detection and Response** e creare una cultura di cybersecurity aziendale che promuova la comunicazione e la condivisione di informazioni.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [APT](https://www.securityinfo.it/tag/apt/), [esfiltrazione dati](https://www.securityinfo.it/tag/esfiltrazione-dati/), [Gh0st](https://www.securityinfo.it/tag/gh0st/), [keylogger](https://www.securityinfo.it/tag/keylogger/), [RAT](https://www.securityinfo.it/tag/rat/), [Unfading Sea Haze](https://www.securityinfo.it/tag/unfading-sea-haze/)

[Le vulnerabilità IoT di Kaylay di ThroughTek impattano oltre 100 milioni di device](https://www.securityinfo.it/2024/05/24/le-vulnerabilita-iot-di-throughtek-kaylay-impattano-oltre-100-milioni-di-device/)
[Una vulnerabilità critica in Veeam Backup Enterprise Manager permette di bypassare l'autenticazione](https://www.securityinfo.it/2024/05/23/una-vulnerabilita-critica-in-veeam-backup-enterprise-manager-permette-di-bypassare-lautenticazione/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Campagne basate su installer ScreenConnect distribuiscono RAT multipli](https://www.securityinfo.it/wp-content/uploads/2025/09/ai-generated-8976964_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/09/22/campagne-basate-su-installer-screenconnect-distribuiscono-rat-multipli-lanalisi-di-acronis-tru/ "Campagne basate su installer ScreenConnect distribuiscono RAT multipli")

  [Campagne basate su installer...](https://www.securityinfo.it/2025/09/22...