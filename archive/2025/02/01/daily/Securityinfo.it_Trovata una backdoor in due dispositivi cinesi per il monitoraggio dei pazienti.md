---
title: Trovata una backdoor in due dispositivi cinesi per il monitoraggio dei pazienti
url: https://www.securityinfo.it/2025/01/31/trovata-una-backdoor-in-due-dispositivi-cinesi-per-il-monitoraggio-dei-pazienti/?utm_source=rss&utm_medium=rss&utm_campaign=trovata-una-backdoor-in-due-dispositivi-cinesi-per-il-monitoraggio-dei-pazienti
source: Securityinfo.it
date: 2025-02-01
fetch_date: 2025-10-06T20:38:15.019100
---

# Trovata una backdoor in due dispositivi cinesi per il monitoraggio dei pazienti

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

## Trovata una backdoor in due dispositivi cinesi per il monitoraggio dei pazienti

Gen 31, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Hacking](https://www.securityinfo.it/category/news/hacking-news/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/01/31/trovata-una-backdoor-in-due-dispositivi-cinesi-per-il-monitoraggio-dei-pazienti/#respond)

---

Pochi giorni fa la CISA [ha pubblicato](https://www.cisa.gov/news-events/cybersecurity-advisories) un avviso di sicurezza in cui informa che **due dispositivi della serie Contec CMS8000**, un sistema di monitoraggio dei pazienti, contengono una **backdoor legata a un indirizzo IP cinese**. Oltre alla backdoor, l’Agenzia statunitense ha trovato anche una funzionalità specifica per la raccolta dei dati sanitari del paziente.

“*La CISA ritiene che l’inclusione di questa backdoor nel firmware del monitor possa creare condizioni tali da **consentire l’esecuzione di codice in remoto e la modifica del dispositivo con la possibilità di alterarne la configurazione**. Ciò comporta un rischio per la sicurezza del paziente, in quanto un monitor malfunzionante potrebbe portare a risposte improprie ai segni vitali visualizzati dal dispositivo*” si legge nell’avviso.

![backdoor pazienti](https://www.securityinfo.it/wp-content/uploads/2025/01/security-6901712_1920.jpg)

**I dispositivi della serie Contec CMS8000 vengono prodotti in Cina e utilizzati globalmente negli ospedali e nei centri sanitari.** I device sono in grado di monitorare l’attività cardiaca, i livelli di saturazione di ossigeno nel sangue, la pressione del sangue, la temperatura e il respiro di un paziente.

La CISA ha analizzato la versione 2.0.6, un’immagine pre-release della 2.0.8 e un’altra pre-release senza numero di versione scoprendo che sono tutte e tre afflitte dalla backdoor; questa, oltre a raccogliere i dati dei pazienti, consente di **scaricare ed eseguire sul dispositivo file da remoto**. L’indirizzo IP, trovato hard-coded nel codice della [backdoor](https://www.securityinfo.it/2025/01/08/gli-stati-uniti-cambiano-opinione-sulla-crittografia-e-sulle-backdoor/), non è associato ad alcun costruttore di dispositivi medici o a centri sanitari, bensì a un’università.

Il team dell’Agenzia ha subito compreso che il codice individuato non era un meccanismo di aggiornamento: la funzione infatti non prevede alcun controllo di integrità, né di tracking degli update; inoltre, quando viene eseguito, **il codice sovrascrive i file presenti sul dispositivo** per fare in modo che gli utenti non si accorgano del software in esecuzione.

La CISA ha creato una rete simulata, un finto profilo di un paziente e ha collegato diversi device di monitoraggio ai **Contec CMS8000**. Dopo la routine di startup, il sistema si è collegato subito all’indirizzo IP specificato nel codice (in questo caso modificato dai ricercatori) e ha cominciato a **inviare i dati raccolti dalla sensoristica.**

Al momento non ci sono patch disponibili per il dispositivo. La CISA consiglia alle organizzazioni sanitarie di tutto il mondo di **disconnettere i device dalla rete**, se possibile, e comunque di verificare l’eventuale presenza di qualsiasi anomalia, come una differenza tra lo stato fisico del paziente e i valori mostrati su schermo.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [backdoor](https://www.securityinfo.it/tag/backdoor/), [Cina](https://www.securityinfo.it/tag/cina/), [CISA](https://www.securityinfo.it/tag/cisa/), [Contec CMS8000](https://www.securityinfo.it/tag/contec-cms8000/), [cyberspionaggio](https://www.securityinfo.it/tag/cyberspionaggio/), [Sanità](https://www.securityinfo.it/tag/sanita/)

[DeepSeek: il top della tecnologia cinese dimentica di chiudere il database esposto](https://www.securityinfo.it/2025/01/31/deepseek-il-top-della-tecnologia-cinese-dimentica-di-chiudere-il-database-esposto/)
[Vulnerabilità Subaru: il vero problema sono le politiche di gestione dei dati](https://www.securityinfo.it/2025/01/30/vulnerabilita-subaru-il-vero-problema-sono-le-politiche-di-gestione-dei-dati/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.](https://www.securityinfo.it/wp-content/uploads/2025/09/ai-generated-9053184_1920-120x85.jpg)](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/ "Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.")

  [Attaccanti sfruttano un bug di...](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/ "Permanent link to Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.")

  Set 24, 2025  [0](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/#respond)
* [![MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente")

  [MuddyWater si evolve: attacchi più...](https://www.securityinfo.it/2025/09/17/muddywater-si-...