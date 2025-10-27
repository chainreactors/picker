---
title: Google Pixel 5 e 6 si sbloccano senza password
url: https://www.securityinfo.it/2022/11/15/google-pixel-5-e-6-si-sbloccano-senza-password/?utm_source=rss&utm_medium=rss&utm_campaign=google-pixel-5-e-6-si-sbloccano-senza-password
source: Over Security - Cybersecurity news aggregator
date: 2022-11-16
fetch_date: 2025-10-03T22:53:54.892451
---

# Google Pixel 5 e 6 si sbloccano senza password

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

## Google Pixel 5 e 6 si sbloccano senza password

Nov 15, 2022  [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/ "Articoli scritti da Dario Orlandi")
 [News](https://www.securityinfo.it/category/news/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2022/11/15/google-pixel-5-e-6-si-sbloccano-senza-password/#respond)

---

L’esperto di sicurezza David Schütz ha scoperto, [sembra accidentalmente](https://bugs.xdavidhu.me/google/2022/11/10/accidental-70k-google-pixel-lock-screen-bypass/), una procedura per **evitare la schermata di blocco** degli smartphone Android Pixel 5 e 6 di Google.

A quanto pare, il bug era esteso a tutta la famiglia Pixel ed è rimasto utilizzabile almeno per sei mesi (la segnalazione di Schütz a Google risale allo scorso giugno), è stato risolto con l’**aggiornamento di sicurezza dello scorso 5 novembre**.

L’impatto della vulnerabilità è **molto ampio**: secondo la descrizione che si trova nel database CVE ([CVE-2022-20465](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-20465)), il problema è esteso alle versioni 10, 11, 12, 12L e 13 di Android.

Il requisito dell’**accesso fisico** al device ha certamente limitato la portata del problema, ma sono molti i casi in cui un bug di questa portata potrebbe comunque essere sfruttato, dalle indagini delle forze dell’ordine alla violazione dei dispositivi rubati.

## Una scoperta casuale

Schütz si è imbattuto nel problema quando il suo device è **rimasto senza batteria** e poi ha dimenticato il Pin della scheda Sim, inserendo un codice sbagliato per tre volte; per sbloccare la scheda ha quindi dovuto digitare anche il Puk.

A questo punto il device **non ha richiesto la password**, ma soltanto una lettura dell’impronta digitale.

Continuando a sperimentare, Schütz è arrivato a individuare una procedura che **non richiede neppure il riavvio** del dispositivo, e quindi consente di aggirare il lock screen a patto che il device sia stato sbloccato almeno una volta dopo il boot.

È sufficiente disporre di **una seconda scheda Sim** di cui si conoscono tutte le informazioni da sostituire al momento opportuno. Il ricercatore ha pubblicato anche [un interessante video](https://www.youtube.com/watch?v=dSgSnYPgzT0) che documenta tutta la procedura.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Android](https://www.securityinfo.it/tag/android/), [bug](https://www.securityinfo.it/tag/bug/), [Google](https://www.securityinfo.it/tag/google/), [Pixel](https://www.securityinfo.it/tag/pixel/), [Pixel 5](https://www.securityinfo.it/tag/pixel-5/), [Pixel 6](https://www.securityinfo.it/tag/pixel-6/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[Il ransomware colpisce nel fine settimana](https://www.securityinfo.it/2022/11/16/il-ransomware-colpisce-nel-fine-settimana/)
[Tre vulnerabilità scoperte nel server Web OpenLiteSpeed](https://www.securityinfo.it/2022/11/14/tre-vulnerabilita-scoperte-nel-server-web-openlitespeed/)

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
* [![Google e la privacy: sanzione multimilionaria per informazioni fuorvianti](https://www.securityinfo.it/wp-content/uploads/2025/09/security-4868167_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/09/10/google-e-la-privacy-sanzione-multimilionaria-per-informazioni-fuorvianti/ "Google e la privacy: sanzione multimilionaria per informazioni fuorvianti")

  [Google e la privacy: sanzione...](https://www.securityinfo.it/2025/09/10/google-e-la-privacy-sanzione-multimilionaria-per-informazioni-fuorvianti/ "Permanent link to Google e la privacy: sanzione multimilionaria per informazioni fuorvianti")

  Set 10, 2025  [0](https://www.securityinfo.it/2025/09/10/google-e-la-privacy-sanzione-multimilionaria-per-informazioni-fuorvianti/#respond)
* [![Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/09/08/una-vulnerabilita-critica-di-sap-s-4h...