---
title: CERT-AGID 27 aprile – 3 maggio 2024: 29 campagne malevole, 218 IoC e il keylogger di PuntoFisco
url: https://www.securityinfo.it/2024/05/06/cert-agid-27-aprile-3-maggio-2024-29-campagne-malevole-218-ioc-keylogger-puntofisco/?utm_source=rss&utm_medium=rss&utm_campaign=cert-agid-27-aprile-3-maggio-2024-29-campagne-malevole-218-ioc-keylogger-puntofisco
source: Securityinfo.it
date: 2024-05-07
fetch_date: 2025-10-06T17:19:31.762476
---

# CERT-AGID 27 aprile – 3 maggio 2024: 29 campagne malevole, 218 IoC e il keylogger di PuntoFisco

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

## CERT-AGID 27 aprile – 3 maggio 2024: 29 campagne malevole, 218 IoC e il keylogger di PuntoFisco

Mag 06, 2024  [Stefano Silvestri](https://www.securityinfo.it/author/stefano-silvestri/ "Articoli scritti da Stefano Silvestri")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [Leaks](https://www.securityinfo.it/category/news/leaks-news/), [Malware](https://www.securityinfo.it/category/news/malware-news/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [Phishing](https://www.securityinfo.it/category/news/phishing/), [Tecnologia](https://www.securityinfo.it/category/news/tecnologia-news/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2024/05/06/cert-agid-27-aprile-3-maggio-2024-29-campagne-malevole-218-ioc-keylogger-puntofisco/#respond)

---

Questa settimana, il **CERT-AGID** ha identificato e analizzato **29 campagne malevole** nell’ambito del panorama italiano di riferimento. Tra queste, **21 erano specificamente dirette verso obiettivi italiani**, mentre le restanti 8, pur essendo generiche, hanno influenzato l’Italia. Inoltre, l’agenzia ha fornito ai suoi enti accreditati **218 indicatori di compromissione (IOC)** rilevati.

## I temi più rilevanti della settimana

Questa settimana, sono stati individuati **nove temi principali** utilizzati per condurre campagne malevole in Italia. Tra questi spicca, come al solito, il tema **Banking**, ricorrente nelle operazioni di phishing e smishing, principalmente dirette ai clienti di banche italiane e impiegate anche per diffondere il malware Irata, volto a compromettere i dispositivi Android degli utenti italiani.

Il tema **Ordine** è stato utilizzato per le campagne che coinvolgono i malware AgentTesla, Formbook e ZgRat, mentre **Rinnovo** è stato adottato per attacchi di phishing rivolti ai clienti di Aruba. Gli altri temi hanno facilitato la propagazione di diverse campagne di malware e phishing.

Tra gli eventi di particolare interesse si segnalano la diffusione di malware **keylogger attraverso PuntoFisco, una falsa pagina dell’Agenzia delle Entrate**. Si annota poi una campagna italiana del malware **Remcos**, veicolata tramite Guloader, e campagne di smishing a nome dell’INPS volte a sottrarre documenti di identità. È stata infine riscontrata ancora una campagna ransomware **Lockbit**.

![](https://www.securityinfo.it/wp-content/uploads/2024/05/CERT-AGID-temi.png)

Fonte: CERT-AGID

## Malware della settimana

Questa settimana sono state monitorate **otto famiglie di malware** con diverse campagne attive. **AgentTesla** si è distinto con sei campagne, quattro delle quali italiane e due generiche, incentrate sui temi Ordine, Contratti e Delivery, veicolate attraverso email contenenti allegati nei formati RAR, CAB, IMG, RAR e ACE. **RemcosRAT** è stato al centro di tre campagne, due italiane e una generica, focalizzate sui temi Pagamenti e Documenti, con allegati in ZIP, 7Z e CAB, tra cui una campagna italiana che utilizza Guloader e i loghi della società Leonardo.

**Formbook** è stato coinvolto in due campagne generiche sui temi Ordine e Delivery, diffuse in Italia tramite allegati LZH e ZIP che contenevano documenti DOC sfruttando una vecchia vulnerabilità di Equation Editor. **Irata** è stato contrastato in due campagne italiane sul tema Banking, diffuse tramite SMS con link per il download di un APK malevolo. **DarkGate** è stato implicato in una campagna generica sul tema Documenti, veicolata tramite email con allegati HTML che scaricano uno script HTA.

**VBLogger** è stato utilizzato in una campagna italiana incentrata sull’Agenzia delle Entrate, mirata a compromettere i sistemi con un keylogger scritto in VB6. **LockBit** si è proposto nuovamente in una campagna sui Documenti, veicolando ransomware tramite email con allegati ZIP contenenti un eseguibile SCR, come già osservato la settimana scorsa. Infine, **ZGrat** è stato rilevato in una campagna sul tema Ordine, diffusa attraverso email con allegati XLAM.

![](https://www.securityinfo.it/wp-content/uploads/2024/05/CERT-AGID-malware.png)

Fonte: CERT-AGID

## Phishing della settimana

Questa settimana, cinque marchi sono stati coinvolti in attività di phishing e smishing. Tra questi, spiccano la succitata campagna di phishing mirata all’Agenzia delle Entrate (Punto Fisco) e diverse campagne di smishing che hanno preso di mira l’**INPS**.

![](https://www.securityinfo.it/wp-content/uploads/2024/05/CERT-AGID-phishing.png)

Fonte: CERT-AGID

## Formati e canali di diffusione

L’ultima settimana ha visto l’utilizzo di **13 diverse tipologie di file per veicolare gli attacchi**. I file ZIP sono stati ancora una volta i più utilizzati (4 volte), seguiti da CAB, RAR, IMG e APK (2 volte). A quota 1 seguono i file LZH, HTML, HTA, DOC, XLAM, ACE, BAT e 7Z.

Quanto ai canali di diffusione, **le email sono state utilizzate 22 volte, gli SMS 5 volte**.

![](https://www.securityinfo.it/wp-content/uploads/2024/05/CERT-AGID-files.png)

Fonte: CERT-AGID

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [CERT-AGID](https://www.securityinfo.it/tag/cert-agid/), [Phishing](https://www.securityinfo.it/tag/phishing/), [Smishing](https://www.securityinfo.it/tag/smishing/)

[Attacchi di phishing: Microsoft e Google le più colpite](https://www.securityinfo.it/2024/05/07/attacchi-di-phishing-microsoft-e-google-le-piu-colpite/)
[Scanner di vulnerabilità: uno solo non basta più](https://www.securityinfo.it/2024/05/06/scanner-di-vulnerabilita-uno-solo-non-basta-piu/)

---

![](https://secure.gravatar.com/avatar/d290cb647e218511e0408135528fb5f2?s=90&d=mm&r=g)

##### [Stefano Silvestri](https://www.securityinfo.it/author/stefano-silvestri/)

##### Articoli correlati

* [![CERT-AGID 27 settembre...