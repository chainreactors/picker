---
title: BlueMoon usato in campagne di spionaggio, le ultime dal versante APT, attività cybercrime globali e con target Italia
url: https://www.telsy.com/bluemoon-usato-in-campagne-di-spionaggio-le-ultime-dal-versante-apt-attivita-cybercrime-globali-e-con-target-italia/
source: Over Security
date: 2026-11-06
fetch_date: 2026-11-07T08:01:46.372576
---

# BlueMoon usato in campagne di spionaggio, le ultime dal versante APT, attività cybercrime globali e con target Italia

* Gruppo TIM

[![Telsy](https://www.telsy.com/wp-content/themes/telsy/images/Logo_Telsy_pos-hor_RGB.png)](https://www.telsy.com/)

[Per fare una ricerca scrivi qualcosa e premi "invio"](/?s=)

Chiudi

* [Chi siamo](https://www.telsy.com/chi-siamo/)
* Soluzioni
  + [Vai a Soluzioni](https://www.telsy.com/soluzioni/)
  + [Cyber](https://www.telsy.com/soluzioni/cyber-ita/)
  + [Crypto](https://www.telsy.com/soluzioni/crypto-ita/)
  + [Quantum](https://www.telsy.com/soluzioni/quantum-ita/)
* [Innovazione](https://www.telsy.com/innovazione/)
* [Lavora con noi](https://www.telsy.com/lavora-con-noi/)
* [Blog](https://www.telsy.com/blog/)

* News in evidenza
  + [06 Nov

    Offensive OT e violazioni informatiche, campagne APT e cyberspionaggio, framework AI e minacce inedite](https://www.telsy.com/offensive-ot-e-violazioni-informatiche-campagne-apt-e-cyberspionaggio-framework-ai-e-minacce-inedite/)
  + [30 Ott

    PHP2Shell, Fragnesia e nuovi exploit ITW, operazioni APT e di cyberspionaggio, le ultime dalla penisola](https://www.telsy.com/php2shell-fragnesia-e-nuovi-exploit-itw-operazioni-apt-e-di-cyberspionaggio-le-ultime-dalla-penisola/)

[Offensive OT e violazioni informatiche, campagne APT e cyberspionaggio, framework AI e minacce inedite](https://www.telsy.com/offensive-ot-e-violazioni-informatiche-campagne-apt-e-cyberspionaggio-framework-ai-e-minacce-inedite/)
[PHP2Shell, Fragnesia e nuovi exploit ITW, operazioni APT e di cyberspionaggio, le ultime dalla penisola](https://www.telsy.com/php2shell-fragnesia-e-nuovi-exploit-itw-operazioni-apt-e-di-cyberspionaggio-le-ultime-dalla-penisola/)
[Vedi tutte](https://www.telsy.com/blog/)

* [English](https://www.telsy.com/en/bluemoon-used-in-espionage-campaigns-the-latest-developments-on-the-apt-front-global-cybercrime-activity-and-operations-targeting-italy/)
* [Italiano](https://www.telsy.com/bluemoon-usato-in-campagne-di-spionaggio-le-ultime-dal-versante-apt-attivita-cybercrime-globali-e-con-target-italia/)

[Threat Intelligence](https://www.telsy.com/categoria/threat-intelligence/), [News](https://www.telsy.com/categoria/news/)

# BlueMoon usato in campagne di spionaggio, le ultime dal versante APT, attività cybercrime globali e con target Italia

11 Set 2026

Condividi

## ![Weekly Threats hor Telsy](https://www.telsy.com/wp-content/uploads/Weekly-Threats-hor-Telsy.png)

## BlueMoon: exploit kit 0-day rapidamente adottato in campagne di spionaggio

Tra la fine di agosto e l’inizio di settembre 2026 è stato osservato **BlueMoon**, un nuovo exploit kit impiegato da gruppi orientati allo spionaggio in campagne di spear phishing mirate. Il primo utilizzo noto risale al 28 agosto, quando il gruppo state-sponsored cinese [**APT31**](https://www.telsy.com/en/tag/apt31/) lo ha utilizzato contro un numero limitato di ONG, aziende minerarie e società statunitensi attive nel commercio di materie prime. Nei giorni successivi BlueMoon è stato adottato anche da **UTA0560**, **UNK\_LateNight**, **UNK\_DoubleCheck** e **UNK\_QuietRacket**. La maggior parte dei gruppi osservati presenta un sospetto collegamento con la Cina, ma alcuni utilizzi rimangono non attribuiti e potrebbero esistere ulteriori avversari che impiegano lo stesso exploit kit. BlueMoon concatena tre [vulnerabilità](https://www.telsy.com/le-vulnerabilita-informatiche/). La prima, **CVE-2026-85046** (CVSS 8.8), è una *Type Confusion* nel motore JavaScript V8 di Chromium che consente l’esecuzione di codice nel renderer. La seconda, **CVE-2026-87491** (CVSS 8.8), è una vulnerabilità di sandbox escape in V8 classificata come *Out-of-bounds Write* e, infine, la terza, **CVE-2026-85880** (CVSS 7.8), è una vulnerabilità di *Privilege Escalation* nel kernel Windows presente in build meno recenti e utilizzata per uscire dal processo renderer e ottenere privilegi elevati. Completata la catena, BlueMoon consente l’esecuzione di un comando scelto dall’attaccante e il successivo caricamento del payload sul sistema compromesso. Le due vulnerabilità V8 erano 0-day di tipo patch-gap: le correzioni erano già disponibili pubblicamente nel codice sorgente upstream di Chromium, ma non erano ancora state distribuite nelle versioni stabili di Chrome e degli altri browser basati su Chromium. Si ritiene probabile che lo sviluppatore di BlueMoon abbia utilizzato queste patch pubbliche per trasformare rapidamente le vulnerabilità in un’exploit chain funzionante. Le campagne hanno distribuito payload differenti. Almeno dal 28 agosto scorso, APT31 ha colpito un numero limitato di ONG, aziende minerarie e società statunitensi attive nel commercio di materie prime. L’APT di Pechino, tramite un loader chiamato **SUPERSTOMP**, ha installato **GemStone (LONGTALE)**, un’estensione malevola per browser Chromium camuffata da Google Gemini e progettata per raccogliere cookie, dati dello storage, sequenze di tasti, informazioni sulla navigazione e screenshot. A partire dal 1° settembre 2026, UTA0560 è stato osservato in operazioni contro diverse ONG nelle quali distribuiva una catena di loader culminante in **GRIMWEDGE**, una backdoor JScript eseguita in memoria con funzionalità di ricognizione, gestione di file e processi, esecuzione di comandi e caricamento di ulteriori payload. Dal 2 settembre, UNK\_LateNight ha preso di mira aziende aerospaziali statunitensi con esche B2B e richieste di preventivo legate alla base industriale della difesa, distribuendo **ShadowPad**. Nello stesso periodo, UNK\_DoubleCheck ha colpito un’azienda manifatturiera vietnamita tramite un account governativo del Sudest asiatico compromesso, mentre dal 3 settembre UNK\_QuietRacket, sospettato di essere allineato alla Cina, ha preso di mira organizzazioni governative, finanziarie e di consulenza in Indonesia e Singapore. Non è noto come i diversi gruppi abbiano ottenuto accesso a BlueMoon. Considerata la facilità con cui è stato adottato, si ritiene probabile una sua ulteriore diffusione tra avversari orientati sia allo spionaggio sia al profitto, mentre le versioni corrette vengono progressivamente distribuite sui browser basati su Chromium. Google ha corretto CVE-2026-85046 e CVE-2026-87491 rispettivamente il 3 e l’8 settembre, mentre Microsoft ha sanato CVE-2026-85880 l’8 settembre.

## APT: notizie inedite riguardanti Corea del Nord, Pakistan, Cina e Turchia

Due organizzazioni sudcoreane dei settori automotive e media sono state target di una campagna orientata alla sorveglianza e allo spionaggio di lungo periodo che ha sfruttato un toolkit Linux composto principalmente da una backdoor chiamata **Ted**, da un RAT basato su curl denominato **curlRAT**, da uno stager e da un keylogger SSH, oltre a versioni trojanizzate di crond, agetty, atd, sshd e polkitd. Parte dell’infrastruttura C2 risulta già associata a [**ScarCruft**](https://www.telsy.com/tag/scarcruft-it/), ma le evidenze disponibili non consentono di attribuire con certezza la campagna a uno specifico gruppo nordcoreano. Sempre ScarCruft ha condotto la campagna **Operation GitPower**, rivolta a personale di banche, assicurazioni e aziende in Corea del Sud, progettata per garantirsi l’accesso persistente ai computer delle vittime. In alcuni PDF di phishing i campi Creator e Producer recano la scritta opencode riconducibile all’omonimo agente AI. Infine, una recente analisi delle capacità cyber della Corea del Nord conferma un apparato articolato, parte integrante della strategia statale e impiegato per attività di intelligence, elusione delle sanzioni e generazione di entrate e fornisce elementi inediti. Spostandoci in Pakistan, **Barmanou** ha condotto una campagna contro target indiani del settore governativo, della Difesa e diplomatico, volta a ottenere controllo persistente e sottrazione di dati tramite il dispiegamento del RAT **Crimson** e di un RAT custom. Passando in Cina, il gruppo di spionaggio **UNC3569** ha sfruttato **CVE-2026-51990** in Sogou Input Method per distribuire una backdoor in C++ chiamata **GRAYRABBIT** attraverso una catena di...