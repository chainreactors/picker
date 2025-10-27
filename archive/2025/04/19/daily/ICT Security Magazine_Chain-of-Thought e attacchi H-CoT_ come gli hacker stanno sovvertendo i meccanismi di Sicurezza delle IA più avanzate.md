---
title: Chain-of-Thought e attacchi H-CoT: come gli hacker stanno sovvertendo i meccanismi di Sicurezza delle IA più avanzate
url: https://www.ictsecuritymagazine.com/articoli/chain-of-thought-h-cot/
source: ICT Security Magazine
date: 2025-04-19
fetch_date: 2025-10-06T22:07:29.920741
---

# Chain-of-Thought e attacchi H-CoT: come gli hacker stanno sovvertendo i meccanismi di Sicurezza delle IA più avanzate

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

![Chain-of-Thought e attacchi H-CoT: come gli hacker stanno sovvertendo i meccanismi di Sicurezza delle IA più avanzate](https://www.ictsecuritymagazine.com/wp-content/uploads/Chain-of-Thought.jpg)

# Chain-of-Thought e attacchi H-CoT: come gli hacker stanno sovvertendo i meccanismi di Sicurezza delle IA più avanzate

A cura di:[Redazione](#molongui-disabled-link)  Ore 18 Aprile 202515 Aprile 2025

Nel panorama in costante evoluzione dell’intelligenza artificiale, una nuova e allarmante vulnerabilità è emersa, colpendo al cuore i sistemi di sicurezza implementati nei modelli linguistici di ragionamento più avanzati. Un recente studio condotto da ricercatori della Duke University ha portato alla luce una metodologia di attacco denominata “[Hijacking Chain-of-Thought](https://arxiv.org/pdf/2502.12893)” (H-CoT), in grado di compromettere i meccanismi di sicurezza di modelli come OpenAI o1/o3, DeepSeek-R1 e Gemini 2.0 Flash Thinking.

## Il paradosso della trasparenza nel ragionamento AI

Il meccanismo di ragionamento “*chain-of-thought*” (catena di pensiero) rappresenta una delle innovazioni più significative nel campo dell’intelligenza artificiale degli ultimi anni. Introdotto nel 2022, questo approccio consente ai modelli IA di affrontare problemi complessi scomponendoli in passaggi intermedi, imitando il processo di ragionamento umano. Questa metodologia ha migliorato notevolmente le capacità dei modelli di risolvere problemi articolati, fornendo risposte più accurate e contestualizzate.

Ironicamente, ciò che era stato concepito come un miglioramento per la sicurezza si è trasformato in una vulnerabilità critica. Come spiega Jianyi Zhang, autore principale dello studio e ricercatore presso la Duke University:

> “La capacità di ragionamento chain-of-thought può effettivamente migliorare la sicurezza, poiché il modello può eseguire un’analisi interna più rigorosa per rilevare violazioni delle policy. Tuttavia, il nostro attacco H-CoT è un metodo più avanzato che sfrutta specificamente la trasparenza di questo processo. Quando un modello condivide apertamente i suoi ragionamenti intermedi sulla sicurezza, gli attaccanti acquisiscono informazioni sui suoi processi decisionali e possono creare prompt avversariali che imitano o sovrascrivono i controlli originali.”

Questa vulnerabilità è stata riconosciuta anche da Anthropic nella [documentazione del suo modello Claude 3.7 Sonnet](https://assets.anthropic.com/m/785e231869ea8b3b/original/claude-3-7-sonnet-system-card.pdf):

> “…consentire agli utenti di vedere il ragionamento di un modello potrebbe permettere loro di comprendere più facilmente come aggirare le protezioni del modello stesso.”

## Anatomia dell’Attacco H-CoT

Per comprendere la portata del problema, i ricercatori hanno sviluppato un dataset chiamato “*Malicious-Educator*“, contenente richieste intrinsecamente pericolose ma mascherate da scopi educativi legittimi. Queste richieste riguardano argomenti estremamente sensibili come terrorismo, cybercrime e abuso di minori – tematiche che i modelli AI responsabili dovrebbero rifiutarsi di trattare in contesti dannosi.

Il processo di attacco H-CoT si articola attraverso l’analisi e la manipolazione di due fasi distinte del ragionamento del modello:

1. **Fase di Giustificazione:** In questa fase iniziale, il modello valuta se una richiesta è conforme alle policy di sicurezza e se dovrebbe fornire una risposta;
2. **Fase di Esecuzione**: Se il modello decide che può fornire una risposta conforme alle policy, procede con questa fase, illustrando i passaggi di ragionamento per risolvere il problema.

Contrariamente ai tentativi più semplici di alterare la fase di giustificazione, che generalmente falliscono poiché il modello è addestrato a riconoscere manipolazioni esplicite, l’approccio H-CoT opera in modo più sofisticato. Invece di cercare di modificare direttamente l’opinione del modello sulla legittimità di una richiesta, l’attacco incoraggia il modello a concentrarsi sulla risoluzione del problema, aggirando efficacemente la fase di giustificazione e passando direttamente alla fase di esecuzione.

Ciò avviene inserendo frammenti di “pensieri” simulati che imitano lo stile del ragionamento del modello, inducendolo a credere che la valutazione della sicurezza sia già stata completata. Come spiegano i ricercatori:

> “Interponendo un frammento di pensiero di esecuzione simulato, incoraggiamo il modello a saltare le giustificazioni attente e a passare direttamente a una mentalità di esecuzione.”

## Nessun modello è veramente sicuro!

I risultati dei test condotti dai ricercatori sono profondamente preoccupanti e mettono in discussione l’efficacia delle attuali misure di sicurezza implementate nei modelli IA di punta.

Il modello o1 di OpenAI, che normalmente rifiuta il 99% delle richieste dannose presenti nel dataset Malicious-Educator, ha visto il suo **tasso di rifiuto crollare a meno del 2% quando sottoposto ad attacchi H-CoT**. Questo rappresenta un deterioramento catastrofico delle sue difese, riducendo praticamente a zero la sua capacità di identificare e bloccare contenuti potenzialmente pericolosi.

La situazione si rivela ancora più critica per DeepSeek-R1, che già in condizioni normali mostra un tasso di rifiuto di appena il...