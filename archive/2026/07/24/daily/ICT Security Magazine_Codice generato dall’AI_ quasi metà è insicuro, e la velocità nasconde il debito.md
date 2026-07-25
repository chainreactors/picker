---
title: Codice generato dall’AI: quasi metà è insicuro, e la velocità nasconde il debito
url: https://www.ictsecuritymagazine.com/articoli/codice-generato-dall-ai-sicurezza/
source: ICT Security Magazine
date: 2026-07-24
fetch_date: 2026-07-25T05:00:35.629657
---

# Codice generato dall’AI: quasi metà è insicuro, e la velocità nasconde il debito

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
  + [Prospettive](https://www.ictsecuritymagazine.com/argomenti/prospettive/)
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

![Codice generato dall'AI](https://www.ictsecuritymagazine.com/wp-content/uploads/Codice-generato-dallAI.png)

# Codice generato dall’AI: quasi metà è insicuro, e la velocità nasconde il debito

A cura di:[Redazione](#molongui-disabled-link)  Ore 24 Luglio 202616 Luglio 2026

Il codice generato dall’AI ha smesso di essere una curiosità da laboratorio ed è entrato nel flusso di lavoro quotidiano di gran parte degli sviluppatori, spesso senza che l’organizzazione se ne sia accorta davvero. La promessa è evidente e reale: scrivere più in fretta, delegare le parti ripetitive, abbassare la barriera d’ingresso a chi programma poco. Il problema è che la sicurezza non è migliorata alla stessa velocità della produttività, e i numeri cominciano a dirlo con precisione. Il *Veracode GenAI Code Security Report*, nella sua prima edizione del luglio 2025, ha messo alla prova oltre cento modelli su ottanta compiti in cui esisteva sia una via sicura sia una insicura, e ha misurato una cosa precisa: [nel 45% dei casi](https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/) il modello sceglie la via insicura.

Il dato più scomodo non è la percentuale in sé, ma la sua ostinazione. L’[aggiornamento di primavera 2026 del report](https://www.veracode.com/blog/spring-2026-genai-code-security/), esteso a oltre 150 modelli tra cui i più recenti (GPT-5.1 e 5.2, Gemini 3, Claude 4.5 e 4.6), fotografa la stessa situazione di due anni prima: solo il 55% del codice generato è sicuro, mentre la correttezza sintattica ha ormai superato il 95%. I modelli hanno imparato benissimo a produrre codice che funziona e compila, e questo genera fiducia; la stessa fiducia non è però giustificata sul piano della sicurezza, dove i progressi sono stati minimi. Va detta un’eccezione, per onestà: la famiglia GPT-5 con *reasoning* esteso ha toccato, nella rilevazione dell’ottobre 2025, il tasso più alto mai registrato, tra il 70 e il 72%, ma le release successive non hanno consolidato il vantaggio, restando nel margine d’errore dei modelli precedenti. E anche quel picco lascia vulnerabile quasi un frammento di codice su tre, lontano da un livello accettabile in produzione. Chi accetta un suggerimento perché “gira” sta valutando la funzionalità, non la resistenza a un attacco, e il modello ha ottimizzato esattamente per la prima cosa.

## Perché il codice generato dall’AI è insicuro per default

La radice del problema è nel modo in cui questi modelli imparano. Un *large language model* è addestrato su enormi quantità di codice pubblico, che include tanto le buone pratiche quanto gli esempi vulnerabili, i tutorial semplificati e le scorciatoie insicure che popolano forum e repository. Il modello non distingue il codice sicuro da quello pericoloso: riproduce ciò che è statisticamente plausibile nel contesto, e il pattern insicuro spesso è più frequente di quello corretto. Manca inoltre la cosa che un buon sviluppatore porta con sé, cioè il contesto di minaccia: chi userà questa funzione, con quali input ostili, in quale posizione della superficie d’attacco.

Il dato di addestramento, però, spiega solo una parte, e i numeri dell’aggiornamento 2026 mostrano dove il problema si concentra davvero. I modelli non sbagliano ovunque: sulla *SQL injection* il codice sicuro sale all’82% e sugli algoritmi crittografici deboli all’86%, perché sono vulnerabilità riconoscibili come pattern locali, viste e riviste etichettate come insicure. Crollano invece dove serve seguire un input non fidato attraverso più funzioni, trasformazioni e file fino al punto in cui viene usato: sul *cross-site scripting* solo il 15% del codice supera i controlli, sulla *log injection* appena il 13%, e su queste categorie Veracode segnala che la tendenza sta perfino peggiorando. È la differenza tra riconoscere una forma e ricostruire un contesto, cioè l’analisi di *dataflow* interprocedurale, difficile da fare in modo consistente perfino per una persona esperta. Non a caso il linguaggio peggiore è Java, fermo al 29% di codice sicuro contro il 62% di Python, e non a caso i modelli con *reasoning* recuperano qualcosa, perché i passaggi di ragionamento funzionano come una revisione interna del codice. Non è dunque un limite che la prossima generazione di modelli risolverà da sé: è strutturale, legato al tipo di analisi che manca, non alla potenza di calcolo.

## Non è (solo) un problema di bug: il debito di sicurezza su scala

La differenza rispetto al passato non è la singola vulnerabilità, che c’è sempre stata, ma la scala e la velocità con cui si moltiplica. Lo ha misurato in produzione Apiiro, su decine di migliaia di repository di aziende Fortune 50 tra dicembre 2024 e giugno 2025: gli sviluppatori assistiti dall’AI committano da tre a quattro volte più spesso e generano circa [dieci volte più problemi di sicurezza](https://www.theregister.com/2025/09/05/ai_code_assistants_security_problems/), con gli errori di sintassi in calo del 76% ma i difetti architetturali in aumento del 153%. È, in numeri di produzione, esattamente la tesi di partenza: codice più corretto in superficie e più fragile nella struttura. Lo stesso pattern insicuro, generato una volta,...