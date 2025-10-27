---
title: Statistiche dei siti / Website analytics
url: https://cavallette.noblogs.org/2025/02/9949
source: cavallette
date: 2025-02-26
fetch_date: 2025-10-06T20:47:52.257862
---

# Statistiche dei siti / Website analytics

# [cavallette](https://cavallette.noblogs.org/)

il blog di autistici.org

---

« [February 1st 2025, Global Switch day](https://cavallette.noblogs.org/2025/02/9937)

[Aggiornamenti per Noblogs/Updates to Noblogs](https://cavallette.noblogs.org/2025/04/9956) »

## Statistiche dei siti / Website analytics

[IT]

Autistici / Inventati ha offerto per molti anni un servizio di analisi del traffico sui siti ospitati, inizialmente nato per offrire un’alternativa centralizzata all’installazione autonoma di strumenti simili, con migliori garanzie di rispetto della privacy ed anonimato dei visitatori.

Questo è sempre stato un compromesso vagamente scomodo: questa tipologia di strumento (nel nostro caso [Piwik/Matomo](https://matomo.org/), la più diffusa implementazione open source) tenta di raccogliere statistiche accurate *lato client*, inserendo codice nelle pagine così da tracciare il comportamento del browser. Prassi intrusiva, condivisa infatti dal mondo dell’advertisement ed in sostanza una forma di tracciamento attivo del comportamento delle persone.

Ma il web di oggi non è più quello di allora, i browser offrono maggiore resistenza a questo tipo di tracciamento, la maggioranza dei nostri visitatori comunque utilizza ad blockers che ne prevengono il funzionamento. Il risultato è che i dati raccolti dal nostro sistema di statistiche sono ampiamente inaccurati, e dunque il compromesso di cui sopra non è più giustificato. Dunque **sospenderemo il servizio di analisi del traffico**così come è stato fornito finora (Piwik/Matomo).

Per chi gestisce un sito, è comunque importante avere una vaga idea dell’andamento delle visite, anche soltanto dal punto di vista volumetrico. Per questo abbiamo implementato un **nuovo servizio di analisi del traffico**, che al contrario del precedente:

* Opera sui log anonimizzati lato server, usando soltanto i parametri “pubblici” inviati dal browser (URL, User agent) per la classificazione del traffico
* Funziona automaticamente per tutti i siti ospitati, senza alcuna necessità di modificare le pagine per inserire codice
* Fornisce soltanto andamenti quantitativi del traffico suddivisi in poche categorie primarie (tipologia di browser, dispositivo mobile o desktop, traffico “umano” oppure “automatico”)

I dati di analisi del traffico sono disponibili:

* Per normali siti ospitati, sul Pannello Utente in corrispondenza del sito
* Per i blog su NoBlogs, tramite il menu “Analytics” nella dashboard del proprio blog

Se siete responsabili di un sito ospitato su A/I, ed avete implementato manualmente l’integrazione con stats.autistici.org, potete rimuoverla quando ne avete l’opportunità in modo da migliorare la performance del sito.

L’attuale servizio Matomo verrà disattivato nel corso delle prossime settimane.

[EN]

For many years, we’ve offered a centralized web traffic analytics service for hosted websites. We initially did this to avoid the proliferation of such self-hosted tools so that we could at least guarantee a good level of privacy and anonymity of the collected information. This has always been a bit of an uncomfortable compromise: these tools (such as [Piwik/Matomo](https://matomo.org), the implementation we’ve been using) collect data by instrumenting *the client*, injecting code in web pages to track the browser’s behavior. This is fundamentally an intrusive practice, a form of tracking, and it’s no coincidence that a lot of the same techniques are used by e.g. the advertisement industry.

The web, however, has changed quite a bit since then: today’s browsers give out less information, and the vast majority of our visitors are using ad blockers that (rightfully) prevent our analytics from working. The result is that the data collected by this service is largely inaccurate, to the extent that we feel the above compromise is no longer justified. As a consequence, we will **terminate the current web analytics service** in the form it has been operating until now (Piwik / Matomo).

Traffic statistics, even approximate, are in any case still very useful for those who manage websites, and we would still like to offer this capability, but in a less intrusive fashion. So, we are launching a **new web analytics service**, that operates on different principles:

* It works using anonymized server-side logs, using only the public information sent by the browser in its requests (URL, User Agent) in order to classify traffic
* It works automatically out of the box for all hosted websites, without requiring to add any code to the site pages themselves
* It only offers quantitative traffic data, sliced along few primary dimensions (browser type, device class, human vs automated traffic)

If you are hosting a website with us, this data will be available:

* Under the “Analytics” dashboard menu, for blogs hosted on NoBlogs
* On the main User Panel, for the other hosted websites

If you are managing a website hosted by A/I, and you have manually added the Piwik/ Matomo code to integrate with stats.autistici.org, you can remove it whenever you have the opportunity to do so, in order to improve the site’s performance slightly.

The existing Matomo service will be de-activated in the next few weeks.

This entry was posted on martedì, Febbraio 25th, 2025 at 10:28 am and is filed under [General](https://cavallette.noblogs.org/category/general). You can follow any responses to this entry through the [RSS 2.0](https://cavallette.noblogs.org/2025/02/9949/feed) feed.
Both comments and pings are currently closed.

Comments are closed.

* ## cavallette

  il blog collettivo di [autistici.org](https://www.autistici.org)
  discussioni su privacy, anonimato,
  liberta’ digitali e non.
* Search for:
* ## +KAOS

  10 anni di hacking e mediattivismo
   il libro di autistici/inventati
   [![](/files/2012/04/ai-book-copertina.png)](https://www.autistici.org/who/book)
  ![](/files/2017/10/ai-book-cover-en-web.jpg)
* ## Categorie

  Categorie
  Seleziona una categoria
  Analogic\_Revenge
  antifascismo
  Appuntamenti
  Avvisi
  Babau
  Comunicati
  Cronache\_Terrestri
  Cyber\_Rights
  DailyHacking
  Downtime
  Ecology
  General
  Generale
  hacks
  home page
  Maintenance
  Manutenzione
  migliorie
  newsletter
  Nuovi\_Arrivi
  Paranoia
  Piano\_R
  Problemi\_Tecnici
  Questioni\_legali
  Tech\_Hype
  Web\_Surfing
* ## Articoli recenti

  + [Ancora problemi con un server / Server issue, again](https://cavallette.noblogs.org/2025/08/10006)
  + [Problemi con un server / Server issues](https://cavallette.noblogs.org/2025/08/10000)
  + [For italian workers](https://cavallette.noblogs.org/2025/05/9994)
  + [Manutenzione / Maintenance](https://cavallette.noblogs.org/2025/05/9990)
  + [Aggiornamenti per Noblogs/Updates to Noblogs](https://cavallette.noblogs.org/2025/04/9956)
  + [Statistiche dei siti / Website analytics](https://cavallette.noblogs.org/2025/02/9949)
  + [February 1st 2025, Global Switch day](https://cavallette.noblogs.org/2025/02/9937)
  + [Newsletter Autistici/Inventati – 2024](https://cavallette.noblogs.org/2024/12/9933)
  + [Problema tecnico, posta parzialmente irraggiungibile / Some mailboxes unavailable due to technical issues](https://cavallette.noblogs.org/2024/12/9925)
  + [mailbox deactivation problem](https://cavallette.noblogs.org/2024/07/9917)
  + [For italian workers !!!](https://cavallette.noblogs.org/2024/05/9914)
  + [GAZAWEB – gli Alberi della RETE a Gaza](https://cavallette.noblogs.org/2024/05/9908)
  + [I Punkreas ci dedicano una canzone!](https://cavallette.noblogs.org/2024/04/9903)
  + [Oops](https://cavallette.noblogs.org/2024/03/9898)
  + [Newsletter Autistici/Inventati – 2023](https://cavallette.noblogs.org/2023/12/9892)
* ## [![RSS](https://cavallette.noblogs.org/wp-includes/images/rss.png)](https://noblogs.org/feed/) [Aggiornamenti noblogs](https://noblogs.org/)

  + [Attivato tema twentytwentyfive](https://noblogs.org/2025/03/30/attivato-tema-twentytwentyfive/)
  + [Nuovo tema ed editor di siti! – New theme and...