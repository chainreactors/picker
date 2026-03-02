---
title: Il concetto di detection e il punto di vista offensivo
url: https://roccosicilia.com/2026/03/01/il-concetto-di-detection-e-il-punto-di-vista-offensivo/
source: Over Security - Cybersecurity news aggregator
date: 2026-03-01
fetch_date: 2026-03-02T04:07:02.064732
---

# Il concetto di detection e il punto di vista offensivo

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/progetto-di-divulgazione/)
* [Sostieni il progetto](https://roccosicilia.com/sostieni-il-progetto/)
* [English version](https://medium.com/%40roccosicilia)

[cyber security](https://roccosicilia.com/category/cyber-security/), [hacking](https://roccosicilia.com/category/hacking/), [ita](https://roccosicilia.com/category/ita/)

## [Il concetto di detection e il punto di vista offensivo](https://roccosicilia.com/2026/03/01/il-concetto-di-detection-e-il-punto-di-vista-offensivo/)

Published by

Rocco Sicilia

on

[1 marzo 2026](https://roccosicilia.com/2026/03/01/il-concetto-di-detection-e-il-punto-di-vista-offensivo/)

[![Il concetto di detection e il punto di vista offensivo](https://roccosicilia.com/wp-content/uploads/2025/08/image.png?w=1024)](https://roccosicilia.com/2026/03/01/il-concetto-di-detection-e-il-punto-di-vista-offensivo/)

Questa miniserie è collegata alla serie sui lab-test che prevedono test offensivi e lo studio della detection. Diciamo che in realtà è la stessa serie declinata in due modi diversi: nel lab gli aspetti pratici e gli “esperimenti”, qui i concetti in parte estratti da alcuni testi e risorse prese in esame negli ultimi due anni.

È giusto prima di tutti mettersi d’accordo su cosa significa *detection*. In estrema sintesi possiamo dire che è l’abilità di identificare azioni malevole/sospette sulla base delle informazioni che abbiamo a disposizione. Nel mondo degli EDR e dei SIEM questo concetto di applica in modo abbastanza lineare: le informazioni vengono dai sensori e dalle fonti e la detection si basa sulla capacità di interpretare correttamente gli eventi. In alcuni casi sono singoli eventi ad essere significativi, in altri casi è un insieme di eventi ed informazioni tra loro correlate a dare un significato a ciò che stiamo osservando.

Basandoci su questo principio di base possiamo affermare che **la potenziale detection** ha un relazione diretta con la quantità di dati a disposizione: se ne ho pochi sarà più difficile ricostruire la storia di quello che sta avvenendo.

La quantità di dati di per se non è un elemento che garantisce una detection efficace, è la **capacità di correlare eventi e riconoscere pattern anomali/sospetti** che ci permette di migliorare la nostra capacità di detection.

---

Se ti interessano gli argomenti che porto sul blog e sui miei canali puoi supportare il mio progetto di divulgazione su [Patreon](https://patreon.com/roccosicilia) e accedere a contenuti aggiuntivi per i sostenitori. Iscriviti al blog per rimanere aggiornato:

Digita la tua e-mail…

Iscriviti

---

Nei moderni security test è necessario confrontarsi con infrastrutture che adottano tecnologie di detection e team operativi che hanno il compito di controllare i sistemi IT ed attivarsi in caso di eventi sospetti (SOC, MDR). Considerando che buona parte della difesa dei sistemi è affidata alla capacità di detection delle soluzioni di sicurezza informatica come EDR, XDR, NDR, SIEM, …, è necessario che i test si adeguino. Se un tempo ci si poteva accontentare di verifica se una vulnerabilità fosse sfruttabile oggi è necessario capire anche se un EDR è aggirabile o se il SOC team interpreta correttamente la telemetria generata da un sistema sotto attacco.

Da punto di vista offensivo diventa quindi necessario trovare il modo di simulare un attacco considerando la capacità dei sistemi di vedere e comprende cosa si sta cercando di fare. L’obiettivo di un test così strutturate è quindi verificare se esistono punti debili nell’infrastruttura target e misurare la capacità di detection e di risposta all’attacco. **Alla ricerca delle falle da sfruttare si aggiunge la necessità di eseguire le azioni di attacco simulato silenziosamente, senza generare detection**.

#### Bypass della detection

Possiamo considerare quattro principali tattiche per aggirare i sistemi di detection (rif. a *Evading EDR*).

Il **bypass a livello di configurazione** si riferisce al fatto che il sistema è in grado di collezionare informazioni che gli consentirebbero di individuare e riconoscere l’anomalia ma la configurazione adottata non gli consente di farlo. Supponiamo di avere una regola che è in grado di riconoscere un determinato threat sulla base di alcuni specifici event-id, questa regola non scatterà mai se il sistema non è stato configurato per collezionare e analizzare tutte le informazioni utili alla detection del threat.

Il **bypass di percezione** si riferisce all’incapacità dell’agente o del sistema di raccogliere telemetria significativa. Banalmente, se la soluzione che stiamo utilizzando non presenta funzionalità di raccolta di alcune specifiche informazioni (es: la modifica di file presenti su disco) potrebbe essere “cieco” in merito ad alcune attività sospette. La mancanza di telemetria a causa di una ridotta capacità di raccolta dei dati è un fattore molto importante da considerare è difficile da arginare se le soluzioni adottate non implementano le funzionalità necessarie ad una detection efficace.

Il **bypass logico** si riferisce a lacune nella definizione di una regole di detection o nel meccanismo stesso di detection. Le regole di detection sono sostanzialmente basate sul match di determinate condizioni che, se definite in modo errato, potrebbero non generare mai un effettivo rilevamento.

Su questo modello aggiungo qualche nota personale a seguito di riflessioni maturate quasi interamente negli ultimi 2-3 anni, diciamo tra il 2023 ed il 2026 e mentre lo scrivo mi rendo conto che sono temi che ho iniziato ad approfondire dopo [il mio ingresso in NTS](https://nts.eu), quando ho trovato l’ambiente giusto per sviluppare un percorso di crescita sui temi che ritenevo sarebbero stati estremamente utili per comprendere meglio il panorama delle nuove minacce.

È un tema che spesso commento su LinkedIn: la qualità degli strumenti ci permette di avere abbondante telemetria ed i vendor ci metto a disposizione un set di regole che potremmo definire standard e che per ovvie ragioni sono relativamente generica in quanto devono andar bene più o meno a tutti. La detection in senso stretto deriva dalla capacità di interpretare i dati che arrivano dalla telemetria, **quindi tanti dati e regole “povere” equivale ad una detection estremamente limitata**. Regole fatte male, per non dire assenti, portano al bypass di strumenti anche ottimi a causa delle logiche di implementazione. Questo è anche il tema del talk che sto preparando per l’[evento Cyber Frontiers](https://www.cyberfrontiers.it/home/programma/).

Il **bypass di classificazione** si riferisce alla difficoltà di distinguere un comportamento sospetto dai normale pattern che si riscontrano in una rete. Se tutta la company fa abitualmente molto traffico verso GitHub o OneDrive è molto più complicato intercettare un tentativo di exfiltration se si usano questi stessi “destinatari”. Questo concetto, in combinazione con il bypass logico, complica moltissimo gli scenari di difesa.

In generale possiamo dire che – semplifico all’estremo – se il threat actor riesce ad evitare che l’agent EDR generi telemetria o riesce a eseguire azioni la cui telemetria non è distinguibile in modo chiaro dal normale “rumore di fondo” che qualsiasi sistema complesso presenta, potremmo trovarci nella situazione di vedere il nostro sistemi di detection aggirato da una minaccia. I sistemi di detection che oggi abbiamo a disposizione sono potentissimi ma non sono infallibili.

#### Quindi?

In generale le risposte facili a problemi complessi non mi piacciono banalmente perché credo che non esistano. Ci sono diversi punti da discutere e comprendere per capire il problema ed in questo posto ho voluto dare una introduzione per poi discutere i singoli temi nei prossimi post e video.

Sul mio canale YouTube e nell’archivio delle live trovate sicuramente divers...