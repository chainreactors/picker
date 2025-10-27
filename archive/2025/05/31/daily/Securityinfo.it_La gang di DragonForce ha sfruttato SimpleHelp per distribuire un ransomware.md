---
title: La gang di DragonForce ha sfruttato SimpleHelp per distribuire un ransomware
url: https://www.securityinfo.it/2025/05/30/la-gang-di-dragonforce-ha-sfruttato-simplehelp-per-distribuire-il-ransomware/?utm_source=rss&utm_medium=rss&utm_campaign=la-gang-di-dragonforce-ha-sfruttato-simplehelp-per-distribuire-il-ransomware
source: Securityinfo.it
date: 2025-05-31
fetch_date: 2025-10-06T22:28:33.239637
---

# La gang di DragonForce ha sfruttato SimpleHelp per distribuire un ransomware

Aggiornamenti recenti Ottobre 6th, 2025 3:00 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Microsoft Sentinel: arriva l’era degli agenti AI e della difesa predittiva](https://www.securityinfo.it/2025/10/06/microsoft-sentinel-arriva-lera-degli-agenti-ai-e-della-difesa-predittiva/)
* [CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)
* [Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)

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

## La gang di DragonForce ha sfruttato SimpleHelp per distribuire un ransomware

Mag 30, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [Malware](https://www.securityinfo.it/category/news/malware-news/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/05/30/la-gang-di-dragonforce-ha-sfruttato-simplehelp-per-distribuire-il-ransomware/#respond)

---

Di recente la gang dietro il ransomware **DragonForce** ha sfruttato **SimpleHelp**, un tool per l’accesso remoto usato dagli MSP, per **distribuire un malware su numerosi endpoint.**

A individuare l’attacco sono stati i ricercatori di [Sophos](https://news.sophos.com/en-us/2025/05/27/dragonforce-actors-target-simplehelp-vulnerabilities-to-attack-msp-customers/), dopo aver ricevuto un alert riguardo un’installer sospetto di SimpleHelp. **Il file era stato inviato tramite un’istanza legittima del software gestita da un MSP**. Gli attaccanti hanno usato questo canale di accesso non solo per distribuire il ransomware, ma anche per raccogliere informazioni sui clienti dell’MSP, come i nomi dei dispositivi usati, le configurazioni, gli utenti attivi e le connessioni di rete.

![DragonForce](https://www.securityinfo.it/wp-content/uploads/2025/05/hacker-6138007_1920.jpg)

Uno dei clienti dell’MSP aveva installati Sophos MDR e Sophos XDR Endpoint; per questo la compagnia di sicurezza ha ricevuto l’alert ed è riuscita a bloccare ulteriormente la diffusione del ransomware. Coloro però che non che avevano queste installazioni sono stati colpiti da DragonForce. Il gruppo, oltre a esfiltrare dati, ha usato il meccanismo della **doppia estorsione** per mettere ancora più pressione alle vittime.

Secondo i ricercatori di Sophos, **il gruppo ha usato tre vulnerabilità di SimpleHelp per ottenere l’accesso agli endpoint**: la CVE-2024-57727, un bug di multiple path traversal; la CVE-2024-57728, una vulnerabilità di arbitrary file upload; infine, la CVE-2024-57726, un bug che consente l’escalation dei privilegi. Tutte e tre le vulnerabilità erano state rese note e patchate a gennaio.

Attivo dal 2023, DragonForce ha guadagnato popolarità negli ultimi mesi dopo aver [modificato il proprio modello di affiliazione](https://news.sophos.com/en-us/2025/05/21/dragonforce-targets-rivals-in-a-play-for-dominance/), rendendolo più flessibile: gli affiliati possono infatti creare delle proprie versioni del ransomware partendo dal codice sorgente, cambiandogli anche nome. Contestualmente, per affermarsi sul mercato, la gang dietro il ransomware ha cominciato una serie di **attività di *defacement* dei siti dei leak gestiti da gruppi molto noti**, quali BlackLock e Mamona.

Di recente il gruppo ha inoltre rivendicato due attacchi che hanno colpito dei rivenditori del Regno Unito. Secondo il team di Sophos, è molto probabile che il noto gruppo Scattered Spiders (GOLD HARVEST) abbia collaborato a stretto contatto con la gang di DragonForce nei suoi ultimi attacchi, compreso quello contro [M&S](https://www.securityinfo.it/2025/05/23/ms-perde-un-terzo-dei-profitti-a-causa-di-un-attacco-informatico/).

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [accesso remoto](https://www.securityinfo.it/tag/accesso-remoto/), [doppia estorsione](https://www.securityinfo.it/tag/doppia-estorsione/), [DragonForce](https://www.securityinfo.it/tag/dragonforce/), [MSP](https://www.securityinfo.it/tag/msp/), [Ransomware](https://www.securityinfo.it/tag/ransomware/), [SimpleHelp](https://www.securityinfo.it/tag/simplehelp/)

[Sophos Annual Threat Report: i malware e gli strumenti più abusati del 2024](https://www.securityinfo.it/2025/05/30/sophos-annual-threat-report-i-malware-e-gli-strumenti-piu-abusati-del-2024/)
[Scoperto un RAT per Windows che corrompe gli header DOS e PE per l'elusione](https://www.securityinfo.it/2025/05/30/scoperto-un-rat-per-windows-che-corrompe-gli-header-dos-e-pe-per-lelusione/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/wp-content/uploads/2025/10/Gemini_Generated_Image_t7m3xlt7m3xlt7m3-120x85.png)](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/ "RedHat vittima di un breach: sottratti oltre 500 GB di dati")

  [RedHat vittima di un breach: sottratti...](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/ "Permanent link to RedHat vittima di un breach: sottratti oltre 500 GB di dati")

  Ott 03, 2025  [0](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/#respond)
* [![Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-6138007_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/ "Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA")

  [Report Acronis: il ransomware rimane la...](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/ "Permanent link to Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA")

  Set 11, 2025  [0](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware...