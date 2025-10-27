---
title: Cybercriminali sfruttano una vulnerabilità di Langflow per prendere il controllo dei server
url: https://www.securityinfo.it/2025/05/07/cybercriminali-sfruttano-una-vulnerabilita-di-langflow-per-prendere-il-controllo-dei-server/?utm_source=rss&utm_medium=rss&utm_campaign=cybercriminali-sfruttano-una-vulnerabilita-di-langflow-per-prendere-il-controllo-dei-server
source: Securityinfo.it
date: 2025-05-08
fetch_date: 2025-10-06T22:30:04.000090
---

# Cybercriminali sfruttano una vulnerabilità di Langflow per prendere il controllo dei server

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

## Cybercriminali sfruttano una vulnerabilità di Langflow per prendere il controllo dei server

Mag 07, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/05/07/cybercriminali-sfruttano-una-vulnerabilita-di-langflow-per-prendere-il-controllo-dei-server/#respond)

---

Una **vulnerabilità di Langflow** sta venendo attivamente sfruttata per prendere il controllo dei server: a dirlo è la CISA in un [advisory](https://www.cisa.gov/news-events/alerts/2025/05/05/cisa-adds-one-known-exploited-vulnerability-catalog) pubblicato lo scorso 5 maggio.

Il bug di mancata autenticazione, tracciato come CVE-2025-3248, consente a un attaccante non autenticato di **prendere il controllo completo dei server Langflow** e comprometterli.

Langflow è un [**tool open-source**](https://www.langflow.org/) **di programmazione visuale** che aiuta gli sviluppatori a creare agenti di IA e workflow che integrano API, modelli e database. L’interfaccia drag & drop consente di aggiungere facilmente elementi al progetto, come input, prompt e output, e di scegliere il modello di IA da utilizzare. Lo strumento è ampiamente usato dalla community degli sviluppatori: su GitHub conta 63.000 fork e oltre 14.000 utenti.

![Langflow](https://www.securityinfo.it/wp-content/uploads/2025/05/hacker-8033977_1920-1.jpg)

A individuare la vulnerabilità sono stati i ricercatori di Horizon3.ai. Il tool consente di **eseguire codice remoto anche agli utenti non autenticati** e non prevede meccanismi di sandboxing. Il team di Horizon3.ai ha analizzato il codice per capire l’impatto di queste scelte architetturali e ha individuato l’endpoint per l’esecuzione remota, `/api/v1/validate/code`, che esegue il comando `exec` di Python sull’input dell’utente senza una corretta validazione.

Tramite questo endpoint, l’input dell’utente viene eseguito direttamente sul server, consentendo a un attaccante di eseguire qualsiasi comando. Sfruttare la vulnerabilità non è in realtà così semplice, ma utilizzando le funzioni decorator di Python è possibile **iniettare un payload malevolo per compromettere il server.**

Il team dietro il progetto **[ha rilasciato una fix](https://github.com/langflow-ai/langflow/pull/6911) per il bug nella versione 1.3.0** pubblicata il 31 marzo scorso. I ricercatori di Horizon3.ai invitano gli sviluppatori che usano il tool ad aggiornarlo il prima possibile a quella versione o all’ultima rilasciata (la 1.4.0).

“*Il codice vulnerabile è presente nelle prime versioni di Langflow, fino a due anni fa, e dai nostri test sembra che molte versioni precedenti alla 1.3.0, se non tutte, sono vulnerabili*” ha spiegato il team di Horizon3.ai. I ricercatori hanno inoltre affermato che **la patch si limita ad aggiungere l’autenticazione per l’endpoint e che quindi il bug può essere ancora sfruttato da qualsiasi utente**, anche se “*questo era comunque già possibile senza la presenza della vulnerabilità*“. L’unico intervento davvero efficace sarebbe quello di utilizzare meccanismi di sandboxing per isolare il codice eseguito da remoto.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [agenti IA](https://www.securityinfo.it/tag/agenti-ia/), [compromissione sistema](https://www.securityinfo.it/tag/compromissione-sistema/), [esecuzione di codice da remoto](https://www.securityinfo.it/tag/esecuzione-di-codice-da-remoto/), [Intelligenza artificiale](https://www.securityinfo.it/tag/intelligenza-artificiale/), [Langflow](https://www.securityinfo.it/tag/langflow/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[L'infrastruttura petrolifera statunitense è sotto attacco](https://www.securityinfo.it/2025/05/08/infrastruttura-petrolifera-statunitense-e-sotto-attacco/)
[I criminali sfruttano la vulnerabilità in Samsung MagicINFO 9 Server](https://www.securityinfo.it/2025/05/07/i-criminali-sfruttano-la-vulnerabilita-in-samsung-magicinfo-9-server/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Microsoft Sentinel: arriva l’era degli agenti AI e della difesa predittiva](https://www.securityinfo.it/wp-content/uploads/2025/10/Microsoft-Sentinel_3ott-2025CG-120x85.png)](https://www.securityinfo.it/2025/10/06/microsoft-sentinel-arriva-lera-degli-agenti-ai-e-della-difesa-predittiva/ "Microsoft Sentinel: arriva l’era degli agenti AI e della difesa predittiva")

  [Microsoft Sentinel: arriva l’era...](https://www.securityinfo.it/2025/10/06/microsoft-sentinel-arriva-lera-degli-agenti-ai-e-della-difesa-predittiva/ "Permanent link to Microsoft Sentinel: arriva l’era degli agenti AI e della difesa predittiva")

  Ott 06, 2025  [0](https://www.securityinfo.it/2025/10/06/microsoft-sentinel-arriva-lera-degli-agenti-ai-e-della-difesa-predittiva/#respond)
* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_d4x8rid4x8rid4x8-120x85.png)](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  [Firewall Cisco sotto attacco: una nuova...](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Permanent link to Firewall Cisco sotto...