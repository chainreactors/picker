---
title: MICROSOFT DOWN: se siamo dipendenti da un servizio straniero, siamo DAVVERO sovrani?
url: https://mgpf.it/2026/11/13/microsoft-down-sovranita.html
source: LastKnight.com Feed
date: 2026-11-13
fetch_date: 2026-11-14T08:21:37.216799
---

# MICROSOFT DOWN: se siamo dipendenti da un servizio straniero, siamo DAVVERO sovrani?

[![Matteo Flora](https://mgpf.it/wp-content/uploads/2022/07/MatteoFlora.thinks-1.png)](https://mgpf.it/)

* [CHI SONO](https://matteoflora.com/)
* [English](https://en.mgpf.it/)

# MICROSOFT DOWN: se siamo dipendenti da un servizio straniero, siamo DAVVERO sovrani?

In [business](https://mgpf.it/category/business), [politics](https://mgpf.it/category/politics), [security](https://mgpf.it/category/security)

12 ore ago

16 min

M

![](https://mgpf.it/wp-content/uploads/2026/11/fax_small-1024x512.jpg)

### Il giorno in cui mezzo mondo è tornato alla carta

Venerdì 13 novembre 2026, a Tokyo, il vicesegretario capo di gabinetto **Masanao Ozaki** spiega in conferenza stampa che i dipendenti del governo giapponese stanno rispondendo al guasto **producendo copie fisiche dei documenti**, come riporta la [CNN](https://edition.cnn.com/2026/11/12/business/live-news/microsoft-global-outage-intl-hnk). Nelle stesse ore in Irlanda l’HSE, il servizio sanitario nazionale (*Health Service Executive*), chiede a medici di base e farmacisti di **tornare alle ricette di carta**, perché la posta sanitaria non viaggia più ([RTÉ](https://www.rte.ie/news/business/2026/1113/1599061-microsoft-tech-outage/)), mentre l’elenco dei colpiti compilato da [Al Jazeera](https://www.aljazeera.com/news/2026/11/13/microsoft-hit-by-global-outages-what-happened-and-why) arriva all’agenzia di intelligence e alla polizia federale australiane e alla Corte suprema delle Filippine. In Australia, racconta [The Register](https://www.theregister.com/saas/2026/11/13/microsofts-massive-m365-outage-stretches-past-20-hours-as-its-fixes-keep-failing/5309609), lo chiamano già *«il lungo weekend di Microsoft»*.

La frase che riassume la giornata meglio di qualunque comunicato la raccoglie però, da un ufficio condiviso in Germania, un altro giornalista di [The Register](https://www.theregister.com/saas/2026/11/13/microsoft-outage-gives-customers-a-crash-course-in-dependence-on-redmond/5309805): *«l’amore della Germania per il fax: finalmente è il nostro momento di brillare! I colleghi britannici non possono mandare mail, noi siamo tornati al modo naturale, il fax»*.

Anche da noi il conto arriva, per fortuna leggero: Regione Lombardia deve precisare con una nota che negli ospedali lombardi il problema ha toccato **soltanto la posta elettronica** delle strutture che usano i sistemi Microsoft, senza conseguenze sulle cure ([MilanoToday](https://www.milanotoday.it/cronaca/microsoft-down-outlook-teams-aziende-milano-13-novembre-2026.html)). Se mettete in fila queste scene vedete un pezzo di mondo ricco, digitale e orgoglioso delle sue infrastrutture che nel giro di una giornata torna al Novecento, perché **un solo fornitore, con sede in un solo Paese, ha avuto un problema**. Conviene partire da qui, perché la domanda che il guasto lascia sul tavolo riguarda molto poco la qualità del software di Redmond e moltissimo **chi decide se il nostro ufficio è acceso o spento**, e se quella persona siamo ancora noi. In questo pezzo chiamo sovranità proprio questo, la capacità di tenere acceso il proprio ufficio anche quando qualcun altro, altrove, decide o sbaglia.

### Un guasto normale, e proprio per questo istruttivo

Il guasto comincia la sera di giovedì 12 novembre 2026, ora italiana: cade Exchange Online, cioè la posta aziendale ospitata nella nuvola di Microsoft, Outlook e Teams vanno a singhiozzo e Copilot *(l’assistente che doveva lavorare al posto nostro, per inciso)* si ferma con loro. Secondo i dati di Downdetector citati dalla CNN, le segnalazioni arrivano da **74 Paesi e territori nel giro di circa un’ora**. La prima spiegazione dell’azienda è quasi poetica nella sua vaghezza, un problema per cui *«i server non superano i controlli automatici di funzionamento e risultano non disponibili»*; poco dopo arriva l’ammissione che *«le azioni intraprese finora non hanno dato il sollievo previsto»*, e il venerdì pomeriggio The Register conta **oltre venti ore** di servizio degradato.

Già nella notte Charles Lamanna, vicepresidente esecutivo di Microsoft per Copilot, agenti e piattaforma, esclude su X qualsiasi attività malevola, e il ministro degli Interni australiano Tony Burke paragona la situazione a **CrowdStrike**, l’aggiornamento andato storto che nel luglio 2024 aveva piantato milioni di computer Windows *(chi c’era si ricorda le schermate blu negli aeroporti: [video.matteoflora.com/1292](https://video.matteoflora.com/1292))*. La causa la dichiara poi Microsoft stessa il 13 novembre: un difetto introdotto **durante un precedente potenziamento della capacità di rete**, rimasto lì in silenzio finché **una modifica più recente non lo ha fatto emergere**. Segue la formula di rito, *«siamo profondamente dispiaciuti»*, con la promessa di un rapporto dettagliato a incidente chiuso.

A questo punto la tentazione è indignarsi, e secondo me è sbagliata. Chi, come me, ha passato i primi dieci anni di lavoro a programmare macchine sa che **i sistemi grandi si rompono**, e che spesso si rompono nei modi più banali. Il sociologo **Charles Perrow** ci ha costruito sopra un classico, *Normal Accidents: Living with High-Risk Technologies* (1984) *(gran libro davvero, se non l’avete, andate a prendervelo: [eccolo](https://www.amazon.it/dp/0691004129?tag=mgpf-21))*, nato dall’incidente nucleare di Three Mile Island del 1979: quando un sistema è insieme **complesso**, cioè fatto di parti che interagiscono in modi che nessuno ha previsto né riesce a vedere, e **ad accoppiamento stretto**, cioè senza margini né tempi morti tra un passaggio e l’altro, l’incidente smette di essere un’eccezione e diventa una proprietà del sistema, tanto che Perrow lo chiama appunto *normale*. C’è poi un dettaglio che nel guasto di giovedì si vede benissimo: in quei sistemi **i dispositivi di sicurezza diventano parte del problema**. I controlli automatici che dovevano togliere dal servizio i server malati li hanno tolti davvero, il traffico si è riversato sugli altri e gli altri sono crollati sotto il carico, come ha spiegato ad Al Jazeera Walter Pasquarelli, ricercatore della Bennett School of Public Policy di Cambridge, con l’immagine di un’autostrada che perde corsie e intasa quelle che restano.

L’immagine che preferisco è più domestica, ed è la presa unica. Attaccate tutto alla stessa presa, il forno, la lavatrice, il computer e il caricatore del telefono, e funziona benissimo finché un elettrodomestico fa i capricci; a quel punto scatta l’interruttore generale e **la casa resta al buio tutta insieme**, e la colpa è della presa unica prima che del forno. **Preso da solo, il guasto è la nuova normalità**, e con la normalità si convive: è successo a Facebook, Instagram e WhatsApp tutti insieme nell’ottobre 2021 *(con mezzo mondo convinto che fosse un attacco: [video.matteoflora.com/898](https://video.matteoflora.com/898))*, è successo con CrowdStrike, è successo a Cloudflare per un file diventato troppo grosso *(niente hacker nemmeno lì: [video.matteoflora.com/1490](https://video.matteoflora.com/1490))*, succederà di nuovo a qualcun altro, e chi vi promette una nuvola che non cade mai vi sta vendendo qualcosa.

### Settanta su cento, e lo scrive la Commissione

Il problema comincia quando si guarda chi c’è dall’altra parte di quella presa. Il 3 giugno 2026 la Commissione europea ha presentato la proposta di **Cloud and AI Development Act**, il regolamento europeo sullo sviluppo del cloud e dell’intelligenza artificiale che tutti chiamano CADA ([COM(2026) 502](https://www.eerstekamer.nl/nonav/bijlage/20260609/com_2026_502_proposal_for_a/document3/f%3D/vmy8optarooc.pdf)), e nella relazione che l’accompagna mette in fila tre affermazioni che conviene leggere una dopo l’altra. La quota di mercato dei fornitori europei di cloud **è scesa dal 29% del 2017 al 15% del 2022**, e da allora è rimasta ferma; alla data della proposta **tre grandi fornitori non europei controllano oltre il 70% del mercato europeo del cloud** *(gli hyperscaler, parola che vuo...