---
title: OpenRecall: l’alternativa Open Source a Microsoft Recall
url: https://luca-mercatanti.com/openrecall-lalternativa-open-source-a-microsoft-recall/?utm_source=rss&utm_medium=rss&utm_campaign=openrecall-lalternativa-open-source-a-microsoft-recall
source: Luca Mercatanti
date: 2024-08-11
fetch_date: 2025-10-06T18:03:20.316088
---

# OpenRecall: l’alternativa Open Source a Microsoft Recall

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

* [Windows](https://luca-mercatanti.com/category/windows/)

# OpenRecall: l’alternativa Open Source a Microsoft Recall

10 Agosto 2024

2 minuti per leggere l'articolo

![Logo di OpenRecall](https://luca-mercatanti.com/wp-content/uploads/2024/08/openrecall-800x500.jpg)

Microsoft Recall è probabilmente [tra i primi progetti](https://learn.microsoft.com/it-it/windows/ai/apis/recall) a sfruttare le funzioni dei computer dotati di Copilot+, ovvero tutti quei dispositivi dotati da un’unità di elaborazione neurale (NPU). Fin dai primi giorni del rilascio, **molte sono la state le critiche, relativamente alla privacy,** mosse a questo strumento. In particolar modo, i problemi principali hanno riguardato il modo in cui i dati di Recall vengono memorizzati all’intero del dispositivo: in chiaro, senza alcun tipo di cifratura. In effetti, b[asta davvero poco](https://doublepulsar.com/recall-stealing-everything-youve-ever-typed-or-viewed-on-your-own-windows-pc-is-now-possible-da3e12e9465e) per accedere ai dati memorizzati.

> This is a Black Mirror episode.
>
> Definitely turning this “feature” off. <https://t.co/bx1KLqLf67>
>
> — Elon Musk (@elonmusk) [May 20, 2024](https://twitter.com/elonmusk/status/1792690964672450971?ref_src=twsrc%5Etfw)

Altresì, per quanto possa essere utile Microsoft Recall, questo non è disponibile per tutti i computer ed anzi, è supportato da un minima parte (per l’appunto, quelli dotati di NPU). **Per far fronte a queste problematiche di privacy e compatibilità**, è nato un progetto open source denominato “[Open Recall](https://github.com/openrecall/openrecall)” e presente su GitHub. Secondo gli sviluppatori:

> OpenRecall è un’alternativa completamente open source e privacy-first a soluzioni proprietarie come Windows Recall di Microsoft o Rewind.ai di Limitless. Con OpenRecall, puoi accedere facilmente alla tua cronologia digitale, migliorando la tua memoria e produttività senza compromettere la tua privacy.

## Microsoft Recall VS OpenRecall

![Comparazione tra Microsoft Recall e sistemi similari](https://luca-mercatanti.com/wp-content/uploads/2024/08/microsoft-recall-vs-openrecall-1024x402.jpg)

OpenRecall, al pari di Microsoft Recall, **effettua una registrazione continua dello schermo (mediante una serie di screenshot a distanza di pochi secondi l’uno dall’altro), rendendo poi il testo ricercabile mediante tecnologia del riconoscimento del testo (OCR).**
A differenza dello strumento ufficiale di Microsoft, i dati ed il sistema di indicizzazione ed analisi è completamente open source e risiede all’interno di precise cartelle all’interno del proprio computer. Altresì, come chiarito all’interno della documentazione presente su GitHub, è possibile cifrare la cartella in cui tutti i dati vengono memorizzati, così da aumentare sensibilmente il livello di privacy dei dati memorizzati.
OpenRecall, altresì, è compatibile non solamente con il sistema operativo Windows, **ma anche con Linux e MacOS.**

## Installazione di OpenRecall

Nel momento in cui questo articolo è stato pubblicato, l’installazione di OpenRecall avviene da riga di comando, sfruttando Python. Nella Roadmap del progetto è però previsto, a stretto giro, la realizzazione di un sistema di installazione automatico, come per la maggior parte delle applicazioni che siamo abituati ad utilizzare.
Nel caso vogliate già provare il sistema, vi basterà seguire il tutorial presente all’interno del progetto GitHub, procedura che richiede non più di qualche minuto.

##### Lascia un commento [Annulla risposta](/openrecall-lalternativa-open-source-a-microsoft-recall/?utm_source=rss&utm_medium=rss&utm_campaign=openrecall-lalternativa-open-source-a-microsoft-recall#respond)

Il tuo indirizzo email non sarà pubblicato. I campi obbligatori sono contrassegnati \*

Commento \*

Nome \*

Email \*

Sito web

[ ]  Salva il mio nome, email e sito web in questo browser per la prossima volta che commento.

[x] Avvisami via email se qualcuno risponde al mio commento.

Δ

![Luca Mercatanti - Le Iene](https://luca-mercatanti.com/wp-content/uploads/2018/05/Luca-Mercatanti-Iene.png)

**Dal 2007 mi occupo di Internet&Web** e dal 2010 aiuto professionisti ed imprese nella Comunicazione Digitale e Marketing Online.

Dal 2019 sono**assistente in “Comunicazione Digitale”** all’Università Europea di Roma.

**[Vuoi scoprire di più? Premi qui!](https://luca-mercatanti.com/about/)**

[Luca Mercatanti](https://luca-mercatanti.com/)

Copyright © 2007 - 2021 Luca Mercatanti's Blog. Tutti i diritti riservati | [Privacy Policy](https://luca-mercatanti.com/privacy-policy)