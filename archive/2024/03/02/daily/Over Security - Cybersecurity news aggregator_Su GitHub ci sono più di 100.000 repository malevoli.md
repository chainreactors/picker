---
title: Su GitHub ci sono più di 100.000 repository malevoli
url: https://www.securityinfo.it/2024/03/01/su-github-ci-sono-piu-di-100-000-repository-malevoli/
source: Over Security - Cybersecurity news aggregator
date: 2024-03-02
fetch_date: 2025-10-04T12:12:20.698175
---

# Su GitHub ci sono più di 100.000 repository malevoli

Aggiornamenti recenti Ottobre 3rd, 2025 6:09 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)
* [Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)
* [Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/)
* [Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/)

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

## Su GitHub ci sono più di 100.000 repository malevoli

Mar 01, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [Phishing](https://www.securityinfo.it/category/news/phishing/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2024/03/01/su-github-ci-sono-piu-di-100-000-repository-malevoli/#respond)

---

I ricercatori di Apiiro, fornitore di soluzioni unificate di sicurezza, [hanno individuato](https://apiiro.com/blog/malicious-code-campaign-github-repo-confusion-attack/) l’espansione di una **campagna di repository confusion** che finora ha impattato **migliaia di repo GitHub**. La campagna, cominciata a metà dello scorso anno, ha avuto un picco negli ultimi mesi.

Negli attacchi di repository confusion gli attaccanti mirano a **far scaricare alle vittime il proprio codice infetto invece di quello reale**. Generalmente gli attaccanti clonano il repo target, lo infettano con payload di malware e lo caricano su GitHub con lo stesso nome. Per aumentare le possibilità di download, effettuano centinaia di fork e poi promuovono il repository sul web, usando forum e chat di sviluppatori.

Dopo che i developer hanno scaricato il repository, **il payload nascosto installa il malware** che raccoglie credenziali di login da diverse applicazioni, password e cookie del browser, oltre ad altri dati sensibili, e li invia al server C2 degli attaccanti.

Molti dei repository malevoli sono stati rimossi da GitHub per via delle centinaia di fork, ma molti altri sono riusciti a eludere i controlli della piattaforma.  I ricercatori spiegano che la campagna avviene su larga scala, quindi **il numero di repository ancora online si aggira intorno alle centinaia di migliaia**; considerando anche i repo rimossi, **si parla di milioni di applicazioni malevole.** Non solo: vista l’ampia portata degli attacchi, essi generano una sorta di rete di “ingegneria sociale di secondo ordine” nel momento in cui gli sviluppatori condividono i repo dannosi senza sapere che contengono malware.

![GitHub repository](https://www.securityinfo.it/wp-content/uploads/2024/03/code-5290465_1920.jpg)

Pixabay

La tecnica di repository confusion su GitHub ha diversi vantaggi: in primis, la piattaforma ospita talmente tanti repo che, nonostante le istanze malevole siano molte, queste r**appresentano comunque una porzione insignificante del totale** ed è quindi difficile individuarle; inoltre, in questa campagna non vengono sfruttati i package manager, e ciò rende più complesso riconoscere i repo malevoli; infine, poiché **i repository colpiti sono poco conosciuti** e utilizzati solo da una nicchia di sviluppatori, è più semplice trarre in inganno gli utenti.

“GitHub è stata avvisata del problema e la maggior parte dei repository malevoli sono stati eliminati” scrivono i ricercatori, “ma **la campagna continua e gli attacchi che tentano di iniettare codice malevolo nella supply chain stanno diventando sempre più diffusi**“.

Oltre a chiedere agli sviluppatori di controllare attentamente i repository che stanno scaricando, Apiiro consiglia alle organizzazioni di **implementare soluzioni per il monitoraggio del codice**, sfruttando tecniche di analisi basate su IA per individuare porzioni di codice sospette.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [GitHub](https://www.securityinfo.it/tag/github/), [ingegneria sociale](https://www.securityinfo.it/tag/ingegneria-sociale/), [payload](https://www.securityinfo.it/tag/payload/), [Phishing](https://www.securityinfo.it/tag/phishing/), [repository](https://www.securityinfo.it/tag/repository/), [repository confusion](https://www.securityinfo.it/tag/repository-confusion/)

[CERT-AGID 24 Febbraio – 1 Marzo: 16 campagne malevole, Banking il tema più gettonato](https://www.securityinfo.it/2024/03/04/cert-agid-24-febbraio-1-marzo-16-campagne-malevole-banking-tema-gettonato/)
[Scoperta una nuova versione di Bifrost che colpisce Linux](https://www.securityinfo.it/2024/03/01/scoperta-una-nuova-versione-di-bifrost-che-colpisce-linux/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Nuova variante del malware XCSSET prende di mira gli sviluppatori Xcode su macOS](https://www.securityinfo.it/wp-content/uploads/2025/09/MalwareCrypto-29-set-2025CG-120x85.png)](https://www.securityinfo.it/2025/09/26/nuova-variante-del-malware-xcsset-prende-di-mira-gli-sviluppatori-xcode-su-macos/ "Nuova variante del malware XCSSET prende di mira gli sviluppatori Xcode su macOS")

  [Nuova variante del malware XCSSET...](https://www.securityinfo.it/2025/09/26/nuova-variante-del-malware-xcsset-prende-di-mira-gli-sviluppatori-xcode-su-macos/ "Permanent link to Nuova variante del malware XCSSET prende di mira gli sviluppatori Xcode su macOS")

  Set 26, 2025  [0](https://www.securityinfo.it/2025/09/26/nuova-variante-del-malware-xcsset-prende-di-mira-gli-sviluppatori-xcode-su-macos/#respond)
* [![Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-6138007_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/ "Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA")

  [Report Acronis: il ransomware rimane la...](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-...