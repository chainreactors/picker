---
title: Come Funzionano I Token BRC20: Comprare e Vendere (Bitcoin)
url: http://darkwhite666.blogspot.com/2023/05/come-funzionano-i-token-brc20-comprare.html
source: Dark Space Blogspot
date: 2023-05-14
fetch_date: 2025-10-04T11:39:59.173594
---

# Come Funzionano I Token BRC20: Comprare e Vendere (Bitcoin)

## Visualizzazioni Totali

[![Dark Space Blogspot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZgt0RUZjHgbkLsu7CbFNAiyAMd0qvDL2fubvcBv5c6R04keICe8K0ig6oXxzqa6519xC3S7eBHP3_F60rvo_NqafkHR83xyZwscmsQgwCw_EPQpiDWkgarGw08kUDwteX-zWL_I_uP1w/s1600/ask-fm.png)](https://darkwhite666.blogspot.com/)

TRA I PRIMI IN ITALIA A PARLARE DI BITCOIN (DAL 2012!): PER ESSERE SEMPRE AGGIORNATI SULLE NOVITA' TECNOLOGICHE DEL WEB SEGUITE LA PAGINA FACEBOOK (LINK A SINISTRA)

## sabato 13 maggio 2023

### Come Funzionano I Token BRC20: Comprare e Vendere (Bitcoin)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjg3bzPpJKCKHuWyJaeBQYopmI6R8Sf_L7tsI0poI1dmoijOPAF04XO1kdkbCOub-29x9vJLSKPlpXqbC44ulEqUGDWAlWCEef9rZldYdGAvxzyznOTYoep6YAK34lf5PzCpJ-vHSPbrJ-3lHv1a1nUGazHyPYWQ3TvP9xWWP05B5tYrT88UKAnktH5/w400-h241/btc20-bitcoin-brc-20-1200.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjg3bzPpJKCKHuWyJaeBQYopmI6R8Sf_L7tsI0poI1dmoijOPAF04XO1kdkbCOub-29x9vJLSKPlpXqbC44ulEqUGDWAlWCEef9rZldYdGAvxzyznOTYoep6YAK34lf5PzCpJ-vHSPbrJ-3lHv1a1nUGazHyPYWQ3TvP9xWWP05B5tYrT88UKAnktH5/s953/btc20-bitcoin-brc-20-1200.jpg)

**BRC20** è un protocollo/standard collegato indirettamente a Bitcoin: sono simili a due rette parallele. Se questi token o una transazione BRC20 viene compromessa, il protocollo di Bitcoin non ne risente (a differenza degli ERC20 su Ethereum). ERC20 rispettano il meccanismo di consenso di Ethereum, per i BRC20 non funziona così. Il protocollo di Bitcoin non "sa" quello che sta succedendo sullo standard BRC20, vede il trasferimento come una normale transazione. Paradossalmente la transazione se rispetta gli standard potrebbe essere accettata sulla blockchain di Bitcoin e rifiutata sullo standard BRC20 (perchè magari non rispetta gli standard BRC20). Se qualcuno provasse ad inviare 30 Ordi (token) ma ne possiede solo 10, Bitcoin vedrebbe ciò come un normale trasferimento di Satoshi da un address all'altro. Tuttavia essa verrebbe considerata non valida dallo standard BRC20 (se posseggo 10 token non ne posso inviare 30!).

COME FUNZIONA IL BRC20

Premettendo che si tratta di una normale transazione a cui viene aggiunto del testo, sostanzialmente abbiamo 3 fasi per la creazione di un token BRC20:

1) Deploy (creazione del token BRC20)

2) Mint (generazione del quantitativo dei token)

3) Transfer (permette il trasferimento da un mittente al destinatario)

Il deploy è un'inscription, ovvero l'aggiunta di metadati ad una transazione (campo witness).

Puoi approfondire qui: [**Ordinals ed Inscriptions Su Bitcoin? Come Funzionano e Come Crearli**](https://darkwhite666.blogspot.com/2023/02/ordinals-ed-inscriptions-su-bitcoin.html)

I dati salvati sono nel formato ".JSON" quindi come detto si tratta di testo. Lo "scheletro" dell'inscription per il deploy sarà:

-P (protocol):  BRC20

-OP (operation): deploy

-Tick (ticker/identificativo del token): ordi

-Max (supply): xxxxx

-Lim (limite di mint per ciascuna inscription): xx

-Dec (decimali): 18

Questo testo verrà inserito nell'iscription. Anche nella funzione di mint verrà inserito testo a sua volta visto come una normale transazione dal protocollo Bitcoin (qui è presente la funzione "AMT" ovvero l'amount da mintare). Quando la funzione mint viene confermata dal network, il creatore del token è come se generasse una transazione verso il suo stesso indirizzo (viene autogenerata). Il trasferimento (transfer) prevede la creazione di un'altra inscription sempre con testo dove l'operazione "OP" prevede la funzione transfer e l' "AMT" il quantitativo da inviare. In seguito viene eseguita una normale transazione su rete Bitcoin che trasferisce l'inscription creata dall'address A all'address B. Il protocollo Bitcoin vede banali transazioni non leggendo i dati: non vede il deploy nè il mint. Vede solo un trasferimento di Satoshi da x a y (e non il trasferimento Satoshi+inscription).

Esempio completo:

Deploy: { "p": "brc-20", "op": "deploy", "tick": "darkspace", "max": "210000", "lim": "1000" }

Mint: { "p": "brc-20", "op": "mint", "tick": "darkspace", "amt": "1000" }

Transfer: { "p": "brc-20", "op": "transfer", "tick": "darkspace", "amt": "10" }

MARKET

E' possibile utilizzare questo wallet: **[OrdinalsWallet](https://ordinalswallet.com/)** (che vede anche inscriptions e BRC20). Tramite la funzione "Inscribe" è possibile creare inscription (upload foto) e token BRC20 (scrivere codice e funzione "mint". Tieni presente che il "deploy" di quel token può essere stato fatto già da altre persone). Sempre sullo stesso sito è possibile comprare sia inscription (Bitcoin NFT) che token BRC20 (compaiono delle offerte con quantitativo di token e relativo prezzo).

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi3b3ecIrZmH5XeNn5ickHgXj-pIjKF_2fscsZVj7LjjixcQvqQNDM5tTf-_KNtMXugJs36altnu21ldTGyOCjknkiflduFawRM2u2FB1t_up-FdWVSarX5wuA21Y7UliZZSXZmvOtH2SFFPJKXFNsfrziBE6ZCmElHOEoA_JT1Yoj3Kn8WGzemZ7kp/w640-h312/Ordinals.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi3b3ecIrZmH5XeNn5ickHgXj-pIjKF_2fscsZVj7LjjixcQvqQNDM5tTf-_KNtMXugJs36altnu21ldTGyOCjknkiflduFawRM2u2FB1t_up-FdWVSarX5wuA21Y7UliZZSXZmvOtH2SFFPJKXFNsfrziBE6ZCmElHOEoA_JT1Yoj3Kn8WGzemZ7kp/s1603/Ordinals.png)

Un altro sito interessante è **[Unisat](https://unisat.io/)** che permette di creare inscription, BRC20 ma anche comprarli e venderli. Tuttavia l'accesso al market è possibile solo per coloro che hanno fatto almeno 20 unisat punti (20 Inscriptions).

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiG_SKufm_5Y48JQUybHvBB72QnVjf2s6EZ5-lEE5HCi8cdrjgT_2GFOAfV9pvDDstzWJI3BtYK4IW0ynhyj6nJ1rba4Rix8s7r69aseK3qT8RVk1-pydxE9ed6hznRjffzK1B6RF0hm6zgb3nVK4h9TA9aO3yk0EQyF8z7KU2SI5bdQCwzcfYM-nth/w640-h316/Unisat%202.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiG_SKufm_5Y48JQUybHvBB72QnVjf2s6EZ5-lEE5HCi8cdrjgT_2GFOAfV9pvDDstzWJI3BtYK4IW0ynhyj6nJ1rba4Rix8s7r69aseK3qT8RVk1-pydxE9ed6hznRjffzK1B6RF0hm6zgb3nVK4h9TA9aO3yk0EQyF8z7KU2SI5bdQCwzcfYM-nth/s1612/Unisat%202.png)

Pubblicato da
[DarkDave.|.666](https://www.blogger.com/profile/02696807736631988356 "author profile")

alle
[12:34](https://darkwhite666.blogspot.com/2023/05/come-funzionano-i-token-brc20-comprare.html "permanent link")

[![](//img1.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/1856644955194422917/1976609451661655326 "Post per email")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=1856644955194422917&postID=1976609451661655326&from=pencil "Modifica post")

[Invia tramite email](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=1976609451661655326&target=email "Invia tramite email")[Postalo sul blog](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=1976609451661655326&target=blog "Postalo sul blog")[Condividi su X](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=1976609451661655326&target=twitter "Condividi su X")[Condividi su Facebook](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=1976609451661655326&target=facebook "Condividi su Facebook")[Condividi su Pinterest](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=1976609451661655326&target=pinterest "Condividi su Pinterest")

Etichette:
[Bitcoin](https://darkwhite666.blogspot.com/search/label/Bitcoin),
[NFT](https://darkwhite666.blogspot.com/search/label/NFT)

#### Nessun commento:

#### Posta un commento

[Post più recente](https://darkwhite666.blogspot.com/2023/05/come-scaricare-storie-e-video-da.html "Post più recente")

[Post più vecchio](https://darkwhite666.blogspot.com/2023/05/come-creare-una-cripto-in-pochi-minuti.html "Post più vecchio")
[Home page](https://darkwhite666.blogspot.com/)

Iscriviti a:
[Commenti sul post (Atom)](https://darkwhite666.blogspot.com/feeds/1976609451661655326/comments/default)

## Segui la nostra pagina Facebook:

* [Dark Space Blogspot (Facebook)](h...