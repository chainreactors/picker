---
title: Lockbit hackerato: infrastruttura compromessa, ma il gruppo non si arrende
url: https://www.securityinfo.it/2025/05/09/lockbit-hackerato-infrastruttura-compromessa-ma-il-gruppo-non-si-arrende/?utm_source=rss&utm_medium=rss&utm_campaign=lockbit-hackerato-infrastruttura-compromessa-ma-il-gruppo-non-si-arrende
source: Securityinfo.it
date: 2025-05-10
fetch_date: 2025-10-06T22:31:23.748678
---

# Lockbit hackerato: infrastruttura compromessa, ma il gruppo non si arrende

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

## Lockbit hackerato: infrastruttura compromessa, ma il gruppo non si arrende

Mag 09, 2025  [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo_security/ "Articoli scritti da Giancarlo Calzetta")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [Hacking](https://www.securityinfo.it/category/news/hacking-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/05/09/lockbit-hackerato-infrastruttura-compromessa-ma-il-gruppo-non-si-arrende/#respond)

---

Il gruppo ransomware LockBit ha subito una **compromissione significativa della propria infrastruttura**, con la pubblicazione di dati sensibili che rivelano dettagli sulle operazioni interne e le negoziazioni con le vittime.

Il 7 maggio 2025, i pannelli di controllo degli affiliati del gruppo ransomware LockBit sono stati defacciati. Chi cercava di raggiungerli trovava una pagina con il messaggio “Don’t do crime CRIME IS BAD xoxo from Prague” e **un link per scaricare un dump** del database MySQL esfiltrato. Questo dump, denominato “paneldb\_dump.zip”, contiene **venti tabelle con informazioni dettagliate sulle operazioni del gruppo**, inclusi indirizzi Bitcoin, configurazioni dei payload e registri delle chat con le vittime .([BleepingComputer](https://www.bleepingcomputer.com/news/security/lockbit-ransomware-gang-hacked-victim-negotiations-exposed/?utm_source=chatgpt.com "LockBit ransomware gang hacked, victim negotiations exposed"))

### ![](https://www.securityinfo.it/wp-content/uploads/2025/05/Lockbit_Compromised-9-mag-2025CG-1024x683.png)

### Cosa c’è nel database

Il database esposto rivela **59.975 indirizzi Bitcoin unici**, presumibilmente utilizzati per ricevere pagamenti di riscatto. La tabella ‘builds’ elenca i **payload generati dagli affiliati**, con dettagli come chiavi pubbliche e, in alcuni casi, i **nomi delle aziende colpite**. La tabella ‘builds\_configurations’ fornisce informazioni sulle **configurazioni specifiche di ciascun payload**, come l’esclusione di server ESXi o determinati tipi di file da criptare. Particolarmente rilevante è la tabella ‘chats’, che contiene **4.442 messaggi di negoziazione** tra LockBit e le vittime, datati dal 19 dicembre al 29 aprile .

### Implicazioni per la sicurezza informatica

La compromissione di LockBit rappresenta un colpo significativo per il gruppo. L’esposizione delle sue operazioni interne **rende potenzialmente più semplice l’identificazione degli affiliati**. Molti esperti di sicurezza considerano questa violazione come un’opportunità per le forze dell’ordine e le organizzazioni di sicurezza informatica di analizzare le tattiche, tecniche e procedure (TTP) del gruppo, **migliorando le strategie di difesa** contro attacchi ransomware simili.

Dal canto suo, **il gruppo attaccato ha ammesso la compromissione, ma ostenta sicurezza**. Sulla sua pagina è apparso un messaggio in cui ammettono di esser caduti, ma anche di potersi rialzare facilmente, cosa che sembra abbiano fatto. Del resto, non è la prima volta che la infrastruttura di Lockbit viene attaccata e messa fuorigioco. L’ultima volta era stata addirittura oggetto di una operazione dell’FBI che sembrava aver smantellato tutto, solo [per vederli ricomparire dopo pochi giorni di nuovo in piena attività](https://www.securityinfo.it/2024/02/26/lockbit-resuscita-e-minaccia-gli-stati-uniti/).

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [compromise](https://www.securityinfo.it/tag/compromise/), [database dump](https://www.securityinfo.it/tag/database-dump/), [defacing](https://www.securityinfo.it/tag/defacing/), [Hacking](https://www.securityinfo.it/tag/hacking/), [LockBit](https://www.securityinfo.it/tag/lockbit/), [Ransomware](https://www.securityinfo.it/tag/ransomware/)

[CERT-AGID 4-9 maggio: utenti SPID sotto attacco e una nuove campagne MintsLoader](https://www.securityinfo.it/2025/05/12/cert-agid-4-9-maggio-utenti-spid-sotto-attacco-campagne-mintsloader/)
[Npm, attacco supply chain: compromesso un package con 45.000 download settimanali](https://www.securityinfo.it/2025/05/09/npm-attacco-supply-chain-compromesso-un-package-con-45-000-download-settimanali/)

---

![](https://secure.gravatar.com/avatar/d6a6ecdad542d883704003e541413ca8?s=90&d=mm&r=g)

##### [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo_security/)

##### Articoli correlati

* [![RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/wp-content/uploads/2025/10/Gemini_Generated_Image_t7m3xlt7m3xlt7m3-120x85.png)](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/ "RedHat vittima di un breach: sottratti oltre 500 GB di dati")

  [RedHat vittima di un breach: sottratti...](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/ "Permanent link to RedHat vittima di un breach: sottratti oltre 500 GB di dati")

  Ott 03, 2025  [0](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/#respond)
* [![TeamItaly, presentata la nuova squadra di giovani cyber defender](https://www.securityinfo.it/wp-content/uploads/2025/09/conferenza_stampa_gruppo_TeamItaly_Marco_Cervellini_CNA_e_Paolo_Prinetto_CINI-scaled-120x85.jpg)](https://www.securityinfo.it/2025/09/15/teamitaly-presentata-la-nuova-squadra-di-giovani-cyber-defender/ "TeamItaly, presentata la nuova squadra di giovani cyber defender")

  [TeamItaly, presentata la nuova squadra...](https://www.securityinfo.it/2025/09/15/teamitaly-presentata-la-nuova-squadra-di-giovani-cyber-defender/ "Permanent link to TeamItaly, presentata la nuova squadra di giovani cyber defender")

  Set 15, 2025  [0](https://www.securityinfo.it/2025/09/15/teamitaly-...