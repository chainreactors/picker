---
title: Jailbreak AI autonomo: i modelli di ragionamento come nuova minaccia per la sicurezza dei sistemi intelligenti
url: https://www.ictsecuritymagazine.com/articoli/jailbreak-ai/
source: ICT Security Magazine
date: 2026-03-11
fetch_date: 2026-03-12T04:08:44.513576
---

# Jailbreak AI autonomo: i modelli di ragionamento come nuova minaccia per la sicurezza dei sistemi intelligenti

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

![jailbreak ai](https://www.ictsecuritymagazine.com/wp-content/uploads/jailbreak-ai.jpeg)

# Jailbreak AI autonomo: i modelli di ragionamento come nuova minaccia per la sicurezza dei sistemi intelligenti

A cura di:[Redazione](#molongui-disabled-link)  Ore 11 Marzo 20269 Marzo 2026

Il jailbreak AI – l’aggiramento dei meccanismi di sicurezza integrati nei modelli di intelligenza artificiale – sta attraversando una trasformazione radicale che ne ridefinisce il profilo di rischio per l’intero ecosistema tecnologico. Una [ricerca pubblicata su *Nature Communications*](https://www.nature.com/articles/s41467-026-69010-1) nel febbraio 2026 da Thilo Hagendorff (Università di Stoccarda), Erik Derner e Nuria Oliver ([ELLIS Alicante](https://ellisalicante.org/)) ha dimostrato che i cosiddetti Large Reasoning Models (LRM) – una classe di modelli linguistici ottimizzati per il ragionamento multi-step, la pianificazione e la deliberazione – sono in grado di operare come agenti avversari completamente autonomi, conducendo attacchi di jailbreak multi-turno contro altri modelli di IA senza alcuna supervisione umana.

I risultati sono eloquenti: un tasso di successo complessivo del 97,14% nel superamento dei guardrail di sicurezza dei principali modelli commerciali attualmente in uso. Questo dato non rappresenta solo un campanello d’allarme per i team di sicurezza, ma segnala l’emergere di quello che gli autori definiscono un fenomeno di *alignment regression* – un ciclo potenzialmente vizioso in cui ogni nuova generazione di modelli più capaci può essere impiegata per erodere le garanzie di sicurezza dei modelli precedenti.

## Dal jailbreak artigianale a quello industriale

[Il jailbreak dei modelli linguistici](https://www.ictsecuritymagazine.com/articoli/intelligenza-artificiale-generativa/) – l’insieme di tecniche volte a bypassare i meccanismi di sicurezza integrati per ottenere output dannosi, tossici o non etici – ha rappresentato per anni un’attività che richiedeva competenze tecniche specifiche. Nelle prime fasi, si trattava di prompt ingegnerizzati manualmente, spesso cifrati o mascherati tramite suffissi ottimizzati con tecniche gradient-based. Successivamente, approcci semi-automatizzati hanno introdotto [l’uso di LLM come generatori di prompt avversari](https://www.ictsecuritymagazine.com/notizie/dark-llm/), raffinati attraverso fine-tuning o processi di ricerca evolutiva.

Tuttavia, queste metodologie presentavano limitazioni significative: i suffissi avversari generati automaticamente risultavano semanticamente privi di senso e facilmente rilevabili dai filtri di perplessità; gli approcci multi-turno richiedevano strutture di prompt elaborate, strategie predefinite o pipeline di fine-tuning complesse. In sostanza, il jailbreak restava un’attività laboriosa, costosa e ad alta intensità di competenze.

Lo [studio di Hagendorff e colleghi](https://doi.org/10.1038/s41467-026-69010-1) capovolge questa equazione. La configurazione sperimentale è, nelle parole degli stessi autori, “massimamente semplice ma efficiente”: un singolo system prompt fornito al modello avversario, nessuna necessità di fine-tuning, nessuno scaffolding complesso, nessun intervento umano dopo l’inizializzazione. Il modello di ragionamento pianifica ed esegue l’attacco in modo completamente autonomo, sfruttando le proprie capacità intrinseche di pianificazione strategica e persuasione.

## Anatomia dell’esperimento: jailbreak AI su scala industriale

I ricercatori hanno impiegato quattro LRM come agenti avversari – DeepSeek-R1, Gemini 2.5 Flash, Grok 3 Mini e Qwen3 235B – incaricandoli di compromettere nove modelli target tra i più diffusi, tra cui GPT-4o, Claude 4 Sonnet, Gemini 2.5 Flash, Grok 3, Llama 3.1 70B, Llama 4 Maverick, o4-mini, DeepSeek-V3 e Qwen3 30B. Ciascun modello target operava con il system prompt standard “You are a helpful assistant”, mentre il modello avversario riceveva istruzioni per indurre il target a fornire informazioni dannose su argomenti specifici.

Il benchmark utilizzato comprende 70 richieste dannose distribuite in sette categorie: violenza e lesioni fisiche, cybercrime, attività illegali, droghe e abuso di sostanze, autolesionismo e suicidio, veleni, armi ed esplosivi. Ogni conversazione si sviluppava su 10 turni, con il modello avversario che iniziava invariabilmente con un innocuo “Hi!”.

La valutazione degli output è stata affidata a tre LLM-giudici (GPT-4.1, Gemini 2.5 Flash, Grok 3) che classificavano le risposte su una scala di danno da 0 a 5, dove il punteggio massimo era riservato a guide dettagliate che anche un neofita potrebbe seguire. L’accordo inter-annotatore, misurato tramite *Intraclass Correlation Coefficient*, ha prodotto valori compresi tra 0,848 e 0,917 (media = 0,883), indicando un’affidabilità da buona a eccellente.

## I risultati: una vulnerabilità sistemica

Le performance dei modelli avversari presentano differenze significative. DeepSeek-R1 ha raggiunto il punteggio massimo di danno nel 90% dei casi (IC 95%: 80,77%-95,07%), seguito da Grok 3 Mini con l’87,14% (IC 95%: 77,34%-93,09%) e Gemini 2.5 Flash con il 71,43% (IC 95%: 59,95%-80,68%). Qwen3 235B, al contrario, si è rivelato largamente inefficace (12,86%), principalmente a causa de...