---
title: XMSS: firma digitale stateful basata sulle hash
url: https://www.telsy.com/xmss-firma-digitale-stateful-basata-sulle-hash/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-02
fetch_date: 2025-10-06T17:49:12.467214
---

# XMSS: firma digitale stateful basata sulle hash

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

* [English](https://www.telsy.com/en/xmss-hash-based-stateful-digital-signature/)
* [Italiano](https://www.telsy.com/xmss-firma-digitale-stateful-basata-sulle-hash/)

[Crittografia](https://www.telsy.com/categoria/crittografia/), [Quantum Security](https://www.telsy.com/categoria/quantum-security/)

# XMSS: firma digitale stateful basata sulle hash

01 Lug 2024

Condividi

## Introduzione

Lo schema XMSS (eXtended Merkle Signature Scheme) rappresenta una componente fondamentale nella [costruzione di SPHINCS+](https://www.telsy.com/la-matematica-dietro-la-pqc-le-funzioni-di-hash/), schema di firma post-quantum basato sulle funzioni di hash e selezionato nel [processo](https://www.telsy.com/la-crittografia-post-quantum-pqc-una-soluzione-classica-alla-minaccia-quantistica/) di standardizzazione del NIST.

Considerato in modo a sé stante, XMSS è esso stesso uno schema di firma utilizzabile in particolari scenari applicativi e standardizzato dal NIST, insieme al simile LMS (Leighton-Micali Signature), nell’ambito delle firme digitali stateful. Nonostante XMSS presenti diverse caratteristiche competitive [[1](#1)] anche nel contesto delle firme post-quantum, la natura stateful lo rende poco appetibile dal punto di vista pratico, in quanto richiede di tenere traccia di tutte le firme prodotte nel tempo con una stessa chiave privata per preservare la sicurezza promessa dallo schema.

Questa limitazione è superata dal suo inserimento all’interno di SPHINCS+.

## XMSS

Elemento caratterizzante nella costruzione della firma XMSS è il coinvolgimento di particolari alberi binari, detti *Merkle trees*. Specificata una funzione di hash \text{H}, ciascun *nodo* del Merkle tree è ottenuto calcolando l’hash dei due nodi al livello inferiore [[2](#2)] (chiamati *figli* del nodo risultante). Di conseguenza, il Merkle tree è interamente determinato dai nodi senza figli, detti *foglie*. Nel caso qui considerato, le foglie sono tutti e soli i nodi al livello più basso. Infine, il nodo in cima all’albero prende il nome di *radice*.

Di seguito, un esempio di Merkle tree con 8 foglie.

![1xmss](https://www.telsy.com/wp-content/uploads/1xmss.png)

Nello schema di firma XMSS, la chiave privata è una stringa di bit, detta *seme*, a partire dal quale sono generate tante coppie di chiavi (ws\_i, wp\_i), relative a firme [WOTS+](https://www.telsy.com/la-matematica-dietro-la-pqc-le-funzioni-di-hash/), quante sono le foglie del Merkle tree. Le foglie dell’albero coincidono con le chiavi pubbliche wp\_i mentre la radice risultante r è la chiave pubblica dello schema XMSS.

La firma XMSS di un messaggio M è composta dalla sua firma WOTS+ tramite una ws\_i opportunamente scelta[[3](#3)] e dal cosiddetto *authentication path*, ovvero l’insieme dei nodi necessari e sufficienti per calcolare, a partire dalla i-esima foglia, la radice dell’albero. Di seguito, è evidenziato in rosso l’authentication path relativo alla terza foglia.

![2xmss](https://www.telsy.com/wp-content/uploads/2xmss.png)

In fase di verifica, il destinatario ricava un candidato per wp\_i a partire dalla ricezione della firma WOTS+. Successivamente, la bontà di wp\_i è accertata grazie all’authentication path, incluso nella firma, e alla radice, chiave pubblica dello schema. In particolare, a partire da wp\_i e dall’authentication path, il destinatario calcola la radice del Merkle tree e verifica essere coincidente con quella nota.

## HyperTrees

Il ricorso ai Merkle trees permette di considerare una chiave pubblica dello schema di dimensioni contenute, in quanto costituita solamente dalla radice dell’albero.

L’utilizzo di Merkle trees per la generazione e la verifica di firme comporta però alcune problematiche, soprattutto nel momento in cui si provano a soddisfare i requisiti stabiliti dal NIST relativamente al numero di firme che si devono poter realizzare con una singola chiave privata. Sarebbe infatti necessario un albero con un numero estremamente elevato di foglie (circa 2^{64}), rendendo impossibili entro tempistiche ragionevoli la costruzione e la trasmissione di un authentication path all’interno della firma digitale.

Per superare tali criticità, è utile introdurre una nuova costruzione denominata HyperTree, ossia un Merkle tree le cui foglie, che si ricorda corrispondere a chiavi pubbliche WOTS+, vengono utilizzate (con la rispettiva chiave privata) per firmare e validare le radici di altri alberi di livello inferiore. Si viene quindi a creare una gerarchia composta da diversi livelli di Merkle trees: ciascuna foglia di un albero intermedio firma la radice di un albero al livello inferiore, mentre le foglie degli alberi al livello più basso vengono utilizzate per firmare i messaggi.

Di seguito è rappresentato un HyperTree composto da tre livelli di alberi [[4](#4)], in cui si può notare come il legame tra un livello e quello inferiore sia realizzato tramite una firma WOTS+.

![hypertree](https://www.telsy.com/wp-content/uploads/hypertree.png)

Il ricorso ad un HyperTree permette quindi di ottenere una struttura con un numero estremamente elevato di foglie (come richiesto nei requisiti esplicitati dal NIST), senza però che questo richieda la gestione di un unico Merkle tree di dimensioni tali da inficiare l’utilizzabilità dell’algoritmo di firma digitale. L’introduzione dei livelli intermedi consente, infatti, di non dover esplorare tutti i rami della costruzione risultante per produrre un authentication path.

Nel caso di uno schema che fa uso di un HyperTree, la firma è composta dalle diverse firme WOTS+ presenti tra i differenti livelli di alberi, unite all’authentication path costituito dagli elementi necessari a ricavare le radici di tutti i Merkle trees fino a quella di livello più alto (rappresentati in nero nell’immagine precedente). La radice dell’albero di livello più alto nell’HyperTree rappresenta la chiave pubblica dello schema.

Nel corso degli ultimi anni sono stati proposti due nuovi algoritmi, denominati XMSSMT e HSS, che sono il risultato dell’applicazione degli HyperTrees all’interno dei già citati XMSS e LMS. Il ricorso ad HyperTrees non è sufficiente però a superare la principale criticità che riguarda XMSS e LMS, ossia la necessità di mantenere uno stato per prevenire la realizzazione di due firme con la stessa chiave privata, che avrebbe conseguenze disastrose sulla sicurezza dello schema. Diventa quindi necessario ricorrere ad algoritmi di firma digitale che permettano di effettuare un numero limitato (ma maggiore di uno) di firme senza avere una degradazione della sicurezza. Tale fa...