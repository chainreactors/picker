---
title: Le vulnerabilità di CocoaPods mettono in pericolo migliaia di device Apple
url: https://www.securityinfo.it/2024/07/04/le-vulnerabilita-di-cocoapods-mettono-in-pericolo-migliaia-di-device-apple/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-05
fetch_date: 2025-10-06T17:44:33.972227
---

# Le vulnerabilità di CocoaPods mettono in pericolo migliaia di device Apple

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

## Le vulnerabilità di CocoaPods mettono in pericolo migliaia di device Apple

Lug 04, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Tecnologia](https://www.securityinfo.it/category/news/tecnologia-news/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2024/07/04/le-vulnerabilita-di-cocoapods-mettono-in-pericolo-migliaia-di-device-apple/#respond)

---

**Migliaia di dispositivi Apple sono vulnerabili** ad attacchi supply chain a causa di alcune **debolezze in** **CocoaPods**: lo hanno scoperto i ricercatori di [E.V.A. Information Security](https://www.evasec.io/blog/eva-discovered-supply-chain-vulnerabities-in-cocoapods), i quali hanno evidenziato che le organizzazioni rischiano danni finanziari e reputazionali a causa di questi attacchi.

![CocoaPods](https://www.securityinfo.it/wp-content/uploads/2024/07/laptop-5987093_1920.jpg)

Pixabay

CocoaPods è un **dependency manager open source** per Swift e i progetti in Objective C. Il gestore si occupa di scaricare le librerie di cui hanno bisogno gli sviluppatori e verificarne l’integrità.

L’ecosistema però, a quanto pare, soffre di diverse vulnerabilità: il team di E.V.A. Information Security spiega che nel 2014 si è verificato un processo di **migrazione dei pacchetti che ha lasciato però migliaia di essi “orfani”**, senza un owner che li reclamasse, e molti di questi sono ancora ampiamente usati in altre librerie. Usando un’API pubblica e un indirizzo email trovati nel codice sorgente di CocoaPods, un attaccante può **reclamare uno o più di questi pacchetti come suo e rimpiazzarne il codice sorgente con un payload malevolo.**

Il team ha scoperto anche che **il** **flusso di verifica di email è insicuro** e può essere sfruttato per eseguire codice arbitrario sul server “Trunk” dell’ecosistema, consentendo a un attaccante di **manipolare o rimpiazzare i pacchetti che vengono scaricati**. Sono inoltre presenti delle **configurazioni errate nei tool di sicurezza per l’email** che permetterebbero a un attaccante di eseguire lo spoofing di un header HTTP ed eseguire un **attacco zero-click per ottenere il token di verifica dell’account dello sviluppatore.**

Infine, una quarta vulnerabilità consentirebbe a un attaccante di **accedere al server Trunk di CocoaPods** ed eseguire numerosi exploit di varia natura.

## CocoaPods: migliaia di device Apple vulnerabili

CocoaPods è molto popolare tra gli sviluppatori e molte delle librerie “orfane” sono presenti come dipendenze in progetti di grandi compagnie come Google, GitHub, Amazon, Dropbox e molte altre.

Secondo la stima dei ricercatori di E.V.A. Information Security, **migliaia di dispositivi Apple sono vulnerabili ad attacchi supply chain e zero-click**, ma il numero potrebbe arrivare anche a milioni di applicazioni. “*Come con molti altri attacchi supply chain, le dipendenze opache nel codice closed-source rendono quasi impossibile capire il potenziale danno*” spiegano i ricercatori.

![](https://www.securityinfo.it/wp-content/uploads/2024/06/line-7146714_1920.jpg)

Se è vero che molte applicazioni non accedono alle informazioni sensibili degli utenti, la possibilità di iniettare codice malevolo nelle app tramite le librerie senza owner permetterebbe agli attaccanti sostanzialmente di prendere il controllo del dispositivo e **attaccare le vittime con ransomware, truffe e campagne di spionaggio nel caso di dispositivi aziendali.**

È fondamentale che gli sviluppatori effettuino una **review delle librerie in uso** e validino i checksum dei pacchetti di terze parti; inoltre, è consigliabile effettuare delle scansioni periodiche delle librerie per individuare codice malevolo o modifiche sospette, e in generale **limitare l’uso di pacchetti “orfani” o non più mantenuti.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Apple](https://www.securityinfo.it/tag/apple/), [attacchi supply chain](https://www.securityinfo.it/tag/attacchi-supply-chain/), [attacchi zero-click](https://www.securityinfo.it/tag/attacchi-zero-click/), [CocoaPods](https://www.securityinfo.it/tag/cocoapods/), [dependency manager](https://www.securityinfo.it/tag/dependency-manager/), [librerie](https://www.securityinfo.it/tag/librerie/)

[Splunk risolve 16 vulnerabilità in Enterprise e Cloud Platform di cui 5 a rischio elevato](https://www.securityinfo.it/2024/07/04/splunk-risolve-16-vulnerabilita-in-enterprise-e-cloud-platform-di-cui-5-a-rischio-elevato/)
[Cisco risolve una vulnerabilità zero-day sfruttata da Velvet Ant](https://www.securityinfo.it/2024/07/03/cisco-risolve-una-vulnerabilita-zero-day-sfruttata-da-velvet-ant/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Apple rilascia una fix per una vulnerabilità di Safari già sfruttata in Chrome](https://www.securityinfo.it/wp-content/uploads/2025/07/Gemini_Generated_Image_1mvtjc1mvtjc1mvt-120x85.png)](https://www.securityinfo.it/2025/07/30/apple-rilascia-una-fix-per-una-vulnerabilita-di-safari-gia-sfruttata-in-chrome/ "Apple rilascia una fix per una vulnerabilità di Safari già sfruttata in Chrome")

  [Apple rilascia una fix per una...](https://www.securityinfo.it/2025/07/30/apple-rilascia-una-fix-per-una-vulnerabilita-di-safari-gia-sfruttata-in-chrome/ "Permanent link to Apple rilascia una fix per una vulnerabilità di Safari già sfruttata in Chrome")

  Lug 30, 2025  [0](https://www.securityinfo.it/2025/07/30/apple-rilascia-una-fix-per-una-vulnerabilita-di-safari-gia...