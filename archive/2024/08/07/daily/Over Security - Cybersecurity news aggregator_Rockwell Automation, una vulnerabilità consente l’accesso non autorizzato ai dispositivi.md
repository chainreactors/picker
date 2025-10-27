---
title: Rockwell Automation, una vulnerabilità consente l’accesso non autorizzato ai dispositivi
url: https://www.securityinfo.it/2024/08/06/rockwell-automation-vulnerabilita-accesso-non-autorizzato/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-07
fetch_date: 2025-10-06T18:05:22.386187
---

# Rockwell Automation, una vulnerabilità consente l’accesso non autorizzato ai dispositivi

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

## Rockwell Automation, una vulnerabilità consente l’accesso non autorizzato ai dispositivi

Ago 06, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2024/08/06/rockwell-automation-vulnerabilita-accesso-non-autorizzato/#respond)

---

I ricercatori di Team82 di Claroty [hanno individuato](https://claroty.com/team82/research/bypassing-rockwell-automation-logix-controllers-local-chassis-security-protection) una **vulnerabilità nei dispositivi Rockwell Automation** che consente a un attaccante di ottenere **accesso non autorizzato** ed eseguire comandi.

Il bug, tracciato come CVE-2024-6242, colpisce i dispositivi della serie **ControlLogix 1756**, pensati per supportare le applicazioni di automazione industriale ad elevate performance che richiedono alta scalabilità. Questi device utilizzano il **protocollo CIP** (Common Industrial Protocol) per la comunicazione tra dispositivi, come sensori, attuatori e altri controller.

![Rockwell Automation vulnerabilità](https://www.securityinfo.it/wp-content/uploads/2024/08/pattern-3232784_1920.jpg)

Pixabay

I ricercatori spiegano che la vulnerabilità colpisce una feature di sicurezza chiamata “trusted slot” che è pensata per negare le comunicazioni tra moduli non riconosciuti come legittimi. “*La funzione trusted-slot aiuta a stabilire e ad applicare i criteri di sicurezza all’interno dello chassis ControlLogix. **Garantisce che solo gli slot autorizzati possano comunicare tra loro**, proteggendo dall’accesso non autorizzato e da potenziali manomissioni*” spiega il team di sicurezza.

I singoli moduli (o slot) sono collegati e comunicano tramite il **backplane**, un circuito stampato che consente al controller e ai moduli di I/O di scambiarsi informazioni. Per via di questo collegamento, i ricercatori sono riusciti a **generare un pacchetto CIP e instradarlo verso uno slot legittimo prima che raggiungesse la CPU.**

Sfruttando il bug, un attaccante è in grado di **bypassare il controllo di sicurezza** e comunicare tramite il protocollo CIP, inviando comandi alla CPU anche da una rete considerata non sicura. Un attaccante può modificare la configurazione del dispositivo a suo piacimento ed **eseguire comandi di download, upload e aggiornamento sulla CPU del dispositivo.**

Rockwell Automation ha rilasciato un **[fix](https://www.rockwellautomation.com/en-us/trust-center/security-advisories/advisory.SD1682.html) per la vulnerabilità** e ha invitato gli utenti ad aggiornare il prima possibile i dispositivi vulnerabili. L’analisi della compagnia ha rivelato che il bug non colpisce solo i device ControlLogix, ma anche i GuardLogic 5580 e in generale tutti i Moduli 1756 ControlLogix I/O. Nel caso non sia possibile aggiornare il firmware, è possibile limitare l’esecuzione di comandi CIP sui controller impostando lo switch in posizione RUN.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [comunicazioni insicure](https://www.securityinfo.it/tag/comunicazioni-insicure/), [CPU](https://www.securityinfo.it/tag/cpu/), [dispositivi di automazione industriale](https://www.securityinfo.it/tag/dispositivi-di-automazione-industriale/), [protocollo CIP](https://www.securityinfo.it/tag/protocollo-cip/), [Rockwell Automation](https://www.securityinfo.it/tag/rockwell-automation/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[Hacker cinesi hanno compromesso un ISP per distribuire malware](https://www.securityinfo.it/2024/08/07/hacker-cinesi-hanno-compromesso-un-isp-per-distribuire-malware/)
[Nathan Howe: "ecco come Zscaler protegge i dispositivi IoT/OT"](https://www.securityinfo.it/2024/08/06/nathan-howe-ecco-come-zscaler-protegge-i-dispositivi-iot-ot/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_d4x8rid4x8rid4x8-120x85.png)](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  [Firewall Cisco sotto attacco: una nuova...](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Permanent link to Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  Set 29, 2025  [0](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/#respond)
* [![Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.](https://www.securityinfo.it/wp-content/uploads/2025/09/ai-generated-9053184_1920-120x85.jpg)](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/ "Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.")

  [Attaccanti sfruttano un bug di...](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/ "Permanent link to Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.")

  Set 24, 2025  [0](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare...