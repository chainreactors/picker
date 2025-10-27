---
title: Gli errori di sicurezza più comuni nelle applicazioni web
url: https://www.securityinfo.it/2023/03/15/errori-sicurezza-applicazioni-web/?utm_source=rss&utm_medium=rss&utm_campaign=errori-sicurezza-applicazioni-web
source: Over Security - Cybersecurity news aggregator
date: 2023-03-16
fetch_date: 2025-10-04T09:47:29.713616
---

# Gli errori di sicurezza più comuni nelle applicazioni web

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

## Gli errori di sicurezza più comuni nelle applicazioni web

Mar 15, 2023  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Hacking](https://www.securityinfo.it/category/approfondimenti/hacking/), [Minacce](https://www.securityinfo.it/category/approfondimenti/minacce/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2023/03/15/errori-sicurezza-applicazioni-web/#respond)

---

**Le applicazioni web sono ancora il vettore preferito dagli attaccanti per effettuare data breach**, rappresentando circa il 70% dei punti di ingresso degli attacchi. Questo perché, [come riportato da **Nick Merritt**](https://www.darkreading.com/application-security/5-lessons-learned-from-hundreds-of-penetration-tests), vice presidente di Security Products and Services di Halo Security, **le applicazioni sono ricche di vulnerabilità non gestite.**

Gli sviluppatori si trovano in una posizione difficile nella quale devono sviluppare più feature possibili nel minor tempo, senza riuscire a implementare adeguati controlli di sicurezza o usare framework di cybersecurity. Nella sua analisi **Merritt ha illustrato i cinque errori più comuni commessi dagli sviluppatori**, individuati tramite ripetuti penetration test su varie applicazioni web.

## Cinque errori di sicurezza degli sviluppatori

Una delle vulnerabilità più comuni presenti nelle applicazioni web è il **cross-site scripting (XSS)**, che permette a un attaccante di iniettare codice malevolo nei siti web per ottenere e manipolare informazioni sensibili. Usare librerie per validare gli input e utilizzare il flag HttpOnly per proteggere i cookie sono due step fondamentali per proteggere gli utenti, ma non sono sufficienti: **gli sviluppatori devono prendere in considerazione e implementare tutte le best practice** e, nel caso di piattaforme come WordPress, tenere sempre aggiornati i componenti.

![errori sicurezza](https://www.securityinfo.it/wp-content/uploads/2023/03/website-hosting-concept-with-search-bar-1.jpg)

Freepik

Molti sviluppatori utilizzano dei **tool automatizzati per scansionare i siti web** e individuare vulnerabilità, ma nella maggior parte dei casi si rivelano inefficaci. Questi strumenti **individuano solo le vulnerabilità più immediate, generano spesso falsi positivi e non sono in grado di fornire delle analisi dettagliate.** Pur essendo un buon aiuto per una scansione superficiale del sito web, da soli non bastano: vanno sempre integrati test manuali più approfonditi.

Un altro errore comune commesso dagli sviluppatori è **sviluppare un proprio sistema di autenticazione e credere che sia sicuro.** Spesso si fanno errori durante l’implementazione dei protocolli, col risultato che gli attaccanti possono accedere alle informazioni sensibili degli utenti. È sempre meglio integrare un sistema già testato e allineato agli standard di sicurezza.

A volte **le stesse funzionalità di business sono vulnerabili per loro natura.** L’esempio di Merritt riguarda il carrello nei siti di e-commerce: si tratta di una feature di alto valore per gli utenti, ma esposta a pericoli come la modifica dei prodotti in carrello o del prezzo totale**. Spesso le feature ad alto valore non vengono analizzate con occhio abbastanza critico.**

![errori sicurezza](https://www.securityinfo.it/wp-content/uploads/2023/03/marketing-creative-collage-with-phone.jpg)

Freepik

Infine, **gli sviluppatori tendono a considerare le componenti di un sito web come parti separate**, mentre è importante pensarle come un unico ecosistema. Alcune risorse vengono considerate “out-of-scope” rispetto ai propri sviluppi e di conseguenza ignorate quando si implementano misure di sicurezza; ciò può portare alla nascita di vulnerabilità anche gravi.

I business manager per primi dovrebbero comprendere i rischi di sicurezza delle applicazioni web e investire su una **maggiore collaborazione tra sviluppatori e team di penetration tester**. I developer, in questo modo, possono allineare il proprio codice agli standard di sicurezza, senza ricadere in errori o dover ripensare i processi al termine degli sviluppi.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [applicazioni web](https://www.securityinfo.it/tag/applicazioni-web/), [cross-site scripting](https://www.securityinfo.it/tag/cross-site-scripting/), [developer](https://www.securityinfo.it/tag/developer/), [penetration testing](https://www.securityinfo.it/tag/penetration-testing/), [sviluppo web](https://www.securityinfo.it/tag/sviluppo-web/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/), [XSS](https://www.securityinfo.it/tag/xss/)

[Dispositivi SonicWall colpiti da un malware che resiste agli update del firmware](https://www.securityinfo.it/2023/03/16/dispositivi-sonicwall-malware-firmware/)
[Lo scorso anno sono stati divulgati 10 milioni di segreti su GitHub](https://www.securityinfo.it/2023/03/14/lo-scorso-anno-sono-stati-divulgati-10-milioni-di-segreti-su-github/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_d4x8rid4x8rid4x8-120x85.png)](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  [Firewall Cisco sotto attacco: una nuova...](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Permane...