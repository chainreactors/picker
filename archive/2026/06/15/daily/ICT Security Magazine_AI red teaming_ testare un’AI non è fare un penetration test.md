---
title: AI red teaming: testare un’AI non è fare un penetration test
url: https://www.ictsecuritymagazine.com/cyber-security/ai-red-teaming/
source: ICT Security Magazine
date: 2026-06-15
fetch_date: 2026-06-16T07:17:00.132927
---

# AI red teaming: testare un’AI non è fare un penetration test

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

![AI red teaming](https://www.ictsecuritymagazine.com/wp-content/uploads/AI-red-teaming.png)

# AI red teaming: testare un’AI non è fare un penetration test

A cura di:[Redazione](#molongui-disabled-link)  Ore 15 Giugno 20269 Giugno 2026

AI red teaming è il nome che ha preso una disciplina nata da una scoperta scomoda: i sistemi basati su modelli linguistici falliscono in modi che il collaudo di sicurezza tradizionale non sa nemmeno cercare. Una applicazione classica si rompe in modo deterministico, e un penetration test la sonda di conseguenza: dato un input, esiste o non esiste una vulnerabilità. Un modello generativo, invece, risponde allo stesso prompt in modi diversi a seconda del contesto, della formulazione, persino del caso. La domanda non è più se sia vulnerabile, ma con quale frequenza un certo attacco riesce. Questo cambia tutto: il metodo, gli strumenti, il senso stesso del risultato.

Conviene dirlo subito per sgombrare un equivoco diffuso. L’*AI red teaming* non è un penetration test applicato a un modello, e non è nemmeno la versione AI dell’emulazione avversaria che la sicurezza offensiva pratica da anni sull’infrastruttura. Condivide con quelle discipline la postura, pensare come un attaccante, ma cambia il bersaglio e la natura della prova. Si collauda un comportamento probabilistico, non una logica fissa, e il verdetto non è binario.

## Perché un modello non si collauda come un’applicazione

La differenza di fondo è statistica. Quando si verifica una applicazione tradizionale, una falla c’è o non c’è, e una volta trovata si corregge. Quando si verifica un modello, lo stesso attacco può riuscire una volta su dieci o nove volte su dieci, e quel tasso è esso stesso il risultato. Per questo nell’*AI red teaming* non si parla di vulnerabilità presente o assente, ma di tasso di successo di un attacco misurato su una categoria di tentativi. Una difesa che blocca il 70 per cento dei *jailbreak* non è sicura né insicura: è descritta da quel numero, che va confrontato nel tempo e contro nuove varianti.

C’è poi una differenza di superficie. Il penetration test sonda reti, applicazioni, configurazioni. L’*AI red teaming* sonda qualcosa che quegli strumenti non vedono: il comportamento del modello sollecitato in modo ostile. Le tecniche che cataloga sono specifiche, e molte non hanno equivalente nel mondo tradizionale, dalla manipolazione dei dati di addestramento all’estrazione di informazioni dal modello, dall’aggiramento delle protezioni alla [manipolazione dei sistemi AI](https://www.ictsecuritymagazine.com/articoli/hacking-dei-sistemi-ai/) tramite input costruiti ad arte. Sono attacchi al modo in cui il modello ragiona, non al server che lo ospita.

## Il bersaglio non è solo il prompt, è il loop

Per un po’ l’*AI red teaming* ha coinciso con la ricerca di prompt malevoli isolati: una frase che induce il modello a violare le proprie regole. È una parte del lavoro, ma è la parte facile, e oggi è la meno rappresentativa. Con la diffusione dei sistemi agentici, dove il modello non si limita a rispondere ma pianifica, invoca strumenti e agisce in più passaggi, il bersaglio si è spostato dal singolo prompt all’intero ciclo di esecuzione.

Testare un agente significa attaccarne il loop. Le sonde più serie non si fermano alla prompt injection diretta, ma esercitano la prompt injection indiretta, nascosta dentro un documento o una pagina web che l’agente leggerà, l’avvelenamento delle basi di conoscenza usate per il recupero, la manomissione della memoria conversazionale, le chiamate a strumenti non sicure, l’abuso dei protocolli di integrazione con sistemi esterni, fino all’esfiltrazione di dati attraverso catene di più passi. È il terreno su cui si misura la sicurezza reale dei sistemi di [AI agentica](https://www.ictsecuritymagazine.com/articoli/ai-agentica/), e dove una singola prova isolata non dice quasi nulla: ciò che conta è cosa l’agente fa quando un’istruzione ostile entra a metà di un compito legittimo.

## L’AI red teaming ha già i suoi framework

La novità del biennio è che questa disciplina ha smesso di essere artigianato individuale e ha acquisito riferimenti condivisi. Nel gennaio 2025 il progetto OWASP dedicato alla sicurezza dell’AI generativa ha pubblicato la sua [guida al red teaming GenAI](https://genai.owasp.org/2025/01/22/announcing-the-owasp-gen-ai-red-teaming-guide/), una metodologia strutturata e basata sul rischio che copre l’intero spettro, dalle vulnerabilità del modello come tossicità e *bias* ai problemi di integrazione di sistema come l’uso improprio delle API e l’esposizione dei dati. È costruita sopra la lista OWASP Top 10 per le applicazioni LLM, dove la prompt injection figura come prima minaccia.

Sul versante della conoscenza degli attacchi, il riferimento è [MITRE ATLAS](https://atlas.mitre.org/), l’equivalente del framework ATT&CK calato sui sistemi di intelligenza artificiale: una base di conoscenza di tattiche e tecniche avversarie tratte da osservazioni reali e da dimostrazioni dei red team, che a inizio 2026 raccoglie oltre ottanta tecniche distribuite su quattordici categorie tattiche. ATLAS dà ai team un vocabolario per tradurre rischi astratti ...