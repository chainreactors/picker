---
title: Personalizzare per proteggere meglio
url: https://www.certego.net/blog/detection-engineering-perche-le-regole-di-detection-standard-non-possono-bastare/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-30
fetch_date: 2025-10-06T23:53:57.988277
---

# Personalizzare per proteggere meglio

* Services

  [Managed Detection & Response](/services/managed-detection-and-response/)[Cyber Threat Intelligence](/services/cyber-threat-intelligence/)[Rapid Incident Response](/services/rapid-incident-response/)
* Platform

  [SecOps Platform](/platform/security-operations-platform/)[Detection Modules](/platform/detection-modules/)[Response Modules](/platform/response-modules/)[Threat Intelligence Modules](/platform/threat-intelligence-modules/)
* Resources

  [Blog](/blog/)[Events & Webinars](/resources/events-and-webinars/)[Datasheets & Whitepapers](/resources/datasheets-and-whitepapers/)
* Company

  [About Us](/company/about-us/)[SecOps Team](/company/security-operations-team/)[News](/company/news/)[Partners](/company/partners/)[Careers](/company/careers/)[Contact Us](/company/contact-us/)
* + [ð®ð¹](/it/blog/detection-engineering-perche-le-regole-di-detection-standard-non-possono-bastare/)

[Are you under attack?](/have-you-been-breached/)

July 29, 2025

## Personalizzare per proteggere meglio

#### PerchÃ© le regole di detection standard non possono bastare

![](data:image/svg+xml;charset=utf-8...)

![image](/static/c1339a08903bd0a4fe41fbea037f8f51/bd885/Inside%20Detection%20Engineer%201%20Certego.png)![image](/static/c1339a08903bd0a4fe41fbea037f8f51/bd885/Inside%20Detection%20Engineer%201%20Certego.png)

## L'importanza della Detection Engineering in un mondo di minacce dinamiche e in continua evoluzione

Le minacce informatiche oggi non sono piÃ¹ eventi isolati o facili da riconoscere. Al contrario, sono diventate sempre piÃ¹ sofisticate, subdole e capaci di adattarsi ai contesti piÃ¹ diversi. In uno scenario tanto mutevole, affidarsi esclusivamente a regole predefinite e generaliste per individuare attivitÃ  malevole si rivela spesso insufficiente e rischia di lasciare aperti varchi importanti nella superficie d'attacco.
Sebbene le regole standard offerte da molte soluzioni EDR rappresentino un buon punto di partenza, sono pensate per operare in contesti molto eterogenei e, di conseguenza, risultano inevitabilmente generiche. Le differenze organizzative, architetturali e persino culturali tra le aziende rendono questi rilevamenti una base iniziale fondamentale, ma che necessita di essere potenziata e adattata per garantire una protezione realmente efficace.

Inoltre, in alcuni casi potrebbero non intercettare tecniche avanzate o comportamenti anomali specifici del contesto aziendale. I threat actor piÃ¹ esperti lo sanno bene: sfruttano queste limitazioni con approcci mirati, evasivi e meno convenzionali.
Ã qui che entra in gioco la Detection Engineering, che consente di:

* **Creare rilevamenti personalizzati** sulla base delle specifiche esigenze infrastrutturali del cliente, tenendo conto di architetture, tecnologie e rischi peculiari;
* **Integrare fonti di log specifiche**, anche non standardizzate;
* **Riconoscere anche segnali deboli**, ma contestualizzati e significativi;
* **Automatizzare correlazioni complesse** tra eventi che hanno senso solo in quello specifico ambiente.

**Non si tratta solo di scrivere regole, ma di progettare rilevamenti su misura che riflettono la specificitÃ  dellâambiente tecnologico, organizzativo e operativo di ciascuna azienda. In un servizio MDR (Managed Detection and Response), questo approccio Ã¨ fondamentale per intercettare minacce che sfuggono ai radar delle soluzioni standard**.

## Ogni infrastruttura Ã¨ diversa: servono regole di detection uniche

Ogni azienda ha un proprio profilo di rischio, un proprio stack tecnologico e flussi operativi distinti. Una regola pensata per un ambiente sanitario, molto probabilmente non potrÃ  avere la stessa efficacia in un contesto manifatturiero, e viceversa, proprio a causa delle differenze infrastrutturali.
Anche aziende dello stesso settore possono esporre superfici d'attacco differenti a seconda degli strumenti adottati, delle configurazioni locali o della maturitÃ  dei processi IT. Ã qui che la Detection Engineering dimostra il proprio valore, permettendo di modellare regole che riflettano fedelmente il contesto operativo.

## Il ruolo della Detection Engineering in un servizio MDR

In Certego, il team di Detection Engineering collabora ogni giorno con le unitÃ  di Incident Response e Threat Intelligence per trasformare evidenze tecniche e indicatori emersi sul campo in regole di rilevamento aggiornate ed efficaci. Ogni regola Ã¨ progettata su misura per il contesto in cui verrÃ  applicata, con lâobiettivo di:

* **Estendere le capacitÃ  degli strumenti EDR**, andando oltre i rilevamenti standard;
* **Abilitare la visibilitÃ  su tecniche evasive o poco documentate**, spesso non tracciate dalle regole predefinite;
* **Aumentare la precisione, riducendo i falsi positivi**, grazie a una logiche di correlazione piÃ¹ consapevoli.

## Un caso reale
Durante un'attivitÃ  di Incident Response su una compromissione in corso, il team di Security Operations di Certego ha analizzato un attacco in cui un attore malevolo era riuscito a ottenere un accesso iniziale sfruttando credenziali valide e un'applicazione esposta su internet. Dopo l'accesso iniziale, l'attaccante ha avviato una serie di movimenti laterali utilizzando strumenti legittimi come PsExec e WMI per spostarsi all'interno dell'infrastruttura, mantenendo un basso profilo e confondendosi tra le attivitÃ  legittime.
Durante la fase di post-analisi, sono stati raccolti indicatori specifici che includevano:

* Sequenze anomale di autenticazioni RDP e SMB tra host non correlati tra loro;
* Esecuzione di servizi remoti tramite sc.exe e wmic all'interno di subnet inconsuete;
* Utilizzo di comandi Powershell offuscati, con payload scaricati da URL temporanei.

Partendo da questi indicatori, il team di Detection Engineering ha progettato una regola personalizzata in grado di correlare questi pattern su ambienti simili, rilevando:

* Tentativi di movimento laterale basati su tool nativi;
* Anomalie nel comportamento degli endpoint rispetto alla baseline abituale;
* Indicatori di persistenza remota poco rumorosi ma altamente sospetti.

La regola Ã¨ stata poi adattata e distribuita selettivamente nei contesti infrastrutturali affini, offrendo una protezione mirata contro attacchi stealth che sfruttano strumenti leciti per scopi illeciti.

## Detection su misura: benefici tangibili

La personalizzazione non Ã¨ un vezzo, ma un vantaggio strategico concreto per migliorare:

* **Accuratezza degli alert**: le regole sono adattate al contesto reale dellâazienda;
* **Efficienza del SOC**: meno rumore equivale a maggiore concentrazione sui segnali reali;
* **Tempo di risposta**: lâidentificazione precoce accelera la containment e lâanalisi.

Ogni incidente gestito contribuisce ad arricchire il set di detection con nuovi elementi contestuali, dando vita a un ciclo virtuoso di apprendimento.

## Certego Halo: visibilitÃ  totale e detection personalizzata

Come abbiamo visto, le soluzioni EDR tradizionali sono spesso progettate per soddisfare esigenze standard e operare in modalitÃ  black-box: offrono regole predefinite, ma impediscono lâaccesso diretto ai dati grezzi e alle logiche di rilevamento. Questo approccio limita profondamente la capacitÃ  di analisi da parte di analisti esperti, in particolare dei power user che necessitano di un controllo avanzato sul processo di detection.
Per risolvere queste limitazioni, Certego ha sviluppato Halo, una piattaforma di Detection Engineering integrata nell'ecosistema applicativo proprietario che consente di raccogliere e arricchire lâintera telemetria degli endpoint, superando cosÃ¬ le barriere imposte dalle soluzioni tradizionali. Con Halo, i team SOC possono:

* **Accedere alla telemetria completa degli endpoint** per effettuare analisi piÃ¹ approfondite;
* **Correlare eventi complessi in modo flessibile**, aggregando segnali deboli in un unico alert rilevante;
* **Sviluppare regole di detection personalizzate**, liberandosi dai vincoli delle logiche chiuse;
*...