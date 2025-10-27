---
title: Google scopre 18 vulnerabilità nei chipset mobile Samsung Exynos
url: https://www.securityinfo.it/2023/03/22/google-scopre-18-vulnerabilita-nei-chipset-mobile-samsung-exynos/?utm_source=rss&utm_medium=rss&utm_campaign=google-scopre-18-vulnerabilita-nei-chipset-mobile-samsung-exynos
source: Securityinfo.it
date: 2023-03-23
fetch_date: 2025-10-04T10:25:10.060120
---

# Google scopre 18 vulnerabilità nei chipset mobile Samsung Exynos

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

## Google scopre 18 vulnerabilità nei chipset mobile Samsung Exynos

Mar 22, 2023  [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/ "Articoli scritti da Dario Orlandi")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2023/03/22/google-scopre-18-vulnerabilita-nei-chipset-mobile-samsung-exynos/#respond)

---

I ricercatori di sicurezza di Google hanno [individuato e segnalato](https://googleprojectzero.blogspot.com/2023/03/multiple-internet-to-baseband-remote-rce.html) diverse **vulnerabilità zero-day nei chipset Samsung destinati agli smartphone Android**, che potrebbero consentire a un utente malintenzionato di controllare a distanza il dispositivo a partire dal solo numero di telefono.

Il team di bug hunting di Google, Project Zero, ha trovato e segnalato tra la fine del 2022 e l’inizio del 2023 ben **18 bug nel firmware del modem integrato nei processori Exynos** di Samsung.

Quattro di questi bug sono particolarmente gravi perché possono consentire l’esecuzione di codice remoto da Internet alla baseband, permettendo ad un intruso di **prendere il pieno controllo del telefono o del dispositivo**.

![](https://www.securityinfo.it/wp-content/uploads/2023/03/anh-nhat-Aon3Ov8toHM-unsplash-scaled.jpg)

## Basta conoscere il numero di telefono

I dettagli esatti delle vulnerabilità non sono stati resi noti per tutelare gli utenti; ma nel post che ha reso pubbliche le vulnerabilità, Tim Willis di Google Project Zero ha dichiarato: “I test condotti da Project Zero confermano che queste quattro vulnerabilità consentono a un utente malintenzionato di compromettere da remoto un telefono a livello di banda base **senza alcuna interazione da parte dell’utente** e richiedono solo che l’attaccante conosca il numero di telefono della vittima”.

“Con attività aggiuntive limitate di ricerca e sviluppo, riteniamo che gli aggressori esperti sarebbero in grado di **creare rapidamente un exploit operativo** per compromettere i dispositivi interessati in modo silenzioso e remoto”, ha aggiunto Willis.

![](https://www.securityinfo.it/wp-content/uploads/2023/03/1517663039037-transformed.jpeg)

Tim Willis, Head of Google Project Zero

**Gli altri problemi non sono così gravi** e richiedono la collaborazione di un operatore di rete mobile o un utente malintenzionato con accesso locale al dispositivo.

Secondo Google, **i dispositivi che utilizzano modem Exynos potenzialmente vulnerabili sono parecchi**: Samsung S22, M33, M13,  M12, A71, A53, A33, A21s, A13, A12 e A04, Vivo S16, S15, S6, X70, X60 e X30, le serie Pixel 6 e Pixel 7 di Google e i veicoli che utilizzano il chipset Exynos Auto T5123.

Google ha rilasciato **una patch per CVE-2023-24033 per i dispositivi Pixel** nel suo [aggiornamento di sicurezza di marzo](https://source.android.com/docs/security/bulletin/pixel/2023-03-01); per i dispositivi di altri produttori, però, è necessario attendere la distribuzione di update dedicati.

Fino a quando ogni produttore non avrà distribuito un aggiornamento, i ricercatori di Google suggeriscono di **disattivare le chiamate Wi-Fi e Voice-over-LTE (VoLTE)** per proteggersi dall’esecuzione di codice remoto nella baseband.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Exynos](https://www.securityinfo.it/tag/exynos/), [Google](https://www.securityinfo.it/tag/google/), [Google Project Zero](https://www.securityinfo.it/tag/google-project-zero/), [Pixel 6](https://www.securityinfo.it/tag/pixel-6/), [Pixel 7](https://www.securityinfo.it/tag/pixel-7/), [S21](https://www.securityinfo.it/tag/s21/), [Samsung](https://www.securityinfo.it/tag/samsung/)

[Kaspersky svela un Apt attivo nell'area del conflitto russo-ucraino](https://www.securityinfo.it/2023/03/22/kaspersky-svela-un-apt-attivo-nellarea-del-conflitto-russo-ucraino/)
[Kaspersky aggiorna il decryptor per il ransomware Conti](https://www.securityinfo.it/2023/03/22/kaspersky-decryptor-ransomware-conti/)

---

![](https://secure.gravatar.com/avatar/9ba6108fae91c2be66a7ef45ac2db49a?s=90&d=mm&r=g)

##### [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/)

##### Articoli correlati

* [![Google e la privacy: sanzione multimilionaria per informazioni fuorvianti](https://www.securityinfo.it/wp-content/uploads/2025/09/security-4868167_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/09/10/google-e-la-privacy-sanzione-multimilionaria-per-informazioni-fuorvianti/ "Google e la privacy: sanzione multimilionaria per informazioni fuorvianti")

  [Google e la privacy: sanzione...](https://www.securityinfo.it/2025/09/10/google-e-la-privacy-sanzione-multimilionaria-per-informazioni-fuorvianti/ "Permanent link to Google e la privacy: sanzione multimilionaria per informazioni fuorvianti")

  Set 10, 2025  [0](https://www.securityinfo.it/2025/09/10/google-e-la-privacy-sanzione-multimilionaria-per-informazioni-fuorvianti/#respond)
* [![Il data breach contro Salesloft impatta centinaia di servizi](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_evjthoevjthoevjt-120x85.png)](https://www.securityinfo.it/2025/09/02/il-data-breach-contro-salesloft-impatta-centinaia-di-servizi/ "Il data breach contro Salesloft impatta centinaia di servizi")

  [Il data breach contro Salesloft impatta...](https://www.securityinfo.it/2025/09/02/il-data-breach-contro-salesloft-impatta-centinaia-di-servizi/ "Permanent link to Il data breach contro Salesloft impatta centinaia di servizi")

  Set 02, 2025  [0](https://www.securityinfo.it/2025/09/02/il-data-breach-contro-salesloft-impatta-centinaia-di-servizi/#respond)
* [![Android, più sicurezza con la verifica dell’ide...