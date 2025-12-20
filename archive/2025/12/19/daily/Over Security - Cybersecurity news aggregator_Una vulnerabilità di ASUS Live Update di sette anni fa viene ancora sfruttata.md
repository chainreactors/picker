---
title: Una vulnerabilità di ASUS Live Update di sette anni fa viene ancora sfruttata
url: https://www.securityinfo.it/2025/12/19/una-vulnerabilita-di-asus-live-update-di-sette-anni-fa-viene-ancora-sfruttata/
source: Over Security - Cybersecurity news aggregator
date: 2025-12-19
fetch_date: 2025-12-20T03:15:10.707042
---

# Una vulnerabilità di ASUS Live Update di sette anni fa viene ancora sfruttata

Aggiornamenti recenti Dicembre 19th, 2025 4:31 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Una vulnerabilità di ASUS Live Update di sette anni fa viene ancora sfruttata](https://www.securityinfo.it/2025/12/19/una-vulnerabilita-di-asus-live-update-di-sette-anni-fa-viene-ancora-sfruttata/)
* [Il cybercrime si evolve velocemente e l’IA diventa protagonista: le previsioni di Group-IB per il 2026](https://www.securityinfo.it/2025/12/18/il-cybercrime-si-evolve-velocemente-e-lia-diventa-protagonista-le-previsioni-di-group-ib-per-il-2026/)
* [Kaspersky, le PMI italiane sono un bersaglio strutturale per il cybercrime](https://www.securityinfo.it/2025/12/17/kaspersky-le-pmi-italiane-sono-un-bersaglio-strutturale-per-il-cybercrime/)
* [Il cybercrime si evolve e si adatta, integrando l’IA nel proprio arsenale: il report di ESET](https://www.securityinfo.it/2025/12/17/il-cybercrime-si-evolve-e-si-adatta-integrando-lia-nel-proprio-arsenale-il-report-di-eset/)
* [L’IA al centro delle strategie di cybersecurity future: le previsioni di Crowdstrike](https://www.securityinfo.it/2025/12/15/ia-al-centro-delle-strategie-di-cybersecurity-future-le-previsioni-di-crowdstrike/)

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

## Una vulnerabilità di ASUS Live Update di sette anni fa viene ancora sfruttata

Dic 19, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/12/19/una-vulnerabilita-di-asus-live-update-di-sette-anni-fa-viene-ancora-sfruttata/#respond)

---

Una **vecchia vulnerabilità di ASUS Live Update** è ancora tutt’altro che “morta”: pochi giorni fa la CISA [ha aggiunto](https://www.cisa.gov/news-events/alerts/2025/12/17/cisa-adds-three-known-exploited-vulnerabilities-catalog) il bug al catalogo delle **vulnerabilità sfruttate attivamente**, rivelando che il rischio è tutt’altro che risolto.

Come riporta [MalwareBytes](https://www.malwarebytes.com/blog/news/2025/12/cisa-warns-asus-live-update-backdoor-is-still-exploitable-seven-years-on), il caso è scoppiato nel 2019 con l’operazione **ShadowHammer**a opera del gruppo APT41. I cybercriminali riuscirono a iniettare codice malevolo nell’utility ASUS Live Update sfruttando questa falla e compromettendo i server di aggiornamento.

Il file malevolo era firmato con certificati digitali autentici ASUS, il che lo rendeva invisibile alla maggior parte degli antivirus. L’aggiornamento malevolo è stato inviato sui server ufficiali di ASUS, rendendo **l’infezione indistinguibile da un normale aggiornamento di sistema.**

![ASUS Live Update](https://www.securityinfo.it/wp-content/uploads/2025/12/Gemini_Generated_Image_8rl13l8rl13l8rl1.png)

Quello che sembrava un incubo ormai concluso è invece tornato prepotentemente alla carica con l’aggiornamento del catalogo CISA. La vulnerabilità, ora tracciata come **CVE-2025-59374**, viene ancora sfruttata attivamente dagli attaccanti dopo sette anni dalla sua individuazione.

Il problema principale sta nella longevità dell’hardware: **molti laptop e PC ASUS vecchi sono ancora in funzione** in ambienti domestici o uffici meno aggiornati. Poiché l’utility ASUS Live Update è stata ufficialmente dichiarata End-of-Support il 4 dicembre 2025, non riceverà più patch di sicurezza, lasciando chiunque utilizzi versioni precedenti alla 3.6.8 (o l’ultima 3.6.15) **esposto a potenziali attacchi.**

L’inclusione nel catalogo della CISA implica che le agenzie governative americane (e per riflesso molte aziende europee che seguono gli stessi standard) sono obbligate a rimuovere o aggiornare il software entro tempi molto brevi. La minaccia non è più limitata a ShadowHammer e APT41, ma **è altamente probabile che altri gruppi continuino a sfruttare la stessa falla** per distribuire ransomware o sottrarre dati sensibili.

Per proteggersi occorre innanzitutto verificare la versione di ASUS Live Update installata, controllando che sia almeno alla 3.6.8. Considerando che si tratta di un software a fine vita, il consiglio migliore è, se possibile, di **disinstallare l’utility** e passare a MyASUS, il tool più moderno e supportato dall’azienda per la gestione dei driver.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [aggiornamento](https://www.securityinfo.it/tag/aggiornamento/), [Asus](https://www.securityinfo.it/tag/asus/), [ASUS Live Update](https://www.securityinfo.it/tag/asus-live-update/), [backdoor](https://www.securityinfo.it/tag/backdoor/), [CISA](https://www.securityinfo.it/tag/cisa/), [ShadowHammer](https://www.securityinfo.it/tag/shadowhammer/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[Il cybercrime si evolve velocemente e l'IA diventa protagonista: le previsioni di Group-IB per il 2026](https://www.securityinfo.it/2025/12/18/il-cybercrime-si-evolve-velocemente-e-lia-diventa-protagonista-le-previsioni-di-group-ib-per-il-2026/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![L’IA al centro delle strategie di cybersecurity future: le previsioni di Crowdstrike](https://www.securityinfo.it/wp-content/uploads/2025/12/ai-7111803_1920-120x85.jpg)](https://www.securityinfo.it/2025/12/15/ia-al-centro-delle-strategie-di-cybersecurity-future-le-previsioni-di-crowdstrike/ "L’IA al centro delle strategie di cybersecurity future: le previsioni di Crowdstrike")

  [L’IA al centro delle strategie di...](https://www.securityinfo.it/2025/12/15/ia-al-centro-delle-strategie-di-cybersecurity-future-le-previsioni-di-crowdstrike/ "Permanent link to L’IA al centro delle strategie di cybersecurity future: le previsioni di Crowdstrike")

  Dic 15, 2025  [0](https://www.securityinfo.it/2025/12/15/ia-al-centro-delle-strategie-di-cybersecurity-future-le-previsioni-di-crowdstrike/#respond)
* [![Patch Tuesday, Microsoft risolve una vulnerabilità già sfruttata e due zero-day](https://www.securityinfo.it/wp-content/uploads/2025/12/Gemini_Generated_Image_k6tcvck6tcvck6tc-120x85.png)](https://www.securityinfo.it/2025/12/11/patch-tuesday-microsoft-risolve-una-vulnerabilita-gia-sfruttata-e-due-zero-day/ "Patch Tuesday, Microsoft risolve una vulnerabilità già sfruttata e due zero-day")

  [Patch Tuesday, Microsoft risolve una...](https://www.securityinfo.it/2025/12/11/patch-tuesday-microsoft-risolve-una-vulnerabilita-gia-sfruttata-e-due-zero-day/ "Permanent link to Patch Tuesday, Microsoft risolve una vulnerabilità già sfruttata e due zero-da...