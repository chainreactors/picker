---
title: Non-Human Identities e agenti di intelligenza artificiale: governare l’identità delle macchine
url: https://www.ictsecuritymagazine.com/articoli/non-human-identities/
source: ICT Security Magazine
date: 2026-07-06
fetch_date: 2026-07-07T06:05:03.846737
---

# Non-Human Identities e agenti di intelligenza artificiale: governare l’identità delle macchine

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

![](https://www.ictsecuritymagazine.com/wp-content/uploads/non-human-identities.png)

# Non-Human Identities e agenti di intelligenza artificiale: governare l’identità delle macchine

A cura di:[Vincenzo Calabrò](#molongui-disabled-link)  Ore 6 Luglio 20266 Luglio 2026

Nelle organizzazioni, le Non-Human Identities (NHI) superano ormai quelle umane di due ordini di grandezza e gli AI agent ne rappresentano la classe più difficile da governare, in quanto autonomi e operanti su delega di un utente. L’articolo ripercorre i rischi rilevati dalla OWASP Non-Human Identities Top 10 e le risposte che emergono dalla letteratura, dall’authenticated delegation al framework della Cloud Security Alliance. Successivamente, il tema viene inserito nel contesto normativo europeo e nazionale e viene proposta un’architettura di riferimento basata su un caso d’uso della Pubblica Amministrazione.

## Non-Human IdentitiesI ntroduzione

Per oltre un decennio, l’identity and access management si è occupato quasi esclusivamente delle persone, dei loro accessi e del ciclo di vita scandito dai processi HR per ciascun account. Nel frattempo, quasi in sordina, la popolazione delle identità digitali ha cambiato natura. Secondo la ricerca “2025 Identity Security Landscape” di CyberArk, condotta su 2.600 decision maker in venti Paesi, le machine identity superano quelle umane con un rapporto di oltre 80 a 1 e quasi la metà di queste dispone di accessi sensibili o privilegiati.

Inoltre, il 68% delle organizzazioni dichiara di non possedere controlli specifici per la sicurezza delle identità nell’ambito dell’intelligenza artificiale [[2]](#_ftn2). L’edizione 2026 dell’analoga rilevazione di Palo Alto Networks stima un rapporto medio di 109 a 1 e prevede una crescita degli AI agent dell’85% nei successivi 12 mesi [[3]](#_ftn3). Le stime variano molto a seconda della metodologia utilizzata (le misurazioni telemetriche sugli ambienti cloud, per esempio, arrivano a rapporti di ordini di grandezza superiori), ma la tendenza è chiara.

A rendere il fenomeno qualitativamente diverso è l’ingresso degli agenti basati su large language model, identità non umane che non si limitano a eseguire comandi, ma che, entro margini di autonomia crescenti, decidono quali azioni compiere e con quali strumenti. Nell’articolo se ne esaminano i rischi e il quadro regolatorio, per arrivare a un’architettura di riferimento.

## Il perimetro delle Non-Human Identities

L’OWASP definisce [le Non-Human Identities (NHI)](https://www.ictsecuritymagazine.com/notizie/non-human-identity-nis2-e-d-lgs-138-2024/) come le identità impiegate per identificare, autenticare e autorizzare entità software (applicazioni, workload, API, bot) nell’accesso a risorse protette [[1]](#_ftn1). La categoria comprende [service account, API key, token OAuth, certificati e chiavi crittografiche](https://www.ictsecuritymagazine.com/digital-id-security/identita-non-umane-2/), nonché le identità dei container e delle funzioni serverless (Figura 1). A differenza delle identità umane, le NHI non hanno trigger di ciclo di vita paragonabili a quelli contrattuali: non ci sono assunzioni e cessazioni. Nascono durante la fase di provisioning di un’applicazione e spesso sopravvivono, dimenticate, ai progetti che le hanno generate.

![](https://www.ictsecuritymagazine.com/wp-content/uploads/fig1-4.png)

Figura 1 – Tassonomia delle Non-Human Identities e collocazione degli AI agent.

La OWASP Non-Human Identities Top 10, pubblicata nel 2025, ha sistematizzato i rischi della categoria a partire da incidenti reali e da dati di settore (survey, CVE) [[1]](#_ftn1). Ai primi due posti si collocano l’improper offboarding e il secret leakage; l’elenco completo è riportato nella Tabella 1. Per quanto riguarda la casistica, nel gennaio 2024, l’attore statuale Midnight Blizzard ha raggiunto l’ambiente di produzione di Microsoft sfruttando un’applicazione legacy OAuth non censita e dotata di privilegi elevati; pochi mesi prima, la compromissione di un service account aveva esposto il sistema di supporto clienti di Okta [[1]](#_ftn1).

## L’AI agent come NHI sui generis

Sarebbe riduttivo considerare un agente AI come un semplice servizio dotato di un modello linguistico. Un agente pianifica sequenze di azioni non predeterminate, sceglie gli strumenti da utilizzare e può generare sub-agenti che necessitano di credenziali proprie. Le sue istanze nascono e muoiono nell’arco di una sessione, troppo in fretta per qualunque processo manuale di provisioning e revoca. Inoltre, opera su delega di un utente umano e, se l’architettura non lo impedisce, finisce per condividere con quest’ultimo permessi che vanno ben oltre il compito assegnato.

La letteratura recente concorda nel ritenere inadeguati i protocolli IAM tradizionali, concepiti per utenti umani o macchine dal comportamento statico. South et al. propongono un framework di autenticazione basato sulla delega che estende OAuth 2.0 e OpenID Connect con credenziali e metadati specifici per gli agenti, in modo da mantenere catene di responsabilità verificabili tra l’utente che delega, l’agente e il servizio[[4]](#_ftn4). La Cloud Security Alliance, dal canto suo, d...