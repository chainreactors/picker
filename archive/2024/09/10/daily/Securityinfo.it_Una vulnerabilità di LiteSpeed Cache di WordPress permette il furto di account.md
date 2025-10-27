---
title: Una vulnerabilità di LiteSpeed Cache di WordPress permette il furto di account
url: https://www.securityinfo.it/2024/09/09/una-vulnerabilita-di-litespeed-cache-di-wordpress-permette-il-furto-di-account/?utm_source=rss&utm_medium=rss&utm_campaign=una-vulnerabilita-di-litespeed-cache-di-wordpress-permette-il-furto-di-account
source: Securityinfo.it
date: 2024-09-10
fetch_date: 2025-10-06T18:36:06.945607
---

# Una vulnerabilità di LiteSpeed Cache di WordPress permette il furto di account

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

## Una vulnerabilità di LiteSpeed Cache di WordPress permette il furto di account

Set 09, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2024/09/09/una-vulnerabilita-di-litespeed-cache-di-wordpress-permette-il-furto-di-account/#respond)

---

I ricercatori di Pathstack [hanno individuato](https://patchstack.com/articles/critical-account-takeover-vulnerability-patched-in-litespeed-cache-plugin/) una nuova **vulnerabilità in LiteSpeed Cache**, un **plugin di WordPress** molto popolare che offre cache di livello server e numerose feature di ottimizzazione.

Il bug permette a un attaccante non autenticato di **ottenere** l**‘accesso all’account di qualsiasi utente loggato sul sito**; nel caso peggiore, ciò significa accedere a un account di amministratore e prendere il controllo dell’intero sito, installando altri plugin malevoli.

![LiteSpeed Cache vulnerabilità](https://www.securityinfo.it/wp-content/uploads/2024/09/wordpress-581849_1920.jpg)

Pixabay

La vulnerabilità, tracciata come CVE-2024-44000, sfrutta un **leak presente negli header HTTP** che espone l’header “Set-Cookie” dopo che l’utente ha effettuato una richiesta di login. Nel dettaglio, la funzione “ended()” del plugin richiama una funzione dei self debug per ottenere la lista di header della risposta; ciò significa che **il plugin include gli header nei propri dati di debug**. Un attaccante può accedere così alle informazioni di login dell’utente e sfruttare i dati di sessione per accedere con il suo account.

Il bug è considerato a rischio basso perché, per essere sfruttato, il plugin **deve avere la funzionalità di active debug log attiva** oppure deve essere stata attivata in passato e l’amministratore del sito non ha rimosso il file debug.log dove vengono scritte le informazioni relative agli header.

I ricercatori consigliano agli utenti che usano LiteSpeed Cache di **aggiornare il plugin alla versione 6.5.0.1 o superiori** che risolvono la vulnerabilità. Si raccomanda inoltre di controllare la presenza del file debug.log ed eliminarlo o ripulirlo nel caso si fosse usata la feature di debug in passato.

“*Questa vulnerabilità evidenzia l’importanza fondamentale di garantire la sicurezza dell’esecuzione di un processo di log di debug, di quali dati non devono essere registrati e di come viene gestito il file di log di debug*” spiega Rafie Muhammad, ricercatore di sicurezza di Patchstack. Nonostante il bug non sia semplice da sfruttare, è importante **fare attenzione ai plugin che si installano** e controllare che non registrino le informazioni di login su file di debug.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [account business](https://www.securityinfo.it/tag/account-business/), [account takeover](https://www.securityinfo.it/tag/account-takeover/), [LiteSpeed Cache](https://www.securityinfo.it/tag/litespeed-cache/), [plugin wordpress](https://www.securityinfo.it/tag/plugin-wordpress/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/), [WordPress](https://www.securityinfo.it/tag/wordpress/)

[ESET scopre NGate, malware per Android che sfrutta l'NFC per clonare le carte di pagamento](https://www.securityinfo.it/2024/09/10/eset-scopre-ngate-malware-per-android-che-sfrutta-lnfc-per-clonare-le-carte-di-pagamento/)
[CERT-AGID 31 agosto - 6 settembre: arriva la terza campagna in un mese che diffonde il malware Vidar](https://www.securityinfo.it/2024/09/09/cert-agid-31-agosto-6-settembre-malware-vidar/)

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
* [![Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/09/08/una-vulnerabilita-critica-di-sap-s-4hana-e-stata-sfruttata-dai-cybecriminali/ "Una vulnerabi...