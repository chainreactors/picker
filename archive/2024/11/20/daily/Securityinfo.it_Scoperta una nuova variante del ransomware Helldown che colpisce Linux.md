---
title: Scoperta una nuova variante del ransomware Helldown che colpisce Linux
url: https://www.securityinfo.it/2024/11/19/scoperta-una-nuova-variante-del-ransomware-helldown-che-colpisce-linux/?utm_source=rss&utm_medium=rss&utm_campaign=scoperta-una-nuova-variante-del-ransomware-helldown-che-colpisce-linux
source: Securityinfo.it
date: 2024-11-20
fetch_date: 2025-10-06T19:19:35.237461
---

# Scoperta una nuova variante del ransomware Helldown che colpisce Linux

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

## Scoperta una nuova variante del ransomware Helldown che colpisce Linux

Nov 19, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Malware](https://www.securityinfo.it/category/news/malware-news/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2024/11/19/scoperta-una-nuova-variante-del-ransomware-helldown-che-colpisce-linux/#respond)

---

I ricercatori di Sekoia [hanno individuato](https://blog.sekoia.io/helldown-ransomware-an-overview-of-this-emerging-threat/) una nuova variante del **ransomware Helldown** che colpisce i sistemi **Linux**. Scoperto lo scorso agosto, inizialmente il ransomware colpiva solo sistemi Windows, mentre ora ha esteso il suo raggio d’azione.

Helldown è un ransomware a **doppia estorsione** che **sfrutta vulnerabilità note** per accedere alle reti aziendali e diffondere il malware. Dalle analisi di Sekoia emerge che il gruppo ha sfruttato alcuni bug nelle appliance Zyxel per l’accesso iniziale e in seguito rubare credenziali e creare tunnel SSL VPN per la comunicazione.

![Helldown ransomware](https://www.securityinfo.it/wp-content/uploads/2024/11/download.png)

Nei suoi attacchi, il gruppo ha ottenuto grandi volumi di dati, per una **media di 70 GB per vittima**, con picchi anche di 431 GB. “***Questo approccio differisce dalla strategia tipica di altri gruppi ransomware**, i quali di solito preferiscono esfiltrazioni più selettive e mirate per rimanere discreti e massimizzare il potenziale danno nel caso di un leak*” scrivono i ricercatori. I file sottratti sono di vario tipo, ma la maggior parte consiste di documenti PDF.

**La variante Linux è stata scoperta il 31 ottobre.** Il malware carica una configurazione XML hard-coded dove sono indicate specifiche azioni e relativi tag; in seguito, il ransomware itera sui path forniti come argomenti della funzione del programma e, quando trova un file con un’estensione di interesse, lo cifra totalmente o parzialmente, in base alla sua dimensione. Finita la fase di cifratura, viene creata la nota di riscatto. Per la chiave di cifratura viene usato RSA PKCS1.

Il ransomware è anche in grado di **accedere alla lista di macchine virtuali in esecuzione e interrompere i singoli processi.**

Secondo i dati dei ricercatori, Helldown è particolarmente attivo: solo **negli ultimi tre mesi il ransomware ha colpito con successo 31 vittime.** Gli obiettivi più colpiti sono realtà medio-piccole degli Stati Uniti, anche se tra le vittime si annoverano business europei. I settori più colpiti sono quelli dei servizi IT, delle telecomunicazione, il manifatturiero e il sanitario.

Al momento non ci sono prove che il gruppo sia legato ad altre gang più note. I ricercatori di Sekoia ritengono che Helldown possa avere qualche connessione con **Darkrace** o **Donex** per via delle similarità tra i ransomware, anche se è ancora difficile confermare l’esistenza di una relazione.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [cifratura](https://www.securityinfo.it/tag/cifratura/), [doppia estorsione](https://www.securityinfo.it/tag/doppia-estorsione/), [Helldown](https://www.securityinfo.it/tag/helldown/), [Linux](https://www.securityinfo.it/tag/linux/), [Ransomware](https://www.securityinfo.it/tag/ransomware/), [Sekoia](https://www.securityinfo.it/tag/sekoia/)

[Una grave data breach ha colpito le aziende statunitensi di telecomunicazioni](https://www.securityinfo.it/2024/11/20/una-grave-data-breach-ha-colpito-le-aziende-statunitensi-di-telecomunicazioni/)
[Una vulnerabilità di un plugin di WordPress mette a rischio più di 4 milioni di siti](https://www.securityinfo.it/2024/11/18/una-vulnerabilita-di-un-plugin-di-wordpress-mette-a-rischio-piu-di-4-milioni-di-siti/)

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
* [![GPUGate, una nuova tecnica che sfrutta Google ...