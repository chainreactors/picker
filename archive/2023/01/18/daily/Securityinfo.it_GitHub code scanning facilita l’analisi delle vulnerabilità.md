---
title: GitHub code scanning facilita l’analisi delle vulnerabilità
url: https://www.securityinfo.it/2023/01/17/github-code-scanning/?utm_source=rss&utm_medium=rss&utm_campaign=github-code-scanning
source: Securityinfo.it
date: 2023-01-18
fetch_date: 2025-10-04T04:11:37.899157
---

# GitHub code scanning facilita l’analisi delle vulnerabilità

Aggiornamenti recenti Ottobre 3rd, 2025 6:09 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)
* [Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)
* [Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/)
* [Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/)

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

## GitHub code scanning facilita l’analisi delle vulnerabilità

Gen 17, 2023  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [News](https://www.securityinfo.it/category/news/), [Prodotto](https://www.securityinfo.it/category/news/prodotto-news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2023/01/17/github-code-scanning/#respond)

---

**GitHub ha rilasciato code scanning, una funzionalità di sicurezza che permette di analizzare il codice di un repository per identificare vulnerabilità ed errori.** La feature è in grado anche di dare una priorità ai problemi e prevenirne di futuri tramite un sistema di alert puntuali sul codice.

**Usato in combinazione con CodeQL, code scanning può eseguire analisi automatizzate del codice in diversi repository.** Attualmente può essere usato solo con la configurazione di default che genera query CodeQL, trigger ed eventi in base al contenuto del repository. In futuro GitHub prevede di rendere personalizzabile la configurazione: gli utenti potranno modificare le query e le azioni da intraprendere in base alle proprie esigenze.

![GitHub code scanning](https://www.securityinfo.it/wp-content/uploads/2023/01/programming-1873854_1280.png)

Una volta abilitata, **la funzionalità scansiona in automatico il codice ogni volta che si verifica uno dei trigger configurati che nella configurazione** di default sono eventi di push e pull sui branch flaggati come “protected”.

## CodeQL per il code scanning di GitHub

La funzionalità di code scanning di GitHub automatizza l’esecuzione di query in CodeQL per individuare problemi di sicurezza, vulnerabilità nel codice ed errori di programmazione. **Il motore di analisi di GitHub lavora con due tipi di query: le alert queries, che evidenziano problemi in punti precisi del codice, e path queries, che descrivono il flusso di informazione** da una sorgente a una destinazione.

**Le prime vengono usate per individuare errori nel codice che potrebbero portare**, come eccezioni non gestite o deserializzazioni non sicure. **Le seconde, invece, si rivelano particolarmente utili per seguire il flusso dei dati nelle funzioni e identificare eventuali data leak o problemi di sicurezza** causati da input malevoli passati come argomenti di funzioni.

![GitHub code scanning](https://www.securityinfo.it/wp-content/uploads/2023/01/pexels-mart-production-7172094.jpg)

Per il momento **la feature di code scanning è disponibile solo per repository in Python, Javascript e Ruby**; nei prossimi mesi GitHub estenderà il supporto anche ad altri linguaggi. Code scanning ha un potenziale elevato e, con diversi gradi di personalizzazione, **potrà rivelarsi un potente alleato per gli sviluppatori.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [code scanning](https://www.securityinfo.it/tag/code-scanning/), [codeql](https://www.securityinfo.it/tag/codeql/), [data flow](https://www.securityinfo.it/tag/data-flow/), [data leak](https://www.securityinfo.it/tag/data-leak/), [GitHub](https://www.securityinfo.it/tag/github/), [programmazione](https://www.securityinfo.it/tag/programmazione/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/), [vulnerabilità codice](https://www.securityinfo.it/tag/vulnerabilita-codice/)

[ChatGPT: una nuova arma nell’arsenale dei criminali informatici](https://www.securityinfo.it/2023/01/17/chatgpt-una-nuova-arma-nellarsenale-dei-criminali-informatici/)
[Il costo del ransomware continua a crescere](https://www.securityinfo.it/2023/01/17/il-costo-del-ransomware-continua-a-crescere/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_d4x8rid4x8rid4x8-120x85.png)](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  [Firewall Cisco sotto attacco: una nuova...](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Permanent link to Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  Set 29, 2025  [0](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/#respond)
* [![Nuova variante del malware XCSSET prende di mira gli sviluppatori Xcode su macOS](https://www.securityinfo.it/wp-content/uploads/2025/09/MalwareCrypto-29-set-2025CG-120x85.png)](https://www.securityinfo.it/2025/09/26/nuova-variante-del-malware-xcsset-prende-di-mira-gli-sviluppatori-xcode-su-macos/ "Nuova variante del malware XCSSET prende di mira gli sviluppatori Xcode su macOS")

  [Nuova variante del malware XCSSET...](https://www.securityinfo.it/2025/09/26/nuova-variante-del-malware-xcsset-prende-di-mira-gli-sviluppatori-xcode-su-macos/ "Permanent link to Nuova variante del malware XCSSET prende di mira gli sviluppatori Xcode su macOS")

  Set 26, 2025  [0](https://www.securityinfo.it/2025/09/26/nuova-variante-del-malware-xcsset-prende-di-mira-gli-sviluppatori-xcode-su-macos/#respond)
* [![Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.](https://www.securityinfo.it/wp-content/uploads/2025/09/ai-generated-9053184_1920-120x85.jpg)](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/ "Attaccanti sfruttano un bug di GeoServer...