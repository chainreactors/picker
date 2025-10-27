---
title: Google ha rilasciato regole Yara per individuare Cobalt Strike
url: https://www.securityinfo.it/2022/11/25/google-ha-rilasciato-regole-yara-per-individuare-cobalt-strike/?utm_source=rss&utm_medium=rss&utm_campaign=google-ha-rilasciato-regole-yara-per-individuare-cobalt-strike
source: Over Security - Cybersecurity news aggregator
date: 2022-11-26
fetch_date: 2025-10-03T23:50:49.412760
---

# Google ha rilasciato regole Yara per individuare Cobalt Strike

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

## Google ha rilasciato regole Yara per individuare Cobalt Strike

Nov 25, 2022  [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/ "Articoli scritti da Dario Orlandi")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [Intrusione](https://www.securityinfo.it/category/news/intrusione/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/)
 [0](https://www.securityinfo.it/2022/11/25/google-ha-rilasciato-regole-yara-per-individuare-cobalt-strike/#respond)

---

Attraverso il suo Cloud Threat Intelligence team, ha portato un contributo significativo alla **protezione contro gli attacchi basati su Cobalt Strike**.

I ricercatori hanno infatti distribuito con la formula open source un [set di 165 regole Yara](https://cloud.google.com/blog/products/identity-security/making-cobalt-strike-harder-for-threat-actors-to-abuse) e la relativa collezione VirusTotal per **individuare i componenti e le versioni** di Cobalt Strike eventualmente presenti e attivi nella rete.

Greg Sinclair, Security Engineer del team Google Cloud Threat Intelligence, ha dichiarato: “Abbiamo deciso che **rilevare la versione esatta** di Cobalt Strike era un elemento importante per determinare la legittimità del suo uso da parte di attori non malintenzionati”.

![](https://www.securityinfo.it/wp-content/uploads/2022/11/GC-Op27_graph.max-2200x2200-1.png)

Il modello dell’infrastruttura di Cobalt Strike (Fonte: Google)

## L’importanza della versione

Le nuove regole, infatti, rendono molto più semplice l’individuazione di eventuali attività pericolose: riconoscere le versioni non aggiornate di Cobalt Strike (spesso ottenute per canali non ufficiali) è molto utile per **distinguere tra le operazioni legittime e gli attacchi**.

Come ha sottolineato Google, nella maggior parte dei casi le versioni non ufficiali di Cobalt Strike **rimangono indietro di almeno una release** rispetto a quelle legittime, e questo ha consentito di raccogliere moltissime informazioni utili alla costruzione di regole di rilevamento estremamente accurate.

Sinclair ha aggiunto: “Il nostro obiettivo era quello di effettuare rilevamenti molto precisi per consentire di individuare la versione esatta di particolari componenti Cobalt Strike. Quando possibile, abbiamo creato firme per rilevare **versioni specifiche di ciascun componente**”.

Google ha anche reso disponibile anche un set di firme di **rilevamento per Sliver**, un framework di emulazione legittimo e open source progettato per i test di sicurezza, che è stato utilizzato anche da attori malintenzionati come alternativa a Cobalt Strike.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Cobalt Strike](https://www.securityinfo.it/tag/cobalt-strike/), [Google](https://www.securityinfo.it/tag/google/), [Google Cloud Threat Intelligence](https://www.securityinfo.it/tag/google-cloud-threat-intelligence/), [VirusTotal](https://www.securityinfo.it/tag/virustotal/), [Yara](https://www.securityinfo.it/tag/yara/)

[Acronis: le novità a Cyberfit e le previsioni per il 2023](https://www.securityinfo.it/2022/11/26/acronis-novita-cyberfit-previsioni/)
[Firewall Sophos sfrutta Xstream per l'Edge Computing](https://www.securityinfo.it/2022/11/24/firewall-sophos-xstream-edge-computing/)

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
* [![Android, più sicurezza con la verifica dell’identità sviluppatori](https://www.securityinfo.it/wp-content/uploads/2025/08/Gemini_Generated_Image_qj2bi3qj2bi3qj2b-120x85.png)](https://www.securityinfo.it/2025/08/27/android-piu-sicurezza-con-la-verifica-dellidentita-sviluppatori/ "Android, più sicurezza con la verifica dell’identità sviluppatori")

  [Android, più sicurezza con la verifica...](https://www.securityinfo.it/2025/08/27/android-piu-sicurezza-con-la-verifica-dellidentita-sviluppatori/ "Permanent link to Android, più sicurezza con la verifica dell’identità sviluppatori")

  Ago 27, 2025  [0](https://www.securityinfo.it/2025/08/27/android-piu-sicurezza-con-la-verifica-dellidentita-sviluppatori/#respond)
* [![Anche Google vittima della campagna di ShinyHunters](https://www.securityinfo.it/wp-content/uploads/2025/08/Google-Crepato-7-ago-2025CG-120x85.p...