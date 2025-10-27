---
title: Npm, attacco supply chain: compromesso un package con 45.000 download settimanali
url: https://www.securityinfo.it/2025/05/09/npm-attacco-supply-chain-compromesso-un-package-con-45-000-download-settimanali/?utm_source=rss&utm_medium=rss&utm_campaign=npm-attacco-supply-chain-compromesso-un-package-con-45-000-download-settimanali
source: Securityinfo.it
date: 2025-05-10
fetch_date: 2025-10-06T22:31:25.511214
---

# Npm, attacco supply chain: compromesso un package con 45.000 download settimanali

Aggiornamenti recenti Ottobre 6th, 2025 3:00 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Microsoft Sentinel: arriva l’era degli agenti AI e della difesa predittiva](https://www.securityinfo.it/2025/10/06/microsoft-sentinel-arriva-lera-degli-agenti-ai-e-della-difesa-predittiva/)
* [CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)
* [Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)

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

## Npm, attacco supply chain: compromesso un package con 45.000 download settimanali

Mag 09, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/05/09/npm-attacco-supply-chain-compromesso-un-package-con-45-000-download-settimanali/#respond)

---

Qualche giorno fa i ricercatori di Aikido [hanno individuato](https://www.aikido.dev/blog/catching-a-rat-remote-access-trojian-rand-user-agent-supply-chain-compromise) un **attacco supply chain contro `rand-user-agent`, un package npm** della compagnia WebScraping API che contra circa 45.000 download settimanali.

![attacco supply chain npm](https://www.securityinfo.it/wp-content/uploads/2025/05/hacking-4038037_1920-1.jpg)

Il [package](https://www.npmjs.com/package/rand-user-agent), nonostante sia deprecato, viene ancora usato da molti utenti per generare stringhe user-agent randomiche, usate per effettuare il web scraping, automatizzare test e condurre analisi di sicurezza. Durante l’esecuzione di una pipeline, il sistema di analisi automatizzata di Aikido ha segnalato `rand-user-agent` come pacchetto sospetto; in particolare, ha evidenziato la presenza di codice malevolo nel file `dist/index.js`.

Il codice malevolo non è immediatamente visibile da una semplice occhiata al file: gli attaccanti hanno offuscato il codice in modo che si potesse visualizzare solo scrollando la barra di navigazione orizzontalmente.

![](https://www.securityinfo.it/wp-content/uploads/2025/05/681a3b0a4b86d503be5acf90_Untitled-design-11.png)

Credits: Aikido

Il codice, nascosto tramite molteplici livelli di offuscamento, appartiene a un **trojan ad accesso remoto** (RAT) in grado di **connettersi a un server C2** tramite `socket.io-client` ed [esfiltrare file](https://www.securityinfo.it/2025/04/11/shuckworm-prende-di-mira-le-missioni-in-ucraina-con-device-rimovibili/) con `axios`.

Il RAT ha anche una feature molto particolare progettata per sistemi Windows gli permette di **eseguire binari malevoli spacciandosi per un tool Python**. Lo script appende un percorso particolare alla variabile d’ambiente `PATH` prima di eseguire qualsiasi comando shell. “*Iniettando questo percorso all’inizio di PATH, qualsiasi comando che si affida a eseguibili environment-resolved (python, pip, ec…) può essere compromesso senza che l’utente se ne accora. Questo è particolarmente efficace sui sistemi dove ci si aspetta che Python sia già presente*“.

**Sembra che il codice malevolo sia presente da 7 mesi sul repository**, a partire dalla versione 2.0.80. Dopo di essa, sono state rilasciate altre cinque versioni e tutte contenevano il payload del RAT. Attualmente su npm le versioni malevole non sono più disponibili ed è possibile scaricare l’ultimo aggiornamento in sicurezza. Nel caso in precedenza si fosse usata una delle versioni compromesse, è importante eseguire una **scansione completa del proprio dispositivo per individuare l’eventuale presenza del trojan.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [attacco supply chain](https://www.securityinfo.it/tag/attacco-supply-chain/), [codice offuscato](https://www.securityinfo.it/tag/codice-offuscato/), [npm](https://www.securityinfo.it/tag/npm/), [Python](https://www.securityinfo.it/tag/python/), [rand-user-agent](https://www.securityinfo.it/tag/rand-user-agent/), [RAT](https://www.securityinfo.it/tag/rat/)

[Lockbit hackerato: infrastruttura compromessa, ma il gruppo non si arrende](https://www.securityinfo.it/2025/05/09/lockbit-hackerato-infrastruttura-compromessa-ma-il-gruppo-non-si-arrende/)
[L'infrastruttura petrolifera statunitense è sotto attacco](https://www.securityinfo.it/2025/05/08/infrastruttura-petrolifera-statunitense-e-sotto-attacco/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Campagne basate su installer ScreenConnect distribuiscono RAT multipli](https://www.securityinfo.it/wp-content/uploads/2025/09/ai-generated-8976964_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/09/22/campagne-basate-su-installer-screenconnect-distribuiscono-rat-multipli-lanalisi-di-acronis-tru/ "Campagne basate su installer ScreenConnect distribuiscono RAT multipli")

  [Campagne basate su installer...](https://www.securityinfo.it/2025/09/22/campagne-basate-su-installer-screenconnect-distribuiscono-rat-multipli-lanalisi-di-acronis-tru/ "Permanent link to Campagne basate su installer ScreenConnect distribuiscono RAT multipli")

  Set 22, 2025  [0](https://www.securityinfo.it/2025/09/22/campagne-basate-su-installer-screenconnect-distribuiscono-rat-multipli-lanalisi-di-acronis-tru/#respond)
* [![Un attacco supply chain ha compromesso oltre 40 pacchetti NPM](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_px0h5ppx0h5ppx0h-120x85.png)](https://www.securityinfo.it/2025/09/16/un-attacco-supply-chain-ha-compromesso-oltre-40-pacchetti-npm/ "Un attacco supply chain ha compromesso oltre 40 pacchetti NPM")

  [Un attacco supply chain ha compromesso...](https://www.securityinfo.it/2025/09/16/un-attacco-supply-chain-ha-compromesso-oltre-40-pacchetti-npm/ "Permanent link to Un attacco supply chain ha compromesso oltre 40 pacchetti NPM")

  Set 16, 2025  [0](https://www.securityinfo.it/2025/09/16/un-attacco-supply-chain-ha-compromesso-oltre-40-pacchetti-npm/#respond)
* [![Malware dentro il malware: trovate bac...