---
title: XorDDoS, il DDoS contro Linux evolve e continua a mietere vittime
url: https://www.securityinfo.it/2025/04/18/xorddos-il-ddos-contro-linux-continua-a-mietere-vittime/?utm_source=rss&utm_medium=rss&utm_campaign=xorddos-il-ddos-contro-linux-continua-a-mietere-vittime
source: Securityinfo.it
date: 2025-04-19
fetch_date: 2025-10-06T22:07:32.213110
---

# XorDDoS, il DDoS contro Linux evolve e continua a mietere vittime

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

## XorDDoS, il DDoS contro Linux evolve e continua a mietere vittime

Apr 18, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Attacchi](https://www.securityinfo.it/category/approfondimenti/attacchi/), [Attacchi](https://www.securityinfo.it/category/news/attachi/), [Campagne malware](https://www.securityinfo.it/category/approfondimenti/campagne-malware/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Malware](https://www.securityinfo.it/category/news/malware-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/04/18/xorddos-il-ddos-contro-linux-continua-a-mietere-vittime/#respond)

---

I ricercatori di Cisco Talos [hanno pubblicato](https://blog.talosintelligence.com/unmasking-the-new-xorddos-controller-and-infrastructure/) una nuova analisi su **XorDDoS**, un malware DDoS attivo dal 2014 e che ha continuato a mietere vittime in tutto il mondo e lo fa ancora oggi.

XorDDoS è un trojan che colpisce le **macchine Linux** per renderle parte di una **botnet** e sfruttarle per eseguire altri attacchi. Il malware, attivo tutt’oggi, è cresciuto notevolmente negli ultimi anni, soprattutto tra il 2020 e il 2023. Nel tempo il malware si è esteso a livello globale, cominciando a colpire anche i server Docker sfruttando **attacchi brute force SSH** per ottenere accesso remoto ai dispositivi.

![XorDDoS](https://www.securityinfo.it/wp-content/uploads/2025/04/8289982_25332-scaled.jpg)

white digital matrix of binary code numbers background

Una volta preso il controllo della macchina, il malware implementa dei **meccanismi di persistenza** per fare in modo che venga eseguito durante il boot del sistema e non venga individuato dai sistemi di sicurezza.

Nel 2024 i ricercatori di Cisco Talos hanno individuato nuove versioni dell’infrastruttura e del payload del malware, probabilmente già in uso dal 2017. Secondo il team di sicurezza, questa nuova suite di prodotti non è stata realizzata solo per migliorare gli attacchi, ma anche per essere **messa in vendita.**

Oggi l’infrastruttura di XorDDoS include anche un “central controller” in grado gestire più controller del malware contemporaneamente. “*Questo controller aggiornato **migliora la capacità dei cybercriminali di coordinare ed eseguire gli attacchi in maniera più efficiente**, a indicare un’evoluzione nelle loro tattiche e nelle loro conoscenze*” hanno spiegato i ricercatori di Cisco Talos.

![XorDDoS](https://www.securityinfo.it/wp-content/uploads/2025/04/XorDDoS-05.jpg)

Credits: Cisco Talos

Il controller invia comandi a ciascuno dei sotto-controller, i quali, a loro volta, gestiscono le botnet di macchine Linux create tramite il malware.

Secondo i ricercatori di sicurezza, i cyberattaccanti dietro XorDDoS sono di origine cinese. Il team di Cisco Talos riporta che tra novembre 2023 e febbraio 2025 il malware **ha colpito per lo più negli Stati Uniti**, nei quali si conta il 50% delle vittime totali. A seguire, i Paesi più colpiti risultano Spagna, Taiwan, Canada, Giappone, Brasile, Paraguay, Argentina, Regno Unito e, tra gli altri, anche l’Italia.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [botnet](https://www.securityinfo.it/tag/botnet/), [Cisco Talos](https://www.securityinfo.it/tag/cisco-talos/), [DDoS](https://www.securityinfo.it/tag/ddos/), [Linux](https://www.securityinfo.it/tag/linux/), [malware](https://www.securityinfo.it/tag/malware/), [XorDdos](https://www.securityinfo.it/tag/xorddos/)

[CERT-AGID 12 – 18 aprile: nuove campagne di phishing per pagoPA e Ministero della Salute](https://www.securityinfo.it/2025/04/21/cert-agid-12-18-aprile-campagne-phishing-pagopa-ministero-salute/)
[Migliaia di chiavi AWS usate in un attacco ransomware](https://www.securityinfo.it/2025/04/17/migliaia-di-chiavi-aws-usate-in-un-attacco-ransomware/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  [MuddyWater si evolve: attacchi più...](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "Permanent link to MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  Set 17, 2025  [0](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/#respond)
* [![File Linux usati per furto di dati e spionaggio: la campagna di APT36](https://www.securityinfo.it/wp-content/uploads/2025/08/cyber-security-4785679_1920-120x85.png)](https://www.securityinfo.it/2025/08/25/file-linux-usati-per-furto-di-dati-e-spionaggio-la-campagna-di-apt36/ "File Linux usati per furto di dati e spionaggio: la campagna di APT36")

  [File Linux usati per furto di dati e...](https://www.securityinfo.it/2025/08/25/file-linux-usati-per-furto-di-dati-e-spionaggio-la-campagna-di-apt36/ "Permanent link to File Linux usati per furto di dati e spionaggio: la campagna di APT36")

  Ago 25, 2025  [0](https://www.securityinfo.it/2025/08/25/file-linux-usati-per-furto-di-dati-e-spionaggio-la-campagna-di-apt36/#respond)
* [![Static Tundra sfrutta una vecchia vulnerabilità Cisco per spionaggio](https://www.securityinfo.i...