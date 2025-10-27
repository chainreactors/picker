---
title: Scoperta GitVenom, campagna che sfrutta GitHub per rubare criptovalute
url: https://www.securityinfo.it/2025/02/26/scoperta-gitvenom-campagna-che-sfrutta-github-per-rubare-criptovalute/?utm_source=rss&utm_medium=rss&utm_campaign=scoperta-gitvenom-campagna-che-sfrutta-github-per-rubare-criptovalute
source: Securityinfo.it
date: 2025-02-27
fetch_date: 2025-10-06T20:38:50.743716
---

# Scoperta GitVenom, campagna che sfrutta GitHub per rubare criptovalute

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

## Scoperta GitVenom, campagna che sfrutta GitHub per rubare criptovalute

Feb 26, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [Hacking](https://www.securityinfo.it/category/news/hacking-news/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Malware](https://www.securityinfo.it/category/news/malware-news/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/02/26/scoperta-gitvenom-campagna-che-sfrutta-github-per-rubare-criptovalute/#respond)

---

I ricercatori di SecureList di Kaspersky hanno individuato **GitVenom**, una nuova campagna che sfrutta GitHub per distribuire codice malevolo e sottrarre criptovalute.

“*Nel corso della campagna GitVenom, **gli attaccanti hanno creato centinaia di repository su GitHub che contengono finti progetti con codice malevolo***” si legge nel [post](https://securelist.com/gitvenom-campaign/115694/) della compagnia. Tra le applicazioni disponibili ci sono strumenti per interagire con account Instagram, bot Telegram per gestire portafogli di Bitcoin e tool di hacking per Valorant.

I progetti malevoli sono **scritti in Python, JavaScript, C, C++ e C#**. Dall’analisi di Kaspersky è emerso che il codice dei repository esegue per lo più comandi inutili, fatta eccezione per la porzione di codice malevolo.

![](https://www.securityinfo.it/wp-content/uploads/2024/11/hacker-6512174_1920.jpg)

In tutti i casi esaminati, il payload si occupa di scaricare altri componenti malevoli da un repository GitHub degli attaccanti. Uno dei moduli è uno **stealer Node.js** che raccoglie informazioni quali credenziali salvate, dati dei portafogli di criptovalute e la cronologia del browser; tutti dati che vengono in seguito inviati a un bot Telegram controllato dagli attaccanti.

Gli altri moduli contengono **AsyncRAT**, un tool open-source per l’accesso remoto al dispositivo compromesso, la backdoor **Quasar** e un **hijacker della clipboard.**

Il team di SecureList evidenzia che gli attaccanti si sono preoccupati di far apparire i repository legittimi, aggiungendo anche file README ricchi di istruzioni per compilare il codice, probabilmente generati dall’IA. I repository inoltre contano **numerosi commit e tag.**

Molti dei progetti analizzati sono stati pubblicati oltre due anni fa. La campagna ha colpito per lo più utenti in Russia, Brasile e Turchia, ma ha avuto impatti significativi anche in altre parti del mondo.

“*Poiché le piattaforme di condivisione del codice come GitHub sono utilizzate da milioni di sviluppatori in tutto il mondo, **gli attaccanti continueranno sicuramente a utilizzare software falsi come esca per le infezioni***” avvisa Kaspersky; per questo motivo, prima di integrare del codice open-source nel proprio progetto è indispensabile analizzare attentamente le operazioni che svolge.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [codice malevolo](https://www.securityinfo.it/tag/codice-malevolo/), [criptovalute](https://www.securityinfo.it/tag/criptovalute/), [GitHub](https://www.securityinfo.it/tag/github/), [GitVenom](https://www.securityinfo.it/tag/gitvenom/), [malware](https://www.securityinfo.it/tag/malware/), [Open Source](https://www.securityinfo.it/tag/open-source/)

[CrowdStrike: ecco le minacce emergenti del 2025](https://www.securityinfo.it/2025/02/27/crowdstrike-report-minacce-2025/)
[Parallels Desktop: un bug 0-day consente di ottenere i permessi di root sui Mac](https://www.securityinfo.it/2025/02/25/parallels-desktop-un-bug-0-day-consente-di-ottenere-i-permessi-di-root-sui-mac/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Nuova variante del malware XCSSET prende di mira gli sviluppatori Xcode su macOS](https://www.securityinfo.it/wp-content/uploads/2025/09/MalwareCrypto-29-set-2025CG-120x85.png)](https://www.securityinfo.it/2025/09/26/nuova-variante-del-malware-xcsset-prende-di-mira-gli-sviluppatori-xcode-su-macos/ "Nuova variante del malware XCSSET prende di mira gli sviluppatori Xcode su macOS")

  [Nuova variante del malware XCSSET...](https://www.securityinfo.it/2025/09/26/nuova-variante-del-malware-xcsset-prende-di-mira-gli-sviluppatori-xcode-su-macos/ "Permanent link to Nuova variante del malware XCSSET prende di mira gli sviluppatori Xcode su macOS")

  Set 26, 2025  [0](https://www.securityinfo.it/2025/09/26/nuova-variante-del-malware-xcsset-prende-di-mira-gli-sviluppatori-xcode-su-macos/#respond)
* [![MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  [MuddyWater si evolve: attacchi più...](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "Permanent link to MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  Set 17, 2025  [0](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/#respond)
* [![GPUGate, una nuova tecnica che sfrutta Google Ads e GitHub per distribuire malware](https://www.securityinfo.it/wp-content/uploads/2025/09/data-theft-9480273_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/09/09/gpugate-una-nuova-tecni...