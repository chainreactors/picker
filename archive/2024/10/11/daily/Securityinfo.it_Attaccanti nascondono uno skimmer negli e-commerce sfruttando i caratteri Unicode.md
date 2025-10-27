---
title: Attaccanti nascondono uno skimmer negli e-commerce sfruttando i caratteri Unicode
url: https://www.securityinfo.it/2024/10/10/attaccanti-nascondono-uno-skimmer-negli-e-commerce-sfruttando-i-caratteri-unicode/?utm_source=rss&utm_medium=rss&utm_campaign=attaccanti-nascondono-uno-skimmer-negli-e-commerce-sfruttando-i-caratteri-unicode
source: Securityinfo.it
date: 2024-10-11
fetch_date: 2025-10-06T18:53:56.450269
---

# Attaccanti nascondono uno skimmer negli e-commerce sfruttando i caratteri Unicode

Aggiornamenti recenti Ottobre 6th, 2025 9:00 AM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)
* [Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)
* [Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/)

* [Home](https://www.securityinfo.it)
* [News](https://www.securityinfo.it/category/news/)
* [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/)
* [Opinioni](https://www.securityinfo.it/category/opinioni/)
* [Top Malware](https://www.securityinfo.it/top-malware-page/)
* [Minacce](https://www.securityinfo.it/category/minacce-2/)
* [Guide alla sicurezza](http://www.securityinfo.it/guide-alla-sicurezza/)
* [Podcast](https://www.securityinfo.it/podcast-page/)
* [Strumenti Utili](https://www.securityinfo.it/category/strumenti-utili/)

* Search for:

## Attaccanti nascondono uno skimmer negli e-commerce sfruttando i caratteri Unicode

Ott 10, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2024/10/10/attaccanti-nascondono-uno-skimmer-negli-e-commerce-sfruttando-i-caratteri-unicode/#respond)

---

I ricercatori di Jscrambler hanno individuato peculiare campagna di attacchi in cui **i cybercriminali offuscavano uno skimmer negli e-commerce sfruttano i caratteri Unicode.**

***“L’ampio uso di caratteri Unicode, molti dei quali invisibili, rende effettivamente il codice molto difficile da leggere per gli esseri umani*“** [affermano](https://jscrambler.com/blog/the-mongolian-skimmer) i ricercatori. Nel dettaglio, gli attaccanti hanno sfruttato la possibilità di usare qualsiasi carattere Unicode per gli identificatori (come nomi di variabili e funzioni) in JavaScript per offuscare il codice dello skimmer.

![skimmer Unicode](https://www.securityinfo.it/wp-content/uploads/2024/10/cyber-security-3480163_1920.jpg)

I ricercatori spiegano che non si tratta affatto di una tecnica avanzata come era sembrato inizialmente, ma **introduce effettivamente un livello di confusione aggiuntivo** per chi cerca di leggere il codice senza tool per il reverse engineering.

Lo skimmer, soprannominato **Mongolian Skimmer** dal team di Jscrambler, si occupa di **monitorare il DOM delle pagine web** per individuare eventuali cambiamenti nei campi di input; questi elementi, spiegano i ricercatori, sono i target primari per raccogliere le informazioni che l’utente inserisce in pagina.

Lo skimmer è anche in grado di controllare l’URL della pagina e **individuare keyword quali “checkout” o “admin”** per identificare pagine che potenzialmente contengono dati sensibili, i quali vengono poi raccolti e inviati agli attaccanti. Lo script **verifica inoltre se è aperta la finestra dei tool per gli sviluppatori** e, in caso positivo, disabilita alcune funzioni. I dati vengono raccolti prima che la pagina venga chiusa o aggiornata. Infine, lo skimmer usa una tecnica di anti-debugging per **“proteggersi” da possibili modifiche di formato che lo** **esporrebbero**, rendendo inutile l’Unicode.

Il Mongolian Skimmer ha utilizzato una tecnica piuttosto obsoleta per aggiungere un ulteriore livello di offuscamento e di certo non più difficile da individuare ed effettuarne il reverse. Lo skimmer ha preso di mira le installazioni vulnerabili di Magento; per questo si consiglia agli utenti di **aggiornare il prima possibile il CMS all’ultima release disponibile.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [CMS](https://www.securityinfo.it/tag/cms/), [e-commerce](https://www.securityinfo.it/tag/e-commerce/), [Magento](https://www.securityinfo.it/tag/magento/), [Mongolian Skimmer](https://www.securityinfo.it/tag/mongolian-skimmer/), [skimmer](https://www.securityinfo.it/tag/skimmer/), [Unicode](https://www.securityinfo.it/tag/unicode/)

[Google lancia Global Signal Exchange per combattere le frodi online](https://www.securityinfo.it/2024/10/11/google-lancia-global-signal-exchange-per-combattere-le-frodi-online/)
[Microsoft individua un aumento di campagne BEC che sfruttano servizi cloud](https://www.securityinfo.it/2024/10/10/microsoft-individua-un-aumento-di-campagne-bec-che-sfruttano-servizi-cloud/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Caratteri Unicode speciali possono essere usati per iniettare comandi nei chatbot](https://www.securityinfo.it/wp-content/uploads/2024/10/chatbot-6626193_1920-120x85.png)](https://www.securityinfo.it/2024/10/22/caratteri-unicode-speciali-possono-essere-usati-per-iniettare-comandi-nei-chatbot/ "Caratteri Unicode speciali possono essere usati per iniettare comandi nei chatbot")

  [Caratteri Unicode speciali possono...](https://www.securityinfo.it/2024/10/22/caratteri-unicode-speciali-possono-essere-usati-per-iniettare-comandi-nei-chatbot/ "Permanent link to Caratteri Unicode speciali possono essere usati per iniettare comandi nei chatbot")

  Ott 22, 2024  [0](https://www.securityinfo.it/2024/10/22/caratteri-unicode-speciali-possono-essere-usati-per-iniettare-comandi-nei-chatbot/#respond)
* [![Cresce Caramel, lo skimmer-as-a-service russo](https://www.securityinfo.it/wp-content/uploads/2022/05/cyber-monday-5463567_1920-120x85.jpg)](https://www.securityinfo.it/2022/05/10/cresce-caramel-lo-skimmer-as-a-service-russo/ "Cresce Caramel, lo skimmer-as-a-service russo")

  [Cresce Caramel, lo skimmer-as-a-service...](https://www.securityinfo.it/2022/05/10/cresce-caramel-lo-skimmer-as-a-service-russo/ "Permanent link to Cresce Caramel, lo skimmer-as-a-service russo")

  Mag 10, 2022  [0](https://www.securityinfo.it/2022/05/10/cresce-caramel-lo-skimmer-as-a-service-russo/#respond)
* [![Falla zero-day in Magento 2 e Adobe Commerce](https://www.securityinfo.it/wp-content/uploads/2022/02/to-buy-3692440_1920-120x85.jpg)](https://www.securityinfo.it/2022/02/15/falla-zero-day-in-magento-2-e-adobe-commerce/ "Falla zero-day in Magento 2 e Adobe Commerce")

  [Falla zero-day in Magento 2 e Adobe...](https://www.securityinfo.it/2022/02/15/falla-zero-day-in-magento-2-e-adobe-commerce/ "Permanent link to Falla zero-day in Magento 2 e Adobe Commerce")

  Feb 15, 2022  [0](https://www.securityinfo.it/2022/02/15/falla-zero-day-in-magento-2-e-adobe-commerce/#respond)
* [![Triplicato l’interesse dei bambini per i siti di e...