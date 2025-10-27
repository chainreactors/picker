---
title: C2 custom (parte 1)
url: https://roccosicilia.com/2025/01/03/c2-custom-parte-1/
source: Over Security - Cybersecurity news aggregator
date: 2025-01-04
fetch_date: 2025-10-06T20:12:38.587041
---

# C2 custom (parte 1)

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/progetto-di-divulgazione/)
* [Sostieni il progetto](https://roccosicilia.com/sostieni-il-progetto/)
* [English version](https://medium.com/%40roccosicilia)

[cyber security](https://roccosicilia.com/category/cyber-security/), [hacking](https://roccosicilia.com/category/hacking/), [ita](https://roccosicilia.com/category/ita/)

## [C2 custom (parte 1)](https://roccosicilia.com/2025/01/03/c2-custom-parte-1/)

Published by

Rocco Sicilia

on

[3 gennaio 2025](https://roccosicilia.com/2025/01/03/c2-custom-parte-1/)

[![C2 custom (parte 1)](https://roccosicilia.com/wp-content/uploads/2025/01/coding.png?w=562)](https://roccosicilia.com/2025/01/03/c2-custom-parte-1/)

È un’esigenza di servizio che soddisfa una mia personale curiosità. Ho dei requisiti specifici da soddisfare:

* Traffico solo in HTTP/HTTPS e solo sulle relative porte standard 80/443
* Payload lato client in Powershell e Python
* Dimensioni payload estremamente ridotte

In questo post ragiono “ad alta voce” mentre scrivo il prototipo di cui pubblico il codice su github: <https://github.com/roccosicilia/http_c2>.

## Prototipo (in python)

La componente **C2** (il server) si deve limitare a ricevere i comandi che si vogliono impartire sul sistema target e metterli a disposizione del client che verrà a riederli via HTTP. Il payload da far girare sul **TARGET** deve chiedere, ad intervalli regolari (o irregolari) che comanda va impartito alla macchina target, eseguirlo ed inviare l’output al **C2** server.

![](https://roccosicilia.com/wp-content/uploads/2025/01/image-4.png?w=1024)

Per interagire con il C2 in modo semplice ho pensato di usare un piccolo “client” per inviare al server i comandi da impartire. In questo primissimo prototipo l’output dei comandi viene visualizzato nei log del server.

## Test in lab

Vi lascio un video in cui racconto brevemente perché mi sono messo a giocare con questo prototipo che ha finalità puramente accademiche:

Il codice del prototipo è in questo path della repo: <https://github.com/roccosicilia/http_c2/tree/main/HTTP_custom>. Il file [server.py](https://github.com/roccosicilia/http_c2/blob/main/HTTP_custom/server.py) si riferisce, ovviamente, alla componente server da avviare sulla macchina che si vuole usare come C2.

![](https://roccosicilia.com/wp-content/uploads/2025/01/image-1.png?w=1024)

Server in esecuzione nel mio LAB.

Il file [payload\_win.py](https://github.com/roccosicilia/http_c2/blob/main/HTTP_custom/payload_win.py) è lo script da far eseguire alla macchina target ed è la parte che probabilmente subirà più manipolazioni in quanto questo script deve necessariamente passare inosservato ai sistemi di Detection lato endpoint. È un semplicissimo python script che genera GET e POST, quindi di per se non fa nulla di male e, come appurato in diversi contesti, non dovrebbe essere identificato come minaccia ne a livello di analisi statica ne all’esecuzione. Mentre scrivo lo script viene eseguito serenamente su un host windows con i sistemi di Detection di base attivi (Defender).

![](https://roccosicilia.com/wp-content/uploads/2025/01/image-2.png?w=1024)

Target VM.

**Non affrontiamo ora il tema della Detection**, ma uno degli obiettivi è quello di restare quanto più possibile invisibili. Per fare un’esempio: scenari simili in powershell verrebbero immediatamente intercettati da WinDefender. Ci limitiamo a considerare che la componente “agent” appare innocua all’avvio dello script e ciò che potrebbe insospettire l’EDR è ciò che avviene dopo, ad esempio analizzando i comandi che vengono impartiti all’endpoint.

Nel file [cli.py](https://github.com/roccosicilia/http_c2/blob/main/HTTP_custom/cli.py) per ora ho predisposto un semplice menu con due scelte: una per uscire dal programma ed una per inserire manualmente un comando da impartire sul target.

![](https://roccosicilia.com/wp-content/uploads/2025/01/http_c2_test.png?w=1024)

Esempio di esecuzione di un comando nel mio LAB.

Probabilmente è l’anima *smanettona* che lo richiede, ma mi piace tenere separata la componente puramente client per interagire da “cli” con il server. Una giusta evoluzione potrebbe essere quella di portare l’output sul client ed aggiungere qualche opzione/funzione al menu.

## Perché il modello funziona?

Le infrastrutture Command and Control (che abbreviamo con C2) sono abbastanza complesse, soprattutto quando sono ricche di funzionalità, ma il principio di base è molto semplice e sfrutta i modelli con cui progettiamo e realizziamo le reti e i possibili entry point delle aziende/organizzazioni. Scomporre ai minimi termini questo tipo di infrastruttura ci permette – credo – di visualizzare meglio i motivi che le rendono così efficaci.

Partirei dalla delivery del payload che spesso è un pezzo di software estremamente ridotto che deve solo preoccuparsi di installarsi sulla macchina target e contattare il C2 per ricevere istruzioni. La via più “semplice” è fare in modo che un utente della rete riceva il nostro pacchetto regalo e lo esegua sulla propria workstation.

Nel mondo vero questo avviene, purtroppo, molto frequentemente: dalla tipica email con allegato il payload camuffato da altro al messaggio contraffatto di un collega/amico/conoscente che ti chiedere di scaricare un documento infetto. Qualche anno fa, giusto per fare un esempio reale, durante un security test il team con cui lavoravo aveva individuato una falla nel portale HR del target tramite cui era possibile eseguire upload arbitrari di file camuffati da CV dei candidati. Ipotizzando che quei file sarebbe stati scaricati ed aperti dal personale interno si decise di presentare delle candidature fittizie allegando il nostro payload camuffato da CV. Il giochetto funzionò.

Già in questa prima fase operativa ci sono (dovrebbero esserci) delle barriere da oltrepassare: email con link sospetti potrebbero essere analizzate dai sistemi di email security, file scaricati sulla workstation potrebbero essere analizzati staticamente dagli anti-malware, i nuovi processi potrebbe eseguire azioni sospette intercettate dell’EDR, le connessioni verso il C2 potrebbero insospettire l’IDS del firewall. Il potenziale lato difesa c’è, ma molto dipende dalla configurazione di questi sistemi e da chi li sta presidiando; considerando che queste tecniche sono ancora utilizzate e funzionanti è molto probabile che sul grado di confidenza con le capacità di detection dei sistemi dobbiamo ancora lavorarci parecchio.

Va anche considerato che non sempre gli endpoint sono nella condizione di essere protetti: un utente che opera remotamente rispetto alla propria sede molto probabilmente non può beneficiare di tutti i sistemi di sicurezza che sono presenti presso gli uffici, soprattuto in relazione alla navigazione. Per inciso, ci sono soluzioni anche per questo scenario ma la loro applicazione è abbastanza limitata, nella maggior parte dei casi un utente che usa il proprio laptop da casa mantiene le protezioni a livello email security ed endpoint security ma parte delle protezioni a livello rete non ci sono.

---

Se gli argomenti che porto su questo blog e sui miei canali ti interessato puoi iscriverti al blog lasciano la tua email:

Digita la tua e-mail…

Iscriviti

Per sostenere il mio progetto di divulgazione ed accedere a contenuti dedicati ai supporter puoi [iscriverti al mio canale Patreon](https://patreon.com/roccosicilia).

---

Il secondo punto di attenzione è ciò che avviene una volta che il paylaod ha fatto quello che doveva fare, ovvero installarsi sulla macchina target. Tralascio in questo post i vari trucchi che si possono usare e su cui torno nei prossimi capitoli, per ora ci basta riflettere sulle azioni che il software compie e gli strumenti che abbiamo per intercettarle.

Questa fase è per me la più affascinante e individuo due famiglie di “comportament...