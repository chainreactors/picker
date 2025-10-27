---
title: La campagna APT CommonMagic sta facendo nuove vittime
url: https://www.securityinfo.it/2023/06/08/la-campagna-apt-commonmagic-sta-colpendo-nuove-vittime/
source: Over Security - Cybersecurity news aggregator
date: 2023-06-09
fetch_date: 2025-10-04T11:49:30.534384
---

# La campagna APT CommonMagic sta facendo nuove vittime

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

## La campagna APT CommonMagic sta facendo nuove vittime

Giu 08, 2023  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Apt](https://www.securityinfo.it/category/minacce-2/apt/), [Attacchi](https://www.securityinfo.it/category/approfondimenti/attacchi/), [Attacchi](https://www.securityinfo.it/category/news/attachi/), [Campagne malware](https://www.securityinfo.it/category/approfondimenti/campagne-malware/), [Malware](https://www.securityinfo.it/category/news/malware-news/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [Minacce](https://www.securityinfo.it/category/minacce-2/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2023/06/08/la-campagna-apt-commonmagic-sta-colpendo-nuove-vittime/#respond)

---

**La campagna APT CommonMagic**, individuata da Kaspersky lo scorso marzo, **ha ampliato il suo raggio d’azione**. Attiva dal 2021, la campagna utilizza impianti PowerMagic e CommonMagic per attività di spionaggio e sfrutta un malware non ancora identificato per sottrarre dati alle proprie vittime, situate nelle regioni di Donetsk, Luhansk e Crimea.

Mentre analizzavano impianti simili a CommonMagic per individuare il gruppo dietro la campagna, **i ricercatori di Kaspersky hanno scoperto nuove attività che utilizzano il framework [CloudWizard](https://securelist.com/cloudwizard-apt/109722/)**, in grado di ottenere screenshot dai dispositivi, usare il microfono per registrare ed effettuare operazioni di keylogging.

CloudWizard è composto da 9 moduli e uno di essi è anche in grado di esfiltrare cookie di Gmail dal browser per poi accedere ai registri delle attività, l’elenco dei contatti e i messaggi e-mail degli account colpiti. **Le aree delle vittim**e, inoltre, **non si limitano più a quelle di CommonMagic, ma anche all’Ucraina centrale e dell’ovest.** Gli obiettivi includono ora anche singoli utenti, in particolare diplomatici, oltre alle organizzazioni.

![](https://www.securityinfo.it/wp-content/uploads/2023/06/kaspersky.png)

Credits: Kaspersky

I ricercatori hanno trovato **numerose analogie con CommonMagic**: alcune sezioni del codice sono identiche, usano la stessa libreria di crittografia, seguono un formato di denominazione dei file simile e condividono l’ubicazione delle vittime.

**Cloud Wizard presenta molte similarità anche con Operation Groundbait e Operation BugDrop**, relative al codice, ai modelli di denominazione dei file e all’hosting da parte di servizi ucraini; per tutti questi motivi, **il team di Kaspersky ritiene che l’attore dietro le varie campagne sia lo stesso e si sia ampliato per colpire nuovi obiettivi.**

“**Il responsabile di queste operazioni ha dimostrato** **un impegno costante nel cyberspionaggio, migliorando continuamente il proprio set di strumenti e prendendo di mira organizzazioni di interesse** per oltre quindici anni. I fattori geopolitici continuano a essere una motivazione significativa per gli attacchi APT e, data la tensione prevalente nell’area del conflitto russo-ucraino, prevediamo che questo attore continuerà a svolgere le sue attività anche in futuro” ha commentato **Georgy Kucherin, Security Researcher di Kaspersky’s Global Research and Analysis Team.**

Al momento non ci sono informazioni sull’identità dell’attore dietro le campagne. Kaspersky consiglia alle organizzazioni di **fornire al proprio team SOC gli strumenti per accedere alle informazioni sulle minacce e aggiornarlo sugli ultimi attacchi**. È importante inoltre **implementare soluzioni EDR** per il monitoraggio e l’analisi degli incidenti a livello di endpoint e **sensibilizzare i dipendenti alle pratiche di sicurezza** per sfuggire agli attacchi di phishing e social engineering.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [APT](https://www.securityinfo.it/tag/apt/), [cloudwizard](https://www.securityinfo.it/tag/cloudwizard/), [CommonMagic](https://www.securityinfo.it/tag/commonmagic/), [conflitto russo-ucraino](https://www.securityinfo.it/tag/conflitto-russo-ucraino/), [Kaspersky](https://www.securityinfo.it/tag/kaspersky/), [operation bugdrop](https://www.securityinfo.it/tag/operation-bugdrop/), [operation groundbait](https://www.securityinfo.it/tag/operation-groundbait/), [Phishing](https://www.securityinfo.it/tag/phishing/)

[Fortinet rilascia un fix per una nuova vulnerabilità dei dispositivi Fortigate](https://www.securityinfo.it/2023/06/12/fortinet-rilascia-un-fix-per-una-nuova-vulnerabilita-dei-dispositivi-fortigate/)
[Quattro tool di IA generativa per migliorare la sicurezza](https://www.securityinfo.it/2023/06/07/quattro-tool-di-ia-generativa-per-migliorare-la-sicurezza/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  [MuddyWater si evolve: attacchi più...](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "Permanent link to MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  Set 17, 2025  [0](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/#respond)
* [![Report Acronis: il ransomware...