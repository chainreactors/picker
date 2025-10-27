---
title: Come l’FBI ha tentato di intercettare Telegram
url: https://luca-mercatanti.com/come-lfbi-ha-tentato-di-intercettare-telegram/?utm_source=rss&utm_medium=rss&utm_campaign=come-lfbi-ha-tentato-di-intercettare-telegram
source: Luca Mercatanti
date: 2024-07-22
fetch_date: 2025-10-06T17:40:50.005017
---

# Come l’FBI ha tentato di intercettare Telegram

[![Luca Mercatanti](https://luca-mercatanti.com/wp-content/uploads/2020/12/logo.png.webp)](https://luca-mercatanti.com/)

* [Home](http://www.luca-mercatanti.com)
* [Chi sono](https://luca-mercatanti.com/about/)
* [Contatti](https://luca-mercatanti.com/contattami/)
* [Perizie Informatica Forense](https://luca-mercatanti.com/perizie-informatica-forense/)

![Luca Mercatanti - Le Iene](https://luca-mercatanti.com/wp-content/uploads/2018/05/Luca-Mercatanti-Iene.png.webp)

**Dal 2007 mi occupo di Digital** e dal 2010 aiuto professionisti ed imprese nella Comunicazione Digitale e Marketing Online.
**Hacker e Smanettone Tecnologico.**

Dal 2019 sono**assistente in “Comunicazione Digitale”** all’Università Europea di Roma.
Dal Settembre 2007 divulgo le mie scoperte e conoscenze all’interno di questo Blog in forma completamente gratuita.
**Ogni anno ricevo circa 1.600.000 visitatori!**

**[Vuoi scoprire di più? Premi qui!](https://luca-mercatanti.com/about/)**

[![Luca Mercatanti](https://luca-mercatanti.com/wp-content/uploads/2020/12/logo.png.webp)](https://luca-mercatanti.com/)

[![Luca Mercatanti](https://luca-mercatanti.com/wp-content/uploads/2020/12/logo.png.webp)](https://luca-mercatanti.com/)

* [Home](http://www.luca-mercatanti.com)
* [Chi sono](https://luca-mercatanti.com/about/)
* [Contatti](https://luca-mercatanti.com/contattami/)
* [Perizie Informatica Forense](https://luca-mercatanti.com/perizie-informatica-forense/)

[![Luca Mercatanti](https://luca-mercatanti.com/wp-content/uploads/2020/12/logo.png.webp)](https://luca-mercatanti.com/)

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

* [Sicurezza Informatica](https://luca-mercatanti.com/category/web/sicurezza-informatica/)

# Come l’FBI ha tentato di intercettare Telegram

21 Luglio 2024

2 minuti per leggere l'articolo

![](https://luca-mercatanti.com/wp-content/uploads/2024/07/telegram-privacy-800x500.jpg.webp)

In una rara intervista con [Tucker Carlson](https://it.wikipedia.org/wiki/Tucker_Carlson), Pavel Durov, fondatore di Telegram, ha rivelato come l’FBI abbia cercato di convincere gli ingegneri di Telegram (di nascosto, ndr) ad installare componenti Open Source nel codice dell’app che avrebbero permesso di creare delle backdoor per facilitare lo spionaggio.

Durov ha raccontato che, durante una visita negli Stati Uniti, uno dei suoi ingegneri è stato avvicinato da Agenti di sicurezza americani che volevano infiltrarsi nel codice di Telegram, principalmente tentando di convincerlo ad utilizzare delle librerie Open Source che, molto probabilmente, avrebbero poi permesso l’installazione di una backdoor nel sistema di messaggistica.

## Open Source e Backdoor

Uno degli elementi più interessanti di tutta l’intervista è sicuramente il metodo di approccio svolto da parte dell’FBI, così come almeno è stato raccontato dal fondatore di Telegram. Invece di convincere, oppure obbligare, la società a collaborare al fine di intercettare determinati utenti, **gli Agenti hanno tentato di garantirsi un accesso autonomo all’applicazione sfruttando delle librerie [Open Source](https://it.wikipedia.org/wiki/Open_source) di cui sono probabilmente note (o meno) delle falle di sicurezza** che, una volta sfruttate, permettano l’accesso ai database delle applicazioni che le utilizzano (Open Source è un modello di sviluppo software in cui il codice sorgente di un programma è reso disponibile al pubblico. Questo significa che chiunque può vedere, utilizzare, modificare e distribuire il software gratuitamente).
Così facendo, ribadiamo, non solo l’FBI avrebbe avuto accesso autonomo alle conversazioni e dati degli utenti, ma probabilmente **avrebbe permesso anche a Telegram, nel caso in cui eventuali violazioni di privacy fossero venute alla luce, di potersi dissociare/scagionare** in quanto il codice delle librerie utilizzate è libero ed eventuali falle di sicurezza non erano ancora note, nonostante la possibilità per chiunque di analizzare il codice sorgente

## Il ruolo di Google ed Apple

Nell’intervista, Pavel Durov, fa riferimento anche al ruolo giocato da Google ed Apple, sottolineando come **le regole da rispettare per poter vedere la propria applicazione presente sui relativi store (App Store e Play Store) siano spesso la sfida principale a cui far fronte.**
In particolar modo, Durov, per quanto condivida i principi generali a cui dover sottostare, chiarisce come sia complicata l’applicazione e l’interpretazione delle regole:

> Le regole stesse, sono piuttosto generali, giusto? Quindi non ci deve essere violenza, discriminazione, materiale di abuso su minori pubblicamente disponibile. È difficile non essere d’accordo con questo. Sì. Ma poi, quando iniziano ad applicare quelle regole, a volte non siamo d’accordo con le loro interpretazioni. E cerchiamo di tornare a Apple o Google, chiunque sia, e dire, guarda, pensiamo che tu abbia sbagliato. Pensiamo che in realtà questo sia un modo legittimo per le persone di esprimere le loro opinioni. E a volte sono d’accordo, a loro merito. A volte non sono d’accordo e dobbiamo comunque rimuovere del contenuto, almeno nella versione di Telegram distribuita attraverso le loro piattaforme.”

L’intervista di Pavel Durov con Tucker Carlson si conclude, in ogni caso, con Durov che esprime il suo ottimismo sul futuro della privacy e della comunicazione.

##### 2 commenti

1. Pingback: Telegram è rintracciabile dalla Polizia? - Luca Mercatanti
2. Pingback: Come l’FBI ha tentato di intercettare Telegram

##### Lascia un commento [Annulla risposta](/come-lfbi-ha-tentato-di-intercettare-telegram/#respond)

Il tuo indirizzo email non sarà pubblicato. I campi obbligatori sono contrassegnati \*

Commento \*

Nome \*

Email \*

Sito web

[ ]  Salva il mio nome, email e sito web in questo browser per la prossima volta che commento.

[x] Avvisami via email se qualcuno risponde al mio commento.

Δ

![Luca Mercatanti - Le Iene](https://luca-mercatanti.com/wp-content/uploads/2018/05/Luca-Mercatanti-Iene.png.webp)

**Dal 2007 mi occupo di Internet&Web** e dal 2010 aiuto professionisti ed imprese nella Comunicazione Digitale e Marketing Online.

Dal 2019 sono**assistente in “Comunicazione Digitale”** all’Università Europea di Roma.
Dal Settembre 2007 divulgo le mie scoperte e conoscenze all’interno di questo Blog in forma completamente gratuita.

**[Vuoi scoprire di più? Premi qui!](https://luca-mercatanti.com/about/)**

##### Articoli simili

![](https://luca-mercatanti.com/wp-content/uploads/2024/11/cape-privacy-telefonica-mobile-260x195.webp)

Continua

* [Sicurezza Informatica](https://luca-mercatanti.com/category/web/sicurezza-informatica/)

## [Cape: l’operatore telefonico incentrato sulla privacy](https://luca-mercatanti.com/cape-loperatore-telefonico-incentrato-sulla-privacy/)

Chiunque segua con interesse il mondo della cybersecurity sa che i rischi legati alla privacy sono più concreti…

![](https://luca-mercatanti.com/wp-content/uploads/2022/05/tecnologia-passwordless...