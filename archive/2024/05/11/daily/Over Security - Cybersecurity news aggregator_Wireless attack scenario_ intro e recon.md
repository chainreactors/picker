---
title: Wireless attack scenario: intro e recon
url: https://roccosicilia.com/2024/05/10/wireless-attack-scenario-intro-e-recon/
source: Over Security - Cybersecurity news aggregator
date: 2024-05-11
fetch_date: 2025-10-06T17:18:29.014320
---

# Wireless attack scenario: intro e recon

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/progetto-di-divulgazione/)
* [Sostieni il progetto](https://roccosicilia.com/sostieni-il-progetto/)
* [English version](https://medium.com/%40roccosicilia)

[cyber security](https://roccosicilia.com/category/cyber-security/), [hacking](https://roccosicilia.com/category/hacking/), [ita](https://roccosicilia.com/category/ita/)

## [Wireless attack scenario: intro e recon](https://roccosicilia.com/2024/05/10/wireless-attack-scenario-intro-e-recon/)

Published by

Rocco Sicilia

on

[10 Maggio 2024](https://roccosicilia.com/2024/05/10/wireless-attack-scenario-intro-e-recon/)

## Premessa

Questo post apre una mini-serie di cui devo prima precisare alcuni elementi di contesto. Per diverse ragioni chi esegue solitamente attacchi alle reti Wireless (in contesti autorizzati come un Network Penetration Test) usa strumenti che sono delle pietre miliari del mondo della sicurezza WiFi ed integra questi strumenti tra loro. Provo a raccontare alcune scelte abbastanza comuni tra i PenTester.

Solitamente si usano delle linux-box con tools come aircrack-ng e diverse utility di sniffing a cui si affiancano dei radio device come le mitiche antenne Alpha Network. Per quanto sia utile eseguire ricognizioni a 2.4 e 5 GHz va considerato che, in contesti reali, è enormemente più facile lavorare a 2.4 GHz in quanto tale frequenza è largamente utilizzata, consente di lavorare a distanze maggiori rispetto ai sistemi a 5 GHz e soffre molto meno della presenza di ostacoli solidi come muri o altre strutture.
Strumenti molto comodi come le WiFi Pineapple sono impiegate meno su campo in quanto, pur integrando molte delle funzionalità utili in questi contesti, presentano inevitabili limiti dati dalle scelte del produttore. Personalmente ne faccio uso solo in alcuni specifici casi, più frequentemente utilizzo attrezzature standard che mi consentono un grado di personalizzazione molto alto.

In questa mini-serie metterò un po’ tutto insieme per vedere anche le differenze tra un approcciò classico rispetto all’utilizzo di strumenti pre-fatti. Precisazione: non ho nulla contro gli strumenti pre-fatti, ritengo semplicemente che partire da questi non consenta di comprendere con sufficiente chiarezza le azioni che si stanno eseguendo e si rischia di cadere nel modello script kiddies (IMHO).

Ultima nota per completare il disclaimer: il contenuto della mini-serie ha scopo puramente divulgativo e di studio e le tecniche discusse devono essere eseguire in un contesto di lavoratorio o per attività concordate di penetration testing.

## Contesto

Partiamo dal contesto di lavoro. I test sulla sicurezza delle reti wireless sono utili per individuare principalmente due cose: eventuali misconfiguration o scelte “deboli” nella configurazione dell’infrastruttura di accesso wireless, eventuali comportamenti poco attenti da parte degli utenti. Questi due temi hanno pari valenza, considerarne solo uno dei due è tecnicamente un errore in quanto il Threat Actor non si farà particolari problemi in fase di attacco.

I test richiedono ovviamente una presenza fisica nei pressi delle strutture del target. Per quanto sia teoricamente possibile accedere fisicamente alle strutture di di una percentuale significativa di enti e aziende (tema che discutiamo spesso con diversi colleghi) è molto probabile che le attività vengano condotte dall’esterno degli edifici, sopratutto se si vuole condurre un test realistico che simuli il più probabile comportamento di un attacker. Un’attività eseguita da una posizione interna può avere comunque senso, da considerare in questo caso l’enorme vantaggio dato dalla vicinanza fisica ai dispositivi.

L’obiettivo più ovvio è quello di trovare il modo di accedere alla rete target ma questo obiettivo transita da attività che consentono di accedere ad informazioni fondamentali ed utilizzabili in molti modi diversi, non necessariamente limitate al contesto del test sulla rete wireless. Solitamente si definiscono dei path in modo da condurre le attività di test in una sequenza specifica così da avere la possibilità di valutare il percorso migliore in virtù dell’esito delle singole fasi. Si parte indubbiamente da attività di ricognizione per comprendere con che tipo di struttura si ha a che fare per poi selezionare gli attacchi che plausibilmente si possono tentare.

## Ricognizione

Procediamo con ordine. Come per altri contesti di Penetration Testing partiamo con l’analisi del target che, in questo caso, deve anche essere fisica. Se volgiamo valutare la realistica possibilità che un Threat Actor agisca dall’esterno dobbiamo necessariamente considerare l’ambiente circostante: è ovvio che in caso di assenza di segnale dalle zone esterne alla struttura le possibilità si riducono enormemente.

Facciamo un esempio assurdo: supponiamo di avere come target la Grande Piramide di Giza (che si trova vicino al Pineapple Garden, per dire) ipotizzando che all’interno ci siano struttura servite da accessi wireless. Come approcciamo la ricognizione?

![](https://roccosicilia.com/wp-content/uploads/2024/05/image.png?w=1024)

Grande Piramide di Giza, a sinistra di vede un angolo del Pineapple Garden.

Per quanto un target sia isolato, solitamente è costeggiato da alcune strada che, in buona parte del pianeta, sono mappate su sito come Google Maps e Google Earth. Anche in questo caso abbiamo la possibilità di accertare la presenza di una strada a sud ed una ad ovest del target. Vi sono anche due aree di sosta: una vicino all’angolo sud-ovest e l’altra a nord. Da una verifica tramite Street View l’area a nord sembra più facile da raggiungere in auto; potrebbe essere un buon punto per una sopralluogo.

Supponendo di posizionarci nel punto più distante dalla struttura all’interno dell’area di sosta nord ci troveremmo a circa 140m di distanza in linea d’aria d’ingresso della struttura, senza ostacoli nel mezzo.

![](https://roccosicilia.com/wp-content/uploads/2024/05/screenshot-2024-05-07-at-16.45.52.png?w=1024)

Misurazione distanza area sosta / ingresso

Nel mondo wireless la distanza dalla fonte è un elemento di attenuazione del segnale che, sotto una certa soglia, diventa praticamente inutilizzabile. A questa distanza le tecnologie 5 GHz sono usabili solo con device outdoor e siamo oltre il limite anche per buona parte delle tecnologie 2.4 GHz. Per ottenere dei risultati dovremmo probabilmente dimezzare la distanza e sperare nella presenza di fonti che utilizzano 802.11g o 802.11n, mentre per l’ampiezza di banda in questo caso ci si fa andar bene tutto.

Non è da escludere una passeggiata tattica attorno al target con uno strumento di scansione attivo (da infilare nello zaino) e che possiamo controllare dal nostro smartphone o da un tablet. Su questo tema molto pratico ragioniamo assieme con degli esempi fissando dei punti molto precisi:

* Dobbiamo accertarci dei dispositivi potenzialmente attaccabili del target per ovvie ragioni, **sarebbe inopportuno uscire dal perimetro di ingaggio** coinvolgendo sistemi che non fanno parte dell’infrastruttura target.
* Se siamo in un contesto di assessment possiamo anche girare per la struttura con il notebook in mano e l’antenna in testa, se stiamo simulando un attacco reale ci serve qualcosa di un’attimo più camuffato. Per chi preferisce gli strumenti custom potrebbe andare bene un raspberry con un wireless adapter utile ad attività di scansione 802.11 (monitor mode), per chi ha esigenze non particolarmente complesse potrebbe tornare utile la famosa WiFi Pineapple.
* L’output deve comprendere l’elenco degli AP disponibili con le relative caratteristiche di segnale e gli eventuali client associati.

## Scansione

Partiamo dal dispositivo che ci permetterà di eseguire le scansioni partendo dallo scenario custom: una linux-box su un hardware di ridotte dimens...