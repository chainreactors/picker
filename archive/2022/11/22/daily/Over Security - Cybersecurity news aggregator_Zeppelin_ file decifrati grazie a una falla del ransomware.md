---
title: Zeppelin: file decifrati grazie a una falla del ransomware
url: https://www.securityinfo.it/2022/11/21/zeppelin-falle-ransomware-file-decriptati/?utm_source=rss&utm_medium=rss&utm_campaign=zeppelin-falle-ransomware-file-decriptati
source: Over Security - Cybersecurity news aggregator
date: 2022-11-22
fetch_date: 2025-10-03T23:24:58.343847
---

# Zeppelin: file decifrati grazie a una falla del ransomware

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

## Zeppelin: file decifrati grazie a una falla del ransomware

Nov 21, 2022  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Malware](https://www.securityinfo.it/category/news/malware-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2022/11/21/zeppelin-falle-ransomware-file-decriptati/#respond)

---

Unit221b, un’azienda di cybersicurezza con sede in New Jersey, **ha sfruttato le vulnerabilità presenti nel ransomware Zeppelin per decriptare i file delle vittime senza pagare il riscatto**. Il team di ricercatori ha individuato alcune falle nel meccanismo di cifratura di Zeppelin e le ha usate per aiutare le vittime del malware a recuperare i dati criptati.

Zeppelin, conosciuto anche come “Buran”, **è un ransomware legato a un gruppo di hacker russi emerso a fine 2019**. Si tratta di un malware scritto in Delphi *Vega* e opera come un ransomware as a service, quindi utilizzabile da chiunque. **Il team dietro il malware ha preso di mira organizzazioni no-profit, di beneficenza e rifugi per senzatetto**, oltre che infrastrutture critiche dei settori della difesa, dell’istruzione e della sanità.

![Ransomware Zeppelin](https://www.securityinfo.it/wp-content/uploads/2022/11/ransomware-ge405f2549_1280.jpg)

I ricercatori di Unit221b, analizzando il ransomware, hanno scoperto che **utilizzava un chiave effimera RSA-512 per criptare la AES che criptava i file.** La chiave di cifratura AES era memorizzata nel footer di ogni file criptato perciò, entrando in possesso della RSA-512, si sarebbe potuto decifrare i file.

Il team dell’azienda è riuscito a crackare la chiave effimera e di conseguenza ottenere la chiave AES per decriptare i file. L’intera operazione è rimasta segreta per due anni, durante i quali gli esperti di Unit221b hanno aiutato le organizzazioni colpite a recuperare i dati.

![Ransomware Zeppelin](https://www.securityinfo.it/wp-content/uploads/2022/11/pexels-soumil-kumar-735911.jpg)

**Unit221b ha deciso di rendere disponibile il tool di decifratura** ora che gli attacchi di Zeppelin si sono ridotti drasticamente. I dettagli dello strumento sono pubblici, e chiunque sia stato colpito dal [ransomware](https://www.securityinfo.it/2022/11/16/il-ransomware-colpisce-nel-fine-settimana/) può richiedere l’accesso al tool. Secondo quanto dichiarato da Unit221b, **il tool funziona anche con le versioni più recenti di Zeppelin.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [cybersecurity](https://www.securityinfo.it/tag/cybersecurity/), [cybersicurezza](https://www.securityinfo.it/tag/cybersicurezza/), [falla](https://www.securityinfo.it/tag/falla/), [malware](https://www.securityinfo.it/tag/malware/), [Ransomware](https://www.securityinfo.it/tag/ransomware/), [Unit221b](https://www.securityinfo.it/tag/unit221b/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/), [zeppelin](https://www.securityinfo.it/tag/zeppelin/)

[SentinelOne: Singularity Xdr per la protezione completa delle aziende](https://www.securityinfo.it/2022/11/22/sentinelone-la-piattaforma-singularity-per-la-protezione-completa-delle-aziende/)
[Nuove alleanze e un nuovo servizio SaaS per Cohesity](https://www.securityinfo.it/2022/11/21/nuove-alleanze-e-un-nuovo-servizio-saas-per-cohesity/)

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
* [![MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  [MuddyWater si evolve: attacchi più...](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "Permanent link to MuddyWater si evolve: ...