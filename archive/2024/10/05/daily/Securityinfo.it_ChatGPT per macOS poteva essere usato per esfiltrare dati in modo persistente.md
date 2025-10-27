---
title: ChatGPT per macOS poteva essere usato per esfiltrare dati in modo persistente
url: https://www.securityinfo.it/2024/10/04/chatgpt-per-macos-poteva-essere-usato-per-esfiltrare-dati-a-lungo-termine/?utm_source=rss&utm_medium=rss&utm_campaign=chatgpt-per-macos-poteva-essere-usato-per-esfiltrare-dati-a-lungo-termine
source: Securityinfo.it
date: 2024-10-05
fetch_date: 2025-10-06T18:54:27.512293
---

# ChatGPT per macOS poteva essere usato per esfiltrare dati in modo persistente

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

## ChatGPT per macOS poteva essere usato per esfiltrare dati in modo persistente

Ott 04, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2024/10/04/chatgpt-per-macos-poteva-essere-usato-per-esfiltrare-dati-a-lungo-termine/#respond)

---

Fino a neanche un mese fa l’applicazione di **ChatGPT per macOS** poteva essere usata per **esfiltrare le informazioni inserite dall’utente o le risposte del chatbot in modo persistente.** A rivelarlo è Johann Rehberger, ricercatore di sicurezza che [ha scoperto](https://embracethered.com/blog/posts/2024/chatgpt-macos-app-persistent-data-exfiltration/) la vulnerabilità nell’aprile 2023.

![ChatGPT macOS](https://www.securityinfo.it/wp-content/uploads/2024/10/chat-7767693_1920.jpg)

All’inizio del 2023 OpenAI aveva implementato una feature per mitigare i vettori di esfiltrazione dati tramite una call a un’API chiamata “url\_safe”. L’API informa il client di ChatGPT se è possibile mostrare all’utente un URL o un’immagine in modo sicuro, in modo da mitigare gli attacchi di prompt injection.

Poiché però il controllo viene eseguito client side, le applicazioni sono rimaste vulnerabili; non solo: una funzionalità più recente, chiamata **“Memory”**, ha aumentato la criticità del bug **permettendo anche alle istruzioni malevole di essere memorizzate.**

La feature “Memory” di fatto consente al chatbot di memorizzare le chat per offrire risposte più rilevanti e in linea con le preferenze già espresse dell’utente. L’exploit realizzato dal ricercatore, chiamato **spAIware**, sfrutta questa capacità per “iniettare delle memorie” che contengono istruzioni volte a esfiltrare i dati dell’utente.

“*Poiché le istruzioni malevole vengono memorizzate nella memoria del chatbot, **tutte le nuove conversazioni da quel momento in poi conterranno le istruzioni dell’attaccante e invieranno continuamente tutti i messaggi della chat e le risposte all’attaccante***” spiega Rehberger. Il bug di data exfiltration diventa in questo modo ancora più pericoloso perché permane in tutte le chat.

Per iniettare queste istruzioni, i cybercriminali possono ricorrere a una tecnica di esfiltrazione già nota che consiste nel mostrare un’immagine proveniente da un server malevolo e chiedere a ChatGPT di includere i dati utenti come parametro nella richiesta. Tutto comincia quando l’utente chiede al chatbot di analizzare un documento malevolo o naviga su un sito web non affidabile: il documento o il sito web contengono istruzioni per prendere il controllo del chatbot e inserire la “memoria” per l’esfiltrazione dei dati.

![ChatGPT macOS](https://www.securityinfo.it/wp-content/uploads/2024/10/chatgpt-macos-persisten3.png)

Credits: Johann Rehberger

Il prompt presente nel sito web controllato dall’attaccante indica al chatbot di inviare al server tutti i messaggi inviati e ricevuti dall’utente, ovviamente a sua insaputa.

OpenAI ha risolto il bug di ChatGPT su macOS con la versione 1.2024.247 e invita gli utenti ad aggiornare l’applicazione il prima possibile. Rehberger chiarisce che l’intervento della compagnia non impedisce a un attaccante di invocare sfruttare la feature “Memory” per iniettare memoria arbitrare, ma mitiga il vettore di esfiltrazione, ovvero impedisce al chatbot di inviare messaggi a un server di terze parti tramite il rendering di immagini.

Per questo motivo, oltre ad aggiornare l’applicazione, il ricercatore consiglia agli utenti di controllare regolarmente le “memorie” salvate dal chatbot ed eliminare quelle sospette.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Chatgpt](https://www.securityinfo.it/tag/chatgpt/), [esfiltrazione dati](https://www.securityinfo.it/tag/esfiltrazione-dati/), [macOS](https://www.securityinfo.it/tag/macos/), [prompt injection](https://www.securityinfo.it/tag/prompt-injection/), [rendering immagine](https://www.securityinfo.it/tag/rendering-immagine/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[CERT-AGID 28 settembre – 4 ottobre: 29 campagne malevole e un malware simile a uno spyware](https://www.securityinfo.it/2024/10/07/cert-agid-28-settembre-4-ottobre-29-malware-spyware/)
[La scadenza della NIS2 si avvicina, ma non mancano lo scetticismo e le difficoltà di adozione](https://www.securityinfo.it/2024/10/03/scadenza-nis2-si-avvicina-non-mancano-scetticismo-difficolta-adozione/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_camyclcamyclcamy-120x85.png)](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/ "Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT")

  [Scoperto ShadowLeak, un attacco che...](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/ "Permanent link to Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT")

  Set 30, 2025  [0](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/#respond)
* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_d4x8rid4x8rid4x8-120x85.png)](https://www.se...