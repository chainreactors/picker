---
title: A chi appartiene il forum accusato di “revenge porn”? Una ricerca OSINT
url: https://lorenzoromani.medium.com/a-chi-appartiene-il-forum-accusato-di-revenge-porn-phica-net-una-ricerca-osint-b0ae04fe9563
source: Over Security - Cybersecurity news aggregator
date: 2025-09-01
fetch_date: 2025-10-02T19:29:22.685092
---

# A chi appartiene il forum accusato di “revenge porn”? Una ricerca OSINT

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fb0ae04fe9563&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderUser&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Florenzoromani.medium.com%2Fa-chi-appartiene-il-forum-accusato-di-revenge-porn-phica-net-una-ricerca-osint-b0ae04fe9563&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Florenzoromani.medium.com%2Fa-chi-appartiene-il-forum-accusato-di-revenge-porn-phica-net-una-ricerca-osint-b0ae04fe9563&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

# A chi appartiene il forum accusato di “revenge porn”? Una ricerca OSINT

[![Lorenzo Romani](https://miro.medium.com/v2/resize:fill:64:64/1*Ja0-L3zlWun6qaI5RYR3Aw.jpeg)](/?source=post_page---byline--b0ae04fe9563---------------------------------------)

[Lorenzo Romani](/?source=post_page---byline--b0ae04fe9563---------------------------------------)

9 min read

·

Mar 12, 2025

--

1

Share

Qualche anno fa mi interessai ([link](/il-network-della-prostituzione-corre-sul-web-86e28a7c026e)) al sito di annunci erotici ***bakecaincontrii.com*** ipotizzando, con l’ausilio di tecniche di *network analysis*, la verosimile esistenza di un network interregionale preposto allo sfruttamento della prostituzione. Nel 2023 il sito è stato al centro di [indagini](https://bari.corriere.it/notizie/cronaca/23_marzo_24/il-sito-di-incontri-frodava-il-fisco-sequestrati-32-milioni-di-euro-c590480e-94e6-426e-bb57-ec2471b7bxlk.shtml) per evasione fiscale, con sequestri per circa 23 milioni di euro. Oggi prendiamo spunto da una denuncia meritoriamente pubblicata dall’ex collega @valeriolilli per dimostrare come le tecniche investigative da fonti aperte (*OSINT*) consentano di desumere informazioni di rilievo per identificare i possibili *beneficial owner* (o talune “parti correlate”) di ***phica.net***, forum frequentato da una platea di ‘addetti ai lavori’ sul quale, secondo il collega, sono talvolta pubblicati dati sensibili, a sfondo sessuale, appartenenti a vittime ignare (c.d. “*revenge porn*”).

Il sito si presenta con un’interfaccia grafica piuttosto basilare ma denota un rilevante numero di *thread* e utenti attivi. Benché l’obiettivo della ricerca non sia l’analisi dei contenuti, rimango colpito da una discussione intitolata “**Scambio foto su Telegram in segreta! LEGGERE TUTTI**”, nella quale l’amministratore “**PhicaMaster**” invita gli utenti ad utilizzare un gruppo Telegram privato per lo scambio di contenuti espliciti.

Press enter or click to view image in full size

![]()

Lo scopo dell’esercizio è acquisire informazioni e formulare ipotesi sull’identità dei soggetti interessati nella proprietà e gestione dell’asset. Il compito, *prima facie*, non sembra immediato. Lo stesso **Garante della Privacy**, in un [provvedimento](https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/9964907) risalente al 28 settembre 2023, ingiungeva a *phica.net* l’adozione di misure volte a fermare la diffusione del materiale segnalato. Siccome il Garante si limitò a identificare ‘*Phica.net*’ (e non l’entità che lo amministra) quale destinatario del provvedimento, si ipotizza che l’Autorità non fosse riuscita a identificare con certezza la persona giuridica o la persona fisica cui indirizzare la comunicazione.

![]()

Avviamo quindi un ciclo di analisi strutturato per verificare se sia possibile, con l’ausilio di sole fonti aperte, attribuire la titolarità della piattaforma, identificare soggetti ad essa ipoteticamente collegati, o formulare ipotesi in tal senso.

Atteso che il sito web non fornisce alcuna indicazione sul titolare del trattamento nelle sezioni usualmente adibite, il primo passo è la verifica dei dati di ***Whois*** (attuali e storici) inerenti il dominio ***phica.net*** e il dominio ‘gemello’ ***phica.eu***. L’adozione, in prima istanza di registrazione, di servizi di *whois privacy*, preclude l’acquisizione di informazioni univoche (nomi di persona, numeri di telefono, indirizzi e-mail) sul conto dell’amministratore di ***phica.net***. Analogamente, la consultazione del Whois di ***phica.eu*** restituisce un indirizzo e-mail (*phicamaster@phica.net*) non utile ai fini dell’analisi.

Procediamo quindi con la mappatura preliminare dell’infrastruttura fisica (*server*) che ospita la piattaforma. L’indirizzo IP della macchina risulta essere **104.21.91.82:**

![]()

Anche in questo caso, l’informazione non è utile ai fini della ricerca, atteso che l’IP rilevato fa riferimento alla CDN (“*Content Delivery Network*”) di **Cloudflare**: l’indirizzo IP non è quello identificante il “server fisico” che ospita l’asset, rappresentando piuttosto una mera interfaccia virtuale interposta all’effettiva identificazione della macchina ospitante.

L’adozione dei *layer* di protezione/anonimato forniti da Cloudflare può rappresentare un rilevante fattore di impedimento rispetto alla conoscibilità dell’indirizzo IP reale, dalla quale dipende spesso la possibilità di percorrere step analitici successivi al fine di mappare ulteriori proprietà digitali ed espandere il perimetro d’indagine.

Nel caso che qui ci occupa, un indirizzo IP realmente collegato a *phica.net* è comunque acquisibile con (almeno) due tecniche differenti.

**A)** Consultazione di un motore di ricerca IoT (“*Internet of Things*”)

La ricerca effettuata su **Censys** tramite mera immissione della stringa “*phica.net*” ci consente di acquisire diversi indirizzi IP non appartenenti alla CDN di Cloudflare ma collegati all’infrastruttura web di nostro interesse:

Press enter or click to view image in full size

![]()

Notiamo che gli indirizzi IP fanno riferimento al provider di servizi di hosting OVH (Francia).

**B)** Ricezione di una mail dal dominio *phica.net*

La registrazione, con un account di posta creato *ad-hoc*, al sito ***phica.net***, ci permette di ricevere una **mail di verifica dell’account**. L’analisi dell’*header* (intestazione) della mail rivela che l’indirizzo IP del server di posta mittente (*mail server*) è **178.32.141.187**, annoverato fra quelli censiti dal motore di ricerca IoT:

![]()

Abbiamo quindi tracciato un collegamento forte fra il dominio *phica.net* e le infrastrutture informatiche dell’hosting provider OVH presso una serie di indirizzi IP, fra cui **178.32.141.187.**

L’acquisizione di queste informazioni consentirebbe all’Autorità Giudiziaria di avviare procedure di rogatoria internazionale per ottenere dati sull’identità del sottoscrittore del contratto di hosting con OVH.

Sospendiamo momentaneamente le verifiche ricorsive sugli indirizzi IP e tentiamo di esperire percorsi investigativi più snelli ed immediati.

Si prospettano alcune strade:

1. Analisi del codice sorgente del sito web *phica.net*
2. Analisi dei certificati SSL del dominio *phica.net* con finalità di *subdomain discovery*

**Analisi del codice sorgente**

Con questo step di verifica ottengo un codice di tracciamento Google Analytics utilizzato per monitorare le prestazioni (accessi/page views, etc) del sito web. Il codice è rintracciabile cercando la stringa ‘UA-’ all’interno del codice HTML della home page:

![]()

Possiamo utilizzare ric...