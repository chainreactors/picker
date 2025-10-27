---
title: Windows, perché dovreste fare attenzione quando ritagliate una foto
url: https://www.wired.it/article/windows-bug-editing-foto/
source: Instapaper: Unread
date: 2023-03-25
fetch_date: 2025-10-04T10:40:16.012269
---

# Windows, perché dovreste fare attenzione quando ritagliate una foto

[Skip to main content](#main-content)

Apri il menu di navigazione

Menu

[![Wired Italia](/verso/static/wired-us/assets/logo-header.svg)](/)

Perché dovreste fare attenzione quando ritagliate una foto su Windows

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

Close Banner

Close

[![Wired Next Fest](/verso/static/wired/assets/wnf-156x40.png)](https://eventi.wired.it/nextfest25-trentino)

00

Giorni

:

00

Ore

:

00

Minuti

:

00

Secondi

[Iscriviti, ingresso gratuito](https://eventi.wired.it/nextfest25-trentino/ticket)[3-5 ottobre, Rovereto](https://eventi.wired.it/nextfest25-trentino)

[Lily Hay Newman](/contributor/lily-hay-newman/)

[Security](/security/)

24.03.2023

# Perché dovreste fare attenzione quando ritagliate una foto su Windows

I ricercatori hanno scoperto un bug negli strumenti di editing fotografico del sistema operativo, che può rivelare informazioni rimosse intenzionalmente dagli utenti

![foto donna ritagli](https://media-assets.wired.it/photos/641c40f14717988e062ec237/16:9/w_2560%2Cc_limit/Some-Photo-Cropping-Tools-Aren't-Fully-Cropping-Your-Photos-Security-GettyImages-636945023.jpg)

Vasilina Popova/Getty Images

All'inizio di marzo [**Google**](https://www.wired.it/topic/google/) ha [distribuito un aggiornamento](https://source.android.com/docs/security/bulletin/pixel/2023-03-01) che correggeva una **vulnerabilità di Markup, lo strumento di editing fotografico di default dei suoi smartphone** [**Pixel**](https://www.wired.it/article/pixel-7-7-pro-google-sicurezza-privacy-vpn/). Dalla sua introduzione nel 2018 per Android 9, lo strumento per ritagliare le foto lasciava all'interno delle immagini modificate alcuni dati che potevano essere utilizzati per **ricostruire in parte o totalmente la foto originale**. Anche se è stata risolta, si tratta comunque di una vulnerabilità grave, dal momento che  per anni gli utenti Pixel hanno creato, e in molti casi presumibilmente condiviso, immagini ritagliate che potrebbero ancora contenere informazioni private o sensibili che un utente stava cercando di eliminare.

Ma c'è di peggio. Il bug, soprannominato "**aCropalypse**", è stato scoperto e originariamente sottoposto all'attenzione di Google dal ricercatore di sicurezza e studente universitario Simon Aarons, che per l'occasione ha collaborato con il collega David Buchanan, esperto di [ingegneria inversa](https://it.wikipedia.org/wiki/Reverse_engineering). Questa settimana i due hanno scoperto, con loro grande sorpresa, che una **versione molto simile della falla** è presente anche in altre utility per ritagliare foto all'interno di [**Windows**](https://www.wired.it/topic/windows/). Lo **Snipping Tool di Windows 11 e lo Snip & Sketch di Windows 10** sono infatti vulnerabili nei casi in cui l'utente esegue uno screenshot e poi salva, ritaglia e salva nuovamente il file. Le foto modificate con Markup, invece, trattenevano i dati anche quando l'utente applicava lo strumento prima di salvare la foto.

Mercoledì 22 marzo Microsoft ha dichiarato a *Wired US* che è "a *conoscenza di queste segnalazioni*" e che sta "*indagando*". L'azienda ha aggiunto che è pronta a prendere "***provvedimenti se necessario***". "*È stato davvero sbalorditivo, come un fulmine che cade due volte nello stesso punto* – racconta Buchanan –. *Era già abbastanza sorprendente che la vulnerabilità originale di Android non fosse già stata scoperta. È stato piuttosto surreale*".

Dopo che le vulnerabilità sono state individuate, i ricercatori hanno iniziato a [trovare vecchie discussioni](https://stackoverflow.com/questions/35842374/how-can-i-overwrite-a-file-in-uwp) sui forum dedicati alla programmazione in cui alcuni sviluppatori avevano notato lo strano comportamento degli strumenti di ritaglio delle immagini. Ma Aarons sembra essere stato il primo a riconoscere le **potenziali implicazioni per la sicurezza e la** [**privacy**](https://www.wired.it/topic/privacy/), o almeno il primo a portare le scoperte a Google e Microsoft.

"*In realtà me ne sono accorto alle quattro del mattino **per puro caso**, quando ho notato che il file di un piccolo screenshot con del testo bianco su sfondo nero che avevo inviato pesava cinque Mb, e la cosa non mi tornava*", spiega Aarons.

Anche se spesso non è possibile recuperarle completamente, le immagini interessate da aCropalypse possono essere sostanzialmente ricostruite. Aarons [ha fornito alcuni esempi](https://twitter.com/ItsSimonTime/status/1636857478263750656?s=20), tra cui uno in cui è riuscito a **recuperare il numero della sua carta di credito dopo aver tentato di ritagliarlo da una foto**. In poche parole, in circolazione c'è una notevole quantità di foto che contengono più dati di quanti dovrebbero, informazioni che nello specifico qualcuno aveva cercato di rimuovere intenzionalmente.

**Microsoft non ha ancora distribuito una correzione per il bug**, mentre l'aggiornamento introdotto da Google non risolve il problema per i file immagine esistenti ritagliati negli anni in cui lo strumento era ancora vulnerabile. Google fa però notare che alcuni social media e servizi di comunicazione sono in grado eliminare automaticamente i dati errati contenuti nei file immagine che vengono condivisi sulle piattaforme.

"*Le applicazioni e i siti web che ricompattano le immagini, come **Twitter, Instagram o Facebook, eliminano automaticamente i dati extra dalle immagini** caricate. Le immagini pubblicate su siti come questi non sono a rischio*", ha dichiarato in in un comunicato Ed Fernandez, portavoce di Google.

I ricercatori tuttavia sottolineano che **alcune piattaforme, come per esempio Discord, non applicano questa procedura**. Da utente di Discord, Buchanan racconta che continuava a vedere utenti del servizio pubblicare schermate ritagliate, e che ha fatto molto fatica a non dire nulla prima che la vulnerabilità fosse resa pubblica.

Steven Murdoch, professore di ingegneria della sicurezza presso l'University College di Londra, ricorda di aver scoperto nel 2004 una [falla](https://murdoch.is/talks/ccc04_hiddendata.pdf) che faceva sì che una versione precedente di un'immagine modificata venisse memorizzata nei dati delle miniature del file. "***Non è la prima volta che vedo questo tipo di vulnerabilità*** – dice –, *e credo che il motivo sia che quando viene scritto, il software viene testato per assicurarsi che ci sia quello che ci si aspetta. Si salva un'immagine, la si può aprire e il gioco è fatto. Quello che non viene controllato è se accidentalmente vengono memorizzati anche dati extra*".

La vulnerabilità delle miniature scoperta da Murdoch nel 2004 era concettualmente simile ad aCropalypse dal punto di vista dei rischi per la privacy, ma aveva basi tecniche molto diverse, legate in quel caso a problemi nella progettazione dell'interfaccia di programmazione delle applicazioni (Api). Nonostante consideri aCropalypse un problema per gli utenti le cui foto sono già in circolazione, Murdoch sottolinea che il suo impatto maggiore potrebbe essere il **dibattito su come promuovere migliori pratiche di sicurezza** nello sviluppo e nell'implementazione delle Api.

[*Questo articolo è comparso originariamente su Wired US.*](https://www.wired.com/story/acropalyse-google-markup-windows-photo-cropping-bug/)

## Le storie da non perdere di Wired

* È iniziato a Rovereto il Wired Next Fest Trentino. Incontri, eventi, workshop e attività per parlare di innovazione, tecnologie e delle “energie” che ci servono fino al 5 ottobre. Per partecipare ai talk e intervist...