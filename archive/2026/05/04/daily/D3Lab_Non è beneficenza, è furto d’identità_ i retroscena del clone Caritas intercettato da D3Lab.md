---
title: Non è beneficenza, è furto d’identità: i retroscena del clone Caritas intercettato da D3Lab
url: https://www.d3lab.net/non-e-beneficenza-e-furto-didentita-i-retroscena-del-clone-caritas-intercettato-da-d3lab/
source: D3Lab
date: 2026-05-04
fetch_date: 2026-05-05T05:04:15.076288
---

# Non è beneficenza, è furto d’identità: i retroscena del clone Caritas intercettato da D3Lab

[![D3Lab](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2019/04/D3Lab_Logo_Enfold-300x102.png?fit=300%2C102&ssl=1 "D3Lab_Logo_Enfold-300×102")](https://www.d3lab.net/ "D3Lab_Logo_Enfold-300×102")

* [Home](https://www.d3lab.net/)
* [Services](/#services)
* [Philosophy](/#philosophy)
* [Contact](/#contact)
* [Blog](https://www.d3lab.net/blog/)
* [Fare clic per aprire il campo di ricerca
  Fare clic per aprire il campo di ricerca

  Cerca](?s= "Fare clic per aprire il campo di ricerca")
* **Menu**
  Menu

* [Collegamento a X](https://twitter.com/D3LabIT "Collegamento a X")
* [Collegamento a LinkedIn](https://www.linkedin.com/company/d3labsrl/ "Collegamento a LinkedIn")
* [Collegamento a Rss questo sito](https://www.d3lab.net/feed/ "Collegamento a Rss  questo sito")
* [Collegamento a Mail](/#contact "Collegamento a Mail")

# Non è beneficenza, è furto d’identità: i retroscena del clone Caritas intercettato da D3Lab

[Brand Monitor](https://www.d3lab.net/category/brand-monitor/), [Phishing](https://www.d3lab.net/category/phishing/)

[![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/05/Screenshot-2026-05-04-alle-10.03.42.png?resize=1039%2C423&ssl=1)](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/05/Screenshot-2026-05-04-alle-10.03.42.png?fit=1030%2C694&ssl=1 "Non è beneficenza, è furto d’identità: i retroscena del clone Caritas intercettato da D3Lab")

Il Threat Intelligence Team di D3Lab, grazie al servizio di Brand Monitor ha intercettato un pericoloso clone malevolo che punta a truffare i cittadini proponendosi come la Caritas Italiana. Nel panorama del cybercrime, si tratta di una delle tattiche più spregevoli: lo sciacallaggio digitale, ovvero lo sfruttamento della fiducia riposta in istituzioni caritatevoli per colpire le fasce più vulnerabili della popolazione.

La **[Caritas Italiana](https://www.caritas.it/)** è l’organismo pastorale della Conferenza Episcopale Italiana (CEI) che promuove la testimonianza della carità, sostenendo e coordinando oltre 200 Caritas diocesane. Si dedica ad aiutare i poveri e gli emarginati, promuovere il volontariato, sensibilizzare la comunità sui bisogni sociali e intervenire in emergenze nazionali e internazionale.

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/05/Screenshot-2026-05-04-alle-10.03.42.png?resize=1030%2C694&ssl=1)

### Profilazione ed Ingegneria Sociale

Come sopra riportato, il sito fraudolendo è stato individuato attraverso il servizio di Brand Monitor e non è al momento noto il vettore di attacco ma è ipotizzabile che attraverso un link contenuto in una email o via sms gli utenti raggiungano la home page del sito fraudolento dove viene promessa una falsa “Assistenza Finanziaria di €”. In questa fase il portale richiede l’inserimento del numero di telefono e della città di residenza della vittima così da fargli credere di trovarsi a far fronte ad un’operazione lecita.

### Esfiltrazione Documenti

Il cuore dell’attacco risiede proprio nel furto d’identità, suddiviso in 2 passaggi.

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/05/Screenshot-2026-05-04-alle-10.09.25_offuscato.png?resize=965%2C775&ssl=1)
![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/05/Screenshot-2026-05-04-alle-10.11.05_offuscato.png?resize=968%2C767&ssl=1)

* **Caricamento Passaporto** ( `/front.php`) : il sistema richiede una foto nitida del passaporto aperto, fornendo istruzioni precise su illuminazione e leggibilità in modo così da assicurarsi che i dati siano utilizzabili
* **Caricamento Codice Fiscale** ( `/selfie.php`) : la pagina richiede la scansione della Tessera Sanitaria, prendendo sempre le stesse accortezze descritte precedentemente.

### Validazione

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/05/Screenshot-2026-05-04-alle-10.28.53.png?resize=969%2C767&ssl=1)

Dopo il caricamento dei documenti, il file `/done.php` mostra una barra che simula l’elaborazione della domanda, invitando l’utente ad attendere 1-2 minuti.

Per massimizzare la portata della frode, il sito implementa anche un meccanismo di ingegneria sociale che sprona l’utente a invitare amici o familiari per accelerare la revisione della propria pratica, promettendo una maggiore priorità nell’invio dei fondi. A tal fine Il sistema fornisce un link di condivisione che utilizza una tecnica di offuscamento tramite url:

`hxxps://cariitas[.]it/?pixel=123456789&ref=true`.

Questo dominio contraffatto sfrutta il typosquatting ( doppia i nel nome ) per indurre i contatti della vittima a credere che il link provenga dal sito ufficiale della Caritas, amentandone la pericolosità vista la catena di condivisioni che si potrebbe venire a creare.

### Phishing Finanziario

Una volta comunicata la falsa accettazione della domanda, l’utente visualizza un messaggio di conferma con un logo Paypal.

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/05/Screenshot-2026-05-04-alle-10.31.34.png?resize=971%2C764&ssl=1)

Cliccando sul logo, avviene il redirect verso la parte dedicata al furto delle credenziali.

**Finto Portale Paypal**

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/05/Screenshot-2026-05-04-alle-10.43.02.png?resize=964%2C772&ssl=1)

Una pagina di login contraffatta che imita il canale ufficiale di paypal per catturare email e password delle vittime.

Una volta inserite le credenziali, l’endpoint `secure.php` gestisce l’esfiltrazione finale trattenendo l’utente con un finto messaggio di elaborazione dati.

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/05/Screenshot-2026-05-04-alle-10.45.16.png?resize=965%2C772&ssl=1)

L’analisi di questo caso mette in luce non solo la complessità tecnica dei criminali, ma anche la loro totale assenza di scrupoli: colpire chi si trova in difficoltà, usando come esca la solidarietà, rappresenta uno dei punti più bassi dello sciacallaggio digitale.

In D3Lab crediamo che fare sicurezza significhi soprattutto fare informazione. Documentare e denunciare pubblicamente questi casi è il nostro modo di fornire agli utenti gli strumenti necessari per riconoscere le frodi online.

**Come di consueto, invitiamo tutti gli utenti a prestare la massima attenzione. È fondamentale non cliccare su link sospetti ricevuti via SMS o e-mail e non divulgare mai le proprie informazioni sensibili (come username, password, indirizzo e-mail, telefono, etc.)**

**Questo articolo è redatto a scopo divulgativo e a tutela dei consumatori dal Cyber Threat Intelligence Team di D3Lab**

### **IoC**

* `hxxps://pass-caritas[.]online`
* `hxxps://dl-caritas[.]online`
* `hxxps://pass-caritas[.]online/front.php`
* `hxxps://pass-caritas[.]online/selfie.php`
* `hxxps://cariitas[.]it/?pixel=123456789&ref=true`
* `hxxps://pass-caritas[.]online/done.php`
* `hxxps://paypal[.]italy-help/`
* `hxxps://paypal[.]italy-helo/secure.php`

4 Maggio 2026/da [Francesco D3Lab](https://www.d3lab.net/author/francesco-s/ "Articoli scritti da Francesco D3Lab")

##### Condividi questo articolo

* [Condividi su Facebook](https://www.facebook.com/sharer.php?u=https://www.d3lab.net/non-e-beneficenza-e-furto-didentita-i-retroscena-del-clone-caritas-intercettato-da-d3lab/&t=Non%20%C3%A8%20beneficenza%2C%20%C3%A8%20furto%20d%E2%80%99identit%C3%A0%3A%20i%20retroscena%20del%20clone%20Caritas%20intercettato%20da%20D3Lab)
* [Condividi su X](https://twitter.com/share?text=Non%20%C3%A8%20beneficenza%2C%20%C3%A8%20furto%20d%E2%80%99identit%C3%A0%3A%20i%20retroscena%20del%20clone%20Caritas%20intercettato%20da%20D3Lab&url=https://wp.me/p7upL6-1An)
* [Condividi su WhatsApp](https://api.whatsapp.com/send?text=https://www.d3lab.net/non-e-beneficenza-e-furto-didentita-i-retroscena-del-clone-caritas-intercettato-da-d3lab/)
* [Condividi su Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.d3lab.net%2Fnon-e-beneficenza-e-furto-didentita-i-retroscena-del-clone-caritas-intercettato-da-d3lab%2F&description=Non%20%C3%A8%20beneficenza%2C%20%C3%A8%20furto%20d%E2%80%99identit%C3%...