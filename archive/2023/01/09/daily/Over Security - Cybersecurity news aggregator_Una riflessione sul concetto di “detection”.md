---
title: Una riflessione sul concetto di “detection”
url: https://roccosicilia.com/2023/01/08/una-riflessione-sul-concetto-di-detection/
source: Over Security - Cybersecurity news aggregator
date: 2023-01-09
fetch_date: 2025-10-04T03:21:45.932569
---

# Una riflessione sul concetto di “detection”

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/progetto-di-divulgazione/)
* [Sostieni il progetto](https://roccosicilia.com/sostieni-il-progetto/)
* [English version](https://medium.com/%40roccosicilia)

[cyber security](https://roccosicilia.com/category/cyber-security/), [hacking](https://roccosicilia.com/category/hacking/), [ita](https://roccosicilia.com/category/ita/)

## [Una riflessione sul concetto di “detection”](https://roccosicilia.com/2023/01/08/una-riflessione-sul-concetto-di-detection/)

Published by

Rocco Sicilia

on

[8 gennaio 2023](https://roccosicilia.com/2023/01/08/una-riflessione-sul-concetto-di-detection/)

Come ho avuto modo di raccontare in qualche post su LinkedIn, negli ultimi mesi ho potuto dialogare con molti attori, italiani e non, del mondo MDR. Per i non addetti ai lavori: MDR è l’acronimo di Managed **Detection** and **Response** e si riferisce ai servizi di presidio degli eventi di una rete con capacità di intercettare minacce informatiche e reagire per mitigare e/o bloccare l’eventuale compromissione. Potremmo dire che si tratta dall’evoluzione dei più tradizionali servizi di Security Operation Center che hanno sempre avuto il compito di intercettare e segnalare eventuali situazioni di compromissione.

Nel discutere i diversi scenari di applicazione del concetto di **detection** ho notato due approcci che definirei complementari. Va detto che alcuni interlocutori utilizzano entrambi gli approcci mentre altri ne prediligono uno all’altro. Il primo approccio è network-oriented: i dati su cui viene eseguita l’analisi vengono da sonde a livello rete che, potendo osservare il traffico sia a confine che all’interno della struttura, analizzano le conversazioni e, se possibile, i contenuti per scovare eventuali minacce. Il secondo approccio è event-oriented: i dati su cui viene eseguita l’analisi provengono dai logs e dagli eventi registrati dai sistemi della rete che possono inviare informazioni “grezze” o già qualificate (es: allarmi da parte di hosts o altri sistemi).

**[Nota tecnica]** Nella discussione nata su LinkedIn emerge l’esigenza di estendere il dominio dell’approccio event-oriented a ciò che è possibile analizzare a livello kernel dei sistemi operativi grazie a specifici agent. Nel post considero questa fonte assimilabile ad un evento anche se non viene segnalata attraverso i classici servizi di gestione degli eventi ma, solitamente, attraverso un agent.

Non voglio arrivare a conclusioni di preferenza, lo scopo del post è illustrare i due approcci in modo semplice così da farsi un’idea. Le valutazioni di merito vanno fatte caso per caso. Come da titolo il post si limita al concetto di **detection**, mentre per il concetto di **response** valuterò un post dedicato più avanti.

## Detection network-oriented

Alla base di questo modello vi è l’assunto di poter osservare tutto il traffico di rete, sia nord/sud che est/ovest. Di per se questo requisito non è impossibile da rispettare ma in contesti complessi potrebbe non essere così immediato. Per ragionare sul modello a prescindere dalla complessità della rete (tema comunque da non trascurare in fase di analisi) mettiamoci comodi e lavoriamo su uno scenario semplice:

![](https://roccosicilia.com/wp-content/uploads/2022/12/image-3.png?w=1006)

Nota di laboratorio: il lab mette a disposizione uno Standard Virtual Switch (su ESXi 7.x) su cui sono configurati tre Port Group in corrispondenza di tre VLAN (LAN, DMZ, WAN) a simulare una semplice rete.

In questo semplice esempio, facilmente applicabile in contesti con più reti e più apparati, vi è l’esigenza di portare tutto il traffico in visibilità di un oggetto “sonda” che si occuperà di analizzarlo a caccia di eventuali anomalie da segnalare direttamente all’amministratore di rete o, in contesti più complessi e completi, da portare a conoscenza di un sistema centralizzato e presidiato come un SIEM gestito da un security operation center (o altro team dedicato).

Virtualmente, se tutto il traffico fosse presidiato ed accessibile a livello di contenuto, dovremmo aver completa visibilità. E’ opportuno considerare che **nel mondo vero** non è così semplice raccogliere tutto il traffico di una rete. In un contesto multi sede sarebbe necessario predisporre almeno una sonda per sede. Inoltre le reti delle singole sedi possono essere molto complesse e potrebbero quindi richiedere più sonde. Ciò che spesso accade è che **alcune porzioni di traffico non vengono raccolte**.

C’è un altro tema da considerare se approcciamo lo scenario dal punto di vista di un threat actor. Cosa succede se volessimo attaccare una workstation (ws1 nello schema) con un’azione locale e che non transiti necessariamente dalla rete? Ovviamente la detection sarebbe impossibile se non grazie a sistemi che lavorano a livello host. Altro esempio: cosa succede se l’attacker utilizzasse l’host ws1 per inviare dati all’esterno della rete generando traffico verso un servizio in uso dall’organizzazione come OneDrive o Google Drive?

Il modello di per se ha il vantaggio di avete un punto di osservazione molto comodo per quantità di informazioni a cui può accedere e per capillarità. Va necessariamente considerato che non tutti gli attacchi hanno bisogno di transitare dall’infrastruttura di rete del target o potrebbero essere utilizzate tecniche particolarmente *stealth* per rendere l’azione difficile da rilevare.

## Detection event-oriented

Ciò che accade sugli hosts è da diversi anni un tema di interesse: i logs delle security appliance come i Firewall sono sempre stati interessanti ma a questi si sono aggiunti gli eventi dei vari sistemi che popolano le reti. A livello cronologico si è prima svilippato in interesse verso i sistemi server per poi estendere il concetto a tutto ciò che può produrre un log: workstation, sistemi operativi, applicazioni, telefoni e caffettiere connesse alla rete LAN per contare quanti caffè vengono fatti ogni giorno (l’IoT ha avuto i suoi impatti).

Va inoltre aggiunto ciò che è possibile osservare a basso livello, in un mio recente post su LinkedIn si è discusso di quanto sia possibile andare in profondità con l’analisi a livello kernel utilizzando sistemi di controllo (es. EDR) in grado di sfruttare specifici moduli. Metto tutto, un po’ impropriamente, nel calderone della detection event-oriented in considerazione del fatto che si tratta di comportamenti che possiamo osservare a bordo di un sistema e di cui possiamo centralizzare il collecting e l’analisi.

![](https://roccosicilia.com/wp-content/uploads/2022/12/image-4.png?w=1024)

L’approccio consente di avere un elevato livello di controllo sui singoli sistemi che popolano la rete (oltre a rendere possibile l’utilizzo di agent in grado di agire attivamente sui sistemi) ed ha l’ovvio limite di non dare evidenza in relazione a ciò che succede laddove non è stato installato/configurato un agent, spesso integrato a livello di sistema operativo, per inviare le informazioni a un sistema centralizzato in grado di analizzarle, SIEM o simili.

Le due aree non presidiate sono infatti determinate da quei sistemi che non hanno la possibilità di inviare eventi o dai sistemi che hanno la possibilità di connettersi alla rete target ma non sono gestiti centralmente (guest). In questi casi, non potendo riceve eventi direttamente dal sistema, possiamo contare solo su ciò che gli altri “agent” sono in grado di osservare a seguito di movimenti laterali. Azioni complesse ma assolutamente fattibili come un attacco MITM possono essere difficili da individuare in questo contesto. Anche attività di scansione passiva della rete diventano difficili da rilevare e, come per il precedente scenario, l’utilizzo di canali “leciti” e cifrati per comunicare con l’esterno rappresenta un problema dal punto di vista della detection in quanto il SIEM deve avere degli elementi per distin...