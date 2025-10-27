---
title: I Computer Quantistici Saranno Pericolosi Per Cripto e Banche? Curve Ellittiche
url: http://darkwhite666.blogspot.com/2023/03/i-computer-quantistici-saranno.html
source: Dark Space Blogspot
date: 2023-03-14
fetch_date: 2025-10-04T09:33:01.211841
---

# I Computer Quantistici Saranno Pericolosi Per Cripto e Banche? Curve Ellittiche

## Visualizzazioni Totali

[![Dark Space Blogspot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZgt0RUZjHgbkLsu7CbFNAiyAMd0qvDL2fubvcBv5c6R04keICe8K0ig6oXxzqa6519xC3S7eBHP3_F60rvo_NqafkHR83xyZwscmsQgwCw_EPQpiDWkgarGw08kUDwteX-zWL_I_uP1w/s1600/ask-fm.png)](https://darkwhite666.blogspot.com/)

TRA I PRIMI IN ITALIA A PARLARE DI BITCOIN (DAL 2012!): PER ESSERE SEMPRE AGGIORNATI SULLE NOVITA' TECNOLOGICHE DEL WEB SEGUITE LA PAGINA FACEBOOK (LINK A SINISTRA)

## lunedì 13 marzo 2023

### I Computer Quantistici Saranno Pericolosi Per Cripto e Banche? Curve Ellittiche

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguBa1OF5nAG3L5WPcp5BgYcZoHWi1Lzx1SiPvkShXKVXVHB8DrlFASb-qsv8gOpzPtbtfyx4u5lD2wlmXdv8YqIX6mhoG4FoimlOGky7qBTG_gvVFQLDul6VUt09gzGcQKRiMuJnhIWnb59Z7e3mR86F7b3NRGT2V2Sr0dT6rGxmKuvfdMHhW9j1hi/w400-h238/d41586_021_03476_5_19875844.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguBa1OF5nAG3L5WPcp5BgYcZoHWi1Lzx1SiPvkShXKVXVHB8DrlFASb-qsv8gOpzPtbtfyx4u5lD2wlmXdv8YqIX6mhoG4FoimlOGky7qBTG_gvVFQLDul6VUt09gzGcQKRiMuJnhIWnb59Z7e3mR86F7b3NRGT2V2Sr0dT6rGxmKuvfdMHhW9j1hi/s388/d41586_021_03476_5_19875844.png)

I **[computer quantistici](https://darkwhite666.blogspot.com/2015/09/la-storia-dei-computer-quantistici-d.html)**, a causa della loro architettura e potenzialità, sono in grado di "rompere" la crittografia moderna (chiave pubblica/privata). Va sottolineato però che ad oggi sono ancora molto limitati nelle loro funzionalità (e super costosi per quel poco che riescono a fare). I computer quantistici possono potenzialmente attaccare sistemi bancari, criptovalute e in particolare le curve ellittiche utilizzando un algoritmo chiamato "algoritmo di Shor". Questo algoritmo può essere utilizzato per fattorizzare i numeri primi, che è un passaggio chiave in molti algoritmi di crittografia utilizzati per proteggere i dati, come l'RSA. Le curve ellittiche sono utilizzate in criptovalute come Bitcoin, Ethereum, etc per generare le chiavi private e pubbliche usate per crittografare e decrittografare le transazioni. Se un computer quantistico abbastanza potente fosse in grado di attaccare le curve ellittiche, potrebbe decifrare le chiavi private e compromettere la sicurezza.

CURVE ELLITTICHE SU BITCOIN

Ad esempio Bitcoin utilizza secp256k1 che è una curva ellittica. La crittografia usata da Bitcoin è a chiave pubblica e privata (SHA 256). Il SHA 256 prende dei dati in input e produce output di 256 per creare hash dei blocchi di transazioni ed è usato anche per l'integrità del blocco ed appunto per la generazione di chiavi private e pubbliche.

Il processo di generazione delle chiavi in Bitcoin è il seguente:

1) Viene scelta una curva ellittica appropriata (secp256k1), definita su un campo di numeri primi di 256 bit

2) Viene scelto un numero casuale ("seed") come chiave privata, che viene mantenuto segreto dal proprietario della chiave

3) La chiave pubblica corrispondente viene calcolata moltiplicando la curva ellittica per il seed. Questo calcolo è eseguito in modo tale che solo la chiave privata possa produrre la chiave pubblica corrispondente

La chiave pubblica viene quindi utilizzata per ricevere pagamenti e firmare transazioni attraverso l'algoritmo ECDSA (basato sulle curve ellittiche). Quando viene inviata una transazione, il mittente utilizza la sua chiave privata per generare una firma digitale che dimostra che è effettivamente il proprietario delle chiavi. In seguito la firma viene verificata utilizzando la chiave pubblica del mittente.

Sostanzialmente, per semplificare il tutto, è presente un punto sulla curva ellittica e un numero scalare enorme di 256 bit. I due numeri vengono moltiplicati, ottenendo l'altro punto (R). Un computer odierno non riesce ad attaccare questo sistema, uno quantistico, dato questo punto R riesce a calcolare lo scalare che è la chiave privata di Bitcoin.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg-UTpipMK_WqUdnWZaId03WUeRO3RsNMo-YaEMlJcLMyfNPeIdtfTI8lDUc2t806IzNEc4_n2b8cLejgUiHx-rkzjjU2xCLO4zXCDfRRXEYhIjMxa-tLqYCW26M1tdphMx25v15ZoYQM4qaW0-AwOFoM6ydhR9y8OzH88jlI1Ax9K2lpTET2Z4YVR5/s320/The-group-law-for-an-elliptic-curve-P-Q-R-The-points-P-and-Q-sum-to-the-point-R.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg-UTpipMK_WqUdnWZaId03WUeRO3RsNMo-YaEMlJcLMyfNPeIdtfTI8lDUc2t806IzNEc4_n2b8cLejgUiHx-rkzjjU2xCLO4zXCDfRRXEYhIjMxa-tLqYCW26M1tdphMx25v15ZoYQM4qaW0-AwOFoM6ydhR9y8OzH88jlI1Ax9K2lpTET2Z4YVR5/s800/The-group-law-for-an-elliptic-curve-P-Q-R-The-points-P-and-Q-sum-to-the-point-R.png)

Più precisamente, l'algoritmo di Shor dei computer quantistici può essere utilizzato per fattorizzare rapidamente numeri interi enormi in fattori primi. Algoritmi di crittografia a chiave pubblica, come l'RSA, basano la loro sicurezza sulla difficoltà di fattorizzare grandi numeri interi in fattori primi.

L'algoritmo di Shor utilizza la proprietà quantistica dell'**[entanglement](https://darkwhite666.blogspot.com/2018/03/linternet-del-futuro-network.html)** per eseguire una ricerca efficiente dei fattori primi di un numero intero enormemente grande. Invece di utilizzare la forza bruta per provare ogni possibile fattore (andando a tentativi), come avviene in un algoritmo classico, l'algoritmo di Shor sfrutta la sovrapposizione quantistica e l'interferenza per cercare i fattori in modo esponenzialmente più efficiente.

Ad esempio moltiplicare due numeri primi enormi (P e Q), viene fatto in modo istantaneo da una calcolatrice o da un computer. Tuttavia se al posto di P e Q, il computer ha il risultato R (dato dal prodotto di P e Q), ci vorrebbero milioni di anni per trovare i 2 numeri P e Q. Invece un computer quantistico grazie all'algoritmo di Shor, risolve questo problema in pochi secondi. Un computer quantistico del genere distruggerebbe non solo le cripto o internet tutta ma anche qualsiasi sistema bancario. Qualsiasi chiave privata verrebbe trovata in pochi secondi. Un sistema così fatto romperebbe non solo la fattorizzazione citata prima (numero composto dato da 2 numeri primi) ma anche le curve ellittiche. L'idea sarebbe costruire algoritmi resistenti al quantum computer. Utilizzando le curve ellittiche, la matematica andrebbe completamente cambiata in caso di avvento di quantum computer.

UTILIZZO DI PIU' CURVE ELLITTICHE E RETICOLI MATEMATICI

Ci sono già algoritmi di crittografia resistenti ai computer quantistici in grado di proteggere le criptovalute e le curve ellittiche, come ad esempio la PQC (Post-Quantum Cryptography), che utilizza algoritmi basati su problemi matematici che sono difficili da risolvere anche per un computer quantistico. L'utilizzo di più curve ellittiche può contribuire a rafforzare la sicurezza delle transazioni in Bitcoin. Ciò è possibile attraverso l'utilizzo di un sistema multicurve, in cui vengono utilizzate più curve ellittiche appunto per la generazione di chiavi e firme. Utilizzando diverse curve ellittiche, si riduce il rischio che una curva specifica venga compromessa da un attacco crittografico ed è possibile distribuire il lavoro di generazione delle chiavi e delle firme su più curve, migliorando le prestazioni complessive del sistema. Si avrebbe anche una maggiore flessibilità basata sulle specifiche esigenze di sicurezza e prestazioni del sistema e maggiore interoperabilità del sistema con altri sistemi crittografici basati su curve ellittiche.

Sono stati sviluppati anche algoritmi crittografici basati su problemi matematici che non possono essere risolti efficientemente da un computer quantistico. Ad esempio, un algoritmo PQC alternativo alla crittografia basato su curve ellittiche è quella inerenti reticoli che sfruttano la geometria dei reticoli matematici per la crittografia. Questi algoritmi crittografici si basano sulla difficoltà di trovare il vettore più corto in un reticolo di dimensione elevata, noto come "problema del vettore più corto".

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj...