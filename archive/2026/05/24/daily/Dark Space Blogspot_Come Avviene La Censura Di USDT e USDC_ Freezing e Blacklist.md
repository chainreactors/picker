---
title: Come Avviene La Censura Di USDT e USDC? Freezing e Blacklist
url: http://darkwhite666.blogspot.com/2026/05/come-avviene-la-censura-di-usdt-e-usdc.html
source: Dark Space Blogspot
date: 2026-05-24
fetch_date: 2026-05-25T06:23:03.972329
---

# Come Avviene La Censura Di USDT e USDC? Freezing e Blacklist

## Visualizzazioni Totali

[![Dark Space Blogspot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZgt0RUZjHgbkLsu7CbFNAiyAMd0qvDL2fubvcBv5c6R04keICe8K0ig6oXxzqa6519xC3S7eBHP3_F60rvo_NqafkHR83xyZwscmsQgwCw_EPQpiDWkgarGw08kUDwteX-zWL_I_uP1w/s1600/ask-fm.png)](https://darkwhite666.blogspot.com/)

TRA I PRIMI IN ITALIA A PARLARE DI BITCOIN (DAL 2012!): PER ESSERE SEMPRE AGGIORNATI SULLE NOVITA' TECNOLOGICHE DEL WEB SEGUITE LA PAGINA FACEBOOK (LINK A SINISTRA)

## domenica 24 maggio 2026

### Come Avviene La Censura Di USDT e USDC? Freezing e Blacklist

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhaFCgwKmZDF-UnFrQqF9RV4oLXCmk6cKVeCP_BvbjOq9bIUslS0myDwCq1QsCb1yUqVPWCs7BHxYqPgCeFZsvKoc3I391iHyLaFLIwsgGv2HfjHPV_EUb9ZTmZz0aMVRk2tbB4m-m8SQtPhb2dPsJkZEjR5luoQieJDdOESl0afwaj1mBnNsrPWGx5r48/w400-h174/Censura%20Circle%20Tether.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhaFCgwKmZDF-UnFrQqF9RV4oLXCmk6cKVeCP_BvbjOq9bIUslS0myDwCq1QsCb1yUqVPWCs7BHxYqPgCeFZsvKoc3I391iHyLaFLIwsgGv2HfjHPV_EUb9ZTmZz0aMVRk2tbB4m-m8SQtPhb2dPsJkZEjR5luoQieJDdOESl0afwaj1mBnNsrPWGx5r48/s613/Censura%20Circle%20Tether.jpg)

Le **stablecoin** grazie al Genius Act stanno acquisendo sempre più popolarità. Ci sono infiniti tipi di stablecoin: quelle centralizzate coperte 1:1 (o quasi) dal dollaro americano (ad esempio USDT e USDC), quelle sovracollateralizzate (tipo Dai, coperta da BTC, ETH, USDC e altri asset. Sostanzialmente viene creata depositando collaterale), altre algoritmiche (il caso più noto fu UST), altre che funzionano con il rebase mintando e burnando supply incentivando vendite/acquisti (AMPL), altre con yield incorporato (mBASIS, USDR, etc). Quelle completamente virtuali e decentralizzate, rischi dei protocolli a parte (hack ad esempio), rimangono non censurabili dalle piattaforme che le emettono. Invece quelle centralizzate (USDT e USDC) possono essere facilmente censurate dalle società che le emettono (rispettivamente Tether Foundation e Circle). Circle è più attiva nella censura: blocca immediatamente indirizzi collegati a liste OFAC. Tether in passato era leggermente meno centralizzata e ha applicato congelamenti in modo più selettivo, ma dal 2022 ha iniziato ad adeguarsi in maniera più sistematica freezando grossi quantitativi tra 2024 e 2025 (oltre 2 miliardi di USDT). Dove Tether ha pieno controllo è su Tron e Ethereum mainnet, invece Circle su Ethereum e Polygon.

E' credenza comune che la censura avvenga solo spostando questi asset sugli exchange. In realtà non è così.

QUANDO AVVIENE LA CENSURA?
Le stablecoin centralizzate, cioè emesse e gestite da società che hanno il controllo diretto sui contratti intelligenti che regolano i token, hanno la possibilità di “censurare” indirizzi o fondi quando richiesto da autorità o per motivi di compliance (AML, hack, indagini su frodi). Chiaramente si deve trattare di motivi validi e gravi, ad oggi è impensabile la censura dei fondi per debiti con autorità fiscali o debiti tra privati.

TECNICHE DI CENSURA: FUNZIONI NELLO SMART CONTRACT
Non è necessario che questi fondi passino su exchange (come deve avvenire per BTC) nè son i validatori chiamati a censurare (anche se vedremo che comunque sono loro a confermare la censura). Il potere di censura è integrato a livello di smart contract. Semplicemente sono funzioni incorporate che impediscono swap e trasferimenti sulle chains che utilizzano il formato nativo "ufficiale" (alcune forme wrapped di USDC e USDT sono più difficilmente censurabili).

-Blacklist: Sia Tether che Circle hanno il pieno controllo amministrativo sui contratti ERC-20 (e altre chain con formato nativo ufficiale) di USDT/USDC. Questo controllo avviene tramite una chiave di amministratore controllata dalla società stessa.
Nei contratti USDC e USDT esiste una funzione blacklist(address) che impedisce il trasferimento dei token che possiede (restano bloccati e inutilizzabili).

-Freeze / Confiscation: Circle (USDC) ha anche la funzione wipeFrozenAddress(), che consente di azzerare il saldo di un indirizzo bloccato e spostare i fondi su un altro indirizzo (spesso sotto controllo dell’emittente). Il contratto USDT include funzioni come destroy blacklist funds che, una volta applicate, possono azzerare il saldo degli indirizzi bloccati. Tether può “congelare” USDT in un wallet impedendo qualsiasi movimento in uscita.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgx_fFqG2qFn_6i0bgK7xYh8GRGO1a5Hi1RAOv8TVZhzxgX-JuWvwk-yzlNEa8CXX1QSvYBMTJqyAdkFKNpxrpHEnDg7ZErVhWxqXxHDAFS6rfhnMBmEFUPJBb6T3susq6kaQBprwcZKq8CLPmGZI7ctlDthKDs1mAmNShwSIwVV0dK585d28D-PEjGQBY/w640-h154/Blacklist.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgx_fFqG2qFn_6i0bgK7xYh8GRGO1a5Hi1RAOv8TVZhzxgX-JuWvwk-yzlNEa8CXX1QSvYBMTJqyAdkFKNpxrpHEnDg7ZErVhWxqXxHDAFS6rfhnMBmEFUPJBb6T3susq6kaQBprwcZKq8CLPmGZI7ctlDthKDs1mAmNShwSIwVV0dK585d28D-PEjGQBY/s756/Blacklist.jpg)

TEMPI DI CENSURA
Quando viene identificato un indirizzo sanzionato, il freeze (blacklist) di Circle avviene praticamente in tempo reale (nell’ordine di pochi minuti / un blocco Ethereum) perché la chiamata alla funzione blacklist(address) è immediata una volta autorizzata.
Tether storicamente è meno veloce a congelare ed esiste una “finestra di rischio” tra la decisione di bloccare un wallet e l’esecuzione tecnica della funzione freeze e destroy blacklist funds. In alcuni casi documentati, questa finestra ha permesso a indirizzi malevoli di spostare/vendere USDT prima che il congelamento fosse operativo. Quindi il ritardo può variare da alcune ore a giorni, a seconda di collaborazioni con autorità e pratiche burocratiche.

VALIDATORI POSSONO CENSURARE LE RICHIESTE?
Come detto, Circle e Tether hanno una chiave di amministratore sul contratto Erc20. Quando devono congelare un wallet, eseguono una transazione che chiama funzioni come:

blacklist(address) (USDC)
freeze(address) o freezeAccount(address) (USDT)

Questa transazione è uguale a qualsiasi altra transazione on chain: viene inviata alla mempool e i validatori la includono in un blocco. I validatori non hanno un ruolo attivo nel decidere se quella transazione sia legittima o meno (importante è che rispetti le regole del protocollo). Se un contratto permette a un certo account (Tether) di chiamare una funzione, i validatori eseguono il bytecode e aggiornano lo stato. Importante è che la transazione sia valida (nonce, firma, gas, etc). In teoria, un validatore potrebbe rifiutarsi di includere quella transazione (censura) ma, a causa della decentralizzazione, sarebbe convalidata da un altro validatore. Unico modo sarebbe una censura coordinata (tipo OFAC/MEV-boost) come il tentativo nel 2023 di alcuni relayer MEV di escludere tx da indirizzi sanzionati (Tornado Cash) ma si trattava di una policy volontaria solo di alcuni. E' quasi impossibile mettere d'accordo tutti: se qualcuno non include quella transazione nel successivo blocco, ci penserà qualcun altro. Quando avviene un hack, il più grande errore che si può commettere è bridgiare fondi su Ethereum swappando in USDT o USDC.

Pubblicato da
[DarkDave.|.666](https://www.blogger.com/profile/02696807736631988356 "author profile")

alle
[14:57](https://darkwhite666.blogspot.com/2026/05/come-avviene-la-censura-di-usdt-e-usdc.html "permanent link")

[![](//img1.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/1856644955194422917/803610262895097902 "Post per email")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=1856644955194422917&postID=803610262895097902&from=pencil "Modifica post")

[Invia tramite email](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=803610262895097902&target=email "Invia tramite email")[Postalo sul blog](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=803610262895097902&target=blog "Postalo sul blog")[Condividi su X](https://www.blogger.com/share-post.g?blogID=18566449551944...