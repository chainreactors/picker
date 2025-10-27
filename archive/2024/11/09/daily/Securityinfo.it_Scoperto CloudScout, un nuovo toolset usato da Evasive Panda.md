---
title: Scoperto CloudScout, un nuovo toolset usato da Evasive Panda
url: https://www.securityinfo.it/2024/11/08/scoperto-cloudscout-un-nuovo-toolset-usato-da-evasive-panda/?utm_source=rss&utm_medium=rss&utm_campaign=scoperto-cloudscout-un-nuovo-toolset-usato-da-evasive-panda
source: Securityinfo.it
date: 2024-11-09
fetch_date: 2025-10-06T19:21:26.266422
---

# Scoperto CloudScout, un nuovo toolset usato da Evasive Panda

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

## Scoperto CloudScout, un nuovo toolset usato da Evasive Panda

Nov 08, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2024/11/08/scoperto-cloudscout-un-nuovo-toolset-usato-da-evasive-panda/#respond)

---

I ricercatori di **ESET** [hanno scoperto](https://www.welivesecurity.com/en/eset-research/cloudscout-evasive-panda-scouting-cloud-services/) **CloudScout**, un nuovo toolset usato dal gruppo cinese **Evasive Panda** per le operazioni post-compromissione. Gli strumenti sono stati per colpire un’organizzazione religiosa e un’entità governativa taiwanesi tra il 2022 e il 2023.

![Evasive Panda](https://www.securityinfo.it/wp-content/uploads/2024/11/Evasive_Panda_Cybersecurity_Landscape.jpeg)

CloudScout è un **framework malware .NET composto da molteplici moduli** capaci di colpire diversi servizi cloud pubblici, tra i quali Google Drive, Gmail e Outlook. La tecnica principale del framework si basa sull’**hijacking di sessioni web di utenti autenticati**: i moduli ottengono i cookie salvati nel browser per accedere ai servizi e quindi ai dati in cloud, eludendo i controlli della 2FA.

Tramite un plugin, il toolset si integra con **MgBot**, il malware più noto del gruppo, per accedere ai dati dei servizi cloud ed esfiltrarli. Tutti i moduli del framework condividono un’architettura uniforme e si basano su una funzionalità core chiamata *Cloud*, praticamente identica per ogni modulo.

Nell’analisi dei ricercatori, i moduli relativi a Google Drive, Gmail e Outlook accedono inizialmente ai cookie di sessione contenuti nel browser. Dopo aver eseguito l’autenticazione con l’account della vittima, comincia la fase di esfiltrazione dei dati: **ciascun modulo usa una serie di richieste web preimpostate per cercare e raccogliere i file** tra le cartelle del servizio cloud.

I moduli relativi a Gmail e Outlook cercano informazioni sugli header delle email, il corpo dei messaggi e gli eventuali allegati condivisi; al contrario, il modulo che colpisce Google Drive cerca le informazioni sull’account e tutti i file con estensioni .doc, .docx, .xls, .xlsx, .ppt, .pptx, .pdf e .txt.

In seguito, i moduli appendono un header a ogni file scaricato con le informazioni sul tipo di dato, l’ID del client, lo username della vittima ed eventualmente il titolo dell’email. Questi dati vengono usati probabilmente per **processare massivamente i file e ordinarli in un database.**

![](https://www.securityinfo.it/wp-content/uploads/2024/10/security-6901712_1920.jpg)

I documenti e i dati raccolti vengono poi compressi in un archivio ZIP; la cartella in seguito verrà inviata al server degli attaccanti usando MgBot o  Nightdoor, una backdoor piuttosto recente realizzata da Evasive Panda.

Stando all’analisi dei ricercatori, **il toolset è stato sviluppato nel 2020** e ha subito diverse revisioni. Oltre ai tre moduli analizzati dal team di ESET, ne esistono altri sette, anche se al momento non è ancora chiaro il loro scopo. Considerando la naming convention usata dal gruppo (CGD = Google Drive, CGM = GMail e COL=Outlook), **è possibile che i moduli CTW e CFB colpiscano rispettivamente Twitter e Facebook.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [CloudScout](https://www.securityinfo.it/tag/cloudscout/), [esfiltrazione dati](https://www.securityinfo.it/tag/esfiltrazione-dati/), [Evasive Panda](https://www.securityinfo.it/tag/evasive-panda/), [MgBot](https://www.securityinfo.it/tag/mgbot/), [Nightdoor](https://www.securityinfo.it/tag/nightdoor/), [toolset malware](https://www.securityinfo.it/tag/toolset-malware/)

[Furto di credenziali, la minaccia di cracking più diffusa](https://www.securityinfo.it/2024/11/08/furto-di-credenziali-la-minaccia-di-cracking-piu-diffusa/)
[Phishing, breach e trojan bancari: Acronis condivide il rapporto sulle minacce più recenti](https://www.securityinfo.it/2024/11/07/phishing-breach-e-trojan-bancari-acronis-condivide-il-rapporto-sulle-minacce-piu-recenti/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Un attacco supply chain ha compromesso oltre 40 pacchetti NPM](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_px0h5ppx0h5ppx0h-120x85.png)](https://www.securityinfo.it/2025/09/16/un-attacco-supply-chain-ha-compromesso-oltre-40-pacchetti-npm/ "Un attacco supply chain ha compromesso oltre 40 pacchetti NPM")

  [Un attacco supply chain ha compromesso...](https://www.securityinfo.it/2025/09/16/un-attacco-supply-chain-ha-compromesso-oltre-40-pacchetti-npm/ "Permanent link to Un attacco supply chain ha compromesso oltre 40 pacchetti NPM")

  Set 16, 2025  [0](https://www.securityinfo.it/2025/09/16/un-attacco-supply-chain-ha-compromesso-oltre-40-pacchetti-npm/#respond)
* [![GPUGate, una nuova tecnica che sfrutta Google Ads e GitHub per distribuire malware](https://www.securityinfo.it/wp-content/uploads/2025/09/data-theft-9480273_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/09/09/gpugate-una-nuova-tecnica-che-sfrutta-google-ads-e-github-per-distribuire-malware/ "GPUGate, una nuova tecnica che sfrutta Google Ads e GitHub per distribuire malware")

  [GPUGate, una nuova tecnica che sfrutta...](https://www.securityinfo.it/2025/09/09/gpugate-una-nuova-tecnica-che-sfrutta-google-ads-e-github-per-distribuire-malware/ "Permanent link to GPUGate, una nuova tecnica che sfrutta Google Ads e GitHub per distribuire malware")

  Set 09, 2025  [0](https://www.securityinfo.it/2025/09/09/gpugate-una-nuova-tecnica-che-sfrutta-google-ads-e-github-per-distribuire-malware/#respond)
* [![Prompt injection nelle imma...