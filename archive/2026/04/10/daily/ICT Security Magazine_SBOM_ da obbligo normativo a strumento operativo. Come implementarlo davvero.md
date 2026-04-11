---
title: SBOM: da obbligo normativo a strumento operativo. Come implementarlo davvero
url: https://www.ictsecuritymagazine.com/notizie/sbom-implementazione/
source: ICT Security Magazine
date: 2026-04-10
fetch_date: 2026-04-11T04:22:54.688409
---

# SBOM: da obbligo normativo a strumento operativo. Come implementarlo davvero

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

![sbom](https://www.ictsecuritymagazine.com/wp-content/uploads/sbom.jpeg)

# SBOM: da obbligo normativo a strumento operativo. Come implementarlo davvero

A cura di:[Redazione](#molongui-disabled-link)  Ore 10 Aprile 202610 Aprile 2026

*Il Cyber Resilience Act impone il Software Bill of Materials su tutti i prodotti digitali. Oltre la compliance: come costruire, mantenere e integrare l’SBOM nella supply chain security, con tool open source e workflow pratici.*

## Il contesto normativo: perché l’SBOM è diventato urgente

Per anni l’SBOM è rimasto un concetto familiare solo agli ambienti DevSecOps più maturi. Poi sono arrivati SolarWinds, Log4Shell e una cascata di attacchi alla supply chain software che hanno reso evidente una verità scomoda: la maggior parte delle organizzazioni non sapeva cosa girasse realmente nei propri sistemi. Da quella consapevolezza è nata la spinta normativa che oggi impone alle aziende di rispondere a una domanda apparentemente banale con un documento formale, strutturato e aggiornato: di cosa è fatto il software che produciamo o utilizziamo?

Il [Cyber Resilience Act](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act) (CRA), pubblicato nella Gazzetta Ufficiale dell’Unione Europea il 20 novembre 2024 come [Regolamento (UE) 2024/2847](https://eur-lex.europa.eu/legal-content/IT/TXT/?uri=CELEX:32024R2847) ed entrato in vigore il 10 dicembre 2024, è il riferimento normativo più rilevante per il mercato europeo. Gli obblighi di notifica di vulnerabilità e incidenti gravi si applicano a partire dall’11 settembre 2026, mentre la piena applicazione di tutti i requisiti di sicurezza diventa obbligatoria dall’11 dicembre 2027. Il regolamento si applica a tutti i prodotti con elementi digitali immessi sul mercato UE, tra cui hardware con componenti software integrato, applicazioni, firmware e sistemi embedded.

Tra i requisiti dell’Allegato I individua esplicitamente l’obbligo per i fabbricanti di “identificare e documentare le vulnerabilità e i componenti contenuti nei prodotti con elementi digitali, anche elaborando una distinta base del software in un formato comunemente usato e leggibile meccanicamente che copra almeno le dipendenze di primo livello dei prodotti”.

Vale la pena sottolineare una sfumatura rilevante: il CRA non impone la pubblicazione dell’SBOM, ma la sua disponibilità su richiesta delle autorità di sorveglianza del mercato. Le linee guida tecniche che CEN/CENELEC sta sviluppando, con uno standard orizzontale atteso entro metà 2026, chiariranno ulteriori aspetti applicativi, inclusa la questione interpretativa sull’estensione dell’obbligo alle dipendenze transitive oltre quelle di primo livello.

Parallelamente, il quadro normativo si articola su più livelli: la [Direttiva NIS2](https://www.ictsecuritymagazine.com/articoli/nis2-implementazione/) richiede alle organizzazioni essenziali e importanti di gestire i rischi della catena di fornitura, inclusa la sicurezza dei componenti software; il DORA impone agli enti finanziari controlli stringenti sulle dipendenze tecnologiche critiche; in ambito statunitense, l’[Executive Order 14028](https://bidenwhitehouse.archives.gov/briefing-room/presidential-actions/2021/05/12/executive-order-on-improving-the-nations-cybersecurity/) del 12 maggio 2021 ha reso l’SBOM un requisito per i fornitori software del governo federale, stabilendo un precedente che ha accelerato l’adozione globale. Per i produttori di software e di dispositivi connessi che operano su mercati internazionali, l’SBOM non è più una scelta architettuale: è un requisito di mercato. Per un approfondimento sugli adempimenti NIS2 in scadenza, si veda anche [questo articolo di ICT Security Magazine](https://www.ictsecuritymagazine.com/articoli/adempimenti-nis2/).

## Cosa è (davvero) un SBOM

Un Software Bill of Materials è un inventario formale e leggibile da macchina di tutti i componenti che compongono un artefatto software: librerie di terze parti, dipendenze transitive, moduli open source, pacchetti interni, strumenti di build incorporati. Ogni componente è descritto da un insieme di attributi minimi che ne permettono l’identificazione univoca e la correlazione con le basi di dati delle vulnerabilità note.

Il [National Telecommunications and Information Administration (NTIA)](https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom) statunitense ha definito nel luglio 2021, in attuazione dell’EO 14028, i sette campi dati minimi che ogni SBOM deve contenere:

* **Nome del produttore** (Producer Name) del componente;
* **Nome del componente** (Component Name);
* **Versione del componente;**
* **Identificatore univoco** aggiuntivo, quali Package URL (PURL), Common Platform Enumeration (CPE) o SWID tag;
* **Relazione di dipendenza** con il componente padre;
* **Autore dei dati SBOM** (SBOM Author);
* **Timestamp** di generazione.

È importante precisare che l’hash crittografico del componente, spesso citato erroneamente come campo obbligatorio, non rientra nei sette campi minimi della versione originale NTIA 2021: il documento lo classifica esplicitamente tra i campi “beyond minimum”, ovvero raccomandati per casi d’uso ad alta garanzia ma non obbligatori nella baseline. Solo la rev...