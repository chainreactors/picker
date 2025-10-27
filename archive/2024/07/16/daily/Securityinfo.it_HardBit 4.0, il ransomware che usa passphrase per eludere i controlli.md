---
title: HardBit 4.0, il ransomware che usa passphrase per eludere i controlli
url: https://www.securityinfo.it/2024/07/15/hardbit-4-0-il-ransomware-che-usa-passphrase-per-eludere-i-controlli/?utm_source=rss&utm_medium=rss&utm_campaign=hardbit-4-0-il-ransomware-che-usa-passphrase-per-eludere-i-controlli
source: Securityinfo.it
date: 2024-07-16
fetch_date: 2025-10-06T17:45:09.991855
---

# HardBit 4.0, il ransomware che usa passphrase per eludere i controlli

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

## HardBit 4.0, il ransomware che usa passphrase per eludere i controlli

Lug 15, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2024/07/15/hardbit-4-0-il-ransomware-che-usa-passphrase-per-eludere-i-controlli/#respond)

---

I ricercatori di Cybereason [hanno scoperto](https://www.cybereason.com/blog/hardening-of-hardbit) una nuova variante del ransomware HardBit che sfrutta una passphrase per offuscare il payload ed eluderei controlli.

Apparso per la prima volta nell’ottobre 2022, HardBit, diversamente da ransomware più conosciuti, **non ha dei siti di leak e non sfrutta il meccanismo della doppia estorsione.** Nella nota del riscatto, il gruppo sottolinea che, se la somma richiesta non viene pagata, attaccherà nuovamente la vittima.

![HardBit](https://www.securityinfo.it/wp-content/uploads/2024/07/ransomware-2320941_1920.jpg)

Pixabay

In ogni caso, **il ransomware presenta molte somiglianze con LockBit**, a partire dal nome ma anche per via delle icone usate, dei font delle scritte nelle immagini e del testo della nota di riscatto. Al momento non si è a conoscenza di possibili legami tra i due gruppi ed è possibile che si tratti solo di una tecnica di “marketing” per imitare LockBit.

I ricercatori non sanno dire con esattezza quale sia il vettore d’attacco iniziale, ma l’ipotesi principale è che il gruppo usi **attacchi brute force contro servizi RDP e SMB.** Una volta ottenuto l’accesso al sistema target, il gruppo si sposta lateralmente ottenendo altre credenziali tramite Mimikatz e il tool NLBrute per attacchi brute force.

A supporto delle attività di movimento laterale, la gang usa Advanced Port Scanner, KPortScan 3.0 e 5-NS new.exe, tre tool per la scansione delle reti.

La particolarità di questo ransomware è che utilizza un **metodo di offuscamento dei file binari** che sfrutta una passphrase. Al contrario delle password, le passphrase sono più lunghe (almeno 20 caratteri) e rappresentano un’intera frase (da qui il loro nome).

Per eseguire il binario, gli attaccanti devono fornire una passphrase; per ottenerla, devono decodificare l’ID di autenticazione presente nel file id\_authorization.txt con la chiave privata presente in Private.txt. “***La passphrase deve essere fornita durante il runtime affinché il ransomware venga eseguito correttament**e. L’ulteriore offuscamento impedisce ai ricercatori di sicurezza di analizzare il malware*” scrivono i ricercatori.

HardBit è anche in grado di **disabilitare Microsoft Defender Antivirus** e terminare processi e servizi, sia per eludere i controlli che per inibire le capacità di recovery del sistema target.

Per proteggersi dai ransomware è consigliato come sempre **dotarsi di soluzioni specifiche contro queste minacce** e impostare l’**autenticazione multi-fattore** per tutti i servizi esposti a Internet. È importante inoltre controllare attentamente gli allegati e i link su cui si clicca e prevede **piani di backup robusti.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Cybereason](https://www.securityinfo.it/tag/cybereason/), [HardBit](https://www.securityinfo.it/tag/hardbit/), [LockBit](https://www.securityinfo.it/tag/lockbit/), [offuscamento](https://www.securityinfo.it/tag/offuscamento/), [passphrase](https://www.securityinfo.it/tag/passphrase/), [Ransomware](https://www.securityinfo.it/tag/ransomware/)

[Proteggere le nuove superfici di attacco con il Cloud Security Posture Management](https://www.securityinfo.it/2024/07/15/proteggere-le-nuove-superfici-di-attacco-con-il-cloud-security-posture-management/)
[Il furto di informazioni è la minaccia più diffusa](https://www.securityinfo.it/2024/07/12/il-furto-di-informazioni-e-la-minaccia-piu-diffusa/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/wp-content/uploads/2025/10/Gemini_Generated_Image_t7m3xlt7m3xlt7m3-120x85.png)](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/ "RedHat vittima di un breach: sottratti oltre 500 GB di dati")

  [RedHat vittima di un breach: sottratti...](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/ "Permanent link to RedHat vittima di un breach: sottratti oltre 500 GB di dati")

  Ott 03, 2025  [0](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/#respond)
* [![Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-6138007_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/ "Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA")

  [Report Acronis: il ransomware rimane la...](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/ "Permanent link to Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA")

  Set 11, 2025  [0](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/#respond)
* [![GPUGate, una nuova tecnica che sfrutta Google Ads e GitHub p...