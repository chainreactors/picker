---
title: Campagne basate su installer ScreenConnect distribuiscono RAT multipli: l’analisi di Acronis TRU
url: https://www.securityinfo.it/2025/09/22/campagne-basate-su-installer-screenconnect-distribuiscono-rat-multipli-lanalisi-di-acronis-tru/?utm_source=rss&utm_medium=rss&utm_campaign=campagne-basate-su-installer-screenconnect-distribuiscono-rat-multipli-lanalisi-di-acronis-tru
source: Securityinfo.it
date: 2025-09-23
fetch_date: 2025-10-02T20:31:42.642454
---

# Campagne basate su installer ScreenConnect distribuiscono RAT multipli: l’analisi di Acronis TRU

Aggiornamenti recenti Ottobre 1st, 2025 2:22 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Il 60% dei firewall non supera i controlli di conformità: la ricerca di FireMon](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)
* [Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/)
* [Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/)
* [CERT-AGID 20–26 settembre: phishing, malware e PEC compromesse](https://www.securityinfo.it/2025/09/29/cert-agid-20-26-settembre-phishing-malware-e-pec-compromesse/)
* [Nuova variante del malware XCSSET prende di mira gli sviluppatori Xcode su macOS](https://www.securityinfo.it/2025/09/26/nuova-variante-del-malware-xcsset-prende-di-mira-gli-sviluppatori-xcode-su-macos/)

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

## Campagne basate su installer ScreenConnect distribuiscono RAT multipli: l’analisi di Acronis TRU

Set 22, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/09/22/campagne-basate-su-installer-screenconnect-distribuiscono-rat-multipli-lanalisi-di-acronis-tru/#respond)

---

L’Acronis Threat Research Unit [ha pubblicato](https://www.acronis.com/en/tru/posts/trojanized-screenconnect-installers-evolve-dropping-multiple-rats-on-a-single-machine/) una nuova ricerca su una serie di campagne malevole che usano **installer ScreenConnect compromessi per distribuire RAT multipli.**

A partire dallo scorso marzo, il numero di attacchi che usano il tool di remote monitoring and management di ConnectWise per ottenere l’accesso iniziale alle reti è aumentato in maniera significativa. I cybercriminali sfruttano **tattiche di social engineering** per distribuire gli installer di ScreenConnect, camuffandoli da documenti ufficiali.

Nel corso dei mesi le tecniche dei cyberattaccanti si sono evolute fino a utilizzare un installer ClickOnce per il tool, ovvero installer che non si appoggiano su una configurazione integrata, ma **reperiscono i diversi componenti a runtime.** “*Questa evoluzione rende meno efficaci i tradizionali metodi di analisi statica e complica la prevenzione, lasciando i ricercatori di sicurezza con poche opzioni*” spiega il team di Acronis.

![ScreenConnect](https://www.securityinfo.it/wp-content/uploads/2025/09/ai-generated-8976964_1920-1.jpg)

Dopo l’installazione, gli attaccanti sfruttano le funzionalità di automazione per eseguire due RAT: uno è il già noto **AsyncRAT**, mentre l’altro è un **RAT custom basato su Powershell**. Questo nuovo trojan è in grado di acquisire informazioni sui sistemi colpiti, esfiltrare i dati tramite Microsoft.XMLHTTP e usare numerose tecniche di offuscamento. Secondo i ricercatori, l’uso di due RAT serve probabilmente sia per avere ridondanza e quindi mantenere più facilmente l’accesso ai sistemi, sia per condividere l’infrastruttura con altri cybercriminali, sia per testare nuovi strumenti.

“*Una volta installato, gli attaccanti sono in grado di assumere il controllo del computer compromesso, consentendo loro di installare ulteriori malware, rubare informazioni, stabilire una persistenza e muoversi lateralmente attraverso la rete*” aggiunge il team di Acronis.

Nel corso dell’analisi, i ricercatori di Acronis hanno individuato inoltre un **terzo RAT**, rilasciato in seguito agli altri due tramite tecniche di process hollowing, ovvero che “svuotano” il codice legittimo di un processo per iniettarvi del codice malevolo.

Dalla ricerca è inoltre emerso che gli attaccanti **utilizzano VM Windows Server 2022 preconfigurate**, con hostname ricorrenti, per più campagne, tutte su indirizzi IP differenti; ciò permette al gruppo di ruotare velocemente l’infrastruttura e attivare velocemente nuove campagne.

I ricercatori ricordano alle organizzazioni di monitorare attentamente i propri strumenti RMM e controllare le istanze di ScreenConnect utilizzate.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Acronis](https://www.securityinfo.it/tag/acronis/), [AsyncRAT](https://www.securityinfo.it/tag/asyncrat/), [RAT](https://www.securityinfo.it/tag/rat/), [RAT multipli](https://www.securityinfo.it/tag/rat-multipli/), [ScreenConnect](https://www.securityinfo.it/tag/screenconnect/), [social engineering](https://www.securityinfo.it/tag/social-engineering/)

[Attaccanti sfruttano un bug di GeoServer per attaccare un'agenzia governativa U.S.A.](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/)
[CERT-AGID 13-19 settembre: il phishing punta alle criptovalute](https://www.securityinfo.it/2025/09/22/cert-agid-13-19-settembre-phishing-criptovalute/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-6138007_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/ "Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA")

  [Report Acronis: il ransomware rimane la...](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/ "Permanent link to Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA")

  Set 11, 2025  [0](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/#respond)
* [![SafePay, cresce la minaccia ransomware contro gli MSP](https://www.securityinfo.it/wp-content/uploads/2025/07/hacker-6138007_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/07/29/safepay-cresce-la-minaccia-ransomware-contro-gli-msp/ "SafePay, cresce la minaccia ransomware contro gli MSP")

  [SafePay, cresce la minaccia ransomware...](https://www.securityinfo.it/2025/07/29/safepay-cresce-la-minaccia-ransomware-contro-gli-msp/ "Permanent link to SafePay, cresce la minaccia ransomware contro gli MSP")

  Lug 29, 2025  [0](https://www.securityinfo.it/2...