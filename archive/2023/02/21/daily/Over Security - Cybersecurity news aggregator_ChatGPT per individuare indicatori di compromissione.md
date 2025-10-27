---
title: ChatGPT per individuare indicatori di compromissione
url: https://www.securityinfo.it/2023/02/20/chatgpt-indicatori-compromissione/?utm_source=rss&utm_medium=rss&utm_campaign=chatgpt-indicatori-compromissione
source: Over Security - Cybersecurity news aggregator
date: 2023-02-21
fetch_date: 2025-10-04T07:38:01.040976
---

# ChatGPT per individuare indicatori di compromissione

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

## ChatGPT per individuare indicatori di compromissione

Feb 20, 2023  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Scenario](https://www.securityinfo.it/category/approfondimenti/scenario/), [Vulnerabilità](https://www.securityinfo.it/category/approfondimenti/vulnerabilita-approfondimenti/)
 [0](https://www.securityinfo.it/2023/02/20/chatgpt-indicatori-compromissione/#respond)

---

**Tra i compiti che ChatGPT può svolgere ce ne sono anche alcuni legati alla cybersecurity**: il tool è in grado di generare report di segnalazione in seguito a incidenti o interpretare codice decompilato per individuare eventuali minacce. Alcuni cybercriminali avrebbero inoltre usato il chatbot per creare email di phishing o [addirittura malware polimorfici](https://www.securityinfo.it/2023/01/25/creare-un-malware-polimorfico-con-chatgpt/).

**Victor Sergeev, Incident Response Team Leader presso Kaspersky, [ha messo alla prova ChatGPT](https://securelist.com/ioc-detection-experiments-with-chatgpt/108756/)** con una serie di domande relative al funzionamento di minacce esistenti e con un test per l’individuazione di indicatori di compromissione.

![ ChatGPT compromissione](https://www.securityinfo.it/wp-content/uploads/2023/02/eye-futuristic-robot-1-scaled.jpg)

Eye of a futuristic robot

Gli esperimenti di Sergeev hanno dimostrato che **il chatbot ha una buona conoscenza di tool comuni di hacking come Mimikatz e Fast Reverse Proxy**, delle loro tecniche e degli indicatori di compromissione. **I risultati sono stati più deludenti nel caso di indicatori più generici come hash e domini malevoli**: non sempre è riuscito a identificarli come pericolosi.

**La situazione è migliorata con la richiesta di elencare i domini utilizzati dai gruppi APT34, APT27 e FIN7**. Il chatbot ha anche fornito una spiegazione basilare ma esaustiva di come proteggersi individuando i domini malevoli.

## Un test più complesso

Sergeev si è spinto oltre e **ha chiesto a ChatGPT di sviluppare del codice che estraesse diversi tipi di metadati da un sistema Windows di test, indicando poi se questi dati fossero indicatori di compromissione.**

![ ChatGPT compromissione](https://www.securityinfo.it/wp-content/uploads/2023/02/5913859_3074190-scaled.jpg)

Freepik

Il team di Sergeev ha cominciato a infettare il sistema simulando due attacchi; in seguito ha eseguito il codice prodotto da ChatGPT, opportunamente corretto in alcuni punti, e analizzato le risposte del tool riguardo agli indicatori di compromissione individuati**. Il tool ha identificato correttamente i due processi malevoli specificando anche perché avesse identificato quei metadati come avversi.**

**L’esperimento ha dato esiti positivi anche quando il team ha provato a installare due malware**: il chatbot ha identificato i processi come malevoli, riuscendo anche a fornire una spiegazione step by step del tentativo di attacco.

Nonostante il successo generale delle prove, **ChatGPT in più occasioni non è riuscito a identificare gli attacchi, come nel caso del tentativo di estrazione di credenziali.** In alcuni test il chatbot ha suggerito che i processi *potevano* essere malevoli, senza però individuare l’effettiva minaccia; in altri non è riuscito affatto a riconoscerli.

![ ChatGPT compromissione](https://www.securityinfo.it/wp-content/uploads/2023/02/hacking-2077124_1280.jpg)

Pixabay

Tutto sommato **ChatGPT può rivelarsi uno strumento utile per supportare la cybersecurity e l’individuazione di minacce.** Se addestrato correttamente, il chatbot è in grado di capire se un malware è simile ad altri già analizzati, così da instradare la miglior strategia di difesa.

Si tratta in ogni caso di uno strumento che, come sottolinea lo stesso autore, può generare falsi positivi e falsi negativi; occorre quindi valutare i risultati prima di fare delle scelte. Come al solito, **la correttezza dell’output dipende fortemente dai dati utilizzati per il training e dai filtri applicati al dataset.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Chatgpt](https://www.securityinfo.it/tag/chatgpt/), [cybersecurity](https://www.securityinfo.it/tag/cybersecurity/), [hacking tool](https://www.securityinfo.it/tag/hacking-tool/), [indicatore di compromissione](https://www.securityinfo.it/tag/indicatore-di-compromissione/), [Kaspersky](https://www.securityinfo.it/tag/kaspersky/), [Securelist](https://www.securityinfo.it/tag/securelist/)

[Sophos: le soluzioni zero trust funzionano meglio delle VPN](https://www.securityinfo.it/2023/02/21/sophos-le-soluzioni-zero-trust-funzionano-meglio-delle-vpn/)
[I dipendenti segnalano solo il 2% degli attacchi email](https://www.securityinfo.it/2023/02/20/i-dipendenti-segnalano-solo-il-2-degli-attacchi-email/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_camyclcamyclcamy-120x85.png)](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/ "Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT")

  [Scoperto ShadowLeak, un attacco che...](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/ "Permanent link to Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT")

  Set 30, 2025  [0](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/#respond)
* [![Ondata di attacc...