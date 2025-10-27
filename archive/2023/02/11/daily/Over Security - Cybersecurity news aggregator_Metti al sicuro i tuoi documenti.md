---
title: Metti al sicuro i tuoi documenti
url: https://hackerjournal.it/11320/metti-al-sicuro-i-tuoi-documenti/
source: Over Security - Cybersecurity news aggregator
date: 2023-02-11
fetch_date: 2025-10-04T06:23:08.434030
---

# Metti al sicuro i tuoi documenti

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

#### Metti al sicuro i tuoi documenti

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

# Metti al sicuro i tuoi documenti

AES Crypt è un software Open Source che permette di proteggere file importanti (tramite crittografia) da occhi indiscreti

![Avatar](https://secure.gravatar.com/avatar/7b274a75782cdb25f96daff3132a6c9c?s=46&d=mm&r=g)

Pubblicato

il

10 Febbraio 2023

By

[hj\_backdoor](https://hackerjournal.it/author/hj_backdoor/ "Articoli scritti da hj_backdoor")

![](https://hackerjournal.it/wp-content/uploads/2023/02/aes_crypt.png)

* Share
* Tweet

[AES Crypt](https://www.aescrypt.com/) è un software di criptazione dei file che **utilizza l’algoritmo [Advanced Encryption Standard](https://hackerjournal.it/2724/wpa3-la-vulnerabilita-arriva-prima-del-lancio/) (AES)**, **ossia quello usato come standard dal governo USA per la sua potenza**. Il programma mira a rendere il suo utilizzo facile. Per crittografare un file, basta fare clic con il tasto destro o sinistro (a seconda del desktop) su di esso e aprirlo con AES Crypt. A questo punto vi viene richiesto di inserire la password desiderata e l’applicazione produce un file che non può essere letto da nessuno che non la conosca. Per eseguire la stessa operazione dal terminale è sufficiente inserire il comando **aescrypt** con gli argomenti della riga di comando appropriati.
**Per esempio, supponiamo di avere un file chiamato contratto.jpg da crittografare con la password 32124G**.

Si immette il seguente comando:

**aescrypt -e -p 32124G contratto.jpg**

Questo è quanto! Il programma crea un file con il nome **contratto.jpg.aes**. Quando volete decriptarlo, se usate l’interfaccia grafica dovete semplicemente fare doppio clic sul file **.aes** e inserire la vostra password segreta quando vi viene richiesta. **Dal terminale si deve invece immettere il seguente comando:**

**aescrypt -d -p 32124G contratto.jpg.aes**

Se usate **AES Crypt** per decriptare un file in un ufficio con altre persone e non volete mostrare la password sulla riga di comando, basta escludere il parametro -p in questo modo:

**aescrypt -d contratto.jpg.aes**

Il programma chiederà la password ma quando la inserirete non verrà visualizzata sullo schermo.

Related Topics:

[Up Next

Messaggi segreti a prova di spia](https://hackerjournal.it/11339/messaggi-segreti-a-prova-di-spia/)

[Don't Miss

Uperfect X Pro LapDock, la recensione](https://hackerjournal.it/11349/uperfect-x-pro-lapdock-la-recensione/)

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

Numerose, infatti, sono le novità che questa versione del sistema operativo cinese offre ai propri utenti, a cominciare dall’**Ambiente Desktop Deepin (DDE)...