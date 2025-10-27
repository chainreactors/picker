---
title: Scanner di vulnerabilità: uno solo non basta più
url: https://www.securityinfo.it/2024/05/06/scanner-di-vulnerabilita-uno-solo-non-basta-piu/
source: Over Security - Cybersecurity news aggregator
date: 2024-05-07
fetch_date: 2025-10-06T17:19:15.034620
---

# Scanner di vulnerabilità: uno solo non basta più

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

## Scanner di vulnerabilità: uno solo non basta più

Mag 06, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Minacce](https://www.securityinfo.it/category/approfondimenti/minacce/), [News](https://www.securityinfo.it/category/news/)
 [0](https://www.securityinfo.it/2024/05/06/scanner-di-vulnerabilita-uno-solo-non-basta-piu/#respond)

---

Gli **scanner di vulnerabilità**, ovvero i software usati per individuare la presenza di bug nei sistemi, sfruttano un database di CVE note per verificare la presenza di debolezze in applicazioni, dispositivi o reti.

Come [sottolinea](https://thehackernews.com/2024/05/when-is-one-vulnerability-scanner-not.html) The Hacker News, questi scanner mirano a individuare più vulnerabilità possibili, ma visto che il numero di bug individuati ogni anno è molto elevato (circa 30.000), **è difficile per un singolo software riuscire ad avere il proprio database sempre aggiornato**; per questo molti scanner favoriscono la scansione solo di alcuni software, quelli più utilizzati dai propri clienti.

I software tendono anche a dare priorità alle vulnerabilità già sfruttato oppure a quelle presenti nei prodotti più utilizzati, creando un gap di conoscenza che può esporre i sistemi a molte minacce.

La soluzione è utilizzare un **approccio “multi-scanner”** per avere una copertura maggiore delle vulnerabilità e ottenere una visione completa della superficie di attacco; questa opzione però non è sempre percorribile a causa di costi elevati e difficoltà di gestione di più software.

![](https://www.securityinfo.it/wp-content/uploads/2024/04/hacking-3112539_1920-1.png)

Pixabay

Intruder, vendor di soluzioni per la gestione della superficie di attacco, ha risposto all’esigenza delle organizzazioni di poter contare su più scanner con **[Nuclei](https://www.intruder.io/blog/what-is-nuclei-vulnerability-scanner)**, un **software open-source che integra diversi motori di ricerca di vulnerabilità in una sola piattaforma.**

Nuclei è sempre più diffuso tra bounty hunter, penetration tester e ricercatori per la sua capacità di effettuare check di vulnerabilità molto velocemente contando su più scanner, come Tenable e OpenVAS. Il software **copre molte più vulnerabilità dei singoli scanner** e offre una dashboard di riepilogo con le priorità dei singoli bug, per aiutare le organizzazioni a scegliere quali servizi rafforzare per primi e quali non andrebbero esposti sul web.

Integrando Nuclei nella piattaforma di controllo di Intruder, le organizzazioni possono **monitorare tutti gli asset aziendali e analizzare immediatamente i nuovi servizi** per individuare eventuali vulnerabilità. Con la visibilità completa del perimetro di rete, è possibile tracciare tutti i servizi attivi, identificare cambiamenti degni di nota e monitorare porte, servizi e protocolli.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Intruder](https://www.securityinfo.it/tag/intruder/), [Nuclei](https://www.securityinfo.it/tag/nuclei/), [scanner](https://www.securityinfo.it/tag/scanner/), [scanner vulnerabilità](https://www.securityinfo.it/tag/scanner-vulnerabilita/)

[CERT-AGID 27 aprile – 3 maggio 2024: 29 campagne malevole, 218 IoC e il keylogger di PuntoFisco](https://www.securityinfo.it/2024/05/06/cert-agid-27-aprile-3-maggio-2024-29-campagne-malevole-218-ioc-keylogger-puntofisco/)
[Germania, Stati Uniti e UE condannano ufficialmente il gruppo russo APT28](https://www.securityinfo.it/2024/05/06/germania-stati-uniti-e-ue-condannano-ufficialmente-il-gruppo-russo-apt28/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

##### Altro in questa categoria

* [![CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco](https://www.securityinfo.it/wp-content/uploads/2025/10/CERT-AGID-cover-120x85.png)](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/ "CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco")

  [CERT-AGID 27 settembre – 3 ottobre:...](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/ "Permanent link to CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco")

  Ott 06, 2025
   [0](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/#respond)
* [![RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/wp-content/uploads/2025/10/Gemini_Generated_Image_t7m3xlt7m3xlt7m3-120x85.png)](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/ "RedHat vittima di un breach: sottratti oltre 500 GB di dati")

  [RedHat vittima di un breach: sottratti...](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/ "Permanent link to RedHat vittima di un breach: sottratti oltre 500 GB di dati")

  Ott 03, 2025
   [0](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/#respond)
* [![Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/wp-content/uploads/2025/10/Home-Odyssey-Cybersecurity-10-03-2025_04_08_PM-120x85.png)](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/ "Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia")

  [Clearskies: la suite di sicurezza...](https://www.secur...