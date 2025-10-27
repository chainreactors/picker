---
title: Smartwatch e attacchi acustici: nuova minaccia alle reti isolate
url: https://www.securityinfo.it/2025/06/12/smartwatch-e-attacchi-acustici-nuova-minaccia-alle-reti-isolate/?utm_source=rss&utm_medium=rss&utm_campaign=smartwatch-e-attacchi-acustici-nuova-minaccia-alle-reti-isolate
source: Securityinfo.it
date: 2025-06-13
fetch_date: 2025-10-06T23:00:02.797158
---

# Smartwatch e attacchi acustici: nuova minaccia alle reti isolate

Aggiornamenti recenti Ottobre 6th, 2025 3:00 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Microsoft Sentinel: arriva l’era degli agenti AI e della difesa predittiva](https://www.securityinfo.it/2025/10/06/microsoft-sentinel-arriva-lera-degli-agenti-ai-e-della-difesa-predittiva/)
* [CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)
* [Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)

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

## Smartwatch e attacchi acustici: nuova minaccia alle reti isolate

Giu 12, 2025  [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo/ "Articoli scritti da Giancarlo Calzetta")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [Hacking](https://www.securityinfo.it/category/news/hacking-news/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/06/12/smartwatch-e-attacchi-acustici-nuova-minaccia-alle-reti-isolate/#respond)

---

Le reti **air-gapped**, ovvero fisicamente separate da Internet e da altri sistemi esterni, sono considerate il baluardo massimo della sicurezza informatica. **Eppure, che non siano invulnerabili lo sappiamo dai tempi di Stuxnet** e adesso arriva l’ennesima dimostrazione sotto forma di ricerca proveniente dal mondo accademico israeliano, che ha svelato un inedito metodo di esfiltrazione dei dati basato sull’uso dei microfoni integrati nei comuni smartwatch.

Questa tecnica, **battezzata *SmartAttack*,** sfrutta la capacità degli altoparlanti integrati nei computer compromessi di emettere segnali ultrasonici che, pur non essendo percepibili dall’orecchio umano, possono essere captati da dispositivi indossabili presenti nell’ambiente. **Il tutto avviene senza interferire con le normali operazioni del sistema bersaglio,** rendendo l’attacco quasi impercettibile dal punto di vista operativo e visivo. **Anche un semplice smartwatch al polso di un dipendente può diventare un alleato inconsapevole dell’attaccante.**

Il principio di funzionamento è noto agli esperti di canali di attacco non convenzionali: un malware installato su una macchina air-gapped raccoglie informazioni sensibili, come password, chiavi crittografiche o sequenze di tasti, e le converte in segnali sonori modulati in frequenza. **Attraverso una tecnica chiamata Binary Frequency Shift Keying (B-FSK), i dati vengono codificati in forma binaria utilizzando frequenze intorno ai 19 kHz.** La trasmissione può avvenire a una distanza di alcuni metri, ma **richiede che lo smartwatch sia posizionato con visibilità diretta verso il computer sorgente.**

L’ideatore di SmartAttack è Mordechai Guri, ricercatore già noto per aver proposto metodi “alternativi” di data-leaking da ambienti segregati, tra cui emissioni elettromagnetiche da cavi SATA o variazioni luminose nei LED delle schede di rete. **E anche stavolta l’obiettivo è mostrare che, con le giuste condizioni e conoscenze, persino una separazione fisica dalla rete può essere aggirata.** **Il progetto rientra in una più ampia linea di ricerca dedicata ai cosiddetti “covert channels”.**

Naturalmente, un attacco del genere non è di facile realizzazione. Occorre prima infettare il sistema isolato, un’impresa che può avvenire tramite un insider, tramite supply chain compromessa o dispositivi USB inseriti manualmente. **Inoltre, gli smartwatch non dispongono di microfoni ad alte prestazioni e la decodifica del segnale acustico diventa tanto più difficile quanto più aumenta la distanza o l’angolo di ricezione.** **I ricercatori hanno dimostrato che, nelle condizioni ideali, è possibile trasmettere da 5 a 50 bit al secondo fino a una distanza massima di circa nove metri.** Insomma, si torna a livelli “pre Commodore 64”, ma per scopi ben specifici.

Per mitigare il rischio, le contromisure più efficaci rimangono l’eliminazione fisica dei componenti vulnerabili. **Disabilitare o rimuovere gli speaker integrati dai sistemi critici rappresenta una protezione robusta non solo contro SmartAttack, ma contro tutti i canali acustici noti.** In ambienti dove ciò non è possibile, **si può ricorrere all’uso di disturbi ultrasonici, tecniche di jamming, filtri software e misure di “audio-gapping”.**

Al di là dell’applicabilità immediata, lo studio dimostra ancora una volta quanto sia sottile la linea tra teoria e pratica nella cybersecurity. **Ogni nuova tecnologia, anche quella indossata al polso, può trasformarsi in un vettore d’attacco se non gestita con consapevolezza.** **Il valore di questa ricerca risiede nel mettere in guardia anche su minacce che oggi sembrano improbabili ma che, domani, potrebbero concretizzarsi.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [attacco air-gapped](https://www.securityinfo.it/tag/attacco-air-gapped/), [cybersecurity industriale](https://www.securityinfo.it/tag/cybersecurity-industriale/), [esfiltrazione dati acustica](https://www.securityinfo.it/tag/esfiltrazione-dati-acustica/), [Mordechai Guri](https://www.securityinfo.it/tag/mordechai-guri/), [sicurezza infrastrutture critiche](https://www.securityinfo.it/tag/sicurezza-infrastrutture-critiche/), [smartwatch malware](https://www.securityinfo.it/tag/smartwatch-malware/), [ultrasonico covert channel](https://www.securityinfo.it/tag/ultrasonico-covert-channel/)

[EchoLeak: è arrivata la prima vulnerabilità zero clic per le IA (Microsoft 365 Copilot)](https://www.securityinfo.it/2025/06/13/echoleak-e-arrivata-la-prima-vulnerabilita-zero-clic-per-le-ia-microsoft-365-copilot/)
[Microsoft rilascia patch per 67 bug, di cui uno già sfruttato](https://www.securityinfo.it/2025/06/11/microsoft-rilascia-patch-per-67-bug-di-cui-uno-gia-sfruttato/)

---

![](https://secure.gravatar.com/avatar/93ad3a1bbb47d1f5755e4f5086cb3f22?s=90&d=mm&r=g)

##### [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo/)

##### Articoli correlati

* [![Attacchi a computer isolati attraverso il giroscopio del cellulare](https://www.securityinfo.it/wp-content/uploads/2022/08/mobile-1419277_1920-120x85.jpg)](https://www.securityinfo.it/2022/08/24/attacchi-a-computer-isolati-attraverso-il-giroscopio-del-cellulare/ "Attacchi a computer isolati attraverso i...