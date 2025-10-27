---
title: CERT-AGID 24 – 30 agosto: Agenzia delle Entrate e INPS sotto attacco
url: https://www.securityinfo.it/2024/09/02/cert-agid-24-30-agosto-agenzia-delle-entrate-e-inps-sotto-attacco/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-03
fetch_date: 2025-10-06T18:28:03.684364
---

# CERT-AGID 24 – 30 agosto: Agenzia delle Entrate e INPS sotto attacco

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

## CERT-AGID 24 – 30 agosto: Agenzia delle Entrate e INPS sotto attacco

Set 02, 2024  [Stefano Silvestri](https://www.securityinfo.it/author/stefano-silvestri/ "Articoli scritti da Stefano Silvestri")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [Malware](https://www.securityinfo.it/category/news/malware-news/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [Phishing](https://www.securityinfo.it/category/news/phishing/), [Tecnologia](https://www.securityinfo.it/category/news/tecnologia-news/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2024/09/02/cert-agid-24-30-agosto-agenzia-delle-entrate-e-inps-sotto-attacco/#respond)

---

Il **CERT-AGID** ha condotto un’analisi approfondita delle minacce informatiche in Italia nell’ultima settimana, identificando **47 campagne malevole**, di cui 27 specificamente mirate a obiettivi italiani. L’agenzia ha fornito **438 indicatori di compromissione** (IoC) agli enti accreditati.

## I temi più rilevanti della settimana

Questa settimana sono stati identificati **20 temi** sfruttati per veicolare campagne malevole in Italia. Tra i più rilevanti troviamo innanzitutto il tema “**Delivery**“, utilizzato per campagne di phishing italiane, mirate ad Aruba, e per campagne generiche che hanno colpito Wix e altri servizi di web hosting.

Il tema “**Undelivered**” è stato sfruttato per campagne di phishing ai danni di Poste Italiane e per veicolare phishing webmail generici. Il tema “**Documenti**” è stato impiegato in campagne di phishing webmail e per la diffusione dei malware AsyncRat e Vip Keylogger.

“**Pagamenti**” è stato usato in campagne di phishing contro SiteGround e per distribuire il malware Snake Keylogger. Infine, il tema “**Erogazioni**” è stato utilizzato in campagne di phishing italiane contro l’INPS e l’Agenzia delle Entrate. Altri temi sono stati sfruttati per diffondere varie campagne di malware e phishing.

Tra gli eventi di particolare interesse si segnala una **campagna di phishing che ha colpito l’Agenzia delle Entrate**, mirata a sottrarre le credenziali bancarie delle vittime. L’email, simulando un rimborso, invita il destinatario a compilare un modulo per completare l’erogazione.

![](https://www.securityinfo.it/wp-content/uploads/2024/09/CERT-AGID-temi.png)

Fonte: CERT-AGID

Inoltre, sono emerse **nuove campagne di smishing dell’INPS**, finalizzate alla raccolta di dati personali come carta d’identità, codice fiscale, patente, IBAN e busta paga. Maggiori dettagli e Indicatori di Compromissione (IoC) sono disponibili sul [canale Telegram del CERT-AGID](https://t.me/certagid/715).

## Malware della settimana

Durante la settimana sono state individuate **sette famiglie di malware** che hanno colpito l’Italia, con alcune campagne particolarmente rilevanti.

**AgentTesla** ha dato origine a due campagne, una italiana e una generica, entrambe a tema “Pagamenti”, diffuse tramite email contenenti allegati EXE e RAR. **Cryptbot** è stato scoperto in una campagna generica a tema “Adobe”, veicolata tramite email con allegato EXE.

**SnakeKeylogger** è stato rilevato in una campagna italiana, anch’essa a tema “Pagamenti”, diffusa tramite email con allegati EXE. **VipKeylogger** ha interessato una campagna italiana a tema “Documenti”, distribuita tramite email con allegati SCR e ZIP.

**Guloader** è stato individuato in una campagna italiana a tema “Preventivo”, diffusa tramite email contenente un allegato VBS. **Clearfake** ha visto una campagna italiana che sfrutta il tema “Cryptovalute”, con eseguibili diffusi attraverso domini italiani compromessi.

Infine, **AsyncRat** è stato rilevato in una campagna generica a tema “Documenti”, diffusa tramite email con allegato JS.

![](https://www.securityinfo.it/wp-content/uploads/2024/09/CERT-AGID-malware.png)

Fonte: CERT-AGID

## Phishing della settimana

Nell’ultima settimana, il panorama delle minacce informatiche ha visto un’intensa attività di phishing che ha coinvolto **13 marchi diversi**. Tra le numerose campagne osservate, tre in particolare hanno dominato lo scenario per la loro frequenza e intensità.

I servizi **Webmail** sono emersi come uno degli obiettivi principali, probabilmente per la loro capacità di fungere da “finestra” su una moltitudine di informazioni personali e professionali.

Parallelamente, **Aruba** è stato ripetutamente preso di mira, sottolineando l’appetibilità delle credenziali legate ai servizi di hosting per i malintenzionati. Non da meno, l’**INPS** ha registrato un numero significativo di attacchi, riflettendo il valore percepito dei dati personali e finanziari gestiti dall’ente previdenziale italiano.

![](https://www.securityinfo.it/wp-content/uploads/2024/09/CERT-AGID-phishing.png)

Fonte: CERT-AGID

## Formati e canali di diffusione

L’analisi delle campagne malevole della settimana ha messo in luce un panorama meno variegato di altre settimane in termini di tipologie di file dannosi e metodi di diffusione. Sono state infatti individuate “solo” **cinque diverse estensioni di file** utilizzate dai cybercriminali.

I file eseguibili (**EXE**) sono risultati i più comuni, essendo stati impiegati in quattro diverse occasioni. Le altre estensioni, ciascuna rilevata una sola volta, includono **ZIP**, **SCR**, **RAR**, **JAR** e **VBS**, evidenziando così la capacità dei malintenzionati di variare le loro tattiche per aggirare i sistemi di sicurezza.

![](https://www.securityinfo.it/wp-content/uploads/2024/09/CERT-AGID-tipi-file.png)

Fonte: CERT-AGID

Per quanto riguarda i metodi di diffusione, le **email** si sono confermate il canale preferito dagli attaccanti, con 44 campagne distinte che hanno sfruttato questo mezzo. In misura minore, ma comunque rilevante...