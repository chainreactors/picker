---
title: Stavolta Piracy Shield l'ha fatta grossa e ha bloccato Google Drive
url: https://www.wired.it/article/piracy-shield-blocco-google-drive-download/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-20
fetch_date: 2025-10-06T18:50:55.879733
---

# Stavolta Piracy Shield l'ha fatta grossa e ha bloccato Google Drive

[Skip to main content](#main-content)

Apri il menu di navigazione

Menu

[![Wired Italia](/verso/static/wired-us/assets/logo-header.svg)](/)

Stavolta Piracy Shield l'ha fatta grossa e ha bloccato Google Drive

* [Scienza](/scienza/)
* [Economia](/economia/)
* [Cultura](/cultura/)
* [Gadget](/gadget/)
* [Security](/security/)
* [Diritti](/diritti/)
* [Idee](/idee/)
* [Video](/video/)
* [Podcast](/podcast-wired/)
* [Wired Consiglia](/wired-consiglia/)

More*Chevron*

[Cerca

Cerca](/search/)

* [Scienza](/scienza/)
* [Economia](/economia/)
* [Cultura](/cultura/)
* [Gadget](/gadget/)
* [Security](/security/)
* [Diritti](/diritti/)
* [Idee](/idee/)
* [Video](/video/)
* [Podcast](/podcast-wired/)
* [Wired Consiglia](/wired-consiglia/)

[Raffaele Angius](/author/rangius/) [Luca Zorloni](/author/lzorloni/)

Epic fail

19.10.2024

# Stavolta Piracy Shield l'ha fatta grossa e ha bloccato Google Drive

Un dominio di Big G finisce nel mirino della piattaforma nazionale anti-pirateria, che lo oscura, impedendo i download dei dati da una delle principali piattaforme cloud al mondo

![Il logo di Google](https://media-assets.wired.it/photos/6714232f9f1f9112df5cebe8/16:9/w_2560%2Cc_limit/Cover%2520foto%2520multiple%2520(4).png)

Il logo di GoogleBeata Zawrzel/NurPhoto via Getty Images - modificata con Canva

Stavolta nella rete di **Piracy Shield, la [piattaforma nazionale antipirateria](https://www.wired.it/article/piracy-shield-piattaforma-agcom-pezzotto-streaming-illegale/),** ci è finito un pesce grosso. Grossissimo: **Google**. Nella serata di sabato 19 ottobre un **ticket caricato sul sistema adottato dall’Autorità garante delle comunicazioni** (Agcom) per debellare lo streaming illegale ha bloccato **una content delivery network** (rete di distribuzione di contenuti) di Big G del nodo di Milano, con conseguenze su vari servizi, tra cui Drive, utilizzato per archiviare e condividere dati in cloud, e **una delle cache di Youtube.** Due risorse che, tra le altre, ovviamente, non hanno niente a che vedere con la trasmissione pirata di partite di calcio e altri sport, che è ciò di cui Piracy shield si dovrebbe occupare, ma che dimostra per l’ennesima volta come la tecnologia regalata dalla Serie A ad Agcom finisca per [asfaltare siti innocui.](https://www.wired.it/article/piracy-shield-siti-ricorso-agcom-codice/) Arrivando a pestare i piedi persino a Google.

## Il blocco di Google drive e i problemi di download

Ricostruiamo i fatti. Almeno dalle ore 18.56 del pomeriggio di sabato, come dimostrato da una fonte a *Wired* attraverso alcune analisi, Piracy shield fa **scattare il blocco dell’indirizzo drive.usercontent.google.com**. È una cdn del nodo di Milano, dove passa il 70% del traffico del colosso del web. [Come spiega la stessa Google](https://support.google.com/a/answer/2589954?hl=en), è uno dei domini critici per Drive. L’oscuramento attuato dalla piattaforma nazionale antipirateria impedisce di raggiungerlo e, di fatto, di poter **effettuare i download dei file archiviati su Drive**. *Wired* ha potuto verificare su [Piracy shield search](https://piracyshield.iperv.it/), un progetto di condivisione pubblica dei domini oscurati fornito da Infotech srl, l'effettivo blocco del dominio.

![Il blocco di Drive su Piracy shield search](https://media-assets.wired.it/photos/671428679d9c313f3ea8cf10/master/w_1600%2Cc_limit/Screenshot%25202024-10-19%2520alle%252022.15.19.png)

Il blocco di Drive su Piracy shield searchPiracy shield search

Il picco di **segnalazioni di interruzioni su Downdetector**, un [sito che raccoglie alert su problemi con i servizi online](https://downdetector.it/problemi/google-drive/), a partire dalle 19 dimostra che, man mano che le persone provano a connettersi a Drive, riscontrano l’**inaccessibilità del portale**. Un problema per singoli utenti, aziende, ma anche scuole e università che si appoggiano a Google Workspace, gli ambienti di lavoro condiviso messi a disposizione per imprese e mondo dell’istruzione. Basti pensare che i [sistemi di intelligenza artificiale che il ministero dell’Istruzione](https://www.wired.it/article/intelligenza-artificiale-scuola-italia-google-assistenti-virtuali/) ha deciso di sperimentare in alcune scuole italiane viaggiano proprio sui Workspace di Google. Il fatto che l'interruzione si sia verificata di sabato sera, quando molte persone che lavorano, anche in modalità agile, non erano impegnate in attività professionali, ha fatto sì che alcuni utenti abbiamo scoperto dei problemi la mattina successiva. E con timori sui tempi di ripristino, che potrebbero impattare sul lavoro dalle prossime ore.

![Le segnalazioni sui disservizi di Drive su Down detector](https://media-assets.wired.it/photos/6714289ba13d057c911781bc/master/w_1600%2Cc_limit/Screenshot%25202024-10-19%2520alle%252022.43.01.png)

Le segnalazioni sui disservizi di Drive su Down detectorDown detector

Un picco di segnalazioni che, in parallelo, si **riflette specularmente anche su Youtube**. Perché, come *Wired* ha potuto verificare, la cdn finita nel mirino del sistema di Agcom ha avuto conseguenze anche sulla piattaforma di video, sempre di casa Google, e su Google foto.

![Il picco di segnalazioni su Youtube di Downdetector](https://media-assets.wired.it/photos/671436c3814e0610dfa674e9/master/w_1600%2Cc_limit/Screenshot%25202024-10-20%2520alle%252000.44.32.png)

Il picco di segnalazioni su Youtube di DowndetectorDowndetector

## Google non è in whitelist?

Ma come è possibile che la **piattaforma nazionale antipirateria abbia oscurato una cdn di uno dei colossi del web** e che peraltro di recente si era reso disponibile a collaborare con Agcom contro le tv pirata (il cosiddetto pezzotto)? Semplice: perché ogni denuncia che i detentori dei diritti sportivi caricano su Piracy Shield si [porta dietro lunghe liste di domini da bloccare](https://www.wired.it/article/piracy-shield-sblocco-siti-oscurati-campionato-lega-serie-a/). Dove spesso finiscono risorse estranee alla pirateria online.

Dopo che la segnalazione è stata caricata, **Piracy Shield invia in automatico un alert ai fornitori** di servizi internet (internet service provider, Isp), che stando alla legge che ha istituito la piattaforma, la 93 del luglio 2023, hanno **30 minuti di tempo per bloccare il sito.** Operazioni che, giocoforza, gli [Isp devono compiere in automatico.](https://www.wired.it/article/piracy-shield-campionato-siti-ricorso-costi-concerti-film/) Esiste una **whitelist di risorse online da non abbattere**, per nessun motivo, e che come *Wired* ha scoperto, contiene **11mila elementi**. A valle di quanto successo con Drive e Youtube, viene dunque da pensare che però, tra questi, non vi siano **alcuni dei più importanti sotto-domini di uno dei più grandi colossi mondiali della tecnologia**. E chissà quali altre risorse mancano da quell'elenco, su cui è stata imposta la massima segretezza.

A quanto apprende *Wired* da diverse fonti impegnate nel controllo delle conseguenze del blocco di Drive effettuato da Piracy Shield, ci [sono volute circa sei ore per il ripristino](https://www.wired.it/article/piracy-shield-blocco-google-drive-download/). Sembra che, nell'immediato, **Tim e Wind3 abbiano eliminato il dominio dalla lista delle risorse da oscurare** ma ci sono volute ore perché il servizio riprendesse a funzionare, con strascichi nella giornata di domenica 20 ottobre. E, in taluni casi, gli utenti hanno **visualizzato anche l’avviso di Agcom** che segnala che il sito è stato reso inaccessibile proprio dalla piattaforma antipirateria. Giulia Pastorella, deputata di Azione, ha anticipato che lunedì 21 ottobre presenterà una interrogazione parlamentare in merito e richiederà una convocazione di Agcom.

#### X content

## La stretta alle regole

Stando alle regole dell’Autorità garante delle comunicazioni, il proprietario di un dominio erroneamente bloccato ha cinque giorni di tempo per fare ricorso contro il blocco e chiedere il ripristino del dominio. Dato il clamore d...