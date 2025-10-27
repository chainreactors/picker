---
title: Avast rilascia un decryptor per il ransomware DoNex
url: https://www.securityinfo.it/2024/07/09/avast-rilascia-un-decryptor-per-il-ransomware-donex/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-10
fetch_date: 2025-10-06T17:47:28.232427
---

# Avast rilascia un decryptor per il ransomware DoNex

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

## Avast rilascia un decryptor per il ransomware DoNex

Lug 09, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Hacking](https://www.securityinfo.it/category/news/hacking-news/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Tecnologia](https://www.securityinfo.it/category/news/tecnologia-news/)
 [0](https://www.securityinfo.it/2024/07/09/avast-rilascia-un-decryptor-per-il-ransomware-donex/#respond)

---

I ricercatori di **Avast** [hanno annunciato](https://decoded.avast.io/threatresearch/decrypted-donex-ransomware-and-its-predecessors/) di aver individuato una vulnerabilità nello schema crittografico di **DoNex** e di averla sfruttata per creare un **decryptor per il ransomware.**

**DoNex è figlio di numerose modifiche e rebrand derivanti da Muse**, ransomware apparso per la prima volta nell’aprile 2022. Nel novembre dello stesso anno il malware si è evoluto per somigliare a LockBit 3.0, mentre a maggio 2023 è stato modificato ancora una volta prendendo il nome di DarkRace; infine, lo scorso marzo è apparso nella sua versione finale.

![decryptor DoNex](https://www.securityinfo.it/wp-content/uploads/2024/07/cybersecurity-7119389_1920.jpg)

Pixabay

Il ransomware ha attaccato organizzazioni in diversi Paesi e, secondo la telemetria di Avast, **è stato attivo per lo più negli Stati Uniti, in Italia e in Belgio.**

I ricercatori hanno spiegato che **la chiave di cifratura viene generata tramite la funzione deprecata CryptGenRandom()** inclusa in Microsoft CryptoAPI. La chiave viene utilizzata poi per inizializzare la chiave simmetrica ChaCha20 e procedere con la cifratura dei file. Dopo che un file viene cifrato, il file della chiave simmetrica viene a sua volta cifrato con RSA-4096 e aggiunto alla fine del file.

Durante l’operazione di cifratura, tutti i file con dimensione massima di 1MB vengono cifrati interamente, mentre quelli più grandi vengono divisi in blocchi cifrati separatamente (cifratura intermittente).

Nel report la compagnia **non ha specificato che tipo di vulnerabilità ha utilizzato per creare il decryptor**, ma ha chiarito che la debolezza era già stata resa nota durante il Recon 2024 e che quindi non c’era più motivo di tenerla segreta.

Il decryptor di Avast funziona sia per DoNex che per tutti i suoi predecessori. **Il tool è scaricabile direttamente dalla pagina del report** e consente di ripristinare in pochi passi i file cifrati.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Avast](https://www.securityinfo.it/tag/avast/), [cifratura](https://www.securityinfo.it/tag/cifratura/), [DarkRace](https://www.securityinfo.it/tag/darkrace/), [decryptor](https://www.securityinfo.it/tag/decryptor/), [Muse](https://www.securityinfo.it/tag/muse/), [NoDex](https://www.securityinfo.it/tag/nodex/), [Ransomware](https://www.securityinfo.it/tag/ransomware/)

[La quasi totalità degli attacchi a device IoT sfrutta vulnerabilità risolte](https://www.securityinfo.it/2024/07/09/la-quasi-totalita-degli-attacchi-a-device-iot-sfrutta-vulnerabilita-risolte/)
[L'Europol si lamenta dell'home routing: "è un ostacolo per le intercettazioni"](https://www.securityinfo.it/2024/07/08/l-europol-si-lamenta-dellhome-routing-e-un-ostacolo-per-le-intercettazioni/)

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
* [![GPUGate, una nuova tecnica che sfrutta Google Ads e GitHub per distribuire malware](https://www.securityinfo.it/wp-content/uploads/2025/09/data-theft-9480273_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/09/09/gpugate-una-nuova-tecnica-che-sfrutta-google-ads-e-github-per-distribuire-malware/ "GPUGate, una nuova tecnica che sfrutta Google Ads e GitHub per distribuire malware")

  [GPUGate, una nuova tecnica che sfrutta...](https://www.securityinfo.it/2025/09/09/gpugate-una-nuova-tecnica-che-sfrutta-google-ads-e-github-per-distribuire-malware/ "Permanent link to GPUGate, una nuova tecnica che sfrutta Google Ads e GitHub per distribuire malware")

  Set 09, 2025  [0](...