---
title: Inception, l’attacco che “impianta” previsioni false nelle CPU AMD
url: https://www.securityinfo.it/2023/08/23/inception-lattacco-che-impianta-previsioni-false-nelle-cpu-amd/
source: Over Security - Cybersecurity news aggregator
date: 2023-08-24
fetch_date: 2025-10-04T12:03:20.308805
---

# Inception, l’attacco che “impianta” previsioni false nelle CPU AMD

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

## Inception, l’attacco che “impianta” previsioni false nelle CPU AMD

Ago 23, 2023  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2023/08/23/inception-lattacco-che-impianta-previsioni-false-nelle-cpu-amd/#respond)

---

I ricercatori di ETH Zurich hanno individuato un **pericoloso attacco che sfrutta la tecnologia di ottimizzazione delle moderne CPU.** Chiamato “Inception”, l’attacco è in grado di accedere a dati sensibili sfruttando la vulnerabilità presente su tutte le CPU AMD Zen, compresi gli ultimi modelli.

Come si legge sul [report dei ricercatori](https://comsec.ethz.ch/research/microarch/inception/), **gli attaccanti sfruttano l’esecuzione speculativa e una tecnica chiamata “speculazione fantasma” per accedere a informazioni sensibili senza ottenere privilegi di amministratore.**

La prima è una funzionalità presente sui processori moderni che consente di **aumentare le performance anticipando l’esecuzione di istruzioni prima di conoscere il risultato delle precedenti**, riducendo il costo dei task condizionali.  L’esecuzione speculativa espone informazioni sensibili, comprese quelle nella memoria nel kernel, e le rende accessibili anche da processi con meno privilegi, come le applicazioni dannose in esecuzione sul dispositivo.

![Inception - Credits: FreedomImage- Depositphotos](https://www.securityinfo.it/wp-content/uploads/2023/08/Depositphotos_1443628_L.jpg)

Credits: FreedomImage- Depositphotos

La seconda tecnica sfrutta invece una vulnerabilità dei processori AMD che consente agli attaccanti di **scatenare previsioni errate, esponendo i dati sensibili.**

L’unione di queste due tecniche ha dato origine a una **catena di attacco estremamente pericolosa in cui gli attaccanti “iniettano” previsioni errate.** “Come nel film con lo stesso nome, Inception impianta un’idea nella CPU mentre, in un certo senso, sta ‘sognando’ per portarla a eseguire azioni errata basate su esperienze auto-concepite” spiegano i ricercatori.

Ciò che fanno gli attaccanti è **creare un flusso di controllo inesistente**, “fantasma”, **per dirottare il flusso dell’esecuzione speculativa** facendo credere alla CPU che un’istruzione XOR sia in realtà una chiamata ricorsiva, causando un overflow del buffer dello stack di ritorno in un indirizzo di destinazione definito dall’attaccante.

![Inception](https://www.securityinfo.it/wp-content/uploads/2023/08/circuit-board-2440249_1920.jpg)

Pixabay

**Un modo per mitigare il problema è svuotare il branch che si occupa delle predizioni** (Branch Predictor Unit, BPU) prima di cambiare contesto; questo approccio, però, **riduce notevolmente le prestazioni della CPU**, con un overhead che va dal 93,1% al 216,9% nelle architetture Zen 1 e Zen 2.

In un [avviso di sicurezza](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-7005.html), AMD ha specificato di non essere a conoscenza di casi in cui è stato eseguito Inception, e che **l’attacco può essere eseguito soltanto in locale**. Il consiglio è comunque quello di a**ggiornare il BIOS e applicare le patch di sicurezza previste.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [AMD](https://www.securityinfo.it/tag/amd/), [CPU](https://www.securityinfo.it/tag/cpu/), [esecuzione speculativa](https://www.securityinfo.it/tag/esecuzione-speculativa/), [ETH Zurich](https://www.securityinfo.it/tag/eth-zurich/), [flusso d'esecuzione](https://www.securityinfo.it/tag/flusso-desecuzione/), [inception](https://www.securityinfo.it/tag/inception/)

[Scoperta una botnet basata su ChatGPT attiva su Twitter (ops, X!)](https://www.securityinfo.it/2023/08/24/una-crypto-botnet-basata-su-chatgpt-spopola-su-twitter-ops-x/)
[Qbot non molla la presa: il trojan è la minaccia principale in Italia](https://www.securityinfo.it/2023/08/22/qbot-non-molla-la-presa-il-trojan-e-la-minaccia-principale-in-italia/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Cina contro Nvidia: dubbi sulla sicurezza dei chip AI e sospetti di backdoor](https://www.securityinfo.it/wp-content/uploads/2025/08/nVidia-13-ago-2025CG-120x85.png)](https://www.securityinfo.it/2025/08/13/cina-contro-nvidia-dubbi-sulla-sicurezza-dei-chip-ai-e-sospetti-di-backdoor/ "Cina contro Nvidia: dubbi sulla sicurezza dei chip AI e sospetti di backdoor")

  [Cina contro Nvidia: dubbi sulla...](https://www.securityinfo.it/2025/08/13/cina-contro-nvidia-dubbi-sulla-sicurezza-dei-chip-ai-e-sospetti-di-backdoor/ "Permanent link to Cina contro Nvidia: dubbi sulla sicurezza dei chip AI e sospetti di backdoor")

  Ago 13, 2025  [0](https://www.securityinfo.it/2025/08/13/cina-contro-nvidia-dubbi-sulla-sicurezza-dei-chip-ai-e-sospetti-di-backdoor/#respond)
* [![Ransomware che infettano la CPU: una nuova, potenziale minaccia](https://www.securityinfo.it/wp-content/uploads/2025/05/2151883593-120x85.jpg)](https://www.securityinfo.it/2025/05/13/ransomware-che-infettano-la-cpu-una-nuova-potenziale-minaccia/ "Ransomware che infettano la CPU: una nuova, potenziale minaccia")

  [Ransomware che infettano la CPU: una...](https://www.securityinfo.it/2025/05/13/ransomware-che-infettano-la-cpu-una-nuova-potenziale-minaccia/ "Permanent link to Ransomware che infettano la CPU: una nuova, potenziale minaccia")

  Mag 13, 2025  [0](https://www.securityinfo.it/2025/05/13/ransomware-che-infettano-la-cpu-una-nuova-potenziale-minaccia/#respond)
* [![Spectre è ancora presente nei...