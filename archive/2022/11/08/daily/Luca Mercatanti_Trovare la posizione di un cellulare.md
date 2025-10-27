---
title: Trovare la posizione di un cellulare
url: https://luca-mercatanti.com/trovare-la-posizione-di-un-cellulare/?utm_source=rss&utm_medium=rss&utm_campaign=trovare-la-posizione-di-un-cellulare
source: Luca Mercatanti
date: 2022-11-08
fetch_date: 2025-10-03T21:59:22.424586
---

# Trovare la posizione di un cellulare

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

* [Hacking](https://luca-mercatanti.com/category/hacking/)

# Trovare la posizione di un cellulare

7 Novembre 2022

4 minuti per leggere l'articolo

![](https://luca-mercatanti.com/wp-content/uploads/2022/11/localizzare-smartphone-2-800x500.jpg)

In questo articolo scopriremo come sia possibile trovare la posizione di un cellulare facilmente e soprattutto senza dover installare alcuna applicazione all’interno del telefono che vogliamo localizzare, **sfruttando semplicemente una pagina Web** ed un po’ di [Ingegneria Sociale.](https://it.wikipedia.org/wiki/Ingegneria_sociale) Per fare ciò, andremmo ad utilizzare lo strumento Open Source [Seeker](https://github.com/thewhiteh4t/seeker), presente su GitHub.

Il concetto alla base di Seeker è semplice: così come esistono le pagine di phishing per ottenere credenziali di accesso (generalmente nome utente e password), perché non creare **una pagina Web in grado di richiedere la posizione dell’utente**?
Per chi non lo sapesse, infatti, una pagina Web è in grado di richiedere la posizione geografia del dispositivo in uso: questo generalmente avviene all’interno di tutti quei servizi in cui la geolocalizzazione è un elemento determinate per l’utilizzo dello stesso, come, ad esempio, nel caso di Google Maps.

[![Logo di Seeker](https://luca-mercatanti.com/wp-content/uploads/2022/11/localizzare-cellulare-seeker.jpeg)](https://luca-mercatanti.com/wp-content/uploads/2022/11/localizzare-cellulare-seeker.jpeg)

**La precisione della posizione dell’utente dipende da una serie di fattori**: in caso di smartphone, ad esempio, la geolocalizzazione avverrà mediante l’interrogazione del GPS, ottenendo così un dato altamente preciso, con uno scarto di pochi metri. In caso di computer, invece, la posizione potrà fare riferimento o ad una zona approssimativa, oppure, nel caso in cui sia in uso un browser collegato allo smartphone (come, ad esempio, Google Chrome), **la posizione esatta richiesta in tempo reale al sensore GPS di quest’ultimo**.

## Quali dati possiamo estrarre oltre alla posizione?

Quindi, capito il concetto che sta alla base di Seeker, lo strumento che andremmo ad utilizzare per localizzare un cellulare, vediamo quali sono i dati che riusciremo ad ottenere:

* Longitudine
* Latitudine
* Accuratezza del dato
* Altitudine, Non sempre disponibile
* Direzione, disponibile solo se l’utente è in movimento
* Velocità, disponibile solo se l’utente è in movimento

Insieme alle informazioni sulla posizione, avremmo accesso anche a queste informazioni sul dispositivo in uso:

* ID univoco del dispositivo
* Modello del dispositivo
* Sistema operativo
* Modello del processore
* Quantità di RAM
* Risoluzione dello schermo
* Nome del browser utilizzato
* Indirizzo IP

Le informazioni relative allo smartphone potrebbero essere particolarmente utili all’interno di una ricerca di tipo OSINT, o per avere contezza effettiva del dispositivo che ha aperto il link.

## Installare Seeker

Seeker deve essere installato all’interno di un computer al fine di generare la pagina Web e relativo URL da inviare alla persona che intendiamo localizzare. Nella pratica, **Seeker andrà a generare una pagina Web simile ad uno dei servizi qui sotto elencati**, tra cui potremmo scegliere, generando un URL da inviare alla persona della quale vogliamo ottenere la posizione GPS:

* NearYou
* Google Drive
* WhatsApp
* Telegram
* Zoom
* Google reCAPTCHA

Qui sta il concetto alla base dell’ingegneria sociale: l’utente che intenda scoprire la posizione di un cellulare, dovrà inviare alla sua “vittima” un messaggio contenente il link fornito da Seeker, il quale mostrerà una pagina Web fasulla simile ad uno dei servizi sopra elencati. Nel momento in cui il destinatario del messaggio farà click sul link, **visionerà effettivamente una grafica simile al servizio desiderato**, ma al contempo, in background, **otterrà la posizione geografica**, inoltrandola al mittente/attaccante.
Per quanto riguarda l’installazione, **le istruzioni da seguire sono presenti all’interno della [pagina GitHub](https://github.com/thewhiteh4t/seeker#installation)** del progetto e richiedono l’utilizzo di una distro di Linux

## Localizzare un cellulare, video dimostrativo

Qui di seguito, vi lascio con il video dimostrativo del funzionamento di Seeker.

## Servizi pronti all’uso

Nel caso in cui non abbiate le conoscenze  tecniche per procedere autonomamente all’installazione del software, **potete rifarvi a dei servizi, a pagamento, in grado di automatizzare tutto il processo**, dandovi come unico onere quello relativo all’invio dell’URL alla persona di cui intendete conoscere la posizione geografica.
Qui un breve elenco:

* IpLogger.org (attualmente il più completo)
* Grabify.link
* ip-trap.com

## Altre soluzioni

Ci sono soluzioni anche di altra natura per localizzare un telefono e tra queste risultano sicuramente le App.
Una potente app di monitoraggio come [mSpy](https://www.mspy.it/) è progettata per le persone che vogliono localizzare un telefono cellulare. Per vedere la posizione di un cellulare (dopo aver installato l’applicazione), sarà sufficiente accedere al pannello di controllo con i propri dati di login. Basterà fare clic su “Posizioni GPS”, voce presente nel menù, per visualizzare un elenco delle posizioni più recenti o visualizzare la posizione in tempo reale.

mSpy può inviarti, inoltre, una...