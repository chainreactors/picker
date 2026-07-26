---
title: Security data lake: perché il SIEM si sdoppia tra raccolta e analisi
url: https://www.ictsecuritymagazine.com/articoli/security-data-lake-siem/
source: ICT Security Magazine
date: 2026-07-25
fetch_date: 2026-07-26T05:24:34.987003
---

# Security data lake: perché il SIEM si sdoppia tra raccolta e analisi

[Salta al contenuto](#main)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

* [Home](https://www.ictsecuritymagazine.com/)
* [Articoli](https://www.ictsecuritymagazine.com/argomenti/articoli/)
* RubricheEspandi
  + [Cyber Security](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)
  + [Cyber Crime](https://www.ictsecuritymagazine.com/argomenti/cyber-crime/)
  + [Cyber Risk](https://www.ictsecuritymagazine.com/argomenti/cyber-risk/)
  + [Cyber Law](https://www.ictsecuritymagazine.com/argomenti/cyber-law/)
  + [Digital Forensic](https://www.ictsecuritymagazine.com/argomenti/digital-forensic/)
  + [Digital ID Security](https://www.ictsecuritymagazine.com/argomenti/digital-id-security/)
  + [Business Continuity](https://www.ictsecuritymagazine.com/argomenti/business-continuity/)
  + [Digital Transformation](https://www.ictsecuritymagazine.com/argomenti/digital-transformation/)
  + [Cyber Warfare](https://www.ictsecuritymagazine.com/argomenti/cyber-warfare/)
  + [Ethical Hacking](https://www.ictsecuritymagazine.com/argomenti/ethical-hacking/)
  + [GDPR e Privacy](https://www.ictsecuritymagazine.com/argomenti/gdpr-e-privacy/)
  + [IoT Security](https://www.ictsecuritymagazine.com/argomenti/iot-security/)
  + [Industrial Cyber Security](https://www.ictsecuritymagazine.com/argomenti/industrial-cyber-security/)
  + [Blockchain e Criptovalute](https://www.ictsecuritymagazine.com/argomenti/blockchain-e-criptovalute/)
  + [Intelligenza Artificiale](https://www.ictsecuritymagazine.com/argomenti/intelligenza-artificiale/)
  + [Geopolitica e Cyberspazio](https://www.ictsecuritymagazine.com/argomenti/geopolitica-cyberspazio/)
  + [Prospettive](https://www.ictsecuritymagazine.com/argomenti/prospettive/)
  + [Interviste](https://www.ictsecuritymagazine.com/argomenti/interviste/)
* [Notizie](https://www.ictsecuritymagazine.com/argomenti/notizie/)
* [Pubblicazioni](https://www.ictsecuritymagazine.com/pubblicazioni/)
* [Cybersecurity Video](https://www.ictsecuritymagazine.com/argomenti/cybersecurity-video/)
* [Eventi](https://eventi.ictsecuritymagazine.com/)
* [Newsletter](https://www.ictsecuritymagazine.com/newsletter/)

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Forum ICT Security 2026](https://www.ictsecuritymagazine.com/wp-content/uploads/forum-ict-security-banner-header-2026.jpg)](https://eventi.ictsecuritymagazine.com/eventi/forum-ict-security-2026)

![Security data lake SIEM](https://www.ictsecuritymagazine.com/wp-content/uploads/Security-data-lake-SIEM.png)

# Security data lake: perché il SIEM si sdoppia tra raccolta e analisi

A cura di:[Redazione](#molongui-disabled-link)  Ore 25 Luglio 202617 Luglio 2026

Il security data lake è la risposta a un problema che i responsabili della sicurezza conoscono bene ma di cui si parla poco: raccogliere e conservare i dati necessari a rilevare un attacco è diventato così costoso da spingere molte organizzazioni a rinunciarvi, cioè a scartare log che sarebbero serviti proprio nel momento peggiore. Il *SIEM*, il sistema che da vent’anni sta al centro del centro operativo di sicurezza, è nato in un’epoca di volumi di dati incomparabilmente più piccoli, e il suo modello economico, che fa pagare in proporzione a quanto si immette, mal si adatta a un mondo in cui i log crescono più in fretta dei budget. Da qui una trasformazione silenziosa ma profonda: la piattaforma non scompare, ma si scompone.

L’idea di fondo è separare due cose che il *SIEM* teneva insieme: la conservazione dei dati e la loro analisi. Da un lato uno strato di raccolta capace di trattenere tutto a costi bassi; dall’altro uno strato analitico che interroga quei dati quando servono. È la stessa logica che ha ridisegnato l’analisi dei dati aziendali dieci anni fa, arrivata ora, con ritardo, alla sicurezza. E non è una moda da fornitori: è la conseguenza aritmetica di un costo per gigabyte che, moltiplicato per i volumi odierni, non regge più.

## Perché il SIEM tradizionale non regge più i volumi

Il nodo è il modello di prezzo. La maggior parte dei *SIEM* fattura in base al volume immesso, così ogni fonte aggiunta, ogni picco di traffico, ogni nuovo sistema da monitorare fa salire il conto. La reazione prevedibile dei team, sotto pressione di budget, è filtrare all’origine: non inviare al *SIEM* i log ritenuti meno critici, campionarli, o conservarli per pochi giorni. Ogni scelta di questo tipo è un risparmio immediato e un punto cieco differito, perché la fonte scartata è spesso quella che, a incidente avvenuto, avrebbe raccontato come l’attaccante è entrato e cosa ha toccato.

È il motivo per cui il problema economico è, in realtà, un problema di sicurezza. Quando l’analista deve scegliere quali dati permettersi invece di quali dati servono, la copertura di rilevamento smette di essere una decisione tecnica e diventa una voce di spesa. La crescita dei volumi, alimentata da *cloud*, identità, *endpoint* e ambienti ibridi, ha reso questa tensione insostenibile, e ha spinto il mercato a cercare un’architettura che disaccoppi il costo della conservazione da quello dell’analisi.

## Che cos’è un security data lake

Un *security data lake* è un archivio centralizzato che raccoglie i dati di sicurezza, strutturati e non, su *storage* a oggetti a basso costo, tenendoli disponibili per l’interrogazione senza il sovrapprezzo di un’indicizzazione permanente. La differenza rispetto al *SIEM* classico è che conservare non implica più pagare per analizzare in continuazione: i dati restano lì, economici, e la potenza di calcolo viene applicata quando serve, sui dati che servono. Questo permette di trattenere anni di storico, invece di giorni, e di condurre indagini retrospettive che con la ritenzione ridotta imposta dai costi sarebbero impossibili.

La contropartita è il *tiering*, cioè la distinzione tra dati “caldi”, subito interrogabili per il [rilevamento in tempo reale](https://www.ictsecuritymagazine.com/articoli/intrusion-detection/), e dati “freddi”, conservati a lungo e richiamabili con qualche attesa in più per le indagini e la conformità. Formati aperti e *storage* di proprietà dell’organizzazione riducono inoltre il rischio di *lock-in*, il vincolo che a lungo ha reso difficile lasciare un fornitore di *SIEM* una volta che ci si erano riversati dentro tutti i log. È un cambio di rapporti di forza: i dati tornano a essere dell’azienda, e la piattaforma di analisi diventa sostituibile.

## La security data pipeline: filtrare prima di pagare

Tra le fonti e lo strato di analisi si è inserito un terzo componente, la [security data pipeline](https://softwareanalyst.substack.com/p/the-convergence-of-siems-and-data), che raccoglie i dati, li normalizza, li arricchisce e decide dove instradarli. La sua funzione economica è semplice e potente: ridurre ciò che arriva al *SIEM* costoso, mandando il resto al *data lake* a basso costo, senza perdere nulla. È la promessa che ha reso questo strato l’oggetto delle acquisizioni che hanno riscritto il mercato tra il 2025 e il 2026: CrowdStrike ha rilevato [Onum](https://www.crowdstrike.com/en-us/press-releases/crowdstrike-to-acquire-onum/) per 290 milioni di dollari, SentinelOne ha rilevato [Observo AI](https://www.sentinelone.com/press/sentinelone-to-acquire-observo-ai-to-revolutionize-siem-and-security-operations/) per 225, e soprattutto Palo Alto Networks si è presa Chronosphere, una piattaforma di *observability* che porta con sé anche capacità di *telemetry pipeline*: l’operazione, annunciata a novembre 2025 per 3,35 miliardi e [perfezionata il 29 gennaio 2026](https://www.paloaltonetworks.com/company...