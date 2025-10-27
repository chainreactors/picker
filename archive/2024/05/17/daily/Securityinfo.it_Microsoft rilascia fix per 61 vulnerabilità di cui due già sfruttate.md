---
title: Microsoft rilascia fix per 61 vulnerabilità di cui due già sfruttate
url: https://www.securityinfo.it/2024/05/16/microsoft-rilascia-fix-per-61-vulnerabilita-di-cui-due-gia-sfruttate/?utm_source=rss&utm_medium=rss&utm_campaign=microsoft-rilascia-fix-per-61-vulnerabilita-di-cui-due-gia-sfruttate
source: Securityinfo.it
date: 2024-05-17
fetch_date: 2025-10-06T17:17:01.781588
---

# Microsoft rilascia fix per 61 vulnerabilità di cui due già sfruttate

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

## Microsoft rilascia fix per 61 vulnerabilità di cui due già sfruttate

Mag 16, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2024/05/16/microsoft-rilascia-fix-per-61-vulnerabilita-di-cui-due-gia-sfruttate/#respond)

---

Nell’ultimo aggiornamento di sicurezza, **Microsoft [ha rilasciato i fix](https://msrc.microsoft.com/update-guide/releaseNote/2024-May) per 61 vulnerabilità**; tra queste, **due risultano sfruttate attivamente dagli attaccanti.**

La **CVE-2024-30040** è un bug di **security bypass** che colpisce **Windows MSHTML Platform**, il browser engine proprietario della compagnia usato per renderizzare le pagine web. A causa di una validazione errata degli input, la vulnerabilità consente a un attaccante di bypassare i controlli di sicurezza ed **eseguire codice sulla macchina nel contesto dell’utente.** Per sfruttare il bug l’attaccante deve convincere la vittima a scaricare e manipolare un file malevolo sul sistema.

L’altra vulnerabilità zero-day è la **CVE-2024-30051**, un bug che consente a un attaccante di **ottenere i privilegi di SYSTEM** sulla macchina colpita ed eseguire codice. La vulnerabilità, un heap-based buffer overflow, colpisce la **DWM Core Library**, la libreria principale del Desktop Window Manager, responsabile degli effetti grafici del sistema operativo.

Gli attaccanti stanno già sfruttando attivamente le due vulnerabilità; la seconda, in particolare, è stata usata in combinazione con il malware **QakBot** a partire da aprile, come riportato dai ricercatori di [SecureList](https://securelist.com/cve-2024-30051/112618/) di Kaspersky.

![Microsoft sicurezza](https://www.securityinfo.it/wp-content/uploads/2024/05/microsoft-1537592_1920.jpg)

Nel report dei fix di [Microsoft](https://www.securityinfo.it/2024/05/10/microsoft-annuncia-il-zero-trust-dns/) non si segnalano vulnerabilità critiche, ma tra i bug della lista ce ne sono 7 a criticità elevata. Oltre alla prima vulnerabilità già segnalata ci sono la CVE-2024-30010 e la CVE-2024-30017 che colpiscono **Hyper-V** e consentono entrambe l’**esecuzione remota di codic**e. Individuati anche un bug in **WDAC OLE DB provider per SQL** che consente di **eseguire codice remoto** nel contesto del client SQL utente, e una vulnerabilità di **elevation of privilege** nel **Brokering File System.**

Il **Routing and Remote Access Service**, usato per creare applicazioni che amministrano il routing e l’accesso remoto al SO, soffre anch’esso di una vulnerabilità di **esecuzione remota di codice** dovuta a un errore di troncamento remoto. Infine, anche il servizio **SharePoint Server Remote** presenta un bug di **esecuzione remota di codice**, in questo caso causata dalla deserializzazione di dati untrusted.

Le patch sono disponibili per il download. Il consiglio è, come sempre, di **aggiornare il prima possibile i prodotti vulnerabili** con gli update del vendor.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [elevation of privileges](https://www.securityinfo.it/tag/elevation-of-privileges/), [esecuzione remota codice](https://www.securityinfo.it/tag/esecuzione-remota-codice/), [Microsoft](https://www.securityinfo.it/tag/microsoft/), [Qakbot](https://www.securityinfo.it/tag/qakbot/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/), [Zero-day](https://www.securityinfo.it/tag/zero-day/)

[Google risolve una vulnerabilità zero-day: è la terza in una settimana](https://www.securityinfo.it/2024/05/16/google-risolve-una-vulnerabilita-zero-day-e-la-terza-in-una-settimana/)
[Apple e Google rilasciano una feature di anti-tracciamento bluetooth](https://www.securityinfo.it/2024/05/14/apple-e-google-rilasciano-una-feature-di-anti-tracciamento-bluetooth/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_d4x8rid4x8rid4x8-120x85.png)](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  [Firewall Cisco sotto attacco: una nuova...](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Permanent link to Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  Set 29, 2025  [0](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/#respond)
* [![Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.](https://www.securityinfo.it/wp-content/uploads/2025/09/ai-generated-9053184_1920-120x85.jpg)](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/ "Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.")

  [Attaccanti sfruttano un bug di...](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/ "Permanent link to Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.")

  Set 24, 2025  [0](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s...