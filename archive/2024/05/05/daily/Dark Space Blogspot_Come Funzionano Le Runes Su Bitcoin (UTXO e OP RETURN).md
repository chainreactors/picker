---
title: Come Funzionano Le Runes Su Bitcoin (UTXO e OP RETURN)
url: http://darkwhite666.blogspot.com/2024/05/come-funzionano-le-runes-su-bitcoin.html
source: Dark Space Blogspot
date: 2024-05-05
fetch_date: 2025-10-06T17:17:24.425653
---

# Come Funzionano Le Runes Su Bitcoin (UTXO e OP RETURN)

## Visualizzazioni Totali

[![Dark Space Blogspot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZgt0RUZjHgbkLsu7CbFNAiyAMd0qvDL2fubvcBv5c6R04keICe8K0ig6oXxzqa6519xC3S7eBHP3_F60rvo_NqafkHR83xyZwscmsQgwCw_EPQpiDWkgarGw08kUDwteX-zWL_I_uP1w/s1600/ask-fm.png)](https://darkwhite666.blogspot.com/)

TRA I PRIMI IN ITALIA A PARLARE DI BITCOIN (DAL 2012!): PER ESSERE SEMPRE AGGIORNATI SULLE NOVITA' TECNOLOGICHE DEL WEB SEGUITE LA PAGINA FACEBOOK (LINK A SINISTRA)

## sabato 4 maggio 2024

### Come Funzionano Le Runes Su Bitcoin (UTXO e OP RETURN)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjcsDgQmV68lXjPEYURls6g45N5sskW8EiA3ZsN8Qz2K2nO7NY38O6TwXvqBdUsGXqOIZVFqpWc0iKiSTvdgJlN_rgaiBuPI2pIAhqWw_ygtmPfE5D_K_znREKjxhqhpiHmSsqegz6HXCpcxKJdcsCKasvAMhkLl6Db2_Dm-XixxOEDVPxLu9YOTukeqcU/w400-h266/NFT-Plazas-Blog-Post-template-800-x-380px-28-fotor-20240304132415-scaled.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjcsDgQmV68lXjPEYURls6g45N5sskW8EiA3ZsN8Qz2K2nO7NY38O6TwXvqBdUsGXqOIZVFqpWc0iKiSTvdgJlN_rgaiBuPI2pIAhqWw_ygtmPfE5D_K_znREKjxhqhpiHmSsqegz6HXCpcxKJdcsCKasvAMhkLl6Db2_Dm-XixxOEDVPxLu9YOTukeqcU/s614/NFT-Plazas-Blog-Post-template-800-x-380px-28-fotor-20240304132415-scaled.jpg)

La blockchain di **Bitcoin** è sostanzialmente un database che contiene transazioni, tuttavia nessuno vieta di aggiungere un testo, immagini o video. Messaggi scritti sulla blockchain di Bitcoin ci sono da sempre, tuttavia negli ultimi anni una delle teorie più note è stata quella degli **[Ordinals](https://darkwhite666.blogspot.com/2023/02/ordinals-ed-inscriptions-su-bitcoin.html)** che sostanzialmente numera in modo arbitrario i Satoshi tramite il software Ord (questo concetto è stato sfruttato dai token **[Brc20](https://darkwhite666.blogspot.com/2023/05/come-funzionano-i-token-brc20-comprare.html)** e dalle **[Inscriptions](https://darkwhite666.blogspot.com/2023/02/ordinals-ed-inscriptions-su-bitcoin.html)** in cui vengono aggiunti dati arbitrari, ovvero testi, immagini e quant'altro, ad una transazione dove viene spostato BTC). Va sottolineato che tutto ciò funziona al di fuori del consenso della blockchain di Bitcoin (i miners vedono solo lo spostamento di Satoshi) ed usa regole proprie.

TRANSAZIONI BITCOIN: UTXO E OP\_RETURN

Ipotizziamo di inviare 0.2 BTC ad un indirizzo, questi 0.2 BTC sono inizialmente associati ad un indirizzo pubblico quindi ad una chiave privata e sono degli UTXO (non spesi). Ogni UTXO contiene un'hash (impronta associata alla chiave pubblica) e il quantitativo di BTC. Una volta inviati, quell'UTXO diventa "speso" e viene creato un nuovo UTXO associato ad una nuova chiave privata (il ricevente della transazione).

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigMfTt3THU_7AylZcXjlOCs4m0-isC6DWCik1HoznZS_Adyg0cdzxEswxSCd_OcqmKVH7BvPk08Cl7Iktq9zw8-JVhJF70Kdwj5MXJxCulxWY_0Gg3sS5lvHlwsjFLzZBG_JnCe0gdG0S0M-paeotUGtKhJyX17Mn_3biOrsEdzWxYmiJSqCY5WbHl7qM/w400-h200/2-c023ccc2-a302-4d24-bf2d-e404c80d07f2.jpeg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigMfTt3THU_7AylZcXjlOCs4m0-isC6DWCik1HoznZS_Adyg0cdzxEswxSCd_OcqmKVH7BvPk08Cl7Iktq9zw8-JVhJF70Kdwj5MXJxCulxWY_0Gg3sS5lvHlwsjFLzZBG_JnCe0gdG0S0M-paeotUGtKhJyX17Mn_3biOrsEdzWxYmiJSqCY5WbHl7qM/s1831/2-c023ccc2-a302-4d24-bf2d-e404c80d07f2.jpeg)

Già nei primi anni della vita di Bitcoin, al posto dell'indirizzo di ricezione, si inserivano messaggi casuali (rispettando ovviamente il formato di una chiave pubblica) "burnando" frazioni di BTC (che appunto diventavano per sempre "non spendibili" essendo associati a chiavi pubbliche di cui nessuno aveva la chiave privata. Sostanzialmente ciò si basa sull'inviare una transazione ad un indirizzo pubblico con dati randomici (UTXO non spendibili ma salvati per sempre sui full node di Bitcoin).

Tuttavia è possibile inviare un messaggio sulla blockchain di Bitcoin utilizzando un'operazione denominata OP\_RETURN all'interno di una transazione.  OP\_RETURN è un codice operativo all'interno degli script di transazione di Bitcoin che consente di inserire dati aggiuntivi e arbitrari sulla blockchain senza richiedere una destinazione per BTC. Questo è utile per includere metadati o messaggi sulla blockchain senza trasferire effettivamente BTC. Il messaggio da inviare deve essere formattato correttamente e rispettare i limiti di dimensione per l'inserimento di dati nella blockchain di Bitcoin. Dopo aver creato la transazione con il messaggio OP\_RETURN, basta inviarla alla rete Bitcoin utilizzando il wallet scelto. La transazione verrà quindi trasmessa attraverso la rete Bitcoin e inclusa in un blocco da un miner. Una volta che la transazione è stata confermata e inclusa in un blocco sulla blockchain di Bitcoin, puoi verificare il messaggio consultando l'output della transazione contenente l'operazione OP\_RETURN. Potrai leggere il messaggio incluso e confermare che sia stato registrato correttamente sulla blockchain. Ovviamente l'inserimento di un messaggio sulla blockchain di Bitcoin attraverso l'operazione OP\_RETURN richiede il pagamento delle fee, inoltre sussistono limiti alla dimensione dei dati che possono essere inclusi in una singola transazione.

RUNES E RUNESTONE

Le Runes permettono di creare token fungibili su Bitcoin utilizzando il modello UTXO. Si tratta di UTXO con amount inviato pari a 0 (a parte le fee di rete). Runestones sono messaggi specifici del protocollo Runes, che vengono inseriti in un output successivamente all'OP\_RETURN seguito dall'OP\_13. L'output sarà del tipo:

OP\_RETURN + OP\_13 + <runestones payload>

dove <runestones payload> è il vero e proprio contenuto specifico relativo al protocollo Runes. OP\_RETURN dice al protocollo Bitcoin di ignorare da lì in poi (i messaggi hanno valore solo nel protocollo Runestone con le sue regole).

Tramite la funzione "edicts" è possibile introdurre della logica custom nei trasferimenti delle rune tra gli input e gli output di una transazione. "Etching" consente di creare una rune, seguendo uno schema commit-reveal. "Mint" permette di mintare una rune. Nel momenti in cui si crea una rune, tramite "etching" è possibile settare una serie di attributi:

-premine

-total supply

-numero di rune per ogni transazione

-divisibilità (quante cifre dopo la virgola può avere)

Per creare una rune, il primo passaggio è quello di andare ad eseguire una transazione che contiene un output con una runestone al suo interno. E questa runestone deve contenere a sua volta un messaggio di etching. Ciò di cui avremo bisogno è:

-il ticker: ipotizziamo la rune XXX (in realtà ora il minimo è 13e sino a 28 caratteri ma nel tempo sarà possibile creare simboli più corti. Diminuisce di un carattere ogni 4 mesi sino ad arrivare ad 1 solo carattere nell'halving 2028)

-la supply: ad esempio massimo 21 unità

-premine di una parte di supply (sul proprio address) o no premine (mintabile da tutti)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg8ZvCtORl3FO7XfueXrngGvK9WQJ_igPFJG9-3zY7lu-ptmI4aA2PT-TaHTBSIjJiBBnVC7pm0_vS1dbFahq-ODz07VhTniszEt1RbdVqgdwGoKBC-dCktg-x499scn1gpt5X_eoXOnSELSV7_1noEvmmULLmdAWhwalTIxuOLb6iyHHoEJJcs4er68C8/w301-h400/Runes.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg8ZvCtORl3FO7XfueXrngGvK9WQJ_igPFJG9-3zY7lu-ptmI4aA2PT-TaHTBSIjJiBBnVC7pm0_vS1dbFahq-ODz07VhTniszEt1RbdVqgdwGoKBC-dCktg-x499scn1gpt5X_eoXOnSELSV7_1noEvmmULLmdAWhwalTIxuOLb6iyHHoEJJcs4er68C8/s561/Runes.png)

Inoltre potremmo scegliere se fare "open mint", ossia consentire a tutti di mintare questa rune fino ad esaurimento supply, oppure consentirlo solo ad alcuni, oppure non consentire il mint a nessuno.

Fatto ciò, è sufficiente pubblicare una transazione Bitcoin in cui uno degli output sia:

OP\_RETURN + OP\_13 + RUNESTONE

dove la runestone include l'etching con il ticker, supply e premine.

Non appena questa transazione viene aggiunta nella blockchain di Bitcoin la nostra rune è creata e, se avessimo settato un premine, immediatamente avremmo...