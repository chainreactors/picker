---
title: APT41, il gruppo cinese amplia il raggio d’azione in Africa
url: https://www.securityinfo.it/2025/07/22/apt41-il-gruppo-cinese-amplia-il-raggio-dazione-in-africa/?utm_source=rss&utm_medium=rss&utm_campaign=apt41-il-gruppo-cinese-amplia-il-raggio-dazione-in-africa
source: Securityinfo.it
date: 2025-07-23
fetch_date: 2025-10-06T23:51:20.918616
---

# APT41, il gruppo cinese amplia il raggio d’azione in Africa

Aggiornamenti recenti Ottobre 6th, 2025 5:03 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Impennata delle scansioni dei portali di login di Palo Alto Networks: +500%](https://www.securityinfo.it/2025/10/06/impennata-delle-scansioni-dei-portali-di-login-di-palo-alto-networks-500/)
* [Microsoft Sentinel: arriva l’era degli agenti AI e della difesa predittiva](https://www.securityinfo.it/2025/10/06/microsoft-sentinel-arriva-lera-degli-agenti-ai-e-della-difesa-predittiva/)
* [CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)

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

## APT41, il gruppo cinese amplia il raggio d’azione in Africa

Lug 22, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/07/22/apt41-il-gruppo-cinese-amplia-il-raggio-dazione-in-africa/#respond)

---

Il gruppo cinese **APT41**, [già noto](https://www.securityinfo.it/2022/03/10/enti-governativi-usa-colpiti-da-apt41/) per attività di cyberspionaggio contro industrie di vari settori in oltre 40 Paesi, ha ampliato ulteriormente il proprio raggio d’azione per **colpire infrastrutture IT governative in Africa.**

A scoprire gli attacchi è stato il team MDR di Kaspersky: come [riportato](https://securelist.com/apt41-in-africa/116986/) sul blog della compagnia, i ricercatori hanno individuato delle attività sospette su diversi sistemi dell’organizzazione. Il gruppo ha sfruttato **servizi interni, indirizzi IP e server proxy hardcoded nel malware** per eseguire operazioni di cyberspionaggio.

Dopo una fase iniziale di rilevamento e analisi dei processi in esecuzione, il gruppo ha distribuito sui sistemi strumenti per la comunicazione C2; tra essi spicca **Cobalt Strike**, usato per raccogliere le informazioni sensibili.

![APT41](https://www.securityinfo.it/wp-content/uploads/2025/07/hacker-8003393_1920.jpg)

Per ottenere dati dagli host colpiti, gli attaccanti hanno usato anche una serie di **tool e stealer automatizzati** quali Pillager, Checkout, RawCopy e Mimikatz. Tra i dati sottratti figurano credenziali salvate in browser e database, codice sorgente di progetti, screenshot, email, la lista di software installati nel dispositivo e l’output dei comandi *systeminfo*e *tasklist*.

Durante l’analisi il team di Kaspersky ha inoltre individuato un server SharePoint compromesso che veniva usato dal gruppo sempre allo scopo di comunicare con l’infrastruttura. Gli attaccanti usavano il server per **distribuire due trojan, agents.exe e agentx.exe**, i quali gli permettevano di eseguire comandi sui sistemi tramite una web shell chiamata CommandHandler.aspx.

“***Gli attaccanti si adattano rapidamente all’infrastruttura del loro obiettivo**, aggiornando i loro strumenti dannosi per tener conto di caratteristiche specifiche*” ha commentato il team di Kaspersky. “*Possono anche sfruttare i servizi interni per la comunicazione C2 e l’esfiltrazione dei dati*“.

Il team MDR della compagnia è riuscito a estromettere APT41 dai sistemi colpiti, ma l’impatto è stato significativo. Kaspersky riporta che alcune parti dell’infrastruttura non erano collegate ai sistemi di monitoraggio, quindi non è stato semplice analizzare fin da subito ciò che stava accadendo.

Kaspersky ricorda di **mantenere sempre la massima visibilità sull’infrastruttura IT** e utilizzare tool di sicurezza in grado di bloccare automaticamente attività malevole o sospette. È inoltre fondamentale evitare di garantire privilegi troppo elevati agli account, soprattutto quelli che vengono usati su tutti o molti host dell’infrastruttura.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [APT41](https://www.securityinfo.it/tag/apt41/), [C2](https://www.securityinfo.it/tag/c2/), [CobaltStrike](https://www.securityinfo.it/tag/cobaltstrike/), [cyberspionaggio](https://www.securityinfo.it/tag/cyberspionaggio/), [esfiltrazione dati](https://www.securityinfo.it/tag/esfiltrazione-dati/), [Trojan](https://www.securityinfo.it/tag/trojan/)

[Attacco ToolShell a Sharepoint: i criminali hanno iniziato usarlo almeno dal 7 luglio](https://www.securityinfo.it/2025/07/22/attacco-toolshell-a-sharepoint-i-criminali-hanno-iniziato-usarlo-almeno-dal-7-luglio/)
[PoisonSeed è riuscito ad aggirare la protezione FIDO](https://www.securityinfo.it/2025/07/21/poisonseed-e-riuscito-ad-aggirare-la-protezione-fido/)

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
* [![File Linux usati per furto di dati e spionaggio: la campagna di APT36](https://www.se...