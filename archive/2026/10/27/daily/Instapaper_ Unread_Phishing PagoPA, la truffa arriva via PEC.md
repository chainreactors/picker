---
title: Phishing PagoPA, la truffa arriva via PEC
url: http://www.zeusnews.it/n.php?c=32655
source: Instapaper: Unread
date: 2026-10-27
fetch_date: 2026-10-28T07:50:14.380616
---

# Phishing PagoPA, la truffa arriva via PEC

![](https://b.scorecardresearch.com/p?c1=2&c2=13879765&cv=2.0&cj=1)

[![Zeus News](/pic/logo.gif)](/)

[Salta il menu](#contenuto)

* [Home](http://www.zeusnews.it)
* [Editoriale](index.php3?ar=sezioni&numero=949)
* [Recensioni](index.php3?ar=sezioni&numero=912)
* [Focus](index.php3?ar=sezioni&numero=913)
* [Sicurezza](index.php3?ar=sezioni&numero=901)
* [Trucchi](index.php3?ar=sezioni&numero=906)
* [Maipiusenza](index.php3?ar=sezioni&numero=903)
* [Segnalazioni](index.php3?ar=sezioni&numero=905)
* [Sondaggi](index.php3?ar=sezioni&numero=902)
* [Antibufala](index.php3?ar=sezioni&numero=904)
* [Download](index.php3?ar=sezioni&numero=916)
* [News](index.php3?ar=sezioni&numero=907)
* [Flash](index.php3?ar=sezioni&numero=914)
* [Pag2](index.php3?ar=sezioni&numero=915)

[![Newsletter](pic/pulsanti/newsletter.png "Newsletter")](http://newsletter.zeusnews.it/index.php?p=subscribe&id=5)
[![RSS](pic/pulsanti/rss.png "Feed RSS")](http://feeds.feedburner.com/ZeusNews)
[![Facebook](pic/pulsanti/facebook.png "Zeus News su Facebook")](http://www.facebook.com/ZeusNews)
[![Forum Olimpo Informatico](pic/pulsanti/forum.png "Forum Olimpo Informatico")](http://forum.zeusnews.com/index.php?c=1)
[![Contatti](pic/pulsanti/contatti.png "Contatti")](http://www.zeusnews.it/index.php3?ar=staff)
[![Accadde oggi](pic/pulsanti/calendar3.png "Accadde oggi")](http://www.zeusnews.it/index.php3?ar=accaddeoggi)
[![Ricerca](pic/pulsanti/ricerca.png "Cerca in Zeus News")](http://www.zeusnews.it/index.php3?ar=ricerca)

[Newsletter](http://newsletter.zeusnews.it/index.php?p=subscribe&id=5)
[Feed RSS](http://feeds.feedburner.com/ZeusNews)
[Facebook](http://www.facebook.com/ZeusNews)
[Forum](http://forum.zeusnews.com/index.php?c=1)
[Contatti](http://www.zeusnews.it/index.php3?ar=staff)
[Accadde oggi](http://www.zeusnews.it/index.php3?ar=accaddeoggi)
[Cerca](http://www.zeusnews.it/index.php3?ar=ricerca)

# Phishing PagoPA, la truffa arriva via PEC

Nuove campagne di phishing sfruttano PEC compromesse per inviare false multe e raccogliere così dati personali e bancari.

[Tweet](https://twitter.com/share)

[*ZEUS News* - [www.zeusnews.it](https://www.zeusnews.it/) - 27-10-2026] Commenti

![truffa pagopa pec](https://www.zeusnews.it/img/5/5/6/2/3/0/032655-620-truffa-pagopa-pec.jpg)

Foto di [Charles Asselin](https://unsplash.com/it/%40crawnical).

Le campagne di phishing che sfruttano il nome di PagoPA hanno compiutodalla un ulteriore salto di qualità: i messaggi fraudolenti adesso non arrivano più soltanto da indirizzi falsificati o domini creati ad hoc, ma vengono diffusi anche attraverso caselle di Posta Elettronica Certificata compromesse. L'obiettivo resta quello di convincere le vittime a pagare una presunta multa stradale e, soprattutto, a consegnare dati personali e informazioni finanziarie ai criminali informatici. Secondo quanto rilevato dal [CERT-AGID](/link/48383 "https://cert-agid.gov.it/news/phishing-pagopa-nuove-campagne-a-tema-multe-diffuse-tramite-pec-compromesse/"), nell'ultima settimana sono state osservate diverse campagne che utilizzano PEC compromesse per inviare richieste di pagamento apparentemente riconducibili a PagoPA. La scelta di sfruttare [caselle](util/extlink/cerca_amazon.php?q=caselle "Cerca caselle su Amazon") certificate aggiunge un elemento di credibilità alla truffa, poiché molti destinatari tendono ad associare la PEC a comunicazioni affidabili e ufficiali.

Nei casi più recenti il messaggio veniva inviato da una PEC compromessa verso un ordinario indirizzo di posta elettronica, mentre in copia comparivano circa 340 indirizzi PEC. Questa modalità di distribuzione contribuisce a rendere la comunicazione più verosimile agli occhi della vittima, che può interpretare la presenza di numerosi destinatari come un segnale di autenticità. L'[esca](util/extlink/cerca_amazon.php?q=esca "Cerca esca su Amazon") utilizzata è una presunta violazione del Codice della Strada. Il testo richiama la forma tipica di un provvedimento amministrativo, impiega un linguaggio particolarmente formale e contiene numerosi riferimenti normativi. Al destinatario viene richiesto il pagamento di una sanzione da 198 euro entro una scadenza ravvicinata, con l'avvertimento che l'importo salirà a 268 euro in caso di ritardo.

All'interno del messaggio compare un pulsante denominato *Accesso al portale istituzionale*. Facendo clic sul collegamento, l'utente viene indirizzato verso un sito fraudolento che riproduce loghi, [colori](util/extlink/cerca_amazon.php?q=colori "Cerca colori su Amazon") e impostazione grafica del sistema PagoPA. In alcuni casi osservati dagli analisti, le pagine erano ospitate su infrastrutture riconducibili a un fornitore di servizi di hosting russo e utilizzavano domini con estensione *.ru*. Una volta aperta la falsa piattaforma, alla vittima viene chiesto di inserire una serie di informazioni personali: nome, cognome, codice fiscale, data di nascita, indirizzo di posta elettronica e numero di telefono. La procedura viene presentata come necessaria per consultare il verbale o completare il pagamento della presunta sanzione.

Le analisi tecniche svolte dal CERT-AGID hanno però evidenziato un elemento particolarmente interessante: il portale fraudolento non si limita a raccogliere informazioni statiche, ma integra un meccanismo che consente agli attaccanti di controllare da remoto il percorso di navigazione dell'utente. La pagina comunica periodicamente con un pannello di gestione presente sul server e verifica continuamente l'eventuale presenza di istruzioni impartite dagli operatori della frode. In pratica, gli autori dell'attacco possono modificare dinamicamente le schermate mostrate alla vittima. Tra le possibili destinazioni individuate dagli analisti figurano pagine dedicate alla raccolta dei dati delle carte di pagamento e dei codici di verifica bancari. Questo approccio permette ai [criminali](util/extlink/cerca_amazon.php?q=criminali "Cerca criminali su Amazon") di adattare il flusso della truffa in funzione delle informazioni già ottenute e di guidare passo dopo passo l'utente verso la consegna dei dati più sensibili.

Leggi anche:

[![](/img/2/1/5/2/3/0/032512-620-microsoft-eviltokens.png)](/zn/32512)

[Microsoft smantella EvilTokens, il servizio di phishing in abbonamento gestito d...](/zn/32512 "Microsoft smantella EvilTokens, il servizio di phishing in abbonamento gestito dalla IA")

[![](/img/2/8/4/2/3/0/032482-620-revolut-attacco-italia.jpg)](/zn/32482)

[Attacco a Revolut, tra i dati rubati spunta una cartella Italy](/zn/32482 "Attacco a Revolut, tra i dati rubati spunta una cartella Italy")

[![](/img/4/4/3/2/3/0/032344-620-truffa-arera-bonus-idrico.jpg)](/zn/32344)

[Phishing con il logo ARERA: attenzione alle email sul bonus sociale idrico](/zn/32344 "Phishing con il logo ARERA: attenzione alle email sul bonus sociale idrico")

[![](/img/7/9/1/2/3/0/032197-620-hackerata-trenitalia-phishing.jpg)](/zn/32197)

[Hackerata Trenitalia, rubati i dati di viaggio dei passeggeri](/zn/32197 "Hackerata Trenitalia, rubati i dati di viaggio dei passeggeri")

Il fenomeno delle false multe a tema PagoPA non è nuovo, ma i numeri raccolti dal CERT-AGID mostrano una dimensione ormai rilevante. Dal 21 aprile 2025 sono state censite 1.874 campagne di phishing collegate ai marchi PagoPA e SEND. Nello stesso periodo sono stati individuati e condivisi 14.279 indicatori di compromissione con le amministrazioni e le organizzazioni accreditate ai servizi dell'agenzia. I dati evidenziano inoltre che le [campagne](util/extlink/cerca_amazon.php?q=campagne "Cerca campagne su Amazon") che sfruttano il nome e l'immagine di PagoPA risultano quasi il doppio rispetto a quelle che impersonano SEND. Il quadro conferma come i servizi digitali utilizzati quotidianamente dai cittadini rappresentino un bersaglio particolarmente appetibile per i gruppi criminali che puntano a massimizzare il numero di vittime facendo leva su marchi ampiamente riconosciuti.

Le segnalazioni pubblicate dal CERT...