---
title: La matematica dietro la PQC: le funzioni di hash
url: https://www.telsy.com/la-matematica-dietro-la-pqc-le-funzioni-di-hash/
source: Over Security - Cybersecurity news aggregator
date: 2024-05-07
fetch_date: 2025-10-06T17:19:22.910091
---

# La matematica dietro la PQC: le funzioni di hash

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

* [English](https://www.telsy.com/en/the-mathematics-behind-pqc-hash-functions/)
* [Italiano](https://www.telsy.com/la-matematica-dietro-la-pqc-le-funzioni-di-hash/)

[Crittografia](https://www.telsy.com/categoria/crittografia/), [Quantum Security](https://www.telsy.com/categoria/quantum-security/)

# La matematica dietro la PQC: le funzioni di hash

06 Mag 2024

Condividi

## Introduzione

Dopo aver analizzato nel dettaglio gli schemi che basano la propria sicurezza su problemi matematici definiti sui reticoli ([Kyber](https://www.telsy.com/crystals-kyber-incapsulamento-chiave-basato-su-lwe/), [Dilithium](https://www.telsy.com/crystals-dilithium-firma-digitale-basata-su-lwe/), [Falcon](https://www.telsy.com/falcon-firma-digitale-basata-su-ntru/)) e sui codici a correzione di errori ([Classic McEliece](https://www.telsy.com/classic-mceliece-incapsulamento-chiave-basato-sui-codici/)), possiamo focalizzare l’attenzione sulle funzioni di hash, ossia gli oggetti matematici alla base di SPHINCS+, schema di firma digitale selezionato al termine del terzo round della [competizione del NIST](https://www.telsy.com/la-crittografia-post-quantum-pqc-una-soluzione-classica-alla-minaccia-quantistica/) e per il quale l’ente statunitense ha pubblicato nell’agosto 2023 la bozza di standard “FIPS-205: Stateless Hash-Based Digital Signature Standard”. Tale bozza rappresenta l’ultimo passo necessario prima della divulgazione, prevista per la metà del 2024, del documento che avrà valenza di standard federale e che rappresenterà il riferimento seguito dall’intera comunità crittografica internazionale nel processo di implementazione dell’algoritmo.

### Road map

I prossimi tre articoli della presente serie a tema PQC saranno funzionali alla descrizione di SPHINCS+ e delle sue principali componenti. Come prima cosa verranno introdotte le proprietà fondamentali delle funzioni di hash che sono alla base della sicurezza di schemi come SPHINCS+ e analizzeremo le principali caratteristiche delle firme hash-based. Ci focalizzeremo in particolar modo su alcune peculiarità che le differenziano in modo significativo da altri schemi basati su differenti problemi matematici e che le rendono una scelta particolarmente conservativa dal punto di vista della sicurezza.

In seguito all’analisi degli aspetti più generali che accomunano la maggior parte degli algoritmi basati sulle funzioni di hash ci concentreremo specificatamente su SPHINCS+. Data la struttura modulare di questo schema procederemo in modo incrementale, descrivendo i diversi blocchi funzionali che vengono poi combinati in SPHINCS+ e le cui caratteristiche di sicurezza permettono di garantire i livelli di sicurezza richiesti dal NIST anche nei confronti di un attaccante in possesso di un computer quantistico. Verranno in particolare introdotte le One-Time Signatures (OTS) e le Few-Time Signatures (FTS), ponendo l’attenzione sulle limitazioni che ne precludono l’utilizzo nella maggior parte dei contesti applicativi reali; saranno però anche definiti altri oggetti matematici, quali i Merkle hash trees e gli Hypertrees che permettono di combinare ed estendere OTS e FTS così da renderle praticamente utilizzabili. Concluderemo infine con la descrizione della struttura generale di SPHINCS+, seguita da alcuni cenni alle principali parametrizzazioni e alle prestazioni dell’algoritmo.

### Funzioni di hash e proprietà di sicurezza

Prima di evidenziare i principali vantaggi in termini di sicurezza che caratterizzano gli algoritmi hash-based è utile definire che cosa si intende con il termine “funzione di hash crittografica”. Una hash function crittografica è una funzione f\colon \{0,1\}^\* \to \{0,1\}^n in grado di mappare stringhe di lunghezza arbitratria in stringhe di lunghezza fissata soddisfando le seguenti proprietà:

* Collision resistance: un attaccante [[1](#1)] non deve essere in grado di trovare due input x, y tali che f(x) = f(y);
* Pre-image resistance: dato y\in \{0,1\}^n un attaccante non deve essere in grado di trovare x tale che f(x) = y;
* Second pre-image resistance: dati x\_1 e y=f(x\_1), un attaccante non deve essere in grado di trovare x\_2\ne x\_1 tale che f(x\_2)=y.

Le funzioni di hash crittografiche e le costruzioni definite a partire da esse hanno conosciuto un’enorme diffusione e sono presenti all’interno della quasi totalità degli algoritmi e dei protocolli di comunicazione oggi utilizzati. Per tale motivo, le hash functions crittografiche sono diventate oggetto di numerosi studi che hanno permesso di accrescere la fiducia dei ricercatori nella sicurezza di tali primitive.

Gli algoritmi di firma digitale che si basano sulle funzioni di hash vengono giudicati dalla comunità crittografica internazionale la scelta più conservativa dal punto di vista della sicurezza, al pari di quanto succede tra i KEM con Classic McEliece. Tali schemi non rappresentano la miglior scelta in termini di prestazioni o di dimensione di chiavi pubbliche/firme: tuttavia, se paragonate con altri schemi, esse basano la propria sicurezza su un numero limitato di assunzioni ampiamente studiate in ambito crittoanalitico e quindi ritenute estremamente stabili di fronte agli attacchi conosciuti.
Se si considera infatti un generico algoritmo di firma digitale capace di operare su messaggi di lunghezza arbitraria (es. Dilithium o Falcon), si può notare come esso basi la propria sicurezza su due assunzioni:

* L’intrattabilità di un dato problema matematico (per es. il Shortest Vector Problem sui reticoli);
* La sicurezza della funzione di hash crittografica utilizzata all’interno dello schema.

Questo significa che se anche solo una delle due assunzioni venisse meno la sicurezza dello schema verrebbe irremediabilmente compromessa.

Le hash-based signatures come SPHINCS+ basano invece la propria sicurezza solamente sulla seconda condizione: ciò comporta che uno schema di firma digitale hash-based risulterebbe attaccabile solo qualora fosse possibile compromettere la sicurezza della funzione di hash utilizzata al suo interno, ma in tal caso verrebbe anche meno la sicurezza di tutti gli altri schemi che utilizzano la stessa funzione di hash.
In aggiunta a ciò, in alcuni schemi crittografici tra cui SPHINCS+, la sicurezza potrebbe essere garantita anche qualora la hash function utilizzata non fosse collision resistant. Rimane però chiaramente consigliabile l’utilizzo di primitive ritenute sicure e per le quali non sono mai stati pubblicati attacchi: gli schemi recentemente proposti fanno utilizzo di funzioni quali SHA2 e SHAKE (appartenente al...