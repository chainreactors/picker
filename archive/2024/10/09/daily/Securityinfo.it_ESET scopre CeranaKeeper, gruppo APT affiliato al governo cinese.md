---
title: ESET scopre CeranaKeeper, gruppo APT affiliato al governo cinese
url: https://www.securityinfo.it/2024/10/08/eset-scopre-ceranakeeper-gruppo-apt-affiliato-al-governo-cinese/?utm_source=rss&utm_medium=rss&utm_campaign=eset-scopre-ceranakeeper-gruppo-apt-affiliato-al-governo-cinese
source: Securityinfo.it
date: 2024-10-09
fetch_date: 2025-10-06T18:54:57.709994
---

# ESET scopre CeranaKeeper, gruppo APT affiliato al governo cinese

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

## ESET scopre CeranaKeeper, gruppo APT affiliato al governo cinese

Ott 08, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2024/10/08/eset-scopre-ceranakeeper-gruppo-apt-affiliato-al-governo-cinese/#respond)

---

I ricercatori di ESET [hanno scoperto](https://www.welivesecurity.com/en/eset-research/separating-bee-panda-ceranakeeper-making-beeline-thailand/) le attività di **CeranaKeeper**, un **gruppo APT allineato alla Cina** che ha preso di mira istituzioni governative in diversi Paesi asiatici, esfiltrando grandi quantità di dati.

Il nome del gruppo, ideato dai ricercatori, è un gioco di parole tra il termine “beekeeper”, ispirato dalle numerose occorrenze della stringa “bectrl” nel codice dei tool del gruppo, e la specie di ape Apis Cerana, l’ape asiatica del miele.

![CeranaKeeper](https://www.securityinfo.it/wp-content/uploads/2024/10/beekeeper.jpg)

Credits: ESET

CeranaKeeper utilizza molti strumenti e tecniche in rapida e continua evoluzione: **gli attaccanti riscrivono il set di strumenti in base alle necessità, per cercare di eludere il rilevamento**. L’obiettivo del gruppo APT è raccogliere il numero maggior di file possibile per accedere a conoscenze militari e governative.

Il gruppo usa servizi cloud e di condivisione file per l’esfiltrazione dei dati, cercando di camuffare il traffico con quello legittimo e difficile da bloccare di questi servizi.

CeranaKeeper è attivo almeno dal 2022 e ha come obiettivo principale gli enti governativi in Thailandia, Myanmar, Filippine, Giappone e Taiwan. Nel dettaglio, negli attacchi contro le istituzioni thailandesi **il gruppo ha usato componenti rivisitate attribuite da altri ricercatori a MustangPanda**, un altro gruppo APT allineato alla Cina, oltre a un nuovo set di strumenti in grado di violare service provider quali Pastebin, Dropbox, OneDrive e GitHub.

I ricercatori ritengono che i due gruppi siano entità separate, anche se **è possibile che condividano informazioni e una parte degli strumenti.** “*Nonostante alcune somiglianze nelle loro attività, come obiettivi comuni e formati di archivi simili, **ESET ha osservato differenze organizzative e tecniche tra i due gruppi, ad esempio nei set di strumenti, infrastrutture, procedure e campagne.** Abbiamo anche notato differenze nel modo in cui i due gruppi svolgono compiti simili*” ha affermato **Romain Dumont**, ricercatore di ESET che ha scoperto CeranaKeeper.

Il gruppo usa un **set di strumenti pubblici chiamato** **“bespoke stagers”** che sfrutta una tecnica di side loading e una specifica sequenza di comandi per esfiltrare file dalla rete. L’uso di componenti PlugX rimanda ancora una volta all’attività di MustangPanda, ma ci sono differenza organizzative e tecniche che confermano l’idea che si tratti di entità differenti.

Dopo l’accesso alla rete, il gruppo installa la **backdoor TONESHELL**, esegue uno strumento per il dump delle credenziali e usa un driver Avast e un’applicazione personalizzata per disabilitare gli antivirus presenti sulle macchine. Per spostarsi lateralmente, **il gruppo distribuisce uno script BAT** e sfrutta il controller di dominio per ottenere i privilegi di amministratore. Ciò permette a CeranaKeeper di esfiltrare enormi quantità di dati.

“*Il gruppo dietro gli attacchi al governo tailandese, CeranaKeeper, sembra particolarmente implacabile, dato che **la pletora di strumenti e tecniche che il gruppo utilizza continua a evolversi a un ritmo rapido***” spiega il team di ESET. Il gruppo sta continuando con le sue attività ed è probabile che **colpirà nuovi obiettivi evolvendo le tecniche e i tool a disposizione.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [APT](https://www.securityinfo.it/tag/apt/), [CeranaKeeper](https://www.securityinfo.it/tag/ceranakeeper/), [Cina](https://www.securityinfo.it/tag/cina/), [ESET](https://www.securityinfo.it/tag/eset/)

[Report Acronis: le minacce e le attività cybercriminali di agosto](https://www.securityinfo.it/2024/10/09/report-acronis-le-minacce-e-le-attivita-cybercriminali-di-agosto/)
[Acronis individua un sofisticato attacco contro produttori di droni di Taiwan](https://www.securityinfo.it/2024/10/07/acronis-individua-un-sofisticato-attacco-contro-produttori-di-droni-di-taiwan/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  [MuddyWater si evolve: attacchi più...](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "Permanent link to MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  Set 17, 2025  [0](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/#respond)
* [![Cina contro Nvidia: dubbi sulla sicurezza dei chip AI e sospetti di backdoor](https://www.securityinfo.it/wp-content/uploads/2025/08/nVidia-13-ago-2025CG-120x85.png)](https://www.securityinfo.it/2025/08/13/cina-contro-nvidia-dubbi-sulla-sicurezza-dei-chip-ai-e-sospetti-d...