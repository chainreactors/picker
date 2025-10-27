---
title: FASTCash: una nuova variante colpisce i sistemi Linux per prelevare denaro dagli sportelli
url: https://www.securityinfo.it/2024/10/16/fastcash-una-nuova-variante-colpisce-i-sistemi-linux-per-prelevare-denaro-dagli-sportelli/?utm_source=rss&utm_medium=rss&utm_campaign=fastcash-una-nuova-variante-colpisce-i-sistemi-linux-per-prelevare-denaro-dagli-sportelli
source: Securityinfo.it
date: 2024-10-17
fetch_date: 2025-10-06T18:55:47.690589
---

# FASTCash: una nuova variante colpisce i sistemi Linux per prelevare denaro dagli sportelli

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

## FASTCash: una nuova variante colpisce i sistemi Linux per prelevare denaro dagli sportelli

Ott 16, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Malware](https://www.securityinfo.it/category/news/malware-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2024/10/16/fastcash-una-nuova-variante-colpisce-i-sistemi-linux-per-prelevare-denaro-dagli-sportelli/#respond)

---

**FASTCash**, un malware attribuito a gruppi nord-coreani, è tornato a colpire con una nuova **variante specifica per i sistemi Linux**. Il malware viene installato negli switch di pagamento all’interno di reti compromesse per consentire agli attaccanti di **prelevare denaro contante senza autorizzazione dagli sportelli bancomat.**

Questo malware è stato individuato per la prima volta nel 2019 e colpiva esclusivamente i sistemi IBM AIX e Windows; la variante Linux è stata scoperta dal ricercatore di sicurezza [haxrob](https://doubleagent.net/fastcash-for-linux) a giugno 2023 ma è stata resa nota al pubblico solo ora. Secondo il ricercatori, sia la variante Linux che Windows colpiscono la stessa infrastruttura di pagamento o comunque infrastrutture simili nello stesso Paese.

![FASTCash](https://www.securityinfo.it/wp-content/uploads/2024/10/atm-7408590_1920.jpg)

“*La variante Linux ha funzionalità leggermente ridotte rispetto al suo predecessore Windows, anche se mantiene comunque una funzionalità chiave: intercettare i messaggi di transazioni rifiutate (a strisciata magnetica) per un elenco predefinito di numeri di conto dei titolari di carte e quindi **autorizzare la transazione con un importo casuale di fondi nella valuta della Lira turca***” ha spiegato il ricercato.

FASTCash è implementato in forma di una libreria condivisa che viene iniettata in un processo in esecuzione sullo switch Linux di pagamento, cioè l’intermediario tra lo sportello e il sistema centrale della banca. L’obiettivo è **intercettare i pacchetti originati dalle transazioni**, in particolare quelli che comunicano il rifiuto del pagamento a causa di fondi insufficienti, e **sostituirli con un messaggio di approvazione.**

A questo punto, dopo aver inserito nel messaggio di approvazione anche la somma di denaro da prelevare (generalmente tra le 12.000 e le 30.000 Lire turche), gli attaccanti prelevano il denaro con successo dallo sportello.

Haxrob ha sottolineato che, al momento della scoperta della variante, non c’erano avvisi del malware su VirusTotal. **“*La scoperta della variante Linux sottolinea ulteriormente la necessità di adeguate capacità di rilevamento che spesso mancano negli ambienti server Linux*“.**

La CISA ha fornito contestualmente delle **indicazioni per prevenire questi attacchi**, le quali comprendono l’implementazione di requisiti di chip e PIN per le carte di debito, la verifica dei codici di autenticazione dei possessori di carte e l’uso del crittogramma per validare la risposta di autorizzazione dell’operazione.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Corea del Nord](https://www.securityinfo.it/tag/corea-del-nord/), [FASTCash](https://www.securityinfo.it/tag/fastcash/), [Linux](https://www.securityinfo.it/tag/linux/), [malware](https://www.securityinfo.it/tag/malware/), [sportelli bancomat](https://www.securityinfo.it/tag/sportelli-bancomat/), [transazioni bancarie](https://www.securityinfo.it/tag/transazioni-bancarie/)

[Motti Ben Shoshan: “F5, innovazione e sicurezza per il futuro del cloud"](https://www.securityinfo.it/2024/10/16/motti-ben-shoshan-f5-intervista-cybertech/)
[Rilasciato il fix per una vulnerabilità critica di Jetpack per WordPress](https://www.securityinfo.it/2024/10/15/rilasciato-il-fix-per-una-vulnerabilita-critica-di-jetpack-per-wordpress/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  [MuddyWater si evolve: attacchi più...](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "Permanent link to MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  Set 17, 2025  [0](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/#respond)
* [![File Linux usati per furto di dati e spionaggio: la campagna di APT36](https://www.securityinfo.it/wp-content/uploads/2025/08/cyber-security-4785679_1920-120x85.png)](https://www.securityinfo.it/2025/08/25/file-linux-usati-per-furto-di-dati-e-spionaggio-la-campagna-di-apt36/ "File Linux usati per furto di dati e spionaggio: la campagna di APT36")

  [File Linux usati per furto di dati e...](https://www.securityinfo.it/2025/08/25/file-linux-usati-per-furto-di-dati-e-spionaggio-la-campagna-di-apt36/ "Permanent link to File Linux usati per furto di dati e spionaggio: la campagna di APT36")

  Ago 25, 2025  [0](https://www.securityinfo.it/2025/08/25/file-linux-usati-per-furto-di-dati-e-spionaggio-la-campagna-di-apt36/#respond)
* [![LameHug, un nuovo malware che sfrutta un LLM per eseguire comandi](https://www.securityinfo.it/wp-content/uploads/...