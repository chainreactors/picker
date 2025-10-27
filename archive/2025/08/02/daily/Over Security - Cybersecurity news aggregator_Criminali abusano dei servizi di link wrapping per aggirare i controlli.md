---
title: Criminali abusano dei servizi di link wrapping per aggirare i controlli
url: https://www.securityinfo.it/2025/08/01/criminali-abusano-dei-servizi-di-link-wrapping-per-aggirare-i-controlli/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-02
fetch_date: 2025-10-07T00:51:21.055890
---

# Criminali abusano dei servizi di link wrapping per aggirare i controlli

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

## Criminali abusano dei servizi di link wrapping per aggirare i controlli

Ago 01, 2025  [Redazione](https://www.securityinfo.it/author/redazione/ "Articoli scritti da Redazione")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/08/01/criminali-abusano-dei-servizi-di-link-wrapping-per-aggirare-i-controlli/#respond)

---

**Nuove tecniche sfruttano i servizi di sicurezza email come Proofpoint e Intermedia per camuffare URL dannosi. In crescita anche l’uso di SVG e finti meeting Zoom per carpire credenziali.**

Le campagne di phishing continuano a evolversi, sfruttando non solo tecniche di ingegneria sociale sempre più raffinate, ma anche abuso di strumenti pensati per difendere gli utenti. È il caso delle nuove attività malevole individuate dai ricercatori di Cloudflare che hanno osservato un utilizzo fraudolento dei servizi di *link wrapping* offerti da provider come Proofpoint e Intermedia per veicolare in modo furtivo link pericolosi.

![](https://www.securityinfo.it/wp-content/uploads/2025/08/MatrioskaMalware1-ago-2025CG-1024x683.png)

Il *link wrapping* è una funzionalità di sicurezza che riscrive gli URL contenuti nei messaggi email, reindirizzandoli attraverso un sistema di scansione in grado di bloccare in tempo reale i collegamenti noti come malevoli. Ma, come sottolineano gli esperti, **questo meccanismo si rivela inefficace nel caso in cui l’URL non sia ancora stato identificato come dannoso al momento del click**.

### Phishing sotto mentite spoglie

Gli attacchi osservati nelle ultime settimane, quindi, simulano messaggi di notifica vocale, richieste di visualizzazione documenti su Microsoft Teams o finte comunicazioni di messaggi non letti. In tutti i casi, il destinatario è indotto a cliccare su un link che lo conduce a una **pagina fasulla di login Microsoft 365**, appositamente costruita per sottrarre le credenziali di accesso.

Uno degli elementi più insidiosi è la tecnica chiamata **“multi-tiered redirect abuse”**, in cui i cybercriminali nascondono il link malevolo dietro una catena di reindirizzamenti: prima viene accorciato tramite un servizio come Bitly, poi è ulteriormente mascherato attraverso il wrapping Proofpoint, rendendo particolarmente difficile l’identificazione automatica del contenuto pericoloso.

Ma non si tratta solo di abuso tecnologico. Queste campagne partono spesso da **account email già compromessi**, appartenenti a organizzazioni che utilizzano i suddetti servizi di protezione. In questo modo, qualsiasi link inviato da questi account viene automaticamente “wrappato” dal sistema, **conferendo una falsa sensazione di sicurezza al destinatario**.

### La risposta dei vendor

Proofpoint ha confermato di essere a conoscenza dell’abuso dei propri servizi e ha dichiarato che queste campagne sono individuate tramite **motori di intelligenza artificiale comportamentale** che analizzano i link reindirizzati e bloccano le URL finali dell’intera catena. Una volta rilevata come malevola, **l’intera catena di redirect viene invalidata** anche per gli utenti esterni al servizio di sicurezza.

Il problema, tuttavia, **riguarda anche altri provider** i cui sistemi di riscrittura URL possono essere manipolati in modo analogo, secondo quanto riferito da Proofpoint.

La crescente complessità delle campagne phishing dimostra che **i cybercriminali lavorano costantemente per migliorare i loro strumenti, inclusi quelli usati per attacchi ormai considerati “banali” come il phishing.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [credential harvesting](https://www.securityinfo.it/tag/credential-harvesting/), [cybersecurity](https://www.securityinfo.it/tag/cybersecurity/), [email security](https://www.securityinfo.it/tag/email-security/), [link wrapping](https://www.securityinfo.it/tag/link-wrapping/), [Microsoft 365 phishing](https://www.securityinfo.it/tag/microsoft-365-phishing/), [Phishing](https://www.securityinfo.it/tag/phishing/), [Proofpoint](https://www.securityinfo.it/tag/proofpoint/), [redirect chain](https://www.securityinfo.it/tag/redirect-chain/)

[Secret Blizzard attacca le ambasciate straniere a Mosca tramite gli ISP](https://www.securityinfo.it/2025/08/01/secret-blizzard-attacca-le-ambasciate-straniere-a-mosca-tramite-gli-isp/)
[Un Raspberry Pi per hackerare accedere alla rete bancaria: l'attacco (fallito) di UNC2891](https://www.securityinfo.it/2025/07/31/un-raspberry-pi-per-hackerare-accedere-alla-rete-bancaria-lattacco-di-unc2891/)

---

![](https://secure.gravatar.com/avatar/57d6369d65bf9ebecae351af675ce2fd?s=90&d=mm&r=g)

##### [Redazione](https://www.securityinfo.it/author/redazione/)

##### Articoli correlati

* [![Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-6138007_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/ "Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA")

  [Report Acronis: il ransomware rimane la...](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/ "Permanent link to Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA")

  Set 11, 2025  [0](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/#respond)
* [![Ondata di attacchi brute-force contro le VPN Fortinet, poi FortiManager](https://www.securityinfo.it/w...