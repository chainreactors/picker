---
title: Scoperto un RAT per Windows che corrompe gli header DOS e PE per l’elusione
url: https://www.securityinfo.it/2025/05/30/scoperto-un-rat-per-windows-che-corrompe-gli-header-dos-e-pe-per-lelusione/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-31
fetch_date: 2025-10-06T22:27:52.054290
---

# Scoperto un RAT per Windows che corrompe gli header DOS e PE per l’elusione

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

## Scoperto un RAT per Windows che corrompe gli header DOS e PE per l’elusione

Mag 30, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Malware](https://www.securityinfo.it/category/news/malware-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/05/30/scoperto-un-rat-per-windows-che-corrompe-gli-header-dos-e-pe-per-lelusione/#respond)

---

I ricercatori di Fortinet [hanno individuato](https://www.fortinet.com/blog/threat-research/deep-dive-into-a-dumped-malware-without-a-pe-header) un nuovo **RAT per Windows** che corrompe gli header DOS e PE per **rimanere nel sistema senza essere individuato.**

Il malware è riuscito a eludere i controlli per settimane prima di essere scoperto. Per fare ciò, **il RAT ha corrotto gli header PE (Portable Executable) e DOS**, intestazioni che contengono le informazioni fondamentali per il caricamento e l’esecuzione di un eseguibile su Windows.

Compromettere queste regione di intestazione significa complicare il lavoro di analisi dei ricercatori e quindi rallentare la risposta all’attacco. Nel caso scoperto da Fortinet, il malware **ha sovrascritto i due header con zeri o dati casuali**, rendendo più difficile il processo di rilevamento.

![Credits: Fortinet](https://www.securityinfo.it/wp-content/uploads/2025/05/fig02-dumped-malware-no-pe-header.png)

Credits: Fortinet

Gli header corrotti hanno complicato l’attività di ricostruzione del malware, ma alla fine i ricercatori di Fortinet sono riusciti a recuperare un dump del malware in memoria e replicarne l’operatività in un ambiente controllato.

Dopo la prima esecuzione, il malware chiama una funzione per decrittare le informazioni del server C2 e cominciare la comunicazione con gli attaccanti tremite protocollo TLS. Per migliorare il livello di elusione, i messaggi vengono cifrati. Il malware implementa un’**architettura socket multi-thread** che gli consente di gestire più comunicazioni contemporaneamente e quindi eseguire attività complesse: ogni volta che un nuovo client (dell’attaccante) tenta di comunicare col RAT, esso crea un nuovo thread dedicato per gestire i messaggi in arrivo.

Oltre a **esfiltrare dati**, come screenshot e i programmi in esecuzione, il RAT è anche in grado di ricevere nuovi comandi dagli attaccanti per **distribuire altri malware** ed enumerare e manipolare i servizi di sistema sfruttando le API di Service Control Manager di Windows.

Come riportato da [The Hacker News](https://thehackernews.com/2025/05/new-windows-rat-evades-detection-for.html), in una comunicazione contestuale alla pubblicazione dell’analisi Fortinet ha affermato di aver rilevato **attività ransomware legata al RAT**. La minaccia è stata neutralizzata prima che venisse eseguito il ransomware.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [elusione](https://www.securityinfo.it/tag/elusione/), [fortinet](https://www.securityinfo.it/tag/fortinet/), [header DOS](https://www.securityinfo.it/tag/header-dos/), [header PE](https://www.securityinfo.it/tag/header-pe/), [RAT](https://www.securityinfo.it/tag/rat/), [Windows](https://www.securityinfo.it/tag/windows/)

[La gang di DragonForce ha sfruttato SimpleHelp per distribuire un ransomware](https://www.securityinfo.it/2025/05/30/la-gang-di-dragonforce-ha-sfruttato-simplehelp-per-distribuire-il-ransomware/)
[Check Point acquisisce Veriti e la sua tecnologia di Preemptive Exposure Management](https://www.securityinfo.it/2025/05/28/check-point-acquisisce-veriti-e-la-sua-tecnologia-di-preemptive-exposure-management/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Campagne basate su installer ScreenConnect distribuiscono RAT multipli](https://www.securityinfo.it/wp-content/uploads/2025/09/ai-generated-8976964_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/09/22/campagne-basate-su-installer-screenconnect-distribuiscono-rat-multipli-lanalisi-di-acronis-tru/ "Campagne basate su installer ScreenConnect distribuiscono RAT multipli")

  [Campagne basate su installer...](https://www.securityinfo.it/2025/09/22/campagne-basate-su-installer-screenconnect-distribuiscono-rat-multipli-lanalisi-di-acronis-tru/ "Permanent link to Campagne basate su installer ScreenConnect distribuiscono RAT multipli")

  Set 22, 2025  [0](https://www.securityinfo.it/2025/09/22/campagne-basate-su-installer-screenconnect-distribuiscono-rat-multipli-lanalisi-di-acronis-tru/#respond)
* [![Ondata di attacchi brute-force contro le VPN Fortinet, poi FortiManager](https://www.securityinfo.it/wp-content/uploads/2025/08/FortinetVPN13-ago-2025CG-120x85.png)](https://www.securityinfo.it/2025/08/12/ondata-di-attacchi-brute-force-contro-le-vpn-fortinet-poi-fortimanager/ "Ondata di attacchi brute-force contro le VPN Fortinet, poi FortiManager")

  [Ondata di attacchi brute-force contro...](https://www.securityinfo.it/2025/08/12/ondata-di-attacchi-brute-force-contro-le-vpn-fortinet-poi-fortimanager/ "Permanent link to Ondata di attacchi brute-force contro le VPN Fortinet, poi FortiManager")

  Ago 12, 2025  [0](https://www.securityinfo.it/2025/08/12/ondata-di-attacchi-brute-force-contro-le-vpn-fortinet-poi-fortimanager/#respond)
* [![Malware dentro il malware: trovate backdoor nel RAT Sakura](https://www.securityinfo.it/wp-content/uploads/2025/06/security-7057561_1920-120x85.jpg)](https://www.securityinfo.it/2025/06/04/malware-dentro-il-malware-trovate-backdoor-nel-rat-sakura/ "Malware dentro il malware...