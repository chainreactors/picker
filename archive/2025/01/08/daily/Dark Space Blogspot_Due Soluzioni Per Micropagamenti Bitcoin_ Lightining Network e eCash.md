---
title: Due Soluzioni Per Micropagamenti Bitcoin: Lightining Network e eCash
url: http://darkwhite666.blogspot.com/2025/01/due-soluzioni-per-micropagamenti.html
source: Dark Space Blogspot
date: 2025-01-08
fetch_date: 2025-10-06T20:27:04.961900
---

# Due Soluzioni Per Micropagamenti Bitcoin: Lightining Network e eCash

## Visualizzazioni Totali

[![Dark Space Blogspot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZgt0RUZjHgbkLsu7CbFNAiyAMd0qvDL2fubvcBv5c6R04keICe8K0ig6oXxzqa6519xC3S7eBHP3_F60rvo_NqafkHR83xyZwscmsQgwCw_EPQpiDWkgarGw08kUDwteX-zWL_I_uP1w/s1600/ask-fm.png)](https://darkwhite666.blogspot.com/)

TRA I PRIMI IN ITALIA A PARLARE DI BITCOIN (DAL 2012!): PER ESSERE SEMPRE AGGIORNATI SULLE NOVITA' TECNOLOGICHE DEL WEB SEGUITE LA PAGINA FACEBOOK (LINK A SINISTRA)

## martedì 7 gennaio 2025

### Due Soluzioni Per Micropagamenti Bitcoin: Lightning Network e eCash

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiGCZjRSHcBJIvwQlN-RqVxBLyi5wDDi9WjjQpFVM9vIswdHeBV8l51cFbPDZihA2TluVKOUlWg_Fwwhc2mQvOXqDCXxYYMO3ALVoYY26xBBf_eFEIGecNeUVgGhl0m2DoTBVhhKYcouZ1l93yuHua3YgRl_NCl6oZ1gTtKBbRSXkqJj5AxkcSXQRYB23E/w400-h309/what-is-lightning-network.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiGCZjRSHcBJIvwQlN-RqVxBLyi5wDDi9WjjQpFVM9vIswdHeBV8l51cFbPDZihA2TluVKOUlWg_Fwwhc2mQvOXqDCXxYYMO3ALVoYY26xBBf_eFEIGecNeUVgGhl0m2DoTBVhhKYcouZ1l93yuHua3YgRl_NCl6oZ1gTtKBbRSXkqJj5AxkcSXQRYB23E/s671/what-is-lightning-network.png)

In questo articolo farò un breve riepilogo sull'utilizzo di **Bitcoin** e due alternative (off chain) basate sulla privacy. Oltre a Bitcoin, abbiamo due soluzioni che ne tracciano il prezzo ma presentano vantaggi e svantaggi: Lightning Network (Layer2) e eCash (che è un fork di Bitcoin Cash, **[a sua volta fork di Bitcoin](https://darkwhite666.blogspot.com/2017/08/lhard-fork-della-blockchain-genera-il.html)**). Non mi dilungherò su Bitcoin in quanto il funzionamento è noto ma mi soffermerò principalmente sulle due soluzioni alternative (per micropagamenti) che utilizzano rispettivamente Satoshi e Wrapped Satoshi (unità di misura minima di Bitcoin).

BITCOIN

Come saprai, **[Bitcoin](https://bitcoin.org/it/)** utilizza una rete decentralizzata di nodi che valida le transazioni tramite un meccanismo di consenso (Proof of Work). Vengono risolti degli algoritmi mediante potenza energetica che permettono di validare transazioni. Una volta che una transazione è registrata sulla blockchain, è praticamente impossibile modificarla, garantendo l'integrità dei dati. Bitcoin utilizza algoritmi crittografici per proteggere le chiavi private e le transazioni. Le transazioni sono pubbliche e visibili sulla blockchain, il che significa che chiunque può tracciare i movimenti di Bitcoin conoscendo un indirizzo. Gli indirizzi Bitcoin non sono direttamente legati all'identità degli utenti, ma è possibile correlare gli indirizzi tramite analisi delle transazioni e delle interazioni.

LIGHTNING NETWORK (LAYER2)

**[Lightning](https://lightning.network/)** è un protocollo Layer2 costruito su Bitcoin, che consente transazioni più veloci e con costi inferiori (è più scalabile). Funzionando off chain (al di fuori della blockchain di Bitcoin) è meno sicuro ed enormemente meno decentralizzato. Sostanzialmente utilizza smart contract per gestire i vari canali di pagamento, garantendo il funzionamento. Le transazioni effettuate sulla rete Lightning non sono visibili sulla blockchain di Bitcoin, aumentando la privacy. Le transazioni tra gli utenti all'interno di un canale Lightning non sono pubbliche, il che significa che sono più difficili da tracciare. I canali di Lightning Network permettono di fare transazioni veloci e a basso costo al di fuori della blockchain di Bitcoin.  Due utenti decidono di aprire un canale di pagamento. Per farlo, inviano una certa quantità di Bitcoin a un "indirizzo multisig" sulla blockchain di Bitcoin, che richiede la firma di entrambi per usare i fondi. Questa operazione viene registrata sulla blockchain. Una volta aperto il canale, i 2 utenti possono inviare Satoshi tra loro senza registrare ogni singola transazione sulla blockchain principale. Possono fare centinaia o migliaia di microtransazioni scambiandosi le informazioni sui saldi in modo istantaneo e privato. Ogni volta che X invia Bitcoin a Y o viceversa, aggiornano il "bilancio" del canale. Solo loro due sanno esattamente come si è evoluto il bilancio nel canale. Finché il canale rimane aperto, le transazioni avvengono solo tra loro, senza costi elevati o attese.

Quando i 2 utenti decidono di chiudere il canale, l'ultimo saldo aggiornato viene registrato sulla blockchain di Bitcoin. Questo garantisce che entrambi ricevano l'importo corretto dei fondi, basato sulle transazioni avvenute nel canale. Tramite soluzioni custodial tipo Wallet Of Satoshi è possibile usare il network senza dover aprire i canali. Se vuoi approfondire: [**Come Funziona Lightning Network: Basse Fee e Privacy**](https://darkwhite666.blogspot.com/2022/10/come-funziona-lightning-network-basse.html)

ECASH (BITCOIN CASH HARD FORK)

Prima di interrompere la lettura (Bitcoin Cash non è molto amato alla community), va detto che **[eCash](https://e.cash/)** è abbastanza decentralizzato ed è progettato per offrire maggiore privacy rispetto a Bitcoin. Si tratta di un fork di Bitcoin Cash (che presenta blocchi più grandi di Bitcoin quindi è più scalabile ma più centralizzato e meno sicuro). eCash utilizza tecnologie come le firme a scadenza (blind signatures) e altre tecniche per nascondere l'importo e gli indirizzi delle transazioni. Permette transazioni anonime, il che significa che le identità degli utenti non sono facilmente rintracciabili. Gli utenti possono creare e firmare transazioni eCash offline, utilizzando dispositivi che non sono connessi a Internet. Una volta che una transazione è stata firmata, può essere trasferita fisicamente (ad esempio, tramite un dispositivo USB) a un altro utente o caricata su un dispositivo connesso a Internet per la trasmissione alla rete. eCash utilizza tecniche avanzate di crittografia, come le firme in scadenza, per garantire che le transazioni possano essere validate anche in assenza di una connessione continua alla rete. Dopo che le transazioni offline sono state completate, possono essere sincronizzate con la blockchain una volta che i dispositivi sono connessi a Internet. 1 XEC ha un valore di 100 satoshi (mentre 1 BTC è suddiviso in 100 milioni di satoshi).

Pubblicato da
[DarkDave.|.666](https://www.blogger.com/profile/02696807736631988356 "author profile")

alle
[21:13](https://darkwhite666.blogspot.com/2025/01/due-soluzioni-per-micropagamenti.html "permanent link")

[![](//img1.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/1856644955194422917/7211194889388706099 "Post per email")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=1856644955194422917&postID=7211194889388706099&from=pencil "Modifica post")

[Invia tramite email](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=7211194889388706099&target=email "Invia tramite email")[Postalo sul blog](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=7211194889388706099&target=blog "Postalo sul blog")[Condividi su X](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=7211194889388706099&target=twitter "Condividi su X")[Condividi su Facebook](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=7211194889388706099&target=facebook "Condividi su Facebook")[Condividi su Pinterest](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=7211194889388706099&target=pinterest "Condividi su Pinterest")

Etichette:
[Bitcoin](https://darkwhite666.blogspot.com/search/label/Bitcoin),
[Lightning Network](https://darkwhite666.blogspot.com/search/label/Lightning%20Network),
[Pagamenti](https://darkwhite666.blogspot.com/search/label/Pagamenti)

#### Nessun commento:

#### Posta un commento

[Post più recente](https://darkwhite666.blogspot.com/2025/01/il-segreto-del-successo-di.html "Post più recente")

[Post più vecchio](https://darkwhite666.blogspot.com/2025/01/come-funziona-fx-protocol-fxn-feth-xeth.html "Post più vecchio")
[Home page](...