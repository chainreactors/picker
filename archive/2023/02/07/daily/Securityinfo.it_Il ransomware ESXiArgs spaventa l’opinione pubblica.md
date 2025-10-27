---
title: Il ransomware ESXiArgs spaventa l’opinione pubblica
url: https://www.securityinfo.it/2023/02/06/il-ransomware-esxiargs-spaventa-lopinione-pubblica/?utm_source=rss&utm_medium=rss&utm_campaign=il-ransomware-esxiargs-spaventa-lopinione-pubblica
source: Securityinfo.it
date: 2023-02-07
fetch_date: 2025-10-04T05:54:10.107833
---

# Il ransomware ESXiArgs spaventa l’opinione pubblica

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

## Il ransomware ESXiArgs spaventa l’opinione pubblica

Feb 06, 2023  [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/ "Articoli scritti da Dario Orlandi")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [Minacce](https://www.securityinfo.it/category/minacce-2/), [News](https://www.securityinfo.it/category/news/), [Ransomware](https://www.securityinfo.it/category/minacce-2/ransomware/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2023/02/06/il-ransomware-esxiargs-spaventa-lopinione-pubblica/#respond)

---

A partire da venerdì 3 febbraio, **una nuova campagna ransomware ha colpito molti server VMware ESXi** in tutto il mondo sfruttando le vulnerabilità di sicurezza [CVE-2021-21972](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-21972) e [CVE-2021-21974](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-21974), categorizzate come critiche (con punteggio di 9.8 e 8.8 su 10 nella scala Cvss).

Le vulnerabilità interessano i sistemi ESXi 6.5.x, 6.7.x e 7.x e possono essere sfruttate per creare un overflow nel servizio OpenSLP, che viene poi utilizzato da attori malintenzionati per eseguire codice arbitrario. Il problema è in realtà **stato risolto con [una patch](https://www.vmware.com/security/advisories/VMSA-2021-0002.html) distribuita da VMware quasi due anni or sono**, il 23 febbraio 2021.

Per bloccare gli attacchi gli amministratori possono **disabilitare il servizio Service Location Protocol (SLP)** sui sistemi vulnerabili, ma la soluzione definitiva è naturalmente quella di aggiornare i sistemi.

Alcune dichiarazioni a caldo provenienti dalla Francia, e in particolare dal provider [OVHcloud](https://blog.ovhcloud.com/ransomware-targeting-vmware-esxi/), hanno in un primo tempo associato gli attacchi al ransomware Nevada, ma le richieste di riscatto pubblicate sembrano provenire da **una nuova famiglia di malware**, che è stata denominata ESXiArgs.

![](https://www.securityinfo.it/wp-content/uploads/2023/02/ESXiArgs-ransom-note.png)

Fonte: BleepingComputer

## Siamo sotto attacco?

La campagna ha avuto **una vasta eco mediatica** in Italia, dove sono stati dipinti scenari piuttosto allarmistici che hanno portato il Governo a convocare nella mattinata del 6 febbraio i vertici dell’Agenzia per la cybersicurezza e del Dipartimento informazione e sicurezza.

Da quanto emerge, l’attacco non sembra particolarmente innovativo e neppure troppo sofisticato: sono però molti i server colpiti a livello mondiale, in particolare in Francia. Una ricerca tramite Censys riporta oltre [3.200 risultati](https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=EXCLUDE&q=services.http.response.body%3A+%22How+to+Restore+Your+Files%22+and+services.http.response.html_title%3A%22How+to+Restore+Your+Files%22), di cui **oltre un terzo si trovano appunto in territorio francese**.

Seguono poi gli Stati Uniti, la Germania e il Canada, mentre **l’Italia è molto più indietro**: sempre stando alla rilevazione Censys, i sistemi coinvolti nel nostro Paese sono 20 contro 1.213 individuati in Francia.

Questa ricerca naturalmente potrebbe non individuare tutti i sistemi coinvolti, ma dalle informazioni disponibili **non sembra che l’attacco abbia colpito su vasta scala nel nostro Paese, e neppure che abbia avuto l’Italia come bersaglio principale**.

Quello che emerge ancora una volta da questa vicenda, al di là degli aspetti sensazionalistici, è un’**attenzione insufficiente alla sicurezza e all’implementazione di buone pratiche**; migliaia di sistemi violati sfruttando vulnerabilità note e risolte da quasi due anni indicano che c’è ancora molto lavoro da fare.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Censys](https://www.securityinfo.it/tag/censys/), [ESXi](https://www.securityinfo.it/tag/esxi/), [ESXiArgs](https://www.securityinfo.it/tag/esxiargs/), [SLP](https://www.securityinfo.it/tag/slp/), [VMware](https://www.securityinfo.it/tag/vmware/)

[File OneNote per distribuire malware: individuate decine di campagne attive](https://www.securityinfo.it/2023/02/06/file-onenote-campagne-malware/)
[Vulnerabilità critica minaccia migliaia di Nas QNAP in Italia](https://www.securityinfo.it/2023/02/03/vulnerabilita-critica-minaccia-migliaia-di-nas-qnap-in-italia/)

---

![](https://secure.gravatar.com/avatar/9ba6108fae91c2be66a7ef45ac2db49a?s=90&d=mm&r=g)

##### [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/)

##### Articoli correlati

* [![I ransomware contro le appliance ESXi sfruttano il tunneling SSH per la persistenza](https://www.securityinfo.it/wp-content/uploads/2025/01/ransomware-2321110_1920-120x85.jpg)](https://www.securityinfo.it/2025/01/28/i-ransomware-contro-le-appliance-esxi-sfruttano-il-tunneling-ssh-per-la-persistenza/ "I ransomware contro le appliance ESXi sfruttano il tunneling SSH per la persistenza")

  [I ransomware contro le appliance ESXi...](https://www.securityinfo.it/2025/01/28/i-ransomware-contro-le-appliance-esxi-sfruttano-il-tunneling-ssh-per-la-persistenza/ "Permanent link to I ransomware contro le appliance ESXi sfruttano il tunneling SSH per la persistenza")

  Gen 28, 2025  [0](https://www.securityinfo.it/2025/01/28/i-ransomware-contro-le-appliance-esxi-sfruttano-il-tunneling-ssh-per-la-persistenza/#respond)
* [![Scoperta una variante Linux del ransomware Play che colpisce gli ambienti ESXi](https://www.securityinfo.it/wp-content/uploads/2024/07/ransomware-2320793_1920-120x85.jpg)](https://www.securityinfo.it/2024/07/22/scoperta-una-variante-linux-del-ransomware-play-che-colpisce-gli-ambienti-esxi/ "Scoperta una variante Linux del ransomware Play che colpisce gli ambienti ESXi")

  [Scoperta una variante Linux del...](https://www.securityinfo.it/2024/07/22/scoperta-una-variante-linux-del-ransomwa...