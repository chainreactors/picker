---
title: Un’estensione di Visual Studio Code consente di rubare le password di sistema
url: https://www.securityinfo.it/2023/08/17/unestensione-di-visual-studio-code-consente-di-rubare-le-password-di-sistema/
source: Over Security - Cybersecurity news aggregator
date: 2023-08-18
fetch_date: 2025-10-04T12:01:19.785007
---

# Un’estensione di Visual Studio Code consente di rubare le password di sistema

Aggiornamenti recenti Ottobre 3rd, 2025 6:09 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)
* [Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)
* [Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/)
* [Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/)

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

## Un’estensione di Visual Studio Code consente di rubare le password di sistema

Ago 17, 2023  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/minacce-2/), [News](https://www.securityinfo.it/category/news/), [Prodotto](https://www.securityinfo.it/category/news/prodotto-news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2023/08/17/unestensione-di-visual-studio-code-consente-di-rubare-le-password-di-sistema/#respond)

---

I ricercatori di [Cycode](https://cycode.com/blog/exposing-vscode-secrets/) hanno individuato una **vulnerabilità in Visual Studio Code che consente a estensioni malevole di ottenere token di autenticazione e le credenziali** memorizzate nei gestori di password del sistema.

In VS Code **le estensioni memorizzano i token d’autorizzazione forniti dagli sviluppatori per integrarsi coi servizi di terze parti**. L’IDE offre una funzionalità per memorizzare i token in maniera sicura nel sistema operativo, o almeno così si pensava prima che Cycode individuasse una vulnerabilità nel processo.

![Visual Studio Code](https://www.securityinfo.it/wp-content/uploads/2023/08/code-820275_1920.jpg)

Pixabay

La vulnerabilità mette a rischio non solo il singolo sviluppatore ma l’intera organizzazione, dal momento che i token solitamente appartengono a degli account aziendali.

Il problema risiede nel fatto che **i token di autenticazione di Visual Studio Code non sono isolati rispetto alle estensioni dell’IDE**: VS Code mette a disposizione delle estensioni Secret Storage, un’API che consente l’accesso ai token salvati sul sistema.

Qualsiasi estensione, anche malevola, può **sfruttare Secret Storage per recuperare i token memorizzati nel gestore delle password**, visto che Visual Studio Code vi ha accesso.

Le password sono cifrate ma, spiegano i ricercatori, non è difficile individuare la chiave di cifratura: il team di sicurezza ha scoperto che la chiave viene generata dal percorso dell’eseguibile e dall’ID della macchina, rendendo quindi molto semplice la generazione della chiave.

![Visual Studio Code](https://www.securityinfo.it/wp-content/uploads/2023/08/padlock-3658577_1920.jpg)

Pixabay

I ricercatori di Cycode hanno notificato **Microsoft** della vulnerabilità, ma il gigante di Redmond, pur riconoscendo l’impatto della vulnerabilità, **ha deciso di non agire in quanto le estensioni non sono state pensate per essere eseguite in maniera isolata**. Il bug deriva dal design stesso del processo, e per questo motivo Microsoft non rilascerà alcun fix.

Di fatto, **la responsabilità rimarrà nelle mani degli sviluppatori**. Cycode ricorda di limitare, per quanto possibile, il numero di estensioni di VS Code e di **controllare sempre l’affidabilità delle fonti da cui provengono**. Nel caso in cui un’estensione utilizzi i token o altre informazioni sensibili, è consigliabile implementare un livello ulteriore di cifratura per aumentare la sicurezza.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [cifratura](https://www.securityinfo.it/tag/cifratura/), [Microsoft](https://www.securityinfo.it/tag/microsoft/), [password di sistema](https://www.securityinfo.it/tag/password-di-sistema/), [password manager](https://www.securityinfo.it/tag/password-manager/), [token di autorizzazione](https://www.securityinfo.it/tag/token-di-autorizzazione/), [Visual Studio Code](https://www.securityinfo.it/tag/visual-studio-code/)

[I leak del codice dei ransomware favoriscono la diffusione di nuove varianti](https://www.securityinfo.it/2023/08/18/i-leak-del-codice-dei-ransomware-favorisce-la-diffusione-di-nuove-varianti/)
[Smantellata 16shop, piattaforma di "phishing-as-a-service"](https://www.securityinfo.it/2023/08/16/smantellata-16shop-piattaforma-di-phishing-as-a-service/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Secret Blizzard attacca le ambasciate straniere a Mosca tramite gli ISP](https://www.securityinfo.it/wp-content/uploads/2025/08/Gemini_Generated_Image_jk74qwjk74qwjk74-120x85.png)](https://www.securityinfo.it/2025/08/01/secret-blizzard-attacca-le-ambasciate-straniere-a-mosca-tramite-gli-isp/ "Secret Blizzard attacca le ambasciate straniere a Mosca tramite gli ISP")

  [Secret Blizzard attacca le ambasciate...](https://www.securityinfo.it/2025/08/01/secret-blizzard-attacca-le-ambasciate-straniere-a-mosca-tramite-gli-isp/ "Permanent link to Secret Blizzard attacca le ambasciate straniere a Mosca tramite gli ISP")

  Ago 01, 2025  [0](https://www.securityinfo.it/2025/08/01/secret-blizzard-attacca-le-ambasciate-straniere-a-mosca-tramite-gli-isp/#respond)
* [![Grave alerta SharePoint: attacco in corso che elude le difese](https://www.securityinfo.it/wp-content/uploads/2025/07/SharePoint_lug-2025CG-120x85.png)](https://www.securityinfo.it/2025/07/21/grave-alerta-per-sharepoint-toolshell-e-un-attacco-in-corso-che-elude-le-difese-tradizionali/ "Grave alerta SharePoint: attacco in corso che elude le difese")

  [Grave alerta SharePoint: attacco in...](https://www.securityinfo.it/2025/07/21/grave-alerta-per-sharepoint-toolshell-e-un-attacco-in-corso-che-elude-le-difese-tradizionali/ "Permanent link to Grave alerta SharePoint: attacco in corso che elude le difese")

  Lug 21, 2025  [0](https://www.securityinfo.it/2025/07/21/grave-alerta-per-sharepoint-toolshell-e-un-attacco-in-corso-che-elude-le-difese-tradizionali/#respond)
* [![Una vulnerabilità di Open VSX Registry mette in pericolo milioni di sviluppatori](https:...