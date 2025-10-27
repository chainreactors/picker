---
title: Da quale recovery point parto?
url: https://roccosicilia.com/2025/06/27/da-quale-recovery-point-parto/
source: Over Security - Cybersecurity news aggregator
date: 2025-06-28
fetch_date: 2025-10-06T22:56:18.381392
---

# Da quale recovery point parto?

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/progetto-di-divulgazione/)
* [Sostieni il progetto](https://roccosicilia.com/sostieni-il-progetto/)
* [English version](https://medium.com/%40roccosicilia)

[cyber security](https://roccosicilia.com/category/cyber-security/), [ita](https://roccosicilia.com/category/ita/)

## [Da quale recovery point parto?](https://roccosicilia.com/2025/06/27/da-quale-recovery-point-parto/)

Published by

Rocco Sicilia

on

[27 giugno 2025](https://roccosicilia.com/2025/06/27/da-quale-recovery-point-parto/)

[![Da quale recovery point parto?](https://roccosicilia.com/wp-content/uploads/2025/06/screenshot-2025-06-27-at-16.53.16.png?w=600)](https://roccosicilia.com/2025/06/27/da-quale-recovery-point-parto/)

Premessa: non è un tema piacevole ed il motivo è abbastanza scontato. Pochissimi IT manager / CIO / CISO hanno seriamente affrontato il task per portarsi a casa una procedura di base (scritta, nero su bianco e adottabile “adesso”) di ricostruzione dei sistemi a seguito di un incidente che non consente una recovery completa da backup.

Qualche tempo fa ho discusso il tema con [**Mattia Parise**](https://www.linkedin.com/in/mattiaparise/) in uno di quegli scambi sempre utili per ragionare su un tema considerando diversi punti di vista. Da quella chiacchierata sono nate un po’ di riflessioni.

Giustamente ci si potrebbe chiedere:

> “In quale occasione dovrei trovarmi a non poter eseguire una recovery da backup? Uso storage immutabili da anni.”

Lo storage immutabile, cosa molto utile ovviamente, ha una funzione precisa: impedisce che un dato archiviato sia compromesso. Quindi, fino a scadenza e fino a quando lo storage funziona, il dato che andiamo ad archiviare in questi sistemi è inalterabile. Il vantaggio è evidente: nessuna modifica possibile significa anche nessuna compromissione da cripto-malware.

Dobbiamo però sempre fare i conti con quello che accade nel mondo vero, durante un attacco vero. Chi ha adottato da qualche tempo tecnologie di detection serie e si è andato a vedere cosa individuano i vadi EDR/XDR/SIEM, avrà probabilmente notato che gli attaccanti tentano di ottenere un accesso ai sistemi compromettendo una credenziale o un sistema all’interno della rete. In questo processo una delle fasi fondamentali è la *persistenza*: l’attaccante fa in modo di modificare uno o più sistemi in modo da garantirsi una “backdoor” (uso questo vecchio termine anche le il modello attuale è un po’ differente) sempre attiva all’interno della rete.

Ne avevo parlato in un paio di vecchi video:

[![](https://roccosicilia.com/wp-content/uploads/2025/06/image-14.png?w=1024)](https://www.youtube.com/%40roccosicilia/search?query=c2)

Archivio video su Villain

Il problema da considerare è che dalla compromissione dei sistemi a livello di persistenza – ovvero il threat actor è dentro e si è garantito un canale di comunicazione stabile – a quando vendono eseguire le azioni che generano impatto sui sistemi (es: cripto-malware) può passare del tempo.

Se mettiamo le fasi di un attacco su una timeline vedremo quindi un momento in cui il threat actor inizia a muoversi nella rete per poi arrivare ad eseguire le azioni di effettivo impatto come la compromissione dei dati di produzione.

![](https://roccosicilia.com/wp-content/uploads/2025/06/image-16.png?w=1024)

Ipotetica timeline

Ovviamente non è possibile fare una previsione dei tempi che intercorrono tra l’inizio delle azioni offensive ed il momento in cui iniziano le attività di compromissione dei dati. Diventa quindi estremamente importante **ricostruire gli eventi per identificare il metodo di accesso e quando la compromissione iniziale è avvenuta**. Comprendere il metodo di accesso ed eseguire le correzioni è necessario per evitare che l’attaccante lo riutilizzi in futuro. Sapere quando è iniziata la compromissione dei sistemi ci server per capire da quale versione degli archivi eseguire la revocery.

Purtroppo capita di non avere informazioni certe a disposizione: meno la struttura è matura dal punto di vista dei sistemi di detection e più è probabile che non ci siano dati, logs, tracce delle azioni del threat actor con l’inevitabile conseguenza di non sapere, con precisione, data e ora della compromissione.

Ci si trova così a non saper rispondere con precisione alla domanda “da quale backup eseguiamo il ripristino?”; restando sulla nostra ipotetica timeline, ripristinare i sistemi di cui si dispongono i backup, utilizzando un recovery point successivo dal 5 maggio compreso equivale a mettere online sistemi che, probabilmente, porteranno online anche il canale di comunicazione che il threat actor ha utilizzato. Conseguenza (vista con i miei occhi più di una volta): tempo qualche giorno e si ricomincia da capo.

## Come se ne esce?

Premesso che al tema vorrei dedicare un video con qualche approfondimento, in questa occasione provo ad argomentare un po’ di spunti a livello di prevenzione e gestione.

#### Prevenzione: se so cosa è successo posso valutare il recovery-point più idoneo

Ovviamente se avessimo la possibilità di sapere, analizzando gli eventi a ritroso, quali azioni ha eseguito il threat actor per compromettere il sistema e garantirsi la permanenza all’interno della rete, il problema sarebbe per lo meno affrontabile: se abbiamo una indicazione temporale precisa abbiamo automaticamente trovato il recovery-point per i sistemi e si potrebbe valutare una restore degli ambienti dagli archivi immediatamente precedenti alla data di compromissione. Ovviamente sto dando per scontato che gli archivi siano disponibili e su supporti immutabili e che non siano stati manomessi in nessun modo.

Considerando che il punto di accesso potrebbe essere un qualsiasi endpoint o asset della rete dovrei avere visione di tutti i logs relativi ad accessi e change di configurazioni dei sistemi. Una parte di questi dati li potremmo avere all’interno della piattaforma EDR/XDR con un livello di dettaglio anche molto alto, ma solitamente la retention di questi dati è bassa. Sui SIEM si adottano retention più profonde ma raramente viene portata tutta la telemetria disponibile sui diversi sistemi di detection anche sul SIEM per un banale problema di spazi e costi di licenza.

In parole povere: disporre dei dati per ricostruire le azioni del threat actor è possibile ma non lo possiamo dare per scontato. Dobbiamo disporre di sistemi di detection che raccolgano le telemetrie utili, dobbiamo raccogliere dati da tutti i dispositivi in rete e dobbiamo disporre di una retention che sia superiore rispetto alla durata dell’attacco. Se tutti questi elementi si incastrano possiamo portarci a casa un risultato.

E se non si incastrano?

#### Non ho certezza di un recovery-point “pulito”

In questo caso abbiamo un bel problema: i backup ci sono ma non sappiamo di quale fidarci perché non sappiamo quanto tempo prima il threat actor ha manomesso i nostri sistemi. Come ci si garantisce una partenza sicura? Ci sono diverse opzioni ed alcune comportano dei rischi da considerare.

Inevitabilmente è necessario considerare come gestiamo e verifichiamo il processo di backup: ad esempio se disponessimo di una immagine verificata dei sistemi operativi e loro configurazione e di un dataset dei dati critici, il problema sarebbe relativamente aggirabile con un processo di “rebuild” basato sulla *gold image* ed i dati. In un periodo storico in cui siamo abituati (per indiscussa comodità) a disporre dei soli backup “Full VM” probabilmente pochi/pochissimi oggi potrebbero pensare di far ripartire i sistemi in questo modo. Un’immagine dei sistemi operativi e delle relative applicazioni consentirebbe una rapida re-installazione pulita degli ambienti a cui potrebbe far seguito una recovery dei soli dati. Ovviamente questo richiede una strategia di backup dedicata che vada per lo meno ad affiancare al clas...