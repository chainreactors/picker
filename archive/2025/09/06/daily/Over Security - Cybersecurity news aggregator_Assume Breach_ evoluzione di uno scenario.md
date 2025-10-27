---
title: Assume Breach: evoluzione di uno scenario
url: https://roccosicilia.com/2025/09/05/assume-breach-evoluzione-di-uno-scenario/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-06
fetch_date: 2025-10-02T19:45:14.653742
---

# Assume Breach: evoluzione di uno scenario

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/progetto-di-divulgazione/)
* [Sostieni il progetto](https://roccosicilia.com/sostieni-il-progetto/)
* [English version](https://medium.com/%40roccosicilia)

[cyber security](https://roccosicilia.com/category/cyber-security/), [hacking](https://roccosicilia.com/category/hacking/), [ita](https://roccosicilia.com/category/ita/)

## [Assume Breach: evoluzione di uno scenario](https://roccosicilia.com/2025/09/05/assume-breach-evoluzione-di-uno-scenario/)

Published by

Rocco Sicilia

on

[5 settembre 2025](https://roccosicilia.com/2025/09/05/assume-breach-evoluzione-di-uno-scenario/)

[![Assume Breach: evoluzione di uno scenario](https://roccosicilia.com/wp-content/uploads/2025/01/coding.png?w=562)](https://roccosicilia.com/2025/09/05/assume-breach-evoluzione-di-uno-scenario/)

Sto preparando una breve presentazione di un ipotetico scenario di test nella modalità Assume Breach e ne approfitto per scrivere due righe in merito… qualche dettaglio sull’esperienza ve lo racconto su [Patreon, come sempre nei miei “***dietro le quinte***“](https://www.patreon.com/c/roccosicilia/posts?filters%5Btag%5D=dietro+le+quinte).

La presentazione sarà in inglese ma per questo post mantengo l’italiano, eventualmente lo traduco per la mia pagina su [Medium](https://roccosicilia.medium.com/).

#### Preparazione dello scenario

Quando si affronta un test in questa modalità è bene definire degli assunti che poi potranno essere verificati su campo. Nel mio scenario si assume che:

* il target/client mette a disposizione un riferimento interno coinvolto nelle attività di test che dovrà essere escludo da eventuali path di escalation
* il test partirà da una workstation a cui il Threat Actor ha accesso con una credenziale valida, non sono quindi in *scope* le azioni che hanno portato l’attaccante in possesso delle credenziali
* il test viene eseguito mantenendo i sistemi di detection attivi ed eventuali servizi di monitoraggio (MDR/SOC) all’oscuro dell’attività
* il test prevede l’esplorazione della rete target ed azioni anche su altri sistemi, non esiste un preciso scope o vincoli se non definiti in anticipo

Prima di eseguire le attività onsite è opportuno raccogliere dati, da fonti pubbliche, sulla corporate: potrebbe essere utile identificare eventuali tecnologie in uso come Firewall, EDR ed eventuali software utilizzati sui client. Questa fase può dare spunti interessanti: identificare eventuali software in uso dal target permette di valutare attack path specifici per il contesto.

![](https://roccosicilia.com/wp-content/uploads/2025/08/image-18.png?w=720)

Guardando alla Cyber Kill Chain così come solitamente la definiamo (oggi prendo in prestito una slide Cisco), le fasi che considero in questo scenario sono quindi la Reconnaissance per poi saltare all’Exploitation e da li seguire le fasi successive.

#### Esecuzione del C2

Il focus della mia presentazione è l’avvio di una sessione di comunicazione con il mio C2 senza farsi intercettare/bloccare da Firewall, IDS ed EDR e da questa posizione eseguire azioni esplorative all’interno della rete. Il mio attuale modo di operare (2025) non è lo stesso che utilizzavo quando ho iniziato a lavorare in modo strutturato a questa tipologia di test (2019-2020), penso sia utile raccontare almeno i principali step del processo che ha portato all’attuale risultato, a prescindere dagli esiti delle singole evoluzione che hanno una valenza legata al periodo di utilizzo, concetto che spiego meglio durante il post.

Tempo fa utilizzavo semplici sessioni tcp o http per aprirmi delle comode reverse shell scritte per lo più in Powershell, con un po’ di furbizia ed *obsuscation* si riusciva ad ingannare AMSI e anche molti EDR. Powershell era/è spesso disponibile sui sistemi target senza particolari limiti e bastavano poche macro ed una USB rubber ducky per ottenere risultati. Ho anche fatto uso di infrastrutture C2 note come *Covenant* ma un bel giorno approdai su *Villain* (ne ho parlato spesso su questo blog) ed ho iniziato a lavorare su varianti dei payload “compatibili” con questo framework.

![](https://roccosicilia.com/wp-content/uploads/2025/08/screenshot-2025-08-28-at-09.18.24.png?w=1024)

Due esempi di payload generati con Villain

Se analizziamo il codice generato si nota la meccanica di funzionamento di questi payload e, se si *bazzica* un po’ il mondo dei C2, il modello risulterà molto familiare. Se indentiamo il codice si capisce subito cosa sta accadendo:

![](https://roccosicilia.com/wp-content/uploads/2025/08/image-19.png?w=1024)

L’esempio precedente ma leggibile

La variabile *$v* contiene il risultato di una *Invoke-RestMethod* (una chiamata *http get*) verso una URL che nel mio script corrisponde all’indirizzo del C2 a cui vengono passare delle informazioni tramite le stesse stringhe inserite in URL: l’identificativo della sessione *aa0471*, l’*hostname* e lo *username*. Questa informazione serve al server Villain per “mappare” la sessione.

Il *core* del funzionamento è il ciclo *for()*: ad ogni iterazione lo script esegue una prima *Invoke-RestMethod* con cui chiede al server il comando da eseguire (variabile *$c*), successivamente il comando viene eseguito localmente tramite *Invoke-Expression $c* (output in variabile *$r*) ed il risultato viene infine inviato al server con una *http post* che nello script è l’ultimo *Invoke-RestMethod […] -Method POST*.

---

Se trovi utili i miei contenuti ed il lavoro di ricerca che svolgo e condivido puoi supportarmi iscrivendoti ad uno dei miei canali come [il mio Patreon](https://patreon.com/roccosicilia).

Se vuoi rimanere aggiornato su prossimi articoli e video puoi iscriverti a questo blog:

Digita la tua e-mail…

Iscriviti

Da qualche giorno è attivo anche un subreddit per discutere dei temi che tratto abitualmente: *[r/SheliakNotes](https://www.reddit.com/r/SheliakNotes/)*.

---

Fortunatamente le capacità di detection di AMSI e degli EDR si sono rapidamente adeguate, oggi (e già dal 2023) la telemetria di uno script Powershell che innesca un ciclo come quello descritto genera una istantanea reazione di AMSI e, se per qualche ragione si riesce ad aggirare il controllo locale, ci pensa l’EDR ad intercettare e riconoscere la sequenza di comandi come un pattern sospetto. Le regole di detection di molti EDR (in configurazione di dafault) sono però legate al contesto Powershell ed all’intercettazione di specifiche sequenze di comandi come una ***curl*** seguita da una ***iex***.

Regole di detection troppo precise sono facilmente aggirabili in quanto è sufficiente alterare a sufficienza le componenti del pattern per non consentire all’EDR di intercettare l’azione pur ottenendo lo stesso risultato. Un tipico esempio è l’utilizzo di utility di sistema “alternative” per eseguire una *http get*: [collection come quelle di ***LOLBAS*** ci hanno insegnato ad usare ***certutil.exe***](https://lolbas-project.github.io/lolbas/Binaries/Certutil/) (grande classico) per eseguire il download di un contenuto.

Chi lavora su questi temi ad alto livello solitamente implementa regole di detection in grado di tener conto di questi tricks, cosa che ovviamente pone dei limiti a chi fa security test (gente come me) ed anche ai Threat Actor.

#### Nuova strategia

> Ma allora come fanno i Threat Actor ad aggirare le regole di detections?

Devo premettere che non so quanto sia merito dei Threat Actor e quanto sia merito dei ricercatori. Quando ho cercato info sul tema sono risalivo a talk (DEFCON e BlackHat) in cui si parla aggirare i sistemi di controllo con diverse tecniche e si fa riferimento a Python, Go e Rust sia per implementare tecniche di evasione che per sfruttare i *Detection GAP*, ovvero la mancanza di regole di detection utili a riconoscere l’evoluzione di alcune minacce. Nel 2023 ho iniziato a lavora seriamente sul conce...