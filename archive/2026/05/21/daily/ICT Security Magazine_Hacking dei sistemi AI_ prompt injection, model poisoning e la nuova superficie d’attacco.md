---
title: Hacking dei sistemi AI: prompt injection, model poisoning e la nuova superficie d’attacco
url: https://www.ictsecuritymagazine.com/articoli/hacking-dei-sistemi-ai/
source: ICT Security Magazine
date: 2026-05-21
fetch_date: 2026-05-22T06:08:37.079012
---

# Hacking dei sistemi AI: prompt injection, model poisoning e la nuova superficie d’attacco

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

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Forum ICT Security 2026](https://www.ictsecuritymagazine.com/wp-content/uploads/forum-ict-security-banner-header-2026.jpg)](https://eventi.ictsecuritymagazine.com/eventi/forum-ict-security-2026)

![hacking dei sistemi ai](https://www.ictsecuritymagazine.com/wp-content/uploads/hacking-dei-sistemi-ai.jpeg)

# Hacking dei sistemi AI: prompt injection, model poisoning e la nuova superficie d’attacco

A cura di:[Redazione](#molongui-disabled-link)  Ore 21 Maggio 202622 Aprile 2026

C’è un paradosso al cuore della rivoluzione dell’intelligenza artificiale generativa: più un modello linguistico è capace di comprendere istruzioni complesse espresse in linguaggio naturale, più è vulnerabile a chi quelle istruzioni le sa costruire in modo malevolo. La potenza degli LLM (la stessa che li rende utili in mille contesti aziendali) è anche la radice strutturale delle minacce che li affliggono. Non si tratta di *bug* nel codice, risolvibili con una *patch*. Si tratta di vulnerabilità architetturali, intrinseche al modo in cui questi sistemi elaborano il testo, accedono a risorse esterne e interagiscono con altri componenti *software*.

Con l’integrazione pervasiva di modelli come GPT-4, Gemini e Claude nei processi aziendali (assistenti documentali, *copiloti* per il codice, agenti autonomi che inviano email e interrogano *database*) la superficie d’attacco si è estesa in modo radicale e, in larga parte, silenzioso. Non è più sufficiente proteggere il perimetro di rete, né applicare le consuete metodologie del *security testing* tradizionale. Serve una tassonomia nuova, un linguaggio condiviso per classificare minacce che non hanno precedenti nell’informatica classica.

## Il problema architetturale di fondo

Prima di entrare nella tassonomia degli attacchi, vale la pena fermarsi su una questione concettuale che molti addetti ai lavori ancora sottovalutano. Un modello linguistico non distingue strutturalmente tra istruzioni del sistema (*system prompt*), dati forniti dall’utente e contenuti recuperati da fonti esterne. Tutto confluisce nello stesso canale di elaborazione, lo stesso spazio vettoriale, la stessa logica di completamento. Questa assenza di separazione netta (che nei sistemi tradizionali sarebbe un errore di progettazione ovvio) è nei LLM una conseguenza necessaria del modo in cui apprendono a seguire le istruzioni.

Nel dicembre 2025, il NCSC (National Cyber Security Centre) britannico ha affrontato questa questione con inedita chiarezza in un [*blog post* del Technical Director](https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection) for Platforms Research “David C”, intitolato *Prompt injection is not SQL injection (it may be worse)*.

La tesi centrale è che il paragone istintivo tra *prompt injection* e *SQL injection* (un’analogia rassicurante perché la seconda è ormai un problema risolto) è in realtà fuorviante e pericoloso. “Sotto il cofano di un LLM non esiste distinzione tra ‘dati’ e ‘istruzioni’: esiste solo ‘*next token*‘”, scrive il funzionario. A differenza della *SQL injection*, che può essere eliminata alla radice con *query* parametrizzate, i LLM sono strutturalmente *inherently confusable*: la confusione non è un difetto correggibile, è la natura stessa del meccanismo. “È molto possibile che gli attacchi di *prompt injection* non vengano mai totalmente mitigati nel modo in cui lo sono stati quelli di *SQL injection*.”

È esattamente su questo piano che si sviluppano le minacce più insidiose.

## La tassonomia dell’hacking dei sistemi AI: da OWASP alle minacce emergenti

La fonte più autorevole per orientarsi in questo paesaggio è l’[OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/), giunta nel 2025 alla sua seconda edizione. Pubblicata alla fine del 2024 e aggiornata nel corso del 2025, la lista riflette non soltanto la ricerca accademica ma anche incidenti reali, segnalazioni di vulnerabilità documentate e il *feedback* di comunità di pratiche internazionali. Di seguito le categorie che più direttamente riguardano le nuove superfici d’attacco AI-specifiche.

### LLM01: la *prompt injection*, vulnerabilità numero uno

La *prompt injection* occupa il primo posto nella classifica OWASP per il secondo anno consecutivo, e la ragione è strutturale: i modelli linguistici non riescono a distinguere in modo affidabile tra istruzioni legittime e contenuti malevoli, anche quando questi ultimi sono invisibili all’occhio umano. Un *input* che manipola il comportamento del modello non ha bisogno di essere leggibile da un essere umano: è sufficiente che venga analizzato e interpretato dal modello stesso.

Si distinguono due varianti principali.

La ***prompt injection* diretta** avviene quando l’attaccante interagisce direttamente con il modello, inserendo istruzioni progettate per aggirare le linee guida del sistema. Tecniche comuni includono l’*obfuscation* (sostituzione di termini sensibili con sinonimi o codifiche alternative per eludere i filtri), la *virtualizzazione* (costruzione di scenari narrativi o giochi di ruolo in cui le istruzioni malevole appaiono legittime all’interno della finzione) e i *payload* frammentati, in cui l’istruzione pericolosa viene suddivisa in messaggi apparentemente innocui che il sistema viene poi indotto a ricombinare.

La ***prompt injection* indiretta** è più subdola e, per certi versi, più pericolosa. Si verifica quando il modello recupera contenuti da fonti esterne (pagine *web*, document...