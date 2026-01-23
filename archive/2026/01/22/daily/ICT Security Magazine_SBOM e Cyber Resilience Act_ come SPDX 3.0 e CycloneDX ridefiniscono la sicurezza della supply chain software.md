---
title: SBOM e Cyber Resilience Act: come SPDX 3.0 e CycloneDX ridefiniscono la sicurezza della supply chain software
url: https://www.ictsecuritymagazine.com/articoli/spdx-3-0/
source: ICT Security Magazine
date: 2026-01-22
fetch_date: 2026-01-23T03:33:31.654148
---

# SBOM e Cyber Resilience Act: come SPDX 3.0 e CycloneDX ridefiniscono la sicurezza della supply chain software

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

![Illustrazione concettuale sulla trasparenza della supply chain software, con componenti di codice stratificati, grafi di dipendenze, inventari SBOM, librerie software e simboli di sicurezza e conformità europea, che rappresentano gli standard SPDX e la resilienza cyber](https://www.ictsecuritymagazine.com/wp-content/uploads/SPDX-3.0.jpg)

# SBOM e Cyber Resilience Act: come SPDX 3.0 e CycloneDX ridefiniscono la sicurezza della supply chain software

A cura di:[Redazione](#molongui-disabled-link)  Ore 22 Gennaio 202614 Gennaio 2026

*La trasparenza del codice diventa obbligo normativo: analisi degli standard tecnici e delle implicazioni per produttori e operatori europei.*

## Introduzione: dalla vulnerabilità sistemica alla tracciabilità obbligatoria

L’attacco a SolarWinds del 2020 e la vulnerabilità Log4Shell del dicembre 2021 hanno rappresentato punti di svolta nella percezione del rischio legato alla *supply chain* software. Il [rapporto ENISA *Threat Landscape* 2024](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2024), pubblicato a settembre 2024, identifica gli attacchi alla catena di approvvigionamento tra le sette minacce principali per la cybersecurity europea, evidenziando come questa tipologia di attacco abbia assunto carattere trasversale, intersecando ransomware, malware e minacce alla disponibilità dei sistemi.

In questo scenario, il concetto di *Software Bill of Materials* (SBOM) emerge come paradigma fondamentale per garantire visibilità e controllo sui componenti che costituiscono qualsiasi prodotto digitale. L’Unione Europea, con l’approvazione definitiva del [Regolamento (UE) 2024/2847](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847), noto come *Cyber Resilience Act* (CRA), pubblicato nella Gazzetta Ufficiale il 20 novembre 2024 ed entrato in vigore il 10 dicembre 2024, ha trasformato questa *best practice* in requisito cogente, inaugurando una nuova era di responsabilità documentata per i produttori di software.

## Il *Software Bill of Materials*: anatomia di un inventario critico

Il SBOM costituisce un inventario formale e leggibile da macchina che elenca tutti i componenti, le librerie e le dipendenze presenti in un prodotto software. La [National Telecommunications and Information Administration (NTIA)](https://www.ntia.gov/page/software-bill-materials) del Dipartimento del Commercio statunitense ha definito nel luglio 2021 gli elementi minimi che un SBOM deve contenere, stabilendo uno standard *de facto* successivamente adottato anche dalle normative europee.

Gli elementi minimi NTIA includono: il nome del fornitore del componente, il nome e la versione del componente stesso, gli identificatori univoci, le relazioni di dipendenza, l’autore del SBOM e il *timestamp* di generazione. Questa struttura apparentemente semplice nasconde una complessità tecnica considerevole quando applicata a software enterprise moderni, che tipicamente integrano centinaia o migliaia di dipendenze transitive.

La distinzione tra dipendenze dirette e transitive assume rilevanza critica nella gestione del rischio. Una dipendenza diretta è un componente esplicitamente incluso dagli sviluppatori; una dipendenza transitiva è un componente richiesto da una dipendenza diretta, spesso invisibile al team di sviluppo ma perfettamente sfruttabile da un attaccatore. Il caso Log4Shell ha dimostrato come una vulnerabilità in una dipendenza transitiva possa propagarsi attraverso l’intero ecosistema software mondiale nel giro di ore.

## SPDX 3.0: l’evoluzione dello standard ISO per la trasparenza software

Il [*System Package Data Exchange* (SPDX)](https://spdx.dev/), sviluppato sotto l’egida della Linux Foundation, rappresenta lo standard più consolidato per la rappresentazione di SBOM. La versione 3.0, [rilasciata ufficialmente il 16 aprile 2024](https://www.linuxfoundation.org/press/spdx-3-revolutionizes-software-management-in-systems-with-enhanced-functionality-and-streamlined-use-cases), costituisce una riscrittura architetturale completa che risponde alle esigenze emergenti del panorama normativo internazionale.

SPDX gode dello status di standard internazionale attraverso la certificazione [ISO/IEC 5962:2021](https://www.iso.org/standard/81870.html), elemento che ne garantisce l’accettazione in contesti regolamentati e conferisce autorevolezza in procedimenti di *compliance*. La versione 3.0 estende significativamente le capacità dello standard precedente, introducendo un modello dati modulare che consente di rappresentare non solo componenti software, ma anche *dataset*, modelli di intelligenza artificiale, specifiche di *build* e informazioni di sicurezza.

L’architettura SPDX 3.0 si basa su profili specializzati che possono essere combinati in base alle esigenze specifiche. Il profilo *Core* definisce le strutture fondamentali; il profilo *Software* descrive pacchetti, file e *snippet* di codice; il profilo *Security* integra informazioni su vulnerabilità secondo lo standard [*Common Vulnerabilities and Exposures* (CVE)](https://www.cve.org/); il profilo AI, particolarmente innovativo, consente di documentare *dataset* di *training* e modelli di *machine learning*.

La serializzazione in SPDX 3.0 supporta formati multipli: JSON-LD per l’interoperabilità semantica, RDF per l’integrazione con *knowledge graph*, XML per la compatibilità con sistemi *legacy*. Questa flessibilità risponde alle diverse esigenze di ecosistemi tecn...