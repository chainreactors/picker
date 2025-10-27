---
title: Una vecchia vulnerabilità nelle telecamere AVTECH è stata sfruttata per attacchi botnet
url: https://www.securityinfo.it/2024/09/04/avtech-vulnerabilita-telecamere-attacchi-botnet/?utm_source=rss&utm_medium=rss&utm_campaign=avtech-vulnerabilita-telecamere-attacchi-botnet
source: Securityinfo.it
date: 2024-09-05
fetch_date: 2025-10-06T18:27:46.250719
---

# Una vecchia vulnerabilità nelle telecamere AVTECH è stata sfruttata per attacchi botnet

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

## Una vecchia vulnerabilità nelle telecamere AVTECH è stata sfruttata per attacchi botnet

Set 04, 2024  [Stefano Silvestri](https://www.securityinfo.it/author/stefano-silvestri/ "Articoli scritti da Stefano Silvestri")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [Hacking](https://www.securityinfo.it/category/news/hacking-news/), [Intrusione](https://www.securityinfo.it/category/news/intrusione/), [News](https://www.securityinfo.it/category/news/), [Tecnologia](https://www.securityinfo.it/category/news/tecnologia-news/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2024/09/04/avtech-vulnerabilita-telecamere-attacchi-botnet/#respond)

---

Una grave vulnerabilità che affligge da anni le telecamere IP di **AVTECH** è stata recentemente sfruttata da degli hacker per trasformare questi dispositivi in parte di una **botnet**, un network di dispositivi compromessi utilizzato per scopi malevoli.

La vulnerabilità, identificata come CVE-2024-7029 con un **punteggio di gravità di 8,7 su 10**, è stata descritta dai ricercatori di Akamai come un **difetto nella funzione di regolazione della luminosità** delle telecamere a circuito chiuso (CCTV) AVTECH. Questo difetto permette l’**esecuzione di codice da remoto**, consentendo agli attaccanti di prendere il controllo delle telecamere.

La Cybersecurity and Infrastructure Security Agency (CISA) degli Stati Uniti ha reso pubblici i dettagli di questa falla di sicurezza **all’inizio di agosto 2024**, sottolineando la facilità con cui può essere sfruttata da remoto. Nonostante ciò, la vulnerabilità rimane **ancora senza una patch correttiva**, lasciando esposti migliaia di dispositivi, molti dei quali sono ancora utilizzati in settori critici come il commercio, i servizi finanziari, la sanità e i sistemi di trasporto.

Secondo Akamai, questa campagna di attacco è **in corso da marzo 2024**, anche se la vulnerabilità era nota e sfruttabile già dal 2019. Il fatto che **solo ora sia stato assegnato un identificativo CVE**, ossia un codice univoco utilizzato per identificare pubblicamente le vulnerabilità di sicurezza informatica, solleva preoccupazioni sulla rapidità con cui vengono riconosciute e affrontate queste falle.

![](https://www.securityinfo.it/wp-content/uploads/2024/09/AVTECH-1024x576.jpg)

Gli attaccanti hanno sfruttato la vulnerabilità delle telecamere AVTECH per diffondere una variante del botnet Mirai.

La tecnica utilizzata dagli attaccanti è relativamente semplice: sfruttano la vulnerabilità delle telecamere AVTECH insieme ad altre falle di sicurezza note per **diffondere una variante del botnet Mirai**.

Questo botnet, denominato “Corona Mirai” in riferimento alla pandemia di COVID-19, **si connette a un gran numero di host tramite Telnet**, un protocollo che permette la connessione remota a server, utilizzando porte specifiche. Una volta infettati i dispositivi, il malware mostra la stringa “Corona” sulla console, un segnale distintivo dell’infezione.

Questa notizia arriva poco dopo la scoperta di un **altro botnet, chiamato 7777 o Quad7**, che ha compromesso router TP-Link e ASUS per condurre attacchi di tipo “password spraying” contro account Microsoft 365. Secondo i ricercatori, questo botnet utilizza dispositivi compromessi per effettuare **attacchi di forza bruta estremamente lenti**, con una rete di oltre 12.000 bot attivi.

Il botnet 7777 prende il nome dalla porta TCP 7777, che viene aperta sui dispositivi compromessi. Tuttavia, recenti indagini suggeriscono che **un secondo gruppo di bot**, che utilizza principalmente router ASUS e la porta 63256, potrebbe essere emerso come parte di una nuova espansione del botnet.

Il team di ricerca di Team Cymru ha avvertito che il botnet Quad7 rappresenta una minaccia importante, dimostrando una notevole capacità di adattamento e resilienza. La connessione tra i botnet 7777 e 63256, pur mantenendo operazioni apparentemente separate, evidenzia l’evoluzione continua delle tattiche degli operatori di queste minacce.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [AVTech](https://www.securityinfo.it/tag/avtech/), [botnet](https://www.securityinfo.it/tag/botnet/)

[Da Trend Micro nuove funzionalità per contrastare i deepfake](https://www.securityinfo.it/2024/09/04/da-trend-micro-nuove-funzionalita-per-contrastare-i-deepfake/)
[Gli italiani si preoccupano dell'eredità digitale dei defunti](https://www.securityinfo.it/2024/09/03/gli-italiani-si-preoccupano-delleredita-digitale-dei-defunti/)

---

![](https://secure.gravatar.com/avatar/d290cb647e218511e0408135528fb5f2?s=90&d=mm&r=g)

##### [Stefano Silvestri](https://www.securityinfo.it/author/stefano-silvestri/)

##### Articoli correlati

* [![Attacchi DDoS ipervolumetrici, ancora numeri da record nonostante il calo](https://www.securityinfo.it/wp-content/uploads/2025/07/Gemini_Generated_Image_ij19w5ij19w5ij19-120x85.png)](https://www.securityinfo.it/2025/07/17/attacchi-ddos-ipervolumetrici-ancora-numeri-da-record-nonostante-il-calo/ "Attacchi DDoS ipervolumetrici, ancora numeri da record nonostante il calo")

  [Attacchi DDoS ipervolumetrici, ancora...](https://www.securityinfo.it/2025/07/17/attacchi-ddos-ipervolumetrici-ancora-numeri-da-record-nonostante-il-calo/ "Permanent link to Attacchi DDoS ipervolumetrici, ancora numeri da record nonostante il calo")

  Lug 17, 2025  [0](https://www.securityinfo.it/2025/07/17/attacchi-ddos-ipervolumetrici-ancora-numeri-da-record-nonostante-il-calo/#respond)
* [![Torna l’incubo BADBOX 2.0: infettati oltre un milione di dispositivi](https://www.securityinfo.it/wp-content/uploads/2025/06/Gemini_Generated_Image_8go7448go7448go7-scaled-120x85.jpg)](https://www.securityinfo.it/2025/06/06/torna-lincubo-badbox-2-0-infettati-oltre-un-milione-di-dispositivi/ "Torn...