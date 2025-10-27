---
title: Microsoft rilascia patch per 67 bug, di cui uno già sfruttato
url: https://www.securityinfo.it/2025/06/11/microsoft-rilascia-patch-per-67-bug-di-cui-uno-gia-sfruttato/?utm_source=rss&utm_medium=rss&utm_campaign=microsoft-rilascia-patch-per-67-bug-di-cui-uno-gia-sfruttato
source: Securityinfo.it
date: 2025-06-12
fetch_date: 2025-10-06T22:54:25.470527
---

# Microsoft rilascia patch per 67 bug, di cui uno già sfruttato

Aggiornamenti recenti Ottobre 6th, 2025 3:00 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Microsoft Sentinel: arriva l’era degli agenti AI e della difesa predittiva](https://www.securityinfo.it/2025/10/06/microsoft-sentinel-arriva-lera-degli-agenti-ai-e-della-difesa-predittiva/)
* [CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)
* [Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)

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

## Microsoft rilascia patch per 67 bug, di cui uno già sfruttato

Giu 11, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/06/11/microsoft-rilascia-patch-per-67-bug-di-cui-uno-gia-sfruttato/#respond)

---

Nell’aggiornamento di sicurezza di giugno **Microsoft** [ha incluso](https://msrc.microsoft.com/update-guide/releaseNote/2025-Jun) le patch per ben **67 bug**, di cui uno già sfruttato dagli attaccanti.

La vulnerabilità in questione colpisce **WEBDAV** (Web Distributed Authoring and Versioning), un protocollo che estende HTTP per definire in che modo le funzioni di file vengono eseguite tramite HTTP. Il bug consente a un attaccante di **eseguire codice da remoto** e, sebbene sia necessaria l’interazione utente per sfruttarla, Microsoft ha confermato che la difficoltà dell’attacco è molto bassa.

![Microsoft vulnerabilità](https://www.securityinfo.it/wp-content/uploads/2025/06/Gemini_Generated_Image_xaqqtnxaqqtnxaqq-scaled.jpg)

A scoprire la campagna che sfruttato il bug sono stati i ricercatori di **Check Point Research**. In un [post](https://research.checkpoint.com/2025/stealth-falcon-zero-day/) sul blog ufficiale, il team ha spiegato che gli attaccanti hanno usato un file .url tramite una mail di phishing per sfruttare la vulnerabilità ed eseguire un malware da un server WEBDAV controllato da essi.

Dietro l’attacco ci sarebbe il gruppo APT **Stealth Falcon**, conosciuto anche come FruityArmor. La gang ha distribuito il già noto **Horus Agent**, una backdoor in grado di raccogliere informazioni sul dispositivo e sui processi in esecuzione, oltre che di scaricare file dal server C2. Obiettivo dell’attacco è stata una compagnia turca del settore della difesa. Secondo i ricercatori di Check Point, il gruppo ha affinato le proprie tecniche per rendere ancora più elusivi i propri attacchi, complicando le analisi di sicurezza.

Degli altri bug Microsoft, 11 sono stati classificati come “critici” e 56 come “importanti”. Uno dei bug più gravi (9.3/10) è quello che colpisce **M365 Copilot**: si tratta di una vulnerabilità di **command injection** che consente a un attaccante di ottenere informazioni riservate.

L’altra vulnerabilità critica (9.8/10) colpisce **Power Automate** e permette a un utente non autorizzato di **elevare i propri** **privilegi**e compromettere le applicazioni e i servizi connessi.

Tra le vulnerabilità risolte dalla [compagnia](https://www.securityinfo.it/2025/06/03/microsoft-e-crowdstrike-collaborano-per-allineare-le-tassonomie-degli-attaccanti/) **ce ne sono nove considerate ad alto rischio di sfruttamento.** Quattro di queste colpiscono Office e una, in particolare Word. Le altre sono invece presenti nel Windows Common Log File System Driver, in Windows Installer, in Windows Netlogon e in Windows SDK.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [backdoor](https://www.securityinfo.it/tag/backdoor/), [command injection](https://www.securityinfo.it/tag/command-injection/), [esecuzione codice remoto](https://www.securityinfo.it/tag/esecuzione-codice-remoto/), [Microsoft](https://www.securityinfo.it/tag/microsoft/), [Stealth Falcon](https://www.securityinfo.it/tag/stealth-falcon/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/), [webdav](https://www.securityinfo.it/tag/webdav/)

[Smartwatch e attacchi acustici: nuova minaccia alle reti isolate](https://www.securityinfo.it/2025/06/12/smartwatch-e-attacchi-acustici-nuova-minaccia-alle-reti-isolate/)
[Un bug di Google consentiva di scoprire il numero di telefono degli utenti in pochi minuti](https://www.securityinfo.it/2025/06/10/un-bug-di-google-consentiva-di-scoprire-il-numero-di-telefono-degli-utenti-in-pochi-minuti/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_d4x8rid4x8rid4x8-120x85.png)](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  [Firewall Cisco sotto attacco: una nuova...](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Permanent link to Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  Set 29, 2025  [0](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/#respond)
* [![Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.](https://www.securityinfo.it/wp-content/uploads/2025/09/ai-generated-9053184_1920-120x85.jpg)](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/ "Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.")

  [Attaccanti sfruttano un bug di...](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/ "Permanent link to Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.")

  Set 24, 2025  [0](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-g...