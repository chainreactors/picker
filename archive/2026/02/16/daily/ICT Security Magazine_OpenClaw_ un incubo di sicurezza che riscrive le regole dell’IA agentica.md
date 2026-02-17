---
title: OpenClaw: un incubo di sicurezza che riscrive le regole dell’IA agentica
url: https://www.ictsecuritymagazine.com/notizie/openclaw-sicurezza-ia/
source: ICT Security Magazine
date: 2026-02-16
fetch_date: 2026-02-17T04:21:37.877720
---

# OpenClaw: un incubo di sicurezza che riscrive le regole dell’IA agentica

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

![OpenClaw sicurezza dell'IA agentica](https://www.ictsecuritymagazine.com/wp-content/uploads/OpenClaw.jpeg)

# OpenClaw: un incubo di sicurezza che riscrive le regole dell’IA agentica

A cura di:[Redazione](#molongui-disabled-link)  Ore 16 Febbraio 202616 Febbraio 2026

OpenClaw non è un chatbot. È un agente autonomo che esegue azioni per conto dell’utente, con accesso diretto a file system, terminale, browser, e-mail, calendari e piattaforme di messaggistica. Nato nel novembre 2025 con il nome Clawdbot dalla mente dello sviluppatore austriaco [Peter Steinberger](https://en.wikipedia.org/wiki/OpenClaw), ribattezzato prima Moltbot e poi OpenClaw dopo dispute di trademark con Anthropic, il progetto ha raggiunto oltre 180.000 stelle su GitHub e oltre 2 milioni di visitatori in una sola settimana, con download settimanali che secondo [OX Security](https://www.csoonline.com/article/4129867/what-cisos-need-to-know-about-clawdbot-i-mean-moltbot-i-mean-openclaw.html) hanno toccato quota 720.000.

La promessa è affascinante: un assistente IA personale, open source, che gira in locale, comunica tramite WhatsApp, Telegram, Discord, Slack o Teams e che non si limita a rispondere – agisce. Prenota voli, gestisce la posta, automatizza workflow, controlla dispositivi smart home. Come ha sintetizzato [Token Security](https://www.darkreading.com/application-security/openclaw-ai-runs-wild-business-environments), OpenClaw è essenzialmente “Claude con le mani”: un LLM dotato di capacità esecutive concrete sul sistema dell’utente.

Il problema è che quelle stesse mani, se compromesse, diventano le mani dell’attaccante. E la comunità della cybersecurity lo ha capito in fretta – forse non abbastanza.

## La triade letale: perché OpenClaw è architetturalmente diverso

Simon Willison, lo sviluppatore che ha coniato il termine “prompt injection”, ha definito con precisione il profilo di [rischio degli agenti IA](https://www.ictsecuritymagazine.com/articoli/agenti-autonomi/) autonomi attraverso il concetto di **triade letale** (*lethal trifecta*). Un sistema diventa strutturalmente pericoloso quando combina tre caratteristiche: accesso a dati privati, esposizione a contenuti non fidati e capacità di comunicare verso l’esterno. [OpenClaw le possiede tutte e tre](https://venturebeat.com/security/openclaw-agentic-ai-security-risk-ciso-guide), simultaneamente e per design.

Questa non è una debolezza accidentale: è una conseguenza architettonica. L’agente legge e-mail e documenti, ingesta contenuti dal web, e può inviare messaggi o attivare automazioni senza supervisione umana continua. Dal punto di vista di un firewall enterprise, il traffico generato è un semplice HTTP 200. Per un SOC team che monitora il comportamento dei processi tramite EDR, l’attività appare legittima. La minaccia è **semantica**, non infrastrutturale – e questo la rende invisibile ai controlli tradizionali.

Come ha osservato [Ross McKerchar, CISO di Sophos](https://www.sophos.com/en-us/blog/the-openclaw-experiment-is-a-warning-shot-for-enterprise-ai-security), chiunque possa inviare un messaggio all’agente ottiene di fatto gli stessi privilegi dell’agente stesso. Un’e-mail contenente istruzioni malevole, un messaggio WhatsApp con un payload nascosto, un documento condiviso con prompt injection indiretta: tutti diventano vettori di compromissione senza che sia necessario alcun exploit tecnico nel senso tradizionale del termine.

È fondamentale, tuttavia, contestualizzare questo rischio. Come ha sottolineato il team di ricerca di [Trend Micro](https://www.trendmicro.com/en_us/research/26/b/what-openclaw-reveals-about-agentic-assistants.html) in un’analisi particolarmente lucida, OpenClaw non introduce nuove categorie di rischio: amplifica quelle già intrinseche al paradigma dell’IA agentica. Azioni non intenzionali, esfiltrazione di dati, esposizione a componenti non verificate sono problemi che riguardano tutti i sistemi agentici. La differenza è che la configurabilità senza restrizioni di OpenClaw – la possibilità di concedere permessi arbitrari senza alcun controllo di sicurezza forzato – eleva drammaticamente il livello di rischio concreto.

## CVE-2026-25253: l’anatomia di un RCE in un click

La vulnerabilità più grave documentata finora su OpenClaw è la [CVE-2026-25253](https://nvd.nist.gov/vuln/detail/CVE-2026-25253), classificata con un punteggio CVSS di 8.8 e catalogata come CWE-669 (*Incorrect Resource Transfer Between Spheres*). Scoperta dal ricercatore Mav Levin di [depthfirst](https://depthfirst.com/post/1-click-rce-to-steal-your-moltbot-data-and-keys), questa falla consente l’esecuzione remota di codice arbitrario con un singolo click.

Il meccanismo di exploit è elegante nella sua semplicità. La Control UI di OpenClaw accettava un parametro
`gatewayUrl`
dalla query string senza alcuna validazione, stabilendo automaticamente una connessione WebSocket che includeva il token di autenticazione dell’utente. Un attaccante poteva quindi creare una pagina web malevola che, una volta visitata dalla vittima, esfiltrava il token in pochi millisecondi.

Il passaggio critico successivo sfrutta una lacuna nell’implementazione dei WebSocket: il server di OpenClaw non validava l’header Origin delle connessioni, consen...