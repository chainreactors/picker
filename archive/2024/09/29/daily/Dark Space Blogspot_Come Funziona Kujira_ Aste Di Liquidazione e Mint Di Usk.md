---
title: Come Funziona Kujira: Aste Di Liquidazione e Mint Di Usk
url: http://darkwhite666.blogspot.com/2024/09/come-funziona-kujira-aste-di.html
source: Dark Space Blogspot
date: 2024-09-29
fetch_date: 2025-10-06T18:27:58.944126
---

# Come Funziona Kujira: Aste Di Liquidazione e Mint Di Usk

## Visualizzazioni Totali

[![Dark Space Blogspot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZgt0RUZjHgbkLsu7CbFNAiyAMd0qvDL2fubvcBv5c6R04keICe8K0ig6oXxzqa6519xC3S7eBHP3_F60rvo_NqafkHR83xyZwscmsQgwCw_EPQpiDWkgarGw08kUDwteX-zWL_I_uP1w/s1600/ask-fm.png)](https://darkwhite666.blogspot.com/)

TRA I PRIMI IN ITALIA A PARLARE DI BITCOIN (DAL 2012!): PER ESSERE SEMPRE AGGIORNATI SULLE NOVITA' TECNOLOGICHE DEL WEB SEGUITE LA PAGINA FACEBOOK (LINK A SINISTRA)

## sabato 28 settembre 2024

### Come Funziona Kujira: Aste Di Liquidazione e Mint Di Usk

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjacX-y4LCyhi7S1stiNCwrV6MKx5D4CWmL9TXwJTPEmpAtBj4sTIXVTkZ7FnJaacaQ15U593bwjb5frr1OErf4Mv7gGLRsy5QOzUqgMxJONi-zqxpuppBPrwl-8I6Qnf0cwfKPdH6GmW3hHxabVT48dfAgJJn9-xLfaeySKHIHCLGTA216vIOwv34u1co/w400-h133/Kujira.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjacX-y4LCyhi7S1stiNCwrV6MKx5D4CWmL9TXwJTPEmpAtBj4sTIXVTkZ7FnJaacaQ15U593bwjb5frr1OErf4Mv7gGLRsy5QOzUqgMxJONi-zqxpuppBPrwl-8I6Qnf0cwfKPdH6GmW3hHxabVT48dfAgJJn9-xLfaeySKHIHCLGTA216vIOwv34u1co/s1152/Kujira.png)

In un vecchio articolo avevo già parlato di **[Kujira](https://kujira.network/)**, quando faceva parte dell'ecosistema di Terra. Dopo **[il fallimento di Terra](https://darkwhite666.blogspot.com/2022/05/cose-successo-luna-ed-ust-e-finita-bank.html)**, Kujira si è costruita una propria chain su Cosmos. Kujira 1.0 **[permetteva di depositare collaterale (principalmente Luna)](https://darkwhite666.blogspot.com/2022/02/come-diventare-un-liquidatore-su-kujira.html)** e di prendere in prestito Ust. Scegliendo determinate fasce di prezzo era possibile comprare collaterale a sconto (Luna) partecipando al processo di liquidazione. In questo articolo vediamo il funzionamento di Kujira 2.0.

KUJIRA SU COSMOS

Tieni presente che il buon funzionamento di una piattaforma non vuol dire andare "all in" sul token Kuji. E' vero, se una piattaforma genera fee e guadagni, molto probabilmente il suo token andrà bene ma non è detto. In ogni caso, qui ci soffermiamo sul funzionamento della piattaforma quindi non sono consigli finanziari sull'investimento di Kuji. Questo protocollo opera principalmente nell'ecosistema di Cosmos, con l'obiettivo di migliorare l'efficienza del mercato delle liquidazioni. Sostanzialmente ho diverse opportunità di utilizzo della piattaforma:

1) Minting della stable Usk, depositando collaterale

2) Lending/borrowing

3) Diventare liquidatore, acquistando collaterale a sconto

MINT DI USK

Il processo di mint di Usk (United States Kujira) è un meccanismo attraverso il quale gli utenti possono creare (mint) nuovi Usk, che è una stablecoin peggata al dollaro USA.

Per creare nuovi Usk, gli utenti devono fornire garanzie (collateral). Solitamente, queste garanzie sono in forma di altre criptovalute supportate dalla piattaforma Kujira, come Atom o altri asset digitali. In base al valore di mercato delle garanzie fornite, gli utenti possono creare una quantità proporzionale di Usk. La quantità massima di Usk che si può creare dipende dal rapporto di collateralizzazione richiesto dal protocollo che può variare in base alle condizioni di mercato (ad esempio, 150% significa che per ogni 15000 dollari in garanzie, si possono creare fino a 10000 USK).

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiz15qP8jVg7n4Q791SdtIQB_7SQlNpCpLd-cRKzCtuIDpFrrktEJAIhFGRopfKgU5vuM0ZVBA89uOP9sA-sCpBW8oA5qXobZYTwfp4Knj7x7bzF88depws3jj34Eoc-0dW5B94MQIH0_iVUF2-BSjcRkl-SpjEFMOdMuMSLsVVk0YFU4dNjJPS7yirSKc/w400-h278/USK%20Mint.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiz15qP8jVg7n4Q791SdtIQB_7SQlNpCpLd-cRKzCtuIDpFrrktEJAIhFGRopfKgU5vuM0ZVBA89uOP9sA-sCpBW8oA5qXobZYTwfp4Knj7x7bzF88depws3jj34Eoc-0dW5B94MQIH0_iVUF2-BSjcRkl-SpjEFMOdMuMSLsVVk0YFU4dNjJPS7yirSKc/s886/USK%20Mint.png)

Il protocollo monitora costantemente il valore delle garanzie fornite rispetto alla quantità di Usk creati. Se il valore delle garanzie scende sotto una certa soglia di sicurezza, gli utenti sono soggetti a liquidazione (le garanzie vengono vendute per mantenere la stabilità del sistema). La vendita delle garanzie serve per coprire il debito in Usk, garantendo che la stablecoin rimanga completamente collateralizzata. Gli utenti possono anche "burnare" i loro Usk, restituendoli al protocollo per ricevere indietro le loro garanzie. Questo processo permette agli utenti di ritirare le loro criptovalute collateralizzate riducendo l'offerta di Usk in circolazione.

Sotto certi versi, Kujira **[funziona come Synthetix Network](https://darkwhite666.blogspot.com/2022/08/come-funziona-synthetix-network-snx.html)** per quanto riguarda il mint di stablecoin. Le sostanziali differenze sono che Kujira utilizza più collaterali (e non solo Snx), ha un meccanismo di aste per liquidazioni (che poi vedremo sotto) e non ha l'offerta di asset sintetici. Il funzionamento di Luna/Ust era completamente diverso, anche se può sembrare ci siano somiglianze.

LENDING/BORROWING ED ASTE DI LIQUIDAZIONE

Il protocollo permette anche di depositare asset per ricevere una rendita e di prendere in prestito altri asset.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh8cTTTcUz1190s3A0_k5fwOaZJEdJmkDgEELE7ex6BhRP5QLOTla1SLm78ZlpZl8ZhoxjaMe9BtzX052rTsax7TkAaXUw4Fs1AXN_mcfQzCoG-lKVy73LMb6IGzQzYIh9jzesKTMqudMYCD1Mu53WXO4wdKistbxHnx1WHM0um0wirwHB-m1LkGbSUVfc/w640-h242/Borrow.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh8cTTTcUz1190s3A0_k5fwOaZJEdJmkDgEELE7ex6BhRP5QLOTla1SLm78ZlpZl8ZhoxjaMe9BtzX052rTsax7TkAaXUw4Fs1AXN_mcfQzCoG-lKVy73LMb6IGzQzYIh9jzesKTMqudMYCD1Mu53WXO4wdKistbxHnx1WHM0um0wirwHB-m1LkGbSUVfc/s1632/Borrow.png)

Kujira inoltre si concentra sulle liquidazioni delle posizioni di prestito aperte sulle piattaforme DeFi. Quando un utente prende in prestito criptovalute depositando un collaterale, la sua posizione può essere liquidata se il collaterale si avvicina al prezzo della somma presa in prestito. Perchè? Le liquidazioni avvengono per proteggere i fondi dei lenders, altrimenti un borrower potrebbe non essere incentivato a restituire il prestito, lasciando la piattaforma con bad debit.

Kujira permette agli utenti di partecipare a queste liquidazioni mediante un sistema di oracoli che gestisce liquidazioni e feed sui prezzi. Il protocollo utilizza un sistema di aste per le liquidazioni. Quando un prestito viene liquidato, viene messo all'asta il deposito del borrower e gli utenti possono fare offerte per acquistare il suo collaterale a prezzi scontati (rispetto a quelli spot). Questo sistema di aste a ribasso può aiutare a ottenere prezzi più equi riducendo l'impatto delle liquidazioni sul mercato.

Gli utenti quindi partecipano all'asta facendo offerte per acquistare il collaterale ad un prezzo inferiore rispetto al prezzo di mercato attuale (è possibile depositare il collaterale scegliendo tra i vari sconti. Quello più elevato, permette di acquistare l'asset ad un prezzo inferiore ma c'è una competizione maggiore). L'asta si conclude quando viene raggiunto il cosiddetto "prezzo equo" (a causa del raggiungimento del prezzo minimo o della scadenza dell'asta). L'utente che si aggiudica l'asta compra il collaterale a sconto, il borrower si vede liquidato il collaterale (ottiene una perdita minore, cioè viene ridotto l'impatto negativo rispetto a una liquidazione tradizionale).

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgeaQjrZKzXRhpNl8UkJ2Bj4XQE2GsRkRhnT17ktNK3YLv_hDfKfeJ-ohW10Q1RAKGbKLKKHlxIpzQuOtXNxa-gcdjn7zupU9jiy1SOtAHRCJ46LDckroPW4wRTsU4ztBN9tttjAW3aJf05pvmdRE5qgLN8H743NybuU0ggNiPiec3D-5t9XI3e2_ypAyc/w396-h400/Liquidations%20Kujira.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgeaQjrZKzXRhpNl8UkJ2Bj4XQE2GsRkRhnT17ktNK3YLv_hDfKfeJ-ohW10Q1RAKGbKLKKHlxIpzQuOtXNxa-gcdjn7zupU9jiy1SOtAHRCJ46LDckroPW4wRTsU4ztBN9tttjAW3aJf05pvmdRE5qgLN8H743NybuU0ggNiPiec3D-5t9XI3e2_ypAyc/s745/Liquidations%20Kujira.png)

I fondi ottenuti dall'asta ve...