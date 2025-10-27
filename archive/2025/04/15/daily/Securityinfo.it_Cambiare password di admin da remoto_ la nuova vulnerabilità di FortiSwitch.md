---
title: Cambiare password di admin da remoto: la nuova vulnerabilità di FortiSwitch
url: https://www.securityinfo.it/2025/04/14/cambiare-password-di-admin-da-remoto-la-nuova-vulnerabilita-di-fortiswitch/?utm_source=rss&utm_medium=rss&utm_campaign=cambiare-password-di-admin-da-remoto-la-nuova-vulnerabilita-di-fortiswitch
source: Securityinfo.it
date: 2025-04-15
fetch_date: 2025-10-06T22:07:38.949856
---

# Cambiare password di admin da remoto: la nuova vulnerabilità di FortiSwitch

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

## Cambiare password di admin da remoto: la nuova vulnerabilità di FortiSwitch

Apr 14, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [Prodotto](https://www.securityinfo.it/category/news/prodotto-news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/04/14/cambiare-password-di-admin-da-remoto-la-nuova-vulnerabilita-di-fortiswitch/#respond)

---

La settimana scorsa **Fortinet** [ha rilasciato](https://www.fortiguard.com/psirt/FG-IR-24-435) un fix per una vulnerabilità critica di **FortiSwitch GUI** che consente a un attaccante non autenticato di **modificare la password di amministratore da remoto.**

Secondo quanto condiviso dalla compagnia, un attaccante può sfruttare il bug inviando una richiesta creata ad hoc all’endpoint `set_password`, **senza alcuna interazione da parte degli utenti.**

Secondo un’analisi di Censys, al momento **non ci sono evidenze di eventuali exploit attivi**. La compagnia ha sottolineato che, in caso di successo dell’attacco, un utente remoto è in grado di prendere il controllo del dispositivo e potenzialmente compromettere l’intera infrastruttura gestita da FortiSwitch. Al momento non sono disponibili dettagli tecnici sull’exploit.

![FortiSwitch](https://www.securityinfo.it/wp-content/uploads/2025/04/118.jpg)

Censys riporta inoltre che attualmente ha individuato 864 istanze FortiSwitch attive online, anche se non è chiaro quante di queste siano vulnerabili.

Come riportato da [BleepingComputer](https://www.bleepingcomputer.com/news/security/critical-fortiswitch-flaw-lets-hackers-change-admin-passwords-remotely/), l’advisory per il bug di FortiSwitch non è l’unico pubblicato dalla compagnia negli ultimi tempi: di recente Fortinet ha risolto un bug di OS command injection presente in FortiOS, FortiProxy, FortiManager, FortiAnalyzer, FortiVoice e FortiWeb.

Considerata la loro diffusione, i dispositivi Fortinet sono un **obiettivo molto interessante per gli attaccanti**, tanto che in passato le vulnerabilità individuate [sono state sfruttate](https://www.securityinfo.it/2024/10/14/cisa-aggiunge-tre-vulnerabilita-di-fortinet-e-ivanti-alla-lista-di-bug-sfruttati-dagli-attaccanti/) più volte dai cybercriminali, spesso anche prima che venissero individuate dai ricercatori di sicurezza.

Il bug colpisce le versioni di FortiSwitch 7.6.0, dalla 7.4.0 alla 7.4.4, dalla 7.2.0 alla 7.2.8, dalla 7.0.0 alla 7.0.10 e dalla 6.4.0 alla 6.4.14. Visto l’impatto della vulnerabilità, è indispensabile **aggiornare le istanze vulnerabili il prima possibile.**Il fix è disponibile nelle versioni 7.6.1, 7.4.5, 7.2.9, 7.0.11 e 6.4.15.

Se non si è in grado di applicare il fix nel giro di poco, Fortinet consiglia come workaround di **disabilitare gli accessi HTTP/HTTPS** dalle interfacce di amministrazione e restringere l’accesso solo agli host conosciuti.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [controllo remoto](https://www.securityinfo.it/tag/controllo-remoto/), [fortinet](https://www.securityinfo.it/tag/fortinet/), [FortiSwitch](https://www.securityinfo.it/tag/fortiswitch/), [password amministratore](https://www.securityinfo.it/tag/password-amministratore/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[Slopsquatting: quando l'IA consiglia pacchetti che non esistono](https://www.securityinfo.it/2025/04/15/slopsquatting-quando-lia-consiglia-pacchetti-che-non-esistono/)
[CERT-AGID 5-11 APRILE: MintLoader e AsyncRAT protagonisti di due campagne malspam](https://www.securityinfo.it/2025/04/14/cert-agid-5-11-aprile-mintloader-asyncrat-malspam/)

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
* [![Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-1-120x85.jpg)](https://www....