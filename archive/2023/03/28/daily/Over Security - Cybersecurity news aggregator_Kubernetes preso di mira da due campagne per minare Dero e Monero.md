---
title: Kubernetes preso di mira da due campagne per minare Dero e Monero
url: https://www.securityinfo.it/2023/03/27/vulnerabilita-kubernetes-dero-monero/?utm_source=rss&utm_medium=rss&utm_campaign=vulnerabilita-kubernetes-dero-monero
source: Over Security - Cybersecurity news aggregator
date: 2023-03-28
fetch_date: 2025-10-04T10:54:38.135789
---

# Kubernetes preso di mira da due campagne per minare Dero e Monero

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

## Kubernetes preso di mira da due campagne per minare Dero e Monero

Mar 27, 2023  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [Hacking](https://www.securityinfo.it/category/news/hacking-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2023/03/27/vulnerabilita-kubernetes-dero-monero/#respond)

---

[I ricercatori di Crowdstrike](https://www.crowdstrike.com/blog/crowdstrike-discovers-first-ever-dero-cryptojacking-campaign-targeting-kubernetes/) hanno individuato la **prima campagna di cryptojacking Dero che colpisce i cluster Kubernetes**. Secondo quanto riportato dal team di sicurezza, l’operazione sarebbe attiva già dall’inizio di febbraio scorso. Dero è una criptovaluta nata da poco i cui ideatori sostengono che offra più feature di anonimato rispetto a monete pensate per la privacy come Monero o Z-Cash.

Gli attaccanti hanno **preso di mira i cluster in esecuzione su porte non di default**, identificando i cluster vulnerabili che avevano l’autenticazione settata su “anonimo” e che permettevano quindi di autenticarsi senza alcun controllo.

![kubernetes dero](https://www.securityinfo.it/wp-content/uploads/2023/03/website-hosting-concept-with-circuits.jpg)

Freepik

Dopo un’interazione iniziale con le API, **gli attaccanti eseguivano un DaemonSet di Kubernetes che a sua volta eseguiva un pod malevolo su ogni nodo del cluster**. Questa operazione serviva agli attaccanti per **ottenere le risorse necessarie per il mining.**

**“Gli attaccanti non hanno tentato di cancellare o interrompere le operazioni del cluster”** si legge nel report Clowdstrike di Benjamin Grap e Manoj Ahuje. “Al contrario, hanno sviluppato un DaemonSet per minare Dero occultandolo coi nomi *proxy-api* e *pause*, termini comuni nei log di Kubernetes”. Gli attaccanti, quindi, guidavano la campagna per scopi esclusivamente economici.

Quella di Dero non è stata l’unica campagna di cryptojacking indirizzata ai cluster Kubernetes: pochi giorni dopo **Clowdstrike ha individuato una serie di operazioni analoghe che puntavano però a minare Monero.**

![kubernetes dero](https://www.securityinfo.it/wp-content/uploads/2023/03/hacking-4038037_1920.jpg)

Pixabay

Ciò che hanno scoperto i ricercatori è che i **cybercriminali dietro la campagna Monero erano a conoscenza di quella di Dero**, in quanto lo script della prima conteneva istruzioni per cancellare il DaemonSet *proxy-api*. **Il secondo gruppo di attaccanti è stato ancora più aggressivo del primo**: Crowdstrike ha esplicitato le differenze tra le due campagne, e ciò che salta all’occhio è che **i criminali che minavano Monero effettuavano anche escalation dei privilegi nei pod** e installavano servizi custom per ottenere il controllo completo dei nodi.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [cryptojacking](https://www.securityinfo.it/tag/cryptojacking/), [Cryptovalute](https://www.securityinfo.it/tag/cryptovalute/), [dero](https://www.securityinfo.it/tag/dero/), [Kubernetes](https://www.securityinfo.it/tag/kubernetes/), [mining criptovalute](https://www.securityinfo.it/tag/mining-criptovalute/), [Monero](https://www.securityinfo.it/tag/monero/)

[Il settore dei trasporti è nel mirino di ransomware e data breach](https://www.securityinfo.it/2023/03/27/settore-trasporti-ransomware-data-breach/)
[Le imprese temono lo stigma degli attacchi e non investono nella cybersecurity](https://www.securityinfo.it/2023/03/27/imprese-attacchi-cybersecurity/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Una nuova campagna sfrutta Selenium Grid per il mining di Monero](https://www.securityinfo.it/wp-content/uploads/2024/07/cyber-4747175_1920-120x85.jpg)](https://www.securityinfo.it/2024/07/29/una-nuova-campagna-sfrutta-selenium-grid-per-il-mining-di-monero/ "Una nuova campagna sfrutta Selenium Grid per il mining di Monero")

  [Una nuova campagna sfrutta Selenium...](https://www.securityinfo.it/2024/07/29/una-nuova-campagna-sfrutta-selenium-grid-per-il-mining-di-monero/ "Permanent link to Una nuova campagna sfrutta Selenium Grid per il mining di Monero")

  Lug 29, 2024  [0](https://www.securityinfo.it/2024/07/29/una-nuova-campagna-sfrutta-selenium-grid-per-il-mining-di-monero/#respond)
* [![Una campagna di cryptojacking colpisce i cluster Kubernetes mal configurati](https://www.securityinfo.it/wp-content/uploads/2024/06/hacking-4038037_1920-120x85.jpg)](https://www.securityinfo.it/2024/06/14/una-campagna-di-cryptojacking-colpisce-i-cluster-kubernetes-mal-configurati/ "Una campagna di cryptojacking colpisce i cluster Kubernetes mal configurati")

  [Una campagna di cryptojacking colpisce...](https://www.securityinfo.it/2024/06/14/una-campagna-di-cryptojacking-colpisce-i-cluster-kubernetes-mal-configurati/ "Permanent link to Una campagna di cryptojacking colpisce i cluster Kubernetes mal configurati")

  Giu 14, 2024  [0](https://www.securityinfo.it/2024/06/14/una-campagna-di-cryptojacking-colpisce-i-cluster-kubernetes-mal-configurati/#respond)
* [![Resi noti i dettagli di una vulnerabilità Kubernetes a rischio elevato](https://www.securityinfo.it/wp-content/uploads/2024/03/pattern-3232784_1920-120x85.jpg)](https://www.securityinfo.it/2024/03/15/resi-noti-i-dettagli-di-una-vulnerabilita-kubernetes-a-rischio-elevato/ "Resi noti i dettagli di una vulnerabilità Kubernetes a rischio elevato")

  [Resi noti i dettagli di una...](https://www.securityinfo.it/2024/03/15/resi-noti-i-dettagli-di-u...