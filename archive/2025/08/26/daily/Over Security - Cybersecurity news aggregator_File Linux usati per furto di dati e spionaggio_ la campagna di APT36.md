---
title: File Linux usati per furto di dati e spionaggio: la campagna di APT36
url: https://www.securityinfo.it/2025/08/25/file-linux-usati-per-furto-di-dati-e-spionaggio-la-campagna-di-apt36/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-26
fetch_date: 2025-10-07T00:49:53.279089
---

# File Linux usati per furto di dati e spionaggio: la campagna di APT36

Aggiornamenti recenti Ottobre 6th, 2025 5:03 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Impennata delle scansioni dei portali di login di Palo Alto Networks: +500%](https://www.securityinfo.it/2025/10/06/impennata-delle-scansioni-dei-portali-di-login-di-palo-alto-networks-500/)
* [Microsoft Sentinel: arriva l’era degli agenti AI e della difesa predittiva](https://www.securityinfo.it/2025/10/06/microsoft-sentinel-arriva-lera-degli-agenti-ai-e-della-difesa-predittiva/)
* [CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)

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

## File Linux usati per furto di dati e spionaggio: la campagna di APT36

Ago 25, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Malware](https://www.securityinfo.it/category/news/malware-news/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/08/25/file-linux-usati-per-furto-di-dati-e-spionaggio-la-campagna-di-apt36/#respond)

---

Il gruppo pakistano **APT36**, noto anche come Transparent Tribe, ha usato **file Linux .desktop per distribuire malware**  **ne****i sistemi BOSS** in una campagna di spionaggio ai danni di realtà governative e del settore della difesa in India.

Secondo il [report](https://www.cyfirma.com/research/apt36-targets-indian-boss-linux-systems-with-weaponized-autostart-files/) di Cyfirma, APT36 ha sfruttato numerose **email di spear-phishing** per distribuire un file .zip, il quale a sua volta contiene un **file .desktop di Linux**. All’apparenza il file si presenta come una shortcut per PDF, ma contiene una serie di comandi che vengono eseguiti non appena viene aperto, tra i quali anche quelli per scaricare il payload malevolo e installare il malware.

Contemporaneamente, per sviare i sospetti, viene eseguito Firefox in background e viene aperto un link Google Drive che contiene un PDF innocuo, così da convincere l’utente che ha effettivamente aperto un documento.

Dopo aver stabilito un canale di comunicazione con il server degli attaccanti, il malware comincia a raccogliere informazioni sensibili dal dispositivo della vittima per inviarle al server C2.

![Linux APT36](https://www.securityinfo.it/wp-content/uploads/2025/08/cyber-security-4785679_1920.png)

Secondo Cyfirma, la campagna sarebbe cominciata il 1° agosto scorso ed è ancora in esecuzione. APT36 è **attivo da oltre 10 anni**e a partire dal 2016 ha affinato le proprie tattiche per eseguire campagne sempre più sofisticate.

Il gruppo, affiliato al governo pakistano, **ha sempre preso di mira realtà indiane**, in particolare nei settori governativo e militare e anche le istituzioni diplomatiche. In alcuni casi le attività della gang si sono estese anche ai settori dell’istruzione, della difesa e delle infrastrutture critiche.

Negli ultimi anni il gruppo ha preso di mira vittime anche in altri Paesi, in maniera per lo più opportunistica, mettendo a rischio partner e fornitori delle realtà colpite.

“L*‘adozione di payload .desktop mirati a Linux BOSS riflette un cambiamento tattico verso lo **sfruttamento delle tecnologie native**. In combinazione con il malware tradizionale basato su Windows e i dispositivi mobile, ciò dimostra l’intenzione del gruppo di diversificare i vettori di accesso e garantire la persistenza anche in ambienti protetti*” hanno affermato i ricercatori di Cyfirma.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [APT36](https://www.securityinfo.it/tag/apt36/), [cyberspionaggio](https://www.securityinfo.it/tag/cyberspionaggio/), [Linux](https://www.securityinfo.it/tag/linux/), [Linux BOSS](https://www.securityinfo.it/tag/linux-boss/), [malware](https://www.securityinfo.it/tag/malware/), [Spear Phishing](https://www.securityinfo.it/tag/spear-phishing/)

[IoT, i dispositivi connessi sono ancora troppo esposti alle minacce: l'allarme di ACN](https://www.securityinfo.it/2025/08/26/iot-i-dispositivi-connessi-sono-ancora-troppo-esposti-alle-minacce-lallarme-di-acn/)
[CERT-AGID 16-22 agosto: registrato il primo abuso di Action1](https://www.securityinfo.it/2025/08/25/cert-agid-16-22-agosto-primo-abuso-action1/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  [MuddyWater si evolve: attacchi più...](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "Permanent link to MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  Set 17, 2025  [0](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/#respond)
* [![Gli U.S.A. offrono 10 milioni di dollari per tre cybercriminali russi](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_30q7yk30q7yk30q7-120x85.png)](https://www.securityinfo.it/2025/09/05/gli-u-s-a-offrono-10-milioni-di-dollari-per-tre-cybercriminali-russi/ "Gli U.S.A. offrono 10 milioni di dollari per tre cybercriminali russi")

  [Gli U.S.A. offrono 10 milioni di...](https://www.securityinfo.it/2025/09/05/gli-u-s-a-offrono-10-milioni-di-dollari-per-tre-cybercriminali-russi/ "Permanent link to Gli U.S.A. offrono 10 milioni di dollari per tre cybercriminali russi")

  Set 05, 2025  [0](https://www.securityinfo.it/2025/09/05/gli-u-s-a-offrono-10-milioni-di-dollari-per-tre-cybercriminali-russi/#respond)
* [![Spionaggio industriale: i gruppi cinesi puntano ai chip di Taiwan](https://www.securityinfo.it/wp-content/uploads/2025/07/Cina_Taiwan-2025-CG-120x85.png)](https://www.securityinfo.it/2025/07/29/spionaggio-industriale-i-gruppi-cinesi-puntano-ai-chip-di-taiwan/ "Spionaggio indus...