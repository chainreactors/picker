---
title: Cos'è Il Reentrancy Attack: Come Vengono Drenati I Pools (DeFi)
url: http://darkwhite666.blogspot.com/2026/05/cose-il-reentrancy-attack-come-vengono.html
source: Dark Space Blogspot
date: 2026-05-03
fetch_date: 2026-05-04T05:32:58.432042
---

# Cos'è Il Reentrancy Attack: Come Vengono Drenati I Pools (DeFi)

## Visualizzazioni Totali

[![Dark Space Blogspot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZgt0RUZjHgbkLsu7CbFNAiyAMd0qvDL2fubvcBv5c6R04keICe8K0ig6oXxzqa6519xC3S7eBHP3_F60rvo_NqafkHR83xyZwscmsQgwCw_EPQpiDWkgarGw08kUDwteX-zWL_I_uP1w/s1600/ask-fm.png)](https://darkwhite666.blogspot.com/)

TRA I PRIMI IN ITALIA A PARLARE DI BITCOIN (DAL 2012!): PER ESSERE SEMPRE AGGIORNATI SULLE NOVITA' TECNOLOGICHE DEL WEB SEGUITE LA PAGINA FACEBOOK (LINK A SINISTRA)

## domenica 3 maggio 2026

### Cos'è Il Reentrancy Attack: Come Vengono Drenati I Pools (DeFi)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjq_Ji-lpOnlo7NoS7U6yEbMQsOEc4g7F4l6qgmlFgToJf7xmd-TiaJWJ2GBM-UkQcVWURxNcw_FdxMy0nCfgnrjQTSAd_TiK_DFDVn3XhPdEsmPUibaDAg0RSL5AlQ5cLg3JuqoUqDa8ajxyTSxEzlODIJKAsgsy6BOgYFt74Y86oZwk218o6TrgWGkLo/s320/Reentrancy%20Attack.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjq_Ji-lpOnlo7NoS7U6yEbMQsOEc4g7F4l6qgmlFgToJf7xmd-TiaJWJ2GBM-UkQcVWURxNcw_FdxMy0nCfgnrjQTSAd_TiK_DFDVn3XhPdEsmPUibaDAg0RSL5AlQ5cLg3JuqoUqDa8ajxyTSxEzlODIJKAsgsy6BOgYFt74Y86oZwk218o6TrgWGkLo/s517/Reentrancy%20Attack.png)

Il **Reentrancy Attack** è un tipo di vulnerabilità molto pericolosa negli smart contracts in cui un attaccante sfrutta una chiamata ricorsiva di un contratto prima che la sua precedente transazione sia completamente eseguita. Sostanzialmente viene sfruttata una funzione del contratto che effettua chiamate esterne ad altri contratti ma non aggiorna immediatamente lo stato del contratto prima di completare queste chiamate esterne. L'attaccante richiama la stessa funzione più volte (in modo ricorsivo, tipo loop) prima che lo smart contract possa aggiornare il suo stato, eseguendo così più prelievi (o operazioni che non dovrebbero essere possibili).

COME AVVIENE L'ATTACCO

Il contratto ha una funzione che permette agli utenti di prelevare fondi (ad esempio, una funzione withdraw), in base al loro saldo. Il contratto effettua una chiamata esterna per trasferire fondi a un altro indirizzo (ad esempio, usando la funzione send). Lo stato del contratto non viene aggiornato immediatamente: la chiamata esterna avviene, permettendo all'attaccante di eseguire azioni prima che il saldo venga ridotto. L'attaccante, grazie alla possibilità di usufruire di una chiamata esterna, esegue nuovamente la funzione di prelievo, causando così più prelievi prima che il saldo venga aggiornato.

Se consideriamo uno smart contract di un wallet che consente agli utenti di depositare e prelevare fondi, un attaccante può sfruttare questo contratto utilizzando questa funziona ricorsiva. Gli utenti possono depositare fondi nel contratto e prelevarli tramite la funzione withdraw, che invia i fondi all'utente e poi aggiorna il suo saldo. L'attaccante crea un contratto che sfrutta la funzione withdraw per richiamarla più volte. L'attaccante richiama la funzione attack nel contratto malevolo, depositando fondi nel contratto vulnerabile. La funzione withdraw del contratto vulnerabile invia i fondi all'indirizzo dell'attaccante, il quale può eseguire un'altra chiamata ricorsiva a withdraw prima che il saldo venga aggiornato. In questo modo, l'attaccante può ripetere l'operazione più volte, prelevando fondi multipli rispetto al suo saldo spettante. Ogni volta che l'attaccante richiama la funzione withdraw, il contratto vulnerabile non ha ancora aggiornato il saldo dell'attaccante. Ciò consente all'attaccante di prelevare ripetutamente più fondi di quelli realmente depositati. Ipotizza di depositare 1 ETH nel contratto, quando l'attaccante chiama la funzione withdraw per la prima volta, riceve 1 ETH, ma lo stato del contratto non è ancora aggiornato. L'attaccante richiama ricorsivamente withdraw e riceve altri 1 ETH e così via. Ogni ciclo di chiamate drena fondi dal contratto (di altri utenti), che non riesce ad aggiornare correttamente il saldo dell'attaccante in tempo reale.

PREVENIRE QUESTI ATTACCHI

Per prevenire questi pericolosi attacchi, la regola fondamentale è aggiornare lo stato del contratto prima di effettuare qualsiasi chiamata esterna cioè basta spostare la riga che aggiorna il saldo dell'utente prima della chiamata esterna. Funzioni di check controllano le condizioni (ad esempio, se l'utente ha abbastanza saldo).

Pubblicato da
[DarkDave.|.666](https://www.blogger.com/profile/02696807736631988356 "author profile")

alle
[09:19](https://darkwhite666.blogspot.com/2026/05/cose-il-reentrancy-attack-come-vengono.html "permanent link")

[![](//img1.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/1856644955194422917/1775611344873103287 "Post per email")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=1856644955194422917&postID=1775611344873103287&from=pencil "Modifica post")

[Invia tramite email](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=1775611344873103287&target=email "Invia tramite email")[Postalo sul blog](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=1775611344873103287&target=blog "Postalo sul blog")[Condividi su X](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=1775611344873103287&target=twitter "Condividi su X")[Condividi su Facebook](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=1775611344873103287&target=facebook "Condividi su Facebook")[Condividi su Pinterest](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=1775611344873103287&target=pinterest "Condividi su Pinterest")

Etichette:
[Cripto](https://darkwhite666.blogspot.com/search/label/Cripto),
[DeFi](https://darkwhite666.blogspot.com/search/label/DeFi),
[Hacking](https://darkwhite666.blogspot.com/search/label/Hacking)

#### Nessun commento:

#### Posta un commento

[Post più vecchio](https://darkwhite666.blogspot.com/2026/04/le-truffe-piu-diffuse-ai-e-call-center.html "Post più vecchio")
[Home page](https://darkwhite666.blogspot.com/)

Iscriviti a:
[Commenti sul post (Atom)](https://darkwhite666.blogspot.com/feeds/1775611344873103287/comments/default)

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
* [✅Articoli Vecchie Tecnologie, AI, Collezio...