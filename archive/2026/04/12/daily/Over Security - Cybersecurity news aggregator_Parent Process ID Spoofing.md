---
title: Parent Process ID Spoofing
url: https://roccosicilia.com/2026/04/12/parent-process-id-spoofing/
source: Over Security - Cybersecurity news aggregator
date: 2026-04-12
fetch_date: 2026-04-13T04:57:11.418628
---

# Parent Process ID Spoofing

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/divulgazione/)
* [Progetti](https://roccosicilia.com/progetti/)

[cyber security](https://roccosicilia.com/category/cyber-security/), [hacking](https://roccosicilia.com/category/hacking/), [ita](https://roccosicilia.com/category/ita/)

## [Parent Process ID Spoofing](https://roccosicilia.com/2026/04/12/parent-process-id-spoofing/)

Published by

Rocco Sicilia

on

[12 aprile 2026](https://roccosicilia.com/2026/04/12/parent-process-id-spoofing/)

[![Parent Process ID Spoofing](https://roccosicilia.com/wp-content/uploads/2026/04/screenshot-2026-04-12-at-16.25.37.png?w=1024)](https://roccosicilia.com/2026/04/12/parent-process-id-spoofing/)

Continuiamo la serie di laboratori sulle tecniche di evasione prima di prenderci una pausa per valutare qualche strategia di difesa. Il nome della tecnica (rif. al titolo del post) è decisamente chiaro: si tratta di modificare una delle informazioni che caratterizzano i processi, ovvero l’ID del processo padre.

Perché dovremmo voler modificare il Process ID del processo padre rispetto al nostro processo “malevolo”? La tecnica punta a generare confusione rispetto a ciò che verrà registrato dall’EDR: gli analisi hanno interesse a capire da quale processo/applicazione è stato lanciato il processo sospetto in quanto alcune tecniche di attacco prevedono specifiche “sequenze” si azioni.

Ad esempio le “vecchie care macro” di MS Word consentivano di eseguire codice VBA sul sistema e spesso i bad actor le utilizzavano per far girare alcuni stage del proprio malware sul sistema target. Quando questo avveniva era possibile osservare che il processo padre del malware era MS Word cosa che consentiva di comprendere meglio quello che si stava osservando. Come sempre per capire bene il concetto la cosa migliore è osservarlo con un piccolo test.

![](https://roccosicilia.com/wp-content/uploads/2026/04/image.png?w=1024)

Se sul vostro ambiente MS Windows aprite un prompt dei comandi (cmd.exe) ed eseguire un comando powershell otterrete un processo powershell che ha come Parent Process ID il cmd.exe da cui è partito.

Per avere il tempo di osservare la cosa potete eseguire un comando sleep:

```
powershell -c "sleep 60"
```

In questo modo il processo powershell partirà e resterà attivo per 60 secondi, più che sufficienti per verifica con il comando ***tasklist*** il PID del comando powershell (5044 nel mio test) e verificarne il padre:

```
wmic process where ProcessId=5044 get Name, ProcessId, ParentProcessId

Name             ParentProcessId    ProcessId

powershell.exe   7716               5044
```

Questa informazione viene registrata dall’EDR sempre tramite l’utilizzo delle callback routines descritte nel precedente post così da avere un’informazione chiara a *console*: qualcuno da ***cmd.exe*** ha eseguito un processo ***powershell.exe*** (informazione ottenuta dal controllo del PPID) ed ha eseguito il comando “*sleep 60*” (informazione ottenuta dalla notifica dei parametri passati al comando powershell).

Tutto fantastico, ma se potessi assegnare un PPID differente al mio processo “malevolo”, ad esempio uno apparentemente lecito come quello di un’operazione di sistema o di un tool interno, potrei ingannare l’analista o non intercettare una detection rule che presenta delle condizioni specifiche. Facciamo un esempio realistico: se sull’ambiente target è attivo un agent per l’asset management potrei far apparite i miei comandi powershell come “figli” del processo dell’agent e probabilmente l’analista non gli darebbe particolare peso in quanto **è abituato a fidarsi delle operazioni che quell’applicazione esegue**.

#### La calcolatrice lancia comandi powershell

Ovviamente possiamo sperimentare tutto quello che abbiamo detto con un po’ di codice e qualche condizione da tenere a mente, la principale è relativa al processo che vogliamo usare come “padre fittizio” su cui dobbiamo avere un livello di accesso sufficiente. Solitamente è meglio scegliere tra processi dell’utente per andare sul sicuro, per il nostro test useremo la calcolatrice: **calc.exe**.

In questo semplice esempio utilizzeremo un PPID specifico di un processo già attivo sul sistema che, come si vede dall’immagine, è l’ID 8004 che corrisponde al processo Windows Calculator.

![](https://roccosicilia.com/wp-content/uploads/2026/04/screenshot-2026-04-06-at-18.54.02-1.png?w=1024)

Nota: durante i test mi sono accorto di alcuni comportamenti inattesi a livello di visualizzazione dei processi tramite Task Manager, ma verificando da CLI il comportamento è quello atteso.

Il nostro codice cercherà di eseguire un comando powershell con un argomento utile al test: ho pensato si usare il comando “*sleep 100*” per tenere il processo attivo per 100 secondi e permetterci di osservare gli effetti anche semplicemente a livello di task manager.

Ovviamente ai fini del test ci basta selezionare un PPID “staticamente” scegliendo tra i processi attivi, in un contesto reale dovremmo fare delle modifiche e scegliere un PPID dinamicamente ad esempio basandoci sul nome processo.

Il punto di partenza è aprire un handle al processo che si vuole usare come parent fittizio. Questo handle non è un semplice riferimento numerico o un ID ma è un oggetto kernel che punta direttamente alla struttura interna del processo target nel kernel (quello che vogliamo usare come “padre”).

![](https://roccosicilia.com/wp-content/uploads/2026/04/image-1.png?w=1024)

Una volta ottenuto l’handle, si prepara una lista di attributi estesi tramite le API e si inserisce nella lista l’attributo che indica il parent desiderato, puntando all’handle appena aperto. Questa lista verrà letta dal kernel durante la creazione del processo.

A questo punto si chiama la funzione di creazione del processo con un flag specifico che istruisce il kernel a leggere la lista attributi invece di ignorarla. È qui che avviene la parte interessante: il kernel segue il riferimento al parent fittizio, ne legge il PID e lo scrive nel campo apposito della struttura interna del nuovo processo. Non è il codice applicativo a scrivere il PPID ma lo scrive il kernel stesso durante la creazione.

Il risultato è che qualsiasi observer (Task Manager, Process Hacker, EDR, ETW) vede il parent fittizio come “padre legittimo” del processo.

#### Risultati del test

Il codice di esempio che metto a disposizione della repo ha qualche limitazione e, come accennato, il PPID viene definito staticamente. SI tratta di qualcosa che ha senso solo in un test di laboratorio. Trovate tutto nella [repo del progetto HAPpy](https://github.com/roccosicilia/HAPpy/blob/main/demo/PPIDSpoof_CreateProc_bypass.c), come per gli esempi già discussi metto a disposizione il codice commentato con più dettagli possibili (mi sta aiutando Claude con questo task e devo dire che viene bene) in modo da renderlo comprensibile.

Oltre all’output che ho previsto a livello codice (di per se eloquente) è utile osservare la telemetria lato EDR. Anche per questo test faccio affidamento al mio lab basato su Elastic.

Vi lascio una demo clip dell’esecuzione che in un video/live commenteremo nel dettaglio:

Il comando eseguito, come si diceva, è un processo powershell che esegue una sleep e come PPID usiamo quello dell’applicazione Windows Calculator che nella demo è 1728. L’evento di creazione del processo viene notificato all’agent di Elastic e possiamo andarlo a cercare.

![](https://roccosicilia.com/wp-content/uploads/2026/04/image-2.png?w=1024)

Ho selezionato i campi che ci interessano. Come si vede dalla demo, che ho registrato appositamente per poi utilizzare gli eventi lato EDR per questo post, il programma viene avviamo direttamente dall’utente ma sia lato task manager che lato EDR si vede come il paret di riferimento sia il PID di Windows Calculator.

Anche l’EDR ha registrato il PID errato dando l’apparenz...