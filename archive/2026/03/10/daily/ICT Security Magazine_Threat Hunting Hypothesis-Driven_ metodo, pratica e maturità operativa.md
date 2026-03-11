---
title: Threat Hunting Hypothesis-Driven: metodo, pratica e maturità operativa
url: https://www.ictsecuritymagazine.com/articoli/threat-hunting-hypothesis-driven/
source: ICT Security Magazine
date: 2026-03-10
fetch_date: 2026-03-11T04:05:26.742040
---

# Threat Hunting Hypothesis-Driven: metodo, pratica e maturità operativa

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

![Threat Hunting Hypothesis-Driven](https://www.ictsecuritymagazine.com/wp-content/uploads/freepik__a-cinematic-cybersecurity-scene-representing-hypot__63905.jpeg)

# Threat Hunting Hypothesis-Driven: metodo, pratica e maturità operativa

A cura di:[Nicolas Fasolo](#molongui-disabled-link)  Ore 10 Marzo 20265 Marzo 2026

Negli ultimi tempi il threat hunting “hypothesis-driven” è diventato la forma più evoluta di difesa proattiva.

Non si tratta semplicemente di cercare indicatori nei log o di fare ricerche casuali in un SIEM, l’idea di fondo è proprio diversa: partire da un’ipotesi concreta su come potrebbe agire un avversario e verificare, in modo strutturato, se nei nostri sistemi esistano tracce compatibili con quel comportamento.

In questo approccio il Threat hunter non aspetta un alert dato da una console. Non reagisce: anticipa.

Parte da una domanda investigativa costruita sulla base di intelligence, conoscenza delle TTP di tutti i Threat Actor (noti e non noti) e la reale comprensione dell’infrastruttura aziendale. L’obiettivo non è trovare “qualcosa di strano”, ma cercare evidenze coerenti con uno scenario d’attacco plausibile, anche se mai ancora intercettato dai meccanismi di detection tradizionali.

## Threat Hunting Hypothesis-Driven: l’evoluzione dell’hunting proattivo

La maturità di un programma di threat hunting non si costruisce in un giorno, è un percorso evolutivo piuttosto chiaro (e prolungato).

All’inizio, molte organizzazioni svolgono attività sporadiche, spesso legate a IOC statici o a esigenze spot. Il logging a disposizione è spesso limitato, le analisi sono manuali e guidate dal buon senso, di conseguenza, non esiste un processo formalizzato. In questa fase l’hunting è più un’iniziativa individuale che un servizio strutturato.

Con il tempo, però, l’approccio può maturare grazie ad esperienza e lesson learned (se viene svolto anch’esso in modo strutturato). L’Hunting Maturity Model ([https://www.sans.org/tools/hunting-maturity-](https://www.sans.org/tools/hunting-maturity-model) [model](https://www.sans.org/tools/hunting-maturity-model)) descrive questa evoluzione considerando diversi fattori: qualità e ampiezza delle fonti dati, formalizzazione delle ipotesi e scopes, competenze analitiche del team e integrazione con il detection engineering del [SOC](https://www.ictsecuritymagazine.com/articoli/evoluzione-soc/) o dell’Incident Response Team.

Quando la maturità aumenta, crescono anche le fonti disponibili: endpoint telemetry, network data, identity logs, audit trail cloud. Framework come MITRE ATT&CK o MITRE D3FEND iniziano a essere usati per modellare le ipotesi e strutturare i report. Nei livelli più avanzati, l’hunting diventa ciclico, misurabile e integrato nel miglioramento continuo: ogni attività produce nuove regole, identifica gap di visibilità o rafforza la copertura esistente.

Un passaggio cruciale in questo percorso è l’abbandono dell’approccio “IOC driven” statico in favore di quello “TTP driven”. Gli indicatori sono fragili, cambiano rapidamente e possono essere facilmente aggirati. Le tecniche, invece, riflettono il modus operandi dell’avversario e tendono a essere più stabili nel tempo.

Ma lavorare sulle TTP richiede esperienza reale e conoscenza degli attori, esposizione a casi concreti, capacità di riconoscere varianti e polimorfismi delle tecniche durante attacchi effettivi.

# Il ruolo centrale della Cyber Threat Intelligence

Un hunting efficace non nasce nel vuoto. Senza intelligence, l’ipotesi rischia di essere astratta o scollegata dal contesto reale.

La Cyber Threat Intelligence fornisce il punto di partenza: attori attivi, campagne in corso, tecniche emergenti, pattern infrastrutturali. Tuttavia, il valore non sta nel report in sé, ma nella capacità di trasformarlo in una domanda operativa.

Se un report descrive l’abuso di token OAuth in ambienti cloud, non è sufficiente conoscere hash o domini. La domanda diventa: “Se un attore con queste capacità stesse operando nel nostro tenant, quali tracce comportamentali dovremmo osservare?”

Da qui nascono query su anomalie nei consensi applicativi, uso atipico di API, persistenza tramite service principal o comportamenti anomali su identity logs.

L’integrazione deve essere bidirezionale. La CTI alimenta l’hunting, ma i risultati dell’hunting evidenze, falsi positivi ricorrenti, nuove tecniche osservate devono a loro volta arricchire il ciclo di intelligence. Solo così si crea un ecosistema realmente dinamico.

**Proviamo a vedere assieme un esempio applicato:**

Un report CTI segnala che un gruppo sta abusando di service principal in Microsoft 365 per ottenere persistenza tramite permessi API elevati.

Il team di Threat Hunting parte da questa informazione e verifica creazioni recenti di service principal, assegnazioni anomale di privilegi e autenticazioni sospette. Durante l’analisi emergono però due aspetti inattesi: un’applicazione legittima che replica parte di quel comportamento (falso positivo ricorrente) e una tecnica non documentata di assegnazione temporanea dei permessi seguita da revoca immediata. Queste evidenze vengono condivise con il team CTI, che aggiorna il proprio dataset inserendo il nuovo pattern e riclassificando alcuni indicatori come d...