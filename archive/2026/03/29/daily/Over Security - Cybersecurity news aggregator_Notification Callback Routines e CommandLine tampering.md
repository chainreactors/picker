---
title: Notification Callback Routines e CommandLine tampering
url: https://roccosicilia.com/2026/03/29/notification-callback-routines-e-commandline-tampering/
source: Over Security - Cybersecurity news aggregator
date: 2026-03-29
fetch_date: 2026-03-30T04:46:49.048785
---

# Notification Callback Routines e CommandLine tampering

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/divulgazione/)
* [Progetti](https://roccosicilia.com/progetti/)

[cyber security](https://roccosicilia.com/category/cyber-security/), [hacking](https://roccosicilia.com/category/hacking/), [ita](https://roccosicilia.com/category/ita/)

## [Notification Callback Routines e CommandLine tampering](https://roccosicilia.com/2026/03/29/notification-callback-routines-e-commandline-tampering/)

Published by

Rocco Sicilia

on

[29 marzo 2026](https://roccosicilia.com/2026/03/29/notification-callback-routines-e-commandline-tampering/)

[![Notification Callback Routines e CommandLine tampering](https://roccosicilia.com/wp-content/uploads/2026/03/screenshot-2026-03-29-at-18.25.43.png?w=1024)](https://roccosicilia.com/2026/03/29/notification-callback-routines-e-commandline-tampering/)

La questione *detection* si comincia a fare interessante a partire da questa funzionalità che – IMHO – fa sembrare il function hooking una modo “grezzo” di approcciare il problema. Ovviamente non è mia intenzione criticare metodi di detection che ci hanno aiutato per anni e continuano ad aiutarci, ma penso sia giusto segnalare il salto che c’è tra le due metodologie.

Va detto che le condizioni per consentire alle metodologie di detection di evolvere, con particolare riferimento alle **funzionalità estese** delle *notification callback routines*, sono state rese disponibili a partire da Windows Vista / Windows Server 2008 in avanti. Prima bisognava necessariamente arrangiarsi con quello che il sistema, che ricordiamo essere un OS chiuso, metteva a disposizione. Da questo punto di vista va riconosciuto a Microsoft di aver fatto – ad un certo punto della storia – la sua parte per rendere il sistema operativo più integrabile con componenti di terze parti.

#### Come funziona la Notification Callback Routines

Come si intuisce dal nome della funzionalità, il sistema operativo può inviare una notifica ad un programma quando un determinato evento si verifica. Questa notifica non riguarda tutti gli eventi e non è inviata indiscriminatamente a tutti i programmi, è possibile per un software “registrarsi” affinché riceva determinate notifiche.

Nel mondo degli EDR significa che il software deve informare il sistema che desidera ricevere notifiche in merito ad eventi di sistema che, come accennato, riguardano una parte di ciò che può avvenire:

* Creazione/terminazione di un processo o di un thread
* Caricamento di immagini (DLL, EXE, driver) in un processo
* Operazioni sul registro
* Pre e post operazioni su handle

Gli EDR tipicamente utilizzano un Kernel Driver che all’avvio chiama l’API di registrazione e passa al Kernel il puntatore alla propria callback. Quindi potremmo dire che – banalizzando all’estremo – l’EDR si registra tra i software che vogliono ricevere una notifica in caso l’evento per i quale si sono registrati si verifichi. Se, come vedremo nella demo, l’EDR si registra per gli eventi legati alla creazione/terminazione di un processo il Kernel chiamerà la callback dell’EDR quando un nuovo processo viene creato o terminato.

È importante sottolineare che questa registrazione avviene a livello di kernel: la callback non è un normale programma in esecuzione, ma codice che gira nello strato più privilegiato del sistema operativo, ovvero in *kernel mode*. Questo è il motivo per cui gli EDR utilizzano un driver e non una semplice applicazione. Ora, a mio modo di vedere **per capire bene questo meccanismo bisogna metterci le mani ed impastare bene**, quindi **proviamo a scriverci il nostro driver per registrare la nostra callback**. Come avevo detto nel precedente articolo anche in questo caso mi baso sugli esempi utilizzati anche in famigerati testi di riferimento per queste tematiche, piegandoli un po’ alle mie esigenze e semplificandoli per “abbassarli” al mio livello di conoscenza di C e della programmazione in ambiente Microsoft.

---

Per non aprire troppe parentesi in questo post in cui mi vorrei concentrare sul tema evasion, ho preparato un’approfondimento sul tema dei windows driver che [pubblicherò su Patreon](https://patreon.com/roccosicilia). Per chi è interessato a costruirsi dei lab “spinti” per lavorare con i concetti di raw-telemetri potrebbe essere un tema utile da approfondire assieme, personalmente sto trovando la tematica molto interessante ed utile alla comprensione profonda del funzionamento degli EDR.

---

Supponiamo di voler implementare una componente del nostro *personal EDR* e di voler essere notificati ogni volta che viene creato un nuovo processo, insieme agli eventuali parametri utilizzati. Il driver che stiamo sviluppando deve quindi registrare una callback tramite *PsSetCreateProcessNotifyRoutineEx()*, così da ricevere notifiche alla creazione dei processi. Questo rappresenta uno degli esempi classici riportati nel famigerato “Evading EDR”.

![](https://roccosicilia.com/wp-content/uploads/2026/03/image-8.png?w=1024)

Il codice è disponibile sulla mia repo [github](https://github.com/roccosicilia) e commentato nell’approfondimento su [Patreon](https://patreon.com/roccosicilia). Oltre al driver scriviamo un altro piccolo *programma* che fa anche un’altra cosa: dialoga direttamente con il driver che abbiamo creato per leggere le informazioni raccolte e scriverle in un comodo logfile così da avere un punto di controllo semplice da consultare (*main.c*).

Nel mio lab ho predisposto i sistemi per poter eseguire i test su Windows 10/11 – rif. compilazione e configurazione per i test nell’approfondimento – ed una volta caricato sulla guest di test (sistema operativo Windows 10) è possibile vederlo all’azione:

![](https://roccosicilia.com/wp-content/uploads/2026/03/image-9.png?w=1024)

Come previsto le informazioni relative ai processi vengono raccolte e, nel nostro caso, stampate in un logfile.

#### Visibilità lato EDR

Torniamo ai prodotti di mercato: come detto questa metodologia è utilizzata da molti EDR e ci permette di ottenere molte informazioni su ciò che accade a livello kernel. Nel lab che ho predisposto per i test possiamo affidarci ai sensori di Elastic per ottenere lo stesso risultato, ovviamente in modo molto più strutturato.

Ovviamente sapere quali processi vengono eseguiti (in questo post ci limitiamo al tema processi e nei prossimi esamineremo altri elementi) è abbastanza importante in quanto tutte le azioni che un bad actor farà potranno essere visibili sotto forma di processo con eventuali parametri. Un banale comando powershell richiede che venga avviato un processo, powershell appunto, a cui saranno passati dei parametri. Utilizzando la nostra configurazione in lab possiamo verificare il livello di visibilità di un agente come quello di Elastic così come fatto per il driver che ci siamo scritti da soli.

Facciamo fare qualcosa a powershell passando un comando qualsiasi:

![](https://roccosicilia.com/wp-content/uploads/2026/03/image-10.png?w=848)

Su Elastic possiamo fare una query abbastanza precisa per intercettare questo evento registrato grazie al sensore dell’EDR:

```
# se l'evento avvia un processo nuovo

event.category : "process" and event.type : "start"

# se l'evento viende da un processo aperto

event.category : "process"

# per eventi powershell con un comando definito

event.category : "process" AND process.command_line : * AND process.executable : *powershell*
```

![](https://roccosicilia.com/wp-content/uploads/2026/03/image-11.png?w=1024)

Questo livello di dettaglio è estremamente utile in quanto permette ad EDR e SIEM di sapere esattamente cosa sta succedendo sul sistema, comprese le azioni del threat actor che, dopo aver ottenuto un primo accesso ad sistema, sfrutta powershell o altri componenti per impartire comandi localmente o l’esecuzione di un payload tramite Fake CAPTCHA ([ne ho parlato qui](https://roccosicilia.com/2026/02/17/analisi-...