---
title: Alla ricerca di elefanti
url: https://osintops.com/alla-ricerca-di-elefanti/
source: Instapaper: Unread
date: 2022-12-02
fetch_date: 2025-10-04T00:19:47.589816
---

# Alla ricerca di elefanti

[![OsintOps Project](https://osintops.com/wp-content/uploads/2024/07/O-Main-File-win.png)](https://osintops.com/)

**OsintOps Blog**

**OsintOps is the blog dedicated to all news** **concerning OSINT (and more)**

* [OsintOps Blog](https://osintops.com/blog)
* [TG OsintLatest News](https://t.me/Osintlatestnews)
* [WA Channel](https://whatsapp.com/channel/0029Va8Mp4k30LKPs32ifa1Z)
* [X](https://twitter.com/OsintOpsProject)
* Mail
* [Github](https://github.com/SOsintOps/Argos)

![](data:image/svg+xml;base64...)

# Mastodon: alla ricerca di elefanti

[Nov 30, 2022](https://osintops.com/alla-ricerca-di-elefanti/)

—

by

[OsintTrapper](https://osintops.com/author/osinttrapper/)

in [intelligence](https://osintops.com/category/intelligence/), [social-network](https://osintops.com/category/social-network/)

Nelle ultime settimane un numero sempre maggiore di utenti ha abbandonato Twitter per passare ad un altro social network, [Mastodon](https://mastodon.it/).

Molti analisti, sia OSInt sia CTI, hanno iniziato a spostarsi in una delle molte varie istanze presenti.
Anche noi abbiamo iniziato a prendere confidenza con questo nuovo ambiente, con lo scopo di capire come effettuare attività di raccolta informazioni, ai fini di OSINT: questo ad esempio è [il mio profilo](https://infosec.exchange/%40ronin13).

Nel presente articolo condivideremo le prime nostre considerazioni, figlie di una brevissima osservazione fatta finora, ma propedeutiche a successive attività che potrebbero risultare molto interessanti.

## **La superficie d’attacco**

La prima riflessione che possiamo fare fin da subito riguarda il fatto che, come altri social network del genere, anche qui è possibile raccogliere parecchie informazioni sul conto degli utenti.

[Sinwindie](https://github.com/sinwindie), nel suo repository Github ha già predisposto la [scheda dedicata a Mastodon](https://github.com/sinwindie/OSINT/blob/master/Mastodon/Mastodon%20OSINT%20Attack%20Surface.pdf), nella quale indica le possibili superfici di attacco utili in caso di investigazioni OSINT.

![](data:image/svg+xml;base64...)

Sinwindie’s Mastodon Attack Surface

## I primi tool per la raccolta informazioni

Questi sono i primi script utili che stiamo testando online

E’ uno script javascript che permette di cercare i profili sulle istanze di Mastodon.

Lo potete trovare disponibile al seguente URL: <https://seintpl.github.io/imagstodon/>

Il suo funzionamento è piuttosto intuitivo: Inserito un nickname, verranno visualizzate le immagini profilo registrate da quell’utente, presente su un’istanza Mastodon.

![](data:image/svg+xml;base64...)

Ricerca dell’utente “Ajeje Brazorf”

Lo script Masto, sviluppato da [Osint Tactical](https://twitter.com/OSINT_Tactical), fornisce informazioni/intelligence sugli utenti di Mastodon.social e sulle istanze di fediverse (server).

<https://github.com/C3n7ral051nt4g3ncy/Masto>

[![workflow di Masto](data:image/svg+xml;base64...)](https://f.hubspotusercontent-eu1.net/hubfs/139496804/Imported_Blog_Media/201748872-60872350-3c70-4988-b3c0-31e3ca194a27.png)

workflow di Masto

Masto permette di:

* Trovare l’ID utente
* Trovare lo username tra piú istanze anche senza accedere al sistema
* Verificare se l’utente è un bot
* Verificare se l’account è un gruppo
* Verificare se l’account è bloccato
* Verificare se l’utente ha scelto di essere elencato nella directory del profilo
* Ottenere la data di creazione del profilo
* Ottenere il numero di follower e following
* Ottenere il numero di messaggi
* molto altro!

<https://github.com/jakecreps/tootfarm>
Uno strumento OSInt che raccoglie istanze fediverse dal federal feed di Mastodon e le salva per analisi future. (utile probabilmente per arricchire l’elenco utilizzato da Imagstodon).

## Comunità

La comunità di esperti Osint già presente in mastodon é piuttosto ricca.

[Qui](https://github.com/cipher387/OSINT-and-Cybersecurity-accounts-in-Mastodon) e [qui](https://github.com/nathanlesage/academics-on-mastodon) trovate molti analisti OSInt (e non) che potrebbe valere la pena seguire.

[intelligence](https://osintops.com/tag/intelligence/) [Social-network](https://osintops.com/tag/social-network/)

## Comments

### Leave a Reply [Cancel reply](/alla-ricerca-di-elefanti/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

[ ]  Save my name, email, and website in this browser for the next time I comment.

Δ

←[Previous:  The Anu₿itux Project](https://osintops.com/the-anubitux-project/)

[Next:  The Two Sides of AI: when humans choose which side they are on](https://osintops.com/the-two-sides-of-ai/)→

## OsintOps News Channel

## Latest Posts

* [![](data:image/svg+xml;base64...)](https://osintops.com/between-osint-music-and-anticensorship/)

  [The difficult detection in Art: between Osint, Music and (anti)censorship](https://osintops.com/between-osint-music-and-anticensorship/)

  by Alessandro Rella

  The difficult detection in Art: between Osint, Music and (anti)censorship. Journey through the hidden meanings of words, both in art and anti-censorship, and on the difficulties of making OSINT in languages and cultures other than one’s own.
* [![](data:image/svg+xml;base64...)](https://osintops.com/tra-osint-musica-e-anticensura/)

  [La difficile detection nell’Arte: tra Osint, Musica e (anti)censura](https://osintops.com/tra-osint-musica-e-anticensura/)

  by Alessandro Rella

  La difficile detection nell’Arte: tra Osint, Musica e (anti)censura. Viaggio tra i significati nascosti delle parole, sia nell’arte che nella lotta alla censura e sulle difficoltà di fare OSINT in lingue e culture diverse dalla propria.
* [![](data:image/svg+xml;base64...)](https://osintops.com/enterprise-incident-response-with-velociraptor-when-tempo-is-all/)

  [Enterprise Incident Response with Velociraptor: when tempo is all](https://osintops.com/enterprise-incident-response-with-velociraptor-when-tempo-is-all/)

  by Alessandro Rella

  On the occasion of Matera DigiSec 2024, I decided to illustrate a tool that is still little known (unfortunately!) but instead is part of the tools of many Incident Response teams and perhaps deserves more prominence.
  I am talking about the opensource tool Velociraptor, on which I based my short talk, entitled “Enterprise Incident Response with Velociraptor: when time is all.”
* [![](data:image/svg+xml;base64...)](https://osintops.com/enterprise-incident-response-with-velociraptor-ita/)

  [Enterprise Incident Response with Velociraptor: when tempo is all](https://osintops.com/enterprise-incident-response-with-velociraptor-ita/)

  by Alessandro Rella

  In occasione del Matera DigiSec 2024 ho deciso di illustrare un tool ancora poco conosciuto (purtroppo!) ma che invece fa parte degli strumenti di molti team di Incident Response e che forse meriterebbe maggior rilievo.
  Sto parlando del tool opensource Velociraptor, sul quale ho basato il mio breve intervento, dal titolo “Enterprise Incident Response with Velociraptor: when tempo is all”.
* [![](data:image/svg+xml;base64...)](https://osintops.com/first-presentation-of-the-anuitux-project/)

  [First Presentation of the Anu₿itux Project](https://osintops.com/first-presentation-of-the-anuitux-project/)

  by Alessandro Rella

  Anubitux Project presented for the absolute first time the open-source distribution Anubitux, during the Cyber forensics IISFA Forum 2024, in Rome

## Popular Categories

* [AI](https://osintops.com/category/ai/) (1)
* [Anubitux](https://osintops.com/category/anubitux/) (2)
* [Argos](https://osintops.com/category/argos/) (3)
* [ArgosVM](https://osintops.com/category/argosvm/) (2)
* [Bazzell](https://osintops.com/category/bazzell/) (1)
* [Bitcoin](https://osintops.com/category/bitcoin/) (23)
* [blockchain](https://osintops.com/category/blockchain/) (10)
* [btcrecover](https://osintops.com/category/btcrecover/) (2)
* [Buscador](https://osintops.com/category/buscador/) (2)
* [Censorshi...