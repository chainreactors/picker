---
title: Come funziona un Command and Control (C2)
url: https://roccosicilia.com/2026/06/16/come-funziona-un-command-and-control-c2/
source: Over Security
date: 2026-06-16
fetch_date: 2026-06-17T07:03:47.110858
---

# Come funziona un Command and Control (C2)

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/divulgazione/)
* [Progetti](https://roccosicilia.com/progetti/)
* [Conferenze](https://roccosicilia.com/conferenze/)

[cyber security](https://roccosicilia.com/category/cyber-security/), [hacking](https://roccosicilia.com/category/hacking/), [ita](https://roccosicilia.com/category/ita/)

## [Come funziona un Command and Control (C2)](https://roccosicilia.com/2026/06/16/come-funziona-un-command-and-control-c2/)

Published by

Rocco Sicilia

on

[16 Giugno 2026](https://roccosicilia.com/2026/06/16/come-funziona-un-command-and-control-c2/)

[![Come funziona un Command and Control (C2)](https://roccosicilia.com/wp-content/uploads/2025/04/in-questo-post-parlo-di-threat-intelligence-e-threat-hunting.png)](https://roccosicilia.com/2026/06/16/come-funziona-un-command-and-control-c2/)

1. [Introduzione](https://roccosicilia.com/2026/06/16/come-funziona-un-command-and-control-c2/#introduzione)
2. [Funzionamento di base](https://roccosicilia.com/2026/06/16/come-funziona-un-command-and-control-c2/#funzionamento-di-base)
3. [Stageless vs. Staged](https://roccosicilia.com/2026/06/16/come-funziona-un-command-and-control-c2/#stageless-vs-staged)
4. [Canale di comunicazione](https://roccosicilia.com/2026/06/16/come-funziona-un-command-and-control-c2/#canale-di-comunicazione)
5. [Lab si esempio](https://roccosicilia.com/2026/06/16/come-funziona-un-command-and-control-c2/#lab-si-esempio)
6. [Detection](https://roccosicilia.com/2026/06/16/come-funziona-un-command-and-control-c2/#detection)
7. [Conclusione](https://roccosicilia.com/2026/06/16/come-funziona-un-command-and-control-c2/#conclusione)

---

Chi segue il blog o il canale YouTube da un po’ è a conoscenza dei miei obiettivi divulgativi: storicamente ho sempre scritto e parlato dei temi che riguardavano il mio quotidiano ma da qualche mese sto cercando di proporre temi che siano utili a chi ha iniziato da poco il proprio percorso nel mondo dell’info. security. Quindi, come su [Substack](https://roccosicilia.substack.com/subscribe) è apparsa una serie dedicata alle basi, qui appariranno post dedicati a temi un po’ più complessi spiegati al meglio delle mie capacità e senza andare a spaccare il bit. Ovviamente le occasioni di approfondimenti non mancheranno soprattutto se ci sono domande o richieste specifiche.

Sul mio canale YouTube ho pubblicato un video-recap:

## Introduzione

I threat actor hanno sempre avuto bisogno di uno strumento per comunicare con i sistemi compromessi. Anni fa, agli albori dell’internet come oggi la conosciamo, si usavano dei malware che erano in grado di attivare delle backdoor sui sistema delle vittime.

![](https://i0.wp.com/roccosicilia.com/wp-content/uploads/2026/06/image-1.png?resize=405%2C357&ssl=1)

Ci si riferiva a questi software con il termine Trojan Horse, programmi che installavano ed avviavano un servizio in ascolto su una specifica porta della macchina della vittima a cui l’attaccante si poteva poi collegare con un client.

Ovviamente parliamo di un mondo piuttosto diverso da quello attuale: le connessioni domestiche erano prevalentemente di tipo dial-up e il provider assegnava l’indirizzo IP direttamente al modem della workstation. I sistemi erano quindi quasi sempre esposti direttamente alla rete con un IP pubblico raggiungibile, cosa che oggi, nelle connettività domestiche ed aziendali, non faremmo mai a meno che non sia necessario per qualche servizio specifico ma solitamente usiamo design di rete completamente differenti. Ad ogni modo questo consentiva di esporre il servizio della backdoor direttamente in internet e l’attaccante ci si poteva comodamente collegare per prendere possesso del sistema.

Se trovi utili i contenuti che condiviso e vuoi restare aggiornato puoi sostenere il mio progetto di divulgazione [iscrivendoti al mio Substack](https://roccosicilia.substack.com/subscribe). Per gli abbonati metto a disposizione articoli e video di approfondimento.

L’esigenza è rimasta ma le reti sono profondamente cambiate: le workstation non vengono più esposte pubblicamente (più o meno) e anche i più banali router dei provider domestici sono dotati di firewall minimali in grado di operare una qualche gestione/filtro del traffico.

![](https://i0.wp.com/roccosicilia.com/wp-content/uploads/2026/06/image-2.png?resize=1024%2C332&ssl=1)

Shodan, filtro *os:”Windows 10″*

Installare un servizio in ascolto sulla workstation vittima non ha più senso e la tecnica di attacco si è dovuta evolvere. Oggi gli attaccanti utilizzano infrastrutture Command and Control per comunicare con le macchine compromesse senza essere intercettati dai sistemi di detection ed il loro funzionamento è abbastanza complesso e merita di essere analizzato.

Questi strumenti sono molto utilizzati per mantenere una persistenza all’interno della rete target, impartire comandi ed estrarre informazioni. Sono un elemento fondamentale per la riuscita di attacchi informatici sofisticati e, nonostante gli strumenti di difesa di cui disponiamo, riescono a rimanere silenziosamente attivi sui sistemi target per settimane o mesi.

[![](https://i0.wp.com/roccosicilia.com/wp-content/uploads/2026/06/image-3.png?resize=1024%2C630&ssl=1)](https://blog.talosintelligence.com/writing-a-bugsleep-c2-server/)

Uno dei tanti [articoli di approfondimento](https://blog.talosintelligence.com/writing-a-bugsleep-c2-server/) di cui vi consiglio una lettura.

Le infrastruttura C2 sono studiate approfonditamente dai vendor, dai team di ricerca e dai professionisti del settore, qualche contenuto lo trovate anche nel mio blog e sul mio canale YouTube. Comprenderne il funzionamento è fondamentale.

## Funzionamento di base

La meccanica alla base del funzionamento è molto semplice e si basa su un assunto nel design delle reti LAN che ancora regge e che tocchiamo solo in parte in questo post. Una caratteristica di molte reti è la presenza di filtri molto rigidi per il traffico in ingresso e molto meno rigidi per il traffico n uscita. È molto frequente non accettare che sistemi esterni contattino direttamente le workstation o i server della nostra rete (ovviamente), mentre è molto più frequente accettare che i propri sistemi interni contattino servizi esterni con differenti protocolli.

Su base di questa ipotesi il malware che deve “colpire” il sistema target deve fare una cosa semplice: aprire una sessione di comunicazione dalla macchina vittima verso il sistema controllato dall’attaccante e fare in modo che questo canale di comunicazione sia utilizzabile dall’attaccante per impartire comandi locali. Per ottenere questo risultato il malware che si utilizza compie una serie di azioni specifiche: viene attivato un loop in il malware si “sveglia”, contatta il servizio in ascolto sul C2, gli chiede se ci sono task da eseguire, esegue il task (comando locale), invia il risultato e torna a “dormire”.

![](https://i0.wp.com/roccosicilia.com/wp-content/uploads/2026/06/image-4.png?resize=1024%2C388&ssl=1)

Esempio super-semplice e funzionante.

Questo comportamento, che qui ho molto semplificato, è chiamato *beacon* e presenta alcune caratteristiche tecniche molto importanti.

Un elemento su cui ragionare è l’intervallo di *sleep*: ogni quanto deve essere reiterata l’azione? Su questo tema va anche detto che un loop regolare è tecnicamente più facile da intercettare rispetto ad un intervallo irregolare, solitamente si introduce un *jitter* al fine di rendere pseudo-casuale il tempo di sleep. C’è anche da considerare, in caso di traffico http/https, gli elementi caratteristici della richiesta http come lo user-agent ed altri elementi che contribuiscono all’analisi del *fingerprinting* del software che sta eseguendo la richiesta.

Sul *fingerprinting* ho in mente di fare un approfondimento per JA3 e JA4 in relazione alla detection a livello rete/firewall.

Stiamo ovviamente tra...