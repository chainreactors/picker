---
title: Kaspersky svela un Apt attivo nell’area del conflitto russo-ucraino
url: https://www.securityinfo.it/2023/03/22/kaspersky-svela-un-apt-attivo-nellarea-del-conflitto-russo-ucraino/?utm_source=rss&utm_medium=rss&utm_campaign=kaspersky-svela-un-apt-attivo-nellarea-del-conflitto-russo-ucraino
source: Securityinfo.it
date: 2023-03-23
fetch_date: 2025-10-04T10:25:08.074771
---

# Kaspersky svela un Apt attivo nell’area del conflitto russo-ucraino

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

## Kaspersky svela un Apt attivo nell’area del conflitto russo-ucraino

Mar 22, 2023  [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/ "Articoli scritti da Dario Orlandi")
 [Apt](https://www.securityinfo.it/category/minacce-2/apt/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/minacce-2/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2023/03/22/kaspersky-svela-un-apt-attivo-nellarea-del-conflitto-russo-ucraino/#respond)

---

Nell’ottobre dello scorso anno i ricercatori di [Kaspersky](https://www.kaspersky.com/) hanno [rilevato **una campagna di Advanced**](https://securelist.com/bad-magic-apt/109087/) **Persistent Threat (APT) che ha denominato Bad Magic,** destinata a organizzazioni situate nell’area di conflitto tra Russia e Ucraina.

La campagna utilizza **una backdoor basata su PowerShell** chiamata PowerMagic e un nuovo framework dannoso chiamato CommonMagic per rubare file dai dispositivi USB e raccogliere dati dai suoi obiettivi, tra cui aziende del settore amministrativo, agricolo e dei trasporti.

I ricercatori hanno suggerito che gli attacchi sono probabilmente iniziati tramite spearphishing o metodi simili: gli obiettivi sono stati indirizzati a un Url contenente un archivio Zip con un file dannoso che installava PowerMagic **insieme a un documento decoy** per indurre le vittime a credere che il contenuto fosse legittimo.

![](https://www.securityinfo.it/wp-content/uploads/2023/03/CommonMagic_backdoor_02.png)

Un documento decoy che portava l’infezione (Fonte: Kaspersky)

La backdoor PowerMagic riceve i comandi **da una cartella remota situata su un servizio di archiviazione cloud pubblico** e si installa nel sistema per essere lanciata in modo persistente all’avvio del dispositivo infetto.

Kaspersky ha **scoperto una serie di archivi di questo tipo** con denominazioni che fanno riferimento a vari decreti di organizzazioni rilevanti per le regioni.

## Un payload modulare

Tutti gli sistemi compromessi tramite PowerMagic sono stati anche **infettati dal framework modulare CommonMagic**, composto da diversi moduli che comunicano tra loro. Il framework è in grado di rubare file dai dispositivi USB e catturare screenshot ogni tre secondi per inviarli all’attaccante.

**Non ci sono collegamenti diretti tra il codice e i dati utilizzati in questa campagna e altri già noti**, ma ulteriori ricerche potrebbero aiutare ad attribuire questa campagna a uno specifico attore di minacce.

La tipologia delle vittime e il tema degli attacchi suggeriscono che gli attaccanti hanno un **interesse specifico per la situazione geopolitica nella regione** della crisi.

![](https://www.securityinfo.it/wp-content/uploads/2023/03/Leonid_Bezvershenko_securelist_2023-transformed.jpeg)

Leonid Bezvershenko, Security Researcher di Kaspersky

Leonid Bezvershenko, Security Researcher di Kaspersky’s Global Research and Analysis Team (GReAT), ha commentato: “**La situazione geopolitica influenza sempre il panorama delle minacce** informatiche e porta all’emergere di nuove sfide”.

“Sebbene il malware e le tecniche impiegate nella campagna CommonMagic non siano particolarmente sofisticate, **l’uso del cloud storage come infrastruttura di comando e controllo è degno di nota**”, ha concluso Bezvershenko.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [APT](https://www.securityinfo.it/tag/apt/), [Bad Magic](https://www.securityinfo.it/tag/bad-magic/), [cloud storage](https://www.securityinfo.it/tag/cloud-storage/), [CommonMagic](https://www.securityinfo.it/tag/commonmagic/), [guerra russia ucraina](https://www.securityinfo.it/tag/guerra-russia-ucraina/), [Kaspersky](https://www.securityinfo.it/tag/kaspersky/), [PowerMagic](https://www.securityinfo.it/tag/powermagic/), [russia](https://www.securityinfo.it/tag/russia/), [spearphishing](https://www.securityinfo.it/tag/spearphishing/), [Ucraina](https://www.securityinfo.it/tag/ucraina/)

[Un nuovo Fraud Prevention Center per Poste Italiane](https://www.securityinfo.it/2023/03/23/un-nuovo-fraud-prevention-center-per-poste-italiane/)
[Google scopre 18 vulnerabilità nei chipset mobile Samsung Exynos](https://www.securityinfo.it/2023/03/22/google-scopre-18-vulnerabilita-nei-chipset-mobile-samsung-exynos/)

---

![](https://secure.gravatar.com/avatar/9ba6108fae91c2be66a7ef45ac2db49a?s=90&d=mm&r=g)

##### [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/)

##### Articoli correlati

* [![MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  [MuddyWater si evolve: attacchi più...](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "Permanent link to MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  Set 17, 2025  [0](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/#respond)
* [![Gli U.S.A. offrono 10 milioni di dollari per tre cybercriminali russi](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_30q7yk30q7yk30q7-120x85.png)](https://www.securityinfo.it/2025/09/05/gli-u-s-a-offrono-10-milioni-di-dollari-per-tre-cybercriminali-russi/ "Gli U.S.A. offrono 10 milioni di dollari per tre cybercriminali russi")

  [Gli U.S.A. offrono 10 milioni di...](https://www.securityinfo.it/2025/09/05/gli-u-s-a-offrono-10-milioni-di-dollari-per-tre-cybercriminali-russi/ "Permanent link to Gli...