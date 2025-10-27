---
title: Google scopre 26 nuove vulnerabilità con l’IA di OSS-Fuzz
url: https://www.securityinfo.it/2024/11/21/google-scopre-26-nuove-vulnerabilita-con-lia-di-oss-fuzz/?utm_source=rss&utm_medium=rss&utm_campaign=google-scopre-26-nuove-vulnerabilita-con-lia-di-oss-fuzz
source: Securityinfo.it
date: 2024-11-22
fetch_date: 2025-10-06T19:17:29.775247
---

# Google scopre 26 nuove vulnerabilità con l’IA di OSS-Fuzz

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

## Google scopre 26 nuove vulnerabilità con l’IA di OSS-Fuzz

Nov 21, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/approfondimenti/minacce/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Tecnologia](https://www.securityinfo.it/category/approfondimenti/tecnologia/), [Tecnologia](https://www.securityinfo.it/category/news/tecnologia-news/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/), [Vulnerabilità](https://www.securityinfo.it/category/approfondimenti/vulnerabilita-approfondimenti/)
 [0](https://www.securityinfo.it/2024/11/21/google-scopre-26-nuove-vulnerabilita-con-lia-di-oss-fuzz/#respond)

---

Google ha annunciato di aver trovato **26 nuove vulnerabilità** in progetti open-source ampiamente usati grazie a **OSS-Fuzz**, un framework di fuzzing che sfrutta l’**intelligenza artificiale per identificare bug in maniera automatica.**

Con “fuzzing” si intende una metodologia di testing del software automatizzata che inietta degli input malformati o inattesi nel sistema per individuare eventuali vulnerabilità. Ad agosto 2023 Google ha annunciato un progetto di **“AI-Powered Fuzzing”** con l’obiettivo di sfruttare gli LLM per trovare bug in maniera automatica e più velocemente.

**“*Il nostro approccio consiste nell’usare le capacità di coding di un LLM per generare più target di fuzzing, simili a a unit test che verificano funzionalità rilevanti alla ricerca di vulnerabilità*“** [hanno spiegato](https://security.googleblog.com/2024/11/leveling-up-fuzzing-finding-more.html) Oliver Chang, Dongge Liu and Jonathan Metzman dell’Open Source Security Team di Google.

![OSS Fuzz](https://www.securityinfo.it/wp-content/uploads/2024/11/digital-1742687_1920.jpg)

Pixabay

Ad oggi il framework, ora open-source, **ha aumentato la copertura di codice in 272 progetti C/C++**; ciò ha portato alla scoperta di 26 nuove vulnerabilità. Una delle più rilevanti è la CVE-2024-9143, un bug critico presente nella libreria OpenSSL. Il team di Google ha notificato la vulnerabilità lo scorso 16 settembre e il fix è arrivato un mese dopo esatto. A detta dei ricercatori, il bug sarebbe presente nella libreria da circa 20 anni e **non sarebbe stato individuato con test scritti da esseri umani.**

“*Uno dei motivi per cui questi bug potrebbero rimanere nascosti per così tanto tempo è che **la copertura delle righe (di codice, n.d.r.) non garantisce che una funzione sia priva di bug**. La copertura del codice come metrica non è in grado di misurare tutti i possibili percorsi e stati del codice: flag e configurazioni diverse possono innescare comportamenti diversi, portando alla luce bug diversi. Questi esempi sottolineano la **necessità di continuare a generare nuove varietà di obiettivi di fuzz, anche per il codice già sottoposto a fuzzing***“.

OSS-Fuzz è in grado di emulare in maniera efficiente il worfklow tipico di testing eseguito dagli sviluppatori, dalla scrittura all’esecuzione del singolo test, oltre che la fase di reporting.

Il team di Google ha in programma di **migliorare il triaging automatico** per segnalare in maniera più precisa i bug individuati ai maintaners del progetto e di **ottimizzare l’accesso dell’LLM a tool di debugging.** Uno degli obiettivi futuri è di **rendere disponibile il framework come feature** per abilitare l’uso di soluzioni end-to-end automatizzate per l’individuazione di vulnerabilità.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [debugging](https://www.securityinfo.it/tag/debugging/), [fuzzing](https://www.securityinfo.it/tag/fuzzing/), [Google](https://www.securityinfo.it/tag/google/), [Intelligenza artificiale](https://www.securityinfo.it/tag/intelligenza-artificiale/), [OSS-Fuzz](https://www.securityinfo.it/tag/oss-fuzz/), [testing](https://www.securityinfo.it/tag/testing/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[Come playlist e podcast su Spotify promuovono software pirata](https://www.securityinfo.it/2024/11/21/come-playlist-e-podcast-su-spotify-promuovono-software-pirata/)
[Una grave data breach ha colpito le aziende statunitensi di telecomunicazioni](https://www.securityinfo.it/2024/11/20/una-grave-data-breach-ha-colpito-le-aziende-statunitensi-di-telecomunicazioni/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_d4x8rid4x8rid4x8-120x85.png)](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  [Firewall Cisco sotto attacco: una nuova...](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Permanent link to Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  Set 29, 2025  [0](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/#respond)
* [![Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.](https://www.securityinfo.it/wp-content/uploads/2025/09/ai-generated-9053184_1920-120x85.jpg)](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/ "Attacc...