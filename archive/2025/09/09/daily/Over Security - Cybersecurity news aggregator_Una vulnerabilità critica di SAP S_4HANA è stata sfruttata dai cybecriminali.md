---
title: Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali
url: https://www.securityinfo.it/2025/09/08/una-vulnerabilita-critica-di-sap-s-4hana-e-stata-sfruttata-dai-cybecriminali/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-09
fetch_date: 2025-10-02T19:52:12.794445
---

# Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali

Aggiornamenti recenti Ottobre 1st, 2025 2:22 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Il 60% dei firewall non supera i controlli di conformità: la ricerca di FireMon](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)
* [Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/)
* [Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/)
* [CERT-AGID 20–26 settembre: phishing, malware e PEC compromesse](https://www.securityinfo.it/2025/09/29/cert-agid-20-26-settembre-phishing-malware-e-pec-compromesse/)
* [Nuova variante del malware XCSSET prende di mira gli sviluppatori Xcode su macOS](https://www.securityinfo.it/2025/09/26/nuova-variante-del-malware-xcsset-prende-di-mira-gli-sviluppatori-xcode-su-macos/)

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

## Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali

Set 08, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/09/08/una-vulnerabilita-critica-di-sap-s-4hana-e-stata-sfruttata-dai-cybecriminali/#respond)

---

I ricercatori di Security Bridge [hanno scoperto](https://securitybridge.com/blog/critical-sap-s-4hana-code-injection-vulnerability-cve-2025-42957/) che una **vulnerabilità critica di SAP S/4HANA è stata sfruttata dagli attaccanti.** Il bug, identificato come CVE-2025-42957, era stato reso noto e risolto da SAP nel Security Patch Day di agosto.

La vulnerabilità, con punteggio di criticità di 9.9, è un **bug di code injection** che consente anche a un utente con privilegi ridotti di prendere il controllo dell’intero sistema e di tutti i dati presenti.

Un cybercriminale sarebbe quindi in grado di cancellare e inserire dati direttamente nel database SAP, creare nuovi utenti con privilegi SAP\_ALL, ottenere gli hash delle password e modificare i processi di business, iniettando codice a ogni livello applicativo. **La vulnerabilità colpisce tutte le release di SAP S/4HANA**, sia su cloud che on-premise.

![vulnerabilità SAP](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-1.jpg)

I ricercatori di Security Bridge hanno pubblicato il loro exploit e hanno comunicato che **c’è stato almeno un caso in cui un attaccante ha sfruttato il bug.**Al momento non è stato segnalato un uso diffuso della vulnerabilità.

Inoltre, non solo i cybercriminali sono già in grado di sfruttare la vulnerabilità, ma “*effettuare il reverse engineering della patch per creare un exploit è relativamente facile per SAP ABAP, visto che il codice di ABAP è visibile a tutti*” hanno spiegato i ricercatori.

Oltre a poter modificare i dati e i processi di business ed entrare in possesso di informazioni sensibili, prendendo il controllo completo del sistema i cybercriminali sono anche in grado di **distribuire ransomware e malware**, con impatti gravissimi sull’operatività aziendale.

Il bug era stato scoperto proprio dal team di Security Bridge lo scorso giugno. La compagnia aveva contattato immediatamente SAP per condividere le informazioni sulla vulnerabilità e analizzarla. Il fix è stato rilasciato l’11 agosto, circa sei settimane dopo la scoperta.

L’indicazione è ovviamente quella di **applicare la patch risolutiva pubblicata da SAP il prima possibile.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [code injection](https://www.securityinfo.it/tag/code-injection/), [privilege elevation](https://www.securityinfo.it/tag/privilege-elevation/), [ransomare](https://www.securityinfo.it/tag/ransomare/), [SAP](https://www.securityinfo.it/tag/sap/), [SAP S/4HANA](https://www.securityinfo.it/tag/sap-s-4hana/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[GPUGate, una nuova tecnica che sfrutta Google Ads e GitHub per distribuire malware](https://www.securityinfo.it/2025/09/09/gpugate-una-nuova-tecnica-che-sfrutta-google-ads-e-github-per-distribuire-malware/)
[CERT-AGID 30 agosto-5 settembre: campagne contro INPS e Agenzia delle Entrate](https://www.securityinfo.it/2025/09/08/cert-agid-30-agosto-5-settembre-campagne-contro-inps-e-agenzia-delle-entrate/)

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
* [![Hexstrike AI, nuovo tool di OffSec, è già stato preso di mira dal cybercrimine](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_amcol3amcol3amco-120x85.png)](https://www.securityinfo.it/2025/09/03/hexstrike-ai-nuovo-tool-di-offsec-e-gia-stato-preso-di-mira-dal-cybercrimine/ "Hexstrike AI, nuovo tool di OffSec, è già stato pre...