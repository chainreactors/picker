---
title: Cos'è La Liquidità Concentrata In DeFi? Range e Fee (CLMM)
url: http://darkwhite666.blogspot.com/2023/03/cose-la-liquidita-concentrata-in-defi.html
source: Dark Space Blogspot
date: 2023-03-07
fetch_date: 2025-10-04T08:52:25.241979
---

# Cos'è La Liquidità Concentrata In DeFi? Range e Fee (CLMM)

## Visualizzazioni Totali

[![Dark Space Blogspot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZgt0RUZjHgbkLsu7CbFNAiyAMd0qvDL2fubvcBv5c6R04keICe8K0ig6oXxzqa6519xC3S7eBHP3_F60rvo_NqafkHR83xyZwscmsQgwCw_EPQpiDWkgarGw08kUDwteX-zWL_I_uP1w/s1600/ask-fm.png)](https://darkwhite666.blogspot.com/)

TRA I PRIMI IN ITALIA A PARLARE DI BITCOIN (DAL 2012!): PER ESSERE SEMPRE AGGIORNATI SULLE NOVITA' TECNOLOGICHE DEL WEB SEGUITE LA PAGINA FACEBOOK (LINK A SINISTRA)

## lunedì 6 marzo 2023

### Cos'è La Liquidità Concentrata In DeFi? Range e Fee (CLMM)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhEjBmLJqc7KFwWMiiOhvYfUXQLHOqC7E1DE_iKsSEmpxSsSlynDx-opOouf7xXHtFd5zH_lUQEz_KWyO7U3h-Umf0FcArZIeoJPG8yRaRwRetWp8cSGUwfclCim4vXicfvkD7Z9gchLWbe0cO3pLKw16Hbay1neHx6I0OCy0cE5D1hfBJLoDxW-R2l/w400-h199/CL.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhEjBmLJqc7KFwWMiiOhvYfUXQLHOqC7E1DE_iKsSEmpxSsSlynDx-opOouf7xXHtFd5zH_lUQEz_KWyO7U3h-Umf0FcArZIeoJPG8yRaRwRetWp8cSGUwfclCim4vXicfvkD7Z9gchLWbe0cO3pLKw16Hbay1neHx6I0OCy0cE5D1hfBJLoDxW-R2l/s730/CL.png)

La "**concentrated liquidity**" su **[Uniswap V3](https://app.uniswap.org/#/swap)** (o **[Raydium](https://raydium.io/)**) è una nuova funzionalità introdotta nell'aprile del 2021. Vengono chiamati CLMM (concentrated liquidity market maker) e migliorano l'uso dell'efficienza dei capitali per i LP, riducendo lo slippage per gli swap.

Per capire di cosa si sta parlando faccio un riepilogo veloce sul funzionamento dei pools di liquidità. Il motore di qualsiasi [**AMM**](https://darkwhite666.blogspot.com/2021/08/come-funzionano-i-dex-amm-automated.html) è la liquidità quindi l'utente deve essere incentivato a fornirla, altrimenti gli scambi non potrebbero avvenire. Sostanzialmente scelgo una coppia (ad esempio wBTC/wETH oppure USDT/USDC) e la fornisco come liquidità. Su questa coppia guadagnerò swap fee e in alcuni casi il token nativo della piattaforma. Questo modello adottato da quasi tutti gli AMM non è ben ottimizzato perchè lavora su intervalli di prezzo da 0 ad infinito (sostanzialmente paga swap fee su tutto l'intervallo ma la rendita è minore rispetto a quello che potrebbe essere). A ciò, si aggiunge anche l' **[Impermanent Loss](https://darkwhite666.blogspot.com/2021/02/cose-limpermanent-loss-e-quali-sono-i.html)** quando i due token scelti divergono troppo di prezzo (quando fornisco liquidità, a meno di utilizzare pool con 3 token tipo quelli di [**Balancer**](https://darkwhite666.blogspot.com/2021/12/cose-il-liquidity-bootstrapping-pool.html), metterò 50% di un token e 50% dell'altro. Il pool si autobilancia quando i due token variano di prezzo uno rispetto all'altro, questa divergenza è nota come Impermanent Loss e rappresenta la differenza che sussiste tra fornire liquidità ed holdare questi token semplicemente nel wallet, a cui vanno però aggiunte swap fee e farming token). Come avrai capito, unici pools senza Impermanent Loss, sono quelli di stablecoin a meno che una delle due non perda il [**peg**](https://darkwhite666.blogspot.com/2022/05/quali-sono-i-rischi-delle-stablecoin.html). Impermament Loss è sempre temporanea e si aggiorna continuamente in base alla volatilità dei due token, diventa però permanente quando prelevo.

LIQUIDITA' CONCENTRATA E COMMISSIONI A GRADINI

Qui sussiste la rivoluzione portata da Uniswap che genera talmente utili (quindi fee) che non ha necessità di fornire il suo token Uni. Gli utenti ricevono solo swap fee che sono molto elevate.

Infatti in Uniswap V3, gli utenti possono fornire liquidità a coppie di token specifiche utilizzando una "gamma" di prezzo personalizzata (concentrata appunto).

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg-WXgHzFR5TF_OqfyKl0SMt3xkM6CK00WxUNzgW0OVECBy-feTmUQPDg0kZmnQ-fy0kC37iW7b7ZOL-CWrDR68GJgMzBRlhlRF5Qw5Ks8TJSMWPRJNgnZsLd4PvaM81DQssz8gE2DgvPROimciQ36oqfqRpQ135iSlv5mfVRdeU08HemfSHfYvnkbd/w640-h290/Uniswap%20V3.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg-WXgHzFR5TF_OqfyKl0SMt3xkM6CK00WxUNzgW0OVECBy-feTmUQPDg0kZmnQ-fy0kC37iW7b7ZOL-CWrDR68GJgMzBRlhlRF5Qw5Ks8TJSMWPRJNgnZsLd4PvaM81DQssz8gE2DgvPROimciQ36oqfqRpQ135iSlv5mfVRdeU08HemfSHfYvnkbd/s572/Uniswap%20V3.png)

In pratica, gli utenti possono specificare un range di prezzo entro cui desiderano fornire liquidità e possono concentrare questa liquidità in una particolare zona. Questo consente loro di guadagnare rendimenti maggiori rispetto alla fornitura di liquidità su una gamma di prezzi indefinita (da 0 ad infinito). In questo caso, tutto il mio capitale sarà concentrato in quel range (e non disposto in un intervallo infinito).

Per esempio, supponiamo che un utente voglia fornire liquidità per la coppia wBTC/USDT e che il prezzo attuale sia di 21000 USDT per wBTC. L'utente potrebbe decidere di fornire liquidità solo per il range di prezzo tra 19000 e 23000 USDT per wBTC, concentrandosi quindi in quella fascia. Ciò significa che se il prezzo di wBTC dovesse oscillare all'interno di quel range, l'utente guadagnerebbe maggiori rendimenti rispetto a coloro che forniscono liquidità su un prezzo infinito (non concentrato). Le fees che si ricevono dipendono dalla quantità di liquidità fornita dall'utente, dal volume degli scambi e dal prezzo degli asset scambiati. Quando gli utenti forniscono liquidità con una coppia di asset specifica, ricevono in cambio degli LP che rappresentano la loro quota di partecipazione alla liquidità di quella coppia. Ogni volta che avviene uno scambio in quella coppia di asset, una parte delle commissioni di scambio viene prelevata dal protocollo e una parte distribuita tra gli utenti che forniscono liquidità in quella coppia, in modo proporzionale alla quota fornita.

Inoltre, in questi modelli, le commissioni vengono calcolate in base alla posizione dell'utente sulla "gamma" di prezzo che ha scelto di fornire liquidità. In pratica, gli utenti che forniscono liquidità in una zona più "concentrata" della gamma di prezzo guadagnano commissioni maggiori rispetto a quelli che forniscono liquidità su un intervallo più ampio di prezzi.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhvXBmUvHt1BIbKHySKBB22q5sLUEL01EtHghOUkkDARnWPB7j9rqRADug-8iw1rJJjNM4lLV3beGZth2dSpGF1Y714zdU0EVnBoV57mbljf6NPJB6TQepEzPxkOk8pBY81S2xj9TqfkHGvcClAEQ1jeUvvJdP6EE_pZq2x95JBOu0EIAbt6Xb-6Iko/w640-h322/0_Gs7KhiJ8V870Mrmz.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhvXBmUvHt1BIbKHySKBB22q5sLUEL01EtHghOUkkDARnWPB7j9rqRADug-8iw1rJJjNM4lLV3beGZth2dSpGF1Y714zdU0EVnBoV57mbljf6NPJB6TQepEzPxkOk8pBY81S2xj9TqfkHGvcClAEQ1jeUvvJdP6EE_pZq2x95JBOu0EIAbt6Xb-6Iko/s1228/0_Gs7KhiJ8V870Mrmz.png)

Sostanzialmente si tratta di un modello di commissione "a gradini", in cui il tasso di commissione varia in base alla gamma di prezzo in cui si fornisce liquidità. In generale, le zone di prezzo più concentrate tendono ad avere guadagni più alti rispetto alle zone di prezzo più ampie. Per esempio, scegliendo di fornire liquidità per una coppia di asset con una gamma di prezzo (range) molto ampia, a parità di pool (quindi dei 2 token scelti) otterrebbero commissioni più basse rispetto a un utente che fornisce liquidità con una gamma di prezzo più concentrata (intervallo più ristretto).

SCELTA DELLE FEES

In Uniswap v3, gli utenti possono anche scegliere il livello di tasso di commissione che desiderano applicare ai loro pools, selezionando uno dei quattro "fee tier" disponibili:

1) 0,01% (consigliato per stablecoin: USDC/USDT)

2) 0,05% (potresti usarlo per wETH/wBTC, cripto ad alti volumi ed alta market cap)

3) 0,3% (ad esempio wETH/USDC, per la maggior parte dei pools)

4) 1% (per pools esotici integranti token con market cap molto diversa, tipo wETH/BOSON)

La scelta del "fee tier" dipende dalla coppia di asset scelta e dal tipo di token fornito in liquidità (stablecoin o token esotici). In generale, le coppie di stablecoin come USDC/USDT o DAI/USDC, dovrebbero avere fee tier più bassi rispetto a coppie di to...