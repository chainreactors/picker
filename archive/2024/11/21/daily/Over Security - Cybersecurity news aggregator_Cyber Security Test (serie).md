---
title: Cyber Security Test (serie)
url: https://roccosicilia.com/2024/11/20/cyber-security-test-serie/
source: Over Security - Cybersecurity news aggregator
date: 2024-11-21
fetch_date: 2025-10-06T19:18:49.196921
---

# Cyber Security Test (serie)

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/progetto-di-divulgazione/)
* [Sostieni il progetto](https://roccosicilia.com/sostieni-il-progetto/)
* [English version](https://medium.com/%40roccosicilia)

[cyber security](https://roccosicilia.com/category/cyber-security/), [ita](https://roccosicilia.com/category/ita/), [study with me](https://roccosicilia.com/category/study-with-me/)

## [Cyber Security Test (serie)](https://roccosicilia.com/2024/11/20/cyber-security-test-serie/)

Published by

Rocco Sicilia

on

[20 novembre 2024](https://roccosicilia.com/2024/11/20/cyber-security-test-serie/)

[![Cyber Security Test (serie)](https://roccosicilia.com/wp-content/uploads/2025/01/cybersecurity-test-serie.png?w=595)](https://roccosicilia.com/2024/11/20/cyber-security-test-serie/)

E’ un po’ che ragiono su una mia esigenza personale/professionale di fare ordine tra le tecniche, gli strumenti e gli approfondimenti tecnici che gravitano attorno alle attività di testing della postura di sicurezza di un target (notare l’abilità nell’evitare di usare le etichette classiche).

Ho chiuso un paio di task abbastanza grossi che mi hanno tenuto impegnato mentalmente per diversi mesi e credo sia arrivato il momento di lavorare a questa riorganizzazione che, a mio modo di vedere, dovrebbe aiutarmi molto anche nell’efficienza operativa e dovrebbe migliorare la qualità del lavoro che svolgo. In questo caso lavoro e ricerca si fondono parecchio: è una di quelle occasioni in cui posso fare una cosa che mi stimola molto (la parte di ricerca pura) assieme ad attività che hanno una finalità operativa, sempre divertenti per quanto mi riguarda visto che questo lavoro me lo sono scelto io, ma solitamente più vincolate a logiche di business. Mescolare per me è sempre piacevole.

Vorrei essere molto pragmatico, cosa che probabilmente mi allontanerà parecchio dal modello che spesso vedo nei corsi di settore, a volte troppo tool-oriented altre volte troppo CTF-oriented. Ho bisogno di un bagno di realtà, con contesti veri e strumenti realisticamente adottabili. Non che sia l’unica via per mettere ordine in questo campo, ma è quello di cui credo di aver bisogno e forse, visti gli argomenti che tratto con le organizzazioni ed i vari addetti ai lavori, credo sia un modello da perseguire in generale (IMHO).

Visto che il confronto resta uno strumento insostituibile vorrei seguire questo progetto condividendo riflessioni, documenti e tutto quello che mi verrà in mente di condividere usando tutti gli strumenti di cui dispongo: [live](https://twitch.tv/roccosicilia) stream (che riprenderanno), [video](https://youtube.com/%40roccosicilia), [blog post](https://roccosicilia.com), [approfondimenti](https://patreon.com/roccosicilia), ecc.

## Argomenti

Provo a mettere giù prima carrellata dei temi. Vorrei mantenere, come guida, la cronologia di un security test “classico” deviando sui vari punti di approfondimento che spesso non appartengono agli scenari più tipici. È una prima traccia.

Vorrei dedicare uno spazio introduttivo all’argomento in sé, sul perché hanno senso i security test e come devono essere condotti a livello di metodologia. È incredibile ma c’è ancora un cultura estremamente limitata sul tema e molte organizzazione commissionano test un po’ a caso e c’è da dire che sul mercato non tutti gli operatori sono altrettanto qualificati. Non mi riferisco ad un tema di certificazioni ma più ad una questione di mindset ed esperienza. Non sono rari team anche preparati dal punto di vista tecnico ma che poi non riescono a portare dei veri outcome a chi ha chiesto (e pagato) il security test.

Gli argomenti tecnici sono più definibile come titoli. L’ambito information gathering vorrei allargarlo ai temi OSInt e parallelizzare con l’affascinante mondo della threat intelligence. I temi sono diversi per obiettivi ma in più punti si toccano come tecniche. Espanderei l’argomenti alle tematiche di sicurezza degli accessi fisici.

In relazione alle attività su campo vorrei ragionare all’interno di un contesto realistico: di solito i temi tecnici vengono immediatamente separati e trattati singolarmente, vorrei ragionare diversamente nel mio modello operativo e definire degli step base che vadano a richiamare degli approfondimenti. È quindi necessario passare da una fase di enumeration del target in cui si trovano device di ogni tipo e connessi in vari modi. Ha quindi senso parlare di mappatura della rete e design logico oltre che dei singoli oggetti che vengono individuati. Per le varie tipologie di oggetti è giusto definire della attività specifiche di analisi ed eventuale exploiting.

Un’attività che vorrei esercitare è la documentazione delle potenziali vulnerabilità nel contesto operativo: vorrei ottenere una mappa ricca di elementi e dettagli per rendermi meglio conto di eventuali attack path da prendere in considerazione. In questa fase operativa ha senso approfondire e migliorare tutto ciò che riguarda la documentazione delle vulnerabilità note e l’eventuale ricerca di informazioni ad essere legate come le reali possibilità di exploiting e cosa si otterrebbe nel contesto analizzato.

Sull’azione di exploiting terrei il modello che tutt’ora utilizzo: primo accesso ed eventuale escalation. Anche in questo caso le tecniche vanno declinate in relazione alla tipologia di device e solitamente si ha una certa esperienza per il mondo web, i servizi base e le tecniche di escalation in ambito unix/linux e windows. Su questo fronte è senso espandere il modello e parlare anche di network device, dispositivi IoT e OT e altri sistemi operativi come il mondo Apple che ho affrontato poco nel tempo ma che non ha senso lasciare in disparte.

Arrivati a questo punto bisognerebbe fare una pausa e parlare di detection ed evasion, argomento su cui c’è una confusione pazzesca su tutti i fronti. Dovrei riuscire a mettere in piedi un lab per fare un po’ di esperimenti e strutturare meglio le azioni sui target in presenza di strumenti di detection. Recentemente sul [canale telegram BitHorn](https://t.me/%2Ba7sF3JQV4bMzY2Nk) c’è stata una discussione in merito e mi è venuta qualche idea da sviluppare su campo.

Dopo aver discussi di come sono fatte le reti, i sistemi e gli strumenti di detection che ci sono in campo, possiamo ragionare anche di lateral movement ed azioni offensive come l’exfiltration di informazioni.

Ecco… ora che ho elencato i temi mi rendo conto che potrei metterci mesi a strutturate tutto, documentarlo e condividerlo. Io comunque non ho particolare fretta.

Vi tengo aggiornati sui vari canali.

### Condividi:

* Fai clic per inviare un link a un amico via e-mail (Si apre in una nuova finestra)
  E-mail
* [Fai clic qui per condividere su LinkedIn (Si apre in una nuova finestra)
  LinkedIn](https://roccosicilia.com/2024/11/20/cyber-security-test-serie/?share=linkedin)
* [Fai clic per condividere su Telegram (Si apre in una nuova finestra)
  Telegram](https://roccosicilia.com/2024/11/20/cyber-security-test-serie/?share=telegram)
* [Fai clic per condividere su WhatsApp (Si apre in una nuova finestra)
  WhatsApp](https://roccosicilia.com/2024/11/20/cyber-security-test-serie/?share=jetpack-whatsapp)

Mi piace Caricamento…

### Lascia un commento [Cancella risposta](/2024/11/20/cyber-security-test-serie/#respond)

Δ

Questo sito utilizza Akismet per ridurre lo spam. [Scopri come vengono elaborati i dati derivati dai commenti](https://akismet.com/privacy/).

←[Precedente: Non trascurare la raccolta delle informazioni: port scan.](https://roccosicilia.com/2024/11/09/non-trascurare-la-raccolta-delle-informazioni-port-scan/)

[Successivo: Cyber Security Test: post introduttivo](https://roccosicilia.com/2024/11/24/cyber-security-test-post-introduttivo/)→

Ciao,

### sono Rocco

![](https://sheliakblog.wordpress.com/wp-content/uploads/2025/04/photo.jpeg?w=389)

… e questo è mio si...