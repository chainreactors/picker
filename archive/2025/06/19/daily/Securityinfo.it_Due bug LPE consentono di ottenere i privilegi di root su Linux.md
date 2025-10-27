---
title: Due bug LPE consentono di ottenere i privilegi di root su Linux
url: https://www.securityinfo.it/2025/06/18/due-bug-lpe-consentono-di-ottenere-i-privilegi-di-root-su-linux/?utm_source=rss&utm_medium=rss&utm_campaign=due-bug-lpe-consentono-di-ottenere-i-privilegi-di-root-su-linux
source: Securityinfo.it
date: 2025-06-19
fetch_date: 2025-10-06T22:54:49.863469
---

# Due bug LPE consentono di ottenere i privilegi di root su Linux

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

## Due bug LPE consentono di ottenere i privilegi di root su Linux

Giu 18, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/06/18/due-bug-lpe-consentono-di-ottenere-i-privilegi-di-root-su-linux/#respond)

---

I ricercatori di Qualys Threat Research Unit [hanno individuato](https://blog.qualys.com/vulnerabilities-threat-research/2025/06/17/qualys-tru-uncovers-chained-lpe-suse-15-pam-to-full-root-via-libblockdev-udisks) **due bug di escalation dei privilegi** locale (LPE) che consentono a un attaccante di **ottenere i privilegi di root sui sistemi Linux.**

La prima vulnerabilità, tracciata come CVE-2025-6018, colpisce la configurazione PAM (Pluggable Authentication Modules) di **openSUSE Leap 15 e SUSE Linux Enterprise 15**. Sfruttando questo bug, un utente malintenzionato senza particolari privilegi può **elevare la propria operatività a “allow\_active” ed eseguire azioni Polkit anche da remoto.**

![bug Linux](https://www.securityinfo.it/wp-content/uploads/2025/06/hacker-2300772_1920.jpg)

La seconda vulnerabilità, la CVE-2025-6019, colpisce invece **libblockdev**, una libreria che permette di manipolare i dispositivi a blocchi. Questo bug è sfruttabile usando il demone udisks presente di default in molte [distribuzioni](https://www.securityinfo.it/2025/06/17/kali-linux-2025-2-la-nuova-versione-ha-anche-un-toolkit-per-lhacking-delle-auto/) Linux; anche in questo caso, il bug permette all’attaccante di **ottenere privilegi di root tramite “allow\_active”.**

I due bug sono particolarmente significativi perché mettono a rischio praticamente ogni distribuzione Linux. “***Un attaccante può concatenare queste vulnerabilità per ottenere compromettere immediatamente la root col minimo sforzo.** Data l’ubiquità degli udisk e la semplicità dell’exploit, le organizzazioni devono considerare questo come un rischio critico e universale e applicare le patch senza aspettare*” spiegano i ricercatori di Qualys.

Grazie a queste due vulnerabilità, un attaccante che dispone di una sessione GUI o SSH può facilmente prendere il controllo del sistema, passando da essere un utente senza privilegi ad admin. Ottenuti i permessi di root, un attaccante può di fatto eseguire qualsiasi altro attacco o spostarsi su altri sistemi della stessa rete.

Per ridurre il rischio di sfruttamento, il team di Qualys consiglia di **mantenere aggiornati i sistemi in rete** e rendere più stringenti le regole Polkit. Nel dettaglio, i ricercatori consigliano di modificare l’impostazione “allow\_active” della regola `org.freedesktop.udisks2.modify-device` da “yes” a “auth\_admin”, in modo che sia necessaria l’approvazione da parte dell’amministratore per eseguire l’azione. “*Questa ampia strategia aiuta a contenere l’accesso iniziale e a proteggere l’intera rete*“.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [bug LPE](https://www.securityinfo.it/tag/bug-lpe/), [elevation dei privilegi](https://www.securityinfo.it/tag/elevation-dei-privilegi/), [Linux](https://www.securityinfo.it/tag/linux/), [permessi di root](https://www.securityinfo.it/tag/permessi-di-root/), [Polkit](https://www.securityinfo.it/tag/polkit/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[Deepfake per distribuire malware su macOS: la nuova minaccia nord-coreana](https://www.securityinfo.it/2025/06/19/deepfake-per-distribuire-malware-su-macos-la-nuova-minaccia-nord-coreana/)
[Kali Linux 2025.2, la nuova versione ha anche un toolkit per l'hacking delle auto](https://www.securityinfo.it/2025/06/17/kali-linux-2025-2-la-nuova-versione-ha-anche-un-toolkit-per-lhacking-delle-auto/)

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
* [![Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali](https:...