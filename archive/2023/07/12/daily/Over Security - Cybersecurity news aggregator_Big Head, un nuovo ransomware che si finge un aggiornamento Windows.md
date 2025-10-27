---
title: Big Head, un nuovo ransomware che si finge un aggiornamento Windows
url: https://www.securityinfo.it/2023/07/11/big-head-un-nuovo-ransomware-che-si-finge-un-aggiornamento-windows/
source: Over Security - Cybersecurity news aggregator
date: 2023-07-12
fetch_date: 2025-10-04T11:57:53.458030
---

# Big Head, un nuovo ransomware che si finge un aggiornamento Windows

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

## Big Head, un nuovo ransomware che si finge un aggiornamento Windows

Lug 11, 2023  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2023/07/11/big-head-un-nuovo-ransomware-che-si-finge-un-aggiornamento-windows/#respond)

---

I ricercatori di [Trend Micro](https://www.trendmicro.com/en_us/research/23/g/tailing-big-head-ransomware-variants-tactics-and-impact.html) hanno individuato e analizzato una **nuova famiglia di ransomware chiamata “Big Head”**. Le prime attività del ransomware, di cui al momento esistono tre varianti, risalgono allo scorso maggio.

Tutte e tre le versioni del ransomware vengono distribuite tramite **pubblicità malevola**, fingendosi **aggiornamenti di Windows o installer per Word.**

Dall’analisi di Trend Micro è emerso che il **ransomware**, nella sua versione “base”, **installa tre file sul sistema**: il primo, chiamato “1.exe”, contiene una copia del malware e viene usato per propagarlo nella rete di dispositivi; il secondo, “Archive.exe”, è un bot Telegram usato per stabilire la connessione con gli attaccanti; infine, “Xarch.exe” si occupa di cifrare i file del sistema e di mostrare una schermata di aggiornamento finta per far credere all’utente che il processo sia legittimo.

All’interno del file 1.exe è presente anche una **nota di riscatto dove è scritto l’indirizzo email da contattare per negoziare il pagamento**. Il ransomware, concluso il processo di cifratura, modifica anche lo sfondo del desktop della vittima impostando un’immagine con le indicazioni su contatti e pagamenti.

![Big Head ransomware](https://www.securityinfo.it/wp-content/uploads/2023/07/malware-7020225_1920-1.png)

Credits: Pixabay

Le altre due varianti si comportano in maniera simile, anche se possiedono capacità aggiuntive: una incorpora **funzioni per raccogliere dati sensibili e inviarli all’attaccante**; l’altra include **Neshta**, un **virus che colpisce gli eseguibili del sistema** target.

Secondo TrendMicro, **il gruppo o l’individuo dietro BigHead sembra ancora inesperto**, e il fatto che siano state rilasciate tre versioni del ransomware in così poco tempo indica che il malware non è ancora stabile; dal punto di vista tecnico inoltre, spiegano i ricercatori, **Big Head usa metodi di cifratura prevedibili e implementa tecniche di evasione deboli e facilmente individuabili.**

Stando agli ultimi aggiornamenti di KELA, [riportati da BleepingComputer](https://www.bleepingcomputer.com/news/security/new-big-head-ransomware-displays-fake-windows-update-alert/), sembra che il principale autore, se non l’unico, del ransomware sia di **origini indonesiane**: la firma ha individuato un utente su Telegram che per molto tempo ha usato gli stessi nomi e lo stesso avatar presenti nella nota del riscatto.

L’utente ha poi cambiato nome a giugno 2022, e a marzo scorso ha cominciato a cercare dei collaboratori per sviluppare un builder per ransomware. Nonostante la relativa semplicità del ransomware, i ricercatori invitano gli utenti a fare attenzione e a **scaricare gli aggiornamenti solo dal sito ufficiale del vendor.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [big head](https://www.securityinfo.it/tag/big-head/), [malware](https://www.securityinfo.it/tag/malware/), [Ransomware](https://www.securityinfo.it/tag/ransomware/), [TrendMicro](https://www.securityinfo.it/tag/trendmicro/), [virus](https://www.securityinfo.it/tag/virus/), [Windows](https://www.securityinfo.it/tag/windows/)

[NokNok: la nuova backdoor per macOS di Charming Kitten](https://www.securityinfo.it/2023/07/12/noknok-la-nuova-backdoor-per-macos-di-charming-kitten/)
[Più di 330.000 firewall FortiGate sono ancora vulnerabili a un bug già risolto](https://www.securityinfo.it/2023/07/11/300000-firewall-fortigate-vulnerabili-bug-risolto/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/wp-content/uploads/2025/10/Gemini_Generated_Image_t7m3xlt7m3xlt7m3-120x85.png)](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/ "RedHat vittima di un breach: sottratti oltre 500 GB di dati")

  [RedHat vittima di un breach: sottratti...](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/ "Permanent link to RedHat vittima di un breach: sottratti oltre 500 GB di dati")

  Ott 03, 2025  [0](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/#respond)
* [![MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  [MuddyWater si evolve: attacchi più...](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "Permanent link to MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  Set 17, 2025  [0](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/#respond)
* [![Rep...