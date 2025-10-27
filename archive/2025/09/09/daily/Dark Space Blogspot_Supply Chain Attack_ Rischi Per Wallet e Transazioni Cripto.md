---
title: Supply Chain Attack: Rischi Per Wallet e Transazioni Cripto
url: http://darkwhite666.blogspot.com/2025/09/supply-chain-attack-rischi-per-wallet-e.html
source: Dark Space Blogspot
date: 2025-09-09
fetch_date: 2025-10-02T19:53:28.545255
---

# Supply Chain Attack: Rischi Per Wallet e Transazioni Cripto

## Visualizzazioni Totali

[![Dark Space Blogspot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZgt0RUZjHgbkLsu7CbFNAiyAMd0qvDL2fubvcBv5c6R04keICe8K0ig6oXxzqa6519xC3S7eBHP3_F60rvo_NqafkHR83xyZwscmsQgwCw_EPQpiDWkgarGw08kUDwteX-zWL_I_uP1w/s1600/ask-fm.png)](https://darkwhite666.blogspot.com/)

TRA I PRIMI IN ITALIA A PARLARE DI BITCOIN (DAL 2012!): PER ESSERE SEMPRE AGGIORNATI SULLE NOVITA' TECNOLOGICHE DEL WEB SEGUITE LA PAGINA FACEBOOK (LINK A SINISTRA)

## lunedì 8 settembre 2025

### Supply Chain Attack: Rischi Per Wallet e Transazioni Cripto

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjtKFNMmI89GJY17bTrzpGOF18fZOT9jSXTBKImHBz9qJBnhoMmYE1Ib-gQV1diK8uJ9eo_fhL8Fkad1EYGAVcdZkzZVkmPIuWA9MiVeTnCMyo3410cnqBYd6e3_4y44srJsGS_hBHpirUeNl-75JTtkApd9J0pkhG8JOohG_9a1oOAfP81ZHwWnTcDvhQ/s320/Supply%20Chain.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjtKFNMmI89GJY17bTrzpGOF18fZOT9jSXTBKImHBz9qJBnhoMmYE1Ib-gQV1diK8uJ9eo_fhL8Fkad1EYGAVcdZkzZVkmPIuWA9MiVeTnCMyo3410cnqBYd6e3_4y44srJsGS_hBHpirUeNl-75JTtkApd9J0pkhG8JOohG_9a1oOAfP81ZHwWnTcDvhQ/s464/Supply%20Chain.jpg)

Oggi, 8 settembre 2025, è andato in scena un attacco su larga scala alla **supply chain di NPM** (che gestisce pacchetti Javascript). Un attaccante ha pubblicato versioni malevole di pacchetti molto diffusi, tra cui error-ex, has-ansi, color-convert, strip-ansi, is-core-module colpendo siti web, CLI e framework (in modo silenzioso).

Cosa fa il malware?

1) Monkey Patching (alterazione delle funzioni nel sito web senza modificare il codice sorgente), scansione di wallet cripto, Levenshtein distance algoritmo (sostituisce gli address con altri visivamente simili. Ad esempio 0x87d...3ad apparirà come 0x87d...3ad, la modifica sta nel mezzo).

2) Intercetta transazioni e le manipola, modifica i dati in memoria (sostituendo address del destinatario o dello smart contract con quello dell'attaccante).

Se un sito web installa una delle versioni malevole dei pacchetti compromessi, il codice malevolo viene eseguito nel runtime dell’applicazione (Node.js server-side sia per applicazioni front-end distribuite su browser tipo i wallet).

QUALI SONO I RISCHI?

Ogni volta che scrivi, copi/incolli o invii un indirizzo di portafoglio (es. Metamask, Phantom, etc), il malware controlla la stringa.

Se trova un indirizzo, lo sostituisce con uno degli indirizzi dell’attaccante. La sostituzione è fatta con address visivamente simili (simile al Poisonous Attack dove vengono inviati piccoli importi, dust, da un address visivamente simile a quello della vittima, in modo tale che se quest'ultimo effettua operazioni di routine tipo invii agli stessi address magari fa "copia e incolla" dell'address sbagliato).

Dunque se apri MetaMask o Phantom, il malware intercetta le chiamate API (eth\_sendTransaction, ecc.). Quando provi a fare una transazione su una dapp affetta (invio fondi), l’indirizzo del destinatario viene modificato in memoria prima che tu firmi la transazione. Se swappi su un dex, sostituisce address dello smart contract con quello dell'attaccante (intercettando dati in uscita e in entrata). Se tu non hai installato il malware non corri rischi, sempre se nel mentre non usi wallet e invii fondi in giro (in quel caso interagendo con una dapp infetta). Meglio aspettare patch e la risoluzione del problema.

JAVASCRIPT

Chiaramente ad esser colpito non è solo il mondo cripto ma anche tutti i siti web che usano quelle librerie, tuttavia lì non ci sono fondi da rubare non essendo avviate transazioni. Ciò che succede è l'interruzione delle funzionalità o errori (come il "fetch is not defined" che ha fatto scattare l’allarme).

Pubblicato da
[DarkDave.|.666](https://www.blogger.com/profile/02696807736631988356 "author profile")

alle
[23:27](https://darkwhite666.blogspot.com/2025/09/supply-chain-attack-rischi-per-wallet-e.html "permanent link")

[![](//img1.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/1856644955194422917/8427114035936716103 "Post per email")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=1856644955194422917&postID=8427114035936716103&from=pencil "Modifica post")

[Invia tramite email](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=8427114035936716103&target=email "Invia tramite email")[Postalo sul blog](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=8427114035936716103&target=blog "Postalo sul blog")[Condividi su X](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=8427114035936716103&target=twitter "Condividi su X")[Condividi su Facebook](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=8427114035936716103&target=facebook "Condividi su Facebook")[Condividi su Pinterest](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=8427114035936716103&target=pinterest "Condividi su Pinterest")

Etichette:
[Cripto](https://darkwhite666.blogspot.com/search/label/Cripto),
[DeFi](https://darkwhite666.blogspot.com/search/label/DeFi),
[Hacking](https://darkwhite666.blogspot.com/search/label/Hacking),
[Malware](https://darkwhite666.blogspot.com/search/label/Malware),
[Wallet](https://darkwhite666.blogspot.com/search/label/Wallet)

#### Nessun commento:

#### Posta un commento

[Post più recente](https://darkwhite666.blogspot.com/2025/09/libri-e-saghe-dark-romance-piu-amate-su.html "Post più recente")

[Post più vecchio](https://darkwhite666.blogspot.com/2025/09/case-prefabbricate-vendute-su-amazon.html "Post più vecchio")
[Home page](https://darkwhite666.blogspot.com/)

Iscriviti a:
[Commenti sul post (Atom)](https://darkwhite666.blogspot.com/feeds/8427114035936716103/comments/default)

## Segui la nostra pagina Facebook:

* [Dark Space Blogspot (Facebook)](https://www.facebook.com/DarkSpaceBlogspot/)

## Politica Privacy Sito

* [Politica Privacy (Cookies)](http://darkwhite666.blogspot.it/2015/06/politica-dei-cookie-di-questo-sito-in.html)

## Indice Completo Articoli Blog (In Aggiornamento)

* [✅Articoli Audio, Video, Youtube e File Hosting](https://darkwhite666.blogspot.com/2020/08/articoli-audio-video-youtube-e-file.html)
* [✅Articoli Bitcoin e Criptovalute](https://darkwhite666.blogspot.com/2019/12/tutti-gli-articoli-su-bitcoin-e.html)
* [✅Articoli Browser, Motori Ricerca, Internet, Servizi Generici](https://darkwhite666.blogspot.com/2020/08/articoli-browser-motori-ricerca.html)
* [✅Articoli Connessione Internet, Router, Hardware, Software](https://darkwhite666.blogspot.com/2020/08/articoli-connessione-internet-router.html)
* [✅Articoli Deep Web](http://darkwhite666.blogspot.it/2014/10/tutti-gli-articoli-sul-deep-web-indice.html)
* [✅Articoli eCommerce, eBay, Amazon](https://darkwhite666.blogspot.com/2020/08/articoli-ecommerce-ebay-amazon-indice.html)
* [✅Articoli Editor Foto, Fotomontaggi, Videogame, Storie Creepy](https://darkwhite666.blogspot.com/2020/08/articoli-editor-foto-fotomontaggi.html)
* [✅Articoli Fisica, Matematica, Elettronica](https://darkwhite666.blogspot.com/2020/08/articoli-fisica-matematica-ed.html)
* [✅Articoli Rimozione Malware, Crittografia, Anonimato, Storie Hacker](https://darkwhite666.blogspot.com/2020/08/articoli-rimozione-malware-privacy.html)
* [✅Articoli SEO, Creazione Siti Internet, Programmazione, Sistemi Operativi](https://darkwhite666.blogspot.com/2020/08/articoli-seo-creazione-siti-internet.html)
* [✅Articoli Social Network (Facebook, Instagram, TikTok, WhatsApp)](https://darkwhite666.blogspot.com/2020/08/articoli-social-network-askfm-facebook.html)
* [✅Articoli Vecchie e Nuove Tecnologie](https://darkwhite666.blogspot.com/2020/08/articoli-vecchie-e-nuove-tecnologie-dal.html)

## Archivio blog

* ▼
  [2025](https://darkwhite666.blogspot.com/2025/)
  (45)
  + ▼
    [settembre](https://darkwhite666.blogspot.com/2025/09/)
    (6)
    - [Sintomi Componenti Hardware Danneggiati (Laptop)](https://darkwhite666.blogspot.com/2025/09/sintomi-compone...