---
title: Speedrunning the Cyber Kill Chain
url: https://roccosicilia.com/2025/11/06/speedrunning-the-cyber-kill-chain/
source: Over Security - Cybersecurity news aggregator
date: 2025-11-06
fetch_date: 2025-11-07T03:11:35.303185
---

# Speedrunning the Cyber Kill Chain

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/progetto-di-divulgazione/)
* [Sostieni il progetto](https://roccosicilia.com/sostieni-il-progetto/)
* [English version](https://medium.com/%40roccosicilia)

[cyber security](https://roccosicilia.com/category/cyber-security/), [hacking](https://roccosicilia.com/category/hacking/), [ita](https://roccosicilia.com/category/ita/)

## [Speedrunning the Cyber Kill Chain](https://roccosicilia.com/2025/11/06/speedrunning-the-cyber-kill-chain/)

Published by

Rocco Sicilia

on

[6 novembre 2025](https://roccosicilia.com/2025/11/06/speedrunning-the-cyber-kill-chain/)

Questo post esce poco dopo rispetto alla mia presentazione al [**Cyber Security Day organizzato da ATED il 29 ottobre a Lugano**](https://ated.ch/). Il workshop che ho presentato aveva l’obiettivo di illustrare in modo pratico ed in 30 minuti – anzi 25 🙂 l’organizzazione ed il mitico [Luca Mauriello](https://www.linkedin.com/in/luca-mauriello/) sono stati molto chiari oltre che **fantastici nella preparazione di questo evento** – il modo in cui ragionano i *bad actor* in determinate fasi dell’azione di attacco con particolare riferimento alle fasi di Delivery di un payload per la ottenere un primo canale di comunicazione con il target. Come si può intuire 25 minuti sono pochi, da questo deriva il titolo per workshop e per questo motivo ho pensato di dedicare un post di approfondimento tecnico e relativo video dimostrativo.

[![](https://roccosicilia.com/wp-content/uploads/2025/11/image-2.png?w=1024)](https://www.patreon.com/posts/usb-rubber-ducky-142968206)

Nota: il post contiene tutti i dettagli operativi mentre il video è la sintesi del funzionamento con demo che metto a disposizione per i sostenitori su Patreon.

## Point of view

Per questo post, come abbiamo fatto durante il workshop, dobbiamo metterci il cappello del threat actor e cambiare punto di vista. Dobbiamo osservare la nostra organizzazione come il nostro prossimo target. Un metodo che ho trovato utile nella preparazione di un security test è scomporre il target in tre macro elementi: *infrastruttur*e, *tecnologie*, *persone*. Se il mio obiettivo è trovare un modo per accedere ad informazioni o sistemi del target e non c’è motivo per non considerare tutte le possibili “dimensioni” come farebbe un bad actor: è possibile valutare un accesso fisico alle infrastrutture o un accesso logico grazie alle tecnologie in uso e/o grazie al fattore umano sfruttando eventuali errori di personale che fa parte dell’organizzazione target.

Vi faccio qualche esempio di cosa significa valutare un accesso fisico. Quando vi recate in un ufficio o ad uno sportello di vario genere in cui è previsto che voi vi sediate di fronte al desk di qualcuno, è molto probabile che, dal vostro punto di vista, il *case* della workstation della persona con cui parlate mostri le porte di I/O sul vostro lato.

![](https://roccosicilia.com/wp-content/uploads/2025/10/gemini_generated_image_43fm0e43fm0e43fm.png?w=1024)

Immagine generata con cavi un po’ a caso.

In molti contesti, se prendiamo in considerazione le “tradizionali” strutture aziendali, spesso nelle sale riunioni sono presenti dispositivi usati per i sistemi di videoconferenza o punti di accesso alla rete, in alcuni casi integrati nell’arredo (talvolta in appositi vani dei tavoli). Molte strutture preferiscono le torrette a pavimento, vani in cui vengono portati gli accessi alla rete cablata e le prese elettriche. Il fatto importante è che di punti di accesso ce ne sono molti nel mondo fisico ed è relativamente semplice sfruttarli se si ha modo di accedere ai locali. Nel caso del nostro *case* (l’immagine poco sopra) e le relative porte di I/O, come le porte USB, questa posizione ci mette nelle condizioni di infilare una nostra chiavetta nel PC del target.

Ora tutti (o quasi) diranno qualcosa tipo “*ah be… noi abbiamo le porte USB disabilitate*” oppure “*abbiamo l’anti-malware / EDR che blocca tutto*“. È molto positivo che siano state prese queste precauzioni, ma va considerato che il fatto che un *device* abbia la forma di una tipica chiavetta USB non significa che sia un USB storage. Inoltre, avere un EDR non significa – purtroppo – bloccare a prescindere qualsiasi minaccia.

## Un esempio pratico

#### Preparazione

Ci sono diversi approcci che si possono valutare, supponiamo di voler sondare la strada meno battuta e considera – almeno per ora – e che richiede un’azione *onsite*: l’obiettivo è compromettere una delle workstation della sede al fine di ottenere un primo punto di presenza all’interno della struttura target. In parole povere dobbiamo lanciare un nostro malware su un sistema client.

Ragioniamo su come – *in qualità di security tester* – potremmo agire: dobbiamo far in modo di eseguire qualcosa sulla macchina target. In questo esempio ci accontentiamo di una variante del mio piccolo [esperimento C2](https://github.com/roccosicilia/http_c2) che, grazie ad una serie di richieste http, è in grado di gestire il *beaconing* e la comunicazione tra client e server.

C2 demo

La scelta del payload da utilizzare è uno step tecnicamente abbastanza complesso: dobbiamo dare per scontato che sulla macchina target ci siano sistemi di controllo in grado di intercettare e bloccare eventuali malware.

![](https://roccosicilia.com/wp-content/uploads/2025/10/image-3.png?w=1024)

L’esempio completo per Rubber Ducky è [disponibile qui](https://github.com/roccosicilia/rootstash/blob/main/c2/demo_rubber_ducky/macro_reverse_shell.txt).

Il comando qui sopra apre una sessione TCP verso la porta 8888 della mia VPS dove è stato predisposto il più semplici dei *server* netcat per ricevere la sessione attraverso la quale è possibile interagire con la shell della macchina target. Come accennavo, nello scenario che vorrei argomentare ci spingiamo un pelo oltre ed andiamo a tentare di attivare una comunicazione con un nostro C2.

Abbiamo già discusso [in questo video](https://www.youtube.com/watch?v=eRJiM7smEpY) il concetto di detection gap e le motivazioni che rendono un semplice payload in python meno sospetto di simili payload in powershell. Dobbiamo però fare in modo di poter eseguire il payload in questione e non è assolutamente detto che la macchina target abbia python installato. Una possibile via potrebbe essere l’esecuzione di alcune operazioni preliminari per predisporre il sistema target.

![](https://roccosicilia.com/wp-content/uploads/2025/11/image.png?w=1024)

Porzione del payload utilizzato via USB Rubber Ducky.

Andiamo con ordine ed inizio col segnalare che i DELAY inseriti sono solo estetici per capirci qualcosa in esecuzione e possono essere enormemente ridotti. Il primo vero comando è la combo **Win+r** che apre l’applicazione **run.exe** che in questo caso sfruttiamo solo per ottenere un **powershell** prompt. A questo punto chiediamo al sistema di installare python3:

```
winget install Python3 --silent --accept-source-agreements
```

Questo comando fa sempre discutere molto e la domanda che giustamente viene posta è: “*come è possibile che python si possa installare in questo modo se gli utenti non hanno privilegi elevati?*“. Grazie alle funzionalità messe a disposizione dal Microsoft Store è possibile installare App senza privilegi elevati all’interno del profilo utente, è quindi poi possibile, per l’utente, eseguire python-script dal proprio profilo. Questo comando precede quindi l’avvio dello script che si troverà python3 installato ed utilizzabile dalla CLI. Come si vede dalla macro viene anche installata una libreria indispensabile per il payload: *requests*.

#### Breve approfondimento sulla USB Rubber Ducky

Il device deve essere “programmato” con la macro di cui abbiamo discusso e per fare questo bisogna utilizzare un tool che esegua la compilazione di quanto scritto.

![](https://roccosicilia.com/wp-content/uploads/2025/...