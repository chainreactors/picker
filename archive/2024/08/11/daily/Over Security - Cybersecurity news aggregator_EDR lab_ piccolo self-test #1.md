---
title: EDR lab: piccolo self-test #1
url: https://roccosicilia.com/2024/08/10/edr-lab-piccolo-self-test-1/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-11
fetch_date: 2025-10-06T18:03:13.242617
---

# EDR lab: piccolo self-test #1

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/progetto-di-divulgazione/)
* [Sostieni il progetto](https://roccosicilia.com/sostieni-il-progetto/)
* [English version](https://medium.com/%40roccosicilia)

[cyber security](https://roccosicilia.com/category/cyber-security/), [hacking](https://roccosicilia.com/category/hacking/), [ita](https://roccosicilia.com/category/ita/)

## [EDR lab: piccolo self-test #1](https://roccosicilia.com/2024/08/10/edr-lab-piccolo-self-test-1/)

Published by

Rocco Sicilia

on

[10 agosto 2024](https://roccosicilia.com/2024/08/10/edr-lab-piccolo-self-test-1/)

[![EDR lab: piccolo self-test #1](https://roccosicilia.com/wp-content/uploads/2024/08/blue-team.png?w=545)](https://roccosicilia.com/2024/08/10/edr-lab-piccolo-self-test-1/)

## Introduzione

Devo fare diverse premesse per questo post e parto dall’inizio. Da circa un paio di anni ho introdotto nei miei security test attività che richiedono di eludere sistemi/servizi di sicurezza, in particolare EDR/IDS e team SOC/MDR. Il tema mi appassiona molto ed ho cercato di approfondire alcune tecniche utili allo scopo, non ho quindi approfondito l’enorme tema dell’evasion degli EDR (argomento fantastico su cui mi sto documentando con calma e nel tempo) ma mi sono limitato a studiare alcune tecniche utili ad aggirare i principali controlli che possono essere attivi sui sistemi operativi client e a livello di sonde di rete.

L’ambito EDR mi aveva particolarmente appassionato ed avevo giocato con piccoli fileless malware da utilizzare in diverse occasioni. In particolare, sempre in riferimento alle mie esigenze operative, ho approfondito un po’ il tema *exfiltration*, *covert channel* e *command and control*. Nei miei lab, alcuni dei quali fatti durante lunghe live su [Twitch](https://twitch.tv/roccosicilia) (archivio oggi disponibile su [Patreon](https://patreon.com/roccosicilia)), ho sperimentato varie tecniche e strumenti tra cui dei framework C2; uno di questi è stato Villain in quanto molto semplice da usare, personalizzabile e di semplice riproduzione, elemento che prendo spesso in considerazione per la parte divulgativa dei miei contenuti.

Sul piano professionale ho sempre fatto notare che gli EDR/XDR hanno bisogno di un certo grado di gestione: questi strumenti sono molto potenti e hanno la capacità di raccogliere una enorme quantità di dati provenienti da logs, telemetrie, eventi esterni, […], ma per funzionare vanno correttamente configurati e gestiti nel tempo. Non mi dilungo perché ne ho parlato veramente tanto e ovunque.

Soprattutto a seguito di diversi miei post su LinkedIn mi è stato chiesto più volte un aiuto a comprendere il grado di maturazione dei più disparati EDR e anti-malware presenti sul mercato. Non sono attrezzato per rispondere a questa domanda in modo completo, ho quindi sempre proposto un minimo di test per comprendere che tipo di telemetria fisse in grado di raccogliere lo strumento e, se presente, che regole di detection fossero presenti o creabili in caso di necessità.

---

Questo post è di accompagnamento al video in cui presento un lab di test per i Patreon Supporter che me lo hanno chiesto, [il video è disponibile sulla mia pagina](https://www.patreon.com/posts/piccolo-self-per-109336393). I post su questo blog sono di pubblico accesso. Se vuoi sostenere la mia ricerca e la mia attività di divulgazione puoi farlo tramite [Patreon](https://www.patreon.com/roccosicilia/membership), per restare aggiornato sui sulle mia attività di ricerca inscriviti al blog:

Digita la tua e-mail…

Iscriviti

---

## Un piccolo caso d’uso

Come dicevo non sono attrezzato per eseguire tutti i test possibili ed immaginabili su un EDR, quello che posso fare è definire dei casi specifici (ad esempio alcune delle tecniche che ho usato in passato) ed eseguire un semplice test da cui trarre delle conclusioni parziali e che ci possano aiutare a valutare ulteriori approfondimenti.

Parto da ciò che mi mette in difficoltà quando agisco su un endpoint: visto che tendenzialmente cerco di sfruttare *powershell* sulla macchina attaccata per eseguire diverse attività, ho pensato di **prendere una delle azioni più rumorose ed eseguirla in presenza di diversi EDR**. L’azione, nello specifico, è l’avvio di una sessione TCP verso un mio sistema C2 tramite Villain: la classica reverse shell. L’idea è di eseguire l’azione in due diverse modalità e vedere come si comporta l’EDR attivo sul sistema, in base agli esiti ognuno di noi deve fare delle valutazioni di merito sulla propria soluzione.

Nel video spiego il dettaglio dell’attività. Non voglio fare l’ennesimo tutoria su Villain (cosa che tra l’altro [avevo in parte fatto qui](https://www.patreon.com/posts/villain-c2-e-dei-99670954)), mi limito a darvi gli elementi per eseguire in autonomia il test.

Dotatevi di una macchina da usare come C2 su cui installare ed avviare Villain. Per rendere il tutto più interessante e realistico suggerisco una istanza pubblica in modo da avviare la sessione verso il C2 tramite internet, possibilmente attraverso il vostro firewall di perimetro (su questo tema ci torniamo con il secondo lab).

Il primo test è semplicissimo: generate il payload di vostro gradimento (io ho usato powershell\_iex che fa esplicito uso di Invoke-Expression) ed utilizzatelo sulla macchina in cui avete predisposto il vostro EDR. Osservate cosa succede.

Qualche nota:

* praticamente tutti i payload di Villain, se usati in versione *vanilla*, sono intercettati anche dal “solo” Microsoft Defender, in particolare dalla funzione real-time protection
* da un test eseguito recentemente Microsoft Defender interviene all’avvio della reverse shell, in caso di bypass della funzione la reverse shell si avvia ed a runtime non vengono eseguite mitigation

Se il vostro EDR non blocca l’azione, prima di strapparvi le vesti accertiamoci di vedere la telemetria raccolta. Ci sono due possibili scenari: la telemetria c’è ma non ci sono regole per la detection di questo tipo di eventi, oppure non c’è telemetria sull’evento.

Nel primo caso potremmo dire “bene ma non benissimo”: possiamo creare nelle regole di detection sulla base della telemetria osservata ed intercettare questo tipo di eventi… e questo è bane. Dobbiamo considerare che ci sono diversi scenari e tecniche di attacco per le quali dovremmo creare delle regole se il nostro strumento non ne ha di attive “built-in”… e questo non è benissimo, nel senso che bisogna lavorarci, a volte anche molto. Se siamo nel secondo caso – no allarmi, no telemetria – abbiamo un problema. L’utilizzo dei software presenti a bordo macchina per eseguire comandi e fileless malware è una tecnica ampiamente utilizzata dai threat actor, non avere telemetria su questi eventi ci rende ciechi. In questo caso lo strumento che stiamo usando non ci aiuta e dobbiamo seriamente valutare **alternative o aggiunte**.

Va considerato il fatto che non stiamo facendo nulla per “nascondere” la nostra azione offensiva, a differenza dei threat actor che lavorerebbero in modo meno rumoroso. E’ vero che questo tipo di azione richiede un accesso al sistema e quindi l’attacker deve aver guadagnato già una posizione, ma come ho raccontato più volte dobbiamo considerare la possibilità di accedere ai locali del target (ogni tanto racconto qualche aneddoto proveniente dal mondo del red teaming) e tutti i possibili effetti collaterali dell’avere reti popolate da sistemi che entrano ed escono dall’azienda: in cima alla lista ci sono i laptop dei collaboratori che possono essere “compromessi” in diverse circostanze. Questo è un altro capitolo del mondo offensive, ci tornerò.

## Un pelo più stealth

Lo stesso payload utilizzato nel primo test possiamo renderlo meno identificabile applicando un po’ di offuscamento nel nostro *comandone powershell*. Ci sono diversi strumenti e tecniche che potete provare, a tito...