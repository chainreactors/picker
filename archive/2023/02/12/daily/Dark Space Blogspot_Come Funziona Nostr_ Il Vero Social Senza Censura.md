---
title: Come Funziona Nostr: Il Vero Social Senza Censura
url: http://darkwhite666.blogspot.com/2023/02/come-funziona-nostr-il-vero-social.html
source: Dark Space Blogspot
date: 2023-02-12
fetch_date: 2025-10-04T06:27:00.053744
---

# Come Funziona Nostr: Il Vero Social Senza Censura

## Visualizzazioni Totali

[![Dark Space Blogspot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZgt0RUZjHgbkLsu7CbFNAiyAMd0qvDL2fubvcBv5c6R04keICe8K0ig6oXxzqa6519xC3S7eBHP3_F60rvo_NqafkHR83xyZwscmsQgwCw_EPQpiDWkgarGw08kUDwteX-zWL_I_uP1w/s1600/ask-fm.png)](https://darkwhite666.blogspot.com/)

TRA I PRIMI IN ITALIA A PARLARE DI BITCOIN (DAL 2012!): PER ESSERE SEMPRE AGGIORNATI SULLE NOVITA' TECNOLOGICHE DEL WEB SEGUITE LA PAGINA FACEBOOK (LINK A SINISTRA)

## sabato 11 febbraio 2023

### Come Funziona Nostr: Il Vero Social Senza Censura

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEge2A5SARLJG62CrJTMDE79JpyPhSn7f9aft4W8rVCcqLBUJ4Yz0o45kElGeKMW7nD0iBwEcX-CdOMk4e8VMm9IAUPK68LfQOihoMXBqLrlxas_sz9vWylRJzo7SWWVO6_iFDNgRYotBaiTv2rTrK9vtGtp8eXZjCxzIrgrIRArWI0x1UwZMiMyGObh/w400-h200/download.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEge2A5SARLJG62CrJTMDE79JpyPhSn7f9aft4W8rVCcqLBUJ4Yz0o45kElGeKMW7nD0iBwEcX-CdOMk4e8VMm9IAUPK68LfQOihoMXBqLrlxas_sz9vWylRJzo7SWWVO6_iFDNgRYotBaiTv2rTrK9vtGtp8eXZjCxzIrgrIRArWI0x1UwZMiMyGObh/s318/download.jpg)

L'idea di **[Nostr](https://nostr.com/)** è quella di creare un social network decentralizzato, resistente alla censura. Infatti su Nostr non c'è alcuna censura di contenuti, non c'è un ente che decide cosa può essere pubblicato e cosa no. Può essere molto utile per diffondere informazioni (ma anche fake news a questo punto) senza che un ente possa censurarle (quello che fa Twitter, Facebook, Youtube ad esempio) ma anche per implementare un sistema di pagamento (che comunque puoi utilizzare già con Bitcoin).

Non c'è alcuna necessità di dare mail, numeri di cellulare e dati personali. Questo social è basato su crittografia e firme digitali ed utilizza un client utile a creare una coppia di chiavi: una pubblica ed una privata. Per pubblicare un post (nota) devo firmarla con una chiave privata, essa poi viene inviata ad un relay (sono tipo server messi a disposizione da volontari) che la riceve, salva su disco e la condivide. I client verificano anche che ogni nota non sia stata compromessa e sia stata firmata correttamente, ciò impedisce che il dato venga manomesso. I vari relay mettono in comunicazione tutti gli utenti (client) condividendo appunto le note pubblicate da altri utenti. I contenuti sono validati dai relay che teoricamente li dovrebbero condividere senza censurarli. Chiunque può crearsi un relay e condividere comunque quella informazione. Il grosso problema è che, ad oggi, non ci sono incentivi economici per tenere attivo un relay.

CLIENT DA USARE

Non esiste un web server/dominio centralizzato. E' possibile utilizzare Nostr con tanti web client e creare facilmente più identità (proprio come posso creare più indirizzi di un wallet). L'infrastruttura è formata da client (sono tipo wallet che firmano ed inviano note), relay (entità che ricevono dati e li condividono, i dati sono crittografati end to end e non sono accessibili) ed utenti ovviamente (account con chiave privata/pubblica).

Tra i client più noti troviamo **[Snort](https://snort.social/login)** (computer ed Android), effettuando il login posso generare una chiave privata online schiacciando su "generate key" oppure la posso generare utilizzando l'estensione Chrome **[Nos2x](https://chrome.google.com/webstore/detail/nos2x/kpgefcfmnafjgpblomihpgmejjdanjjp)**. La chiave privata, una volta generata, va salvata. Essa rappresenta la vostra identità digitale su Nostr. Se ho usato l'estensione, da Snort posso fare il login appunto con quest'estensione ed autorizzare la connessione per un tempo variabile (5 minuti, solo per adesso, per sempre). Questa è la registrazione.

Poi posso aggiornare il profilo scrivendo nome, nick, biografia, immagine profilo, etc

Posso inserire anche un indirizzo Lightning Network (Wallet Of Satoshi ad esempio, qui trovi una [**lista di LightningAddress**](https://lightningaddress.com/), inserirò una mail) per ricevere "tip" (a grandi linee quello che succede con Brave Browser), cioè dei pagamenti. Per ogni interazione devo autorizzare tramite la firma digitale.

Per approfondire su questo layer2 di Bitcoin: [**Come Funziona Lightning Network: Basse Fee e Privacy**](https://darkwhite666.blogspot.com/2022/10/come-funziona-lightning-network-basse.html)

Un altro client è [**Astral Ninja**](https://astral.ninja/) dal quale posso effettuare il login sempre con la stessa estensione oppure generare un'altra identità digitale quindi una chiave privata. Se uso la stessa estensione, i miei dati immessi su Snort me li ritroverò anche qui perchè l'identità (chiave privata/pubblica) è la stessa. Tramite questo web client è più semplice cercare i profili da seguire.

Altri client: [**Amethyst**](https://play.google.com/store/apps/details?id=com.vitorpamplona.amethyst&hl=en) (Android), [**Damus**](https://apps.apple.com/ca/app/damus/id1628663131) (iPhone) ed [**Iris**](https://iris.to/) (web)

ALTRI CRYPTO SOCIAL

Qualcosa di simile era stata fatta già da [**Deso (Decentralized Social)**](https://signup.deso.com/). Sempre connesso al mondo Crypto ma non social decentralizzato in quanto basato su credenziali di accesso troviamo il social [**Torum**](https://www.torum.com/?referral_code=omegablack666) che permette anche di guadagnare il token nativo della piattaforma postando contenuti e svolgendo alcune operazioni.

Pubblicato da
[DarkDave.|.666](https://www.blogger.com/profile/02696807736631988356 "author profile")

alle
[10:20](https://darkwhite666.blogspot.com/2023/02/come-funziona-nostr-il-vero-social.html "permanent link")

[![](//img1.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/1856644955194422917/6726236293733802020 "Post per email")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=1856644955194422917&postID=6726236293733802020&from=pencil "Modifica post")

[Invia tramite email](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=6726236293733802020&target=email "Invia tramite email")[Postalo sul blog](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=6726236293733802020&target=blog "Postalo sul blog")[Condividi su X](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=6726236293733802020&target=twitter "Condividi su X")[Condividi su Facebook](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=6726236293733802020&target=facebook "Condividi su Facebook")[Condividi su Pinterest](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=6726236293733802020&target=pinterest "Condividi su Pinterest")

Etichette:
[Bitcoin](https://darkwhite666.blogspot.com/search/label/Bitcoin),
[Social Network](https://darkwhite666.blogspot.com/search/label/Social%20Network)

#### Nessun commento:

#### Posta un commento

[Post più recente](https://darkwhite666.blogspot.com/2023/02/crypto-inerenti-intelligenza.html "Post più recente")

[Post più vecchio](https://darkwhite666.blogspot.com/2023/02/doodles-i-dooplicator-e-doodles-2-come.html "Post più vecchio")
[Home page](https://darkwhite666.blogspot.com/)

Iscriviti a:
[Commenti sul post (Atom)](https://darkwhite666.blogspot.com/feeds/6726236293733802020/comments/default)

## Segui la nostra pagina Facebook:

* [Dark Space Blogspot (Facebook)](https://www.facebook.com/DarkSpaceBlogspot/)

## Politica Privacy Sito

* [Politica Privacy (Cookies)](http://darkwhite666.blogspot.it/2015/06/politica-dei-cookie-di-questo-sito-in.html)

## Indice Completo Articoli Blog (In Aggiornamento)

* [✅Articoli Audio, Video, Youtube e File Hosting](https://darkwhite666.blogspot.com/2020/08/articoli-audio-video-youtube-e-file.html)
* [✅Articoli Bitcoin e Criptovalute](https://darkwhite666.blogspot.com/2019/12/tutti-gli-articoli-su-bitcoin-e.html)
* [✅Articoli Browser, Motori Ricerca, Internet, Servizi Generici](https://darkwhite666.blogspot.com/2020/08/articoli-browser-motori-ricerca.html)
* [✅Articol...