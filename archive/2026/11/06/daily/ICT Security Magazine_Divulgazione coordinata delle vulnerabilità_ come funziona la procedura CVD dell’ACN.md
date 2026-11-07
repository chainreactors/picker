---
title: Divulgazione coordinata delle vulnerabilità: come funziona la procedura CVD dell’ACN
url: https://www.ictsecuritymagazine.com/articoli/divulgazione-coordinata-vulnerabilita-acn/
source: ICT Security Magazine
date: 2026-11-06
fetch_date: 2026-11-07T08:02:03.366316
---

# Divulgazione coordinata delle vulnerabilità: come funziona la procedura CVD dell’ACN

[Salta al contenuto](#main)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/logo-ict-security-trasparente-1.webp)](https://www.ictsecuritymagazine.com/)

Cerca nel magazine

* Argomenti

  [Cyber Security: tutti gli articoli 1.349 articoli](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)

  Minacce e attacchi

  + [Vulnerabilità](https://www.ictsecuritymagazine.com/argomenti/vulnerabilita/)
  + [Cyber Crime](https://www.ictsecuritymagazine.com/argomenti/cyber-crime/)
  + [Cyber Warfare](https://www.ictsecuritymagazine.com/argomenti/cyber-warfare/)
  + [Ethical Hacking](https://www.ictsecuritymagazine.com/argomenti/ethical-hacking/)
  + [Digital Forensic](https://www.ictsecuritymagazine.com/argomenti/digital-forensic/)

  Rischio, norme e privacy

  + [GDPR e Privacy](https://www.ictsecuritymagazine.com/argomenti/gdpr-e-privacy/)
  + [Cyber Risk](https://www.ictsecuritymagazine.com/argomenti/cyber-risk/)
  + [Cyber Law](https://www.ictsecuritymagazine.com/argomenti/cyber-law/)
  + [Business Continuity](https://www.ictsecuritymagazine.com/argomenti/business-continuity/)

  Tecnologie

  + [Intelligenza Artificiale](https://www.ictsecuritymagazine.com/argomenti/intelligenza-artificiale/)
  + [IoT Security](https://www.ictsecuritymagazine.com/argomenti/iot-security/)
  + [Industrial Cyber Security](https://www.ictsecuritymagazine.com/argomenti/industrial-cyber-security/)
  + [Digital ID Security](https://www.ictsecuritymagazine.com/argomenti/digital-id-security/)
  + [Blockchain e Criptovalute](https://www.ictsecuritymagazine.com/argomenti/blockchain-e-criptovalute/)
  + [Digital Transformation](https://www.ictsecuritymagazine.com/argomenti/digital-transformation/)

  Scenari

  + [Geopolitica e Cyberspazio](https://www.ictsecuritymagazine.com/argomenti/geopolitica-cyberspazio/)
  + [Prospettive](https://www.ictsecuritymagazine.com/argomenti/prospettive/)

  Ultimi in **Cyber Security**

  [Tutti gli articoli di Cyber Security →](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)
* [Notizie](https://www.ictsecuritymagazine.com/argomenti/notizie/)
* [Approfondimenti](https://www.ictsecuritymagazine.com/argomenti/articoli/)
* [Video](https://www.ictsecuritymagazine.com/argomenti/cybersecurity-video/)
* [Pubblicazioni](https://www.ictsecuritymagazine.com/pubblicazioni/)
* [Eventi ↗](https://eventi.ictsecuritymagazine.com/)

[Newsletter](/newsletter/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/logo-ict-security-trasparente-1.webp)](https://www.ictsecuritymagazine.com/)

Cerca

Attiva/disattiva menu

[Vulnerabilità](https://www.ictsecuritymagazine.com/argomenti/vulnerabilita/) · [Cyber Security](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)

# Divulgazione coordinata delle vulnerabilità: come funziona la procedura CVD dell’ACN

La divulgazione coordinata delle vulnerabilità in Italia: come segnalare uno zero day al CSIRT Italia, i limiti penali che restano e l’embargo rotto di PHP2Shell.

A cura di:[Redazione](https://www.ictsecuritymagazine.com/author/redazione/)  Ore Pubblicato il6 Novembre 20264 Novembre 2026  Condividi

![Divulgazione coordinata delle vulnerabilità: la procedura CVD dell'ACN: Tre mani si passano una busta sigillata sopra una linea del tempo con due tacche; a destra una busta dal sigillo spezzato](https://www.ictsecuritymagazine.com/wp-content/uploads/divulgazione-coordinata-vulnerabilita-acn.webp)

In sintesi

* Dal 7 ottobre 2026 l'ACN ha una Politica nazionale per segnalare al CSIRT Italia le vulnerabilità zero day, anche in forma anonima.
* Dopo la validazione il fornitore ha 7 giorni solari per individuare la mitigazione e 90 per la patch, salvo casi complessi.
* La Politica non prevede una clausola di non punibilità e i reati perseguibili d'ufficio vanno comunicati all'autorità giudiziaria.

La divulgazione coordinata delle vulnerabilità, in inglese coordinated vulnerability disclosure (CVD), ha dal 7 ottobre 2026 una procedura nazionale. Quel giorno l’Agenzia per la cybersicurezza nazionale (ACN) ha [comunicato](https://www.acn.gov.it/portale/w/l-acn-invita-la-comunita-digitale-e-gli-hacker-etici-a-segnalare-tutte-le-vulnerabilita-zero-day-) l’adozione della Politica CVD, con determina del direttore generale Andrea Quacivi.

La [Politica](https://www.acn.gov.it/portale/documents/20119/1157905/ACN_Politica%2BCVD.pdf/0b7bf785-4cde-65f4-bd8f-a090917da90d?t=1791358234324), di 16 pagine, spiega come segnalare una vulnerabilità al CSIRT Italia, che cosa fa l’agenzia dopo la segnalazione e in quanto tempo il fornitore deve intervenire. Non contiene una clausola di non punibilità per chi fa ricerca. Questa guida segue la procedura passo dopo passo, la confronta con le regole europee e con le politiche di Project Zero e del CERT/CC, e la mette alla prova con due casi recenti: l’alert del CSIRT Italia su Magistra e l’embargo rotto di PHP2Shell.

## Che cos’è la divulgazione coordinata delle vulnerabilità

La direttiva NIS2 la descrive nel [considerando 58](https://eur-lex.europa.eu/legal-content/IT/TXT/HTML/?uri=CELEX:32022L2555): chi trova una vulnerabilità la segnala al fabbricante o al fornitore, che può così diagnosticarla ed eliminarla prima che i dettagli diventino pubblici. Il coordinamento riguarda anche i tempi di risoluzione e di pubblicazione.

Lo stesso considerando rimanda alle norme ISO/IEC 29147 e ISO/IEC 30111. Secondo la [scheda ISO](https://www.iso.org/standard/72311.html), la 29147:2018 fissa requisiti e raccomandazioni per i fornitori che ricevono le segnalazioni e pubblicano le informazioni di rimedio. Le attività tra la ricezione e la pubblicazione rientrano nella 30111. La 29147 è stata confermata nel 2024 e risulta da rivedere. Il rapporto tecnico [ISO/IEC TR 5895:2022](https://www.iso.org/standard/81807.html) applica le due norme ai casi con più parti coinvolte.

All’estremo opposto sta la full disclosure: rendere pubbliche subito le informazioni sulla falla. Il [CERT/CC](https://certcc.github.io/certcc_disclosure_policy/) osserva che, senza una divulgazione responsabile e qualificata, chi scopre le vulnerabilità spesso sente di non avere altra scelta che pubblicarle per costringere i fornitori a intervenire. Tra i due estremi stanno le politiche di ricercatori e centri di coordinamento, che concedono al fornitore un termine e poi pubblicano; ne parla la sezione sull’embargo.

## Dalla direttiva NIS2 alla Politica dell’ACN

L’[articolo 12 della NIS2](https://eur-lex.europa.eu/legal-content/IT/TXT/HTML/?uri=CELEX:32022L2555) impone a ogni Stato membro di designare un CSIRT come coordinatore. Il CSIRT fa da intermediario di fiducia tra chi segnala e il fabbricante o il fornitore, su richiesta di una delle parti. Individua e contatta i soggetti interessati, assiste chi segnala, negozia i tempi di pubblicazione e gestisce le vulnerabilità che toccano più soggetti. Gli Stati devono consentire la segnalazione anonima e, se l’impatto riguarda più Stati, i CSIRT cooperano nella rete.

L’[articolo 16 del d.lgs. 138/2024](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2024-09-04;138~art16) recepisce queste regole e designa il CSIRT Italia. Il comma 4 affida all’autorità nazionale competente NIS, cioè all’ACN, il compito di adottare la politica nazionale di divulgazione coordinata delle vulnerabilità e di realizzare i mezzi tecnici per applicarla.

La [determina](https://www.acn.gov.it/portale/documents/d/guest/determina_cvd-pdf_signed) di adozione precisa che l’ACN ha acquisito l’intesa del Ministero della giustizia (comunicazione del 31 ottobre 2025) e ha sentito il Tavolo per l’attuazione della disciplina NIS (riunione del 18 dicembre 2025). Prevede inoltre che la Politica possa essere modificata e aggiornata periodicamente, anche a seguito di revisioni normative. La firma digitale reca la data del 6 ottobre 2026; l’ACN ne ha dato notizia il giorno dopo.

Il considerando 60 della NIS...