---
title: Dio Mythos e la sua gabbia d’acciao: nerfing, allineamento e guardrails
url: https://mgpf.it/2026/07/03/l-dio-mythos-e-la-sua-gabbia-dacciao-nerfing-allineamento-e-guardrails.html
source: LastKnight.com Feed
date: 2026-07-03
fetch_date: 2026-07-04T05:49:49.666684
---

# Dio Mythos e la sua gabbia d’acciao: nerfing, allineamento e guardrails

[![Matteo Flora](https://mgpf.it/wp-content/uploads/2022/07/MatteoFlora.thinks-1.png)](https://mgpf.it/)

* [CHI SONO](https://matteoflora.com/)
* [English](https://en.mgpf.it/)

# Dio Mythos e la sua gabbia d’acciao: nerfing, allineamento e guardrails

di [Matteo Flora](https://mgpf.it/author/mgpf)

In [Uncategorized](https://mgpf.it/category/uncategorized-it)

9 ore ago

16 min

[aggiungi commento](https://mgpf.it/2026/07/03/l-dio-mythos-e-la-sua-gabbia-dacciao-nerfing-allineamento-e-guardrails.html#respond)

D

![](https://mgpf.it/wp-content/uploads/2026/07/dio_small-1024x512.jpg)

Chi ha passato le ultime settimane a scrollare le community di sviluppatori e power user avrà visto tornare, con la puntualità di una liturgia, la solita accusa: Anthropic ha **«nerfato», “instupidito”** *(ma ne parliamo più avanti con la definizione)* i suoi ultimi modelli. Il caso più chiacchierato è quello di **Fable 5**: appena ri-rilasciato al pubblico ha mostrato **paletti evidenti su alcune categorie di richieste**, e a caldo un pezzo di pubblico ha letto quei paletti come un cedimento politico o forse commerciale, chissà. Il caso Fable si è chiuso in pochi giorni con un’ammissione secca dell’azienda: quel giro di guardrail, paratie di sicurezza, nascosti, pensati per contrastare tentativi di *distillation* (l’estrazione sistematica di output usati per addestrare modelli concorrenti, ma se mi leggete era [il tema della scorsa settimana](https://mgpf.it/2026/06/27/distillazione-ai-cosa-e-rubare.html)…), stava degradando **anche risposte legittime**, e quindi è stato ritirato. Su questo, Anthropic ha ragione a chiedere scusa, e i critici avevano un punto.

Sotto quel caso specifico, però, c’è un dibattito più profondo che vale la pena estrarre dal rumore. La scelta strutturale di Anthropic, quella che resta anche dopo il mea culpa su Fable, è di bloccare a monte, con guardrail difficili da negoziare, due categorie di richieste molto specifiche: quelle relative alla creazione di agenti biologici pericolosi e quelle relative allo sviluppo di codice offensivo per attacchi informatici. È questa la scelta che vale la pena difendere, e per farlo occorre prendere sul serio due parole che circolano spesso nei titoli e quasi mai nei ragionamenti: **allineamento** e **guardrail**.

### Cosa vuol dire davvero “nerfing” (e cosa in molti hanno frainteso)

Partiamo dai fatti: la polemica di Fable riguardava un guardrail invisibile, il modello continuava a rispondere, ma le sue risposte peggioravano *silenziosamente* quando il sistema sospettava un pattern di distillation. È una scelta di **prodotto**, non di **sicurezza** in senso stretto, e Anthropic ha correttamente riconosciuto che quel modo di implementarla era sbagliato. Il punto interessante è che quel guardrail non era mai stato il vero problema per chi lavora seriamente sull’AI: i guardrail che davvero contano sono altri, e sono quelli che si attivano quando la richiesta orbita attorno alla **sintesi di patogeni**, all’ottimizzazione di **attacchi informatici**, allo sviluppo di **malware in produzione**.

Anche in quel caso, va detto subito, la parola *nerfing* è ingannevole: quei paletti non sono definitivi, non sono un cancello con la serratura buttata via, sono un filtro che si può negoziare. Il feedback dell’utente, se argomentato, se documentato, se accompagnato da un contesto legittimo (una ricerca accademica, un progetto di *biosecurity*, un *pentest* autorizzato, un lavoro di *red team* corporate), è lo strumento con cui **si sblocca quel filtro sul singolo caso**. Non è un porto di guerra: è un’ostruzione mobile che si sposta se qualcuno si prende la responsabilità di argomentare perché va spostata. Chi si è indignato perché il modello «non lo lascia fare» ha, nella grande maggioranza dei casi, saltato il passo del feedback e ha preso il primo rifiuto come una sentenza.

Il che ci porta al vero cuore del problema: perché quel filtro esiste, come è fatto, e perché quelle due aree e non altre.

### L’allineamento, in una frase che si capisce

L’allineamento è il tentativo di far sì che un modello di intelligenza artificiale, o *Large Language Model* nella dicitura tecnica, faccia quello che vogliamo che faccia, **e non altro**. Detta così sembra banale; non lo è, e il motivo per cui non lo è è il problema più studiato dell’ultima decade nella ricerca sull’AI di frontiera. Il modello, per come è costruito, non sa cosa vogliamo: sa solo predire qual è la prossima parola più probabile a partire da un contesto. Tutto il resto, educazione, prudenza, rispetto delle regole, è una **vernice che gli si dà sopra** con l’addestramento, ed è una vernice che copre bene ma non sempre allo stesso modo.

Il caso archetipico si trova nel libro di **Nick Bostrom**, [*Superintelligence: Paths, Dangers, Strategies*](https://global.oup.com/academic/product/superintelligence-9780199678112) (Oxford University Press, 2014): un modello a cui si dà l’obiettivo di massimizzare la produzione di graffette, se abbastanza potente, finirà per convertire l’intero pianeta in graffette, ed è la storia che nel gergo tecnico ha preso il nome di *paperclip maximizer*. Il modello ha fatto proprio quello che gli è stato chiesto; siamo stati noi a chiedere la cosa sbagliata. **Stuart Russell**, professore di computer science a Berkeley, ci ha costruito sopra un libro intero, [*Human Compatible: AI and the Problem of Control*](https://people.eecs.berkeley.edu/~russell/hc.html) (Viking, 2019), sostenendo che l’unica via d’uscita è progettare macchine che siano *incerte* rispetto ai nostri valori e che chiedano conferma prima di agire. È una posizione forte, controversa, ma cattura il nodo: il problema non è insegnare al modello cosa vogliamo, il problema è che noi stessi non sappiamo scriverlo in modo abbastanza preciso.

Anthropic, nel 2022, ha provato a dare una risposta concreta con la *Constitutional AI*, descritta nel paper di **Yuntao Bai** e colleghi, [*Constitutional AI: Harmlessness from AI Feedback*](https://arxiv.org/abs/2212.08073) (dicembre 2022): al modello si dà una specie di codice etico scritto in linguaggio naturale, una *constitution* di una decina di principi, e lo si addestra a criticare e revisionare le proprie risposte rispetto a quella. È un approccio elegante, in gran parte trasparente, e ha il pregio di rendere ispezionabile il fondamento morale del sistema, cosa che i concorrenti fanno molto meno. Ma la constitution, per quanto raffinata, resta un documento scritto da esseri umani con opinioni, priorità e punti ciechi (tantissimi): è la **miglior toppa** che oggi sappiamo mettere, non la **soluzione definitiva**, ed è un limite che dovremo tenere a mente nella sezione conclusiva.

### I guardrail, ovvero come si dice di no a una macchina che non ha morale

Se l’allineamento è la vernice generale, i guardrail sono i **cartelli di divieto piazzati nei punti in cui la vernice, statisticamente, potrebbe screpolarsi** con conseguenze gravi. Non sono censura, non sono etica, non sono giudizio morale: sono **ingegneria del rischio** applicata al comportamento di un sistema probabilistico.

Il modello, sotto il cofano, è una macchina che ragiona per associazioni statistiche: gli chiedete una cosa, lui prende quello che ha visto in fase di addestramento, ricombina, restituisce. Se in fase di addestramento ha visto milioni di manuali di sintesi organica, protocolli di laboratorio, procedure di *dual-use research (metodi usati SIA in contesto civile che offensivo/militare)*, quello che sa fare non è **distinguere il chimico curioso dal terrorista** con dottorato: è produrre passaggi plausibili di sintesi. Il modello non ha morale né intento, e nemmeno la capacità di leggere il contesto sociale della richiesta; ha solo la sua distribuzione di probabilità, e il guardrail interviene proprio lì, prima che quella distribuzione sputi fuori un pezzo di catena di sintesi.

Ci sono due modi di implementare un guardrail. Il primo è *post-hoc*: si ...