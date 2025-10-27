---
title: Piracy Shield, ma come funzionano i sistemi di sicurezza
url: https://www.wired.it/article/piracy-shield-white-list-come-funziona-domini/
source: Instapaper: Unread
date: 2024-10-22
fetch_date: 2025-10-06T19:01:14.092687
---

# Piracy Shield, ma come funzionano i sistemi di sicurezza

[Skip to main content](#main-content)

Apri il menu di navigazione

Menu

[![Wired Italia](/verso/static/wired-us/assets/logo-header.svg)](/)

Piracy Shield, ma come funzionano i sistemi di sicurezza?

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

Il caso

21.10.2024

# Piracy Shield, ma come funzionano i sistemi di sicurezza?

L’incidente della piattaforma nazionale anti-pirateria che per sei ore ha tenuto in scacco Big G apre squarci inquietanti sulle misure di sicurezza della tecnologia scelta da Lega Serie A e Agcom per combattere il pezzotto

![Il logo di Google](https://media-assets.wired.it/photos/62d03f276d33406571afb58a/16:9/w_2560%2Cc_limit/GettyImages-1240824438.jpg)

Il logo di GoogleFABRICE COFFRINI/AFP via Getty Images

Come è stato possibile che **Piracy Shield, la piattaforma nazionale antipirateria,** abbia [**oscurato un dominio di Google Drive?**](https://www.wired.it/article/piracy-shield-blocco-google-drive-download/) È questa la domanda rimasta in sospeso dopo che sabato 19 ottobre, pochi minuti prima delle sette di sera, un **ticket caricato su Piracy shield ha inibito l’accesso a una content delivery network** (rete di distribuzione di contenuti) di Big G del nodo di Milano, con conseguenze su vari servizi. Di cui il più evidente è il **blocco dei download da Google Drive.** Un blackout durato circa sei ore, revocato dopo la mezzanotte, ma con strascichi per alcuni utenti proseguiti nelle prime ore della giornata di domenica 20 ottobre.

L’incidente apre squarci inquietanti sulle **misure di protezione adottate dalla tecnologia scelta da Lega Serie A** e Autorità garante delle comunicazioni (Agcom) per combattere il pezzotto e sulla **cosiddetta white list**, introdotta per impedire che la piattaforma anti-pirateria possa abbattere servizi internet critici. Come Google, che si è ritrovato con un segmento di rete (si tratta di una cdn dello snodo) dove passa il 70% del suo traffico inaccessibile per ore.

## Come funziona Piracy Shield

Per provare a capire cosa sia successo con Google, dobbiamo fare un passo indietro. E spiegare come è organizzata **Piracy shield, istituita dalla legge 93 del 24 luglio 2023** per oscurare la trasmissione illegale di partite di calcio e altri eventi sportivi. La piattaforma raccoglie le **segnalazioni di chi detiene i diritti (come Lega Serie, Mediaset, Sky e Dazn)** sugli **indirizzi Ip “incriminati”** e **allerta i fornitori dei servizi internet** (internet service provider, Isp), che [hanno 30 minuti per provvedere al blocco](https://www.wired.it/article/piracy-shield-piattaforma-agcom-pezzotto-streaming-illegale/). Un’attività che svolgono in automatico, dato che ogni segnalazione contiene persino migliaia di risorse online da oscurare. Chi **carica un ticket per denunciare un indirizzo Ip** da abbattere, ha 60 secondi per correggere la segnalazione.

È questo l’ingranaggio nel quale è finita anche la cdn di Google bloccata sabato sera. Non è tuttavia la prima volta in cui **Piracy shield oscura siti che non fanno pirateria online**. È un problema connaturato alla progettazione della piattaforma stessa, curata da Sp tech (braccio tecnologico dello Studio legale Previti), che non tiene conto del fatto che oggi, [su uno stesso dominio, insistono varie risorse online.](https://www.wired.it/article/piracy-shield-siti-ricorso-agcom-codice/) È come se, per fermare un reato che si svolge in un appartamento, Piracy Shield radesse al suolo un intero quartiere.

Ma come è stato possibile oscurare un dominio come drive.usercontent.google.com, che richiama in modo inequivocabile una risorsa legittima e non destinata alla pirateria online? A più di 24 ore dall’incidente, **né Google né l’Autorità garante delle comunicazioni** hanno preso ufficialmente una posizione sull’accaduto.

![article image](https://media-assets.wired.it/photos/615da627b217d49ff6a16db3/master/w_775%2Cc_limit/wired_placeholder_dummy.png)

[WiredLeaks, come mandarci una segnalazione anonima](/internet/web/2021/02/15/wiredleaks-come-fare-segnalazioni-anonime/)

Hai segnalazioni su Piracy Shield: usa WiredLeaks per dialogare in modo sicuro e anonimo con la nostra redazione

## La questione delle white list

Agcom ha sempre rassicurato sul fatto che **Piracy Shield è dotata di varie white list** con i domini da non abbattere, qualora finissero per sbaglio in una segnalazione. *Wired* in passato ha scoperto che questo elenco **comprende circa 11mila elementi**. Tra i quali, pare di intendere, non c’era il dominio di Google bloccato da Piracy Shield.

[In una diretta su Youtube](https://www.youtube.com/live/2CUzcZZQZSs) organizzata da Matteo Flora, esperto di digitale, imprenditore e docente, il commissario dell'Agcom Massimiliano Capitanio, che ha menzionato che dall'avvio di Piracy shield nel febbrai 2024 si sono fatti interventi su 24mila tra indirizzi Ip e *fully qualified domain name* (fqdn, ossia un nome di dominio non ambiguo che consente di identificare senza dubbio una risorsa online), ha detto che “*l'Autorità potrebbe valutare che chi fa le segnalazioni e non si attiene rigorosamente a quanto previsto dalla legge e dal regolamento Agcom in maniera continua potrebbe essere escluso*”. E ha aggiunto che “*nonostante la legge imponga a tutti i fornitori di servizi media di iscriversi alla piattaforma, i signori di Google e Cloudflare hanno deciso di non iscriversi e quindi iscrivendosi, **Google non ha potuto comunicare alla white list**"* le risorse da includere. Per poi correggersi e affermare che “*potrebbe essere nella white list*”, anche se almeno una risorsa, la cdn colpita sabato sera, evidentemente non c'era.

Secondo una seconda fonte interpellata da *Wired*, che ha partecipato ai lavori del tavolo tecnico di Piracy shield, dentro le white list ci sarebbero anche **alcune risorse online dei detentori dei diritti, alcune degli Isp.** E anche la **virtual private network attraverso cui si accede a Piracy shield stesso**. Insomma, gli strumenti per tenere in piedi la piattaforma. *Wired* ha chiesto a Google se ha indicato i domini da inserire nella white list di Piracy shield, senza tuttavia ricevere risposta prima della pubblicazione di questo articolo.

Un'altra white list è stata fornita dall'**Autorità per la cybersicurezza nazionale** (Acn), che ha inserito nella sua, a titolo di esempio, alcuni domini istituzionale, come quelli della presidenza del Consiglio dei ministri, dei ministeri, della Banca d’Italia, di alcune aziende sanitarie.

Secondo la fonte di *Wired* che ha partecipato ai lavori, il **principio della white list** non era tanto quello di **coprire tutti i siti che non sono “accusabili” di pirateria**, ma di inserire una serie di siti istituzionali e alcune risorse di Isp e detentori dei diritti, per non rischiare di bloccare del tutto la loro operatività. Tutto il resto, di conseguenza, è filtrabile. Un principio che esporrebbe in pratica la quasi totalità dei servizi online al rischio di erronee segnalazioni su Piracy Shield. Per fare chiarezza sarebbe utile poter consultare la white list, alla cui ostensione tuttavia si oppongono per supposte ragioni di sicurezza nazionale.

## La mancanza del soc

A questo si aggiunge il fatto che **non esiste un centro che coordini le attività di Piracy Shield.** Secondo il racconto di un operatore internet a *Wired*, la scoperta del blocco di Google è stata **gestita attraverso un incrocio di telefonate e messaggi** tra...