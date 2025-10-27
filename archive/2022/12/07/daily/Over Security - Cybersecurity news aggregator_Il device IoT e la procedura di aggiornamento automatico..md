---
title: Il device IoT e la procedura di aggiornamento automatico.
url: https://roccosicilia.com/2022/12/06/il-device-iot-e-la-procedura-di-aggiornamento-automatico/
source: Over Security - Cybersecurity news aggregator
date: 2022-12-07
fetch_date: 2025-10-04T00:42:14.654274
---

# Il device IoT e la procedura di aggiornamento automatico.

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/progetto-di-divulgazione/)
* [Sostieni il progetto](https://roccosicilia.com/sostieni-il-progetto/)
* [English version](https://medium.com/%40roccosicilia)

[cyber security](https://roccosicilia.com/category/cyber-security/), [ita](https://roccosicilia.com/category/ita/), [OT/IoT](https://roccosicilia.com/category/ot-iot/)

## [Il device IoT e la procedura di aggiornamento automatico.](https://roccosicilia.com/2022/12/06/il-device-iot-e-la-procedura-di-aggiornamento-automatico/)

Published by

Rocco Sicilia

on

[6 dicembre 2022](https://roccosicilia.com/2022/12/06/il-device-iot-e-la-procedura-di-aggiornamento-automatico/)

Vi condivido una breve riflessione a seguito di diversi casi reali che ho avuto modo di osservare nelle ultime settimane, ovviamente senza dare riferimenti di nessun tipo sui protagonisti. E’ per me importante condividere questo tipo di esperienza per un motivo banale: è qualcosa che può accadere a chiunque e non è detto che si abbiano gli strumenti per intercettare rapidamente alcuni indicatori di compromissione, è quindi opportuno condividere esperienze in merito al fine di essere tutti più consapevoli.

Lo scenario è oggi un grande classico ma solo un paio di anni fa, quando ne parlavo con i diretti interessati, sembrava fantascienza: un dispositivo IoT interconnesso alla rete dell’azienda con esigenza di accesso alla rete internet per conversare, anche solo dall’interno verso l’esterno, con i sistemi in cloud del fornitore e/o gestore del servizio. Nel corso dell’ultimo anno ho seguito diverse attività in ambito cyber sec. in contesti di “rete di fabbrica” ed ho avuto la fortuna di vedere in dettaglio alcune implementazioni. La banalizzo un po’ per rendere il concetto fruibile a più persone possibili, gli esperti mi perdoneranno ed eventualmente integreranno con la loro saggezza (sempre apprezzata).

![](https://roccosicilia.com/wp-content/uploads/2022/12/image-1.png?w=1024)

Di solito abbiamo diversi dispositivi che dialogano con i sistemi di produzione per raccogliere informazioni e/o impartire istruzioni. I sistemi su cui queste informazioni vengono depositate possono essere all’interno dell’infrastruttura di rete come all’esterno. Molti player del mondo Public Cloud mettono a disposizione fantastiche piattaforme per la gestione di questi dati, non è quindi raro trovare sistemi IoT che dialogano con l’esterno della rete per atterrare sui sistemi che ospitano i servizi incaricati di elaborare i dati raccolti.

Quella che nel disegno è definita come “magic network(s)” sappiamo essere un tema complesso ma non è il focus di questo post; l’argomento segregazione delle reti in ambito IT ed OT in risposta alle esigenze di prevenzione delle minacce informatiche che hanno come target i sistemi industriali merita un capitolone dedicato. In questa occasione mi concentro sulle implicazioni di un sistema che dall’interno della rete è titolato a dialogare con un sistema all’esterno della rete di cui non abbiamo una completa gestione (visto che non è nostro) e di cui non siamo in grado di definire direttamente le politiche di sicurezza dovendo accettare, **si spera dopo averle validate**, quelle del fornitore.

In relazione ai dati scambiati il tema è relativamente semplice: proporzionalmente all’impatto che avrebbe la perdita, la manomissione o la sottrazione di questi dati dovremmo definire delle politiche di protezione, dalla sicurezza della comunicazione alle politiche di backup dei dati storici. Questo è un elemento che di solito trovo presidiato: si cerca di utilizzare protocolli che facciano uso della cifratura e si prediligono servizi consoni al trasferimento di informazioni. Per farla breve, c’è ancora chi spara archivi .zip via FTP ma, almeno nei contesti in cui opero io, sono decisamente pochi.

Avendo la possibilità di dialogare sempre con la propria infrastruttura cloud il dispositivo IoT viene spesso dotato di procedure di self provisioning si per le configurazioni che per le componenti software, fino a poter anche aggiornare il firmware del dispositivo stesso. E’ una scelta tecnicamente validissima in quanto da modo al fornitore di aggiornare il dispositivo senza intervenire on-site, sarà quindi il dispositivo a chiedere ai sistemi centralizzati se ci sono nuovi elementi software da installare o configurazioni da modificare. Per chi fa il mio lavoro **ricorda molto il funzionamento dei C2**.

![](https://roccosicilia.com/wp-content/uploads/2022/12/image-2.png?w=1024)

Se chi gestisce la rete in cui il dispositivo viene inserito ha l’onere di assicurarsi che le policies di comunicazione siano idonee (ne parliamo in un post a parte come già detto), chi gestisce la cloud deve garantire la sicurezza delle informazioni e dei sistemi a cui i devices accedono. Un threat actor in grado di accedere ai sistemi cloud potrebbe compromettere in profondità il sistema in cloud oppure potrebbe limitarsi a manomettere il sistema al fine di far atterrare sul device IoT una componente malevola. In questo caso l’attacker avrebbe potenziale accesso a tutti i sistemi IoT che afferiscono alla cloud compromessa.

La scelta dipende ovviamente dalle funzionalità che il sistema mette a disposizione: se è possibile impartire comandi al dispositivo IoT (ci sono sistemi che lo prevedono per garantire un certo livello di amministrazione) diventa possibile eseguire **azioni anche molto invasive dall’interno della rete target** in un contesto tipicamente delicato come la rete di fabbrica, diventa quindi semplice eseguire attività di ricognizione a caccia di altri sistemi o informazioni utili a mettere radici.

## Come intercettare il problema

Premesso che dovremmo iniziare a **lavorare di prevenzione qualificando opportunamente i fornitori**, è bene avere una strategia di intercettazione e gestione di questa tipologia di incident. Non avendo pertinenza sulla componente cloud ed essendo le comunicazioni necessariamente autorizzate oltre che cifrate, la detection difficilmente può avvenire a monte (non impossibile, ma difficile). Quello che possiamo sicuramente fare è lavorare sulla pertinenza locale: eventuali attività da parte dell’attacker genereranno sicuramente del traffico in rete verso destinazioni differenti dalle solite. In molti casi questi dispositivi dialogano con un numero limitato di sistemi interni, potremmo quindi insospettirci di qualsiasi comunicazione verso hosts insoliti (funzionalità disponibile in molte soluzioni di detection).

Anche il tipo di traffico è un elemento importante, questi sistemi solitamente utilizzano un set specifico di protocolli del mondo OT oltre ad HTTPS per la comunicazione con le API ed a qualche protocollo base come NTP e DNS. Proprio su questi ultimi due va fatto un focus ulteriore: esistono diverte tattiche di tunnelling basate proprio su questi protocolli, pur essendo traffico spesso legittimo è bene fare degli approfondimenti per verificare che non siano in corso azioni di exfiltration. Personalmente suggerisco di utilizzare, se disponibili, servizi interni per NTP e DNS in modo da negare il traffico verso l’esterno da questi dispositivi, ma non è sempre possibile.

Gli attacchi informatici, ce lo diciamo spesso, non sono composti da singola azioni chirurgiche. Esiste un path, un set di azioni che vengono svolte in sequenza e che inevitabilmente lasciano qualche traccia. In un contesto come quello descritto, in cui l’attacker di fatto trova un punto di accesso a causa di un problema introdotto da un terzo attore, è indispensabile essere preparati per intercettare gli effetti delle azioni di attacco più che le azioni in se in quanto potenzialmente non visibili.

## Conclusioni e riflessioni

Nel prossimo periodo parlerò in più occasioni di detection e delle soluzioni e servizi che possiamo mettere in campo a tal fine. In questa occasi...