---
title: Scoperto PathWiper, un nuovo wiper che colpisce le infrastrutture critiche ucraine
url: https://www.securityinfo.it/2025/06/05/scoperto-pathwiper-un-nuovo-wiper-che-colpisce-le-infrastrutture-critiche-ucraine/
source: Over Security - Cybersecurity news aggregator
date: 2025-06-06
fetch_date: 2025-10-06T22:56:19.668054
---

# Scoperto PathWiper, un nuovo wiper che colpisce le infrastrutture critiche ucraine

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

## Scoperto PathWiper, un nuovo wiper che colpisce le infrastrutture critiche ucraine

Giu 05, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Malware](https://www.securityinfo.it/category/news/malware-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/06/05/scoperto-pathwiper-un-nuovo-wiper-che-colpisce-le-infrastrutture-critiche-ucraine/#respond)

---

I ricercatori di Cisco Talos [hanno individuato](https://blog.talosintelligence.com/pathwiper-targets-ukraine/) una campagna ai danni delle infrastrutture critiche ucraine che utilizza **PathWiper**, un nuovo wiper di origine russa.

L’attacco è stato portato avanti sfruttando un framework di gestione di endpoint legittimo: gli attaccanti hanno evidentemente ottenuto accesso alla console di admin e l’hanno usata per distribuire il wiper sugli endpoint connessi. “*Durante l’attacco, i nomi dei file e le azioni utilizzate puntavano a* *imitare quelli impiegati dalla console amministrativa di utility, indicazione del fatto che **gli aggressori avevano una conoscenza preliminare della console e forse anche delle sue funzionalità usate nell’ambiente aziendale della*** ***vittima***” spiegano i ricercatori.

![PathWiper](https://www.securityinfo.it/wp-content/uploads/2025/06/Gemini_Generated_Image_58nu3458nu3458nu.jpg)

Nel dettaglio, gli attaccanti hanno inviato un comando creato ad hoc in modo che venisse eseguito dal client come un **file batch** (BAT). Il file eseguiva a sua volta un file VBScript malevolo, `uacinstall.vbs`, che installava ed eseguiva `sha256sum.exe`, il payload di PathWiper.

Una volta eseguito, il wiper **sovrascrive i contenuti degli artefatti del file system con dati randomici** generati sul momento. PathWiper si occupa inoltre di stilare una lista di tutti i supporti di archiviazione, volumi e path del client; in seguito, crea un thread per ogni elemento e, nuovamente, rimpiazza gli artefatti con dati casuali. Prima della sovrascrittura, il wiper tenta di effettuare il dismount dei volumi.

Stando a quanto riportato da Cisco Talos, **PathWiper è semanticamente simile a HermeticWiper** (noto anche come FoxBlade e NEARMISS), un wiper russo attivo nel 2022 e attribuito al gruppo Sandworm. Entrambi i wiper, inoltre, cercando di corrompere il *master boot record*(MBR) e gli artefatti legati a NTFS.

Nonostante le somiglianze, i due malware presentano una diff**erenza significativa nel meccanismo di corruzione utilizzato.** Non è chiaro quindi se il nuovo wiper sia una versione aggiornata del precedente o se dietro ci sia un altro gruppo hacker legato alla Russia.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Cisco Talos](https://www.securityinfo.it/tag/cisco-talos/), [conflitto russo-ucraino](https://www.securityinfo.it/tag/conflitto-russo-ucraino/), [HermeticWiper](https://www.securityinfo.it/tag/hermeticwiper/), [Infrastrutture critiche](https://www.securityinfo.it/tag/infrastrutture-critiche/), [PathWiper](https://www.securityinfo.it/tag/pathwiper/), [wiper](https://www.securityinfo.it/tag/wiper/)

[Torna l'incubo BADBOX 2.0: infettati oltre un milione di dispositivi](https://www.securityinfo.it/2025/06/06/torna-lincubo-badbox-2-0-infettati-oltre-un-milione-di-dispositivi/)
[Malware dentro il malware: trovate backdoor nel RAT Sakura](https://www.securityinfo.it/2025/06/04/malware-dentro-il-malware-trovate-backdoor-nel-rat-sakura/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Static Tundra sfrutta una vecchia vulnerabilità Cisco per spionaggio](https://www.securityinfo.it/wp-content/uploads/2025/08/StaticTundra_21-ago-2025CG-120x85.png)](https://www.securityinfo.it/2025/08/21/static-tundra-sfrutta-una-vecchia-vulnerabilita-cisco-per-spionaggio/ "Static Tundra sfrutta una vecchia vulnerabilità Cisco per spionaggio")

  [Static Tundra sfrutta una vecchia...](https://www.securityinfo.it/2025/08/21/static-tundra-sfrutta-una-vecchia-vulnerabilita-cisco-per-spionaggio/ "Permanent link to Static Tundra sfrutta una vecchia vulnerabilità Cisco per spionaggio")

  Ago 21, 2025  [0](https://www.securityinfo.it/2025/08/21/static-tundra-sfrutta-una-vecchia-vulnerabilita-cisco-per-spionaggio/#respond)
* [![Anubis, un nuovo ransomware che integra un wiper](https://www.securityinfo.it/wp-content/uploads/2025/06/Gemini_Generated_Image_olrxraolrxraolrx-scaled-120x85.jpg)](https://www.securityinfo.it/2025/06/16/anubis-un-nuovo-ransomware-che-integra-un-wiper/ "Anubis, un nuovo ransomware che integra un wiper")

  [Anubis, un nuovo ransomware che integra...](https://www.securityinfo.it/2025/06/16/anubis-un-nuovo-ransomware-che-integra-un-wiper/ "Permanent link to Anubis, un nuovo ransomware che integra un wiper")

  Giu 16, 2025  [0](https://www.securityinfo.it/2025/06/16/anubis-un-nuovo-ransomware-che-integra-un-wiper/#respond)
* [![Spionaggio russo: scoperta una campagna attiva dal 2022](https://www.securityinfo.it/wp-content/uploads/2025/05/ransomware-2321110_1920-120x85.jpg)](https://www.securityinfo.it/2025/05/22/spionaggio-russo-scoperta-una-campagna-attiva-dal-2022/ "Spionaggio russo: scoperta una campagna attiva dal 2022")

  [Spionaggio russo: scoperta una campagna...](https://www.securityinfo.it/2025/05/22/spionaggio-russo-scoperta-una-campagna-attiva-dal-2022/ "Permanent link to Spionaggio russo: scoperta una campagna attiva dal 2022")

  Mag 22, 2025  [0](https://www.securityinfo.it/2025/05/22/spionaggio-russo-scoperta-u...