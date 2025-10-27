---
title: Ecosistema Di Gnosis: Chain, Aggregatore Aste Batch, Gnosis Pay
url: http://darkwhite666.blogspot.com/2024/10/ecosistema-di-gnosis-chain-aggregatore.html
source: Dark Space Blogspot
date: 2024-10-04
fetch_date: 2025-10-06T19:04:17.703962
---

# Ecosistema Di Gnosis: Chain, Aggregatore Aste Batch, Gnosis Pay

## Visualizzazioni Totali

[![Dark Space Blogspot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZgt0RUZjHgbkLsu7CbFNAiyAMd0qvDL2fubvcBv5c6R04keICe8K0ig6oXxzqa6519xC3S7eBHP3_F60rvo_NqafkHR83xyZwscmsQgwCw_EPQpiDWkgarGw08kUDwteX-zWL_I_uP1w/s1600/ask-fm.png)](https://darkwhite666.blogspot.com/)

TRA I PRIMI IN ITALIA A PARLARE DI BITCOIN (DAL 2012!): PER ESSERE SEMPRE AGGIORNATI SULLE NOVITA' TECNOLOGICHE DEL WEB SEGUITE LA PAGINA FACEBOOK (LINK A SINISTRA)

## giovedì 3 ottobre 2024

### Ecosistema Di Gnosis: Chain, Aggregatore Aste Batch, Gnosis Pay

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEif16W20NZTh39cCoJs_pzenqWj8epX4heerRZNJJWIrPRowp1AjocTgZz1ihaJtJb_mO-7KbtbX5DPqg9e1_liNB80T6DEKv9z7DaMMj_fHLH9d57PR36o95oxSkhofurzJwlAxmdAo11vMV3q7YwV9HhuC_I6kio36ztDtIek7CQlBQa4D7uO0hoymjA/s320/Gnosis.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEif16W20NZTh39cCoJs_pzenqWj8epX4heerRZNJJWIrPRowp1AjocTgZz1ihaJtJb_mO-7KbtbX5DPqg9e1_liNB80T6DEKv9z7DaMMj_fHLH9d57PR36o95oxSkhofurzJwlAxmdAo11vMV3q7YwV9HhuC_I6kio36ztDtIek7CQlBQa4D7uO0hoymjA/s471/Gnosis.png)

**[Gnosis Chain](https://www.gnosischain.com/)** è una sidechain di Ethereum che funziona come un layer1. Sostanzialmente è simile a Polygon: ha un collegamento diretto con la mainnet di Ethereum ma ha un suo token, un gas token (xDai peggato a Dai), suoi validatori e un sistema di staking con il token $Gno. Venne lanciata nel 2015 come mercato di previsioni tramite una piattaforma di DeFi (simile a PolyMarket). Il mercato previsionale era basato sulla formula poi utilizzata da Uniswap e dagli AMM classici: x\*y=k. Successivamente sono stati sviluppati diversi servizi terzi e dapps.

COWSWAP

[**Cow Swap**](https://swap.cow.fi/#/1/swap/WETH) è un aggregatore dex (di aste batch) dove gli ordini di acquisto/vendita vengono raccolti ed aggregati in un determinato periodo di tempo chiamato time-batch, al termine del quale gli stessi vengono eseguiti simultaneamente ad uno stesso prezzo uniforme nell'ambito della stessa transazione. Dunque, invece di eseguire le operazioni di trading una per una, queste aste batch raccolgono più ordini nell'intervallo di tempo definito e li eseguono in un singolo batch, aggregando la liquidità viene ridotto lo slippage. Il modello consente ai traders di negoziare più asset in un'unica asta. Avere più ordini in un singolo batch consente anche scambi P2P, che garantiscono prezzi migliori. Questo tipo di aste in batch incoraggiano i risolutori a trovare il miglior percorso di esecuzione per ogni negoziazione, ottimizzando così l'efficienza dell'esecuzione piuttosto. Un altro protocollo che utilizza questo modello è **[Balancer per i suoi Liquidity Bootstrapping Pools](https://darkwhite666.blogspot.com/2021/12/cose-il-liquidity-bootstrapping-pool.html)** usati per raccolta di liquidità e per stabilire un prezzo dinamico che appunto varia nel tempo. Il meccanismo di asta batch riduce la possibilità di MEV, un fenomeno in cui gli esecutori possono trarre vantaggio dalle transazioni degli utenti re-ordinando o includendo transazioni proprie. Rispetto agli aggregatori Dex "classici", le aste batch raccolgono ordini e li eseguono contemporaneamente a un prezzo unico, mentre gli aggregatori come 1inch, Odos e Paraswap dividono e distribuiscono gli ordini tra vari Dex per ottenere i migliori prezzi. Ad esempio 1inch utilizza un algoritmo chiamato Pathfinder per dividere gli ordini in più segmenti (cioè trovato il miglior tasso di scambio, gli ordini vengono divisi in piccole parti), eseguendoli su diverse piattaforme per minimizzare il costo e lo slippage. Odos e Paraswap sono basati sull'ottimizzazione del routing, trovando percorsi più efficienti per la trade richiesta. Altri aggregatori di liquidità sono Kyber Network e Matcha.

GNOSIS SAFE/SAFE GLOBAL

Account multi-sig [**Safe Global**](https://safe.global/) che richiede più firme per confermare le transazioni, aumentando la sicurezza rispetto ai wallet tradizionali. Per maggiori info: [**Come Creare Uno Smart Contract Multi Firma (Gnosis Safe Proxy)**](https://darkwhite666.blogspot.com/2023/07/come-creare-uno-smart-contract-multi.html)

CONDITIONAL TOKENS

[**Conditional Tokens**](https://docs.gnosis.io/conditionaltokens/) sono strumenti per la creazione di mercati di previsione e finanziari complessi. Questi token rappresentano scommesse o previsioni su eventi futuri e possono essere utilizzati per vari scopi, tra cui scommesse, assicurazioni e strumenti finanziari derivati

ZODIAC/GUILD

Si tratta di un framework modulare per le DAO, esso è basato sul concetto di "astro" (moduli) che possono essere combinati per costruire sistemi di governance personalizzati.

La modularità permette alle organizzazioni di creare sistemi di governance flessibili e adattabili utilizzando moduli predefiniti. Esso funziona anche con vari framework di governance esistenti, inclusi Gnosis Safe e altri sistemi di gestione delle risorse. Per maggiori info: [**Gnosis Guild**](https://www.gnosisguild.org/)

GNOSIS PAY

**[Gnosis Pay](https://gnosispay.com/)** è un sistema di pagamento basato su blockchain che mira a facilitare i pagamenti tramite criptovaluta nella vita quotidiana. Supporta transazioni sicure collegando semplicemente Metamask ad un'app utilizzando sistemi di pagamento VISA (carta di debito che utilizza safe smart contract). Il vantaggio è holdare asset su wallet non custodial ed eseguire pagamenti trasferendo solo la somma necessaria sulla carta, il tutto senza utilizzare enti centralizzati. Utilizzando il circuito VISA è comunque richiesto il KYC. Gnosis può essere integrato con Monerium che facilita trasferimenti da fiat a mondo blockchain, mediante Iban. Inoltre supporta anche asset peggati a fiat tipo EURe. Se depositi collaterale in cripto su Aave e prendi in prestito EURe, non solo non spendi le tue cripto che holdi long term ma non generi neanche eventi tassabili. Gnosis Pay può essere anche integrato con Zeal Wallet che è focalizzato sulla privacy e la sicurezza delle transazioni, inoltre permette di gestire la carta mediante smartphone.

ALTRE DAPPS

GnosisDAO ha approvato uno spin-off di un protocollo di gestione della tesoreria DAO **[Karpatkey](https://www.karpatkey.com/)** con token nativo $Kpk. Gnosis ha anche investito 1,5 milioni di dollari in **[Hoprnet](https://hoprnet.org/)** per creare una VPN privata e decentralizzata. Inoltre ha lanciato **Gnosis AI** per i mercati di previsione. La chain ha un TVL di circa 280 milioni di dollari e tra le dapps principali troviamo **[RealT](https://realt.co/)**, basata su RWA per investire nel settore immobiliare comprando asset reali frazionati.

Pubblicato da
[DarkDave.|.666](https://www.blogger.com/profile/02696807736631988356 "author profile")

alle
[11:05](https://darkwhite666.blogspot.com/2024/10/ecosistema-di-gnosis-chain-aggregatore.html "permanent link")

[![](//img1.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/1856644955194422917/4154333348713504857 "Post per email")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=1856644955194422917&postID=4154333348713504857&from=pencil "Modifica post")

[Invia tramite email](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=4154333348713504857&target=email "Invia tramite email")[Postalo sul blog](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=4154333348713504857&target=blog "Postalo sul blog")[Condividi su X](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=4154333348713504857&target=twitter "Condividi su X")[Condividi su Facebook](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=4154333348713504857&target=facebook "Condividi su Facebook")[Condividi su Pinterest](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=4154333348713504857&target=pinterest "Condividi su Pinterest")

Etichette:
[AMM](https://d...