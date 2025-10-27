---
title: Le stampanti Brother sono piene di bug. Uno espone la password di admin
url: https://www.securityinfo.it/2025/06/27/le-stampanti-brother-sono-piene-di-bug-uno-espone-la-password-di-admin/
source: Over Security - Cybersecurity news aggregator
date: 2025-06-28
fetch_date: 2025-10-06T22:56:29.047865
---

# Le stampanti Brother sono piene di bug. Uno espone la password di admin

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

## Le stampanti multifunzione sono piene di bug! Uno espone la password di admin e Brother fa il record

Giu 27, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/06/27/le-stampanti-brother-sono-piene-di-bug-uno-espone-la-password-di-admin/#respond)

---

Durante un processo di analisi di vulnerabilità zero-day, la compagnia di cybersecurity **Rapid7** ha individuato **8 bug che colpiscono centinaia di stampanti Brother**; uno di questi bug, considerato critico, consente a un attaccante di **ottenere la password di amministratore** del dispositivo. I bug, individuati a maggio dello scorso anno, sono stati resi noti solo ora.

Secondo il [report](https://www.rapid7.com/blog/post/multiple-brother-devices-multiple-vulnerabilities-fixed/) di Rapid7, **i modelli vulnerabili ad almeno uno dei bug individuati sono ben 689** e comprendono, oltre che le stampanti, anche scanner e dispositivi per l’etichettatura. I bug però non colpiscono solo il marchio Brother: tra i modelli di stampanti che soffrono delle vulnerabilità scoperte ce ne sono 46 della FUJIFLM Business Innovation, 5 di Ricoh, 2 di Toshiba Tec Corporation e 6 di Monika Minolta. In totale, si contano **748 modelli di 5 diversi vendor vulnerabili** a uno o più dei bug individuati (689 di Brother).

![Brother bug](https://www.securityinfo.it/wp-content/uploads/2025/06/Gemini_Generated_Image_c97drsc97drsc97d.png)

Il bug più grave, tracciato come CVE-2024-51978, permette a un attaccante di **ottenere il numero di serie del dispositivo e usarlo per recuperare la password di amministratore**. “*Ciò è dovuto alla scoperta della procedura di generazione della password predefinita utilizzata dai dispositivi Brother*” spiega Stephen Fewer di Rapid7. “*Questa procedura trasforma un numero di serie in una password predefinita. La password predefinita dei dispositivi interessati è stata impostata durante il processo di produzione, in base al numero di serie univoco di ciascun dispositivo*“.

Una volta ottenuta la password, gli attaccanti possono riconfigurare il dispositivo a proprio piacimento, accedere ai documenti salvati e sfruttare le altre vulnerabilità del modello.

Poiché la vulnerabilità risiede nella logica stessa del processo produttivo, Brother ha specificato che **il bug non può essere risolto con aggiornamenti del firmware**e che richiede un cambiamento nella produzione dei modelli.

Delle altre vulnerabilità, **tre sono considerate di gravità elevata.** Due di esse (CVE-2024-51982 e CVE-2024-51983) consentono a un attaccante di interrompere l’operatività del dispositivo, mentre la terza (CVE-2024-51978) permette di scatenare un buffer-overflow.

Le altre quattro vulnerabilità sono considerate di gravità media: la CVE-2024-51977 permette a un attaccante di esporre informazioni sensibili; la CVE-2024-51980 consente invece di forzare il dispositivo ad aprire una connessione TCP; la CVE-2024-51981 permette di forzare il dispositivo a eseguire una richiesta HTTP; infine, la CVE-2024-51984 consente a un attaccante di ottenere la password di un dispositivo esterno.

Brother ha rilasciato aggiornamenti firmware per tutte le vulnerabilità. Nel caso della CVE-2024-51978, **l’aggiornamento non risolve il bug, ma applica un workaround per limitare i rischi.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [aggiornamento di sicurezza](https://www.securityinfo.it/tag/aggiornamento-di-sicurezza/), [Brother](https://www.securityinfo.it/tag/brother/), [bug](https://www.securityinfo.it/tag/bug/), [password amministratore](https://www.securityinfo.it/tag/password-amministratore/), [Rapid7](https://www.securityinfo.it/tag/rapid7/), [stampanti](https://www.securityinfo.it/tag/stampanti/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[Una vulnerabilità di Open VSX Registry mette in pericolo milioni di sviluppatori](https://www.securityinfo.it/2025/06/30/una-vulnerabilita-di-open-vsx-registry-mette-in-pericolo-milioni-di-sviluppatori/)
[L'Iran lancia un attacco di spear-phishing contro obiettivi israeliani](https://www.securityinfo.it/2025/06/26/liran-lancia-un-attacco-di-spear-phishing-contro-obiettivi-israeliani/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_d4x8rid4x8rid4x8-120x85.png)](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  [Firewall Cisco sotto attacco: una nuova...](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Permanent link to Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  Set 29, 2025  [0](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/#respond)
* [![Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.](https://www.securityinfo.it/wp-content/uploads/2025/09/ai-generated-9053184_1920-120x85.jpg)](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/ "Attaccanti sfruttano un bug di GeoServer ...