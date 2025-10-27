---
title: Come Funziona StarkWare e STARK Proof: StarkEx e StarkNet
url: http://darkwhite666.blogspot.com/2022/12/come-funziona-starkware-e-stark-proof.html
source: Dark Space Blogspot
date: 2022-12-31
fetch_date: 2025-10-04T02:49:12.743517
---

# Come Funziona StarkWare e STARK Proof: StarkEx e StarkNet

## Visualizzazioni Totali

[![Dark Space Blogspot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZgt0RUZjHgbkLsu7CbFNAiyAMd0qvDL2fubvcBv5c6R04keICe8K0ig6oXxzqa6519xC3S7eBHP3_F60rvo_NqafkHR83xyZwscmsQgwCw_EPQpiDWkgarGw08kUDwteX-zWL_I_uP1w/s1600/ask-fm.png)](https://darkwhite666.blogspot.com/)

TRA I PRIMI IN ITALIA A PARLARE DI BITCOIN (DAL 2012!): PER ESSERE SEMPRE AGGIORNATI SULLE NOVITA' TECNOLOGICHE DEL WEB SEGUITE LA PAGINA FACEBOOK (LINK A SINISTRA)

## venerdì 30 dicembre 2022

### Come Funziona StarkWare e STARK Proof: StarkEx e StarkNet

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhl7W3a81ZnIET_ZRaJXqasgVYCrAyWdHrAjtcXg3SZZL9jvNf8vvOh87hzyevFyaqPJVq_qg_jKpY2IQqyti5xuhq8ybvoDrNZ3Cd0o-UXAWZaL-tX6BAxPIUFArNYbeH9SgFkwhzZZArSRXbFrXjY112dy0BYn_ONrgyO0zWFDBO3jpgQePo5lLOd/w400-h284/BUO94cDgRieGKyVpIk0z_21_04_What-is-StarkWare-STARK.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhl7W3a81ZnIET_ZRaJXqasgVYCrAyWdHrAjtcXg3SZZL9jvNf8vvOh87hzyevFyaqPJVq_qg_jKpY2IQqyti5xuhq8ybvoDrNZ3Cd0o-UXAWZaL-tX6BAxPIUFArNYbeH9SgFkwhzZZArSRXbFrXjY112dy0BYn_ONrgyO0zWFDBO3jpgQePo5lLOd/s608/BUO94cDgRieGKyVpIk0z_21_04_What-is-StarkWare-STARK.jpg)

L'ecosistema di **[Starkware](https://starkware.co/)** è basato su STARK Proof (Scalable, Transparent ARgument Of Knowledge) che consente la verifica delle informazioni. Starkware è la società madre di queste soluzioni di scalabilità di ZK-rollup (ZK-snarks). Esse permettono di elaborare calcoli di grandi dimensioni, generare una dimostrazione per la correttezza degli stessi e in seguito la verifica.

Le prove ZK sono ottime anche per la privacy perché invece di mostrare i dettagli di una transazione, vedi solo la prova che la transazione è avvenuta. E' un po' come se al posto di vedere un 6+6= 12 e 3+3=6, vedi solo un 12 e un 6, e il 6 è rappresentato dal codice A1. Quando vedi A1, puoi dimostrare che le altre transazioni sono 6+6= 12 e 3+3= 6, ma non devi necessariamente vedere i singoli componenti che compongono la prova A1 (questo vuol dire Zero Conoscenza: mostrare la prova ma non i passaggi). Inoltre, puoi mostrare a qualcun altro la prova "A1" e loro possono sapere che un risultato è valido senza vedere le informazioni o i dati all'interno della prova. Dunque A1 è tutto ciò che si sa sulla transazione ma non si sanno le singole parti della transazione. La prova protegge gli input privati ​​senza rivelare altre informazioni. Le prove sulle reti blockchain si riducono a tre componenti, la dichiarazione, la persona che prova la dichiarazione e la persona che verifica la dichiarazione.

Per approfondire: [**Qual è La Differenza Tra ZK Rollups ed Optimistic Rollups?**](https://darkwhite666.blogspot.com/2022/08/qual-e-la-differenza-tra-zk-rollups-ed.html)

Il tipo di ZK usato da StarkWare è chiamato STARK appunto e questi svolgono un ruolo chiave nella scalabilità della blockchain consentendo di eseguire calcoli off-chain, dove è più economico, lasciando solo la verifica, che richiede una frazione del calcolo, da eseguire on-chain. In altre parole, eseguendo pochissimi calcoli on-chain, il validatore verifica l'integrità di un calcolo molto più ampio eseguito off-chain. I layer 2 che utilizzano STARK Proof raggruppano e calcolano migliaia di transazioni (ciò permette anche di risparmiare sulla larghezza di banda), quindi ne verificano la validità on-chain con un'unica prova. Il costo del processo on-chain viene suddiviso tra tutte le transazioni nel batch. Il sistema sfrutta la sicurezza della blockchain Ethereum e basso costo del gas per transazione svolgendo le operazioni più dispendiose off-chain. Un aspetto negativo è che si tratta di codice Closed Source.

A differenza degli SNARKS (utilizzati da altri layer 2 ZK, tipo Polygon), STARK garantisce anche una sicurezza post quantistica. La sicurezza quantistica si riferisce a una resistenza che non può essere spezzata da un qualche tipo di attacco proveniente da computer quantistici. I computer quantistici sono più intelligenti e veloci dei computer classici, in grado di eseguire calcoli crittografici in pochi minuti che per i computer classici richiederebbero centinaia di migliaia di anni. La velocità degli attacchi di cui sono capaci i computer quantistici è attualmente difficile da capire. Anche se oggi ancora poco diffusi potrebbero essere una minaccia futura, tuttavia, anche una volta diffusi, gli STARK sono considerati al sicuro da questi attacchi "post-quantici".

StarkWare fornisce due soluzioni per scalare Ethereum con STARK: StarkEx e StarkNet.

STARKEX

**[StarkEx](https://dashboard.starkware.co/starkex)** è un framework per la creazione di soluzioni di scalabilità che permette di svolgere calcoli off-chain a basso costo. Esso è utilizzato da Immutable X (market NFT), **[Sorare](https://sorare.com/r/0xdavide)** (fantacalcio, fantabaseball e fantabasket con NFT), dYdX (exchange decentralizzato) o Celer. Una prova STARK, che attesta la correttezza dell'esecuzione, viene generata off-chain. Tale prova può includere fino a 500.000 transazioni. La prova viene quindi inviata al verificatore STARK per essere accettata on-chain. La verifica riguarda tutte le transazioni raggruppate in una sola, per un costo del gas notevolmente minore rispetto a quanto pagheresti su Ethereum. StarkEx potrebbe essere la soluzione giusta per un'applicazione che è in gran parte autonoma e si adatta alle API fornite da StarkEx stesso.

Qui puoi approfondire su Sorare: [**Play To Earn Su Blockchain? Guida Veloce a Sorare: Calcio, MLB e NBA**](https://darkwhite666.blogspot.com/2022/09/play-to-earn-su-blockchain-guida-veloce.html)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiGNSfK2HWTfYeG77P8s3MTLf5ITGr3PRGxBUwqWCnJxrQL288HdQlXvkT-i03wYEBdCLkvkS048daixBvTKpgz96k9stm5MZGaQB9QC7SPvToloIfJeMmBfVDSdjjJb3C39TOSKrxwb3PBieDXnwGYREQli-yUiUC7te3u19cxXsiv0L4q-STaCsqs/w400-h128/5785298_watermarknone.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiGNSfK2HWTfYeG77P8s3MTLf5ITGr3PRGxBUwqWCnJxrQL288HdQlXvkT-i03wYEBdCLkvkS048daixBvTKpgz96k9stm5MZGaQB9QC7SPvToloIfJeMmBfVDSdjjJb3C39TOSKrxwb3PBieDXnwGYREQli-yUiUC7te3u19cxXsiv0L4q-STaCsqs/s218/5785298_watermarknone.jpg)

Starkware ha già annunciato che ci sarà un airdrop del token STARK che probabilmente ingloberà le community sia di StarkEx che di StarkNet. A loro volta, queste 2 soluzioni di scalabilità potrebbero in futuro creare anche il loro token. Se vuoi essere eleggibile ti consiglio di interagire con **[Sorare](https://sorare.com/r/0xdavide)** per StarkEx (puoi utilizzare Metamask e vincere qualche giocatore all'asta, trovi la guida sopra). Di solito quando si interagisce con piattaforme senza token, qualora poi il protocollo lanciasse il suo token, premia gli early adopters che hanno usato il protocollo. L'airdrop di Optimism (altro layer 2) andava da 1500$ a circa 20000$ in token OP, poi vendibili in euro o dollari sugli exchange dove questo token è stato listato.

STARKNET

**[StarkNet](https://starknet.io/)** è un layer 2 ZK senza autorizzazione in cui qualsiasi utente o sviluppatore può distribuire smart contract. Esso è stato creato da sviluppatori israeliani, tra cui un membro fondatore di ZeroCash. All'interno dell'ecosistema StarkNet, il tuo contratto può interagire con qualsiasi altro contratto distribuito su StarkNet, consentendo la creazione di protocolli componibili. I contratti StarkNet possono anche interagire con i contratti Ethereum tramite il passaggio di messaggi asincroni. A differenza di StarkEx, in cui le applicazioni sono responsabili dell'invio delle transazioni, StarkNet sequenzia le transazioni in batch e le invia per essere elaborate e verificate dai sequencer di StarkWare. StarkNet supporta la modalità di disponibilità dei dati di rollup, il che significa che lo stato del rollup viene scritto su Ethereum insieme alle prove STARK. Ci sono molte piattaforme già attive: giochi, intelligenza artificiale, market NFT ed altre dapps. StarkNet potrebbe...