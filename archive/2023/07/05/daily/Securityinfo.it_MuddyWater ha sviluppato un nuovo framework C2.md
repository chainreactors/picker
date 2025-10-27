---
title: MuddyWater ha sviluppato un nuovo framework C2
url: https://www.securityinfo.it/2023/07/04/muddywater-ha-sviluppato-un-nuovo-framework-c2/?utm_source=rss&utm_medium=rss&utm_campaign=muddywater-ha-sviluppato-un-nuovo-framework-c2
source: Securityinfo.it
date: 2023-07-05
fetch_date: 2025-10-04T11:55:50.355353
---

# MuddyWater ha sviluppato un nuovo framework C2

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

## MuddyWater ha sviluppato un nuovo framework C2

Lug 04, 2023  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Apt](https://www.securityinfo.it/category/minacce-2/apt/), [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Intrusione](https://www.securityinfo.it/category/news/intrusione/), [Minacce](https://www.securityinfo.it/category/minacce-2/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2023/07/04/muddywater-ha-sviluppato-un-nuovo-framework-c2/#respond)

---

[I ricercatori di Deep Instinct](https://www.deepinstinct.com/blog/phonyc2-revealing-a-new-malicious-command-control-framework-by-muddywater) hanno individuato un **nuovo framework di Command & Control (C2) a opera del gruppo APT MuddyWater**. Conosciuto anche come Mango Sandstorm o Mercury, il gruppo si occupa di cyber spionaggio ed è legato al Ministero dell’Intelligence e della Sicurezza iraniano.

Il framework, chiamato **PhonyC2**, **è in uso dal 2021** ed è stato utilizzato nel recente attacco contro il Technion Institute, un istituto di ricerca israeliano.

Lo scorso aprile i ricercatori della firma di sicurezza hanno individuato tre script PowerShell malevoli, parte di un archivio chiamato PhonyC2\_v6.zip. Il team di Deep Instinct ha analizzato il contenuto del file e il codice sorgente del framework, scoprendo che **il server che ospitava il C2 era legato all’infrastruttura usata da MuddyWater nell’attacco contro Technion Insitute.**

Ulteriori ricerche hanno dimostrato che questo nuovo framework era collegato anche alla campagna che sfrutta la [vulnerabilità di PaperCut](https://www.securityinfo.it/2023/05/02/vulnerabilita-critica-papercut-usata-attivamente-attaccanti/) e al tool Ligolo usato regolarmente da MuddyWater.

![MuddyWater framework C2 ](https://www.securityinfo.it/wp-content/uploads/2023/07/hacking-4038037_1920.jpg)

Credits: Pixabay

**Il gruppo APT sta lavorando attivamente al framework per migliorarlo.** La versione corrente individuata da Deep Instinct è scritta in Python3 ed è strutturalmente e funzionalmente simile a MuddyC3, un altro framework custom di MuddyWater scritto in Python2, rendendolo di fatto un suo successore.

Il framework si inserisce nelle fasi finali dell’Intrusion Kill Chain e permette a un attaccante di ottenere i dati di interesse dal dispositivo target.

Tra i comandi centrali del framework c’è “**payload**” per la generazione dei payload “C:\programdata\db.sqlite” e”C:\programdata\db.ps1″; “**droper**” che crea diverse varianti di comandi PowerShell per generare “C:\programdata\db.sqlite”; “**list**” per enumerare tutte le macchine connesse al server C2; “**use**” per ottenere una shell PowerShell su un computer remoto ed eseguire altri comandi; infine, “**persist**” per ottenere la persistenza sulla macchina colpita.

Per ottenere l’accesso iniziale ai sistemi, **MuddyWater sfrutta tecniche di social engineering** e server vulnerabili esposti sul web.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [APT](https://www.securityinfo.it/tag/apt/), [Command and Control](https://www.securityinfo.it/tag/command-and-control/), [deep instinct](https://www.securityinfo.it/tag/deep-instinct/), [framework](https://www.securityinfo.it/tag/framework/), [MuddyWater](https://www.securityinfo.it/tag/muddywater/), [Phishing](https://www.securityinfo.it/tag/phishing/), [phonyc2](https://www.securityinfo.it/tag/phonyc2/)

[Attacco all'aeroporto di Dublino: compromessi i dati di 2000 membri dello staff](https://www.securityinfo.it/2023/07/05/aeroporto-di-dublino-vittima-di-un-cyber-attacco-sottratti-i-dati-di-2000-membri-dello-staff/)
[Le 25 vulnerabilità software più pericolose secondo CWE](https://www.securityinfo.it/2023/07/04/le-25-vulnerabilita-software-piu-pericolose-secondo-cwe/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  [MuddyWater si evolve: attacchi più...](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "Permanent link to MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  Set 17, 2025  [0](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/#respond)
* [![Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-6138007_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/ "Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA")

  [Report Acronis: il ransomware rimane la...](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/ "Permanent link to Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA")

  Set 11, 2025  [0](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/#respond)
* [![Criminali abusano dei ser...