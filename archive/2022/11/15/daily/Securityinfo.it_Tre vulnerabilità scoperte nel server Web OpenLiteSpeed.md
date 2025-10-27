---
title: Tre vulnerabilità scoperte nel server Web OpenLiteSpeed
url: https://www.securityinfo.it/2022/11/14/tre-vulnerabilita-scoperte-nel-server-web-openlitespeed/?utm_source=rss&utm_medium=rss&utm_campaign=tre-vulnerabilita-scoperte-nel-server-web-openlitespeed
source: Securityinfo.it
date: 2022-11-15
fetch_date: 2025-10-03T22:49:07.969447
---

# Tre vulnerabilità scoperte nel server Web OpenLiteSpeed

Aggiornamenti recenti Ottobre 3rd, 2025 4:00 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)
* [Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)
* [Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/)
* [Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/)
* [CERT-AGID 20–26 settembre: phishing, malware e PEC compromesse](https://www.securityinfo.it/2025/09/29/cert-agid-20-26-settembre-phishing-malware-e-pec-compromesse/)

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

## Tre vulnerabilità scoperte nel server Web OpenLiteSpeed

Nov 14, 2022  [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/ "Articoli scritti da Dario Orlandi")
 [News](https://www.securityinfo.it/category/news/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2022/11/14/tre-vulnerabilita-scoperte-nel-server-web-openlitespeed/#respond)

---

I ricercatori della [Unit 42](https://www.paloaltonetworks.com/unit42) di Palo Alto Networks hanno annunciato l’individuazione di **tre diverse vulnerabilità** nel server Web open source [OpenLiteSpeed](https://github.com/litespeedtech/openlitespeed); LiteSpeed è un server web ottimizzato per garantire prestazioni elevate; secondo le analisi di Palo Alto Networks, le istanze del server online sono quasi due milioni, pari al 2% di tutti i Web server installati.

Sfruttando e combinando queste vulnerabilità, che sono presenti sia nella versione open source del server sia in quelle aziendali, un attaccante potrebbe ottenere un **accesso completo** al server, con i diritti di esecuzione illimitati.

## Tre falle pericolose

Il punto di partenza del test di penetrazione svolto dai ricercatori è stato un semplice **accesso alla dashboard** di amministrazione; partendo da questa premessa, i ricercatori hanno scoperto che l’interfaccia era vulnerabile a una tecnica di [command injection](https://www.cve.org/CVERecord?id=CVE-2022-0073), sfruttabile poi per effettuare una [privilege escalation](https://www.cve.org/CVERecord?id=CVE-2022-0074) per eseguire codice con diritti di root.

![](https://www.securityinfo.it/wp-content/uploads/2022/11/word-image-17.png)

Fonte: Unit 42 Palo Alto Networks.

Sempre nel corso dello stesso audit, i ricercatori hanno individuato anche un’ulteriore vulnerabilità che potrebbe consentire la navigazione tra le directory ([directory traversal](https://www.cve.org/CVERecord?id=CVE-2022-0072)) per raggiungere file teoricamente inaccessibili che si trovano nella **cartella radice del sito web**.

Tutte le vulnerabilità sono state comunicate agli sviluppatori che hanno prontamente **provveduto a risolverle**, con le patch 1.7.16.1 per OpenLiteSpeed e 6.0.12 per LiteSpeed. Inoltre, gli sviluppatori hanno anche modificato il repository di Docker.

Per mettere al sicuro un’installazione LiteSpeed non bisogna quindi far altro che **aggiornare il software** all’ultima versione disponibile.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [command injection](https://www.securityinfo.it/tag/command-injection/), [LiteSpeed](https://www.securityinfo.it/tag/litespeed/), [OpenLiteSpeed](https://www.securityinfo.it/tag/openlitespeed/), [Palo Alto Networks](https://www.securityinfo.it/tag/palo-alto-networks/), [Privilege escalation](https://www.securityinfo.it/tag/privilege-escalation/), [Unit 42](https://www.securityinfo.it/tag/unit-42/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[Google Pixel 5 e 6 si sbloccano senza password](https://www.securityinfo.it/2022/11/15/google-pixel-5-e-6-si-sbloccano-senza-password/)
[Vulnerabilità Windows scoperta in seguito ad attacchi russi](https://www.securityinfo.it/2022/11/11/vulnerabilita-windows-cyberspionaggio-russo/)

---

![](https://secure.gravatar.com/avatar/9ba6108fae91c2be66a7ef45ac2db49a?s=90&d=mm&r=g)

##### [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/)

##### Articoli correlati

* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_d4x8rid4x8rid4x8-120x85.png)](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  [Firewall Cisco sotto attacco: una nuova...](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Permanent link to Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  Set 29, 2025  [0](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/#respond)
* [![Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.](https://www.securityinfo.it/wp-content/uploads/2025/09/ai-generated-9053184_1920-120x85.jpg)](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/ "Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.")

  [Attaccanti sfruttano un bug di...](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/ "Permanent link to Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.")

  Set 24, 2025  [0](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/#respond)
* [![Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/09/08/una-vulnerabilita-critica-di-sap-s-4hana-e-stata-sfruttata-dai-cybecriminali/ "Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali")

  [Una vulnerabilità critica di SAP...](https://www.securityinfo.it/2025/09/08/una-vulnerabilita-critica-di-sap-s-4hana-e-stata-sfruttata-dai-cybecriminali/ "Permanent link to Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali")

  Set 08, 2025  [0](https://www.securityinfo.it/2025/09/08/una-vulnerabilita-critica-di-sap-s-4hana-e-stata-sfruttata-dai-cybecriminali/#respond)
*...