---
title: Apple rilascia una fix per una vulnerabilità di Safari già sfruttata in Chrome
url: https://www.securityinfo.it/2025/07/30/apple-rilascia-una-fix-per-una-vulnerabilita-di-safari-gia-sfruttata-in-chrome/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-31
fetch_date: 2025-10-06T23:54:43.714662
---

# Apple rilascia una fix per una vulnerabilità di Safari già sfruttata in Chrome

Aggiornamenti recenti Ottobre 6th, 2025 5:03 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Impennata delle scansioni dei portali di login di Palo Alto Networks: +500%](https://www.securityinfo.it/2025/10/06/impennata-delle-scansioni-dei-portali-di-login-di-palo-alto-networks-500/)
* [Microsoft Sentinel: arriva l’era degli agenti AI e della difesa predittiva](https://www.securityinfo.it/2025/10/06/microsoft-sentinel-arriva-lera-degli-agenti-ai-e-della-difesa-predittiva/)
* [CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)

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

## Apple rilascia una fix per una vulnerabilità di Safari già sfruttata in Chrome

Lug 30, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/07/30/apple-rilascia-una-fix-per-una-vulnerabilita-di-safari-gia-sfruttata-in-chrome/#respond)

---

Martedì Apple ha rilasciato una **fix che risolve una vulnerabilità 0-day presente in WebKit**, il motore di rendering usato in Safari, già nota e sfruttata in Chrome in almeno un attacco.

Il bug, tracciato come **CVE-2025-6558**, risiede nei componenti open-source ANGLE e GPU di Google ed è causata da una validazione errata dell’input. Stando alla [descrizione fornita](https://nvd.nist.gov/vuln/detail/CVE-2025-6558), la vulnerabilità consente a un attaccante di eseguire un **sandbox escape** da remoto utilizzando una pagina HTML creata ad hoc.

![vulnerabilità Safari](https://www.securityinfo.it/wp-content/uploads/2025/07/Gemini_Generated_Image_1mvtjc1mvtjc1mvt.png)

Poiché WebKit utilizza i componenti open-source di Google, anche Safari è colpito dalla vulnerabilità. Google [ha affermato](https://chromereleases.googleblog.com/2025/07/stable-channel-update-for-desktop_15.html) di essere a conoscenza di un exploit che ha sfruttato il bug, ma non ha reso noto alcun dettaglio in merito. Il [comunicato](https://support.apple.com/en-us/124147) di Apple non accenna invece a potenziali exploit.

Nel caso di Safari, lo sfruttamento della vulnerabilità può portare al **crash di Safari**. Apple non ha condiviso altri dettagli.

La patch è disponibile in **iOS 18.6** e **iPadOS 18.6** per iPhone XS e successivi, iPad Pro da 13 pollici, iPad Pro da 12,9 pollici di terza generazione e successive, iPad Pro da 11″ di prima generazoine e successive, iPad Air di terza generazione e successive, iPad di settima generazione e successive e iPad mini di quinta generazione e successive.

Il fix è inoltre presente in **iPadOS 17.7.9** per iPad Pro da 12.9 pollici di seconda generazione, iPad Pro da 10.5 pollici e iPad di sesta generazione; macOS Sequoia 15.6; in **tvOS 18.6** per Apple TV HD e Apple TV 4K (tutti i modelli); in **watchOS 11.6** per Apple Watch Series 6 e successivi e in **visionOS 2.6** per Apple Vision Pro. Per quanto riguarda Chrome, la patch è disponibile nella versione 138.0.7204.157 del browser.

Anche lo scorso marzo Apple aveva avuto a che fare con una [vulnerabilità 0-day in WebKit](https://www.securityinfo.it/2025/03/12/apple-risolve-un-bug-0-day-di-webkit-gia-sfruttato/): la CVE-2025-24201, un problema di scrittura out-of-bound, permetteva a un attaccante di sfruttare un contenuto web creato ad hoc per uscire dalla sandbox del browser.

È consigliato aggiornare il prima possibile i prodotti vulnerabili.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Apple](https://www.securityinfo.it/tag/apple/), [Chrome](https://www.securityinfo.it/tag/chrome/), [Google](https://www.securityinfo.it/tag/google/), [Safari](https://www.securityinfo.it/tag/safari/), [sandbox escape](https://www.securityinfo.it/tag/sandbox-escape/), [webkit](https://www.securityinfo.it/tag/webkit/)

[Un Raspberry Pi per hackerare accedere alla rete bancaria: l'attacco (fallito) di UNC2891](https://www.securityinfo.it/2025/07/31/un-raspberry-pi-per-hackerare-accedere-alla-rete-bancaria-lattacco-di-unc2891/)
[SafePay, cresce la minaccia ransomware contro gli MSP](https://www.securityinfo.it/2025/07/29/safepay-cresce-la-minaccia-ransomware-contro-gli-msp/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Google e la privacy: sanzione multimilionaria per informazioni fuorvianti](https://www.securityinfo.it/wp-content/uploads/2025/09/security-4868167_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/09/10/google-e-la-privacy-sanzione-multimilionaria-per-informazioni-fuorvianti/ "Google e la privacy: sanzione multimilionaria per informazioni fuorvianti")

  [Google e la privacy: sanzione...](https://www.securityinfo.it/2025/09/10/google-e-la-privacy-sanzione-multimilionaria-per-informazioni-fuorvianti/ "Permanent link to Google e la privacy: sanzione multimilionaria per informazioni fuorvianti")

  Set 10, 2025  [0](https://www.securityinfo.it/2025/09/10/google-e-la-privacy-sanzione-multimilionaria-per-informazioni-fuorvianti/#respond)
* [![Il data breach contro Salesloft impatta centinaia di servizi](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_evjthoevjthoevjt-120x85.png)](https://www.securityinfo.it/2025/09/02/il-data-breach-contro-salesloft-impatta-centinaia-di-servizi/ "Il data breach contro Salesloft impatta centinaia di servizi")

  [Il data breach contro Salesloft impatta...](https://www.securityinfo.it/2025/09/02/il-data-breach-contro-salesloft-impatta-centinaia-di-servizi/ "Permanent link to Il data breach contro Salesloft impatta centinaia di servizi")

  Set 02, 2025  [0](https://www.securityinfo.it/2025/09/02/il-data-breach-contro-salesloft-impatta-centinaia-di-servizi/#respond)
* [![Android, più sicurezza con la verifica dell’identità sviluppatori](https://www.securityinfo.it/wp-content/uploads/2025/08/Gemini_Generated_Image_qj2bi3qj2bi3qj2b-120x85.png)](https://www.securityinfo.it/2025/08/27/android-piu-sicurezza-con-la-verifica-dellidentita-sviluppatori/ "Android, più sicurezza con la verifica dell’identità sviluppatori")

  [Android, più sicurezza con la verifica...](https://www.security...