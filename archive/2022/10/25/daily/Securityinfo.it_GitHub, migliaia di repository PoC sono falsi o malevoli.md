---
title: GitHub, migliaia di repository PoC sono falsi o malevoli
url: https://www.securityinfo.it/2022/10/24/github-poc-false-repository/?utm_source=rss&utm_medium=rss&utm_campaign=github-poc-false-repository
source: Securityinfo.it
date: 2022-10-25
fetch_date: 2025-10-03T20:49:11.219735
---

# GitHub, migliaia di repository PoC sono falsi o malevoli

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

## GitHub, migliaia di repository PoC sono falsi o malevoli

Ott 24, 2022  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Malware](https://www.securityinfo.it/category/news/malware-news/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/)
 [0](https://www.securityinfo.it/2022/10/24/github-poc-false-repository/#respond)

---

Un team di ricercatori del Leiden Institute of Advanced Computer Science ha individuato **migliaia di repository GitHub di finte proof-of-concept (PoC) per diverse vulnerabilità conosciute.**

**Molti di questi repository**, oltre a non essere in alcun modo una reale PoC di falle di sicurezza, **contengono anche codice malevolo**. Nel loro report i ricercatori hanno spiegato che **alcuni progetti, se eseguiti, installano malware sul sistema o collezionano dati sensibili**.

**Le PoC false trovate dai ricercatori riguardavano vulnerabilità rese note tra il 2017 e il 2021**. Gli indizi che hanno portato il team ad approfondire la natura dei repository sono stati diversi; in particolare i ricercatori hanno controllato la presenza di IP in blacklist nel codice, di file binari malevoli e di payload offuscati.

![GitHub poc](https://www.securityinfo.it/wp-content/uploads/2022/10/ransomware-g144102148_1280.jpg)

Nel primo caso **il team ha individuato tutti quei repository che nel codice avevano degli indirizzi IP presenti in blacklist pubbliche, catalogati come pericolosi e sospetti**. Alcuni repository, poi, contenevano dei file eseguibili: i ricercatori hanno controllato l’hash di questi file per verificare se anch’esso fosse presente nelle blacklist. Infine **il team ha controllato la presenza di payload offuscati e codificati in base64 o esadecimali**, analizzandone poi la natura.

**Su 47.313 repository GitHub analizzati, 4.893 sono stati classificati come PoC false o codice malevolo**. Purtroppo la tecnica adottata non è in grado di individuarli tutti, ma è comunque un buon punto di partenza per sviluppi futuri.

“**Questo approccio non è in grado di individuare ogni PoC falsa, in quanto esistono altri modi più ingegnosi per offuscare il codice malevolo”** hanno specificato i ricercatori [nel loro paper](https://arxiv.org/pdf/2210.08374.pdf). “**Abbiamo analizzato le similarità del codice come una feature per aiutare a identificare nuovi repository malevoli.** I nostri risultati mostrano infatti che questi repository, in media, sono molto simili tra loro rispetto a quelli sicuri. Si tratta comunque di un primo step per sviluppare tecniche di analisi più precise”.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [blacklist](https://www.securityinfo.it/tag/blacklist/), [codice malevolo](https://www.securityinfo.it/tag/codice-malevolo/), [GitHub](https://www.securityinfo.it/tag/github/), [malware](https://www.securityinfo.it/tag/malware/), [PoC](https://www.securityinfo.it/tag/poc/), [proof-of-concept](https://www.securityinfo.it/tag/proof-of-concept/), [repository](https://www.securityinfo.it/tag/repository/)

[L'agenzia per l'energia atomica dell'Iran è stata hackerata](https://www.securityinfo.it/2022/10/24/agenzia-energia-atomica-iran-hackerata/)
[WithSecure scopre una falla nella crittografia di Office 365](https://www.securityinfo.it/2022/10/22/withsecure-falla-crittografia-office-365/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Nuova variante del malware XCSSET prende di mira gli sviluppatori Xcode su macOS](https://www.securityinfo.it/wp-content/uploads/2025/09/MalwareCrypto-29-set-2025CG-120x85.png)](https://www.securityinfo.it/2025/09/26/nuova-variante-del-malware-xcsset-prende-di-mira-gli-sviluppatori-xcode-su-macos/ "Nuova variante del malware XCSSET prende di mira gli sviluppatori Xcode su macOS")

  [Nuova variante del malware XCSSET...](https://www.securityinfo.it/2025/09/26/nuova-variante-del-malware-xcsset-prende-di-mira-gli-sviluppatori-xcode-su-macos/ "Permanent link to Nuova variante del malware XCSSET prende di mira gli sviluppatori Xcode su macOS")

  Set 26, 2025  [0](https://www.securityinfo.it/2025/09/26/nuova-variante-del-malware-xcsset-prende-di-mira-gli-sviluppatori-xcode-su-macos/#respond)
* [![MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  [MuddyWater si evolve: attacchi più...](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "Permanent link to MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  Set 17, 2025  [0](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/#respond)
* [![GPUGate, una nuova tecnica che sfrutta Google Ads e GitHub per distribuire malware](https://www.securityinfo.it/wp-content/uploads/2025/09/data-theft-9480273_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/09/09/gpugate-una-nuova-tecnica-che-sfrutta-google-ads-e-github-per-distribuire-malware/ "GPUGate, una nuova tecnica che sfrutta Google Ads e GitHub per distribuire malware")

  [GPUGate, una nuova tecnica che sfrutta...](https://www.securityinfo.it/2025/09/09/gpugate-una-nuova-tecnica-che-sfrutta-google-ads-e-github-per-distribuire-malware/ "Permanent link to GPUGate, una nuova tecnica che sfrutta Google Ads e GitHub per di...