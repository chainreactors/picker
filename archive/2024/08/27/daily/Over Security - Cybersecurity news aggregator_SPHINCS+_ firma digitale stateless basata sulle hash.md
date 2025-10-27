---
title: SPHINCS+: firma digitale stateless basata sulle hash
url: https://www.telsy.com/sphincs-firma-digitale-stateless-basata-sulle-hash/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-27
fetch_date: 2025-10-06T18:08:06.713532
---

# SPHINCS+: firma digitale stateless basata sulle hash

* Gruppo TIM

[![Telsy](https://www.telsy.com/wp-content/themes/telsy/images/Logo-Telsy-TIM-blu.png)](https://www.telsy.com/)

[Per fare una ricerca scrivi qualcosa e premi "invio"](/?s=)

Chiudi

* [Chi siamo](https://www.telsy.com/chi-siamo/)
* Soluzioni
  + [Vai a Soluzioni](https://www.telsy.com/soluzioni/)
  + [Cyber](https://www.telsy.com/soluzioni/cyber-ita/)
  + [Crypto](https://www.telsy.com/soluzioni/crypto-ita/)
  + [Quantum](https://www.telsy.com/soluzioni/quantum-ita/)
* [Innovazione](https://www.telsy.com/innovazione/)
* [Lavora con noi](https://www.telsy.com/lavora-con-noi/)
* [Blog](https://www.telsy.com/blog/)

* News in evidenza
  + [06 Ott

    Attacchi rivolti a target italiani, notificati nuovi data breach, vulnerabilità sfruttate ITW](https://www.telsy.com/attacchi-rivolti-a-target-italiani-notificati-nuovi-data-breach-vulnerabilita-sfruttate-itw/)
  + [29 Set

    Le nuove minacce cyber realizzate col supporto dell’AI](https://www.telsy.com/le-nuove-minacce-cyber-realizzate-col-supporto-dellai/)

[Attacchi rivolti a target italiani, notificati nuovi data breach, vulnerabilità sfruttate ITW](https://www.telsy.com/attacchi-rivolti-a-target-italiani-notificati-nuovi-data-breach-vulnerabilita-sfruttate-itw/)
[Le nuove minacce cyber realizzate col supporto dell’AI](https://www.telsy.com/le-nuove-minacce-cyber-realizzate-col-supporto-dellai/)
[Vedi tutte](https://www.telsy.com/blog/)

* [English](https://www.telsy.com/en/sphincs-stateless-hash-based-digital-signature/)
* [Italiano](https://www.telsy.com/sphincs-firma-digitale-stateless-basata-sulle-hash/)

[Crittografia](https://www.telsy.com/categoria/crittografia/), [Quantum Security](https://www.telsy.com/categoria/quantum-security/)

# SPHINCS+: firma digitale stateless basata sulle hash

26 Ago 2024

Condividi

## Introduzione

Lo schema Forest Of Random Subset (FORS) rappresenta l’ultimo elemento necessario alla descrizione della struttura completa della firma digitale SPHINCS+, selezionata al termine del terzo round del [processo di standardizzazione](https://www.telsy.com/la-crittografia-post-quantum-pqc-una-soluzione-classica-alla-minaccia-quantistica/) del NIST. L’inclusione di FORS permette di rendere SPHINCS+ uno schema di firma stateless, superando le principali criticità che affliggono altre hash-based signatures come [XMSS](https://www.telsy.com/XMSS-firma-digitale-stateful-basata-sulle-hash/) e LMS. Dopo aver descritto il funzionamento di FORS, verrà presentata la struttura generale di SPHINCS+, sottolineando come la combinazione delle strutture crittografiche introdotte nei precedenti due articoli della presente rubrica dia origine allo schema in corso di standardizzazione da parte del NIST.

## FORS

Tassello conclusivo nella costruzione di SPHINCS+ è quindi costituito dalla firma Forest Of Random Subsets (FORS). Si tratta di una Few Time Signature (FTS), ovvero di uno schema che permette di firmare un numero limitato di messaggi diversi con la stessa chiave privata. All’aumentare delle firme prodotte, la sicurezza dello schema subisce una graduale diminuzione fino ad esaurirsi, ma senza incorrere nella catastrofica ed immediata perdita di sicurezza che si ha quando vengono firmati due o più messaggi utilizzando una one-time signature come [WOTS+](https://www.telsy.com/la-matematica-dietro-la-pqc-le-funzioni-di-hash/).

Di seguito è riportata una descrizione ad alto livello di FORS.

Lo schema è determinato dai parametri k, t=2^a ed n, nell’ottica di firmare stringhe di ka bit. La chiave privata è costituita da k insiemi di t stringhe di lunghezza n bytes, generate a partire da un singolo seme (*seed*) segreto. Per ottenere la chiave pubblica è necessario calcolare i digest, tramite un’opportuna funzione di hash, di ciascuna delle kt stringhe segrete e distribuirli come foglie di k [Merkle Tree](https://www.telsy.com/XMSS-firma-digitale-stateful-basata-sulle-hash/) di altezza a. Si ricorda che un generico nodo appartenente ai k alberi è ottenuto come hash della concatenazione dei suoi figli. Infine, una volta calcolate le k radici degli alberi risultanti, la chiave pubblica è data dall’hash della concatenazione di queste.

A scopo esplicativo, la struttura sotto riportata rappresenta il caso k=3 e t=2^2, in cui sono necessari 3 Merkle Tree di altezza 2. La chiave privata è data da sk\_{0,0},\dots,sk\_{2,3} mentre la chiave pubblica da f\!pk.

![SPHINCS+ firma digitale stateless basata sulle hash_Telsy 1](https://www.telsy.com/wp-content/uploads/SPHINCS-firma-digitale-stateless-basata-sulle-hash_Telsy-1.png)

Dato un messaggio di ka bit, questo viene scomposto in k stringhe l\_0,\dots, l\_{k-1} di a bit, ciascuna interpretata come un intero nell’intervallo [0,t). La firma del messaggio è ottenuta concatenando le k stringhe sk\_{0,l\_0},sk\_{1,l\_1},\dots, sk\_{k,l\_{k-1}}, una per ogni Merkle Tree, e gli authentication path [[1](#1)] per risalire alle radici r\_i e di conseguenza alla chiave pubblica f\!pk. Di seguito sono evidenziati gli authentication path relativi alla firma del messaggio 11\,01\,10 nel caso k=3 e t=2^2.

![SPHINCS+ firma digitale stateless basata sulle hash_Telsy 2](https://www.telsy.com/wp-content/uploads/SPHINCS-firma-digitale-stateless-basata-sulle-hash_Telsy-2.png)

Possiamo ora analizzare più nel dettaglio le caratteristiche che rendono FORS una Few Time Signature e che quindi permettono di firmare più messaggi con la stessa chiave privata mantenendo un elevato livello di sicurezza.

Nella maggior parte delle One Time Signatures ogni volta che viene apposta una firma viene resa pubblica una parte consistente della chiave privata del firmatario: un esempio chiaro in tal senso è la OTS proposta da Lamport [[2](#2)], nella quale viene esposta metà chiave privata, rendendo impossibile il suo riutilizzo sicuro per la firma di un secondo messaggio. Si noti che anche in FORS, ogniqualvolta viene apposta una firma, vengono rivelate alcune parti della chiave privata, ma il leak di informazione è molto più contenuto.

Facendo riferimento allo schema riportato sopra, possiamo notare come una firma comporti la pubblicazione del valore di una sola stringa segreta per ciascuno dei tre Merkle Tree (sk\_{0,3}, sk\_{1,1}, sk\_{2,2} nel caso qui considerato). Se si considera che nelle istanze di FORS di interesse per l’utilizzo all’interno di SPHINCS+ t può assumere valori da 2^6 fino a 2^{14}, appare chiaro che una firma, rivelando solamente una stringa in ciascuno dei k Merkle Tree, non sia sufficiente ad inficiare immediatamente la sicurezza di firme successive prodotte con la medesima chiave privata. Infatti, un attaccante può forgiare una firma di un messaggio, senza la conoscenza della chiave privata, solamente se il suo digest è composto da blocchi di a bit tali da identificare stringhe che sono già state rese pubbliche, ma se è a conoscenza di un numero limitato di firme questo scenario diventa estremamente improbabile. È chiaro, comunque, che man mano che il numero di firme apposte con la stessa chiave aumenta, cresce anche la probabilità che un attaccante riesca a trovare un messaggio per cui gli è possibile forgiare la firma.

La struttura di FORS garantisce anche una maggiore protezione nel caso di “weak messages”, ossia di messaggi in cui molti blocchi del digest risultano uguali e che possono comportare una riduzione della sicurezza in altre note FTS come ad esempio Hash to Obtain Random Subset (HORS), in cui invece di k Merkle Trees di t foglie se ne utilizza uno solo. Inoltre, in FORS vengono adottate altre accortezze quali ad esempio la randomizzazione dell’hash del messaggio. Questo impedisce ad un attaccante di costruire messaggi che permettono di massimizzare il leak di informazione derivante da ciascuna firma.

## SPHINCS+

L’introduzione di FORS permette di superare l’esigenza di tracciabilità delle firme già eseguite, presente ad esempio in XMSS, risultando fondamentale nel design di schemi [*stateless*](https://www.telsy.com/la-matem...