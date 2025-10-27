---
title: Apple risolve una vulnerabilità di macOS scoperta da Microsoft
url: https://www.securityinfo.it/2022/12/20/apple-risolve-una-vulnerabilita-di-macos-scoperta-da-microsoft/?utm_source=rss&utm_medium=rss&utm_campaign=apple-risolve-una-vulnerabilita-di-macos-scoperta-da-microsoft
source: Over Security - Cybersecurity news aggregator
date: 2022-12-21
fetch_date: 2025-10-04T02:06:34.596415
---

# Apple risolve una vulnerabilità di macOS scoperta da Microsoft

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

## Apple risolve una vulnerabilità di macOS scoperta da Microsoft

Dic 20, 2022  [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/ "Articoli scritti da Dario Orlandi")
 [Concept](https://www.securityinfo.it/category/minacce-2/concept/), [Minacce](https://www.securityinfo.it/category/minacce-2/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Social engineering](https://www.securityinfo.it/category/minacce-2/social-engineering/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2022/12/20/apple-risolve-una-vulnerabilita-di-macos-scoperta-da-microsoft/#respond)

---

[Microsoft](https://www.microsoft.com/it-it/) ha recentemente [svelato tutti i dettagli](https://www.microsoft.com/en-us/security/blog/2022/12/19/gatekeepers-achilles-heel-unearthing-a-macos-vulnerability/) su un **bug di sicurezza scoperto in Apple macOS**, che potrebbe essere sfruttato da un attaccante per aggirare le protezioni di sicurezza imposte per impedire l’esecuzione di software dannoso.

Il difetto, chiamato Achilles ([CVE-2022-42821](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42821)), **è** **stato corretto da Apple** in macOS Ventura 13, Monterey 12.6.2 e Big Sur 11.7.2.

Microsoft ha descritto il difetto come un problema logico che potrebbe essere sfruttato da un’applicazione malevola per **aggirare il meccanismo di sicurezza di Apple chiamato Gatekeeper**.

Questo componente fa parte degli strumenti di sicurezza inseriti in macOS ed è progettato per garantire che **solo il software attendibile venga eseguito** sul sistema operativo.

Se un’app potenzialmente dannosa che impersona software legittimo viene scaricata da un utente, **Gatekeeper ne impedisce l’esecuzione** poiché non è correttamente firmata e autenticata da Apple.

## Impedire la marcatura

La vulnerabilità Achilles sfrutta un modello di autorizzazione chiamato Access Control Lists (ACL) per **aggiungere autorizzazioni estremamente restrittive** a un file scaricato, impedendo così a Safari di impostare l’attributo che consente poi a Gatekeeper di attivare le restrizioni.

![](https://www.securityinfo.it/wp-content/uploads/2022/12/1644979064216.jpg)

Jonathan Bar Or, principal security researcher di Microsoft

Jonathan Bar Or, principal security researcher di Microsoft, ha dichiarato: “questa strategia potrebbe essere sfruttata come **vettore per l’accesso iniziale** da malware e altre minacce e potrebbe aiutare ad aumentare il tasso di successo di campagne dannose e attacchi su macOS”.

In un ipotetico scenario di attacco, un avversario potrebbe **creare un’app falsa** e ospitarla su un server, che poi potrebbe essere inviata a un possibile obiettivo tramite social engineering o altri metodi.

Questa strategia **elude anche il nuovo Lockdown Mode** (opzionale) introdotto da Apple in macOS Ventura; gli utenti dei sistemi operativi Apple dovrebbero quindi scaricare e applicare al più presto tutti gli aggiornamenti di sicurezza disponibili per la propria versione di macOS.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Apple](https://www.securityinfo.it/tag/apple/), [Gatekeeper](https://www.securityinfo.it/tag/gatekeeper/), [macOS](https://www.securityinfo.it/tag/macos/), [Microsoft](https://www.securityinfo.it/tag/microsoft/), [Ventura](https://www.securityinfo.it/tag/ventura/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[Il gruppo UNC4166 colpisce il governo ucraino](https://www.securityinfo.it/2022/12/21/il-gruppo-unc4166-colpisce-il-governo-ucraino/)
[Cloud: sfide e opportunità del collante della "vita ibrida"](https://www.securityinfo.it/2022/12/20/cloud-sfide-opportunita/)

---

![](https://secure.gravatar.com/avatar/9ba6108fae91c2be66a7ef45ac2db49a?s=90&d=mm&r=g)

##### [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/)

##### Articoli correlati

* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_d4x8rid4x8rid4x8-120x85.png)](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  [Firewall Cisco sotto attacco: una nuova...](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Permanent link to Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  Set 29, 2025  [0](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/#respond)
* [![Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.](https://www.securityinfo.it/wp-content/uploads/2025/09/ai-generated-9053184_1920-120x85.jpg)](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/ "Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.")

  [Attaccanti sfruttano un bug di...](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/ "Permanent link to Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.")

  Set 24, 2025  [0](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/#respond)
* [![Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/09/08/una-vulnerabilita-critica-di-sap-s-4hana-e-stata-sfruttata-dai-cybecriminali...