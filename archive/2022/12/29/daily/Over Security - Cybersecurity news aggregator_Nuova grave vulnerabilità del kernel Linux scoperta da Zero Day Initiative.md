---
title: Nuova grave vulnerabilità del kernel Linux scoperta da Zero Day Initiative
url: https://www.securityinfo.it/2022/12/28/nuova-grave-vulnerabilita-del-kernel-linux-scoperta-da-zero-day-initiative/?utm_source=rss&utm_medium=rss&utm_campaign=nuova-grave-vulnerabilita-del-kernel-linux-scoperta-da-zero-day-initiative
source: Over Security - Cybersecurity news aggregator
date: 2022-12-29
fetch_date: 2025-10-04T02:42:01.845269
---

# Nuova grave vulnerabilità del kernel Linux scoperta da Zero Day Initiative

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

## Nuova grave vulnerabilità del kernel Linux scoperta da Zero Day Initiative

Dic 28, 2022  [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/ "Articoli scritti da Dario Orlandi")
 [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2022/12/28/nuova-grave-vulnerabilita-del-kernel-linux-scoperta-da-zero-day-initiative/#respond)

---

La [Zero Day Initiative (Zdi),](https://www.zerodayinitiative.com/) una società di ricerca sulla sicurezza zero-day, ha annunciato di avere individuato una **nuova vulnerabilità del kernel Linux**. Questo bug consente a utenti remoti autenticati di recuperare informazioni sensibili ed eseguire codice.

Che il problema sia piuttosto grave è evidente dalla [classificazione Cvss](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?calculator&version=3.0&vector=(AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:H)): originariamente Zdi aveva assegnato al bug una valutazione di 10, ma dopo una revisione più attenta il **punteggio è sceso a 9,6**.

**La vulnerabilità è presente in ksmbd**, il modulo SMB (Server Message Block) in-kernel di Linux 5.15; il problema deriva dalla mancanza di convalida dell’esistenza di un oggetto prima di eseguire operazioni su di esso. Un utente malintenzionato può sfruttare questa vulnerabilità per eseguire codice nel contesto del kernel.

Ksmbd è stato aggiunto al kernel nel 2021, ed è stato sviluppato da Samsung. Il suo scopo è **migliorare le prestazioni per la gestione dei file SMB3**, la versione più recente del protocollo di condivisione dei file e degli oggetti hardware utilizzato principalmente da Windows

## Samba non è coinvolto

Jeremy Allison, uno dei creatori di Samba, ha commentato: “**ksmbd non condivide alcun codice con Samba**; è sviluppato completamente da zero. Quindi, questo problema non ha nulla a che fare con il file server Samba”.

![](https://www.securityinfo.it/wp-content/uploads/2022/12/1280px-Jeremy_allison.jpg)

Jeremy Allison, sviluppatore di Samba.

Qualsiasi distribuzione che utilizza il kernel Linux 5.15 o superiore è potenzialmente vulnerabile. Tra gli altri, Ubuntu 22.04 e i suoi derivati e Deepin Linux 20.3. Nell’ambito delle distribuzioni server, **quello di Ubuntu è probabilmente il caso più preoccupante**; altre distribuzioni, come la famiglia Red Hat Enterprise Linux (Rhel), non usano il kernel 5.15.

Per **verificare la versione del kernel e la presenza del modulo vulnerabile** è sufficiente raggiungere una finestra del terminale e digitate i comandi *uname -r* e *modinfo ksmb.*

Se il modulo è presente, la soluzione migliore è l’**aggiornamento al kernel 5.15.61 o successivi**; non molte distribuzioni, però, offrono già oggi l’upgrade alla versione più recente del kernel. In alternativa, è più saggio evitare di usare il modulo ksmbd, anche rinunciando a parte delle prestazioni.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [5.15](https://www.securityinfo.it/tag/5-15/), [Deepin](https://www.securityinfo.it/tag/deepin/), [Kernel](https://www.securityinfo.it/tag/kernel/), [ksmbd](https://www.securityinfo.it/tag/ksmbd/), [Linux](https://www.securityinfo.it/tag/linux/), [SMB](https://www.securityinfo.it/tag/smb/), [Ubuntu](https://www.securityinfo.it/tag/ubuntu/)

[Il progresso della cybersecurity: tre previsioni per il 2023](https://www.securityinfo.it/2022/12/28/cybersecurity-previsioni-sicurezza/)
[I robot sono pronti per il posto di lavoro?](https://www.securityinfo.it/2022/12/27/i-robot-sono-pronti-per-il-posto-di-lavoro/)

---

![](https://secure.gravatar.com/avatar/9ba6108fae91c2be66a7ef45ac2db49a?s=90&d=mm&r=g)

##### [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/)

##### Articoli correlati

* [![File Linux usati per furto di dati e spionaggio: la campagna di APT36](https://www.securityinfo.it/wp-content/uploads/2025/08/cyber-security-4785679_1920-120x85.png)](https://www.securityinfo.it/2025/08/25/file-linux-usati-per-furto-di-dati-e-spionaggio-la-campagna-di-apt36/ "File Linux usati per furto di dati e spionaggio: la campagna di APT36")

  [File Linux usati per furto di dati e...](https://www.securityinfo.it/2025/08/25/file-linux-usati-per-furto-di-dati-e-spionaggio-la-campagna-di-apt36/ "Permanent link to File Linux usati per furto di dati e spionaggio: la campagna di APT36")

  Ago 25, 2025  [0](https://www.securityinfo.it/2025/08/25/file-linux-usati-per-furto-di-dati-e-spionaggio-la-campagna-di-apt36/#respond)
* [![Due bug LPE consentono di ottenere i privilegi di root su Linux](https://www.securityinfo.it/wp-content/uploads/2025/06/hacker-2300772_1920-120x85.jpg)](https://www.securityinfo.it/2025/06/18/due-bug-lpe-consentono-di-ottenere-i-privilegi-di-root-su-linux/ "Due bug LPE consentono di ottenere i privilegi di root su Linux")

  [Due bug LPE consentono di ottenere i...](https://www.securityinfo.it/2025/06/18/due-bug-lpe-consentono-di-ottenere-i-privilegi-di-root-su-linux/ "Permanent link to Due bug LPE consentono di ottenere i privilegi di root su Linux")

  Giu 18, 2025  [0](https://www.securityinfo.it/2025/06/18/due-bug-lpe-consentono-di-ottenere-i-privilegi-di-root-su-linux/#respond)
* [![XorDDoS, il DDoS contro Linux evolve e continua a mietere vittime](https://www.securityinfo.it/wp-content/uploads/2025/04/8289982_25332-scaled-120x85.jpg)](https://www.securityinfo.it/2025/04/18/xorddos-il-ddos-contro-linux-continua-a-mietere-vittime/ "XorDDoS, il DDoS contro Linux evolve e continua a mietere vittime")

  [XorDDoS, il DDoS contro Linux evolve e...](https://www.securityinfo.it/2025/04/18/xorddos-il-ddos-contro-linux-continua-a-mietere-vittime/ "Permanent link to XorDDoS, il DDo...