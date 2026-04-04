---
title: Prompt injection negli agenti AI aziendali: il nuovo vettore che i SOC non stanno monitorando
url: https://www.ictsecuritymagazine.com/notizie/prompt-injection-negli-agenti-ai/
source: ICT Security Magazine
date: 2026-04-03
fetch_date: 2026-04-04T04:17:45.744088
---

# Prompt injection negli agenti AI aziendali: il nuovo vettore che i SOC non stanno monitorando

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

![prompt injection negli agenti AI](https://www.ictsecuritymagazine.com/wp-content/uploads/prompt-injection-1.jpeg)

# Prompt injection negli agenti AI aziendali: il nuovo vettore che i SOC non stanno monitorando

A cura di:[Redazione](#molongui-disabled-link)  Ore 3 Aprile 202627 Marzo 2026

La prompt injection negli agenti AI aziendali è emersa come una delle principali minacce per i sistemi basati su modelli linguistici e applicazioni enterprise. In questo approfondimento vengono analizzate le dinamiche con cui istruzioni nascoste, inserite in contenuti apparentemente legittimi come email o documenti, possono influenzare il comportamento degli agenti e portare a esfiltrazione di dati o azioni non autorizzate. Attraverso esempi concreti, vulnerabilità documentate e casi reali, il testo mette in evidenza come questo tipo di attacco non sia legato a un singolo bug, ma a un limite strutturale dei LLM, offrendo una panoramica utile a comprendere rischi, impatti e implicazioni per la sicurezza e la governance dei sistemi AI.

Il 13 giugno 2025, Microsoft ha corretto in silenzio una vulnerabilità critica in Microsoft 365 Copilot. Nessuna notifica proattiva agli utenti, nessun advisory con toni allarmistici. Solo un fix server-side distribuito come parte del Patch Tuesday di giugno 2025, con una CVE assegnata ([CVE-2025-32711](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32711)) e un CVSS score di 9.3. Il nome in codice dato dai ricercatori di [Aim Security](https://www.aim.security/lp/aim-labs-echoleak-m365) era EchoLeak. Era il primo exploit zero-click documentato contro un agente AI in produzione, e funzionava con una singola email. Nessun malware. Nessun payload. Nessun click. Solo testo.

## Il problema strutturale: i modelli linguistici non distinguono istruzioni da dati

Prima di analizzare i casi documentati, è necessario comprendere perché la prompt injection non sia un bug correggibile con una patch, ma una vulnerabilità architettonica dei modelli linguistici.

Un LLM riceve in input una sequenza di token. A quel modello non importa se quei token provengono dal prompt di sistema scritto dallo sviluppatore, dall’input dell’utente, da un documento recuperato via RAG, da una email processata dall’agente o da una pagina web visitata durante una sessione di browsing. Tutti i token finiscono nella stessa finestra di contesto e vengono trattati con lo stesso livello di fiducia. Il modello è addestrato a seguire istruzioni espresse in linguaggio naturale. Se un’istruzione appare nella finestra di contesto, il modello tende a eseguirla, indipendentemente da dove provenga.

Come [riconosciuto da OpenAI stessa in un post pubblico del 22 dicembre 2025](https://openai.com/index/hardening-atlas-against-prompt-injection/) relativo al browser agentivo ChatGPT Atlas: “Prompt injection, much like scams and social engineering on the web, is unlikely to ever be fully ‘solved’.” Non è una resa: è una presa di coscienza dell’architettura del problema. La finestra di contesto è un mezzo fisico uniforme. Fare distinzioni semantiche su cosa sia “istruzione” e cosa sia “dato” in modo affidabile e universale è un problema non risolto nella ricerca attuale.

L’[OWASP Top 10 for LLM Applications 2025](https://owasp.org/www-project-top-10-for-large-language-model-applications/) ha classificato la prompt injection al primo posto tra le vulnerabilità critiche per il secondo anno consecutivo, riconoscendo che questa classe di vulnerabilità sfrutta il design stesso degli LLM, non difetti correggibili con patch convenzionali.

## La tassonomia degli attacchi: diretti, indiretti e cross-agente

Il termine “prompt injection” copre una famiglia di tecniche con caratteristiche operative molto diverse. La distinzione più importante per i team di sicurezza è quella tra attacchi diretti e indiretti.

La prompt injection diretta è l’attacco più intuitivo: un utente malintenzionato invia al sistema AI un input costruito per sovrascrivere le istruzioni di sistema e far compiere all’agente azioni non autorizzate. È il classico “Ignora le istruzioni precedenti e fai X.” È anche il tipo di attacco più facile da contrastare con filtri di input.

La prompt injection indiretta è il vettore che i SOC non stanno monitorando, e che nel 2025 ha generato i casi più gravi. In questo caso l’attaccante non interagisce direttamente con l’agente AI: inserisce istruzioni malevole in contenuti che l’agente elaborerà in futuro come parte del suo lavoro normale. Un documento condiviso, una email in arrivo, una pagina web visitata durante il browsing, un record in un sistema CRM. Quando l’agente processa quel contenuto in risposta a una richiesta legittima dell’utente, le istruzioni iniettate si attivano.

Come analizzato da [Lakera AI](https://www.lakera.ai/), l’efficacia degli attacchi indiretti deriva dall’impossibilità strutturale per il modello di distinguere il testo in un documento dal testo delle sue istruzioni originali: entrambi arrivano come flusso di token nella stessa finestra di contesto.

La prompt injection cross-agente è la variante più sofisticata, documentata per la prima volta in ambienti di produzione nel tardo 2025. In sistemi multi-agente dove più modelli AI cooperano con diversi...