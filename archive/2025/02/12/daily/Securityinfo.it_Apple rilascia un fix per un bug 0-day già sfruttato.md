---
title: Apple rilascia un fix per un bug 0-day già sfruttato
url: https://www.securityinfo.it/2025/02/11/apple-rilascia-un-fix-per-un-bug-0-day-gia-sfruttato/?utm_source=rss&utm_medium=rss&utm_campaign=apple-rilascia-un-fix-per-un-bug-0-day-gia-sfruttato
source: Securityinfo.it
date: 2025-02-12
fetch_date: 2025-10-06T20:57:15.819786
---

# Apple rilascia un fix per un bug 0-day già sfruttato

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

## Apple rilascia un fix per un bug 0-day già sfruttato

Feb 11, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/02/11/apple-rilascia-un-fix-per-un-bug-0-day-gia-sfruttato/#respond)

---

Ieri Apple ha rilasciato un **fix urgente per un bug 0-day** che, come riportato dalla compagnia stessa, **sarebbe già stato sfruttato** dagli attaccanti. “*Apple è a conoscenza del fatto che questa vulnerabilità potrebbe essere stata sfruttata in un attacco estremamente sofisticato contro specifici individui*” si legge sull’[advisory ufficiale](https://support.apple.com/en-us/122174).

![Apple bug](https://www.securityinfo.it/wp-content/uploads/2025/02/iphone-563067_1920.jpg)

La vulnerabilità, tracciata come CVE-2025-24200, consente a un attaccante di **disabilitare USB Restricted Mode** su un dispositivo per scaricare le informazioni dell’utente.

La funzionalità di sicurezza **impedisce a chiavette USB e altri strumenti di accedere a un iPhone o a un iPad bloccato** **e ottenere i dati salvati** sul dispositivo. La feature disabilita le connessioni dati dopo 60 minuti di inattività del dispositivo, rendendo di fatto la porta per il connettore Lightning un’interfaccia di solo caricamento della batteria e non di comunicazione.

Evidentemente però gli attaccanti sono riusciti a **bypassare questo meccanismo di sicurezza** per scaricare i dati dal dispositivo. A scoprire la vulnerabilità è stato **Bill Marczak**, ricercatore del The Citizen Lab presso la University of Toronto’s Munk School, che ha avvisato gli utenti con un post su X:

> Update your iPhones.. again! iOS 18.3.1 out today with a fix for an ITW USB restricted mode bypass (via Accessibility) <https://t.co/jcrsab7RGu> [pic.twitter.com/ER42QQcsLj](https://t.co/ER42QQcsLj)
>
> — Bill Marczak (@billmarczak) [February 10, 2025](https://twitter.com/billmarczak/status/1889022293432819766?ref_src=twsrc%5Etfw)

La vulnerabilità colpisce l’iPhone XS e i modelli successivi, l’iPad Pro da 13 pollici, iPad Pro da 12.9 pollici di terza generazione e successiva, l’iPad Pro da 11 pollici di prima generazione e successive, l’iPad Air di terza generazione e successive, l’iPad di settima generazione e successive e l’iPad mini di quinta generazione e successive.

**Apple non ha rilasciato dettagli tecnici sul bug**, né informazioni sull’exploit o sulle vittime colpite. Vista la natura della funzionalità, gli attaccanti sono riusciti a ottenere accesso fisico ai dispositivi colpiti.

La compagnia ha invitato tutti gli utenti con device vulnerabili ad **applicare la patch il prima possibile**, disponibile nella versione 18.3.1 di iOS e iPadOs.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Apple](https://www.securityinfo.it/tag/apple/), [bug 0-day](https://www.securityinfo.it/tag/bug-0-day/), [iPad](https://www.securityinfo.it/tag/ipad/), [iPhone](https://www.securityinfo.it/tag/iphone/), [USB Restricted Mode](https://www.securityinfo.it/tag/usb-restricted-mode/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[Arrestati quattro hacker dietro il ransomware Phobos](https://www.securityinfo.it/2025/02/12/arrestati-quattro-hacker-dietro-il-ransomware-phobos/)
[La nuova feature di Brave può diventare molto pericolosa](https://www.securityinfo.it/2025/02/10/la-nuova-feature-di-brave-puo-diventare-molto-pericolosa/)

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
* [![Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/09/08/una-vulnerabilita-cri...