---
title: Downfall: Intel era a conoscenza della vulnerabilità da un anno
url: https://www.securityinfo.it/2023/08/14/downfall-intel-era-a-conoscenza-della-vulnerabilita-da-un-anno/?utm_source=rss&utm_medium=rss&utm_campaign=downfall-intel-era-a-conoscenza-della-vulnerabilita-da-un-anno
source: Securityinfo.it
date: 2023-08-15
fetch_date: 2025-10-04T12:04:20.880999
---

# Downfall: Intel era a conoscenza della vulnerabilità da un anno

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

## Downfall: Intel era a conoscenza della vulnerabilità da un anno

Ago 14, 2023  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2023/08/14/downfall-intel-era-a-conoscenza-della-vulnerabilita-da-un-anno/#respond)

---

Daniel Moghimi, un ricercatore di Google, ha individuato **[Downfall](https://downfall.page/)**, una **falla nei processori Intel che consente di ottenere i dati sensibili degli utenti di un sistema.**

La vulnerabilità, identificata come CVE-2022-40982, è **causata da una feature di ottimizzazione di memoria dei processori che rivela alcuni registri hardware interni alle componenti software**; ciò, spiega Moghimi, consente a un software malevolo di accedere ai dati memorizzati da altri programmi, cosa che normalmente non dovrebbe accadere.

![Downfall Intel - Credits: Dan74- Depositphotos](https://www.securityinfo.it/wp-content/uploads/2023/08/Depositphotos_148466087_L.jpg)

Credits: Dan74- Depositphotos

Nel dettaglio, l’istruzione incriminata è la “gather”  che si occupa di velocizzare l’accesso ai dati in memoria; durante il processo, però, **la funzione rende disponibile alle applicazioni il contenuto dei registri interni.**

Grazie a questa vulnerabilità **un attaccante è in grado di [sottrarre password e chiavi di cifratura](https://www.securityinfo.it/2023/05/19/il-leak-delle-chiavi-private-di-intel-avra-conseguenze-a-lungo-termine/)** per poi sferrare altri attacchi volti a violare l’integrità dei dati sul dispositivo.

**Per sfruttare la vulnerabilità l’attaccante e la vittima devono condividere lo stesso processore fisico**, una casistica oggi abbastanza frequente sui dispositivi che implementano multithreading simultaneo e multitasking con prelazione. Il ricercatore è riuscito a replicare il caso in sole due settimane, sviluppando un attacco end-to-end in grado di sottrarre chiavi di cifratura da OpenSSL.

Secondo Moghimi è possibile sfruttare la vulnerabilità anche da remoto tramite browser, anche se in questo caso l’esecuzione dell’attacco è più complessa e necessita di ulteriori approfondimenti.

![Downfall Intel](https://www.securityinfo.it/wp-content/uploads/2023/08/matrix-1799651_1920.jpg)

Pixabay

La vulnerabilità è presente da almeno 9 anni: i processori vulnerabili vanno dagli Intel Core Skylake di sesta generazione fino ai Tiger Lake di undicesima generazione. **Moghimi aveva individuato la falla un anno fa**, il 24 agosto 2022, ma **Intel ha deciso di renderla nota soltanto all’inizio di questo mese.**

Intel ha rilasciato la [lista completa di processori vulnerabili](https://www.intel.com/content/www/us/en/developer/topic-technology/software-security-guidance/processors-affected-consolidated-product-cpu-model.html) invitando gli utenti ad aggiornarli all’ultima versione del firmware disponibile. La compagnia ha affermato che **il fix potrebbe causare fino al 50% di overhead in più nell’esecuzione di alcuni carichi di lavoro.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [downfall](https://www.securityinfo.it/tag/downfall/), [Intel](https://www.securityinfo.it/tag/intel/), [processori](https://www.securityinfo.it/tag/processori/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[Smantellata 16shop, piattaforma di "phishing-as-a-service"](https://www.securityinfo.it/2023/08/16/smantellata-16shop-piattaforma-di-phishing-as-a-service/)
[Decine di cluster Kubernetes colpiti da campagne di crypto-mining ancora attive](https://www.securityinfo.it/2023/08/11/decine-di-cluster-kubernetes-colpiti-da-campagne-di-crypto-mining-ancora-attive/)

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
* [![Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali]...