---
title: Differenza BFU e AFU su iOs
url: https://luca-mercatanti.com/differenza-bfu-e-afu-su-ios/?utm_source=rss&utm_medium=rss&utm_campaign=differenza-bfu-e-afu-su-ios
source: Luca Mercatanti
date: 2023-05-18
fetch_date: 2025-10-04T11:42:17.424722
---

# Differenza BFU e AFU su iOs

[![Luca Mercatanti](https://luca-mercatanti.com/wp-content/uploads/2020/12/logo.png)](https://luca-mercatanti.com/)

* [Home](http://www.luca-mercatanti.com)
* [Chi sono](https://luca-mercatanti.com/about/)
* [Contatti](https://luca-mercatanti.com/contattami/)
* [Perizie Informatica Forense](https://luca-mercatanti.com/perizie-informatica-forense/)

![Luca Mercatanti - Le Iene](https://luca-mercatanti.com/wp-content/uploads/2018/05/Luca-Mercatanti-Iene.png)

**Dal 2007 mi occupo di Digital** e dal 2010 aiuto professionisti ed imprese nella Comunicazione Digitale e Marketing Online.
**Hacker e Smanettone Tecnologico.**

Dal 2019 sono**assistente in “Comunicazione Digitale”** all’Università Europea di Roma.
Dal Settembre 2007 divulgo le mie scoperte e conoscenze all’interno di questo Blog in forma completamente gratuita.
**Ogni anno ricevo circa 1.600.000 visitatori!**

**[Vuoi scoprire di più? Premi qui!](https://luca-mercatanti.com/about/)**

[![Luca Mercatanti](https://luca-mercatanti.com/wp-content/uploads/2020/12/logo.png)](https://luca-mercatanti.com/)

[![Luca Mercatanti](https://luca-mercatanti.com/wp-content/uploads/2020/12/logo.png)](https://luca-mercatanti.com/)

* [Home](http://www.luca-mercatanti.com)
* [Chi sono](https://luca-mercatanti.com/about/)
* [Contatti](https://luca-mercatanti.com/contattami/)
* [Perizie Informatica Forense](https://luca-mercatanti.com/perizie-informatica-forense/)

[![Luca Mercatanti](https://luca-mercatanti.com/wp-content/uploads/2020/12/logo.png)](https://luca-mercatanti.com/)

##### Ultime pubblicazioni

![](https://luca-mercatanti.com/wp-content/uploads/2025/09/annullare-email-110x110.jpg)

###### [Annullare un’email inviata](https://luca-mercatanti.com/annullare-unemail-inviata/)

6 minuti per leggere l'articolo

![](https://luca-mercatanti.com/wp-content/uploads/2025/08/esecuzione-copia-forense-110x110.jpg)

###### [Copia forense: requisiti, strumenti e procedure per prove digitali in ambito giudiziario](https://luca-mercatanti.com/copia-forense-requisiti-strumenti-e-procedure-per-prove-digitali-in-ambito-giudiziario/)

8 minuti per leggere l'articolo

![](https://luca-mercatanti.com/wp-content/uploads/2025/08/conosceza-ai-110x110.png)

###### [le AI non sanno davvero ciò che dicono](https://luca-mercatanti.com/le-ai-non-sanno-davvero-cio-che-dicono/)

2 minuti per leggere l'articolo

![](https://luca-mercatanti.com/wp-content/uploads/2025/08/chatgpt-condivide-chat-110x110.jpg)

###### [ChatGPT: le tue chat finiscono su Google](https://luca-mercatanti.com/chatgpt-le-tue-chat-finiscono-su-google/)

3 minuti per leggere l'articolo

* [Informatica Forense](https://luca-mercatanti.com/category/informatica-forense/)

# Differenza BFU e AFU su iOs

17 Maggio 2023

4 minuti per leggere l'articolo

![iPhone collegato ad un cavo](https://luca-mercatanti.com/wp-content/uploads/2023/05/differenza-bfu-afu-800x500.webp)

**Per informazioni, consulenze e preventivi**

Per informazioni o Consulenze relative ai servizi di Informatica Forense e Perizie Informatiche, potete fare click sul bottone “Contattaci” per inviare una richiesta o contattarci telefonicamente.

[Contattaci](https://luca-mercatanti.com/copia-forense/)

Quando si parla di [Informatica Forense](https://luca-mercatanti.com/perizie-informatica-forense/) e [copie forensi](https://luca-mercatanti.com/copia-forense) in ambito iOs, ci si scontra con i termini ed i concetti legati a **BFU (Before First Unlock)** e **AFU (After First Unlock)**. Capire la loro differenza è fondamentale, in quanto indicano lo stato in cui un dispositivo iPhone o iPad può trovarsi e sulla base del quale è possibile o meno accedere non solo a determinati dati contenuti all’interno del dispositivo informatico, ma che **cambia drasticamente il modo in cui è possibile bypassare il codice di sblocco** di un dispositivo Apple.

Partiamo dalla situazione in cui l’iPhone si trova (generalmente, ma non solo) non appena acceso: **BFU (Before First Unlock).**
I dispositivi in modalità BFU sono quelli che sono stati spenti o riavviati e **non sono mai stati successivamente sbloccati**, nemmeno una volta, inserendo il codice di blocco dello schermo corretto.
Nel mondo di Apple, **il contenuto dell’iPhone rimane crittografato** in modo sicuro fino al momento in cui l’utente non inserisce il codice di sblocco: quest’ultimo è assolutamente necessario per generare la chiave di crittografia, che a sua volta è assolutamente necessaria per decifrare il file system dell’iPhone.

![Estrazione in modalità BFU e AFU](https://luca-mercatanti.com/wp-content/uploads/2023/04/eift.png)

In altre parole, quasi tutto all’interno dell’iPhone rimane crittografato fino a quando l’utente non lo sblocca con il proprio passcode dopo l’avvio del telefono. In questo articolo tralasciamo la parte del “quasi del tutto”, in quanto nella realtà vi sono delle **porzioni di memoria che sono comunque accessibili** nei dispositivi iOs anche prima dello sblocco e che vengono sfruttate da software specifici (come quello di cui vi pubblico lo screenshot qui sotto) per ottenere informazioni che potrebbero risultare importanti all’interno di una perizia informatica forense.

A contrario, **la modalità AFU (After First Unlock)** è lo stato in cui il telefono si trova dopo aver inserito il codice di sblocco almeno una volta. In tale circostanza, infatti, la chiave di crittografia “Master” è stata generata ed i dati personali dell’utente sono accessibili.
Questo rende possibile, mediante software forensi quali “Cellebrite UFED”, l’accesso ad informazioni sensibili ed anche lo sblocco del dispositivo iOs in modo abbastanza rapido. Ecco il motivo per cui, in caso di sequestro di un iPhone o iPad, **il dispositivo mobile dovrebbe rimanere alimentato**, in particolar modo se il soggetto al quale lo smartphone è stato sequestrato non intende rivelare il codice di sblocco.

## BFU (Before First Unlock)

Iniziamo ad approfondire lo stato BFU, che sta per “Before First Unlock”. Questo termine si riferisce a una modalità di funzionamento del dispositivo iOS prima che venga effettuato il primo sblocco. In sostanza, quando accendi per la prima volta il tuo dispositivo iOS o lo riavvii dopo un completo spegnimento, si trova nello stato BFU.
Durante la modalità BFU, molte funzionalità del dispositivo sono limitate o addirittura disabilitate. Ad esempio, non è possibile accedere ai dati dell’utente, come le foto, i messaggi o le app protette da password. Inoltre, molte app di terze parti non possono essere eseguite fino a quando il dispositivo non viene sbloccato.

## AFU (After First Unlock)

Passiamo adesso all’AFU, che sta per “After First Unlock”. Una volta che hai sbloccato il tuo dispositivo iOS con il codice di accesso o con l’impronta digitale (Touch ID) o il riconoscimento facciale (Face ID), il dispositivo passa dallo stato BFU allo stato AFU.
Nella modalità AFU, il dispositivo iOS diventa completamente accessibile. Puoi utilizzare tutte le funzionalità del tuo dispositivo, comprese le app protette da password e l’accesso ai tuoi dati personali. Le app di terze parti possono essere eseguite normalmente, consentendo di sfruttare appieno tutte le potenzialità del tuo dispositivo iOS.

## Differenze tra BFU e AFU

Ora che abbiamo compreso le modalità BFU e AFU su iOS, possiamo analizzare le differenze principali tra di esse.

1. **Funzionalità limitate vs. Accesso completo:** La differenza più evidente tra BFU e AFU è il livello di accesso e le funzionalità disponibili. Mentre BFU limita molte funzioni e restrizioni, AFU offre un accesso completo a tutte le funzionalità del dispositivo.
2. **Protezione dei dati vs. Convenienza:** La modalità BFU è progettata per proteggere i dati dell’utente in situazioni in cui il dispositivo viene perso o rubato. Durante questa modalità, i dati sono inaccessibili, offrendo una maggiore sicurezza. D’altro canto, AFU offre maggiore comodità all’utente, consentendo di accedere rapidamente ai propri dati.
3. **...