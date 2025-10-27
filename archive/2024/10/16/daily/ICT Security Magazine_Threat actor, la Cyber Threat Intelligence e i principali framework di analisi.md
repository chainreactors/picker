---
title: Threat actor, la Cyber Threat Intelligence e i principali framework di analisi
url: https://www.ictsecuritymagazine.com/articoli/threat-actor-intelligence/
source: ICT Security Magazine
date: 2024-10-16
fetch_date: 2025-10-06T18:56:51.557543
---

# Threat actor, la Cyber Threat Intelligence e i principali framework di analisi

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
  + [Interviste](https://www.ictsecuritymagazine.com/argomenti/interviste/)
* [Notizie](https://www.ictsecuritymagazine.com/argomenti/notizie/)
* [Pubblicazioni](https://www.ictsecuritymagazine.com/pubblicazioni/)
* [Cybersecurity Video](https://www.ictsecuritymagazine.com/argomenti/cybersecurity-video/)
* [Eventi](https://www.ictsecuritymagazine.com/eventi/)
* [Newsletter](https://www.ictsecuritymagazine.com/newsletter/)

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine1403) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Forum ICT Security 2025](https://www.ictsecuritymagazine.com/wp-content/uploads/banner-header-2025.jpg)](https://www.ictsecuritymagazine.com/eventi/forumictsecurity2025)

![Threat actor, Cyber Threat Intelligence e framework di analisi](https://www.ictsecuritymagazine.com/wp-content/uploads/Cyber-Threat-Intelligence-1.jpg)

# Threat actor, la Cyber Threat Intelligence e i principali framework di analisi

A cura di:[Achille Pierre Paliotta](#molongui-disabled-link)  Ore 15 Ottobre 2024

> «*The great accomplishments of today’s intelligence brotherhood have* *been of two sorts: collection and analysis*»
>  Sherman Kent [1903-1986], *Strategic Intelligence for American World Policy*, 1965, xv-xvi

### Introduzione

Come già messo in risalto in un precedente Quaderno SOCINT, l’essenza centrale di un’attività di *Cyber Threat Intelligence* (CTI) è costituita da dati e informazioni raccolte da una serie di fonti sugli attacchi attuali o potenziali contro un’organizzazione, da parte di attori malevoli[[1]](#_ftn1).

Più in dettaglio, la CTI è costituita da dati e informazioni che vengono raccolti, elaborati e analizzati per comprendere le motivazioni, gli obiettivi e i comportamenti di attacco di un agente portatore di una minaccia (*Threat actor,* TA).

La CTI è importante per i seguenti motivi:

1. apporta nuove informazioni su attività malevoli che sono celate, consentendo ai team di sicurezza di approntare delle risposte basate su decisioni adeguate;
2. svela i motivi degli avversari così come le loro tattiche, tecniche e procedure (TTP) nonché gli indicatori di compromissione (IOC);
3. aiuta a comprendere meglio il processo decisionale dell’autore della minaccia;
4. responsabilizza e potenzia gli *stakeholder* aziendali, come Consigli di amministrazione, *Chief information security officer* (CISO), *Chief information officer* (CIO) e *Chief technology officer* (CTO) così da mitigare il rischio, diventare più efficienti e prendere decisioni più rapide basate sui dati disponibili. In questo senso, lo scopo principale della CTI è rendere consapevoli le organizzazioni dei vari rischi che devono affrontare a causa di minacce esterne, come le minacce *zero-day* e le minacce persistenti avanzate (*Advanced persistent threat*, APT).

Tra i vari strumenti che sono stati messi a punto, nel corso degli ultimi decenni, al fine di mitigare tali minacce vi sono senz’altro i framework per l’identificazione dei TA, importanti poiché forniscono un modello comune per analizzare e categorizzare le minacce informatiche, rendendo più facile per le organizzazioni comprendere e rispondere agli attacchi. Inoltre, i framework forniscono un linguaggio comune per la collaborazione e la condivisione delle informazioni tra le diverse organizzazioni e le forze dell’ordine, il che a sua volta migliora la capacità di identificare e neutralizzare i TA.

Tutto ciò si inserisce all’interno di un risoluto e ultradecennale processo di standardizzazione che la comunità CTI ha inteso portare avanti per raggiungere i fini anzidetti e che è consistita, sostanzialmente, di tre fasi principali, qui necessariamente succinte:

1. identificare i principali elementi dei dati, quali informazioni sul tipo di minaccia, sulla gravità della stessa, sulla fonte della minaccia, sull’impatto potenziale, ecc.;
2. sviluppare un modello di dati mediante la creazione di una tassonomia o di un’ontologia per classificare i diversi tipi di minacce e i loro attributi;
3. definire i formati dei dati che verranno utilizzati, i più importanti dei quali possono essere considerati i framework STIX (*Structured Threat Information eXpression*) e TAXII (*Trusted Automated eXchange of Indicator Information*).

STIX è un linguaggio standardizzato per descrivere le informazioni sulle minacce informatiche sviluppato da MITRE Corporation nel 2012 ed è arrivato, ad oggi, alla versione 2.0, progettata per essere più flessibile, estensibile e facile da usare rispetto al suo predecessore 1.0. STIX 2.0 include una serie di nuove funzionalità e miglioramenti, tra cui: un’architettura più modulare che consente una più facile personalizzazione ed estensione; un modello di dati semplificato che facilita la rappresentazione di informazioni complesse sulle minacce; un supporto migliorato per gli indicatori di compromissione (IOC) e altri tipi di dati sulle minacce; un migliore supporto per la condivisione e la collaborazione tra le diverse organizzazioni utilizzatrici.

TAXII è, invece, un protocollo che consente lo scambio di informazioni sulle minacce informatiche tra diverse organizzazioni. Lo standard TAXII specifica i dettagli tecnici per lo scambio di informazioni quali il formato dei dati, i protocolli per la loro trasmissione e le misure di sicurezza che devono essere adottate per proteggere le informazioni in transito. Sono ricomprese in TAXII anche delle linee guida per l’implementazione dello stesso in diversi ambienti quali i sistemi di rilevamento delle intrusioni (IDS) e i sistemi di gestione delle informazioni e degli eventi di sicurezza (SIEM).

Lo sforzo di sintesi che viene compiuto in questo testo è, dunque, finalizzato a dar conto dei framework più importanti per l’identificazione dei *threat actors* nella cybersecurity, considerando che non esiste un elenco esaustivo di questi ma che i più influenti e consigliati possono essere considerati i seguenti:

1. *Intrusion Lifecycle Model*;
2. *Indicator Types Model*;
3. *Attribut...