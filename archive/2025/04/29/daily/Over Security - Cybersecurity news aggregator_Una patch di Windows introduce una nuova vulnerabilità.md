---
title: Una patch di Windows introduce una nuova vulnerabilità
url: https://www.securityinfo.it/2025/04/28/una-patch-di-windows-introduce-una-nuova-vulnerabilita/
source: Over Security - Cybersecurity news aggregator
date: 2025-04-29
fetch_date: 2025-10-06T22:08:40.070566
---

# Una patch di Windows introduce una nuova vulnerabilità

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

## Una patch di Windows introduce una nuova vulnerabilità

Apr 28, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/04/28/una-patch-di-windows-introduce-una-nuova-vulnerabilita/#respond)

---

Una delle ultime patch di **Windows**, rilasciata per risolvere un bug di symlink, **ha in realtà introdotto una nuova vulnerabilità** che permette a un attaccante di bloccare l’installazione di futuri aggiornamenti di sicurezza.

Come [spiega](https://doublepulsar.com/microsofts-patch-for-cve-2025-21204-symlink-vulnerability-introduces-another-symlink-vulnerability-9ea085537741) Kevin Beaumont, ricercatore di sicurezza che ha individuato il problema, l’aggiornamento di Windows di aprile ha risolto la vulnerabilità CVE-2025-21204, un bug che permette agli utenti di sfruttare i link simbolici (symlink). L’aggiornamento prevede la creazione di una nuova cartella, **c:\inetpub**, che Microsoft [ha confermato](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21204) essere parte della soluzione introdotto. “*Questa cartella non deve essere cancellata indipendentemente dal fatto che Internet Information Services (IIS) sia attivo sul dispositivo*” ha spiegato la compagnia.

![windows vulnerabilità](https://www.securityinfo.it/wp-content/uploads/2025/04/cyber-security-1923446_1920.png)

Beaumont ha però scoperto che questo fix introduce una **vulnerabilità di denial of service** che permette anche agli utenti non amministratori di bloccare tutti gli aggiornamenti di sistema.

Gli utenti possono infatti creare dei punti di giunzione, ovvero cartelle che fanno il redirect ad altre, sotto c:\. Utilizzando il comando:

> mklink /j c:\inetpub c:\windows\system32\notepad.exe

è possibile creare un link simbolico tra la cartella inetpub e una qualsiasi altra posizione di sistema, in modo che qualsiasi aggiornamento successivo venga bloccato con errori.

![](https://www.securityinfo.it/wp-content/uploads/2025/04/errorupdate.png)

Credits: Kevin Beaumont

Beaumont ha segnalato il problema al Microsoft Security Response Center, il quale ha risposto spiegando che si tratta di una vulnerabilità di livello “Moderato” e che “***Non soddisfa l’attuale livello MSRC per l’assistenza immediata**, poiché l’aggiornamento non viene applicato solo se la cartella inetpub viene collegata a un file e ha successo se si elimina il collegamento simbolico inetpub e si riprova*“.

Microsoft ha precisato che potrà comunque valutare un fix futuro, anche se per a stretto giro non sono previste soluzioni mirate. Secondo Beaumont, è probabile che i provider EDR, compresa la compagnia di Redmond, introdurranno **meccanismi di detection per individuare i punti di giunzione creati da c:\inetpub.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [elevation dei privilegi](https://www.securityinfo.it/tag/elevation-dei-privilegi/), [patch](https://www.securityinfo.it/tag/patch/), [Patch Tuesday](https://www.securityinfo.it/tag/patch-tuesday/), [symlink](https://www.securityinfo.it/tag/symlink/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/), [Windows](https://www.securityinfo.it/tag/windows/)

[Oltre 70 vulnerabilità 0-day sfruttate nel 2024: il report di Google](https://www.securityinfo.it/2025/04/29/oltre-70-vulnerabilita-0-day-sfruttate-nel-2024-il-report-di-google/)
[Scoperto un nuovo spyware Android che colpisce l'esercito russo](https://www.securityinfo.it/2025/04/24/scoperto-un-nuovo-spyware-android-che-colpisce-lesercito-russo/)

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
* [![Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali](https://www.securityinfo.it/wp-content/uploads/2025/09/h...