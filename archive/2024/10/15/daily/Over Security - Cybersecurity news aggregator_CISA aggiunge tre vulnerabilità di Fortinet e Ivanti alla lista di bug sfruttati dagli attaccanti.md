---
title: CISA aggiunge tre vulnerabilità di Fortinet e Ivanti alla lista di bug sfruttati dagli attaccanti
url: https://www.securityinfo.it/2024/10/14/cisa-aggiunge-tre-vulnerabilita-di-fortinet-e-ivanti-alla-lista-di-bug-sfruttati-dagli-attaccanti/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-15
fetch_date: 2025-10-06T18:53:58.556270
---

# CISA aggiunge tre vulnerabilità di Fortinet e Ivanti alla lista di bug sfruttati dagli attaccanti

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

## CISA aggiunge tre vulnerabilità di Fortinet e Ivanti alla lista di bug sfruttati dagli attaccanti

Ott 14, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2024/10/14/cisa-aggiunge-tre-vulnerabilita-di-fortinet-e-ivanti-alla-lista-di-bug-sfruttati-dagli-attaccanti/#respond)

---

Lo scorso mercoledì la CISA (Cybersecurity & Infrastructure Security Agency) [ha aggiunto](https://www.cisa.gov/news-events/alerts/2024/10/09/cisa-adds-three-known-exploited-vulnerabilities-catalog) **tre vulnerabilità alla lista di bug attivamente sfruttati** dagli attaccanti. Le vulnerabilità, a rischio medio, elevato e critico, colpiscono alcuni prodotti **Fortinet** e l’**Ivanti Cloud Services Appliance (CSA)**.

![vulnerabilità Fortinet Ivanti](https://www.securityinfo.it/wp-content/uploads/2024/10/hacker-8858353_1920.jpg)

Il **[bug](https://www.securityinfo.it/2024/10/02/trovate-vulnerabilita-critiche-nei-sistemi-di-misurazione-automatica-del-livello-dei-serbatoi/) più critico**, tracciato come **CVE-2024-23113**, colpisce alcune versioni di **FortiOS** (dalla 7.4.0 alla 7.4.2,dalla 7.2.0 alla 7.2.6, dalla 7.0.0 alla 7.0.13), di **FortiProxy** (dalla 7.4.0 alla 7.4.2, dalla 7.2.0 alla 7.2.8, dalla 7.0.0 alla 7.0.14), di **FortiPAM** (la 1.2.0, dalla 1.1.0 alla 1.1.2, dalla 1.0.0 alla 1.0.3,) e di **FortiSwitchManager** (dalla 7.2.0 alla 7.2.3, dalla 7.0.0 alla 7.0.3) e consente a un attaccante di **eseguire codice o inviare comandi senza autorizzazione**, sfruttando pacchetti creati appositamente. Si tratta di una **format-string** **vulnerability** che colpisce il demone fgfmd dei prodotti indicati e, secondo quanto riportato dal CISA, è attivamente sfruttata dagli attaccanti.

La seconda vulnerabilità, tracciata come CVE-**2024-938**0 e considerata a **rischio elevato**, è una **OS command injection** presente nella **console admin web di Ivanti CSA**, nelle versioni precedenti alla 5.0.2. Il bug permette a un attaccante remoto e autenticato con privilegi di admin di **eseguire codice da remoto**. Il problema deriva da una neutralizzazione errata di alcuni elementi inseriti nei comandi che rende vulnerabili i componenti della suite.

La vulnerabilità a criticità **media**, la **CVE-2024-9379**, è invece una **SQL injection** che colpisce a sua volta la console admin web di Ivanti CSA, sempre nelle versioni precedenti alla 5.0.2. Un attaccante remoto con privilegi di amministratore può **eseguire query SQL arbitrarie per ottenere dati sensibili, cancellarli o alterarli.**

Le tre vulnerabilità di Fortinet e Ivanti sono state risolte dai vendor nelle ultime versioni dei software. Gli utenti sono invitati ad **aggiornare il prima possibile i prodotti colpiti dai bug.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [CISA](https://www.securityinfo.it/tag/cisa/), [command injection](https://www.securityinfo.it/tag/command-injection/), [Format String vulnerability](https://www.securityinfo.it/tag/format-string-vulnerability/), [fortinet](https://www.securityinfo.it/tag/fortinet/), [ivanti](https://www.securityinfo.it/tag/ivanti/), [SQL Injection](https://www.securityinfo.it/tag/sql-injection/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[Rilasciato il fix per una vulnerabilità critica di Jetpack per WordPress](https://www.securityinfo.it/2024/10/15/rilasciato-il-fix-per-una-vulnerabilita-critica-di-jetpack-per-wordpress/)
[CERT-AGID 5-11 ottobre: 378 IoC e una campagna di phishing che basata sulla Polizia di Stato](https://www.securityinfo.it/2024/10/14/cert-agid-5-11-ottobre-378-ioc-e-una-campagna-di-phishing-che-basata-sulla-polizia-di-stato/)

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
* [...