---
title: Nuove patch da Microsoft
url: https://www.securityinfo.it/2022/10/12/nuove-patch-da-microsoft/?utm_source=rss&utm_medium=rss&utm_campaign=nuove-patch-da-microsoft
source: Over Security - Cybersecurity news aggregator
date: 2022-10-20
fetch_date: 2025-10-03T20:24:31.753441
---

# Nuove patch da Microsoft

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

## Nuove patch da Microsoft

Ott 12, 2022  [Redazione news](https://www.securityinfo.it/author/redazione-news/ "Articoli scritti da Redazione news")
 [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2022/10/12/nuove-patch-da-microsoft/#respond)

---

##### Il Patch Tuesday di ottobre porta la risoluzione di 15 bug classificati come critici, tra cui alcuni di elevazione dei privilegi ed esecuzione di codice remoto

Nel Patch Tuesday, ossia la risoluzione mensile dei bug di Microsoft, di [ottobre 2022](https://msrc.microsoft.com/update-guide/releaseNote/2022-Oct) viene affrontata una serie di vulnerabilità, ma **ci sono anche dei grandi assenti**.

Microsoft sta infatti [indagando](https://msrc-blog.microsoft.com/2022/09/29/customer-guidance-for-reported-zero-day-vulnerabilities-in-microsoft-exchange-server/) su **due vulnerabilità zero-day segnalatele che interessano Microsoft Exchange Server 2013, Exchange Server 2016 ed Exchange Server 2019** per cui ha pubblicato mitigazioni a partire da fine settembre.

![](https://www.securityinfo.it/wp-content/uploads/2022/10/computer-g9dd3f8f74_1920-1024x649.jpg)

La prima, identificata come **CVE-2022-41040, è una vulnerabilità SSRF (Server-Side Request Forgery)**, mentre la seconda, la **CVE-2022-41082, consente l’esecuzione di codice remoto** (RCE) quando PowerShell è accessibile all’attaccante.

**I bug sono attivamente sfruttati dai pirati** e, come riporta [Zero Day Initiative](https://www.zerodayinitiative.com/blog/2022/10/11/the-october-2022-security-update-review) (ZDI), non essendo disponibili aggiornamenti per risolvere completamente questi problemi, la soluzione migliore che gli amministratori possono adottare è assicurarsi che sia installato l’aggiornamento cumulativo (CU) di settembre 2021.

**Delle 85 nuove patch rilasciate da Microsoft, 15 sono per bug classificati come critici**. Tra questi, la [CVE-2022-41033](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41033), una vulnerabilità attivamente sfruttata di elevazione dei privilegi nel servizio sistema eventi COM+ che può conferire a un attaccante i privilegi di sistema.

Questo mese il bug più grave è stato invece il **[CVE-2022-37968](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-37968), una falla nell’escalation dei privilegi in Azure Arc Connect**, che ha ricevuto il punteggio CVSS massimo di 10 su 10.

**Riguarda i cluster Kubernetes abilitati ad Azure Arc** e potrebbe essere sfruttato da un utente non autenticato per ottenere il controllo a livello di amministratore sul cluster.

**Vulnerabilità critiche di escalation dei privilegi sono state riscontrate anche in Windows Active Directory e Hyper-V** ([CVE-2022-37976](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-37976) e [CVE-2022-37979](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-37979) ).

Sono stati inoltre risolti **sette bug critici di esecuzione di codice remoto per il protocollo point-to-point (PPP) in Windows**, che ha ricevuto otto patch: [CVE-2022-22035](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-22035), [CVE-2022-24504](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-24504), [CVE-2022-30198](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-30198), [CVE-2022-33634](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-33634), [CVE-2022-38000](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-38000), [CVE-2022-38047](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-38047) e [CVE-2022-41081](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41081).

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Microsoft](https://www.securityinfo.it/tag/microsoft/), [Patch Tuesday](https://www.securityinfo.it/tag/patch-tuesday/), [Privilege escalation](https://www.securityinfo.it/tag/privilege-escalation/), [Zero-day](https://www.securityinfo.it/tag/zero-day/)

[Nuove misure da Microsoft contro gli attacchi brute force](https://www.securityinfo.it/2022/10/12/nuove-misure-da-microsoft-contro-gli-attacchi-brute-force/)
[CONUS: verso il monitoraggio real-time delle calamità](https://www.securityinfo.it/2022/10/11/conus-ia-monitoraggio-real-time/)

---

![](https://secure.gravatar.com/avatar/c5974e9c8e007cf085089d7686c35ca4?s=90&d=mm&r=g)

##### [Redazione news](https://www.securityinfo.it/author/redazione-news/)

##### Articoli correlati

* [![Secret Blizzard attacca le ambasciate straniere a Mosca tramite gli ISP](https://www.securityinfo.it/wp-content/uploads/2025/08/Gemini_Generated_Image_jk74qwjk74qwjk74-120x85.png)](https://www.securityinfo.it/2025/08/01/secret-blizzard-attacca-le-ambasciate-straniere-a-mosca-tramite-gli-isp/ "Secret Blizzard attacca le ambasciate straniere a Mosca tramite gli ISP")

  [Secret Blizzard attacca le ambasciate...](https://www.securityinfo.it/2025/08/01/secret-blizzard-attacca-le-ambasciate-straniere-a-mosca-tramite-gli-isp/ "Permanent link to Secret Blizzard attacca le ambasciate straniere a Mosca tramite gli ISP")

  Ago 01, 2025  [0](https://www.securityinfo.it/2025/08/01/secret-blizzard-attacca-le-ambasciate-straniere-a-mosca-tramite-gli-isp/#respond)
* [![Grave alerta SharePoint: attacco in corso che elude le difese](https://www.securityinfo.it/wp-content/uploads/2025/07/SharePoint_lug-2025CG-120x85.png)](https://www.securityinfo.it/2025/07/21/grave-alerta-per-sharepoint-toolshell-e-un-attacco-in-corso-che-elude-le-difese-tradizionali/ "Grave alerta SharePoint: attacco in corso che elude le difese")

  [Grave alerta SharePoint: attacco in...](https://www.securityinfo.it/2025/07/21/grave-alerta-per-sha...