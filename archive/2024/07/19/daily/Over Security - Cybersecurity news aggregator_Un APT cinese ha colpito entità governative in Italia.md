---
title: Un APT cinese ha colpito entità governative in Italia
url: https://www.securityinfo.it/2024/07/18/un-apt-cinese-ha-colpito-entita-governative-in-italia/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-19
fetch_date: 2025-10-06T17:43:32.422790
---

# Un APT cinese ha colpito entità governative in Italia

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

## Un APT cinese ha colpito entità governative in Italia

Lug 18, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2024/07/18/un-apt-cinese-ha-colpito-entita-governative-in-italia/#respond)

---

[TG Soft](https://www.tgsoft.it/news/news_archivio.asp?id=1557), compagnia di cybersecurity italiana, ha reso noto che un **gruppo APT cinese ha colpito società governative in Italia** con due attacchi mirati, il 24 giugno e il 2 luglio.

![](https://www.securityinfo.it/wp-content/uploads/2024/07/ransomware-2321110_1920.jpg)

Pixabay

I due attacchi inducevano le vittime a scaricare e **installare un pacchetto di Skype for Business** da un link di un dominio simil-governativo, il quale poi installava una variante del malware Rat 9002. La prima campagna ha sfruttato un documento Office per distribuirla, mentre la seconda diffondeva direttamente un link malevolo.

Il documento Office era un file .docx chiamato “GUIDA OPERATIVA PER L’UTENTE” che invitava gli utenti a partecipare a una riunione Skype. Il file conteneva un link indicato come l’URL per scaricare la versione più recente del software, insieme a una breve guida per l’installazione.

Cliccando sul link, le vittime navigavano su un **sito che simulava una pagina ufficiale per i meeting di Equitalia Giustizia** e invitava l’utente a scaricare un pacchetto MSI per l’installazione del software. I ricercatori sottolineano che nella pagina era presente un link legittimo del dominio di Equitalia Giustizia, probabilmente intercettato in operazioni precedenti.

Una volta scaricato e installato il file, viene eseguito il malware RAT 9002 che esegue funzioni di proxy per monitorare il traffico e invia le informazioni al server controllato dagli attaccanti.

RAT 9002 è un **trojan modulare in grado di scaricare plugin aggiuntivi in base alle esigenze dei cybercriminali**, arricchendosi di funzionalità. L’analisi di TG Soft ha evidenziato che, nel caso degli attacchi alle entità italiane, il malware aveva scaricato i moduli ScreenSpyS.dll per catturare lo schermo, RemoteShellS.dll per l’esecuzione di programmi, UnInstallS.dll per la disintallazione dei software, FileManagerS.dll per navigare tra i file e ProcessS.dll per la gestione dei processi.

I ricercatori spiegano che il malware sembra essere in continuo aggiornamento, con **varianti anche diskless**. L’utilizzo di più moduli consente ai cyberattaccanti di ridurre la possibilità di essere intercettati.

![](https://www.securityinfo.it/wp-content/uploads/2024/06/hacker-6512174_1920.jpg)

A prendere di mira l’Italia è stato il gruppo APT cinese **DeputyDog**, conosciuto anche come APT17. “***L’attacco nella sua globalità risulta particolarmente sofisticato e progettato nei minimi dettagli**, i domini utilizzati sono molto simili a domini ufficiali ed anche la creazione del pacchetto MSI malevolo è stata realizzata con cura in quanto comporta l’installazione del software legittimo Skype for Business ed in parallelo la versione diskless del RAT 9002*” scrive il team di sicurezza.

Il consiglio è come sempre quello di non aprire file sospetti, installare software solo da fonti legittime e controllare attentamente il mittente di email e messaggi.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [APT](https://www.securityinfo.it/tag/apt/), [Cina](https://www.securityinfo.it/tag/cina/), [Italia](https://www.securityinfo.it/tag/italia/), [malware](https://www.securityinfo.it/tag/malware/), [RAT 9002](https://www.securityinfo.it/tag/rat-9002/), [Trojan](https://www.securityinfo.it/tag/trojan/)

[Apache HugeGraph-Server è sotto attacco: scoperta una vulnerabilità critica](https://www.securityinfo.it/2024/07/18/apache-hugegraph-e-sotto-attacco-scoperta-una-vulnerabilita-critica/)
[Gli hacker sfruttano gli exploit dopo 22 minuti dalla pubblicazione delle PoC](https://www.securityinfo.it/2024/07/17/gli-hacker-sfruttano-gli-exploit-dopo-22-minuti-dalla-pubblicazione-delle-poc/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  [MuddyWater si evolve: attacchi più...](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "Permanent link to MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  Set 17, 2025  [0](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/#respond)
* [![Un attacco supply chain ha compromesso oltre 40 pacchetti NPM](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_px0h5ppx0h5ppx0h-120x85.png)](https://www.securityinfo.it/2025/09/16/un-attacco-supply-chain-ha-compromesso-oltre-40-pacchetti-npm/ "Un attacco supply chain ha compromesso oltre 40 pacchetti NPM")

  [Un attacco supply chain ha compromesso...](https://www.securityinfo.it/2025/09/16/un-attacco-supply-chain-ha-compromesso-oltre-40-pacchetti-npm/ "Permanent link to Un attacco supply chain ha compromesso oltre 40 pacchetti NPM")

  Set 16, 2025  [0](htt...