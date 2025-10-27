---
title: WhoFi: da La Sapienza arriva un sistema di riconoscimento biometrico basato sul Wi-Fi
url: https://www.securityinfo.it/2025/07/23/whofi-da-la-sapienza-arriva-un-sistema-di-riconoscimento-biometrico-basato-sul-wi-fi/?utm_source=rss&utm_medium=rss&utm_campaign=whofi-da-la-sapienza-arriva-un-sistema-di-riconoscimento-biometrico-basato-sul-wi-fi
source: Securityinfo.it
date: 2025-07-24
fetch_date: 2025-10-06T23:55:33.457356
---

# WhoFi: da La Sapienza arriva un sistema di riconoscimento biometrico basato sul Wi-Fi

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

## WhoFi: da La Sapienza arriva un sistema di riconoscimento biometrico basato sul Wi-Fi

Lug 23, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/07/23/whofi-da-la-sapienza-arriva-un-sistema-di-riconoscimento-biometrico-basato-sul-wi-fi/#respond)

---

Dall’Università La Sapienza di Roma arriva **WhoFi**, un nuovo sistema che migliora le operazioni di **re-identificazione (Re-ID)**sfruttando le alterazioni delle onde del Wi-Fi.

Con re-identificazione si intende il processo di **identificare una stessa persona su registrazioni o immagini di più sistemi di videosorveglianza**; nel dettaglio, si tratta di riuscire a determinare se due rappresentazioni sono riferite a uno stesso individuo oppure no.

![WhoFi](https://www.securityinfo.it/wp-content/uploads/2025/07/Gemini_Generated_Image_dow2bbdow2bbdow2.png)

Come spiegano i ricercatori nel [paper](https://arxiv.org/html/2507.12869v1) relativo alla loro ricerca**, i metodi tradizionali di riconoscimento biometrico si basano sul confronto di caratteristiche visive**, come il colore dei vestiti o la forma del corpo, per identificare potenziali persone di interesse tra due registrazioni o tra una registrazione e delle immagini d’archivio. Questi metodi però soffrono di alcune **limitazioni** che complicano l’analisi, quali una certa sensibilità ai cambiamenti delle condizioni luminose, occlusioni, elementi di disturbo sullo sfondo e la diversa angolazione delle videocamere.

“*Queste sfide spesso comportano una riduzione della robustezza, specialmente in ambienti non vincolati o reali. Per superare queste limitazioni, una strada alternativa della ricerca esplora **modalità non visive, come il Re-ID basato su Wi-Fi***” spiegano i ricercatori Danilo Avola, Daniele Pannone, Dario Montagnini ed Emad Emam.

WhoFi si basa sull’idea che la **forma dell’onda del segnale Wi-Fi che si propaga in un ambiente viene alterata dalla presenza di ostacoli**, come oggetti e persone, in base alle loro caratteristiche fisiche. Queste alterazioni, catturate e classificate come Channel State Information, una proprietà che descrive la propagazione del segnale Wi-Fi, forniscono importanti informazioni biometriche per identificare una persona.

“*A differenza dei sistemi ottici che percepiscono solo la superficie esterna di una persona, **i segnali Wi-Fi interagiscono con le strutture interne, come ossa, organi e composizione corporea, determinando distorsioni del segnale specifiche per ogni persona** che fungono da firma unica*” continuano i ricercatori.

![biometria](https://www.securityinfo.it/wp-content/uploads/2025/07/Gemini_Generated_Image_td6fhgtd6fhgtd6f.png)

Di fatto studiando il modo in cui il segnale Wi-Fi viene alterato dal singolo, è possibile creare una **“firma biometrica” univoca** per essere in grado di identificare un soggetto precisamente e su diversi sistemi. Stando ai benchmark condivisi dai ricercatori, WhoFi è riuscito a raggiungere una **precisione del 95.5%**.

“***I risultati incoraggianti ottenuti confermano la validità dei segnali Wi-Fi come modalità biometrica robusta** e in grado di preservare la privacy, e posizionano questo studio come un significativo passo avanti nello sviluppo di sistemi Re-ID basati sui segnali*” concludono i ricercatori.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Re-ID](https://www.securityinfo.it/tag/re-id/), [re-identificazione](https://www.securityinfo.it/tag/re-identificazione/), [riconoscimento biometrico](https://www.securityinfo.it/tag/riconoscimento-biometrico/), [videosorveglianza](https://www.securityinfo.it/tag/videosorveglianza/), [WhoFi](https://www.securityinfo.it/tag/whofi/), [Wi-Fi](https://www.securityinfo.it/tag/wi-fi/)

[Voci IA indistinguibili da quelle reali: Sam Altman lancia l'allarme](https://www.securityinfo.it/2025/07/24/voci-ia-indistinguibili-da-quelle-reali-sam-altman-lancia-lallarme/)
[Attacco ToolShell a Sharepoint: i criminali hanno iniziato usarlo almeno dal 7 luglio](https://www.securityinfo.it/2025/07/22/attacco-toolshell-a-sharepoint-i-criminali-hanno-iniziato-usarlo-almeno-dal-7-luglio/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Il 25% dei Wi-Fi pubblici di Parigi non è sicuro](https://www.securityinfo.it/wp-content/uploads/2024/07/nature-2564502_1920-120x85.jpg)](https://www.securityinfo.it/2024/07/26/il-25-dei-wi-fi-pubblici-di-parigi-non-e-sicuro/ "Il 25% dei Wi-Fi pubblici di Parigi non è sicuro")

  [Il 25% dei Wi-Fi pubblici di Parigi non...](https://www.securityinfo.it/2024/07/26/il-25-dei-wi-fi-pubblici-di-parigi-non-e-sicuro/ "Permanent link to Il 25% dei Wi-Fi pubblici di Parigi non è sicuro")

  Lug 26, 2024  [0](https://www.securityinfo.it/2024/07/26/il-25-dei-wi-fi-pubblici-di-parigi-non-e-sicuro/#respond)
* [![GoldPickaxe, il malware iOS che ti ruba il volto](https://www.securityinfo.it/wp-content/uploads/2024/02/scam-4126798_1920-120x85.jpg)](https://www.securityinfo.it/2024/02/15/goldpickaxe-il-malware-ios-che-ti-ruba-il-volto/ "GoldPickaxe, il malware iOS che ti ruba il volto")

  [GoldPickaxe, il malware iOS che ti ruba...](https://www.securityinfo.it/2024/02/15/goldpickaxe-il-malware-ios-che-ti-ruba-il-volto/ "Permanent link to GoldPickaxe, il malware iOS che ti ruba il volto")

  Feb 15, 2024  [0](https://www.securityinfo.it/2024/02/15/goldpickaxe-il-malware-ios-che-ti-ruba-il-volto/#respond)
* [...