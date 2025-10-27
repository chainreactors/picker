---
title: Apache HugeGraph-Server è sotto attacco: scoperta una vulnerabilità critica
url: https://www.securityinfo.it/2024/07/18/apache-hugegraph-e-sotto-attacco-scoperta-una-vulnerabilita-critica/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-19
fetch_date: 2025-10-06T17:42:52.893624
---

# Apache HugeGraph-Server è sotto attacco: scoperta una vulnerabilità critica

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

## Apache HugeGraph-Server è sotto attacco: scoperta una vulnerabilità critica

Lug 18, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2024/07/18/apache-hugegraph-e-sotto-attacco-scoperta-una-vulnerabilita-critica/#respond)

---

**Apache HugeGraph-Server è sotto attacco**: i cybercriminali stanno sfruttando una **vulnerabilità critica** del database per eseguire codice remoto sulle istanze colpite.

HugeGraph è un graph database [open-source](https://www.securityinfo.it/2024/06/28/piu-della-meta-dei-software-open-source-critici-non-usa-codice-memory-safe/) implementato nel framework TinkerPop3. Gli scenari applicativi del database includono l’esplorazione delle relazioni tra oggetti (nodi), analisi associative, ricerca di percorsi, estrazione di feature, clustering dei dati, community detection e grafi di conoscenza.

![vulnerabilità Apache](https://www.securityinfo.it/wp-content/uploads/2024/07/hacker-8033977_1920.jpg)

Pixabay

Il bug, CVE-2024-27348, colpisce l’**API Gremlin graph traversal language**, il linguaggio funzionale di Apache ThinkerPop che consente agli utenti di esprimere query complesse in maniera semplice e ridotta sul property graph della loro applicazione.

I ricercatori di [SecureLayer7](https://blog.securelayer7.net/remote-code-execution-in-apache-hugegraph/) hanno approfondito l’exploit della vulnerabilità di Apache spiegando che **può essere usata per bypassare i controlli e le restrizioni della sandbox.** Nel dettaglio, il SecurityManager di Gremlin manca del reflection filtering e consente a un attaccante di manipolare diverse funzioni della classe, permettendogli in ultima analisi di eludere i controlli della sandbox.

A individuare gli attacchi sono stati i ricercatori di The Shadowserver Foundation: “*Stiamo osservando tentativi di sfruttamento della CVE-2024-27348 di Apache HugeGraph-Server “POST /gremlin” da più sorgenti. **Il codice della PoC è disponibile dall’inizio di giugno.** Se state eseguendo HugeGraph, assicuratevi di aggiornarlo*” hanno spiegato in un [post su X](https://infosec.exchange/%40shadowserver/112795058069606954).

Le versioni vulnerabili di HugeGraph-Server sono dalla 1.0.0 a prima della 1.3.0 in Java 8 e Java 11. **Apache consiglia di aggiornare il prima possibile il database alla versione 1.3.0 con Java 11 e abilitare il sistema Auth.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [APache](https://www.securityinfo.it/tag/apache/), [esecuzione codice remoto](https://www.securityinfo.it/tag/esecuzione-codice-remoto/), [graph database](https://www.securityinfo.it/tag/graph-database/), [Gremlin](https://www.securityinfo.it/tag/gremlin/), [HughGraph-Server](https://www.securityinfo.it/tag/hughgraph-server/), [Open Source](https://www.securityinfo.it/tag/open-source/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[Cresce il numero di attacchi informatici: +30% nel Q2 2024](https://www.securityinfo.it/2024/07/19/cresce-il-numero-di-attacchi-informatici-30-nel-q2-2024/)
[Un APT cinese ha colpito entità governative in Italia](https://www.securityinfo.it/2024/07/18/un-apt-cinese-ha-colpito-entita-governative-in-italia/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_d4x8rid4x8rid4x8-120x85.png)](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  [Firewall Cisco sotto attacco: una nuova...](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Permanent link to Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  Set 29, 2025  [0](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/#respond)
* [![Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.](https://www.securityinfo.it/wp-content/uploads/2025/09/ai-generated-9053184_1920-120x85.jpg)](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/ "Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.")

  [Attaccanti sfruttano un bug di...](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/ "Permanent link to Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.")

  Set 24, 2025  [0](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/#respond)
* [![Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/09/08/una-vulnerabilita-critica-di-sap-s-4hana-e-stata-sfruttata-dai-cybecriminali/ "Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali")

  [Una vulnerabilità critica di SAP...](https://www.securityinfo.it/2025/09/08/una-vulnerabilita-critica-di-sap-s-4hana-e-stata-sfruttata-dai-cybecriminali/ "Permanent link...