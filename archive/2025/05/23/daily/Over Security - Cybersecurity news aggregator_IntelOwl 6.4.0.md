---
title: IntelOwl 6.4.0
url: https://www.certego.net/blog/intelowl-threat-intelligence-investigation-platform-nuova-release-2025/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-23
fetch_date: 2025-10-06T22:30:40.419848
---

# IntelOwl 6.4.0

* Services

  [Managed Detection & Response](/services/managed-detection-and-response/)[Cyber Threat Intelligence](/services/cyber-threat-intelligence/)[Rapid Incident Response](/services/rapid-incident-response/)
* Platform

  [SecOps Platform](/platform/security-operations-platform/)[Detection Modules](/platform/detection-modules/)[Response Modules](/platform/response-modules/)[Threat Intelligence Modules](/platform/threat-intelligence-modules/)
* Resources

  [Blog](/blog/)[Events & Webinars](/resources/events-and-webinars/)[Datasheets & Whitepapers](/resources/datasheets-and-whitepapers/)
* Company

  [About Us](/company/about-us/)[SecOps Team](/company/security-operations-team/)[News](/company/news/)[Partners](/company/partners/)[Careers](/company/careers/)[Contact Us](/company/contact-us/)
* + [ð®ð¹](/it/blog/intelowl-threat-intelligence-investigation-platform-nuova-release-2025/)

[Are you under attack?](/have-you-been-breached/)

May 22, 2025

## IntelOwl 6.4.0

#### Nuova release della piattaforma di Threat Intelligence Investigation

![](data:image/svg+xml;charset=utf-8...)

![image](/static/846e4d00b45db4ee8fb7abec95fdc4cb/bd885/Cover%20Certego%20IntelOwl%20v6.4.png)![image](/static/846e4d00b45db4ee8fb7abec95fdc4cb/bd885/Cover%20Certego%20IntelOwl%20v6.4.png)

[Ã disponibile la nuova release 6.4.0 di IntelOwl](https://github.com/intelowlproject/IntelOwl/releases/tag/v6.4.0), frutto di un percorso di evoluzione continua volto a rendere sempre piÃ¹ efficaci, strutturate e integrate le attivitÃ  di Threat Intelligence e le operazioni del Security Operation Team di Certego.

Questa versione introduce nuove funzionalitÃ  chiave che rappresentano un importante passo avanti nella capacitÃ  della piattaforma di supportare gli analisti nella valutazione, correlazione e gestione degli indicatori di compromissione.

## 1. Analyzable: riferimento unico per ogni oggetto analizzato

Con la versione 6.4.0, la funzionalitÃ  Analyzable introduce una rappresentazione unificata dellâoggetto analizzato â che si tratti di un osservabile (come un IP, dominio, hash) o di un campione (sample).
Ora, ogni job di analisi Ã¨ direttamente associato al relativo Analyzable, rendendo possibile collegare piÃ¹ report di analisi a un unico oggetto.
Questo approccio **consente una visione piÃ¹ completa e strutturata della cronologia analitica di un osservabile, semplificando la consultazione dei risultati e la loro correlazione nel tempo**.

## 2. Data Models: standardizzazione avanzata per lâinteroperabilitÃ  degli output

Ogni analyzer in IntelOwl produce risultati strutturalmente diversi, riflettendo le specificitÃ  degli strumenti e delle tecniche utilizzate. Sebbene questa flessibilitÃ  sia necessaria, confrontare in modo sistematico unâinformazione ricorrente tra piÃ¹ analyzer poteva richiedere unâanalisi manuale e frammentata da parte dellâutente.
La versione 6.4.0 introduce il nuovo sistema dei Data Models, che consente di mappare i dati rilevanti generati dagli analyzer allâinterno di uno schema strutturato e condiviso.
Questo approccio **riduce la necessitÃ  di interpretazioni manuali e favorisce una lettura piÃ¹ rapida, omogenea e comparabile delle informazioni critiche**.

[![Certego MDR Threat Research](/static/fc8b3fdec270daa11a484b70767e6f6c/71c1d/Certego-MDR-Threat-Research.png)](https://www.certego.net/blog/threat-research-la-chiave-per-un-servizio-mdr-proattivo/)

## 3. User Events: valutazioni personalizzate a supporto dellâanalisi

La versione 6.4.0 introduce un aggiornamento che consente agli utenti di associare manualmente valutazioni e osservazioni personalizzate a un analyzable, tramite gli User Events.
Questa funzionalitÃ  permette, ad esempio, di registrare che un dominio analizzato (es. google.com) Ã¨ ritenuto lecito con un elevato livello di confidenza. Le annotazioni vengono cosÃ¬ strutturate in modo coerente allâinterno della piattaforma, arricchendo il contesto analitico con informazioni qualitative generate dagli analisti stessi. In questo modo, IntelOwl **integra la conoscenza umana con i dati tecnici, favorendo una gestione collaborativa e condivisa degli osservabili**.

## 4. Engine: sintesi automatica tra dati tecnici e input umani

LâEngine aggiornato ha il compito di combinare in modo intelligente i dati provenienti dagli analyzer con i contributi degli analisti (tramite User Events), fornendo una valutazione aggregata per ogni job. Il risultato Ã¨ unâ**indicazione piÃ¹ completa, utile per indirizzare rapidamente lâattenzione sugli elementi piÃ¹ rilevanti**.

IntelOwl Ã¨ integrata nativamente con la piattaforma di Unified Security Operations PanOptikon, costituendo uno strumento fondamentale per gli analisti di Certego.
Grazie a questa integrazione, gli analisti possono contare su un sistema di Threat Intelligence ad alta precisione e affidabilitÃ , che consente di:

* monitorare e validare in tempo reale gli indicatori di compromissione (IOC);
* svolgere analisi approfondite su domini, file, IP, hash e altri osservabili;
* correlare evidenze tecniche e conoscenze umane in un unico flusso operativo integrato.

IntelOwl 6.4.0 potenzia ulteriormente la capacitÃ  di Certego di rispondere con tempestivitÃ  e precisione agli attacchi informatici, rafforzando il presidio continuo contro le minacce avanzate.

[![Cybersecurity trasporti](/static/69e3bd8479618e23f080a5653400daf8/71c1d/Cybersecurity%20trasporti.png)](https://www.certego.net/blog/cybersecurity-nei-trasporti-una-sfida-che-corre-veloce/)

Â Pier Giorgio Bergonzi, Product Marketing

## Subscribe

#### Sign up to our newsletter

[ ] Clicking Submit, I agree to the use of my personal data in accordance with [Certego Privacy Policy](/privacy/)Â  for the purpose sub. 2 paragraph âPurposes of the Data processing and legal basisâ.Â Certego will not sell, trade, lease, or rent your personal data to third parties.

##### Services

* [Managed Detection & Response](/services/managed-detection-and-response/)
* [Cyber Threat Intelligence](/services/cyber-threat-intelligence/)
* [Rapid Incident Response](/services/rapid-incident-response/)

##### Platform

* [SecOps Platform](/platform/security-operations-platform/)
* [Detection Modules](/platform/detection-modules/)
* [Response Modules](/platform/response-modules/)
* [Threat Intelligence Modules](/platform/threat-intelligence-modules/)

##### Resources

* [Blog](/blog/)
* [Events & Webinars](/resources/events-and-webinars/)
* [Datasheets & Whitepapers](/resources/datasheets-and-whitepapers/)

##### Company

* [About Us](/company/about-us/)
* [SecOps Team](/company/security-operations-team/)
* [News](/company/news/)
* [Partners](/company/partners/)
* [Careers](/company/careers/)
* [Contact Us](/company/contact-us/)

---

Copyright Â© 2025 www.certego.net

Certego S.R.L.