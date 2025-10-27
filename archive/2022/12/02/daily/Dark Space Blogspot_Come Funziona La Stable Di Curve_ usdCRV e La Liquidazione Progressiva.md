---
title: Come Funziona La Stable Di Curve? usdCRV e La Liquidazione Progressiva
url: http://darkwhite666.blogspot.com/2022/12/come-funziona-la-stable-di-curve-usdcrv.html
source: Dark Space Blogspot
date: 2022-12-02
fetch_date: 2025-10-04T00:21:36.832213
---

# Come Funziona La Stable Di Curve? usdCRV e La Liquidazione Progressiva

## Visualizzazioni Totali

[![Dark Space Blogspot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZgt0RUZjHgbkLsu7CbFNAiyAMd0qvDL2fubvcBv5c6R04keICe8K0ig6oXxzqa6519xC3S7eBHP3_F60rvo_NqafkHR83xyZwscmsQgwCw_EPQpiDWkgarGw08kUDwteX-zWL_I_uP1w/s1600/ask-fm.png)](https://darkwhite666.blogspot.com/)

TRA I PRIMI IN ITALIA A PARLARE DI BITCOIN (DAL 2012!): PER ESSERE SEMPRE AGGIORNATI SULLE NOVITA' TECNOLOGICHE DEL WEB SEGUITE LA PAGINA FACEBOOK (LINK A SINISTRA)

## giovedì 1 dicembre 2022

### Come Funziona La Stable Di Curve? usdCRV e La Liquidazione Progressiva

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhrUkk6ll65qebg_adC-AgMlEzVLpYVIHYE2GKXuXFifuofMpc0BgKTb4dIckCCjtMa3Q8e0Ucz8whMCgesbDkSlVwAoNwO9BEk82xmUqhJ2uOe6p7CClXTSgSoTg1_sq8t8GtFFHPSvhSqGYdUxPsnvO0REfjMrKvPcxq8ncInMWCTBAlY7x5s_oE1/w400-h284/download.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhrUkk6ll65qebg_adC-AgMlEzVLpYVIHYE2GKXuXFifuofMpc0BgKTb4dIckCCjtMa3Q8e0Ucz8whMCgesbDkSlVwAoNwO9BEk82xmUqhJ2uOe6p7CClXTSgSoTg1_sq8t8GtFFHPSvhSqGYdUxPsnvO0REfjMrKvPcxq8ncInMWCTBAlY7x5s_oE1/s262/download.jpg)

Sostanzialmente esistono [**stablecoin**](https://darkwhite666.blogspot.com/2022/05/quali-sono-i-rischi-delle-stablecoin.html) sovracollateralizzate (Dai), [**algoritmiche**](https://darkwhite666.blogspot.com/2022/05/la-storia-di-alcune-stablecoin.html) (come Frax, Usdd o l'ormai fallita [**Ust**](https://darkwhite666.blogspot.com/2021/10/lecosistema-di-terra-luna-ust-il.html)) e collateralizzate 1:1 da dollari reali (Usdt, Usdc, Busd).

Per mintare una sovracollateralizzata hai bisogno di tanti capitali, per una algoritmica non hai bisogno di capitali però è un modello troppo pericoloso nelle fasi ribassiste in quanto soggetto ad arbitraggio, questa di Curve potrebbe essere una via di mezzo.

La stablecoin di Curve (**crvUSD**) infatti utilizza un modello completamente diverso, essendo collateralizzata da token LP e funzionante mediante l'algoritmo LLAMMA (Lending-Liquidating Automated Market Maker Algorithm). Sostanzialmente questo modello, per evitare liquidazioni e "bad debit", vende il collaterale (garanzia) in stablecoin, in modo lineare.

MODELLO SOVRA-COLLATERALIZZATO DI DAI

In generale parlando di sovracollateralizzate, Dai viene mintata bloccando un collaterale (ad esempio Eth). Blocco 1000$ e posso prendere in prestito ad esempio il 60% del collaterale in Dai. Cosa succede se Eth scende troppo di prezzo? Parte la margin call o comunque bisogna lockare altro collaterale, per evitare la liquidazione (se non ci fosse la liquidazione, chi ha chiesto il prestito non sarebbe più invogliato a restituirlo, visto che si ritroverebbe in prestito un controvalore in dollari maggiore della garanzia). Per un protocollo che deve evitare questa situazione, quale potrebbe essere il problema? Dover liquidare una garanzia maggiore rispetto alla liquidità presente on chain, questo lo rimarrebbe con "bad debit".

MODELLO DI CRVUSD

Invece per mintare crvUSD, ipotizziamo di bloccare Eth: qualora quest'ultimo scenda troppo di prezzo, piano piano che si riduce il suo valore, viene venduto in stablecoin (Usdc o Usdt). Questo non fa altro che allontanare il prezzo di liquidazione, sino a portarlo all'infinito (cioè impossibile essere liquidati perchè la garanzia rimarrà sempre superiore al prestito, in quanto il caso estremo, per ipotesi, è la conversione al 100% del collaterale Eth in stablecoin). In realtà il collaterale sarà formato da un LP token (inizialmente Eth/Usdc o Eth/Usdt). Pertanto, in un pool Eth/Usdc, man mano che il prezzo di Eth scende, l'LP vende gradualmente Eth in Usdc. Quando il prezzo risale, accade il contrario e Usdc viene venduto per Eth. Se Eth non risale mai, l'LP ha abbastanza Usdc a portata di mano per garantire il debito.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgA4EHPJkGZa1YQj-VOJuL-drSkYTI_2yr89359XOdHorEg-v9-4oJAUhdhcPRM9rWHhqUbqlaIBwytoc41-aYJk2FMUSNjJUwmAHFR6hLnplcJdkD3FA8RW2zSslz_BcFmqA1bPMvySFBOSIL7Onfx7vvpQexcEv8Aea-MP9uJTMvJzoAX-deUvCmu/w363-h400/Screen-Shot-2022-11-23-at-11.17.08-AM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgA4EHPJkGZa1YQj-VOJuL-drSkYTI_2yr89359XOdHorEg-v9-4oJAUhdhcPRM9rWHhqUbqlaIBwytoc41-aYJk2FMUSNjJUwmAHFR6hLnplcJdkD3FA8RW2zSslz_BcFmqA1bPMvySFBOSIL7Onfx7vvpQexcEv8Aea-MP9uJTMvJzoAX-deUvCmu/s601/Screen-Shot-2022-11-23-at-11.17.08-AM.png)

PERMANENT LOSS?

Quali interrogativi pone un modello del genere? Gli swap tra LP token in stablecoin porterebbero ad una "permanent loss" (se 1 ETH=1000$ e quando sta scendendo mi viene swappato in stablecoin, ottengo una perdita quindi una liquidazione progressiva e non istantanea). Infatti l'AMM è destinato ad operare attraverso la liquidità concentrata. Ciò significa che la liquidità stessa è concentrata all'interno di un intervallo. Quando la proporzione dell'LP si sposta troppo da un lato, il collaterale verrà completamente convertito in Eth o Usdc. Questo è l'opposto di come funzionano normalmente gli AMM, in cui il detentore di LP subisce l'impermanent loss, ottenendo sempre meno asset in apprezzamento e più asset in deprezzamento (a causa della divergenza del prezzo dei due token, inseriti inizialmente nel pool 50 e 50%). In questo caso però la perdita è temporanea (a parte qualora si rimuovesse la liquidità dal pool) perchè se i due token si auto-bilanciano tornando in modo progressivo alla situazione iniziale, essa si riduce man mano.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_fFefRywc0dtV_hnoL0e7SJdZR039u7cziEcJdqKAPSUqPPaCSG3XSKukJ_hM_QSGWP9o6KAngmgF3E_rWdKkTsCw5d5L1AGD4_aL6fDnq0GUy04NieA5SLZdtnS0oUhygh-vXJ4YP6pCoo9WQlU9uByfV1__q8z9SNpsVqsnpJcg71pn622KLevl/w640-h286/crvUSD.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_fFefRywc0dtV_hnoL0e7SJdZR039u7cziEcJdqKAPSUqPPaCSG3XSKukJ_hM_QSGWP9o6KAngmgF3E_rWdKkTsCw5d5L1AGD4_aL6fDnq0GUy04NieA5SLZdtnS0oUhygh-vXJ4YP6pCoo9WQlU9uByfV1__q8z9SNpsVqsnpJcg71pn622KLevl/s839/crvUSD.png)

Invece, ad oggi, tramite il modello di Curve la perdita sarebbe permanente. Questo è il principale problema di un modello del genere, tuttavia se esso fosse risolto, la tolleranza al rischio sarebbe molto maggiore. Teoricamente quando questa garanzia è in calo, l'algoritmo liquida automaticamente una parte del tuo portafoglio. Se il prezzo sale, la tua garanzia viene riacquistata. Pertanto, invece di una liquidazione istantanea, il processo avviene su un intervallo continuo.

Questa strategia limita fortemente le tue potenziali perdite e consente una gestione più passiva del prestito. E' un po' come se il prezzo del collaterale è suddiviso in "bande". Invece di depositare ad un prezzo di liquidazione specifico, depositi la garanzia su un intervallo di prezzi di liquidazione. Man mano che il prezzo scende, il contratto tiene traccia di quale banda è "attiva", ovvero quale banda è attualmente in fase di liquidazione.

La liquidità è come detto suddivisa in bande. Una banda più ampia significa che la tua posizione inizia a liquidarsi prima, ma più gradualmente. Un intervallo più piccolo significa che il processo può essere più veloce. Immagina di sottoscrivere un prestito utilizzando 1 Eth, con un intervallo di liquidazione compreso tra $ 1000 e $ 1100. Le tue bande di liquidazione potrebbero avere il seguente aspetto:

Banda 100 ($ 1000 - $ 1020): 0,2 ETH

Banda 101 ($ 1020 - $ 1040): 0,2 ETH

Banda 102 ($ 1040 - $ 1060): 0,2 ETH

Banda 103 ($ 1060 - $ 1080): 0,2 ETH

Banda 104 ($ 1080 - $ 1100): 0,2 ETH

Una volta che il prezzo scende nell'intervallo $ 1080 - $ 1100, la tua posizione inizia a essere liquidata. La tua posizione in $crvUSD è ora supportata da 0,8 ETH e un quantitativo in Usdc. Man mano che il prezzo scende, c'è un'attenuazione. In questo caso e parlando di Fisica, si tratta di un "processo adiabatico" che descrive se qualcosa accade velocemente o lentamente: alcuni sistemi si comportano in modo diverso quando i cambiamenti avvengono troppo veloc...