---
title: L'Attacco A Curve Finance: Reentrant Lock e Contromisure Adottate
url: http://darkwhite666.blogspot.com/2023/08/lattacco-curve-finance-reentrant-lock-e.html
source: Dark Space Blogspot
date: 2023-08-07
fetch_date: 2025-10-04T12:00:33.026976
---

# L'Attacco A Curve Finance: Reentrant Lock e Contromisure Adottate

## Visualizzazioni Totali

[![Dark Space Blogspot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZgt0RUZjHgbkLsu7CbFNAiyAMd0qvDL2fubvcBv5c6R04keICe8K0ig6oXxzqa6519xC3S7eBHP3_F60rvo_NqafkHR83xyZwscmsQgwCw_EPQpiDWkgarGw08kUDwteX-zWL_I_uP1w/s1600/ask-fm.png)](https://darkwhite666.blogspot.com/)

TRA I PRIMI IN ITALIA A PARLARE DI BITCOIN (DAL 2012!): PER ESSERE SEMPRE AGGIORNATI SULLE NOVITA' TECNOLOGICHE DEL WEB SEGUITE LA PAGINA FACEBOOK (LINK A SINISTRA)

## domenica 6 agosto 2023

### L'Attacco A Curve Finance: Reentrant Lock e Contromisure Adottate

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlLeYb_lYlYY6AKL5RClk8WA_vhoVG1j4eJNihan_7RHHhRG94vXWGdhJXTIKptMyvovSPmpb2kUA_KtJaYoG_2SOQE1jKyhDH51skm_RKu4I1UKKv-s_BB9FwVxr4hABHJQgo_rHILMnxWIj9tHTwvoAN2bfBO2SbL-H08j1VRVFveLUQy4pF-HSPsd4/w400-h233/Curve%20Hack.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlLeYb_lYlYY6AKL5RClk8WA_vhoVG1j4eJNihan_7RHHhRG94vXWGdhJXTIKptMyvovSPmpb2kUA_KtJaYoG_2SOQE1jKyhDH51skm_RKu4I1UKKv-s_BB9FwVxr4hABHJQgo_rHILMnxWIj9tHTwvoAN2bfBO2SbL-H08j1VRVFveLUQy4pF-HSPsd4/s723/Curve%20Hack.png)

[**Curve Finance**](https://curve.fi/#/ethereum/swap) ha avuto diversi problemi negli ultimi giorni. Il peggio sembra essere passato perchè l'hacker ha iniziato a restituire i fondi rubati (a causa di una taglia) però vediamo quello che è successo, anche per comprendere meglio i rischi della DeFi.

Il 30 Luglio 2023, un hacker ha sfruttato la vulnerabilità di alcuni pool di Curve, programmati nel linguaggio di programmazione Vyper tramite un meccanismo di reentrancy lock. Sostanzialmente un reentrant lock è un meccanismo di esclusione reciproca che consente ai thread di rientrare in un blocco di una risorsa (più volte) senza una situazione di deadlock.

Attraverso questa debolezza, l’hacker ha potuto drenare una parte dei 69M$ da diversi pool di Curve:

CRV/ETH (circa 30M)

alETH/ETH (20.5M$)

pETH/ETH (11.5M$)

msETH/ETH (1.6M$ tramite un frontrun attack attraverso un MEV Bot di un secondo attaccante ma poi i soldi sono stati restituiti)

Per maggiori info: [**Vyper Nonreentrancy Lock Vulnerability Technical Post-Mortem Report**](https://hackmd.io/%40vyperlang/HJUgNMhs2)

Oltre a far perdere il peg a numerose versioni liquide di ETH, ciò ha anche ridotto di molto la liquidità del primo pool in assoluto del token CRV (CRV/ETH). Ovviamente, questo drenaggio di liquidità, oltre a creare problemi ai liquidity provider e alle DAO che hanno fornito asset a questi pool, ha anche ridotto di molto la liquidabilità dell’asset Curve. L'exploit ha coinvolto progetti come l'exchange decentralizzato Ellipsis, le piattaforme di lending Alchemix e JPEG'd e il synthetic protocol Metronome, che hanno visto sottrarsi milioni di dollari di asset dai liquidity pool. Oltre a Curve, naturalmente. Il codice che ha parzialmente risolto la vulnerabilità è il seguente:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2zDSkotz5xRO9UsRZpGBzEzU_Kh70xjdRZs13kTmcsfr10BEipPnn4R-fsOTI3cjUFyq4Vtt4nQfWFh-ADert54HsT-XA8xjxJfBx8V17fd8AfZI1bVCpU3cG-pPH1DRrJO5ndz0FbWtOR8zaINFV4bL9eT_ihf6iA3HqKpHmF1st--Wayh8XKH_Iiu4/w640-h566/Codice.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2zDSkotz5xRO9UsRZpGBzEzU_Kh70xjdRZs13kTmcsfr10BEipPnn4R-fsOTI3cjUFyq4Vtt4nQfWFh-ADert54HsT-XA8xjxJfBx8V17fd8AfZI1bVCpU3cG-pPH1DRrJO5ndz0FbWtOR8zaINFV4bL9eT_ihf6iA3HqKpHmF1st--Wayh8XKH_Iiu4/s729/Codice.png)

Il codice ora assegnerà correttamente un singolo storage\_slotla la prima volta che identifica una chiave di rientro duplicata. Tuttavia, non richiamerà la set\_reentrancy\_key\_positionfunzione su ciascuna type\_con lo stesso offset, il che significa che qualsiasi @nonreentrant(<key>) oltre la prima avrebbe un offset di archiviazione "non definito" da utilizzare.

SCARSA LIQUIDITA' ON CHAIN

La scarsa liquidità on chain per grossi acquisti comporta il non poter vendere/comprare l'asset ed altissimo slippage ("price impact is too high").

Ipotizziamo che il pool CRV/ETH aveva al suo interno 30M$ (15M CRV e 15M ETH). In condizioni normali se tu vuoi acquistare 5M di CRV puoi farlo. Dopo lo scambio, il pool ospiterebbe 10M$ di CRV e 20M$ di ETH.

Se un pool viene drenato invece, la scarsa liquidità rende difficoltosi/impossibili gli scambi.

A questo punto, chi volesse scambiare questi due asset fra di loro dovrebbe utilizzare delle size più piccole, oppure optare per un altro pool. Il secondo pool più grande in termini di TVL è quello creato su Uniswap, ossia CRV/ETH 0.3% (2.2M$). Questa assenza di liquidità nei principali pool che consentono lo scambio di CRV crea un grosso problema per il token CRV. Esso è diventato un asset molto illiquido on-chain e che quindi non può essere acquistato o venduto in grosse quantità.

Dopo l’exploit e il drenaggio di liquidità da parte dell’hacker, molte persone hanno avuto paura che questo potesse accadere anche in altri pool di Curve, andando così a prelevare gran parte della liquidità sul protocollo. Il TVL complessivo ha perso il 50% della liquidità complessiva. Tutto ciò si è poi propagato in maniera simile anche sui vari booster di Curve, ossia Convex, Yearn Finance, StakeDAO.

CROLLO DI CRV

Tutta questa sfiducia ha portato di conseguenza i token dei vari protocolli, soprattutto $CRV, ad avere massive vendite a mercato. Questo ha fatto crollare il prezzo da un valore iniziale di 0,70$ a meno di 0,50$, una contrazione di circa il 35%.

Un altro problema da considerare è che la gran parte degli AMM hanno un programma di liquidity mining per chiunque decida di fornire liquidità alla piattaforma.

Curve decide ogni due settimane di emettere 100.000 CRV a mercato e di destinarli verso diversi pool della propria piattaforma. Ovviamente, chi riceve più token avrà maggiori incentivi e così aumenterà la possibilità di attrarre più TVL nei pool, che porterà inevitabilmente a maggiori trade a causa di una ridotta presenza di slippage.

Questo è ciò che da il via al meccanismo del bribing, mediante veCRV che permette di decidere a quale pool destinare maggiore quantità di token per le prossime due settimane. Questo ti fa capire come il prezzo di CRV sia molto importante perchè fornendo le solite reward in termini quantitativi, i  liquidity provider verranno pagati molto meno (perchè CRV vale meno).

PRESTITO DI MICHAEL EGOROV (CURVE CEO)

A complicare tutta questa vicenda c’è l'enorme debito del CEO di Curve, Michael Egorov, che possiede una grandissima quantità di CRV. Non potendoli dumpare a mercato, egli ha deciso qualche anno fa di collateralizzarli sui principali protocolli di lending:

AAVE (55M$ di debito)

Fraxlend(10M$ di debito)

Abracadabra(12M$ di debito)

Inverse Finance (7M$ di debito)

Totale: circa 85M$ di debito in stablecoin. Se il prezzo di CRV dovesse raggiungere un livello che va da 0,4$ a 0,37$, porterebbe gran parte delle sue posizioni a essere vendute a mercato, innescando la sua liquidazione. In generale il collaterale CRV sarebbe venduto a mercato per ripagare il debito mantenendo la piattaforma solvente.

Le varie piattaforme di lending ne beneficerebbero guadagnando una parte della sua perdita.

Tuttavia la liquidità del pool maggiormente utilizzato da questi protocolli per liquidare, e quindi convertire CRV in ETH o in asset stabili, è stato drenato. Ciò rende CRV un token illiquido; di conseguenza, se ci fosse un grosso dump del token, queste piattaforme non avrebbero una controparte per ripagare il debito trovandosi a dover creare del bad debt.

Il fatto che Aave o altre piattaforme di lending possano dare la possibilità ai propri utenti di collateralizzare delle grosse posizioni tramite asset che possono diventare illiquidi è un problema. Ciò potrebbe portare il debito a non essere ripagato, obbligando la piattaforma stessa a utilizzare parte della propria treasury/fondo d’emergenza.

In assenza di questo fondo, invece, la piattaforma dovrà farsi carico di questo bad debt e quindi gli utenti perderebbero par...