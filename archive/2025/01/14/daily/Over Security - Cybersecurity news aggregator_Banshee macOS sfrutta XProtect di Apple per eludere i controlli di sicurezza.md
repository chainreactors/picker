---
title: Banshee macOS sfrutta XProtect di Apple per eludere i controlli di sicurezza
url: https://www.securityinfo.it/2025/01/13/banshee-macos-sfrutta-xprotect-di-apple-per-eludere-i-controlli-di-sicurezza/
source: Over Security - Cybersecurity news aggregator
date: 2025-01-14
fetch_date: 2025-10-06T20:12:53.668521
---

# Banshee macOS sfrutta XProtect di Apple per eludere i controlli di sicurezza

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

## Banshee macOS sfrutta XProtect di Apple per eludere i controlli di sicurezza

Gen 13, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Malware](https://www.securityinfo.it/category/news/malware-news/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/01/13/banshee-macos-sfrutta-xprotect-di-apple-per-eludere-i-controlli-di-sicurezza/#respond)

---

I ricercatori di Check Point Research [hanno studiato](https://blog.checkpoint.com/research/cracking-the-code-how-banshee-stealer-targets-macos-users/) una **nuova versione dello stealer Banshee macOS** che include nuove feature per eludere i controlli di sicurezza standard.

Il malware, scoperto a metà 2024, è in grado di sottrarre credenziali salvate nel browser, portafogli di criptovalute e altri dati sensibili. La nuova versione, rimasta inosservata per più di due mesi, **usa la funzionalità di cifratura delle stringhe di XProtect di Apple per superare i controlli degli antivirus.**

“*Questo malware furtivo non si limita a infiltrarsi, ma opera senza essere rilevato, mescolandosi perfettamente con i normali processi di sistema e rubando le credenziali del browser, i portafogli di criptovalute, le password degli utenti e i dati sensibili dei file. **Ciò che rende Banshee davvero allarmante è la sua capacità di eludere il rilevamento*****“** hanno sottolineato i ricercatori.

![Banshee macOS](https://www.securityinfo.it/wp-content/uploads/2025/01/macbook-pro-2381729_1920.jpg)

Gli attaccanti dietro Banshee macOS sono riusciti a sottrarre l’algoritmo per la cifratura delle stringhe dal motore antivirus di Apple, XProtect, permettendo così allo stealer di operare indisturbato per più di due mesi.

Il malware, nato come **stealer-as-a-service**, è stato distribuito tramite siti di phishing e repository GitHub che si fingevano software popolari come Chrome, Telegram e TradingView.

Una volta scaricato e installato, il malware è in grado di ottenere **credenziali e altri dati sensibili da browser quali Chrome, Brave, Edge** e Vivaldi, oltre che sfruttare le estensioni installate per sottrarre i fondi dei portafogli di criptovalute; inoltre, lo stealer mostra dei pop-up agli utenti che appaiono come prompt legittimi di sistema per indurli a **inserire la propria password macOS.**

Lo scorso novembre il codice sorgente dello stealer è stato pubblicato sui forum del dark web, permettendo così ai ricercatori di comprendere il suo meccanismo e rafforzare le difese. Nonostante **il progetto originale sia stato chiuso dopo il leak**, il team di Check Point Research ha scoperto numerose campagne che continuano a distribuire il malware. Non è chiaro se dietro queste operazioni ci sia il vecchio team di attaccanti o i clienti del gruppo.

I ricercatori di Check Point evidenziano anche che l’ultima versione del malware aveva **rimosso il controllo sulla lingua russa**: inizialmente lo stealer si fermava se individuava l’uso del russo sul dispositivo target, mentre nelle ultime campagne questo check è stato eliminato del tutto, ampliando di conseguenza il raggio di possibili vittime.

**“*Il successo di Banshee evidenzia la natura in evoluzione delle cyberminacce e la necessità di adottare difese robuste*“** spiegano i ricercatori. Anche se il progetto principale non è più attivo, la minaccia di Banshee non si arresta e potrebbe ripresentarsi in futuro in altre forme, sotto altri nomi.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [antivirus](https://www.securityinfo.it/tag/antivirus/), [Apple](https://www.securityinfo.it/tag/apple/), [Banshee macOS](https://www.securityinfo.it/tag/banshee-macos/), [rilevamento](https://www.securityinfo.it/tag/rilevamento/), [stealer](https://www.securityinfo.it/tag/stealer/), [xProtect](https://www.securityinfo.it/tag/xprotect/)

[L'IA generativa rivoluziona il cybercrimine e rende gli attacchi più pericolosi](https://www.securityinfo.it/2025/01/15/ia-generativa-rivoluziona-il-cybercrimine-e-rende-gli-attacchi-piu-pericolosi/)
[CERT-AGID 4 – 10 gennaio: Vidar protagonista con una campagna malspam](https://www.securityinfo.it/2025/01/13/cert-agid-4-10-gennaio-vidar-protagonista-con-una-campagna-malspam/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Apple rilascia una fix per una vulnerabilità di Safari già sfruttata in Chrome](https://www.securityinfo.it/wp-content/uploads/2025/07/Gemini_Generated_Image_1mvtjc1mvtjc1mvt-120x85.png)](https://www.securityinfo.it/2025/07/30/apple-rilascia-una-fix-per-una-vulnerabilita-di-safari-gia-sfruttata-in-chrome/ "Apple rilascia una fix per una vulnerabilità di Safari già sfruttata in Chrome")

  [Apple rilascia una fix per una...](https://www.securityinfo.it/2025/07/30/apple-rilascia-una-fix-per-una-vulnerabilita-di-safari-gia-sfruttata-in-chrome/ "Permanent link to Apple rilascia una fix per una vulnerabilità di Safari già sfruttata in Chrome")

  Lug 30, 2025  [0](https://www.securityinfo.it/2025/07/30/apple-rilascia-una-fix-per-una-vulnerabilita-di-safari-gia-sfruttata-in-chrome/#respond)
* [![Apple risolve un bug 0-day di WebKit già sfruttato](https://www.securityinfo.it/wp-content/uploads/2025/03/2808-120x85.jpg)](https://www.securityinfo.it/2025/03/12/apple-risolve-un-bug-0-day-di-webkit-gia-sfruttato/ "Apple risolve un bug 0-day di WebKit già sfruttato")

  [Apple risolve un bug 0-day di WebKit...](https://www.securityinfo.it/2025/03/12/apple-risolve-un-bug-0-day-di-webkit-gia...