---
title: I dati di chi ha un prestito con Agos potevano essere scoperti con pochi clic
url: https://www.wired.it/article/agos-dati-clienti-prestiti-codice-fiscale/
source: Over Security - Cybersecurity news aggregator
date: 2025-04-18
fetch_date: 2025-10-06T22:06:45.840166
---

# I dati di chi ha un prestito con Agos potevano essere scoperti con pochi clic

[Skip to main content](#main-content)

Apri il menu di navigazione

Menu

[![Wired Italia](/verso/static/wired-us/assets/logo-header.svg)](/)

Agos, i dati di chi ha un prestito potevano essere scoperti con pochi clic

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

[Raffaele Angius](/author/rangius/)

[Security](/security/)

17.04.2025

# Agos, i dati di chi ha un prestito potevano essere scoperti con pochi clic

Ma ora il problema del sito web della società di finanziamenti è stato risolto, dopo la scoperta di un hacker e la segnalazione di *Wired*. Ma per l'azienda non è necessario avvertire il Garante della privacy

![Il logo di Agos su uno sfondo digitale](https://media-assets.wired.it/photos/67ffe07fac8ad7d55118cae7/16:9/w_2560%2Cc_limit/Progetto%2520senza%2520titolo%2520(59).png)

Il logo di Agos su uno sfondo digitale

Non è certo un comportamento voluto o intenzionale quello del **sito web di Agos, società finanziaria italiana specializzata nel credito al consumo**, [dal quale fino a qualche giorno](https://www.wired.it/article/gen-z-truffe-online/) fa è stato **possibile acquisire in modo fraudolento** il **codice fiscale** e il **codice cliente** degli utenti che hanno una **posizione aperta presso l’istituto**.

A scoprire il comportamento anomalo è stato prima di tutti il ricercatore ed esperto di *intelligence* da fonti aperte **Lorenzo Romani**, che a sua volta non ha divulgato informazioni utili a intuire quale fosse il portale affetto dal problema. La ragione è chiara: qualunque sito web che **riveli involontariamente i dati dei propri utenti** può costituire una preziosa fonte di informazioni per costruire **attacchi informatici e truffe online**. Svelare l’esistenza del sito affetto da una vulnerabilità e, peggio ancora, i dettagli per replicarla, avrebbe quindi potuto [compromettere alcune informazioni personali degli utenti](https://www.wired.it/article/truffe-online-maxi-operazione-polizia-postale-italia/) e, di conseguenza, la loro sicurezza.

**Il problema è stato risolto in seguito a una segnalazione di *Wired***, che per la pubblicazione di questo articolo ha deciso di attendere un ragionevole lasso di tempo per dare modo all’azienda, controllata da Crédit Agricole e da Banco Bpm, di **intervenire tempestivamente a tutela dei suoi clienti**.

## Il diavolo sta nei dettagli

**Pagina di accesso, recupero credenziali, recupero della password** o del codice utente: il procedimento è familiare a chiunque disponga di un **dispositivo digitale**. Tanto più se si è inclini a perdere le proprie credenziali e dunque a chiederne delle nuove. È da questo meccanismo che, a causa di un comportamento non previsto del sito web di Agos era possibile **acquisire informazioni personali** degli utenti attraverso le funzioni di “ispezione degli elementi” delle pagine web, comuni in qualunque browser e **ben note** a qualsiasi sviluppatore.

È chiaro che a ogni azione su un sito, il computer e il sito stesso comunicano: nel caso di Agos, la comunicazione era ben troppo ricca di dettagli e tutti questi venivano trasferiti in chiaro. Così, in caso di **smarrimento del codice utente il sistema chiedeva di inserire il proprio codice fiscale**: inserendone uno qualunque era possibile verificare se fosse effettivamente associato a **un’utenza di Agos**, acquisendone anche il codice cliente. In tal senso, un utente qualunque avrebbe potuto inserire codici fiscali di cui era a conoscenza per controllare se il legittimo titolare aveva mai ricevuto prestiti dalla finanziaria.

Ma il problema forse più cogente riguardava **il recupero della password**, per la quale il sistema chiede il codice utente assegnato al cliente al momento dell’iscrizione. Infatti, a ogni richiesta di password tramite suddetto codice, il sistema **restituiva in chiaro il codice fiscale associato**.

Di per sé potrebbe sembrare un problema minore, dal momento che per eseguire questa procedura **occorre conoscere in partenza il codice del cliente**. Tuttavia, questi sono composti da stringhe di numeri da otto cifre. Era dunque facile comporre **stringhe di numeri casuali** comprese tra un milione e 19999999, estraendo il codice fiscale **associato a ogni combinazione corretta**, come *Wired* ha potuto verificare.

![Screenshot del funzionamento della vulnerabilità testata con dati personali da Wired](https://media-assets.wired.it/photos/67ffc883916c7c772530718d/master/w_1600%2Cc_limit/screenagos1.png)

Screenshot del funzionamento della vulnerabilità, testata con dati personali da Wired

*“Cinque anni fa scoprivo che una funzionalità della piattaforma web di Findomestic consentiva di stabilire se al codice fiscale di un soggetto fosse abbinato un finanziamento o una richiesta di finanziamento”*, scrive su Linkedin Lorenzo Romani, a cui va la paternità della scoperta: “*A un lustro di distanza siamo al punto di partenza”*. Il riferimento è a una **simile denuncia** fatta sempre da Romani e anche all’epoca [riportata](https://www.wired.it/internet/web/2019/12/09/findomestic-prestito-codice-fiscale/) da *Wired*, in seguito alla quale Findomestic chiarì come il meccanismo fosse progettato per *“facilitare l*’onboarding *degli utenti”*.

Il problema fu comunque risolto. Ma nel caso di Findomestic si limitava al fatto che fosse possibile verificare se un dato codice fiscale era associato a un finanziamento. Come detto, la vulnerabilità scoperta sul sito di Agos avrebbe permesso, al contrario, di elencare codici utente casuali, **svelando l’identità dei clienti della finanziaria**.

## Perché questo è un problema

In un quotidiano ripetersi di truffe e raggiri, qualunque informazione in rete porta l’acqua al mulino di chi vuole approfittarsene. Se un truffatore avesse sfruttato questo meccanismo, avrebbe potuto facilmente **individuare bersagli fragili** dei quali avrebbe a quel punto conosciuto sia i dati personali (rappresentati nel codice fiscale) sia il fatto che avevano sottoscritto dei finanziamenti con Agos. Con tanto di codice utente - un dato verosimilmente **noto solo all’intestatario del credito e all’azienda** che lo eroga - chiunque avrebbe potuto costruire una campagna di truffe ai danni del più sprovveduto, spacciandosi a sua volta per un operatore della società di credito. Fortuna vuole che ad accorgersene sia stato un *ethical hacker*, termine che identifica normalmente quegli esperti informatici che preferiscono rivelare le vulnerabilità piuttosto che trarne un vantaggio personale, anche se nel caso di falle nei sistemi è sempre difficile accertare che nessuno se ne fosse accorto prima, magari **trattenendo per sé l’informazione**.

***"Non ci risulta che ci sia stato alcun abuso",*** ha fatto sapere l’azienda a *Wired*, con cui ha dimostrato la **massima collaborazione** fin dal primo contatto. L’azienda ha spiegato che il problema era noto ma giudicato non di priorità massima in quanto non permette la compromissione delle credenziali di accesso degli utenti. Per la stessa ragione, **Agos ritiene di non dover informare l’Autorità garante per la protezione dei dati personali**, che generalmente deve essere coinvolta in caso di violazione dei dati.

*"Il tema da lei evidenziato era noto, monitorato e in pianificazione di intervento nell’ambito dei processi di miglioramento e revisione continui, ritenuto non critico in quanto non avrebbe potuto avere un seguito di accesso al profilo utente -* scrive Agos in una nota in risposta alle domande di *Wired* -. *Sono infatti necessarie autorizzazioni ed Ot...