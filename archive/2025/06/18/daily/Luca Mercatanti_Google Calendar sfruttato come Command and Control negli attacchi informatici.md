---
title: Google Calendar sfruttato come Command and Control negli attacchi informatici
url: https://luca-mercatanti.com/google-calendar-sfruttato-come-command-and-control-negli-attacchi-informatici/?utm_source=rss&utm_medium=rss&utm_campaign=google-calendar-sfruttato-come-command-and-control-negli-attacchi-informatici
source: Luca Mercatanti
date: 2025-06-18
fetch_date: 2025-10-06T22:55:08.566347
---

# Google Calendar sfruttato come Command and Control negli attacchi informatici

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

# Google Calendar sfruttato come Command and Control negli attacchi informatici

17 Giugno 2025

3 minuti per leggere l'articolo

![](https://luca-mercatanti.com/wp-content/uploads/2025/06/c2-google-calendar-800x500.jpg)

Alla fine di ottobre 2024, il Google Threat Intelligence Group (GTIG) ha scoperto una sofisticata campagna di cyber-spionaggio condotta dal gruppo statale cinese **APT41**. In questa operazione è stato utilizzato **Google Calendar come canale di comando e controllo (C2)**, un metodo inedito e difficile da rilevare. Il malware impiegato, denominato **TOUGHPROGRESS**, riusciva a comunicare in modo occulto con i sistemi infetti sfruttando eventi del calendario privi di durata e campi descrizione per trasmettere dati e ricevere comandi.

## Meccanismo di infezione

La catena d’attacco iniziava con l’invio di email di spear‑phishing contenenti un archivio ZIP ospitato su un sito governativo compromesso. Al suo interno era presente:

* un file .lnk camuffato da documento PDF,
* sette immagini JPG, due delle quali (6.jpg e 7.jpg) in realtà erano eseguibili mascherati.

[![LNK Infetti](https://luca-mercatanti.com/wp-content/uploads/2025/06/windows-lnk.png)](https://luca-mercatanti.com/wp-content/uploads/2025/06/windows-lnk.png)

Una volta aperto il collegamento, venivano eseguiti i seguenti step:

* PLUSDROP decrittava ed eseguiva codice in memoria,
* PLUSINJECT iniettava il payload in `svchost.exe` usando tecniche di *process hollowing*,
* il malware TOUGHPROGRESS si attivava, collegandosi a Google Calendar per iniziare le operazioni di C2.

## Analisi tecnica di TOUGHPROGRESS

Il malware impiega **shellcode offuscato tramite XOR** con chiavi hardcoded a 16 byte. Una volta decifrato, il codice viene compresso con algoritmo `LZNT1` e caricato dinamicamente. Il tutto avviene in memoria, evitando l’uso del disco e rendendo difficile la rilevazione da parte degli antivirus.

Tra le tecniche di evasione impiegate vi sono:

* indirizzamento indiretto tramite `dispatch tables`,
* overflow controllato dei registri a 64 bit,
* uso di chiamate indirette (*indirect call*) per confondere l’analisi statica.

La comunicazione avviene con la creazione di eventi su Google Calendar a durata zero: i comandi vengono letti dal campo “description”, i risultati cifrati vengono inviati in nuovi eventi. Le date di polling includono il 30 maggio e il 30–31 luglio 2023, suggerendo attività pianificate e controllate a distanza.

## Perché usare Google Calendar come canale C2?

Questa tecnica garantisce numerosi vantaggi:

* il traffico verso `calendar.google.com` appare legittimo,
* non sono necessari domini o server di controllo esposti,
* nessun log di connessione anomalo appare nei sistemi proxy o firewall aziendali,
* la comunicazione avviene su HTTPS, eludendo la maggior parte delle ispezioni.

## Risposta di Google

Google ha reagito rapidamente alla minaccia con le seguenti contromisure:

* rimozione dei calendari e degli account Workspace utilizzati,
* blocco dei file ZIP e LNK coinvolti tramite Safe Browsing,
* condivisione degli hash e delle IOC con le aziende colpite,
* rilascio di firme specifiche per strumenti di threat hunting e detection (es. regole Sigma).

## Chi è APT41?

APT41 è un gruppo sponsorizzato dallo Stato cinese, attivo dal 2012. Si distingue per la sua attività ibrida tra cyber-crimine e cyber-spionaggio, avendo preso di mira settori come sanità, telecomunicazioni, pubblica amministrazione, logistica e media. Già nel 2020 alcuni membri del gruppo sono stati incriminati dal Dipartimento di Giustizia USA per attacchi condotti in tutto il mondo.

## Come difendersi da questi attacchi

Per contrastare minacce di questo livello, è fondamentale adottare un approccio multilivello:

* formare gli utenti sul riconoscimento di email di phishing,
* monitorare le API cloud (Google Calendar incluso),
* implementare EDR/XDR in grado di intercettare esecuzioni in memoria e injection di processo,
* analizzare comportamenti anomali come accessi a calendari non autorizzati,
* integrare feed di threat intelligence aggiornati (ad esempio da SOC Prime).

Il caso TOUGHPROGRESS dimostra quanto gli attaccanti siano capaci di sfruttare risorse legittime in modo creativo per condurre operazioni sofisticate. La sicurezza aziendale moderna deve quindi estendersi oltre il perimetro tradizionale, includendo il monitoraggio continuo di servizi cloud e API legittime. Solo con un approccio proattivo e informato sarà possibile contrastare le nuove forme di malware in evoluzione.

---

##### 1 commento

1. Pingback: Google Calendar sfruttato come Command and Control negli attacchi informatici

##### Lascia un commento [Annulla risposta](/google-calendar-sfruttato-come-command-and-control-negli-attacchi-informatici/?utm_source=rss&utm_medium=rss&utm_campaign=google-calendar-sfruttato-come-command-and-control-negli-attacchi-informatici#respond)

Il tuo indirizzo email non sarà pubblicato. I campi obbligatori sono contrassegnati \*

Commento \*

Nome \*

Email \*

Sito web

[ ]  Salva il mio nome, email e sito web in questo browser per la prossima volta che commento.

[x] Avvisami via email se qualcuno risponde al mio commento.

Δ

![Luca Mercatanti - Le Iene](https://luca-mercatanti.com/wp-content/uploads/2018/05/Luca-Mercatanti-Iene.png)

**Da...