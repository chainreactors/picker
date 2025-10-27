---
title: GenAI: sicurezza e protezione
url: https://www.ictsecuritymagazine.com/articoli/sicurezza-genai/
source: ICT Security Magazine
date: 2025-02-15
fetch_date: 2025-10-06T20:39:32.521741
---

# GenAI: sicurezza e protezione

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

![GenAI: sicurezza e protezione](https://www.ictsecuritymagazine.com/wp-content/uploads/GENAI.jpg)

# GenAI: sicurezza e protezione

A cura di:[Vincenzo Calabrò](#molongui-disabled-link)  Ore 14 Febbraio 202521 Febbraio 2025

Questo articolo fa parte di una [serie di approfondimenti](https://www.ictsecuritymagazine.com/articoli/generative-ai/) dedicati all’evoluzione e alle sfide della GenAI. In questa puntata, esploreremo i meccanismi di sicurezza, protezione e gestione dei rischi nei sistemi basati sulla GenAI, offrendo una prospettiva tecnica e strategica sulle attuali complessità tecnologiche.

## Tassonomia dei Rischi nella GenAI

In questo paragrafo si analizza il tema della sicurezza e della protezione nel contesto dell’AI, applicata allo sviluppo di sistemi critici, attraverso l’esame di specifici esempi di fragilità e vulnerabilità dell’AI generativa. I rischi a cui è esposta la GenAI sono organizzati seguendo una tassonomia analoga agli attributi di confidenzialità, integrità e disponibilità (CIA) adoperati nel contesto dei rischi informatici:

* **rischi di confidenzialità**: si palesano nel caso in cui i risultati di un modello di AI rivelano dati di input che i progettisti avevano intenzione di mantenere riservati.
* **rischi di integrità**: si presentano nel caso in cui i risultati di un modello di AI sono errati, involontariamente o tramite manipolazione deliberata da parte degli avversari.
* **rischi di governance**: si rivelano nel caso in cui i risultati di un modello di AI, o l’utilizzo di tale modello in un sistema, possono avere impatti negativi nel contesto delle applicazioni, spesso anche quando i risultati del modello sono corretti rispetto alla formazione.

Partiamo dall’assunto che la gestione del [rischio per l’AI,](https://www.ictsecuritymagazine.com/articoli/ai-controlli-di-sicurezza/) compresa la modellazione e la valutazione, è distinguibile in tre livelli:

1. le capacità del *“core AI”* dei singoli modelli di reti neurali,
2. le scelte effettuate su come tali capacità siano incorporate nell’ingegneria dei sistemi basati sull’AI,
3. come tali sistemi siano integrati in workflow operativi incentrati sulle applicazioni.

Questi workflow possono includere sia applicazioni autonome, che applicazioni abilitate a interagire con soggetti umani. Questa ampia flessibilità è importante perché l’intelligenza artificiale generativa può portare non solo aumenti significativi della produttività e dell’efficacia della mission all’interno di processi organizzativi consolidati, ma può anche generare nuove capacità basate sulla reingegnerizzazione delle attività sul posto di lavoro incentrate sulla mission e sull’operatività.

## Considerazioni sulla GenAI

La natura stocastica dei modelli di GenAI, combinata con una quasi totale assenza di trasparenza rispetto all’interrogazione e all’analisi, rende complessa la loro descrizione, il testing, l’analisi e il monitoraggio. Ciò che si percepisce come somigliante tra i vari input di un modello, non corrisponde necessariamente al modo in cui risponde il modello.

Durante l’addestramento, le differenziazioni possono essere effettuate in base a dettagli che normalmente consideriamo accidentali. Un esempio noto è quello in cui il lupo è distinto dagli altri cani non per la morfologia, ma perché c’è neve sullo sfondo, come rivelato dalle mappe di salienza[[1]](#_ftn1). Infatti, la metrologia[[2]](#_ftn2) della GenAI è appena agli inizi.

Un altro esempio rappresentativo dell’aleatorietà del ML è quello che riguarda l’autonomia dei veicoli. In questo caso, la combinazione tra la scarsa capacità di valutazione dei test e le pressanti direttive aziendali ha portato alla produzione di intere flotte di autoveicoli a guida autonoma e al successivo ritiro dal mercato a causa di comportamenti inaspettati. Inoltre, sono stati individuati diversi bias negli algoritmi predittivi applicati alla stipula di contratti di credito, oppure al reclutamento del personale e all’elaborazione delle richieste di rimborso sanitario. Questi sono i motivi per cui è facilmente realizzabile l’*”adversarial machine learning”*[[3]](#_ftn3).

Analizziamo i principali fattori che caratterizzano i sistemi basati sul GenAI.

### Dal punto di vista della mission

Molto spesso i modelli di intelligenza artificiale generativi, addestrati sui dati, sono inclusi all’interno di *“mission system”*[[4]](#_ftn4) sottoforma di componenti o servizi subordinati e, come già visto, spesso questi sistemi rappresentano dei componenti di *workflow* operativi che supportano un’applicazione all’interno di un determinato processo. Per tanto, affinché si possano misurare e valutare, occorre comprendere tutti e tre i livelli: componente, sistema e *workflow*.

Per esempio, i problemi dei *“bias”* (preconcetto/pregiudizio/parzialità) possono essere il risultato della mancata corrispondenza tra i dati utilizzati per addestrare il modello con i dati reali di input. Nel contesto del *“Test and Evaluation (T&E)”* significa che è fondamentale caratterizzare e valutare i tre livelli di classificazione indicati in precedenza:

1. le caratteristiche delle capacità di intelligenza artificiale integrate,
2. il modo in cui tali capacità vengono utilizzate nei sistemi basati sull’intelligenza artificial...