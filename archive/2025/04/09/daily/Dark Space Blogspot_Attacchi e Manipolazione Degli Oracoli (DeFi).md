---
title: Attacchi e Manipolazione Degli Oracoli (DeFi)
url: http://darkwhite666.blogspot.com/2025/04/attacchi-e-manipolazione-degli-oracoli.html
source: Dark Space Blogspot
date: 2025-04-09
fetch_date: 2025-10-06T22:20:21.262316
---

# Attacchi e Manipolazione Degli Oracoli (DeFi)

## Visualizzazioni Totali

[![Dark Space Blogspot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZgt0RUZjHgbkLsu7CbFNAiyAMd0qvDL2fubvcBv5c6R04keICe8K0ig6oXxzqa6519xC3S7eBHP3_F60rvo_NqafkHR83xyZwscmsQgwCw_EPQpiDWkgarGw08kUDwteX-zWL_I_uP1w/s1600/ask-fm.png)](https://darkwhite666.blogspot.com/)

TRA I PRIMI IN ITALIA A PARLARE DI BITCOIN (DAL 2012!): PER ESSERE SEMPRE AGGIORNATI SULLE NOVITA' TECNOLOGICHE DEL WEB SEGUITE LA PAGINA FACEBOOK (LINK A SINISTRA)

## martedì 8 aprile 2025

### Attacchi e Manipolazione Degli Oracoli (DeFi)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgCmfAgCVKai_PGyVHtELv1xCnNRKKEQr3g65lYP80JpBXKH1zaBCdDiPrkTgU5YXgiB8w1aMamVUUHNKlZG-21mxUuecf2u9e_RLk-IoIheB59wfFNRSxX7AhUM02fnqs8WArOVTiCYmbv5yzur2xLCZ8DsJXJ53oG1CG4sUMtKf6-G8lclOfJbuQukOA/s320/Oracle%20Attack.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgCmfAgCVKai_PGyVHtELv1xCnNRKKEQr3g65lYP80JpBXKH1zaBCdDiPrkTgU5YXgiB8w1aMamVUUHNKlZG-21mxUuecf2u9e_RLk-IoIheB59wfFNRSxX7AhUM02fnqs8WArOVTiCYmbv5yzur2xLCZ8DsJXJ53oG1CG4sUMtKf6-G8lclOfJbuQukOA/s368/Oracle%20Attack.png)

La manipolazione degli **oracoli** è una delle vulnerabilità più pericolose nei protocolli DeFi, dato che gli oracoli forniscono dati esterni alla blockchain (feed dei prezzi) per consentire l’esecuzione corretta di smart contract. Gli attacchi agli oracoli si verificano quando un attaccante manipola i prezzi o i dati forniti agli smart contract, inducendoli a prendere decisioni errate. Quali? Liquidare posizioni, alterare prestiti, garantire arbitraggi artificiali (arbitraggio vuol dire comprare un asset ad X prezzo e rivenderlo subito dopo ad un prezzo più alto) o influenzare gli swap.

Abbiamo due grosse categorie:

-Oracoli nativi usano dati presi direttamente dalla blockchain, come i prezzi dei token in pool di liquidità su DEX come Uniswap. Sono molto vulnerabili alla manipolazione del mercato su singole piattaforme.

-Off-chain oracles aggregano dati da fonti esterne (exchange centralizzati, fonti multiple) e li riportano sulla blockchain tramite un sistema di feed decentralizzati, come Chainlink. Sono più sicuri, ma possono avere latenze.

MANIPOLAZIONE DI ORACOLI ON CHAIN

Gli oracoli basati su DEX, come quelli che utilizzano i dati di prezzi da Uniswap o Sushiswap, sono vulnerabili poiché i prezzi in questi AMM vengono determinati dalle riserve nei pool di liquidità. Questi pool possono essere facilmente manipolati se hanno bassa liquidità o se un attaccante ha accesso a grandi quantità di capitale.

Ad esempio un attaccante prende in prestito una grande quantità di token (ETH o USDC) tramite un flash loan ed utilizza questi fondi per comprare o vendere grandi quantità di un asset (ad esempio, una memecoin detto X token) su un DEX come Uniswap. Ciò provoca una variazione significativa nel prezzo dell’asset, perché il DEX ricalcola il prezzo in base alla nuova distribuzione di riserve nel pool.

Se l'attaccante compra X token in grande quantità, ne aumenta il prezzo in modo significativo. Se un protocollo di prestiti utilizza l'oracolo del DEX manipolato per determinare il prezzo del token X, l'attaccante può ora sfruttare il prezzo falsificato.

Se il prezzo di Token X è stato artificialmente gonfiato, l'attaccante può usarlo come collaterale per prendere in prestito più fondi di quelli che dovrebbe ricevere. Se il prezzo è stato abbassato, l’attaccante potrebbe far sì che gli smart contract liquidino posizioni di altri utenti, acquistando i loro asset a prezzi scontati. Dopo aver realizzato il guadagno sfruttando l'oracolo manipolato, l'attaccante restituisce il flash loan, mantenendo il profitto netto. L'oracolo del DEX segnala questo nuovo prezzo al protocollo DeFi. Immagina ad esempio che X token raddoppia il prezzo quindi può essere preso messo a collaterale prendendo in prestito asset con valore più alto. L'attaccante deposita X come collaterale nel protocollo di prestito (che lo valuta a 2$ invece di 1$), ottenendo in cambio un prestito esagerato (quasi il doppio di quanto avrebbe dovuto ricevere). Successivamente, l’attaccante vende i token X al prezzo normale su un altro mercato e restituisce il flash loan, incassando la differenza.

MANIPOLAZIONE DI ORACOLI OFF CHAIN

Gli oracoli off-chain aggregano dati da fonti esterne (Binance, Coinbase, CoinMarketCap, CoinGecko, etc) per fornire un prezzo medio. Oracoli decentralizzati come Chainlink utilizzano una rete di nodi che trasmettono dati alla blockchain. Sebbene questi siano più sicuri rispetto agli oracoli on-chain, possono essere vulnerabili a manipolazioni se una parte significativa dei nodi viene compromessa.

In un oracolo decentralizzato, se l'attaccante riesce a corrompere un numero sufficiente di nodi (chiamati reporter), può falsificare il prezzo fornito dall'oracolo. Anche se i nodi non sono compromessi, l'attaccante potrebbe manipolare il prezzo dell'asset sugli exchange centralizzati da cui i nodi prelevano i dati. Ad esempio, può fare trading con enormi volumi su piccoli exchange o mercati con bassa liquidità per alterare temporaneamente i prezzi.

Se l'oracolo aggrega dati da exchange con bassa liquidità, l'attaccante potrebbe effettuare ordini massivi su questi exchange per manipolare i prezzi riportati. Una volta manipolato il prezzo, l'oracolo decentralizzato lo trasmette alla blockchain, inducendo gli smart contract ad agire in modo errato.

A questo punto, potrebbe:

-far liquidare le posizioni di altri utenti

-ottenere prestiti eccessivi basati su collaterale sopravvalutato

-comprare asset a prezzi gonfiati o sottovalutati, approfittando della manipolazione.

-arbitraggio (se gli oracoli presentano ritardi di sincronizzazione, un attaccante potrebbe sfruttare la differenza tra il prezzo aggiornato e quello obsoleto per eseguire arbitraggi)

ATTACCO SYBIL SU ORACOLI DECENTRALIZZATI

Un attacco Sybil si verifica quando un attaccante crea molteplici identità false in un sistema decentralizzato per ottenere il controllo.

L'attaccante crea molteplici nodi Sybil in un oracolo decentralizzato, ciascuno dei quali fornisce dati di prezzo. Se l'oracolo accetta dati senza un'adeguata verifica di affidabilità (ad esempio, assegnando peso uguale a tutti i nodi), l'attaccante può inviare dati di prezzo falsificati attraverso i suoi nodi Sybil. Gli smart contract che utilizzano questi dati di prezzo alterati prenderanno decisioni basate su informazioni errate, come liquidare posizioni o approvare prestiti sbagliati.

CONTROMISURE

Oracoli molto evoluti come Chainlink utilizzano meccanismi di sicurezza avanzati, inclusa la diversificazione delle fonti di dati, per rendere più difficile la manipolazione. Aggregando dati da più fonti con un'ampia rete di nodi e svolgendo delle medie sui feed dei prezzi, è molto più difficile per un attaccante manipolare il prezzo. Alcuni oracoli utilizzano la media ponderata del prezzo nel tempo (TWAP) per prevenire manipolazioni temporanee. Invece di usare il prezzo corrente, viene calcolata una media su un periodo (ad esempio 30 minuti), riducendo l'effetto di brevi fluttuazioni artificiali.

Inoltre invece di utilizzare solo i prezzi da un singolo DEX o exchange, i protocolli possono aggregare dati da molte fonti, inclusi exchange centralizzati e decentralizzati, riducendo la possibilità di manipolazione su una singola piattaforma.

Pubblicato da
[DarkDave.|.666](https://www.blogger.com/profile/02696807736631988356 "author profile")

alle
[17:54](https://darkwhite666.blogspot.com/2025/04/attacchi-e-manipolazione-degli-oracoli.html "permanent link")

[![](//img1.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/1856644955194422917/2609130950770302344 "Post per email")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=1856644955194422917&postID=2609130950770302344&from=pencil "Modifica post")

[Invia tramite email](https://www.blogger.com/share-post.g?blogID=185664495519442291...