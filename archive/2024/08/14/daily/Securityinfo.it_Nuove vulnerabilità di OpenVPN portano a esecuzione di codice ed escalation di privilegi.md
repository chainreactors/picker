---
title: Nuove vulnerabilità di OpenVPN portano a esecuzione di codice ed escalation di privilegi
url: https://www.securityinfo.it/2024/08/13/nuove-vulnerabilita-openvpn-esecuzione-codice-escalation-privilegi/?utm_source=rss&utm_medium=rss&utm_campaign=nuove-vulnerabilita-openvpn-esecuzione-codice-escalation-privilegi
source: Securityinfo.it
date: 2024-08-14
fetch_date: 2025-10-06T18:04:21.316524
---

# Nuove vulnerabilità di OpenVPN portano a esecuzione di codice ed escalation di privilegi

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

## Nuove vulnerabilità di OpenVPN portano a esecuzione di codice ed escalation di privilegi

Ago 13, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2024/08/13/nuove-vulnerabilita-openvpn-esecuzione-codice-escalation-privilegi/#respond)

---

Microsoft [ha individuato](https://www.microsoft.com/en-us/security/blog/2024/08/08/chained-for-attack-openvpn-vulnerabilities-discovered-leading-to-rce-and-lpe/) diverse **vulnerabilità in OpenVPN**, noto software VPN open source usato da centinaia di compagnie in tutte il mondo. Il team di ricercatori ha spiegato che un attaccante può sfruttare alcune di queste vulnerabilità a catena per eseguire attacchi di esecuzione di codice da remoto e di escalation dei privilegi locale, **prendendo il controllo completo degli endpoint target.**

Nel dettaglio, il team di Microsoft ha individuato quattro bug che possono essere **usati in combinazione** per eseguire attacchi più complessi, tutti presenti sul lato client dell’architettura di OpenVPN.

![vulnerabilità OpenVPN](https://www.securityinfo.it/wp-content/uploads/2024/08/cyber-security-3374252_1920.jpg)

Pixabay

La prima, la **CVE-2024-1305**, è un bug di **memory overflow c**he colpisce il driver Windows TAP (Terminal Access Point) e consente a un attaccante di eseguire codice arbitrario sul kernel della macchina, potenzialmente causando un’interruzione di servizio.

La seconda vulnerabilità scoperta, la **CVE-2024-27459**, risiede nel meccanismo di comunicazione tra il processo openvpn.exe e il servizio openvpnserv.exe. Questo meccanismo ha una criticità che può essere sfruttata per causare uno **stack overflow** ed effettuare escalation dei privilegi.

La **CVE-2024-24974** risiede nel servizio openvpnserv.exe e in particolare nello step di creazione di un nuovo processo openvpn.exe. Sfruttando questa vulnerabilità, un attaccante può **accedere da remoto alla pipe di comunicazione** ed eseguire operazioni su di essa.

Infine, la **CVE-2024-27903** è una vulnerabilità del meccanismo di aggiunta di plugin di OpenVPN. I plugin possono essere caricati da diversi path su un dispositivo, e questo comportamento può essere sfruttato dagli attaccanti per **caricare plugin malevoli.**

I ricercatori di Microsoft spiegano che queste vulnerabilità possono essere usate solo dopo essere entrati in possesso di **credenziali utente valide**. Oltre a essere sfruttati singolarmente, i bug possono anche essere combinati per eseguire attacchi più sofisticati e difficili da bloccare.

Per eseguire questi attacchi complessi, sottolinea il team di Microsoft, **è necessario possedere una profonda conoscenza dei meccanismi interni di funzionamento di OpenVPN**, oltre ad avere accesso a un account utente. In ogni caso, visto che l’impatto degli attacchi è significativo, non bisogna abbassare la guardia e occorre invece proteggere i propri endpoint in maniera adeguata.

“*Gli aggressori potrebbero lanciare una catena di attacchi completa su un dispositivo che utilizza una versione vulnerabile di OpenVPN, ottenendo il **pieno controllo dell’endpoint target**. Questo controllo potrebbe consentire loro di rubare dati sensibili, manometterli o addirittura cancellare e distruggere informazioni critiche, causando danni sostanziali agli ambienti privati e aziendali*” specifica Microsoft.

![](https://www.securityinfo.it/wp-content/uploads/2024/07/background-5035258_1920.jpg)

**Tutte le versioni di OpenVPN precedenti alla 2.5.10 e alla 2.6.10 sono vulnerabili** ai bug indicati. Microsoft consiglia di aggiornare il prima possibile il software all’ultima versione, limitare l’accesso a OpenVPN solo agli utenti autorizzati e mettere in campo soluzioni di protezione degli endpoint robuste.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [denial of service](https://www.securityinfo.it/tag/denial-of-service/), [escalation dei privilegi](https://www.securityinfo.it/tag/escalation-dei-privilegi/), [esecuzione di codice da remoto](https://www.securityinfo.it/tag/esecuzione-di-codice-da-remoto/), [Kernel](https://www.securityinfo.it/tag/kernel/), [OpenVPN](https://www.securityinfo.it/tag/openvpn/), [VPN](https://www.securityinfo.it/tag/vpn/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[0.0.0.0 Day, la vulnerabilità "maggiorenne" che colpisce i principali browser](https://www.securityinfo.it/2024/08/14/0-0-0-0-day-la-vulnerabilita-maggiorenne-che-colpisce-tutti-i-principali-browser/)
[INTERPOL: I-GRIP contro le truffe BEC](https://www.securityinfo.it/2024/08/12/interpol-i-grip-contro-le-truffe-bec/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_d4x8rid4x8rid4x8-120x85.png)](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  [Firewall Cisco sotto attacco: una nuova...](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Permanent link to Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  Set 29, 2025  [0](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-...