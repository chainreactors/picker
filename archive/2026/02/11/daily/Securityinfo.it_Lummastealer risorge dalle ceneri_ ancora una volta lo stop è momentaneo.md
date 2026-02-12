---
title: Lummastealer risorge dalle ceneri: ancora una volta lo stop è momentaneo
url: https://www.securityinfo.it/2026/02/11/lummastealer-risorge-dalle-ceneri-ancora-una-volta-lo-stop-e-momentaneo/?utm_source=rss&utm_medium=rss&utm_campaign=lummastealer-risorge-dalle-ceneri-ancora-una-volta-lo-stop-e-momentaneo
source: Securityinfo.it
date: 2026-02-11
fetch_date: 2026-02-12T04:23:09.320518
---

# Lummastealer risorge dalle ceneri: ancora una volta lo stop è momentaneo

Aggiornamenti recenti Febbraio 11th, 2026 4:07 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Lummastealer risorge dalle ceneri: ancora una volta lo stop è momentaneo](https://www.securityinfo.it/2026/02/11/lummastealer-risorge-dalle-ceneri-ancora-una-volta-lo-stop-e-momentaneo/)
* [ZeroDayRAT: La Nuova Minaccia per Android e iOS](https://www.securityinfo.it/2026/02/10/zerodayrat-la-nuova-minaccia-per-android-e-ios/)
* [L’arma dell’autenticità: come il cybercrimine sta piegando i servizi SaaS](https://www.securityinfo.it/2026/02/09/larma-dellautenticita-come-il-cybercrimine-sta-piegando-i-servizi-saas/)
* [n8n: nuove vulnerabilità critiche aggirano le patch di dicembre](https://www.securityinfo.it/2026/02/06/n8n-sotto-pressione-nuove-vulnerabilita-critiche-aggirano-le-patch-di-dicembre/)
* [TrendAI: il 2026 sarà l’anno dell’industrializzazione del cybercrime](https://www.securityinfo.it/2026/02/06/trendai-2026-anno-industrializzazione-cybercrime/)

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

## Lummastealer risorge dalle ceneri: ancora una volta lo stop è momentaneo

Feb 11, 2026  [Redazione](https://www.securityinfo.it/author/redazione/ "Articoli scritti da Redazione")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Malware](https://www.securityinfo.it/category/news/malware-news/), [Minacce](https://www.securityinfo.it/category/minacce-2/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2026/02/11/lummastealer-risorge-dalle-ceneri-ancora-una-volta-lo-stop-e-momentaneo/#respond)

---

L’ecosistema del cybercrime dimostra ancora una volta una resilienza straordinaria: a meno di dodici mesi dall’operazione di smantellamento internazionale che sembrava averne decretato la fine, **LummaStealer è riemerso con una catena di infezione profondamente rinnovata**. Il ritorno di questo infostealer non è un semplice “rebranding”, ma una ristrutturazione tattica che vede l’introduzione di CastleLoader come primo stadio critico.

![](https://www.securityinfo.it/wp-content/uploads/2026/02/LummaFenice.png)

Questa nuova architettura dimostra come i gruppi MaaS (Malware-as-a-Service) **siano in grado di riorganizzare le proprie infrastrutture C2 e i vettori di delivery in tempi record**, capitalizzando sulle lezioni apprese dai precedenti shutdown delle autorità.

### L’Architettura Modulare e il Ruolo di CastleLoader

La nuova struttura offensiva si basa su un design modulare a più stadi, dove **CastleLoader funge da sofisticato “apripista” per il payload finale**. Questo loader non è un semplice downloader, ma un componente progettato per l’evasione preventiva. Una volta eseguito, solitamente attraverso archivi compressi che simulano software legittimo, CastleLoader avvia una serie di controlli ambientali per rilevare la presenza di sandbox o debugger. **Solo dopo aver confermato di trovarsi su un host reale e non in un ambiente di analisi**, il loader stabilisce una connessione cifrata per recuperare LummaStealer, iniettandolo direttamente nella memoria di processi di sistema già attivi, minimizzando così l’impronta sul file system dell’host.

Il nucleo operativo di LummaStealer è caratterizzato da **un offuscamento estremamente aggressivo**, finalizzato a neutralizzare sia l’analisi statica che quella euristica. Il malware impiega tecniche di risoluzione dinamica delle funzioni API, evitando di importare palesemente le librerie sospette nella propria tabella di importazione (IAT). Questo approccio, unito all’uso di junk code e metamorfismo del codice sorgente, **rende estremamente difficile la creazione di firme rilevanti**. Inoltre, il malware sfrutta il controllo del flusso indiretto per confondere i motori di disassemblaggio, garantendo che l’esecuzione del codice malevolo avvenga in modo non lineare e protetto da trigger di rilevamento comportamentale.

### Esfiltrazione Mirata e Gestione dei Dati Sensibili

Una volta stabilita la persistenza in memoria, LummaStealer attiva i suoi moduli di scansione focalizzati sull’estrazione di asset digitali di alto valore. Il targeting è chirurgico: **il malware interroga i database SQL dei browser per recuperare cookie di sessione** (utili per il session hijacking), **dati di auto-fill e credenziali salvate**. Particolare enfasi viene posta sui **cold wallet di criptovalute** e sulle estensioni browser dedicate alla gestione di asset digitali, dove il malware tenta di **esfiltrare chiavi private e seed**. I dati raccolti vengono pacchettizzati e inviati a server C2 attraverso protocolli di comunicazione che imitano il normale traffico web, spesso sfruttando servizi cloud legittimi come tunnel per mascherare la destinazione finale dei pacchetti esfiltrati.

### Infrastruttura di Comando e Strategie di Hardening

La rete di Comando e Controllo (C2) è stata riprogettata per **evitare i singoli punti di fallimento che hanno portato al precedente abbattimento**. Gli operatori utilizzano ora un’architettura decentralizzata o domini a vita breve (fast-flux), che rendono complessa l’identificazione dei server master. Per i difensori IT, il contrasto a questa minaccia richiede un monitoraggio intensivo dei tentativi di iniezione di memoria e delle anomalie nel traffico di rete in uscita. È essenziale **implementare soluzioni EDR** capaci di correlare l’apertura di file sospetti con chiamate di sistema insolite, oltre a una rigorosa segmentazione dei privilegi utente per impedire che il loader possa scalare le autorizzazioni necessarie per l’esfiltrazione dei dati di sistema.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [analisi tecnica malware](https://www.securityinfo.it/tag/analisi-tecnica-malware/), [C2 infrastructure](https://www.securityinfo.it/tag/c2-infrastructure/), [CastleLoader](https://www.securityinfo.it/tag/castleloader/), [cybercrime 2026](https://www.securityinfo.it/tag/cybercrime-2026/), [evasione EDR](https://www.securityinfo.it/tag/evasione-edr/), [Google Cloud Threat Intelligence](https://www.securityinfo.it/tag/google-cloud-threat-intelligence/), [infostealer](https://www.securityinfo.it/tag/infostealer/), [LummaStealer](https://www.securityinfo.it/tag/lummastealer/), [malware recovery](https://www.securityinfo.it/tag/malware-recovery/), [sicurezza endpoint](https://www.securityinfo.it/tag/sicurezza-endpoint/)

[ZeroDayRAT: La Nuova Minaccia per Android e iOS](https://www.securityinfo.it/2026/02/10/zerodayrat-la-nuova-minaccia-per-android-e-ios/)

---

![](https://secure.gravatar.com/avatar/57d6369d65bf9ebecae351af675ce2fd?s=90&d=mm&r=g)

##### [Redazione](https://www.securityinfo.it/author/redazione/)

##### Articoli correlati

* [![Il cybercrime si evolve e si adatta, integrando l’IA nel proprio arsenale: il report di ESET](https://www.securityinfo.it/wp-content/uploads/2025/12/Gemini_Generated_Image_r8bu02r8bu02r8bu-120x85.png)](https://www...