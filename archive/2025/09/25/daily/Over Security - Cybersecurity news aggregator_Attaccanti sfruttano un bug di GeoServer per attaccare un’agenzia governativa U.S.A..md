---
title: Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.
url: https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-25
fetch_date: 2025-10-02T20:39:16.658968
---

# Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.

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

## Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.

Set 24, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [Hacking](https://www.securityinfo.it/category/news/hacking-news/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/#respond)

---

In un recente [advisory di sicurezza](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-266a), la CISA ha reso noto che un gruppo di attaccanti ha sfruttato una **vulnerabilità di GeoServer**per attaccare un’agenzia governativa U.S.A., riuscendo ad **agire di nascosto per tre settimane** prima di far scattare qualsiasi alert di sicurezza.

Il gruppo ha sfruttato la CVE-2024-36401, una vulnerabilità di GeoServer che permette l’**esecuzione di codice remoto** anche agli utenti non autenticati. Secondo il report, il gruppo è riuscito ad accedere separatamente a due server per poi muoversi lateralmente verso altri due.

La vulnerabilità era stata resa nota il 30 giugno 2024 e gli attaccanti sono riusciti a ottenere un primo accesso ai sistemi governativi l’11 luglio, poco più di una settimana dopo. Il secondo server è stato compromesso il 24 luglio. Su ogni server, gli attaccanti hanno caricato alcune web shell, tra le quali China Chopper, insieme a script per l’accesso remoto, il mantenimento della persistenza, l’esecuzione di comandi da remoto e l’escalation dei privilegi.

Il gruppo, dopo aver ottenuto l’accesso, ha anche eseguito una serie di **tecniche brute force per ottenere le password** salvate sui sistemi.

![GeoServer](https://www.securityinfo.it/wp-content/uploads/2025/09/ai-generated-9053184_1920.jpg)

Oltre all’analisi tecnica dell’accaduto, CISA ha evidenziato gli errori commessi dall’agenzia che hanno portato all’incidente, al fine di sensibilizzare le organizzazioni. In primo luogo, **l’agenzia non aveva applicato le patch disponibili per la vulnerabilità**. “*Le agenzie FCEB sono obbligate a risolvere le vulnerabilità presenti nel catalogo KEV della CISA entro i tempi prescritti dalla direttiva operativa vincolante (BOD) 22-01*” spiega la CISA.

L’agenzia, inoltre, **non ha testato né messo in pratica il suo Piano di Risposta agli Incidenti** (IRP), né l’IRP prevedeva il coinvolgimento di terze parti che potessero accedere alle risorse necessarie, complicando l’attività della CISA.

Infine, gli alert EDR non venivano monitorati adeguatamente e alcuni sistemi esposti a internet non erano protetti.

L’Agenzia di cybersecurity statunitense non ha reso nota la provenienza del gruppo, ma l’uso di China Copper indicherebbe un coinvolgimento di cybercriminali cinesi.

CISA ha soprannominato queste tre criticità delle **“lesson learned”**; bisognerà valutare a stretto giro se effettivamente queste problematiche sono state recepite e comprese dalle organizzazioni.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [ChinaChopper](https://www.securityinfo.it/tag/chinachopper/), [CISA](https://www.securityinfo.it/tag/cisa/), [EDR](https://www.securityinfo.it/tag/edr/), [esecuzione codice remoto](https://www.securityinfo.it/tag/esecuzione-codice-remoto/), [GeoServer](https://www.securityinfo.it/tag/geoserver/), [IRP](https://www.securityinfo.it/tag/irp/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[L'importanza delle coperture assicurative cyber per ridurre i costi degli attacchi informatici](https://www.securityinfo.it/2025/09/25/limportanza-delle-coperture-assicurative-cyber-per-ridurre-i-costi-degli-attacchi-informatici/)
[Campagne basate su installer ScreenConnect distribuiscono RAT multipli: l'analisi di Acronis TRU](https://www.securityinfo.it/2025/09/22/campagne-basate-su-installer-screenconnect-distribuiscono-rat-multipli-lanalisi-di-acronis-tru/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_d4x8rid4x8rid4x8-120x85.png)](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  [Firewall Cisco sotto attacco: una nuova...](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Permanent link to Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  Set 29, 2025  [0](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/#respond)
* [![Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/09/08/una-vulnerabilita-critica-di-sap-s-4hana-e-stata-sfruttata-dai-cybecriminali/ "Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali")

  [Una vulnerabilità critica di SAP...](https://www.securityinfo.it/2025/09/08/una-vulnerabilita-critica-di-sap-s-4hana-e-stata-sfruttata-dai-cybecriminali/ "Permanent link to Una vulnerabilità critica di SAP S/4HANA è ...