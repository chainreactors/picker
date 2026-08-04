---
title: Threat Hunting and Defending #2: concepts, framework, Threat Model (p2)
url: https://roccosicilia.com/2026/08/03/threat-hunting-and-defending-2-concepts-framework-threat-model-p2/
source: Over Security
date: 2026-08-03
fetch_date: 2026-08-04T05:01:10.619869
---

# Threat Hunting and Defending #2: concepts, framework, Threat Model (p2)

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/divulgazione/)
* [Progetti](https://roccosicilia.com/progetti/)
* [Conferenze](https://roccosicilia.com/conferenze/)

[cyber security](https://roccosicilia.com/category/cyber-security/), [hacking](https://roccosicilia.com/category/hacking/), [ita](https://roccosicilia.com/category/ita/), [study with me](https://roccosicilia.com/category/study-with-me/)

## [Threat Hunting and Defending #2: concepts, framework, Threat Model (p2)](https://roccosicilia.com/2026/08/03/threat-hunting-and-defending-2-concepts-framework-threat-model-p2/)

Published by

Rocco Sicilia

on

[3 Agosto 2026](https://roccosicilia.com/2026/08/03/threat-hunting-and-defending-2-concepts-framework-threat-model-p2/)

[![Threat Hunting and Defending #2: concepts, framework, Threat Model (p2)](https://roccosicilia.com/wp-content/uploads/2026/05/gemini-threat-hunting.png)](https://roccosicilia.com/2026/08/03/threat-hunting-and-defending-2-concepts-framework-threat-model-p2/)

Come detto nei precedenti blog-post, la disciplina richiede l’acquisizione di diverse skills che, per essere applicate con efficacia ed in modo efficiente, devono essere affiancate a **strumenti e piattaforme** dedicate.

Il processo di hunting parte dalla formulazione di un’ipotesi relativa a possibili minacce che possono riguardare le infrastrutture che vogliamo proteggere. Per verificare l’ipotesi è necessario accedere alle informazioni ed ai sistemi sotto il proprio controllo e per ovvie ragioni sarebbe impensabile operare direttamente sui singoli host. Solitamente è necessario disporre di strumenti dedicati da utilizzare nel day-by-day per attività come la verifica di logs, eventi ed anomalie al fine di metterle in relazione con TTPs o comportamenti sospetti.

Se trovi utili i contenuti che condivido e vuoi aiutarmi a migliorare il mio progetto di divulgazione iscriviti e abbonati [al mio Substack](https://roccosicilia.substack.com/subscribe).

Solitamente i tools con cui si deve prendere confidenza sono:

* Piattaforme di Threat Intelligence (TIP)
* Security Information and Event Management system (SIEM)
* Soluzioni di Security Orchestration, Automation and Response (SOAR)
* XDR / EDR / NSM / DPL
* Sistemi di Threat Emulation
* vari tools specifici utili all’analisi dei dati

La soluzione che “fa tutto” e copre tutte le casistiche non esiste, solitamente ci si affida a più soluzioni di cui si cerca un certo livello di integrazione. In questo senso si parla per lo più di piattaforme dedicate al threat hunting: un insieme di soluzioni e strumenti che l’hunter utilizza in modo strutturato.

È sicuramente necessario disporre di qualcosa dove archiviare ed organizzare le informazioni, non a caso si citano SIEM e vari software che raccolgono log e telemetria. È sicuramente necessario disporre di strumenti che ci consentano di applicare logiche di machine learning ed analisi del comportamento. Non va dimenticata l’esigenza di automatizzare task e la possibilità di generare report ed analitiche.

Sulle **piattaforme di Cyber Threat Intelligence** (TIP) bisogna dedicarci un po’ di spazio. La Cyber Threat Intelligence genera molte informazioni:

* dati provenienti da attività di OSInt
* ricerche eseguite da analisiti
* collection di dati telemetrici
* informazioni provenienti da studi in collaborazione tra team e ricercatori indipendenti

Le informazioni raccolte consentono di individuare e catalogare gli elementi costitutivi degli attacchi informatici, quelli citati nella *[pyramid of pain](https://roccosicilia.com/2026/07/16/threat-hunting-and-defending-2-frameworks-p1/)* nel precedente post. È una mole di dati enorme che vien continuamente arricchita ed aggiornata e che richiedere una certa gestione dello storico: alcuni elementi sono molto effimeri come IP e HASH, antro sono molto più strutturati come i TTPs.

Solitamente gli analisti utilizzano database di terze parti per accedere a questa enorme mole di informazioni. Ad esempio nel [mio contesto lavorativo](https://www.linkedin.com/posts/roccosicilia_cybersecurity-realismo-share-7483217213320151041-83Z0/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAATK5U0By2qlNbOT_QThQp0s692DGhr_JfU) usiamo molto Cisco Talos e Unit42 come fonti enterprise assieme a molte altre fonti disponibili pubblicamente o parzialmente pubbliche.

Come si può intuire si lavora a più livelli. I ricercatori studiano ed analizzano i nuovi vettori di attacco, nuove tecniche e nuove vulnerabilità. La telemetria generata dai sistemi di detection come IDS, Firewall e EDR consentono di osservare eventuali elementi tecnici relativi ad eventi sospetti. Le piattaforme di Cyber Threat Intelligence pensate per organizzare i dati raccolti, gestire priorità ed in generale supportare l’attività di analisi.

Nel materiale relativo alla certificazione Cisco sono citate alcune piattaforme specifiche per le quali è necessario avere degli accessi con sottoscrizione. In questa occasione le cito e prendo spunto per cercare anche qualche alternativa open.

**ThreatConnect** è una piattaforma che mette a disposizioni, oltre alle fonti dati, integrazioni con sistemi SIEM, SOAR, EDR e NSM. La piattaforma è a pagamento ma il vendor mette a disposizione un altro tool per lo scambio federato di informazioni: [Polarity](https://knowledge.threatconnect.com/docs/polarity). Sembra interessante e me lo appunto per fare dei test.

**Anomali** è un’altra piattaforma di CTI per la condivisione di feeds qualificati, tema che ho spesso discusso quando ho parlato di CTI feeds. Anche questa piattaforma è prettamente ad uso commerciale e si accede tramite subscription ma ho notato che c’è un’interessante [utility per la gestione di feed](https://www.anomali.com/resources/staxx) STIX/TAXII. Anche questa da indagare.

**Recorded Future** probabilmente non ha bisogno di presentazioni, piattaforma nota e molto utilizzata per l’analisi di dati CTI che integra funzionalità tipiche degli LLM per agevolare il lavoro degli analisti. Ho avuto modo di metterci le mani grazie al fatto che è tra i prodotti proposti da [NTS](https://nts.eu/?utm_source=roccosicilia), la company per cui lavoro.

Anche questa piattaforma richiede una subscription per essere utilizzata ma mette a disposizione un set di tools free interessanti che [potete trovare qui](https://www.recordedfuture.com/get-started#free-tools).

**Intel 471** è una piattaforma specializzata nell’analisi e condivisione di informazioni provenienti dal monitoraggio delle Dark Net. Molto interessante ed utile anche prendere visione periodica del blog e dei [post relativi alle nuove minacce](https://www.intel471.com/blog?category=emerging-threats).

**IBM X-Force Exchange** è una piattaforma di condivisione di dati analiticy in relazione a threats e feeds oltre che diversi reports. Molto utile anche per [ricerche realtime di IoC](https://exchange.xforce.ibmcloud.com/).

**MISP** è un progetto open-source per la condivisione di informazioni di cui ho parlato molto in questo [blog](https://roccosicilia.com/?s=MISP) e sul canale [YouTube](https://www.youtube.com/%40roccosicilia/search?query=MISP).

Curiosamente assente, nell’elenco proposto dal materiale di studio della certificazione, **VirusTotal** di Google.

Disporre di dati valutati e commentati da altri analisti da la possibilità di valutare nuovi criteri di ricerca all’interno della nostra base dati di eventi e ci consente di comprendere meglio gli elementi che stiamo osservando.

Ovviamente questi dati vanno condivisi in qualche modo ed esistono standard specifici per la loro formattazione e condivisione. Su questo tema ho avuto modo di sperimentare la complessità della cosa ed i problemi di integrazione che le piattaforme presentano. Di base il formato più diffuso è STIX v2.x (Structured Threat Information Expression), ovvero una struttura dati JSON che consen...