---
title: HomeLab – Intro
url: https://roccosicilia.com/2026/02/10/homelab-intro/
source: Over Security - Cybersecurity news aggregator
date: 2026-02-10
fetch_date: 2026-02-11T04:24:06.704375
---

# HomeLab – Intro

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/progetto-di-divulgazione/)
* [Sostieni il progetto](https://roccosicilia.com/sostieni-il-progetto/)
* [English version](https://medium.com/%40roccosicilia)

[cyber security](https://roccosicilia.com/category/cyber-security/), [hacking](https://roccosicilia.com/category/hacking/), [ita](https://roccosicilia.com/category/ita/), [study with me](https://roccosicilia.com/category/study-with-me/)

## [HomeLab – Intro](https://roccosicilia.com/2026/02/10/homelab-intro/)

Published by

Rocco Sicilia

on

[10 febbraio 2026](https://roccosicilia.com/2026/02/10/homelab-intro/)

[![HomeLab – Intro](https://roccosicilia.com/wp-content/uploads/2026/02/create-a-featured-image-for-a-blog-post-titled-homelab.png?w=1024)](https://roccosicilia.com/2026/02/10/homelab-intro/)

Come detto in [questo post su LinkedIn](https://www.linkedin.com/posts/roccosicilia_ids-ips-ed-analisi-del-traffico-share-7423779325562355713-nHq4?utm_source=share&utm_medium=member_desktop&rcm=ACoAAATK5U0By2qlNbOT_QThQp0s692DGhr_JfU) dedico qualche articolo (e video) al mio HomeLab con lo scopo di pubblicare i dettagli tecnici della struttura che ho scelto e renderlo replicabile per chiunque sia interessato a *smanettare* con dei test di laboratorio in ambito info sec. Nel mio caso l’esigenza specifica è disporre di un ambiente completo in cui eseguire e migliorare tecniche di attacco specifiche (per chi non sa mi occupo di security test sia come attività lavorativa che come campo di ricerca) in un contesto controllato da sistemi di detection a vari livelli.

#### Perché un HomeLab?

Chi lavora in un ambito tecnico informatico (come capita per molte discipline tecniche) hai bisogno di studiare (molto) e fare pratica (molta). Non importa l’età anagrafica raggiunta o gli anni di esperienza, lo studio è una costante anche a 44 anni (la mia età attuale) e con poco più di 20 anni di servizio alle spalle.

Disporre di un proprio HomeLab diventa presto una necessità. Epoche diverse hanno portato a strumenti e possibilità diversi: pre-virtualizzazione avere un HomeLab significava avere hardware, tanto hardware, su cui installare *cose*. Virtualizzazione e cloud computing hanno modificato enormemente il paradigma e oggi tutti noi possiamo disporre anche di molte risorse senza dover acquisire hardware di proprietà.

L’[azienda per cui lavoro](https://www.linkedin.com/company/nts-italy-gmbh-srl/) (che, sottolineo, è molto attenta alla preparazione dei team tecnici e mette a disposizione molti strumenti) mi mette a disposizione un ricco laboratorio con la possibilità di creare guest ed utilizzare prodotto commerciali. Da anni utilizzo anche risorse in cloud (in particolare AWS) per alcuni test. Nonostante l’abbondanza di risorse ci sono dei vincoli di cui devo tener conto e probabilmente tutti quelli che si occupano di cyber sec. e di security test hanno incontrato: le infrastruttura messe a disposizione dalla propria azienda o dai cloud provider sono sistemi che devono aderire a determinati standard di sicurezza, cosa che “cozza” con l’esigenza di simulare ambienti con vulnerabilità per spararci contro attacchi specifici. Mi è capitato più di una volta di trovarmi una istanza AWS isolata perché avvenivano cose “strane” o sospette dal punto di vista della sicurezza… ed effettivamente i miei test ad un sistema di controllo esterno sembrano ciò che sono, attacchi informatici (anche se simulati).

È per me stato naturale, ad un certo punto, riconsiderare la possibilità di disporre di un HomeLab in cui fare serenamente ***disastri***: far girare payload, far crashare sistemi, saturare le risorse, ecc., senza che questo si traduca in “risposte di prevenzione” da parte del provider o fastidi verso i miei colleghi con cui condivido il lab aziendale.

#### Struttura di base: hardware

![](https://roccosicilia.com/wp-content/uploads/2026/02/image-1.png?w=1024)

Schema di sintesi

In questo primo post descrivo l’infrastruttura di base. L’obiettivo è quindi consentire il setup iniziale dell’host e delle VMs con i sistemi operativi che sto utilizzando. Ovviamente avete pienamente titolo di valutare delle variazioni, le mie scelte sono legate a specifiche esigenze che vi riporto in modo che possiate fare una scelta soggettiva sul replicare la mia configurazione o apportare delle variazioni.

Partirei dall’hardware coinvolto. Il cuore del lab è un host che fa parte della mia dotazione aziendale (come dicevo [NTS Italy](https://www.linkedin.com/company/nts-italy-gmbh-srl/) ed in generale il gruppo [NTS Netzwerk Telekom Service](https://nts.eu) è molto attento alle esigenze tecniche ed agli strumenti di lavoro) che utilizzo come base per diverse operazioni di security test. L’host ha di fatto il compito di far girare diverse macchine virtuali che, a seconda dell’attività che devo svolgere, attivo e configuro opportunamente. Inizialmente usavo un device molto piccolo, un Raspberry PI che in realtà utilizzo ancora per alcune attività, ma con la crescita della complessità delle azioni ho avuto l’esigenza di cambiare device.

Ho scelto, dopo averlo già visto all’opera, un miniPC T9 pro (il riferimento al prodotto non ha scopi pubblicitari, per il lab potete prendere una qualsiasi macchina x86 64bit).

[![](https://roccosicilia.com/wp-content/uploads/2026/02/image-2.png?w=1024)](https://www.instagram.com/p/DS4yAkWioLm/)

Instagram post del setup

La macchina ha un onesto processore [Intel N95](https://www.intel.com/content/www/us/en/products/sku/231800/intel-processor-n95-6m-cache-up-to-3-40-ghz/specifications.html) con 4 core, 16 GB di RAM (aumentabili), SSD da 512 GB (la GPU è integrata). Come I/O ports ha 2 NIC Ethernet 1 Gbps + 1 NIC Wireless, 3 USB ports e 3 HDMI (che onestamente al momento non ho pensato di usare).

Per una mia esigenza personale ho mantenuto il sistema operativo Windows 11 (mi serve un sistema operativo Microsoft installato *bare metal* per alcuni test) ma per molti potrebbe avere più senso utilizzare una distro Linux o un hypervisor. Se come me decidete di mantenere Windows 11 suggerisco di lavorare un po’ sull’ottimizzazione delle risorse in modo da “contenere” la RAM che il sistema utilizzerebbe per l’avvio di Apps e servizio che probabilmente poi non userete. Lo so che è banale ma semplicemente disattivando qualche servizio e desktop app ho ridotto il consumo di memoria RAM “a sistema fermo” di quasi 2 GB e visto che l’obiettivo è far girare più VMs possibile su un singolo host la RAM va gestita bene.

Oltre al miniPC l’altro “pezzo di ferro” è lo switch, o meglio il router che utilizzo come uno switch. Si tratta di un RouterBoard che svariati anni fa ebbi in dono durante un corso MikroTik. Qui faccio una nota: per quanto riguarda il mondo enterprise ho sempre usato o cercato di usare tecnologia Cisco per la parte network e datacenter per un tema di affidabilità e funzionalità, non è un segreto il fatto che Cisco è stato uno dei vendor che ho approcciato per primo in ambito network e che ho ritrovato in moltissimi step del mio percorso professionale. La tecnologia Cisco come molte altre tecnologie è *virtualizzabile* ([Andrea mostra spesso](https://www.adainese.it/blog/) network lab completamente virtuali) ma le mie esigenze non sono compatibili con quelle di un host dedicato ad un tool come EVE-NG, per questo ho deciso di ripiegare sull’oggetto più piccolo che avevo e che mi consentisse di disporre di molte funzionalità mentre a costo di perdere in affidabilità e prestazioni. Fine della nota.

Torniamo al RouterBoard che per le esigenze del lab di base, quello che ho intenzione di descrivere in questa mini serie di post, deve fungere da switch per interconnettere gli host fisici (cioè quello che appoggio sulla mia scrivania) con gli host software, le virtual machines.

Nel mondo MikroTik questa configurazione è possibile asseg...