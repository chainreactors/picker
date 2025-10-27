---
title: I ransomware contro le appliance ESXi sfruttano il tunneling SSH per la persistenza
url: https://www.securityinfo.it/2025/01/28/i-ransomware-contro-le-appliance-esxi-sfruttano-il-tunneling-ssh-per-la-persistenza/
source: Over Security - Cybersecurity news aggregator
date: 2025-01-29
fetch_date: 2025-10-06T20:10:55.535896
---

# I ransomware contro le appliance ESXi sfruttano il tunneling SSH per la persistenza

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

## I ransomware contro le appliance ESXi sfruttano il tunneling SSH per la persistenza

Gen 28, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/01/28/i-ransomware-contro-le-appliance-esxi-sfruttano-il-tunneling-ssh-per-la-persistenza/#respond)

---

I ricercatori di Sygnia, compagnia di sicurezza, [hanno scoperto](https://www.sygnia.co/blog/esxi-ransomware-ssh-tunneling-defense-strategies/) che i **ransomware** che prendono di mira le **appliance ESXi** sfruttano il **tunneling SSH per mantenere persistenza** sul dispositivo e comunicare col server C2.

![ransomware ESXi](https://www.securityinfo.it/wp-content/uploads/2025/01/ransomware-2321110_1920.jpg)

Già da diversi anni le appliance ESXi sono diventate dei **target molto interessanti per gli attaccanti**: questi dispositivi hanno un ruolo critico nelle infrastrutture virtualizzate aziendali; quando compromessi, possono provocare l’interruzione dell’operatività con **gravi conseguenze** reputazionali ed economiche per le compagnie.

**“*Le appliance ESXi, le quali non sono monitorate, sono sempre più sfruttate come meccanismo di persistenza e gateway per accedere alle reti aziendali*“** affermano Zhongyuan Hau e Ren Jie Yow di Sygnia.

Negli attacchi analizzati dalla compagnia, la maggior parte delle appliance erano state compromesse o usando le credenziali di amministratore, oppure sfruttando una vulnerabilità nota. Una volta preso il controllo del dispositivo, gli attaccanti hanno creato il tunnel di comunicazione sfruttando **SSH** o altri tool analoghi già presenti sulla macchina.

Effettuare il setup del canale di comunicazione col server C2 è molto semplice: è sufficiente eseguire un **singolo comando** per stabilire una connessione stabile con il server degli attaccanti. La natura delle appliance ESXi consente inoltre di mantenere la comunicazione aperta a lungo: “*Poiché le appliance ESXi sono resilienti e raramente si spengono in modo inaspettato**, il tunneling funge da backdoor semi-persistente all’interno della rete***” sottolineano i ricercatori.

![ransomware ESXi](https://www.securityinfo.it/wp-content/uploads/2025/01/image-13.png)

Credits: Sygnia

A complicare la situazione c’è anche una certa **difficoltà nel monitorare i log di ESXi** per individuare eventuali attività pericolose, conseguenze di ransomware e altri malware. I ricercatori spiegano infatti che, a differenza di altri formati di logging, quello di ESXi non aggrega i log rilevanti per le attività forensi, ma li divide per specifiche attività, separandoli in file differenti.

In caso di attacco o attività sospette, le analisi dei team di sicurezza si complicano ed è necessario unire più fonti per rintracciare le informazioni rilevanti e ricostruire il flusso di eventi. Per risolvere questo problema si può **configurare l’inoltro dei file di lo**g più importanti a un server di analisi esterno che si occupa di individuare le informazioni più importanti.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [ESXi](https://www.securityinfo.it/tag/esxi/), [persistenza](https://www.securityinfo.it/tag/persistenza/), [Ransomware](https://www.securityinfo.it/tag/ransomware/), [server c2](https://www.securityinfo.it/tag/server-c2/), [SSH](https://www.securityinfo.it/tag/ssh/), [tunneling](https://www.securityinfo.it/tag/tunneling/)

[PlushDaemon: un nuovo gruppo APT cinese colpisce la Corea del Sud. Il report di ESET](https://www.securityinfo.it/2025/01/29/plushdaemon-un-nuovo-gruppo-apt-cinese-colpisce-la-corea-del-sud-il-report-di-eset/)
[Le implementazioni LTE e 5G soffrono di centinaia di vulnerabilità](https://www.securityinfo.it/2025/01/27/le-implementazioni-lte-e-5g-soffrono-di-centinaia-di-vulnerabilita/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/wp-content/uploads/2025/10/Gemini_Generated_Image_t7m3xlt7m3xlt7m3-120x85.png)](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/ "RedHat vittima di un breach: sottratti oltre 500 GB di dati")

  [RedHat vittima di un breach: sottratti...](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/ "Permanent link to RedHat vittima di un breach: sottratti oltre 500 GB di dati")

  Ott 03, 2025  [0](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/#respond)
* [![Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-6138007_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/ "Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA")

  [Report Acronis: il ransomware rimane la...](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/ "Permanent link to Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA")

  Set 11, 2025  [0](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-...