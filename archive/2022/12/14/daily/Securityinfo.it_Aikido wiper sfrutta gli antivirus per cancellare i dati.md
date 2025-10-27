---
title: Aikido wiper sfrutta gli antivirus per cancellare i dati
url: https://www.securityinfo.it/2022/12/13/aikido-wiper-sfrutta-gli-antivirus-per-cancellare-i-dati/?utm_source=rss&utm_medium=rss&utm_campaign=aikido-wiper-sfrutta-gli-antivirus-per-cancellare-i-dati
source: Securityinfo.it
date: 2022-12-14
fetch_date: 2025-10-04T01:27:28.612019
---

# Aikido wiper sfrutta gli antivirus per cancellare i dati

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

## Aikido wiper sfrutta gli antivirus per cancellare i dati

Dic 13, 2022  [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/ "Articoli scritti da Dario Orlandi")
 [Malware](https://www.securityinfo.it/category/news/malware-news/), [Minacce](https://www.securityinfo.it/category/minacce-2/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2022/12/13/aikido-wiper-sfrutta-gli-antivirus-per-cancellare-i-dati/#respond)

---

Or Yair, un ricercatore di [SafeBreach](https://www.safebreach.com/), ha ideato una tecnica per sfruttare le funzioni degli antivirus o delle soluzioni Edr installate nel sistema per **agire come un data wiper**, una categoria di malware che elimina o distrugge i dati con lo scopo di danneggiare la vittima.Il ricercatore ha avuto l’idea di sfruttare le funzioni di protezione offerte dagli strumenti di sicurezza, che spesso agiscono preventivamente individuando ed eliminando i file che considerano pericolosi.

Questi tool sono infatti sempre attivi e analizzano il filesystem alla ricerca di potenziali pericoli. Il ricercatore ha spiegato che il processo di eliminazione di una minaccia si svolge generalmente in due fasi: **prima il tool identifica il pericolo, e poi lo elimina**. Yair ha pensato di sfruttare l’intervallo che intercorre tra i due eventi per sostituire il file originale e quindi far agire l’antivirus su dati diversi da quelli rilevati.

## Windows esegue senza fare domande

L’antivirus non consente modifiche ai file rilevati prima della cancellazione, ma è stato sufficiente **mantenere attivo un handle** per evitare il blocco da parte dell’antivirus. Il software di sicurezza non è quindi in grado di cancellare il file e suggerisce il riavvio per completare la pulizia.

![](https://www.securityinfo.it/wp-content/uploads/2022/12/reboot.png)

Fonte: SafeBreach

Le operazioni da completare al reboot vengono **memorizzate in una specifica chiave del registro**, che Windows legge al riavvio eseguendo poi le istruzioni senza effettuare nessuna ulteriore verifica.

Seguendo questa strategia, il ricercatore ha creato un tool chiamato Aikido Wiper che ha poi provveduto a testare con 11 strumenti antimalware, con risultati piuttosto preoccupanti: **oltre la metà dei software, infatti, è risultato vulnerabile** a questa tecnica. L’elenco comprende Microsoft Defender e Defender for Endpoint, SentinelOne, TrendMicro Apex One e gli antivirus di Avast e Avg. Hanno invece resistito le soluzioni di PaloAlto, Cylance, CrowdStrike, McAfee e Bitdefender.

Il problema è stato segnalato ai produttori tra luglio e agosto, e nel frattempo la vulnerabilità è stata **risolta con la distribuzione di aggiornamenti** per i motori di scansione.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Aikido](https://www.securityinfo.it/tag/aikido/), [Avast](https://www.securityinfo.it/tag/avast/), [AVG](https://www.securityinfo.it/tag/avg/), [Microsoft Defender](https://www.securityinfo.it/tag/microsoft-defender/), [SafeBreach](https://www.securityinfo.it/tag/safebreach/), [SentinelOne](https://www.securityinfo.it/tag/sentinelone/), [TrendMicro](https://www.securityinfo.it/tag/trendmicro/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/), [wiper](https://www.securityinfo.it/tag/wiper/)

[La sicurezza IT assume sempre più importanza in Europa](https://www.securityinfo.it/2022/12/15/sicurezza-it-europa/)
[Ancora più protezione per gli utenti enterprise di Microsoft Defender for Endpoint](https://www.securityinfo.it/2022/12/13/protezione-enterprise-microsoft-defender-endpoint/)

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
* [![Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/09/08/una-vulnerabilita-critica-di-sap-s-4hana-e-stata-sfruttata-dai-cybecriminali/ "Una vulnerabilità cri...