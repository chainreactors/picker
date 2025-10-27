---
title: I nuovi Pos sono a rischio violazione
url: https://www.wired.it/article/nuovi-pos-rischio-violazione/
source: Instapaper: Unread
date: 2024-10-19
fetch_date: 2025-10-06T18:56:53.853958
---

# I nuovi Pos sono a rischio violazione

[Skip to main content](#main-content)

Apri il menu di navigazione

Menu

[![Wired Italia](/verso/static/wired-us/assets/logo-header.svg)](/)

I nuovi Pos sono a rischio violazione

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

[Marco Schiaffino](/contributor/marco-schiaffino/)

[Security](/security/)

18.10.2024

# I nuovi Pos sono a rischio violazione

Una vulnerabilità nei dispositivi basati su Android permette di sottrarre tutte le informazioni che consentono di clonare carte di credito e Bancomat

![Unrecognizable people making an online payment. Anonymous man is holding a card machine while the other person is...](https://media-assets.wired.it/photos/6711321b212f6609a0f45822/16:9/w_2560%2Cc_limit/1447777322)

Unrecognizable people making an online payment. Anonymous man is holding a card machine while the other person is placing their phone to pay.miniseries

Una catena di vulnerabilità che permetterebbero di sottrarre le informazioni di carte di credito e Bancomat sui POS basati su sistema operativo Android. A individuarle è stato Jacopo Jannone, un **ingegnere informatico e penetration tester italiano** che illustrerà la sua ricerca nel corso di un talk al No Hat 2024, la sesta edizione del convegno organizzato da Berghem-in-the-Middle che si terrà il prossimo sabato 19 ottobre al Centro Congressi Giovanni XXIII - Viale Papa Giovanni XXIII 106.

## L’anello debole dei pagamenti digitali

La digitalizzazione dei pagamenti rappresenta un indubbio salto di qualità a livello tecnologico, ma anche sociale. I pagamenti su digitale non solo contribuiscono a **ridurre il fenomeno dell’evasione fiscale**, ma hanno anche un impatto positivo sull’ambiente. Nel nord Europa, per esempio, capita spesso di incappare in locali e negozi che **permettono solo pagamenti tramite carta di credito e Bancomat**, considerati più “ecologici” rispetto ai contanti, la cui produzione (e distribuzione) impatta sull’ambiente.

Il lato negativo, però, è quello legato alla possibilità che le transazioni vengano intercettate o che **le informazioni delle carte siano sottratte e utilizzate per clonarle**. Una tecnica che passa sotto il nome di skimming, ma che prevede normalmente tecniche piuttosto artigianali, come l’uso di videocamere per riprendere la digitazione del PIN nel momento in cui viene utilizzata la carta. La tecnica individuata da Jacopo Jannone, invece, ha le caratteristiche di un classico attacco hacker e permette di attingere alle informazioni direttamente dalla fonte.

## Quando i POS sono troppo “smart”

Alla base della vulnerabilità ci sono le caratteristiche dei nuovi Smart POS (Point Of Sale) che, lentamente ma inesorabilmente, stanno rimpiazzando i vecchi dispositivi che siamo abituati a utilizzare nei punti vendita.

“I vecchi dispositivi con tastierino e display a cristalli liquidi hanno funzionalità limitate e una struttura molto semplice” spiega Jacopo Jannone. “Le nuove generazioni di POS sono invece dei **dispositivi molto simili a un qualsiasi smartphone**. Questo significa che hanno un sistema operativo Android e, in particolare, permettono livelli di interazione molto più complessi, per esempio il collegamento tramite usb. Sono proprio queste caratteristiche che **aumentano a dismisura la superficie di attacco** di un eventuale cyber criminale”.

Insomma: l’evoluzione dei dispositivi dedicati ai pagamenti, oltre a fornire nuove funzionalità e una maggiore versatilità, espongono a un maggiore rischio. Nel caso specifico, consentirebbero di **modificare il funzionamento dello Smart POS** per fare in modo che le informazioni memorizzate all’interno della carta siano inviate automaticamente a un cyber criminale.

## Un hacking “fisico” per rubare i dati: gli scenari di un possibile attacco

Fortunatamente, le vulnerabilità individuate da Jannone non possono essere sfruttate in remoto. “Per compromettere il POS è necessario avere **accesso fisico al dispositivo**” spiega il ricercatore. Una buona notizia, che però lascia campo aperto a varie ipotesi di sfruttamento delle vulnerabilità. Il primo è che la “modifica” nel software del dispositivo venga fatta **direttamente dall’operatore del POS**. Con quali vantaggi? Per esempio la possibilità di clonare un Bancomat e poterlo utilizzare a proprio piacimento.

“La maggior parte delle informazioni che identificano carte di credito e Bancomat, come il numero di serie e la data di scadenza, sono visibili sulla carta stessa e, di conseguenza, potrebbero essere sottratti senza troppi problemi anche con strumenti ‘analogici’, per esempio una semplice fotografia” spiega Jannone. “Le cose cambiano per quanto riguarda il PIN. La catena di vulnerabilità che ho individuato permette infatti di registrarlo nel momento in cui viene digitato”.

Uno scenario ulteriore è quello di un attore malevolo che riesca, in qualche modo, a **modificare i dispositivi intervenendo nella filiera di consegna dei POS stessi**. In questo caso non sarebbe necessario il coinvolgimento dell’esercente, ma il furto di informazioni sarebbe comunque garantito e, potenzialmente, su vasta scala.

“Nel Proof of Concept che ho realizzato il collegamento per sottrarre i dati richiede un collegamento alla stessa rete wi-fi del dispositivo” specifica Jannone. “Non è escluso, però, che sia possibile mettere a punto varianti dell’attacco che consentano una trasmissione via web”.

## Le storie da non perdere di Wired

* È iniziato a Rovereto il Wired Next Fest Trentino. Incontri, eventi, workshop e attività per parlare di innovazione, tecnologie e delle “energie” che ci servono fino al 5 ottobre. Per partecipare ai talk e interviste, [iscriviti sul sito dedicato o segui la diretta live!](https://eventi.wired.it/nextfest25-trentino/)
* ⛵️ Come seguire la missione della [Global Sumud Flotilla](https://www.wired.it/topic/global-sumud-flotilla), la flotta umanitaria diretta a Gaza
* 🔌 È in edicola il nuovo numero di *Wired* che parla di energia. [Abbonati!](https://abbonatiqui.it/rivista/wired)
* ❗️Il caso di Alberto Trentini, il cooperante in carcere in Venezuela da novembre 2024: [le notizie per non spegnere l'attenzione](https://www.wired.it/topic/alberto-trentini/) e chiederne l'immediata liberazione
* 🇺🇦 Le condizioni per un accordo tra Ucraina e Russia e [gli sviluppi del conflitto](https://www.wired.it/topic/ucraina/)
* 🇮🇱 🇵🇸 L'escalation [in Medio Oriente](https://www.wired.it/topic/israele/): cosa sta succedendo in [Israele](https://www.wired.it/topic/israele/) e la [crisi umanitaria a Gaza](https://www.wired.it/topic/striscia-di-gaza/)
* 🎤 [Leggi e guarda le interviste](https://www.wired.it/the-big-interview) agli ospiti di The Big Interview, il nuovo evento di Wired. [Anche su Youtube](https://www.youtube.com/%40wireditalia)
* 🎥 Le interviste, le video-news, i nostri reportage: [le notizie “da guardare”](https://www.wired.it/video/) di Wired
* ✍️ Vuoi ricevere comodamente a casa il magazine di Wired? [Abbonati qui](https://abbonatiqui.it/rivista/wired)
* 💬 Wired ha aperto il canale Whatsapp: [iscriviti subito!](https://www.wired.it/article/whatsapp-canali-wired/)
* 🛡️ Contro la violenza online, il [progetto Wired Safe Web](https://www.wired.it/topic/wired-safe-web/) offre strumenti di tutela e di consapevolezza
* 📺 Scopri i video di Wired: [seguici su YouTube](https://www.youtube.com/user/wireditalia)
* 📩 Scopri le nostre newsletter: le ultime su tecnologia, gadget, ambiente, salute e diritti. [Iscriviti subito](https://www.wired.it/newsletter-subscribe/)
* 🖥 Notizie,...