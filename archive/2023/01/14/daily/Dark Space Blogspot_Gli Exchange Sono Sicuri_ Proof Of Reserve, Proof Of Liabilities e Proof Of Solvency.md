---
title: Gli Exchange Sono Sicuri? Proof Of Reserve, Proof Of Liabilities e Proof Of Solvency
url: http://darkwhite666.blogspot.com/2023/01/gli-exchange-sono-sicuri-proof-of.html
source: Dark Space Blogspot
date: 2023-01-14
fetch_date: 2025-10-04T03:55:42.619129
---

# Gli Exchange Sono Sicuri? Proof Of Reserve, Proof Of Liabilities e Proof Of Solvency

## Visualizzazioni Totali

[![Dark Space Blogspot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZgt0RUZjHgbkLsu7CbFNAiyAMd0qvDL2fubvcBv5c6R04keICe8K0ig6oXxzqa6519xC3S7eBHP3_F60rvo_NqafkHR83xyZwscmsQgwCw_EPQpiDWkgarGw08kUDwteX-zWL_I_uP1w/s1600/ask-fm.png)](https://darkwhite666.blogspot.com/)

TRA I PRIMI IN ITALIA A PARLARE DI BITCOIN (DAL 2012!): PER ESSERE SEMPRE AGGIORNATI SULLE NOVITA' TECNOLOGICHE DEL WEB SEGUITE LA PAGINA FACEBOOK (LINK A SINISTRA)

## venerdì 13 gennaio 2023

### Gli Exchange Sono Sicuri? Proof Of Reserve, Proof Of Liabilities e Proof Of Solvency

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyQhG2LmRMxR-3h79kSDFGDfWqOFbWXk48qbY-M-VcrnnPAhvXNVfDbU6XGMMr47IrZeSOz0HoSSPNeT-y9WeeolwtUPmJOOPvcq9PJA7p9Q4veDSVXvVItZaxQnH0xqAHKz6tWwyEKaEvbr9oNf-5vaAF6GvmrSJs6fAERAyFcexIMz_z8tU76kTu/w400-h223/download.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyQhG2LmRMxR-3h79kSDFGDfWqOFbWXk48qbY-M-VcrnnPAhvXNVfDbU6XGMMr47IrZeSOz0HoSSPNeT-y9WeeolwtUPmJOOPvcq9PJA7p9Q4veDSVXvVItZaxQnH0xqAHKz6tWwyEKaEvbr9oNf-5vaAF6GvmrSJs6fAERAyFcexIMz_z8tU76kTu/s366/download.jpg)

La **Proof Of Reserves** è un rapporto inerente la liquidità a disposizione di un exchange centralizzato (dex in DeFi non ne hanno bisogno perchè sono non custodial, anche se le piattaforma sono auditate dal punto di vista degli smart contract). Questo quantitativo, revisionato da terze parti, dovrebbe coprire una quantità uguale (o superiore) ai fondi depositati dai clienti sull'exchange (Proof Of Reserve e cold wallet). Ogni asset dovrebbe essere coperto 1:1, questo per garantire il 100% del prelievo dei fondi degli utenti che stanno usando il suddetto servizio. Questa riserva dovrebbe prevenire una crisi di liquidità in uno scenario di "bank run", qualora tutti gli utenti volessero prelevare. La Proof Of Reserve, affinchè possa avere una certa valenza, dovrebbe essere un audit di terze parti che mostra i fondi dei clienti. Non si tratta di un audit in senso stretto ma il senso è quello. Gli exchange possono, a loro volta, pubblicare periodicamente i risultati degli audit e consentire ai clienti di tracciare in tempo reale le proprie riserve. Un auditor crea uno snapshot (albero Merkle) in un certo momento di tutti i fondi della società in questione, mostrando così una prova del fatto che la piattaforma analizzata abbia tutte le risorse necessarie per coprire il 100% dei prelievi in qualsiasi momento. L'albero Merkle aggrega il totale dei fondi dei clienti depositati sull'exchange, senza esporre dati privati.

Questo consente ai clienti di avere la certezza che la società a cui si stanno affidando i propri asset non abbia buchi di liquidità, dall’altro rende possibile prelevare i propri fondi in qualsiasi momento senza avere problemi eccessivi di privacy.

Questo auditor Merkle, a sua volta, consiste in un’impronta digitale a prova di manomissione, a cui gli auditor possono accedere per verificare le informazioni sui fondi. Il fatto che questi controlli possano essere fatti in tempo reale consente ai clienti di avere anche una garanzia di monitoraggio. Un eventuale limite è rappresentato dall’impossibilità di garantire una contabilità variabile nel tempo. Ovvero è possibile verificare gli asset on-chain del depositario, ma non la provenienza degli stessi, i quali potrebbero anche essere stati presi in prestito proprio per eseguire la Proof Of Reserve (e poi essere ridati indietro al reale proprietario. Chiaramente ogni operazione on chain è pubblica quindi grossi movimento verrebbero comunque notati). Sotto questa ottica sembrano un po' ridicole le (poche) Proof Of Reserve che andavano di moda sino a qualche mese fa, visto che venivano eseguite ogni 4-5 mesi.

Un altro limite può essere rappresentato dalla natura di queste riserve, ovvero se sono riserve reali, derivanti dalla vendita di altro, se sono cripto volatili (BTC, ETH, etc) o se sono stablecoin. Alto limite è se sono riserve liquide (subito disponibili) o illiquide (staking, vesting, etc). Le illiquide non dovrebbero contare come bilancio. Ovviamente avere una Proof Of Reserve come si deve e cold wallet pubblici non vuol dire che un exchange non possa andare in bancarotta perchè bisogna sempre vedere come questi fondi vengono gestiti.

Qui puoi trovare i cold wallet monitorati:

[**Exchange Holding (Nansen)**](https://portfolio.nansen.ai/entities)

Qui invece le Proof Of Reserves:

[**Binance (PoR)**](https://www.binance.com/en/proof-of-reserves)

[**Crypto.com (PoR)**](https://crypto.com/eea/proof-of-reserves)

[**Kraken (PoR)**](https://www.kraken.com/proof-of-reserves)

[**OKx (PoR)**](https://www.okx.com/it/account/login?forward=/it/balance/audit)

[**Bybit (PoR)**](https://www.bybit.com/app/user/proof-of-reserve)

[**Bitmex (PoR e PoL)**](https://blog.bitmex.com/bitmex-provides-snapshot-update-to-proof-of-reserves-proof-of-liabilities/)

[**Kucoin (PoR)**](https://www.kucoin.com/it/proof-of-reserves)

La **Proof Of Liabilities** è la prova che non devi più di un certo quantitativo di asset (è la somma delle passività di tutti i clienti). Se ai clienti devi 50.000 BTC e ne hai 55000, sei solvente. Il problema di questa prova è che non viene dimostrato che l'exchange abbia il reale possesso di quei fondi nè il controllo delle chiavi.

La **Proof Of Solvency** è lo step finale che un exchange dovrebbe garantire: ovvero avere fondi maggiori del proprio debito e dimostrarne la proprietà. Insomma ingloba sia la prova di riserva che quella di passività. Ovvero l'importo detenuto in custodia deve essere maggiore delle passività. Essa si attua mediante:

-un albero Merkle per il rapporto sulle passività pronto per essere verificato

-Meccanismi di auditing e verifica in tempo reale delle riserve e delle passività

-Prova di proprietà sulle chiavi dei portafogli in cui sono detenuti i fondi

-Meccanismi per garantire la privacy del cliente e mostrare evidenza di riserve e passività

Pubblicato da
[DarkDave.|.666](https://www.blogger.com/profile/02696807736631988356 "author profile")

alle
[19:00](https://darkwhite666.blogspot.com/2023/01/gli-exchange-sono-sicuri-proof-of.html "permanent link")

[![](//img1.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/1856644955194422917/8308525502497690749 "Post per email")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=1856644955194422917&postID=8308525502497690749&from=pencil "Modifica post")

[Invia tramite email](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=8308525502497690749&target=email "Invia tramite email")[Postalo sul blog](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=8308525502497690749&target=blog "Postalo sul blog")[Condividi su X](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=8308525502497690749&target=twitter "Condividi su X")[Condividi su Facebook](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=8308525502497690749&target=facebook "Condividi su Facebook")[Condividi su Pinterest](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=8308525502497690749&target=pinterest "Condividi su Pinterest")

Etichette:
[Cripto](https://darkwhite666.blogspot.com/search/label/Cripto),
[Exchange](https://darkwhite666.blogspot.com/search/label/Exchange)

#### Nessun commento:

#### Posta un commento

[Post più recente](https://darkwhite666.blogspot.com/2023/01/differenza-tra-etf-futures-ed-etf-spot.html "Post più recente")

[Post più vecchio](https://darkwhite666.blogspot.com/2023/01/prestiti-in-defi-cose-il-ltv-e-la.html "Post più vecchio")
[Home page](https://darkwhite666.blogspot.com/)

Iscriviti a:
[Commenti sul post (Atom)](https://darkwhite666.blogspot.com/feeds/8308525502497690749/comments/default)

## Segui la nostra pagina Facebook:

* [Dark Space Blogspot (Facebook)](https://www.facebook.com/DarkSpaceBlogspot/)

## Politica Privacy Sito
...