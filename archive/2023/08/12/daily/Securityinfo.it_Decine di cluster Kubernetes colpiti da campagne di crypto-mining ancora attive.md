---
title: Decine di cluster Kubernetes colpiti da campagne di crypto-mining ancora attive
url: https://www.securityinfo.it/2023/08/11/decine-di-cluster-kubernetes-colpiti-da-campagne-di-crypto-mining-ancora-attive/?utm_source=rss&utm_medium=rss&utm_campaign=decine-di-cluster-kubernetes-colpiti-da-campagne-di-crypto-mining-ancora-attive
source: Securityinfo.it
date: 2023-08-12
fetch_date: 2025-10-04T12:02:34.576875
---

# Decine di cluster Kubernetes colpiti da campagne di crypto-mining ancora attive

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

## Decine di cluster Kubernetes colpiti da campagne di crypto-mining ancora attive

Ago 11, 2023  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2023/08/11/decine-di-cluster-kubernetes-colpiti-da-campagne-di-crypto-mining-ancora-attive/#respond)

---

[I ricercatori della compagnia di sicurezza Aqua](https://blog.aquasec.com/kubernetes-exposed-one-yaml-away-from-disaster) hanno individuato **diverse campagne di crypto-mining tuttora attive contro diversi cluster Kubernetes vulnerabili.** La compagnia aveva individuato cluster vulnerabili appartenenti a più di 350 organizzazioni, sia piccole-medie imprese che grandi aziende, e il 60% di questi è stato colpito dalla campagna malware.

Stando all’analisi dei ricercatori, **attualmente ci sono 3 [campagne di crypto-mining](https://www.securityinfo.it/2023/03/27/vulnerabilita-kubernetes-dero-monero/)** attive, oltre a **una campagna che sfrutta il Role-Base Access Control di Kubernetes** per creare backdoor nei cluster e **una campagna di TeamTNT  per ottenere credenziali.**

![Kubernetes - Credits: SergeyNivens- Depositphotos](https://www.securityinfo.it/wp-content/uploads/2023/08/Depositphotos_499558608_L.jpg)

Credits: SergeyNivens- Depositphotos

Il team di sicurezza ha individuato **due principali vulnerabilità** nei cluster analizzati: una, già conosciuta, consente l’**accesso anonimo alle macchine con i privilegi di amministratore**; l’altra sfrutta invece l’**esecuzione del proxy `kubectl` per esporre il cluster in rete**, rendendolo un target per gli attacchi.

La prima vulnerabilità riguarda l’impostazione per l’autenticazione anonima che è permessa di default. **Gli utenti anonimi non hanno privilegi, ma possono effettuare comunque richieste al cluster**. Combinata con altre vulnerabilità o impostazioni errate, spiegano i ricercatori, questa configurazione può portare gli attaccanti a ottenere accesso completo al cluster, potenzialmente compromettendo tutte le applicazioni in esecuzione.

La seconda vulnerabilità riguarda invece il comando `kubectl proxy` che consente di creare un proxy per inoltrare le richieste al server API di Kubernetes. Eseguendo il comando coi flag `` --address=`0.0.0.0` --accept-hosts `.*` `` **il proxy accetta tutte le richieste da qualsiasi host, per di più con gli stessi privilegi dell’utente che ha eseguito il comando.**

![Kubernetes ](https://www.securityinfo.it/wp-content/uploads/2023/08/cyber-security-7231027_1920.jpg)

Pixabay

Le conseguenze degli attacchi ai cluster Kubernetes potrebbero essere disastrose: **i cluster colpiti contengono dati sensibili** sia dell’azienda proprietaria che dei suoi clienti, **record finanziari**, proprietà intellettuali, **credenziali** di accesso all’infrastruttura, certificati e **chiavi di cifratura.**

La maggior parte delle aziende, a prescindere dalla grandezza, ha problemi di configurazione dei cluster, indice di una **grave carenza nella gestione della sicurezza**. I ricercatori consigliano innanzitutto di configurare il proxy kubectl in modo che non sia raggiungibile dal web, all’interno di un ambiente sicuro e accessibile solo agli utenti autorizzati.

Le organizzazioni dovrebbero inoltre promuovere audit regolari per le attività dei cluster e **implementare soluzioni per il controllo degli accessi**, oltre a **investire nel training dello staff sui rischi delle configurazioni errate.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [cluster](https://www.securityinfo.it/tag/cluster/), [configurazione](https://www.securityinfo.it/tag/configurazione/), [crypto-mining](https://www.securityinfo.it/tag/crypto-mining/), [CryptoLocker](https://www.securityinfo.it/tag/cryptolocker/), [Kubernetes](https://www.securityinfo.it/tag/kubernetes/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[Downfall: Intel era a conoscenza della vulnerabilità da un anno](https://www.securityinfo.it/2023/08/14/downfall-intel-era-a-conoscenza-della-vulnerabilita-da-un-anno/)
[Wazuh, la soluzione open-source per migliorare la sicurezza aziendale](https://www.securityinfo.it/2023/08/10/wazuh-la-soluzione-open-source-per-migliorare-la-sicurezza-aziendale/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_d4x8rid4x8rid4x8-120x85.png)](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  [Firewall Cisco sotto attacco: una nuova...](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Permanent link to Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  Set 29, 2025  [0](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/#respond)
* [![Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.](https://www.securityinfo.it/wp-content/uploads/2025/09/ai-generated-9053184_1920-120x85.jpg)](https://www.securityinfo.it/2025/09/24/attaccanti-s...