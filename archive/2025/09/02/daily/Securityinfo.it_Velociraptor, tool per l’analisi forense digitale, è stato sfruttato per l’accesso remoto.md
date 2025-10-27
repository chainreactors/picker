---
title: Velociraptor, tool per l’analisi forense digitale, è stato sfruttato per l’accesso remoto
url: https://www.securityinfo.it/2025/09/01/velociraptor-tool-per-lanalisi-forense-digitale-e-stato-sfruttato-per-laccesso-remoto/?utm_source=rss&utm_medium=rss&utm_campaign=velociraptor-tool-per-lanalisi-forense-digitale-e-stato-sfruttato-per-laccesso-remoto
source: Securityinfo.it
date: 2025-09-02
fetch_date: 2025-10-02T19:31:53.307744
---

# Velociraptor, tool per l’analisi forense digitale, è stato sfruttato per l’accesso remoto

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

## Velociraptor, tool per l’analisi forense digitale, è stato sfruttato per l’accesso remoto

Set 01, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Intrusione](https://www.securityinfo.it/category/news/intrusione/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/09/01/velociraptor-tool-per-lanalisi-forense-digitale-e-stato-sfruttato-per-laccesso-remoto/#respond)

---

Qualche giorno fa la Counter Threat Unit di Sophos [ha scoperto](https://news.sophos.com/en-us/2025/08/26/velociraptor-incident-response-tool-abused-for-remote-access/) che **Velociraptor**, un tool per l’analisi forense digitale e la risposta agli incidenti di sicurezza, è stato **sfruttato per ottenere l’accesso remoto a una rete aziendale.**

Secondo il team, gli attaccanti hanno usato il software per scaricare ed eseguire Visual Studio Code con l’obiettivo di creare un canale di comunicazione con un server C2.

Nel dettaglio, gli attaccanti hanno usato msiexec di Windows per scaricare un installer da un dominio Cloudflare Workers, una cartella di staging contenente diversi tool per gli attacchi. Il file ha installato Velociraptor, il quale ha permesso agli attaccanti di scaricare Visual Studio Code dalla stessa cartella di staging in modo da eseguire codice da remoto. Secondo quanto riportato dai ricercatori di Sophos, i cybercriminali hanno usato msiexec per scaricare e installare altri payload malevoli.

![Velociraptor. Credits: Sophos](https://www.securityinfo.it/wp-content/uploads/2025/09/Velociraptor2508-fig1.png)

Velociraptor usato per creare un canale di comunicazione sfruttando Visual Studio Code. Credits: Sophos

L’attività sospetta di Visual Studio Code ha scatenato un alert che ha permesso al team di Sophos di agire tempestivamente e bloccare l’attacco del gruppo, isolando l’host colpito prima che gli attaccanti raggiungessero il loro vero scopo. Secondo la Counter Threat Unit, **è molto probabile che il gruppo volesse distribuire un ransomware.**

“*Gli attaccanti spesso abusano degli strumenti di monitoraggio e gestione remota (RMM). In alcuni casi, sfruttano strumenti preesistenti sui sistemi presi di mira. In altri, implementano gli strumenti durante l’attacco. **L’incidente Velociraptor rivela che gli attaccanti stanno passando all’uso di strumenti di risposta agli incidenti per ottenere persistenza nelle reti e ridurre al minimo la quantità di malware che distribuiscono***” ha spiegato il team di Sophos.

Per ridurre il rischio di questo tipo di attacchi e prevenire la minaccia ransomware, i ricercatori della compagnia consigliano di implementare un sistema EDR, monitorare attentamente l’uso dei tool ed eventuali attività sospette, effettuare backup regolari e, in generale, seguire le best practice note per garantire la sicurezza dei sistemi.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [analisi forense digitale](https://www.securityinfo.it/tag/analisi-forense-digitale/), [monitoraggio endpoint](https://www.securityinfo.it/tag/monitoraggio-endpoint/), [Ransomware](https://www.securityinfo.it/tag/ransomware/), [Sophos](https://www.securityinfo.it/tag/sophos/), [tool accesso remoto](https://www.securityinfo.it/tag/tool-accesso-remoto/), [Velociraptor](https://www.securityinfo.it/tag/velociraptor/)

[Il data breach contro Salesloft impatta centinaia di servizi](https://www.securityinfo.it/2025/09/02/il-data-breach-contro-salesloft-impatta-centinaia-di-servizi/)
[Migrazione a Windows 11: le aziende devono affrontare molte sfide, ma qualsiasi ritardo è pericoloso](https://www.securityinfo.it/2025/08/29/migrazione-a-windows-11-le-aziende-devono-affrontare-molte-sfide-ma-qualsiasi-ritardo-e-pericoloso/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-6138007_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/ "Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA")

  [Report Acronis: il ransomware rimane la...](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/ "Permanent link to Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA")

  Set 11, 2025  [0](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/#respond)
* [![GPUGate, una nuova tecnica che sfrutta Google Ads e GitHub per distribuire malware](https://www.securityinfo.it/wp-content/uploads/2025/09/data-theft-9480273_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/09/09/gpugate-una-nuova-tecnica-che-sfrutta-google-ads-e-github-per-distribuire-malware/ "GPUGate, una nuova tecnica che sfrutta Google Ads e GitHub per distribuire malware")

  [GPUGate, una nuova tecnica che sfrutta...](https://www.securityinfo.it/2025/09/09/gpugate-una-nuova-tecnica-che-sfrutta-google-ads-e-github-per-distribuire-malware/ "Permanent link to GPUGate, una nuova tecnica che sfrutta Google Ads e GitHub per distribuire malware")

  Set 09, 2025  [0](https://www.securityinfo.it/2025/09/09/gpugate-una-nuova-tecnica-che-sfrutta-google-ads-e-github-per-distribuire-malware/#respond)
* [![Anche G...