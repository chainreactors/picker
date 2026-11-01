---
title: Tipi Di Attacchi Front Running In DeFi
url: http://darkwhite666.blogspot.com/2026/10/tipi-di-attacchi-front-running-in-defi.html
source: Dark Space Blogspot
date: 2026-10-31
fetch_date: 2026-11-01T08:21:32.112150
---

# Tipi Di Attacchi Front Running In DeFi

## Visualizzazioni Totali

[![Dark Space Blogspot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZgt0RUZjHgbkLsu7CbFNAiyAMd0qvDL2fubvcBv5c6R04keICe8K0ig6oXxzqa6519xC3S7eBHP3_F60rvo_NqafkHR83xyZwscmsQgwCw_EPQpiDWkgarGw08kUDwteX-zWL_I_uP1w/s1600/ask-fm.png)](https://darkwhite666.blogspot.com/)

TRA I PRIMI IN ITALIA A PARLARE DI BITCOIN (DAL 2012!): PER ESSERE SEMPRE AGGIORNATI SULLE NOVITA' TECNOLOGICHE DEL WEB SEGUITE LA PAGINA FACEBOOK (LINK A SINISTRA)

## sabato 31 ottobre 2026

### Tipi Di Attacchi Front Running In DeFi

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhYnPcubC3_dFTnn9bIYa4_YrI9_-K-ydLK5Xomjf4PNUlQ4Xq5w86ZxCKi5mIvykE0i04EEGRYC8EA4db0FEV9Oo3BpbM9a_JO6j5fY753fFvkgZ2HYa9mQvXe5GXprsr9-33eehNWhpIot-qirSawnQ3IrXDkhGwcz5QKM7q9-M4CCseVpImfAvQinxc/w400-h179/Front%20Running%20Bot.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhYnPcubC3_dFTnn9bIYa4_YrI9_-K-ydLK5Xomjf4PNUlQ4Xq5w86ZxCKi5mIvykE0i04EEGRYC8EA4db0FEV9Oo3BpbM9a_JO6j5fY753fFvkgZ2HYa9mQvXe5GXprsr9-33eehNWhpIot-qirSawnQ3IrXDkhGwcz5QKM7q9-M4CCseVpImfAvQinxc/s614/Front%20Running%20Bot.png)

Gli attacchi front-running in **DeFi** sfruttano la natura pubblica della blockchain dove le transazioni sono visibili, anche prima di essere confermate. Se n'era già parlato qui: [**Come Funzionano I Bot Front-Running Sugli AMM**](https://darkwhite666.blogspot.com/2021/09/come-funzionano-i-bot-front-running.html). In ogni caso questo tipo di attacco si verifica quando un attaccante, vedendo una transazione pendente nella mempool (la coda delle transazioni non ancora incluse in un blocco), inserisce una transazione simile ma più vantaggiosa per sé stesso, facendola processare prima di quella originale (aumentando le gas fee). Gli attacchi di front-running sono particolarmente comuni negli AMM, dove i prezzi degli asset cambiano dinamicamente in base alle transazioni eseguite (soprattutto per quelli poco liquidi). Ad esempio su Ethereum, tutte le transazioni in pending vengono inviate nella mempool prima di essere incluse in un blocco dai validatori. Queste transazioni sono pubbliche e chiunque può visualizzarle, inclusi bot o i "front-runners" che monitorano costantemente questa coda. Se un attaccante vede che un utente sta provando a swappare un token, la transazione va nella mempool, dove attende di essere processata. Un bot di front-running monitora la mempool e vede che questa transazione influenzerà il prezzo di un token. Il front-running può essere utilizzato con strategie diversificate.

FRONT RUNNING SU UN AMM

L’attaccante effettua una transazione su quello stesso AMM (ad esempio Uniswap) che ne altera il prezzo dell'asset prima che l'utente originale possa eseguire la sua operazione. Immagina un utente che vuole comprare 10.000 token di una memecoin su Uniswap per un prezzo di 0,05 ETH per token.

L'attaccante vede questa transazione nella mempool e invia un ordine di acquisto anticipato della stessa memecoin, ma pagando una commissione del gas più alta rispetto alla transazione originale.

Il validatore prioritizza la transazione dell'attaccante perché paga una commissione maggiore.

L'attaccante riesce a comprare la memecoin a 0,05 ETH per token, facendo salire il prezzo (ad esempio a 0,06 ETH per token) a causa dell'acquisto. Ora, quando la transazione originale dell'utente viene processata, deve comprare i token a un prezzo più alto (0,06 ETH per token invece di 0,05 ETH) e ne riceverà meno. Dopo che la transazione dell'utente ha avuto effetto e ha ulteriormente aumentato il prezzo, l'attaccante vende immediatamente i token acquistati al prezzo più alto (ad esempio, a 0,07 ETH per token). In questo modo, l'attaccante ha acquistato i token a un prezzo più basso e li ha rivenduti a un prezzo più alto grazie alla transazione dell'utente originale.

FRONT RUNNING SU PIATTAFORME DI PRESTITI

In questo tipo di attacco, l’attaccante sfrutta transazioni che potrebbero liquidare posizioni di utenti in protocolli DeFi come Aave, MakerDAO e simili. Le liquidazioni sono processi automatici in cui posizioni di prestito vengono chiuse se il collaterale scende sotto una certa soglia, permettendo a chi liquida di ottenere un guadagno (fee di liquidazione e/o collaterale a sconto).

Immagina un utente che ha un prestito aperto su Compound che rischia di essere liquidato. Se il prezzo del collaterale scende sotto una soglia, un altro utente può liquidare la posizione e guadagnare una commissione. L'attaccante vede una transazione nella mempool che cerca di liquidare la posizione.

L'attaccante invia la sua transazione di liquidazione con una commissione del gas più alta, facendola eseguire per prima. Esso otterrà la liquidazione che sarebbe dovuta andare all'utente originale.

In questo caso, l'attaccante ha sfruttato la lentezza dell'inclusione della transazione originale per ottenere il guadagno della liquidazione.

FRONT RUNNING ED ARBITRAGGIO

Per arbitraggio si intende guadagnare su inefficienze di mercato trovando differenze di prezzo tra vari mercati (comprare X e rivendere subito dopo altrove ad un prezzo più elevato). L'attaccante può anticipare un arbitraggista quando nota che sta per essere eseguita una transazione che bilancia i prezzi tra due exchange. L'utente che sta facendo arbitraggio nota che su Uniswap un token viene venduto a 100 USDT mentre su Sushiswap lo stesso token vale 105 USDT. L'arbitraggista invia una transazione per comprare il token a 100 USDT su Uniswap e rivenderlo a 105 USDT su Sushiswap.

L'attaccante vede la transazione in pending nella mempool e invia una transazione con una commissione del gas più alta per eseguire l'arbitraggio prima dell'utente originale. L'attaccante compra il token su Uniswap a 100 USDT e lo rivende su Sushiswap a 105 USDT, realizzando il guadagno dell'arbitraggio. Quando la transazione dell'arbitraggista originale viene processata, il prezzo si è già equilibrato e non c'è più differenza di prezzo.

FRON RUNNING E SANDWICH ATTACK

Si tratta di una variante molto comune del front-running nei dex. In questo tipo di attacco, l'attaccante "incastra" una transazione dell'utente tra due sue transazioni: una prima dell'utente e una successiva. Il nome deriva dal fatto che la transazione dell'utente è "messa nel mezzo".

Un utente invia una transazione per acquistare 100 token su Sushiswap. L'attaccante vede questa transazione nella mempool ed invia una transazione di acquisto dello stesso token, pagando una commissione del gas più alta per farla eseguire prima di quella dell'utente.

L'acquisto dell'attaccante fa aumentare il prezzo del token. Quando la transazione dell'utente viene eseguita, l'utente acquista i token a un prezzo più alto. Subito dopo, l'attaccante esegue una seconda transazione di vendita dello stesso token, vendendo al prezzo più alto (gonfiato dalla transazione dell'utente), realizzando un guadagno fulmineo. In un sandwich attack, l'attaccante compra a un prezzo più basso prima dell'utente e vende a un prezzo più alto dopo l'utente, sfruttando la transazione dell'utente per ottenere un guadagno.

DIFESE

Aumentare le fee ha un effetto relativo perchè un bot, conoscendole, potrebbe aumentarle a sua volta. Anche se con fee più elevate c'è meno tempo per l'attaccante per accorgersi della transazione in pending ed eseguire l'attacco. Un'altra soluzione è nascondere i dettagli delle transazioni fino a quando non vengono eseguite, come i meta-transaction relayers o soluzioni di privacy come zk-Rollups. Un'altra possibilità è il Commit-Reveal scheme:  prima, gli utenti inviano un commitment (che nasconde i dettagli della transazione). Poi, in una fase successiva, si svela il contenuto del commitment (fase di reveal). Questo rende difficile per un attaccante conoscere i dettagli della transazione in tempo per eseguire un front-running. Alcuni protocolli DeFi impongono anche limiti alle commissioni del gas per impedire agli attaccanti di manipolare l'ordine delle transazioni. Infine grazie all...