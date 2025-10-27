---
title: PlushDaemon: un nuovo gruppo APT cinese colpisce la Corea del Sud. Il report di ESET
url: https://www.securityinfo.it/2025/01/29/plushdaemon-un-nuovo-gruppo-apt-cinese-colpisce-la-corea-del-sud-il-report-di-eset/
source: Over Security - Cybersecurity news aggregator
date: 2025-01-30
fetch_date: 2025-10-06T20:12:44.309831
---

# PlushDaemon: un nuovo gruppo APT cinese colpisce la Corea del Sud. Il report di ESET

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

## PlushDaemon: un nuovo gruppo APT cinese colpisce la Corea del Sud. Il report di ESET

Gen 29, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Malware](https://www.securityinfo.it/category/news/malware-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/01/29/plushdaemon-un-nuovo-gruppo-apt-cinese-colpisce-la-corea-del-sud-il-report-di-eset/#respond)

---

I ricercatori di ESET [hanno scoperto](https://www.welivesecurity.com/en/eset-research/plushdaemon-compromises-supply-chain-korean-vpn-service/) **PlushDaemon**, un nuovo **gruppo APT affiliato al governo cinese** che ha colpito la **supply chain di un provider VPN della Corea del Sud.**

“*Nel maggio 2024, abbiamo notato delle rilevazioni di **codice dannoso in un installer NSIS per Windows** che gli utenti della Corea del Sud avevano scaricato dal sito web del legittimo **software VPN IPany**. Analizzando ulteriormente, abbiamo scoperto che l’installer distribuiva sia il software legittimo che la backdoor*” ha affermato Facundo Muñoz, il ricercatore che ha scoperto la campagna.

![PlushDaemon](https://www.securityinfo.it/wp-content/uploads/2025/01/2025-01-28-Plush-Daemon.jpg)

Credits: ESET

Il gruppo ha sostituito l’installer legittimo della VPN con uno che distribuiva **SlowStepper**, una **backdoor con oltre 30 componenti** e funzionalità in grado di raccogliere grandi volumi di dati, anche dal browser, scattare foto, scansionare documenti, spiare gli utenti tramite audio e video e sottrarre le credenziali.

La backdoor non è nuova: secondo l’analisi di Muñoz, **esistono diverse versioni di Slowstepper**, di cui la prima risale al 31 gennaio 2019. La più nuova è stata compilata il 13 giugno 2024 (versione 0.2.12) ed è ad oggi la versione più completa in termini di funzionalità. Nell’attacco al provider di VPN, PlushDaemon ha utilizzato una versione antecedente, la **0.2.10 Lite**; il nome suggerisce che questa backdoor abbia meno funzionalità di quelle in altre versioni.

“*Le numerose componenti del toolset di PlushDaemon e la sua ricca storia di versionamento dimostrano che, anche se in precedenza sconosciuto, questo gruppo APT affiliato al governo cinese ha operato assiduamente per sviluppare un’ampia gamma di tool, rendendoli una **minaccia significativa dalla quale proteggersi***” avvisa ESET.

Dopo la scoperta, la compagnia ha informato il fornitore VPN riguardo la compromissione e l’installer dannoso è stato rimosso dal loro sito.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [APT](https://www.securityinfo.it/tag/apt/), [backdoor](https://www.securityinfo.it/tag/backdoor/), [Cina](https://www.securityinfo.it/tag/cina/), [PlushDaemon](https://www.securityinfo.it/tag/plushdaemon/), [SlowStepper](https://www.securityinfo.it/tag/slowstepper/), [VPN](https://www.securityinfo.it/tag/vpn/)

[L'IA generativa unifica le interfacce di gestione e migliora la cybersecurity](https://www.securityinfo.it/2025/01/29/lia-generativa-unifica-le-interfacce-di-gestione-e-migliora-la-cybersecurity/)
[I ransomware contro le appliance ESXi sfruttano il tunneling SSH per la persistenza](https://www.securityinfo.it/2025/01/28/i-ransomware-contro-le-appliance-esxi-sfruttano-il-tunneling-ssh-per-la-persistenza/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  [MuddyWater si evolve: attacchi più...](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "Permanent link to MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  Set 17, 2025  [0](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/#respond)
* [![Cina contro Nvidia: dubbi sulla sicurezza dei chip AI e sospetti di backdoor](https://www.securityinfo.it/wp-content/uploads/2025/08/nVidia-13-ago-2025CG-120x85.png)](https://www.securityinfo.it/2025/08/13/cina-contro-nvidia-dubbi-sulla-sicurezza-dei-chip-ai-e-sospetti-di-backdoor/ "Cina contro Nvidia: dubbi sulla sicurezza dei chip AI e sospetti di backdoor")

  [Cina contro Nvidia: dubbi sulla...](https://www.securityinfo.it/2025/08/13/cina-contro-nvidia-dubbi-sulla-sicurezza-dei-chip-ai-e-sospetti-di-backdoor/ "Permanent link to Cina contro Nvidia: dubbi sulla sicurezza dei chip AI e sospetti di backdoor")

  Ago 13, 2025  [0](https://www.securityinfo.it/2025/08/13/cina-contro-nvidia-dubbi-sulla-sicurezza-dei-chip-ai-e-sospetti-di-backdoor/#respond)
* [![Ondata di attacchi brute-force contro le VPN Fortinet, poi FortiManager](https://www.securityinfo.it/wp-content/uploads/2025/08/FortinetVPN13-ago-2025CG-120x85.png)](https://www.securityinfo.it/2025/08/12/ondata-di-attacchi-brute-force-contro-le-vpn-fortinet-poi-fortimanager/ "Ondata di attacchi brute-force contro le VPN Fortinet, poi FortiManager")

  [Ondata di attacchi brute-force contro...](https://www.securityinfo.it/2025/08/12/ondata-di-attacchi-brute-force-contro-le-vpn-fortinet-poi-fortimanager/ "Permanent link to Ondata di attacchi brute-force contro le VPN Fortin...