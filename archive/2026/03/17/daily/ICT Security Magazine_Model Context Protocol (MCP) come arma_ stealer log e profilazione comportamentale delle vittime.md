---
title: Model Context Protocol (MCP) come arma: stealer log e profilazione comportamentale delle vittime
url: https://www.ictsecuritymagazine.com/articoli/model-context-protocol/
source: ICT Security Magazine
date: 2026-03-17
fetch_date: 2026-03-18T04:22:40.001502
---

# Model Context Protocol (MCP) come arma: stealer log e profilazione comportamentale delle vittime

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
* [Eventi](https://eventi.ictsecuritymagazine.com/)
* [Newsletter](https://www.ictsecuritymagazine.com/newsletter/)

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine1403) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Cyber Crime Conference 2026](https://www.ictsecuritymagazine.com/wp-content/uploads/Cyber-Crime-Conference-2026-1920x278-2.jpg)](https://eventi.ictsecuritymagazine.com/eventi/cyber-crime-conference-2026)

![Model Context Protocol](https://www.ictsecuritymagazine.com/wp-content/uploads/Model-Context-Protocol-.jpeg)

# Model Context Protocol (MCP) come arma: stealer log e profilazione comportamentale delle vittime

A cura di:[Redazione](#molongui-disabled-link)  Ore 17 Marzo 202610 Marzo 2026

Il **Model Context Protocol offensivo** è l’ultima frontiera dell’integrazione tra intelligenza artificiale e cybercrime. Non perché rappresenti una tecnica di attacco inedita, ma perché trasforma radicalmente ciò che accade *dopo* il furto dei dati, nel momento in cui le informazioni rubate cessano di essere materiale grezzo e diventano intelligence operativa strutturata.

Fino a ieri, analizzare milioni di credenziali rubate era un lavoro manuale, lento, costoso. I broker di accesso iniziale su forum come xss.is e exploit.in setacciavano stealer log alla ricerca di credenziali aziendali con la stessa fatica con cui un cercatore d’oro scava nella ghiaia. L’AI ha cambiato le proporzioni di quello sforzo. Ma è il Model Context Protocol – il protocollo aperto creato da Anthropic nel novembre 2024 per connettere i modelli linguistici a strumenti e fonti dati esterni – ad aver fornito l’architettura che ha reso possibile la trasformazione dei dati rubati in profili comportamentali delle vittime. Un passaggio qualitativo che merita un’analisi dedicata.

Nel [Threat Intelligence Report di agosto 2025](https://www.anthropic.com/news/detecting-countering-misuse-aug-2025), Anthropic ha documentato un threat actor operante sul forum russofono xss.is che ha utilizzato MCP e Claude per analizzare stealer log e costruire profili dettagliati delle vittime. L’attore non si limitava a estrarre credenziali: categorizzava i domini visitati, analizzava pattern di navigazione, e assegnava punteggi di priorità per attacchi successivi. È il primo caso documentato pubblicamente di uso offensivo del Model Context Protocol, e le sue implicazioni ridefiniscono il rapporto tra dato rubato e azione criminale.

## Cos’è il Model Context Protocol e perché è al centro di questa analisi

Per comprendere la portata dell’uso offensivo, è necessario chiarire cosa sia MCP e perché la sua architettura si presta a un impiego che i progettisti non avevano previsto.

Il [Model Context Protocol](https://modelcontextprotocol.io/specification/2025-11-25) è uno standard aperto, rilasciato da Anthropic nel novembre 2024 e adottato in meno di un anno da OpenAI, Google DeepMind, Microsoft e centinaia di sviluppatori. Funziona come un adattatore universale tra modelli linguistici e sistemi esterni: database, API, file system, strumenti di sviluppo. L’analogia più utilizzata è quella con l’USB-C: un’unica interfaccia che sostituisce decine di connettori proprietari.

L’architettura è basata su un modello client-server. Il *client MCP* risiede all’interno dell’applicazione AI (Claude Desktop, un agente autonomo, un IDE) e stabilisce connessioni con uno o più *server MCP*, ciascuno dei quali espone risorse, strumenti o prompt in modo standardizzato. Il client interroga i server, riceve dati strutturati, e li utilizza come contesto per le risposte del modello. È un meccanismo elegante e potente: consente a un agente AI di leggere file, interrogare database, eseguire funzioni e coordinare workflow complessi attraverso un’unica interfaccia.

A dicembre 2025, Anthropic ha donato MCP alla [Agentic AI Foundation (AAIF)](https://blog.modelcontextprotocol.io/posts/2025-11-25-first-mcp-anniversary/) sotto la Linux Foundation, sancendone il ruolo di standard *de facto* per l’integrazione degli agenti AI. La specifica 2025-11-25 ha introdotto operazioni asincrone, gestione dell’identità dei server, e un registro comunitario per la scoperta dei server MCP.

Il problema è che questa stessa architettura – progettata per consentire agli agenti AI di accedere a informazioni strutturate e agire su di esse – funziona altrettanto bene quando le “informazioni strutturate” sono credenziali rubate e l'”azione” è la profilazione delle vittime per attacchi mirati.

## Il caso: stealer log come materia prima, MCP come raffineria

Il caso documentato da Anthropic descrive un threat actor che operava su [xss.is](https://www.secureworks.com/research/the-growing-threat-from-infostealers), uno dei forum underground russofoni più attivi nel commercio di credenziali e accessi compromessi. L’attore ha sviluppato un sistema che integra MCP e Claude per processare stealer log su scala, trasformando dati grezzi in intelligence azionabile.

L’operazione si articolava su tre livelli funzionali.

**Ingestione e parsing automatizzato.** Gli stealer log – archivi prodotti da malware come Lumma, RedLine e Raccoon Stealer contenenti credenziali salvate nel browser, cookie di sessione, cronologia di navigazione, dati di compilazione automatica e informazioni sul sistema della vittima – venivano caricati nel sistema attraverso server MCP configurati per leggere e strutturare i dati. L’AI processava ogni log estraendo non solo le credenziali, ma l’intero contesto comportamentale della vittima.

**Categorizzazione dei domini.** L’aspetto più innovativo del sistema era la classificazione automatica dei siti web visitati dalle vittime in categorie semantiche definite dall...