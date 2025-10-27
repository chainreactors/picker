---
title: Slopsquatting: quando l’IA consiglia pacchetti che non esistono
url: https://www.securityinfo.it/2025/04/15/slopsquatting-quando-lia-consiglia-pacchetti-che-non-esistono/
source: Over Security - Cybersecurity news aggregator
date: 2025-04-16
fetch_date: 2025-10-06T22:09:08.251133
---

# Slopsquatting: quando l’IA consiglia pacchetti che non esistono

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

## Slopsquatting: quando l’IA consiglia pacchetti che non esistono

Apr 15, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Attacchi](https://www.securityinfo.it/category/approfondimenti/attacchi/), [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/approfondimenti/minacce/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/04/15/slopsquatting-quando-lia-consiglia-pacchetti-che-non-esistono/#respond)

---

La diffusione dell’IA e il progressivo miglioramento degli LLM ha reso questi strumenti un **aiuto ormai essenziale per il mondo dello sviluppo software**. Nonostante i guadagni in produttività, l’uso di questi tool comporta anche numerosi rischi di sicurezza, tra i quali anche il novello “**Slopsquatting**“.

Il termine, coniato da **Seth Larson**, ricercatore per la Python Software Foundation, indica **l’introduzione da parte degli attaccanti di package Python con nomi che potrebbero essere generati (per sbaglio) dagli assistenti di IA.** Questi pacchetti contengono codice malevolo; la speranza è appunto che, per via delle allucinazioni degli strumenti, qualche sviluppatore lo copi e lo installi senza rendersi conto che sia falso.

![Slopsquatting](https://www.securityinfo.it/wp-content/uploads/2025/04/13311397_v617batch2-kul-05-technology-scaled.jpg)

Blue futuristic networking technology vector

## Gli errori degli LLM

In un post dedicato all’argomento, il team di Socket [riporta](https://socket.dev/blog/slopsquatting-how-ai-hallucinations-are-fueling-a-new-class-of-supply-chain-attacks) i risultati di una ricerca proprio sulle allucinazioni legate ai nomi dei package Python nel codice generato dagli LLM. Condotta da un team della University of Texas e della University of Oklahoma, la ricerca ha testato 16 tra i modelli di generazione del codice più usati, sia commerciali che open-source.

Dai risultati è emerso che **il 19,7% dei pacchetti consigliati dagli LLM non esiste**. I modelli open-source hanno commesso errori più frequentemente rispetto a quelli commerciali, con CodeLlama 7B e CodeLlama 34B che hanno “allucinato” più degli altri, in più di un terzo degli input. Il meno prono a errori è stato invece GPT-4 Turbo con tasso di allucinazione del 3,59%. In tutto, sono stati generati **205.000 nomi errati e unici di pacchetti.**

Durante l’esperimento, i ricercatori hanno eseguito per 10 volte ognuno dei 500 prompt di sviluppo di codice. Dalle prove è emerso che il 43% dei pacchetti inesistenti è stato riproposto ogni volta, mentre il 39% non è più comparso dopo la prima volta. “*Questa netta differenza suggerisce un pattern bimodale nel comportamento dei modelli: **le allucinazioni sono o altamente stabili o del tutto imprevedibili***” ha spiegato il team di Socket.

Ancora più significativo è il fatto che il 58% dei pacchetti falsi è stato ripetuto più di una volta durante le ripetizioni: ciò significa che la maggior parte delle allucinazioni non sono solo “*rumore casuale*” ma nomi ripetibili che dipendono da come i modelli rispondono ai prompt. Questo facilita il lavoro degli attaccanti nell’**individuare gli LLM più proni a errori e i nomi dei package errati più ripetuti**, così da creare i pacchetti malevoli con quei nomi.

![](https://www.securityinfo.it/wp-content/uploads/2025/04/13311414_v627-aew-41-technologybackground-scaled.jpg)

Un’altra questione preoccupante è che **la maggior parte dei nomi falsi dei pacchetti è semanticamente convincente**, con il 38% dei risultati che erano molto simili a quelli reali e ne simulavano la struttura di naming. Inoltre, l’8,7% dei pacchetti Python “allucinati” erano in realtà pacchetti npm validi.

Un aspetto positivo è che alcuni modelli riescono a identificare i nomi errati che hanno generato con un’accuratezza media del 75%.

## Slopsquatting: un rischio per la supply chain

Lo Slopsquatting si aggiunge alla lista di attacchi di tipo “package confusion” che **mettono a serio rischio la supply chain.** “*I pacchetti “allucinati” possono essere generati in maniera consistente e condivisi ampiamente con auto-completamenti, tutorial e porzioni di codice scritte dall’IA*“.

Questa minaccia può scalare in breve tempo: se un pacchetto falso viene consigliato da sempre più modelli e un attaccante ha registrato quel nome, il codice malevolo si diffonde senza troppi problemi. “*Visto che molti sviluppatori si fidano dell’output dei tool di IA senza una validazione rigorosa, la finestra di opportunità è spalancata*“. Con sempre più sviluppatori che affidano all’IA l’implementazione completa del codice, **il rischio di fidarsi ciecamente delle dipendenze introdotte dall’IA e di non verificare l’esistenza dei pacchetti aumenta.**

Aumentare il livello di attenzione in questo caso è essenziale: se l’IA è un ottimo aiuto per velocizzare la produzione di codice, è importante **verificare attentamente gli output**, soprattutto quando si sceglie di usare librerie e pacchetti. Visto l’impatto dello Slopsquatting, è anche indispensabile **fare affidamento a strumenti in grado di segnalare pacchetti pubblicati di recente o sospetti** prima che vengano installati.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Intelligenza artificiale](https://www.securityinfo.it/tag/intelligenza-artificiale/), [librerie](https://www.securityinfo.it/tag/librerie/), [LLM](https://www.securityinfo.it/tag/llm/), [python package](https://www.securityinfo.it/tag/python-package/), [Slop...