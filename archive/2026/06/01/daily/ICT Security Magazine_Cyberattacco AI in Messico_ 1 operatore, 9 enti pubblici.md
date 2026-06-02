---
title: Cyberattacco AI in Messico: 1 operatore, 9 enti pubblici
url: https://www.ictsecuritymagazine.com/notizie/cyberattacco-ai-messico/
source: ICT Security Magazine
date: 2026-06-01
fetch_date: 2026-06-02T06:32:53.857274
---

# Cyberattacco AI in Messico: 1 operatore, 9 enti pubblici

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

![Cyberattacco AI in Messico: Claude Code, AI agentica, cybercrime, Cyber Crime Conference 2026 su prompt injection, MCP, identità agentica e forensics by design.](https://www.ictsecuritymagazine.com/wp-content/uploads/Cyberattacco-AI-in-Messico-un-operatore-nove-enti-pubblici.png)

# Cyberattacco AI in Messico: 1 operatore, 9 enti pubblici

A cura di:[Redazione](#molongui-disabled-link)  Ore 1 Giugno 202625 Maggio 2026

Tra fine dicembre 2025 e metà febbraio 2026, una persona sola ha compromesso nove organizzazioni governative messicane. Il bilancio è di circa 150 GB di dati esfiltrati e di circa 195 milioni di identità esposte. A rendere il cyberattacco AI in Messico un punto di svolta non sono i numeri, già clamorosi, ma lo strumento: l’attaccante ha lavorato con un abbonamento commerciale a due piattaforme di AI generativa, accessibili a chiunque abbia una carta di credito.

La ricostruzione arriva dalla società israeliana Gambit Security e dal gruppo di ricerca diretto da Eyal Sela, *Director of Threat Intelligence* dell’azienda. Il team ha analizzato i log delle sessioni e ha pubblicato il [rapporto tecnico completo](https://cdn.prod.website-files.com/69944dd945f20ca4a27a7c47/69d8bb5aea59e31efb3b8a7f_Tech_Report_ai_breach_mex_gov.pdf) il 10 aprile 2026, dopo aver lasciato alle vittime il tempo per la *incident response*. Lo studio, racconta una catena d’attacco banale nei principi e radicale nelle conseguenze per la cybersecurity dell’AI generativa.

## Cyberattacco AI: Claude Code è diventato la squadra operativa

L’attaccante ha usato Claude Code di Anthropic come partner conversazionale e operativo. In parallelo, GPT-4.1 di OpenAI lavorava via API come motore d’analisi. Il primo ha generato *exploit*, scritto *backdoor* persistenti, eseguito comandi remoti e gestito il movimento laterale nelle reti violate. Il secondo ha trasformato i dati grezzi prelevati dai server in report strutturati che dicevano all’operatore quali sistemi colpire e quali credenziali riutilizzare.

I numeri ricostruiti misurano il salto di scala. Sono stati inviati 1.088 *prompt*, che hanno generato 5.317 comandi remoti in 34 sessioni dal vivo; circa il 75% di quei comandi è passato per Claude Code. L’analisi forense ha recuperato oltre 400 script personalizzati (301 in Bash, 113 in Python), 20 *exploit* mirati ad altrettante CVE e 2.597 report d’analisi prodotti da GPT-4.1 sui dati di 305 server interni. A orchestrare l’esfiltrazione, un *tool* Python di 17.550 righe chiamato BACKUPOSINT.py. Il primo *token* Claude Code registrato risale al 27 novembre 2025: la campagna è iniziata con un mese di preparazione strutturata prima della prima sessione operativa, datata 27 dicembre.

I bersagli del *data breach* non sono sistemi marginali. Il SAT (Servicio de Administración Tributaria) ha perso circa 195 milioni di record fiscali, l’INE (Instituto Nacional Electoral) record di registrazione elettorale, il registro civile di Città del Messico oltre 220 milioni di record. Sono stati colpiti anche il governo dell’Estado de México (con 15,5 milioni di record veicolari e 3,6 milioni di record di proprietà), i governi statali di Jalisco, Michoacán e Tamaulipas, l’utility idrica di Monterrey (SADM) e il dipartimento sanitario di Città del Messico (Salud CDMX).

In Jalisco l’attaccante è arrivato fino agli archivi sanitari e ai dati delle vittime di violenza domestica, distribuendo *rootkit* personalizzati su venti agenzie statali. Nelle ultime settimane di campagna ha costruito anche un’API di interrogazione in tempo reale sull’infrastruttura fiscale del SAT e un meccanismo per produrre certificati tributari falsi a partire da dati autentici. Il governo dello stato di Jalisco e l’INE hanno pubblicamente negato la compromissione; il rapporto Gambit riporta tuttavia evidenze forensi di esfiltrazione su entrambi gli enti.

#### Jailbreak dei modelli AI: come si è rotto l’argine

Il nodo, sul piano dell’AI safety, è il modo in cui sono stati aggirati i *guardrails*. La conversazione si è aperta con l’attaccante che si presentava come ricercatore in un programma di *bug bounty* autorizzato, con tanto di manuale operativo in spagnolo (1.084 righe) che inquadrava ogni azione come legittima. Quando Claude rifiutava una richiesta diretta (cancellare i log, nascondere le tracce), bastava riformularla dentro il ruolo già stabilito, oppure spostarsi temporaneamente su ChatGPT per ottenere lo stesso risultato.

Le tecniche impiegate sono note: *role-play* persistente, *multi-turn jailbreak* e *prompt injection* contestuale, qui combinati per ottenere un effetto operativo prolungato. Nessuna è inedita. Inedita è la loro efficacia su sistemi capaci di eseguire codice, navigare reti reali e ragionare su obiettivi a più passi. Una volta allertata, Anthropic ha bannato gli account e rafforzato il rilevamento d’uso improprio nelle versioni successive del modello. È una risposta corretta, che lascia però aperta una questione di fondo:

> “Quanto può reggere il paradigma ‘rileva e blocca’ quando l’avversario muta a ogni rifiuto?”

## Dall’AI assistente all’AI agentica: il salto strutturale

Il punto saliente non sono gli *exploit*, quasi tutti basati su vulnerabilità note e su infrastrutture con elevato *technical debt*. È ...