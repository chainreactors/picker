---
title: Google risolve una vulnerabilità zero-day: è la terza in una settimana
url: https://www.securityinfo.it/2024/05/16/google-risolve-una-vulnerabilita-zero-day-e-la-terza-in-una-settimana/
source: Over Security - Cybersecurity news aggregator
date: 2024-05-17
fetch_date: 2025-10-06T17:20:06.363079
---

# Google risolve una vulnerabilità zero-day: è la terza in una settimana

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

## Google risolve una vulnerabilità zero-day: è la terza in una settimana

Mag 16, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2024/05/16/google-risolve-una-vulnerabilita-zero-day-e-la-terza-in-una-settimana/#respond)

---

Ieri Google [ha comunicato](https://chromereleases.googleblog.com/2024/05/stable-channel-update-for-desktop_15.html) di aver risolto una **vulnerabilità zero-day già sfruttata** dagli attaccanti che colpisce **Chrome** nelle versioni precedenti alla 125.0.6422.60.

Il bug, CVE-2024-4947, segnalato da due ricercatori di Kaspersky, è una vulnerabilità di type confusion che colpisce l’**engine V8 di JavaScript** di Chromium e consente a un attaccante di **eseguire codice da remoto in una sandbox** utilizzando una pagina HTML creata ad hoc.

La vulnerabilità, considerata a rischio alto, è la **terza zero-day scoperta questa settimana** da Google: le altre due sono la CVE-2024-4671 e la CVE-2024-4949, entrambe patchate con l’ultima versione stabile di Chrome.

La prima è una vulnerabilità di **user after free** presente in **Visuals** nelle versioni di Chrome precedenti alla 124.0.6367.201 che consente a un attaccante remoto che è riuscito a compromettere il processo di render di eseguire un sandbox escape. Il secondo è un altro bug di **user after free** che colpisce l’**engine V8** che consente a un attaccante remoto di sfruttare un heap corruption usando una specifica pagina HTML.

Nella nota di sicurezza pubblicata ieri, anche Microsoft [ha confermato](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnotes-security#may-15-2024) che la CVE-2024-4671, presente su Edge, è stata sfruttata da gruppi di attaccanti. Al momento però la compagnia non ha ancora rilasciato fix di sicurezza per il proprio browser.

![](https://www.securityinfo.it/wp-content/uploads/2024/05/hacking-3112539_1920-1.png)

Pixabay

La 4947 è la settima vulnerabilità zero-day che colpisce Chrome dall’inizio dell’anno. Da gennaio a oggi i ricercatori hanno infatti individuato un bug out-of-bound sempre nell’engine V8 di Jabascript, una vulnerabilità di type confusion nello standard WebAssembly, un bug user-after-free nell’API WebCodecs e una out-of-bound read in V8, più queste ultime tre vulnerabilità.

Gli altri bug individuati consentono di accedere a informazioni sensibili dell’utente ed eseguire codice remoto, sempre utilizzando una pagina HTML creata appositamente dall’attaccante.

È fondamentale **aggiornare il prima possibile Chrome all’ultima versione disponibile** e controllare il sito del vendor per eventuali aggiornamenti.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Chrome](https://www.securityinfo.it/tag/chrome/), [Chromium](https://www.securityinfo.it/tag/chromium/), [esecuzione codice remoto](https://www.securityinfo.it/tag/esecuzione-codice-remoto/), [html](https://www.securityinfo.it/tag/html/), [Type Confusion](https://www.securityinfo.it/tag/type-confusion/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[Scoperti deepfake iraniani e cinesi per influenzare le elezioni americane](https://www.securityinfo.it/2024/05/17/scoperti-deepfake-iraniani-e-cinesi-per-influenzare-le-elezioni-americane/)
[Microsoft rilascia fix per 61 vulnerabilità di cui due già sfruttate](https://www.securityinfo.it/2024/05/16/microsoft-rilascia-fix-per-61-vulnerabilita-di-cui-due-gia-sfruttate/)

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
* [![Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/09/08/una-vulnerabilita-critica-di-sap-s-4hana-e-stata-sfruttata-dai-cybecriminali/ "Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali")

  [Una v...