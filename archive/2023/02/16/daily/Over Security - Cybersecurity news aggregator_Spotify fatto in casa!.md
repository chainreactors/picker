---
title: Spotify fatto in casa!
url: https://hackerjournal.it/11358/spotify-fatto-in-casa/
source: Over Security - Cybersecurity news aggregator
date: 2023-02-16
fetch_date: 2025-10-04T06:48:01.342758
---

# Spotify fatto in casa!

[![Hackerjournal.it](https://hackerjournal.it/wp-content/uploads/2017/12/hjnegw-1.png)](https://hackerjournal.it/)

* [Forum](https://hackerjournal.it/forum/)
* [News](https://hackerjournal.it/category/news/)
* [Tech](https://hackerjournal.it/category/tecno/)
* [Articoli](https://hackerjournal.it/category/tech/)
* [Trending](https://hackerjournal.it/trending/)
* [Accademia](https://hackerjournal.it/corsi/)
* [Contest](https://hackerjournal.it/contest/)
* [Glossario](https://hackerjournal.it/encyclopedia/)
* [Abbonati](https://hackerjournal.it/81/abbonati-ad-hacker-journal/)
* [Arretrati](https://hackerjournal.it/arretrati-hackerjournal/)

Connect with us

[![Hackerjournal.it](https://hackerjournal.it/wp-content/uploads/2017/12/hjnew-1.png)](https://hackerjournal.it/)
[![Hackerjournal.it](https://hackerjournal.it/wp-content/uploads/2017/12/hjnegw-1.png)](https://hackerjournal.it/)

## Hackerjournal.it

#### Spotify fatto in casa!

* [Forum](https://hackerjournal.it/forum/)
* [News](https://hackerjournal.it/category/news/)

  + [![](https://hackerjournal.it/wp-content/uploads/2025/09/coppadelmondo-400x240.png)

    Mondiali 2026: la truffa corre sul Web](https://hackerjournal.it/14527/mondiali-2026-la-truffa-corre-sul-web/)
  + [![](https://hackerjournal.it/wp-content/uploads/2025/09/massive_npm-400x240.png)

    Il virus che “ruba” il codice](https://hackerjournal.it/14522/il-virus-che-ruba-il-codice/)
  + [![](https://hackerjournal.it/wp-content/uploads/2025/09/stellarium-400x240.jpg)

    Il malware che spia chi visita siti porno](https://hackerjournal.it/14518/il-malware-che-spia-chi-visita-siti-porno/)
  + [![](https://hackerjournal.it/wp-content/uploads/2025/09/kaspesky_corso-400x240.png)

    Un corso online per difendere gli LLM](https://hackerjournal.it/14504/un-corso-online-per-difendere-gli-llm/)
  + [![](https://hackerjournal.it/wp-content/uploads/2025/09/truffa_iphone-400x240.png)

    Truffe online dell’iPhone 17](https://hackerjournal.it/14495/truffe-online-delliphone-17/)
* [Tech](https://hackerjournal.it/category/tecno/)
* [Articoli](https://hackerjournal.it/category/tech/)

  + [![](https://hackerjournal.it/wp-content/uploads/2025/09/deepin_home-400x240.png)

    Linux incontra il design](https://hackerjournal.it/14508/linux-incontra-il-design/)
  + [![](https://hackerjournal.it/wp-content/uploads/2025/09/concetto-di-gestione-delle-relazioni-con-i-clienti-400x240.jpg)

    L’arte di ascoltare le reti](https://hackerjournal.it/14474/larte-di-ascoltare-le-reti/)
  + [![](https://hackerjournal.it/wp-content/uploads/2025/04/attacchi-cibenetici-400x240.jpg)

    Attacchi ai servizi di rete](https://hackerjournal.it/14439/attacchi-ai-servizi-di-rete/)
  + [![](https://hackerjournal.it/wp-content/uploads/2025/08/persona-che-scrive-su-un-primo-piano-del-computer-portatile-400x240.jpg)

    Enumerazione: la vera identità della rete](https://hackerjournal.it/14421/enumerazione-la-vera-identita-della-rete/)
  + [![](https://hackerjournal.it/wp-content/uploads/2025/08/codice-binario-con-globo-sul-computer-portatile-400x240.jpg)

    I migliori tool per la scansione di rete](https://hackerjournal.it/14410/i-migliori-tool-per-la-scansione-di-rete/)
* [Trending](https://hackerjournal.it/trending/)
* [Accademia](https://hackerjournal.it/corsi/)
* [Contest](https://hackerjournal.it/contest/)
* [Glossario](https://hackerjournal.it/encyclopedia/)
* [Abbonati](https://hackerjournal.it/81/abbonati-ad-hacker-journal/)
* [Arretrati](https://hackerjournal.it/arretrati-hackerjournal/)

### [Articoli](https://hackerjournal.it/category/tech/)

# Spotify fatto in casa!

Con il server di streaming musicale mStream si può accedere alla propria raccolta musicale ovunque

![Avatar](https://secure.gravatar.com/avatar/7b274a75782cdb25f96daff3132a6c9c?s=46&d=mm&r=g)

Pubblicato

il

15 Febbraio 2023

By

[hj\_backdoor](https://hackerjournal.it/author/hj_backdoor/ "Articoli scritti da hj_backdoor")

![](https://hackerjournal.it/wp-content/uploads/2023/02/mstream.png)

* Share
* Tweet

**[Mstream](https://mstream.io/) è un server di streaming musicale che permette di sincronizzare la vostra collezione tra i vostri dispositivi per accedervi offline**. Come si legge sul sito del progetto, potete “considerare mStream come il vostro [cloud privato](https://hackerjournal.it/11297/servizi-cloud-di-ia-pronti-alluso/)”. È possibile utilizzarlo per trasmettere facilmente la propria musica dal computer di casa a qualsiasi dispositivo e fare l’hosting del proprio server consente un’esperienza più personalizzata, senza pubblicità o servizi di streaming che raccolgono statistiche sulle abitudini di ascolto. Potete anche trasmettere la vostra musica non compressa per ottenere la massima qualità. Il server è relativamente facile da usare mStream e non pesa molto su memoria e CPU. **I formati di file supportati sono flac, mp3, mp4, wav, ogg, opus, aac e m4a**. È possibile eseguirlo su un computer Linux o su schede ARM come la Raspberry Pi. Implementare un server mStream è semplice. Clonatelo da Git con:

**git clone https://github.com/IrosTheBeggar/**

**mStream.git**

**cd mStream**

Quindi installate le dipendenze ed eseguitelo con:

**npm run-script wizard**

Dei player per dispositivi mobili iOS e [Android](https://play.google.com/store/) sono disponibili nei rispettivi store.

Related Topics:[cloud](https://hackerjournal.it/tag/cloud/)[mstream](https://hackerjournal.it/tag/mstream/)[streaming audio](https://hackerjournal.it/tag/streaming-audio/)

[Up Next

La distro leggera basata su Slackware](https://hackerjournal.it/11324/la-distro-leggera-basata-su-slackware/)

[Don't Miss

Creare malware utilizzando ChatGPT](https://hackerjournal.it/11354/creare-malware-utilizzando-chatgpt/)

![Avatar](https://secure.gravatar.com/avatar/7b274a75782cdb25f96daff3132a6c9c?s=60&d=mm&r=g)

[hj\_backdoor](https://hackerjournal.it/author/hj_backdoor/ "Articoli scritti da hj_backdoor")

![](https://hackerjournal.it/wp-content/uploads/2017/12/hjnew-1.png)

[wpdevart\_facebook\_comment curent\_url="http://developers.facebook.com/docs/plugins/comments/" order\_type="social" title\_text="Facebook Comment" title\_text\_color="#000000" title\_text\_font\_size="22" title\_text\_font\_famely="monospace" title\_text\_position="left" width="100%" bg\_color="#d4d4d4" animation\_effect="random" count\_of\_comments="7" ]

### [Articoli](https://hackerjournal.it/category/tech/)

# Linux incontra il design

Dalle finestre arrotondate alla sicurezza avanzata con snapshot automatici, fino al nuovo formato Linyaps compatibile con Ubuntu e Debian: ecco perché Deepin 25 non è una distro qualsiasi

![Avatar](https://secure.gravatar.com/avatar/7b274a75782cdb25f96daff3132a6c9c?s=46&d=mm&r=g)

Pubblicato

il

26 Settembre 2025

By

[hj\_backdoor](https://hackerjournal.it/author/hj_backdoor/ "Articoli scritti da hj_backdoor")

![](https://hackerjournal.it/wp-content/uploads/2025/09/deepin_home.png)

Basato su Debian e sviluppato dalla società cinese Deepin Technology, questo sistema operativo è noto per la
sua grande stabilità, per la sua innegabile qualità estetica e per la sua facilità d’uso. Il progetto, che ha mosso i suoi primi passi nel 2004, ha sempre avuto come obiettivo quello di fornire un’esperienza di ottimo livello sia a utenti già esperti del mondo Linux sia a un pubblico neofita. Questa nuova versione viene presentata con lo slogan Tutto Avanti, Tutto Rinnovato, per sottolineare i tanti miglioramenti introdotti dagli sviluppatori. La ISO può essere scaricata da [qui](https://www.deepin.org/en/download/).

### La nuova versione

Numerose, infatti, sono le novità che questa versione del sistema operativo cinese offre ai propri utenti, a cominciare dall’**Ambiente Desktop Deepin (DDE) 7.0**. Si tratta di un’interfaccia completamente ridisegnata per renderla ancora più elegante e gradevole all’uso. Per ottenere questo risultato, gli sviluppatori hanno usato il linguaggio di programmazione QML (Qt Modeling Languag...