---
title: Ethereum è Centralizzato? Infura, AWS e Node Provider
url: http://darkwhite666.blogspot.com/2023/01/ethereum-e-centralizzato-infura-aws-e.html
source: Dark Space Blogspot
date: 2023-01-28
fetch_date: 2025-10-04T05:06:36.461718
---

# Ethereum è Centralizzato? Infura, AWS e Node Provider

## Visualizzazioni Totali

[![Dark Space Blogspot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZgt0RUZjHgbkLsu7CbFNAiyAMd0qvDL2fubvcBv5c6R04keICe8K0ig6oXxzqa6519xC3S7eBHP3_F60rvo_NqafkHR83xyZwscmsQgwCw_EPQpiDWkgarGw08kUDwteX-zWL_I_uP1w/s1600/ask-fm.png)](https://darkwhite666.blogspot.com/)

TRA I PRIMI IN ITALIA A PARLARE DI BITCOIN (DAL 2012!): PER ESSERE SEMPRE AGGIORNATI SULLE NOVITA' TECNOLOGICHE DEL WEB SEGUITE LA PAGINA FACEBOOK (LINK A SINISTRA)

## venerdì 27 gennaio 2023

### Ethereum è Centralizzato? Infura, AWS e Node Provider

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhgME9NTRFJZT_m1MLAEXJoIqKZ24Kff7wdl1ErxPkA7g-6p0RtlLQ6vbiNhdcddJrkwZgfwMspvCNkSJF3cNwPPEYLgSVdo_fLeXBUSyrc3kEnnlVpswb-Gj-Jp1zxZwGhx9QXfjDZGWOYYVLJHjRFinjQepHeXLYdYX6RBhKUU_izoEqvrKkoJEoB/w400-h195/Ethereum%20Archive%20Node.jpeg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhgME9NTRFJZT_m1MLAEXJoIqKZ24Kff7wdl1ErxPkA7g-6p0RtlLQ6vbiNhdcddJrkwZgfwMspvCNkSJF3cNwPPEYLgSVdo_fLeXBUSyrc3kEnnlVpswb-Gj-Jp1zxZwGhx9QXfjDZGWOYYVLJHjRFinjQepHeXLYdYX6RBhKUU_izoEqvrKkoJEoB/s523/Ethereum%20Archive%20Node.jpeg)

Con il Merge (passaggio da Proof Of Work a Proof Of Stake), **Ethereum** è stato criticato per una sua eventuale centralizzazione. Infura è un'infrastruttura utilizzata da molti service provider di Ethereum, tra cui il wallet Metamask, che permette di non avere un proprio full node (sostanzialmente è simile ad Amazon Web Service). Cioè se devi offrire un servizio e non hai risorse, puoi appoggiarti ad Infura. Infura è stato lanciato nel 2016. All'epoca, l'obiettivo alla base del lancio era ridurre l'attrito per gli sviluppatori Web3 rendendo più semplice l'accesso alle reti Ethereum e IPFS. L'API di Infura Ethereum ha supportato più di 430.000 sviluppatori che ora stanno costruendo prodotti che ruotano attorno a giochi blockchain, finanza decentralizzata (DeFi), organizzazioni autonome decentralizzate (DAO) e token non fungibili (NFT). Qual è il problema di tutto questo? Che ti appoggi ad un ente terzo e soprattutto ad un servizio centralizzato (per quanto riguarda l'infrastruttura). Infura, tra l'altro, è americano quindi soggetto ad imposizioni da parte del governo. Ad esempio lo scorso anno, Metamask appoggiandosi ad Infura aveva avuto problemi di censura in alcuni paesi quindi si era urlato allo scandalo in quanto Ethereum appoggiandosi a Metamask quindi ad Infura era stato etichettato centralizzato (Metamask di default utilizza l'end-point di Infura). Sostanzialmente è possibile accedere ad Ethereum collegandosi a qualsiasi full node in modo decentralizzato, tuttavia utilizzando Metamask che di default usa Infura, se quest'ultimo decide di blacklistare indirizzi IP a causa di decisioni dei governi, si attua una censura. In realtà in questi casi basta cambiare URL RPC su Metamask, proprio perchè la censura è infrastrutturale e non dipende dalla blockchain. In realtà va aggiunta una rete manuale (le informazioni da aggiungere sono sempre le classiche della mainnet di Ethereum ovvero Chain ID, Block Explorer e simbolo che trovate anche nello screen di sotto, unica cosa che va modificato è appunto l'URL RPC e volendo il nome della rete dove potete scrivere Ethereum RPC Privacy per distinguerla da quella di default di Infura). Qui trovi una lista di URL RPC: [**Chainlist**](https://chainlist.org/chain/1)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg9mVaFElVIDHs7LZBYD6XuQz9_nOUuMdYP-dxheCVo2GbR5fVE0RoanNdD8MgVKahlYMF2scmtr1c0jqBzisW7rGJYhiLhx3zG-zzRD9XQaPOwIlTm2ePBKSazNPBM91jQxJIFsrctWXpg7fVEdCT-H7pZHRkFnW-nD8Yl4NXXr56DIFx5Fw0jrlrD/w488-h640/Infura.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg9mVaFElVIDHs7LZBYD6XuQz9_nOUuMdYP-dxheCVo2GbR5fVE0RoanNdD8MgVKahlYMF2scmtr1c0jqBzisW7rGJYhiLhx3zG-zzRD9XQaPOwIlTm2ePBKSazNPBM91jQxJIFsrctWXpg7fVEdCT-H7pZHRkFnW-nD8Yl4NXXr56DIFx5Fw0jrlrD/s591/Infura.png)

Infura in futuro proverà a diventare più decentralizzato utilizzando più nodi sparsi nel mondo. Questo fornitore di infrastrutture è appunto controllato da ConsenSys di Joseph Lubin che ha sviluppato anche il wallet Metamask. Oltre a supportare gli sviluppatori su Ethereum, Infura supporta anche altri prodotti web3 come Ethereum Name Service e reti di livello 2. Esso supporta anche un'ampia gamma di API blockchain per realizzare un network multi-chain. Il passaggio ad una maggiore decentralizzazione arriverà nel 2023.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhLf5233r5CEa6Usdzh9X16qEKuvhx4XbU-5mmM9v2MwnNDsZPnuhS28QaVEhbTY2s0yirGbdATSFsb0iAsTPuUlM-dAGTjZ-GELvRPNdpXWp17oM9csHwIjpwNVPExhxIqN7TJP-F5B0TkYYO6U0SEoBduGLRKCgxQsy4VlA8oqf8SCYeXuHAVuHEG/w400-h305/1_9maPQBbLMBcGAsRqb8FvGw.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhLf5233r5CEa6Usdzh9X16qEKuvhx4XbU-5mmM9v2MwnNDsZPnuhS28QaVEhbTY2s0yirGbdATSFsb0iAsTPuUlM-dAGTjZ-GELvRPNdpXWp17oM9csHwIjpwNVPExhxIqN7TJP-F5B0TkYYO6U0SEoBduGLRKCgxQsy4VlA8oqf8SCYeXuHAVuHEG/s658/1_9maPQBbLMBcGAsRqb8FvGw.png)

Ad inizio 2021, quando si parlava ancora di Proof Of Work, più di 6000 (56%) di tutti i nodi Ethereum erano in esecuzione su hosting provider, in particolare 2.500 (36%) su Amazon Web Services (AWS). Il secondo classificato per il maggior numero di nodi Ethereum era residenziale, con un discreto 4.500 (o 38,91%). Il vantaggio di avere il proprio full node, oltre a favorire la decentralizzazione, risiede nel non preoccuparsi che ad esempio AWS possa non funzionare o che qualche altro provider di hosting venga utilizzato per una dapp influendo sulle prestazioni degli utenti. Si può citare Quicknode, Allnodes, Alchemy o lo stesso Infura, il fornitore numero 1 di node-as-a-service, che nel corso della sua storia ha avuto anche altre interruzioni. La maggior parte dei pool/nodi minerari (quando Ethereum veniva minato) sono collegati tra loro, quindi i blocchi continuerebbero a passare, anche se la rete subirebbe rallentamenti (ci sarebbero meno transazioni convalidate). Chi ha un proprio full node non vedrebbe alcuna differenza. In realtà hosting provider come Infura e AWS non hanno solo aspetti negativi ma sono fondamentali per il buon funzionamento della rete. Gestire oltre 800 GB di spazio di archiviazione solo per sincronizzare la chain e quindi aggiungere 1 GB ogni giorno non è pratico per la persona media. Inoltre, non c'è quasi nessun incentivo economico per gestire un nodo, sebbene progetti come vipnode stiano lavorando su questo problema.

Pubblicato da
[DarkDave.|.666](https://www.blogger.com/profile/02696807736631988356 "author profile")

alle
[10:15](https://darkwhite666.blogspot.com/2023/01/ethereum-e-centralizzato-infura-aws-e.html "permanent link")

[![](//img1.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/1856644955194422917/6865349609350570141 "Post per email")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=1856644955194422917&postID=6865349609350570141&from=pencil "Modifica post")

[Invia tramite email](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=6865349609350570141&target=email "Invia tramite email")[Postalo sul blog](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=6865349609350570141&target=blog "Postalo sul blog")[Condividi su X](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=6865349609350570141&target=twitter "Condividi su X")[Condividi su Facebook](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=6865349609350570141&target=facebook "Condividi su Facebook")[Condividi su Pinterest](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=6865349609350570141&target=pinterest "Condividi su Pinterest")

Etichette:
[Amazon Web Service](https://darkwhite666.blogspot.com/search/label/Amazon%20Web%20Service),
[ConsensYs](https://darkwhite666.blogspot.com/search/label/ConsensYs),
[Cripto](https://darkwhite666.blogspot.com/se...