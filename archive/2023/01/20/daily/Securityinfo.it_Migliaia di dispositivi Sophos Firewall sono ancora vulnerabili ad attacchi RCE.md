---
title: Migliaia di dispositivi Sophos Firewall sono ancora vulnerabili ad attacchi RCE
url: https://www.securityinfo.it/2023/01/19/sophos-firewall-vulnerabili-rce/?utm_source=rss&utm_medium=rss&utm_campaign=sophos-firewall-vulnerabili-rce
source: Securityinfo.it
date: 2023-01-20
fetch_date: 2025-10-04T04:25:36.285458
---

# Migliaia di dispositivi Sophos Firewall sono ancora vulnerabili ad attacchi RCE

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

## Migliaia di dispositivi Sophos Firewall sono ancora vulnerabili ad attacchi RCE

Gen 19, 2023  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2023/01/19/sophos-firewall-vulnerabili-rce/#respond)

---

Lo scorso settembre Sophos aveva individuato e corretto una vulnerabilità che colpiva le versioni 19.0.1 e minori di Firewall; oggi **ci sono ancora più di 4.000 dispositivi attivi in rete che non hanno ricevuto gli aggiornamenti necessari e che risultano ancora vulnerabili.**Lo ha riportato Jacob Baines, ricercatore di sicurezza di VulnCheck, che ha analizzato lo stato dei dispositivi in rete.

La falla, identificata come CVE-2022-3236, **colpisce lo User Portal e la console di web admin del componente, e permette a un attaccante di eseguire codice remoto.** Resa nota diversi mesi fa, molti cybercriminali l’avevano sfruttata per colpire i dispositivi vulnerabili connessi alla rete.

![Sophos Firewall](https://www.securityinfo.it/wp-content/uploads/2023/01/analytics-3088958_1280.jpg)

La vulnerabilità è causata da una validazione errata di alcune chiavi JSON destinate all’endpoint Controller, utilizzato da User Portal e Web Admin Console. Per sfruttare la falla un attaccante poteva quindi creare una richiesta ad hoc per ottenere il controllo del server ed eseguire codice remoto coi privilegi di root.

## Sophos Firewall: migliaia di dispositivi ancora vulnerabili

Nonostante Sophos abbia rilasciato la patch dopo pochi giorni, **ci sono migliaia di dispositivi che non sono stati ancora aggiornati**. L’azienda aveva invitato gli amministratori di rete a procedere subito con l’installazione della patch o di aggiornare Firewall alle ultime versioni.

Baines rassicura sulla pericolosità della falla: le impostazioni di sicurezza del componente sono riuscite a bloccare la maggior parte degli attacchi e limitare le conseguenze. Inoltre, **Baines esclude compromissioni di massa per via della presenza di un CAPTCHA richiesto durante le fase di autenticazione.** La vulnerabilità infatti può essere sfruttata solo dopo la risoluzione del test, e la maggior parte degli attaccanti trova molta difficoltà nel riuscirci.

![Sophos Firewall](https://www.securityinfo.it/wp-content/uploads/2023/01/cyber-security-3374252_1280.jpg)

**Ciò non esclude però la necessità di aggiornare i dispositivi e applicare le patch ufficiali rilasciate da Sophos**; la stessa azienda ha comunicato che alcune organizzazioni sono state colpite da cybercriminali che hanno sfruttato questa vulnerabilità. In occasione dell’articolo di Baines, **Sophos ha ricordato agli utenti che usano ancora versioni obsolete di aggiornare [Firewall](https://www.securityinfo.it/2022/11/24/firewall-sophos-xstream-edge-computing/) alla versione più recente.**

Pubblichiamo la nota inviataci da Sophos sul report del ricercatore:

*“Sophos ha provveduto immediatamente a risolvere questo problema con un hotfix automatico inviato nel settembre 2022. Abbiamo inoltre avvisato gli utenti che non ricevono hotfix automatici di applicare l’aggiornamento autonomamente.  Il restante 6% delle versioni che si interfacciano con Internet, secondo le stime di Baines nel suo articolo, utilizza versioni vecchie e non supportate del software. Questa è una buona occasione per ricordare a questi utenti, così come a tutti gli utenti di qualsiasi tipo di software obsoleto, di seguire le migliori pratiche di sicurezza e di aggiornare alla versione più recente disponibile, come Sophos fa regolarmente con i suoi clienti”.*

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [esecuzione remota codice](https://www.securityinfo.it/tag/esecuzione-remota-codice/), [firewall](https://www.securityinfo.it/tag/firewall/), [RCE](https://www.securityinfo.it/tag/rce/), [remote code execution](https://www.securityinfo.it/tag/remote-code-execution/), [Sophos](https://www.securityinfo.it/tag/sophos/), [sophos firewall](https://www.securityinfo.it/tag/sophos-firewall/)

[Le tendenze della cyber security per il 2023](https://www.securityinfo.it/2023/01/19/le-tendenze-della-cyber-security-per-il-2023/)
[Come proteggere le università dai cyber attacchi](https://www.securityinfo.it/2023/01/18/universita-cyber-attacchi-sicurezza/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità](https://www.securityinfo.it/wp-content/uploads/2025/10/Gemini_Generated_Image_eubydneubydneuby-120x85.png)](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/ "Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità")

  [Ricerca FireMon: il 60% dei firewall...](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/ "Permanent link to Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità")

  Ott 01, 2025  [0](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/#respond)
* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_d4x8rid4x8rid4x8-120x85.png)](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Firewall Cisco sotto at...