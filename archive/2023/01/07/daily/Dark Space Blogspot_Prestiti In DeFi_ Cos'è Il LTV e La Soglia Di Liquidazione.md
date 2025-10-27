---
title: Prestiti In DeFi? Cos'è Il LTV e La Soglia Di Liquidazione
url: http://darkwhite666.blogspot.com/2023/01/prestiti-in-defi-cose-il-ltv-e-la.html
source: Dark Space Blogspot
date: 2023-01-07
fetch_date: 2025-10-04T03:18:01.676562
---

# Prestiti In DeFi? Cos'è Il LTV e La Soglia Di Liquidazione

## Visualizzazioni Totali

[![Dark Space Blogspot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZgt0RUZjHgbkLsu7CbFNAiyAMd0qvDL2fubvcBv5c6R04keICe8K0ig6oXxzqa6519xC3S7eBHP3_F60rvo_NqafkHR83xyZwscmsQgwCw_EPQpiDWkgarGw08kUDwteX-zWL_I_uP1w/s1600/ask-fm.png)](https://darkwhite666.blogspot.com/)

TRA I PRIMI IN ITALIA A PARLARE DI BITCOIN (DAL 2012!): PER ESSERE SEMPRE AGGIORNATI SULLE NOVITA' TECNOLOGICHE DEL WEB SEGUITE LA PAGINA FACEBOOK (LINK A SINISTRA)

## venerdì 6 gennaio 2023

### Prestiti In DeFi? Cos'è Il LTV e La Soglia Di Liquidazione

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjr-1PCL8j7J3HzLQ4bG1XSJr_mlQXzR4yz0CuvOo0FHSlTmrWj5ZO6F9oJGXLGKgOOqlrgCVGEQHWJu3bSx_sXSiDhU9Xp_i-fo76cHZpZhs8buWdSl3bfefPKVbF9DXELTKPFVTw7emVXdI7gd6QxgpjungW7EVBzmi4Omahm6cdfGuHMADwSJlZ_/w400-h229/defi-lending-and-borrowing-platform-development.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjr-1PCL8j7J3HzLQ4bG1XSJr_mlQXzR4yz0CuvOo0FHSlTmrWj5ZO6F9oJGXLGKgOOqlrgCVGEQHWJu3bSx_sXSiDhU9Xp_i-fo76cHZpZhs8buWdSl3bfefPKVbF9DXELTKPFVTw7emVXdI7gd6QxgpjungW7EVBzmi4Omahm6cdfGuHMADwSJlZ_/s924/defi-lending-and-borrowing-platform-development.jpg)

Quando si chiede un prestito (**Borrow**) in DeFi sostanzialmente ci si indebita quindi si rischia la liquidazione se la mia garanzia scende troppo di prezzo. Il tutto avviene su piattaforma di **Lending** (Money Market). Un Lender deposita liquidità ed ottiene un'interesse che viene pagato dal Borrower che chiede un prestito (chi chiede un prestito poi dovrà restituirlo con gli interessi e questi vanno a chi deposita liquidità e una parte alla piattaforma). Il tasso di interesse per chi deposita aumenta all'aumentare della domanda per quell'asset. Al contrario, se tutti depositano un asset e nessun lo prende in prestito (poca domanda e tanta offerta), il tasso d'interesse per chi fornisce liquidità di quell'asset...scende. Un Money Market deve sempre avere liquidità libera (cioè una riserva che consenta al Lender di prelevare in qualsiasi momento), a questo proposito ogni piattaforma ha una certa % di saturazione, oltre la quale l'interesse per chiedere un prestito diventa altissimo e allo stesso modo anche l'APY per chi fornisce liquidità diventa altissimo: ciò serve per incentivare i depositi e ridurre i prestiti (perchè costa di più restituirli). All'aumentare del tasso di utilizzo di un asset, aumenta l'interesse per chiedere il prestito (Borrow APY). Ovviamente questi incentivi funzionano se la piattaforma è liquida (molto meno se ha poca liquidità).

PERCHE' CHIEDERE PRESTITI?

Perchè dovrei chiedere un prestito? Magari sto holdando ETH, ho bisogno di liquidità e non li voglio vendere. Blocco i miei ETH come garanzia (collaterale) ed ottengo un prestito (di norma in stablecoin che posso mettere a rendita o utilizzarle per comprare altro o uscire in fiat; prestiti non sono eventi tassabili). Altrimenti potrei anche bloccare ETH (o BTC), prendere stable e comprare altri ETH (o BTC). Di base se 1 ETH vale 1000$ non posso ottenere 1000$ in prestito perchè altrimenti il mio prestito, in pochi secondi, potrebbe diventare sottocollateralizzato (qualora ETH scendesse di prezzo). Se ETH scende a 900$ e ne ho presi 1000$ in prestito potrei non essere più invogliato a ripagare il prestito, per questo motivo posso al massimo prendere in prestito ad esempio 2/3 del collaterale (ovvero blocco 1000$ e ne prendo in prestito 660).

Di solito le strategie di Borrow sono due:

1) Blocco un token volatile e prendo in prestito una stablecoin (vengo liquidato se il mio collaterale scende di prezzo)

2) Blocco una stablecoin e prendo in prestito un token volatile (in questo caso vengo liquidato se la somma presa in prestito sale troppo di prezzo)

Il LTV ci indica la quantità massima che posso prendere in prestito, oltre la quale potrei essere liquidato ("potrei" perchè di solito il LTV massimo è qualche punto in % inferiore rispetto alla liquidazione). Ogni collaterale non deve essere come controvalore in dollari minore rispetto ai prestiti elargiti altrimenti la piattaforma si ritrova con "bad debit" (insolvenza/default). Nessun borrower deve essere insolvente, quando il collaterale scende troppo avviene la liquidazione.

LTV

Il **Loan To Value (LTV)** è dunque il mio potere di indebitamento massimo dopo aver depositato una determinata garanzia (collaterale). "Value" è riferito al mio deposito. Nel momento in cui chiedo un prestito, andrò a depositare una garanzia X. Di questa garanzia posso prendere in prestito un controvalore in dollari inferiore ovviamente alla somma depositata.

Ad esempio, se una garanzia ha un LTV del 60%, puoi prendere in prestito fino a 0,60 ETH (in dollari) per ogni ETH depositato. Se 1 ETH=1000$ posso prendere in prestito al massimo 600 USDC (600$). Ovvero il LTV massimo a cui ti puoi spingere. Di solito il LTV massimo è inferiore alla soglia di liquidazione. Così non fosse, se ipotizziamo appunto la liquidazione sia al 60% e puoi prendere il 60% in prestito, verresti liquidato quando il LTV supera il 60% (magari dopo qualche secondo, se il collaterale scendesse di pochissimo). Invece non ho problemi se LTV si mantiene sotto questa percentuale. Da questo discorso si evince che se la soglia di liquidazione è fissata al 70%, dovrei poter prendere in prestito al massimo un 60 o 65% come LTVmax (nessuno mi vieta, per un questione di sicurezza, di prendere in prestito il 50% o anche meno).

LTV è dunque il rapporto tra "valore preso in prestito"/"deposito". Se ho preso in prestito 400$ e ne ho depositati 1000$, ho un indebitamento dato da 400$/1000$=0.4 per 100=40%.

Se il mio LTV max è del 60% posso prendere in prestito sino a 600$, ovvero 600$/1000$=0.6 per 100=60%.

Come si può vedere, se LTVmax corrisponde alla liquidazione ed ho un LTV massimo del 60%, potrei prendere in prestito 600$ dei 1000$ depositati ma se la mia garanzia scendesse a 999$ (il mio deposito come garanzia è sempre di 1 ETH ma appunto ETH sta scendendo di prezzo), avrei 600$/999$=0.6006 per 100=60,06% (ovvero avendo superato il 60%, i miei asset andrebbero in liquidazione perchè sono sotto-collateralizzati e ne perderei una parte o il prestito mi viene chiuso + una fee di liquidazione). Quando si verifica una liquidazione, i liquidatori rimborsano parte o tutto l'importo in prestito per conto del mutuatario. In cambio, possono acquistare la garanzia con uno sconto e trattenere la differenza come bonus.

Riepilogando, se ho un collateral factor (liquidazione) del 70% sulla somma depositata, dovrei poter prendere in prestito al massimo il 60% (LTV max) della mia somma depositata. Tuttavia, per essere ancora più sicuro, posso prendere in prestito "solo" il 55 o 50% e non il 60% (ovvero sfrutto un potere d'indebitamento inferiore rispetto al massimo, quello che alcune piattaforme chiamano "Borrowing Power"). Queste % sono variabili, in base alla piattaforma. Se il prestito che ho preso arriva a valere il 70% del mio collaterale vengo liquidato (il prestito viene chiuso, il mio collaterale è venduto a sconto + fee di liquidazione).

HEALTH FACTOR

Alcuni protocolli utilizzano l' "Health Factor" che indica quanto è "sicuro" il tuo prestito, calcolato come la proporzione della garanzia depositata rispetto all'importo preso in prestito (rapporto tra LTV attuale e quello della liquidazione). La liquidazione viene evitata se questo fattore è superiore ad 1.

Per approfondire su argomenti simili:

[**Che Differenza C'è Tra Staking e Lending (Interessi)?**](https://darkwhite666.blogspot.com/2021/10/che-differenza-ce-tra-staking-e-lending.html)

[**Come Funziona Tarot: Lending, Borrowing e Leveraged Farming**](https://darkwhite666.blogspot.com/2022/02/come-funziona-tarot-lending-borrowing-e.html)

C-RATIO

Ci sono protocolli come **[Synthetix Network](https://darkwhite666.blogspot.com/2022/08/come-funziona-synthetix-network-snx.html)** che aprono debiti in automatico quando si fa staking del token nativo della piattaf...