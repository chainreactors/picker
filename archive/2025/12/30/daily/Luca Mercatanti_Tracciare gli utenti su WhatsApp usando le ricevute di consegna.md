---
title: Tracciare gli utenti su WhatsApp usando le ricevute di consegna
url: https://luca-mercatanti.com/tracciare-gli-utenti-su-whatsapp-usando-le-ricevute-di-consegna/?utm_source=rss&utm_medium=rss&utm_campaign=tracciare-gli-utenti-su-whatsapp-usando-le-ricevute-di-consegna
source: Luca Mercatanti
date: 2025-12-30
fetch_date: 2025-12-31T03:25:34.179519
---

# Tracciare gli utenti su WhatsApp usando le ricevute di consegna

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

![](https://luca-mercatanti.com/wp-content/uploads/2025/12/whatsapp-hacking-110x110.png)

###### [Tracciare gli utenti su WhatsApp usando le ricevute di consegna](https://luca-mercatanti.com/tracciare-gli-utenti-su-whatsapp-usando-le-ricevute-di-consegna/)

5 minuti per leggere l'articolo

![Sim card in un telefono](https://luca-mercatanti.com/wp-content/uploads/2025/11/iccid-sim-card-110x110.jpg)

###### [Guida Completa all’ICCID della scheda SIM: cos’è, come trovarlo ed a cosa serve](https://luca-mercatanti.com/guida-completa-alliccid-della-scheda-sim-cose-come-trovarlo-ed-a-cosa-serve/)

5 minuti per leggere l'articolo

![](https://luca-mercatanti.com/wp-content/uploads/2025/09/annullare-email-110x110.jpg)

###### [Annullare un’email inviata](https://luca-mercatanti.com/annullare-unemail-inviata/)

6 minuti per leggere l'articolo

![](https://luca-mercatanti.com/wp-content/uploads/2025/08/esecuzione-copia-forense-110x110.jpg)

###### [Copia forense: requisiti, strumenti e procedure per prove digitali in ambito giudiziario](https://luca-mercatanti.com/copia-forense-requisiti-strumenti-e-procedure-per-prove-digitali-in-ambito-giudiziario/)

8 minuti per leggere l'articolo

* [Hacking](https://luca-mercatanti.com/category/hacking/)

# Tracciare gli utenti su WhatsApp usando le ricevute di consegna

31 Dicembre 2025

5 minuti per leggere l'articolo

![](https://luca-mercatanti.com/wp-content/uploads/2025/12/whatsapp-hacking-800x500.png)

In questi giorni mi sono imbattuto in un paper su Arxiv.gov dal titolo “*[Careless Whisper: sfruttare le ricevute di consegna silenziose per monitorare gli utenti sui servizi di messaggistica istantanea per dispositivi mobili](https://arxiv.org/abs/2411.11194)*“. Il paper analizza una vulnerabilità di privacy presente in alcune app di messaggistica istantanea molto diffuse, in particolare WhatsApp e Signal.
In sintesi, **gli autori mostrano che le spunte di conferma di consegna dei messaggi possono essere sfruttati come tecnica per monitorare un utente senza che questo riceva alcuna notifica**.

Grazie all’utilizzo di messaggi appositamente costruiti (come reazioni, modifiche o cancellazioni), è possibile forzare la generazione di ricevute di consegna invisibili all’utente e, **analizzando il tempo di risposta (RTT) di queste ricevute, un attaccante può ottenere informazioni utili**, ad esempio all’interno di un contesto OSINT, tra cui:

* se lo schermo del telefono è acceso o spento
* se l’app di messaggistica è in primo piano
* gli orari di attività e inattività quotidiani
* la presenza e lo stato di più dispositivi collegati allo stesso account (smartphone, web client, desktop)

Se a primo avviso questo potrebbe sembrare un problema di privacy “da poco”, riflettendoci, **è possibile in realtà tracciare con estrema precisione il comportamento degli utenti** in relazione all’utilizzo dei loro smartphone, conoscendo semplicemente il numero di telefono. Realizzando infatti un semplice script, è possibile inviare, ad intervalli regolari ed in modo automatizzato, dei messaggi “invisibili” che, analizzati secondo quanto riportato nel paper, permettono di comprendere la relazione tra l’utente e lo smartphone.

Lo screenshot qui sopra riportato (il quale fa riferimento alla Figura 1 nel documento originale) mostra in modo molto chiaro **il cuore della vulnerabilità** descritta nel paper.
Gli autori hanno misurato il **Round-Trip Time (RTT)** delle *delivery receipts* di WhatsApp su iPhone, cioè il tempo che passa tra l’invio di un messaggio “silenzioso” e la ricezione della conferma di consegna dal dispositivo della vittima. La misura è stata fatta con una frequenza di **1 ping al secondo**.

![](https://luca-mercatanti.com/wp-content/uploads/2025/12/2025-12-31_001059.jpg)

Il grafico mette a confronto due stati del telefono della vittima:

* **Screen On** (schermo acceso)
* **Screen Off** (schermo spento)

Sull’asse orizzontale c’è il **tempo di risposta in millisecondi**, su quello verticale la **probabilità** (distribuzione statistica degli RTT osservati).
Quello che emerge è una **separazione netta delle due distribuzioni**:

* Quando lo **schermo è acceso**, i delivery receipt tornano **molto velocemente**, quasi sempre **sotto 1 secondo**. Questo accade perché il sistema operativo mantiene CPU, rete e app in uno stato attivo, rispondendo immediatamente ai pacchetti.
* Quando lo **schermo è spento**, i tempi di risposta aumentano in modo evidente, con RTT **superiori a 1 secondo**, spesso tra **1.5 e 2.5 secondi**. Qui entrano in gioco i meccanismi di risparmio energetico (sleep, deep sleep, background scheduling).

Il punto fondamentale è che **questa differenza è sistematica e stabile**, non casuale. Un attaccante che osserva solo i tempi di ritorno delle ricevute può quindi stabilire con ottima affidabilità se il telefono della vittima è:

* in uso attivo
* inattivo / in standby

Il tutto **senza inviare messaggi visibili**, senza notifiche e senza che la vittima possa accorgersene.
Dal punto di vista pratico, questa figura dimostra che i delivery receipt diventano un **sensore remoto dello stato del dispositivo**. Ripetendo la misura nel tempo, si può ricostruire:

* cambiamenti improvvisi di attività
* orari di utilizzo del telefono
* pattern giornalieri (sonno, lavoro, pause)

## Quali messaggi vengono utilizzati per tracciare gli utenti

Nel capitolo **“Delivery Receipt Sources”** gli autori del paper spiegano **da quali azioni concrete nascono le delivery receipt** e, soprattutto, **quali di queste azioni sono sfruttabili come canale laterale “silenzioso”** per monitorare un utente senza che se ne accorga.
Il punto di partenza è chiarire che **non solo i messaggi di testo** generano una delivery receipt. Gli autori testano in modo sistematico diverse azioni supportate dai client di WhatsApp, Signal e Threema, osservando due aspetti per ciascuna:

1. se l’azione genera una delivery receipt verso il mittente
2. se l’azione produce una notifica visibile per il destinatario

Le azioni analizzate sono quattro:

* invio di un messaggio normale
* modifica di un messaggio già inviato
* reazione a un messaggio (emoji)
* cancellazione di un messaggio (“delete for everyone”)

Il risultato chiave è che **WhatsApp e Signal inviano delivery receipt anche per reazioni, modifiche e cancellazioni**, mentre **Threema limita le ricevute ai soli messaggi normali**. Questo dettaglio è cruc...