---
title: Asana: un bug nell’integrazione AI esponeva i dati aziendali
url: https://www.securityinfo.it/2025/06/19/asana-un-bug-nellintegrazione-ai-espone-i-dati-aziendali-al-rischio/
source: Over Security - Cybersecurity news aggregator
date: 2025-06-20
fetch_date: 2025-10-06T22:53:59.281216
---

# Asana: un bug nell’integrazione AI esponeva i dati aziendali

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

## Asana: un bug nell’integrazione AI esponeva i dati aziendali

Giu 19, 2025  [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo_security/ "Articoli scritti da Giancarlo Calzetta")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/06/19/asana-un-bug-nellintegrazione-ai-espone-i-dati-aziendali-al-rischio/#respond)

---

Abbiamo appena parlato della [prima vulnerabilità mai rilevata a spese di un sistema AI in produzione](https://www.securityinfo.it/2025/06/13/echoleak-e-arrivata-la-prima-vulnerabilita-zero-clic-per-le-ia-microsoft-365-copilot/) ed ecco che arriva un altro caso. Un’integrazione sperimentale basata sull’intelligenza artificiale, infati, ha costretto Asana a **disattivare per quasi due settimane** il suo server MCP (Model Context Protocol), dopo aver rilevato una vulnerabilità che avrebbe potuto esporre i dati di un’organizzazione ad altri utenti della piattaforma.

![](https://www.securityinfo.it/wp-content/uploads/2025/06/AI_Vulnerabilità_20-giu-2025CG-1024x683.png)

L’MCP è un protocollo open source introdotto da Anthropic nel 2024 con l’obiettivo di collegare agenti AI e modelli linguistici a fonti esterne, come database e strumenti di messaggistica. La tecnologia consente a modelli differenti di comunicare e interagire tra loro, aprendo nuovi scenari per l’automazione intelligente nelle piattaforme enterprise. Asana, noto fornitore di software per la collaborazione aziendale, ha abilitato il proprio server MCP il 1° maggio, permettendo agli utenti di **eseguire query in linguaggio naturale** sui dati aziendali e integrarsi con altre app AI.

Tuttavia, la sperimentazione ha avuto una battuta d’arresto: il 4 giugno, Asana ha rilevato un bug nel server MCP che, secondo una comunicazione inviata ai clienti, avrebbe potuto potenzialmente esporre informazioni del vostro dominio Asana ad altri utenti MCP. L’incidente ha portato alla **disattivazione del servizio dal 5 al 17 giugno**, in attesa di una correzione.

La falla, i cui dettagli tecnici non sono stati divulgati, sembra legata a un difetto nei meccanismi di isolamento dei tenant, un elemento cruciale quando si lavora con modelli di intelligenza artificiale in ambienti multi-tenant. Sebbene Asana affermi di non avere prove di accessi non autorizzati o sfruttamenti attivi, l’episodio conferma che **qualsiasi sistema messo in produzione, soprattutto se di recente implementazione, va tenuto sotto stretto controllo.**

Nella nota pubblicata a seguito dell’incidente, Asana ha dichiarato di aver **resettato tutte le connessioni al server MCP**, chiedendo agli utenti di riconnettere manualmente le proprie istanze. La società ha inoltre promesso un report completo sull’accaduto, ancora in fase di redazione, e ha già contattato direttamente i clienti potenzialmente coinvolti.

L’integrazione AI, quindi, inizia a presentare il conto: man mano che le installazioni diventeranno più numerose e sempre più ricercatori cominceranno a testarne la robustezza, **salteranno fuori vulnerabilità e lacune** che bisognerà sistemare. Un tema già visto con altre tecnologie e che nonostante la maggior consapevolezza e maturazione del mercato risulta ancora ineluttabile.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [AI](https://www.securityinfo.it/tag/ai/), [AI generativa](https://www.securityinfo.it/tag/ai-generativa/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/), [Zero-day](https://www.securityinfo.it/tag/zero-day/)

[Anche Viasat vittima del cyberspionaggio di Salt Typhoon](https://www.securityinfo.it/2025/06/20/anche-viasat-vittima-del-cyberspionaggio-di-salt-typhoon/)
[Deepfake per distribuire malware su macOS: la nuova minaccia nord-coreana](https://www.securityinfo.it/2025/06/19/deepfake-per-distribuire-malware-su-macos-la-nuova-minaccia-nord-coreana/)

---

![](https://secure.gravatar.com/avatar/d6a6ecdad542d883704003e541413ca8?s=90&d=mm&r=g)

##### [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo_security/)

##### Articoli correlati

* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_d4x8rid4x8rid4x8-120x85.png)](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  [Firewall Cisco sotto attacco: una nuova...](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Permanent link to Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  Set 29, 2025  [0](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/#respond)
* [![Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.](https://www.securityinfo.it/wp-content/uploads/2025/09/ai-generated-9053184_1920-120x85.jpg)](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/ "Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.")

  [Attaccanti sfruttano un bug di...](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/ "Permanent link to Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.")

  Set 24, 2025  [0](https://www.securityinfo.it/2025/09/24/...