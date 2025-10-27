---
title: Google annuncia OSS Rebuild per migliorare la sicurezza dell’open-source
url: https://www.securityinfo.it/2025/07/28/google-annuncia-oss-rebuild-per-migliorare-la-sicurezza-dellopen-source/?utm_source=rss&utm_medium=rss&utm_campaign=google-annuncia-oss-rebuild-per-migliorare-la-sicurezza-dellopen-source
source: Securityinfo.it
date: 2025-07-29
fetch_date: 2025-10-06T23:56:47.481466
---

# Google annuncia OSS Rebuild per migliorare la sicurezza dell’open-source

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

## Google annuncia OSS Rebuild per migliorare la sicurezza dell’open-source

Lug 28, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/07/28/google-annuncia-oss-rebuild-per-migliorare-la-sicurezza-dellopen-source/#respond)

---

La scorsa settimana Google [ha annunciato](https://security.googleblog.com/2025/07/introducing-oss-rebuild-open-source.html) **OSS Rebuild**, un’iniziativa che mira a **rendere più sicuro il software open-source** rendendo l’accesso agli artefatti più trasparente per gli sviluppatori.

![OSS Rebuild](https://www.securityinfo.it/wp-content/uploads/2025/07/Gemini_Generated_Image_qq7sk8qq7sk8qq7s.png)

“*L’open-source è diventato la base del nostro mondo digitale. Dalle infrastrutture critiche alle applicazioni di tutti i giorni, **le componenti open-source oggi rappresentano il 77% del software moderno***” ha affermato Matthew Suozzo del Google Open Source Security Team. Questa ubiquità rende però il software open-source un obiettivo perfetto per i cybercriminali: compromettendo i pacchetti più usati, è possibile realizzare attacchi supply-chain con impatti elevati.

OSS Rebuild garantisce la trasparenza basandosi su un **processo di build dichiarativo e riproducibile** per garantire la sicurezza di un determinato pacchetto. Dato un artefatto già caricato, OSS Rebuild dichiara una definizione di build per il pacchetto e riesegue la build; in seguito, compara semanticamente il risultato con l’artefatto già caricato.

Una volta riprodotta la build, ne viene pubblicata la definizione e il risultato tramite **SLSA** (Supply-chain Levels for Software Artifacts), un framework Google per garantire e proteggere l’integrità dei pacchetti software. Il processo mette a disposizione della community dei metadati sui pacchetti open-source che validano l’origine degli artefatti e garantiscono che non sono stati compromessi.

![OSS Rebuild](https://www.securityinfo.it/wp-content/uploads/2025/07/Screenshot-2025-07-21-at-2.36.43 PM.png)

Credits: Google

**OSS Rebuild è in grado di identificare diverse problematiche e classi di attacchi supply-chain**, come backdoor nascoste o codice presente nei pacchetti ma non nel codice sorgente. L’iniziativa contribuisce inoltre a velocizzare il processo di individuazione delle vulnerabilità, aumenta l’affidabilità dei pacchetti in uso ed elimina la necessità dei controlli di sicurezza nelle piattaforme di CI/CD. Attualmente il progetto supporta NPM, PyPI e Crates.io.

“*OSS Rebuild non si limita a risolvere i problemi, ma **mira a responsabilizzare gli utenti finali affinché rendano gli ecosistemi open source più sicuri e trasparenti attraverso un’azione collettiva**. Se sei uno sviluppatore, un’azienda o un ricercatore nel campo della sicurezza interessato alla sicurezza OSS, ti invitiamo a seguirci e a partecipare*” ha concluso Suozzo.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [attacchi supply chain](https://www.securityinfo.it/tag/attacchi-supply-chain/), [Google](https://www.securityinfo.it/tag/google/), [Open Source](https://www.securityinfo.it/tag/open-source/), [OSS Rebuild](https://www.securityinfo.it/tag/oss-rebuild/), [pacchetti open-source](https://www.securityinfo.it/tag/pacchetti-open-source/), [SLSA](https://www.securityinfo.it/tag/slsa/)

[Spionaggio industriale: i gruppi cinesi puntano ai chip di Taiwan](https://www.securityinfo.it/2025/07/29/spionaggio-industriale-i-gruppi-cinesi-puntano-ai-chip-di-taiwan/)
[CERT-AGID 19 – 25 luglio: il Fascicolo Sanitario Elettronico come leva](https://www.securityinfo.it/2025/07/28/cert-agid-19-25-luglio-il-fascicolo-sanitario-elettronico-come-leva/)

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
* [![Android, più sicurezza con la verifica dell’identità sviluppatori](https://www.securityinfo.it/wp-content/uploads/2025/08/Gemini_Generated_Image_qj2bi3qj2bi3qj2b-120x85.png)](https://www.securityinfo.it/2025/08/27/android-piu-sicurezza-con-la-verifica-dellidentita-sviluppatori/ "Android, più ...