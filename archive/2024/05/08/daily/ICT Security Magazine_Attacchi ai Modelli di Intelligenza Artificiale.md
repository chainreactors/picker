---
title: Attacchi ai Modelli di Intelligenza Artificiale
url: https://www.ictsecuritymagazine.com/articoli/attacchi-ai-modelli-di-intelligenza-artificiale/
source: ICT Security Magazine
date: 2024-05-08
fetch_date: 2025-10-06T17:20:55.826625
---

# Attacchi ai Modelli di Intelligenza Artificiale

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

![](https://www.ictsecuritymagazine.com/wp-content/uploads/Attacchi-ai-Modelli-di-Intelligenza-Artificiale.jpg)

# Attacchi ai Modelli di Intelligenza Artificiale

A cura di:[Andrea Pasquinucci](#molongui-disabled-link)  Ore 7 Maggio 2024

I modelli di Intelligenza Artificiale (AI) stanno assumendo molto velocemente un grande ruolo nella vita di tutti noi. Le previsioni sono che nei prossimi anni utilizzeremo quotidianamente modelli AI sia in ambito lavorativo sia personale per moltissimi scopi. Ad esempio IDC [Rif. 1] prevede che entro il 2027 il 60% dei PC venduti avrà componenti Hardware (“system-on-a-chip – SoC”, diversi dalle GPU) dedicate all’elaborazione locale di modelli AI (si veda anche [Rif. 2]). Ci si aspetta un simile sviluppo anche per i dispositivi mobili quali smartphone, tablet ecc. oltre, ovviamente, ai server.

Oltre alle possibili debolezze comuni a qualsiasi programma informatico, i modelli AI hanno delle debolezze specifiche e in alcuni casi nuove, contro le quali non siamo abituati a confrontarci quasi quotidianamente. La ricerca in questo campo è molto attiva e nuovi risultati sono annunciati ogni giorno. È comunque possibile fare già ora una rassegna dei principali tipi di debolezze dei modelli AI che possono essere sfruttate da un attaccante.

### Approcci allo Studio dei Tipi di Attacchi ai Modelli AI

In generale lo studio di un attacco ad un sistema informatico può essere analizzato considerando le **vulnerabilità** che l’attaccante intende sfruttare, le **tecniche** per implementare l’attacco e l’**effetto** dell’attacco sul sistema attaccato. Vi sono vari approcci allo studio degli attacchi ai sistemi informatici. Fra i più noti è quello che fa riferimento alla “Kill Chain”, ovvero identificare nell’ordine le azioni che un attaccante porta a termine per realizzare l’attacco per trovare i punti ove poterlo fermare. La metodologia più utilizzata per i modelli AI è quella sviluppata da MITRE con ATLAS™ [Rif. 3]. Questo approccio, focalizzandosi sulle azioni dell’attaccante, è sicuramente quello più appropriato per la gestione degli incidenti in tempo reale perché aiuta il difensore a identificare la migliore maniera per gestire l’incidente.

Un altro approccio è più preventivo e consiste nel valutare principalmente le vulnerabilità e i possibili effetti di un eventuale loro sfruttamento da parte di un attaccante per poter implementare misure di sicurezza sulla base di una valutazione dei rischi. In questo caso si ricorre spesso alla formulazione di tassonomie quale quella di NIST [Rif. 4] o di Microsoft [Rif. 5].

In questa sede non si intende descrivere in dettaglio una “Kill Chain” o proporre una tassonomia, ma fare una rassegna ad alto livello di quanto ad oggi si è capito cercando di organizzare le informazioni in uno schema sufficientemente semplice. Per questo l’approccio adottato è più simile a quello di una tassonomia mancandone però il rigore e la completezza.

Per questo articolo sono state considerate le debolezze o vulnerabilità dei modelli AI e le possibili conseguenze o effetti del loro sfruttamento. Questi sono stati raggruppati in quelli che genericamente saranno chiamati “attacchi”. Seguendo [Rif. 4] conviene distinguere due tipi di attacchi: quelli comuni a molti tipi di modelli AI, che sono indicati come modelli **AI Predittivi**, e quelli specifici ai modelli **Generativi** e “General Purpose” quali ad esempio i “Large Language Models” (LLM) come GPT, Bard/Gemini, LLaMA ecc.

In sicurezza informatica, gli effetti dello sfruttamento di una debolezza o vulnerabilità sono usualmente classificati dalla violazione di una o più caratteristiche di sicurezza tra Riservatezza, Integrità e Disponibilità (RID, in Inglese CIA). Nella letteratura già richiamata, questa classificazione è utilizzata anche per i modelli AI con due piccole varianti: si considerano Riservatezza insieme a Privacy, Integrità, Disponibilità e per i modelli Generativi anche Abuso. Con Abuso si intende proprio l’utilizzo di un modello AI Generativo per generare dati in violazione degli scopi e/o dei modi di utilizzo del modello stesso. Si noti che l’abuso di un modello AI Generativo qui considerato è diverso dall’abuso di una tradizionale applicazione informatica. Tutte le funzionalità e possibili dati prodotti da una usuale applicazione informatica sono disegnati e implementati dai programmatori; in questa situazione un abuso si può verificare nel caso di utilizzo di funzionalità esistenti da parte di chi non ne è autorizzato (violazione dell’Integrità del sistema di autorizzazione dell’applicazione) o in violazione della licenza d’uso. Come sarà descritto in seguito, per i modelli Generativi un ulteriore caso di abuso è l’utilizzo del modello per generare dati non previsti dai programmatori o in violazione degli scopi dell’addestramento del modello, senza però violarne le caratteristiche RID.

### Attacchi ai Modelli AI Predittivi

In generale gli attacchi ai modelli AI possono essere classificati in tre classi:

* “Poisoning” (Avvelenamento)
* “Evasion / Adversarial Attacks” (Evasione)
* “Extraction / Reconstruction” (Estrazione / Ricostruzione).

##### Avvelenamento

Gli attacchi di avvelenamento sono quelli più simili ai comuni attacchi alla sicurezza dei sistemi informatici e...