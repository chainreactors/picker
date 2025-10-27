---
title: Daggerfly sta usando una nuova versione di Macma, una backdoor per macOS
url: https://www.securityinfo.it/2024/07/25/daggerfly-sta-usando-una-nuova-versione-di-macma-una-backdoor-per-macos/?utm_source=rss&utm_medium=rss&utm_campaign=daggerfly-sta-usando-una-nuova-versione-di-macma-una-backdoor-per-macos
source: Securityinfo.it
date: 2024-07-26
fetch_date: 2025-10-06T17:44:32.732021
---

# Daggerfly sta usando una nuova versione di Macma, una backdoor per macOS

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

## Daggerfly sta usando una nuova versione di Macma, una backdoor per macOS

Lug 25, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2024/07/25/daggerfly-sta-usando-una-nuova-versione-di-macma-una-backdoor-per-macos/#respond)

---

**Daggerfly**, gruppo di cybercriminali cinesi conosciuto anche come Evasive Panda e Bronze Highland, ha di recente aggiornato il proprio arsenale di strumenti di attacco. Tra le novità c’è una nuova famiglia di malware basata su **MgBot**, il framework modulare di malware del gruppo, e una nuova versione di **Macma**, una **backdoor per macOS.**

Finora i ricercatori di sicurezza non erano riusciti ad associare Macma a uno specifico gruppo hacker; **è stato il [Threat Hunter Team di Symantec](https://symantec-enterprise-blogs.security.com/threat-intelligence/daggerfly-espionage-updated-toolset) a scoprire il legame tra Daggerfly e Macma** analizzando una serie di attacchi che hanno colpito organizzazioni a Taiwan e una NGO statunitense con sede in Cina.

![Macma backdoor](https://www.securityinfo.it/wp-content/uploads/2024/07/hacker-7192873_1920-1.jpg)

Pixabay

Macma è una **backdoor per macOS** documentata per la prima volta nel 2021, ma sembra che sia attiva in realtà almeno dal 2019. La backdoor è stata utilizzata inizialmente in una serie di **attacchi *watering holes*** contro siti web di Hong Kong; questo tipo di attacchi mira a colpire i dispositivi di un gruppo specifico di utenti, di solito appartenenti a un determinato settore o a un’azienda, infettando con diversi malware i siti web che visitano più spesso.

Nel caso di Macma, gli attacchi sfruttavano exploit per iOS e macOS; in particolare, per i dispositivi macOS gli attaccanti usavano la CVE-2021-30869, una vulnerabilità di privilege escalation che gli permetteva di installare la backdoor sui sistemi.

Macma si presenta come una **backdoor modulare** in grado di eseguire comandi sul dispositivo, catturare istantanee dello schermo, effettuare keylogging, registrare audio e caricare e scaricare file.

Gli ultimi aggiornamenti della backdoor incrementano le sue funzionalità tramite nuovi moduli. Il modulo principale presenta ora una nuova logica per ottenere la lista di file del dispositivo, parametrizzazione e logging di debug addizionali e un nuovo file legato alla feature “autoScreenCaptureInfo”.

Secondo il Threat Hunter Team di Symantec, **ci sono indizi chiari che legano Macma a Daggerfly**: la backdoor si collega a un server C2 già utilizzato da un dropper di MgBot; inoltre, Macma e il malware di Daggerfly contengono codice che proviene dalla stessa libreria condivisa.

![](https://www.securityinfo.it/wp-content/uploads/2024/06/hacker-6512174_1920.jpg)

## Non solo Macma: Daggerfly usa una nuova backdoor

Il team di Symantec ha scoperto che, tra le novità dell’arsenale di Daggerfly c’è **un’altra backdoor oltre a Macma**: in questo caso è una backdoor per Windows, la Trojan.Suzasfk conosciuta anche come **Nightdoor**. Questa backdoor ha fatto la sua apparizione più di recente (lo scorso marzo), quando è stata usata insieme a MgBot. Anche in questo caso, la libreria usata per sviluppare il malware è la stessa di MgBot e Macma.

Nightdoor è una backdoor multi-stage **in grado di usare TCP e OneDrive** per la comunicazione con gli attaccanti. A giudicare dal codice individuato da Symantec, la funzionalità per connettersi a OneDrive è in sviluppo o potrebbe essere presente in altre varianti del malware. La backdoor può inoltre individuare macchine virtuali, sandbox ed effettuare l’analisi dell’ambiente in cui si trova.

Il Threat Hunter Team di Symantec sottolinea che Daggerfly è un gruppo molto capace, in grado di sviluppare velocemente nuovi tool per colpire diverse piattaforme, con funzionalità sempre nuove. **“*Daggerfly sembra essere in grado di reagire allo smascheramento aggiornando rapidamente il suo set di strumenti per continuare le sue attività di spionaggio con interruzioni minime*“** conclude il team.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [backdoor](https://www.securityinfo.it/tag/backdoor/), [Daggerfly](https://www.securityinfo.it/tag/daggerfly/), [Macma](https://www.securityinfo.it/tag/macma/), [macOS](https://www.securityinfo.it/tag/macos/), [Nightdoor](https://www.securityinfo.it/tag/nightdoor/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[Scoperta EvilVideo, una vulnerabilità zero-day di Telegram per Android](https://www.securityinfo.it/2024/07/25/scoperto-evilvideo-una-vulnerabilita-zero-day-di-telegram-per-android/)
[Qual è la causa dei disservizi di venerdì scorso? Ce la rivela CrowdStrike](https://www.securityinfo.it/2024/07/24/qual-e-la-causa-dei-disservizi-di-venerdi-scorso-ce-la-spiega-crowdstrike/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_d4x8rid4x8rid4x8-120x85.png)](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  [Firewall Cisco sotto attacco: una nuova...](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-u...