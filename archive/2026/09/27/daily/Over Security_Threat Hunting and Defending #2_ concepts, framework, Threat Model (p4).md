---
title: Threat Hunting and Defending #2: concepts, framework, Threat Model (p4)
url: https://roccosicilia.com/2026/09/27/threat-hunting-and-defending-2-concepts-framework-threat-model-p4/
source: Over Security
date: 2026-09-27
fetch_date: 2026-09-28T07:56:50.398568
---

# Threat Hunting and Defending #2: concepts, framework, Threat Model (p4)

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/divulgazione/)
* [Progetti](https://roccosicilia.com/progetti/)
* [Conferenze](https://roccosicilia.com/conferenze/)

[cyber security](https://roccosicilia.com/category/cyber-security/), [ita](https://roccosicilia.com/category/ita/), [study with me](https://roccosicilia.com/category/study-with-me/)

## [Threat Hunting and Defending #2: concepts, framework, Threat Model (p4)](https://roccosicilia.com/2026/09/27/threat-hunting-and-defending-2-concepts-framework-threat-model-p4/)

Published by

Rocco Sicilia

on

[27 Settembre 2026](https://roccosicilia.com/2026/09/27/threat-hunting-and-defending-2-concepts-framework-threat-model-p4/)

![](https://roccosicilia.com/wp-content/uploads/2026/09/image-1.png)

1. [Intro](#intro)
2. [PASTA](#pasta)
3. [DREAD](#dread)
4. [Conclusioni](#conclusioni)

## Intro

Devo un po’ accelerare con lo studio anche perché mi si è sovrapposta un’altra certificazione 🙂

Chiuso il giro su questa parte con il Threat Modeling, argomento che ricorre in diverse discipline oltre al Threat Hunting. Solo per fare un esempio: quando si discute di un potenziale scenario di attacco sulla base delle debolezze di una infrastruttura stiamo di fatto “modellando la minaccia”. Nel mondo “offensive” questo porta alla valutazione dei path di attacco efficaci e lo stesso ragionamento consente di valutare gli effettivi rischi di una minaccia, almeno su carta, e di definire delle priorità.

Il Threat Modeling consente di comprende meglio il contesto delle minacce che realisticamente possono interessare la nostra organizzazione e di conseguenza ci consente di valutare delle azioni correttive in modo efficiente e concentrandoci sugli effettivi rischi.

Ci sono diversi modelli presi in considerazione dal materiale del corso e quello su cui pare si punti maggiormente, almeno in questo corso, è PASTA: **Process of Attack Simulation and Threat Analysis**. Devi dire che il nome è esplicativo e si avvicina molto al mio modo di lavorare e la cosa ovviamente mi piace 🙂

## PASTA

Il modello consente di:

* individuare potenziali debolezze e path di attacco
* definire una priorità sulla base di probabilità di successo e impatto della minaccia
* definire una strategia di remediation effettiva/operativa

Il modello si sviluppa in sette stage molto strutturati:

1. **Definizione degli obiettivi** – va definito un contesto di rischio in cui eseguire l’analisi e per questo servono informazioni precise sul modello di business del target, sulla struttura operativa, sulle politiche di sicurezza e compliance, ecc. L’output di questo stage comprende l’elenco delle applicazioni/funzioni interessanti, l’elenco dei potenziali obiettivi di business, i requisiti di sicurezza delle applicazioni/funzioni interessate ed una business impact analysis. In parole povere va capito e documentato come il target (l’azienda o l’ente) funziona veramente e quali sono gli “ingranaggi più grossi”.
2. **Definizione del perimetro tecnico (technical scope)** – Sulla base dell’analisi fatta vanno identificati gli assets tecnologici che fanno capo alle funzioni fondamentali del target. In questa fase è utile prendere in considerazione documentazione tecnica specifica e tutte le informazioni relative alla funzionamento dei sistemi coinvolti con particolare attenzione alla catena delle dipendenze.
3. “**Destrutturazione**” – I sistemi che si è deciso di portare nel perimetro dell’analisi vanno analizzati come se fossero un aggregato di funzioni, vanno quindi schematizzati in un workflow funzionale in cui sia chiara la funzione e gli eventuali rischi associati.
4. **Analisi delle minacce (threats)** – Lo schema prodotto viene sottoposto ad un’analisi delle effettive minacce che possono interessare le tecnologie e le funzioni individuate. Le valutazioni devono considerare la probabilità che una determinata minaccia abbia effetto considerando anche report di terze parti sullo scenario delle minacce globali, va quindi tenuto conto anche del contesto oltre che della struttura tecnica (“il contesto fa tutta la differenza”, cit.).
5. **Analisi delle vulnerabilità** – L’analisi delle minacce richiede una precisa verifica delle vulnerabilità software e logiche e la loro qualifica in termini di sfruttabilità, asset e funzioni coinvolte, mappatura del rischio effettivo, capacità di detection, …
6. **Analisi dell’attacco** – Sulla base delle analisi fatte va identificata una chain di attacco realistica e va dimostrata tecnicamente e praticamente la sua efficacia. L’attacco va quindi effettivamente strutturato ed eseguito tramite azioni simulate al fine di appurarne l’efficacia.
7. **Analisi di rischio e impatto** – L’esercizio si chiude con un report di analisi dei rischi ed i relativi impatti in cui devono essere riportati le minacce che rappresentano un effettivo rischio e gli assets correlate ed una strategia di mitigation concreta che non si limiti a dire cosa va “aggiornato” ma che vada a definire azioni operative specifiche come nuovi controlli da attuare, design deboli da migliorare, tecnologie da implementare o potenziale, …

La fase 6 della metodologia è per me un punto chiave: come si è forse notato da mie recenti “annotazioni” credo che le skills di chi si occupa di sicurezza offensiva e security test possano essere molto utili nella pratica del threat hunting in quanto è richiesta una buona dose di “mindset” orientato all’attacco.

Nel mio ambito di lavoro questo modello è estremamente utile e costituisce la base di molte attività di analisi anche grazie alla sua somiglianza con il processo che utilizzo per preparare le mie sessioni di security test.

## DREAD

Damage, Reproducibility, Exploitability, Affected users, Discoverability (DREAD) è un framework sviluppato da Microsoft che ha come focus la gestione delle priorità nei rischi di sicurezza nel contesto dello sviluppo software.

La struttura è molto diversa rispetto a PASTA e si basa essenzialmente sull’assegnazione di un punteggio ai vari temi citati e che rapidamente riassumo:

* **Damage** – Quanto impatto viene ipotizzato, in termini economici, al business. Si applicano i seguenti score: 0 (nessun danno), 4 (information disclosure), 6 (compromissione dati non sensibili), 8 (compromissione dati amministrativi non sensibili), 10 (potenziale distruzione di dati o compromissione di funzioni).
* **Reproducibility** – La probabilità che la minaccia/faccia sia effettivamente sfruttabile in termini di quanto poco complessa è da sfruttare. Si applicano i seguenti score: 0 (impossibile o molto complesso), 4 (complesso), 8 (semplice), 10 (molto semplice)
* **Exploitability** – Il livello tecnico, in termini di skills, per sfruttare la falla. Si applicano i seguenti score: 3 (camacità avanzate di programmazione e skills tecniche), 5 (conoscenza di tools di attacco), 9 (utilizzo di proxy web), 10 (utilizzo di browser).
* **Affected users** – Abbastanza evidente, si applicano i seguenti score: 0 (no users), 2 (singolo utente), 6 (più utenti), 8 (utenze amministrative), 10 (tutti gli utenti).
* **Discoverability** – Potremmo sintetizzarlo nel parametro che identifica quanto è semplice da individuare la falla e si applicano i seguenti score: 0 (molto difficile), 5 (moderato), 8 (semplice), 10 (molto semplice).

## Conclusioni

Questa parte del programma, pur essendo molto teorica, consente di affrontare il tema in modo strutturato. PASTA è sicuramente un framework da prendere a riferimento e mi ha permesso di arricchire il modello che oggi utilizzo nella mia fase di Threat Modeling relativa alla preparazione di un security test.

Mentre studiavo ragionavo anche sulla possibilità di arricchire i miei strumenti di analisi con nuove funzioni utili alla raccolta delle informazioni: come per attività come OSInt anche questa attività richiede di analizzare molti dati e correlare info...