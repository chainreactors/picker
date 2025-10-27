---
title: Una Breve Guida ai Test di Sicurezza delle API by Equixly
url: https://www.ictsecuritymagazine.com/notizie/una-breve-guida-ai-test-di-sicurezza-delle-api-by-equixly/
source: ICT Security Magazine
date: 2024-09-13
fetch_date: 2025-10-06T18:29:50.897194
---

# Una Breve Guida ai Test di Sicurezza delle API by Equixly

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

![Equixly: test di sicurezza delle API](https://www.ictsecuritymagazine.com/wp-content/uploads/Test-di-Sicurezza-delle-API-by-Equixly.jpg)

# Una Breve Guida ai Test di Sicurezza delle API by Equixly

A cura di:[Redazione](#molongui-disabled-link)  Ore 12 Settembre 202416 Ottobre 2024

Cosa comprende un test di sicurezza delle API:

* Valutare le API per individuare falle di sicurezza, difetti e vulnerabilità
* Valutare la qualità dei meccanismi di sicurezza impiegati, come autorizzazione e autenticazione
* Valutare la capacità delle API di resistere agli attacchi mirati così come agli attacchi in cui le API vulnerabili svolgono un ruolo secondario

I test di sicurezza delle API sono una componente distinta ed essenziale dei test di sicurezza.

### Perché Separare i Test di Sicurezza delle API?

Mentre altri tipi di test, come gli “integration test” e “unit test”, sono ben integrati nel processo di sviluppo, i [test di sicurezza](https://www.ictsecuritymagazine.com/articoli/no-secure-sdlc-no-party-perche-e-fondamentale-implementare-la-sicurezza-in-ogni-fase-del-ciclo-di-vita-del-prodotto/) non hanno ancora raggiunto lo stesso livello di integrazione in molte organizzazioni.

Il sondaggio “State of APIs 2022” ha rivelato che i test di sicurezza rappresentavano solo il [4,0% delle risorse](https://stateofapis.com/) dedicate ai test delle API. I test funzionali, di integrazione e di accettazione erano i tre tipi di test delle API più prevalenti eseguiti dai partecipanti al sondaggio.

I risultati si basavano su 850 risposte da professionisti di oltre 100 paesi. Molti partecipanti erano sviluppatori.

Queste statistiche ci lasciano a bocca aperta. Le organizzazioni devono integrare molto meglio i test di sicurezza; il 4% è sproporzionatamente basso.

Anche se la situazione è migliorata negli ultimi due anni, è difficile immaginare miglioramenti radicali, specialmente considerando il costante [aumento degli incidenti di sicurezza delle API](https://equixly.com/blog/2024/01/05/top-5-api-security-incidents-of-2023/).

Com’è possibile che le API, una componente cruciale dell’attuale digitalizzazione dei settori economici, ricevano così poca attenzione riguardo alla sicurezza?

Una ragione potrebbe essere che sia i team di sviluppo che quelli di sicurezza sono sovraccarichi di lavoro e sotto pressione per le scadenze, quindi le organizzazioni fanno dei compromessi a scapito dei test di sicurezza delle API.

Qualunque sia la ragione, una cosa è certa: i test di sicurezza sono diversi dai test “classici” effettuati in fase di sviluppo e irriducibili a qualsiasi altro tipo di test – sia che si tratti di un altro tipo di test delle API o di test di sicurezza generici delle applicazioni.

Dal rilascio della prima [OWASP Top 10 API Security Risks](https://equixly.com/blog/2023/11/28/owasp-api-security-top-10/) nel 2019, abbiamo un quadro di riferimento specializzato per la sicurezza informatica delle API su cui costruire il nostro programma di sicurezza delle API, con i test di sicurezza come componente critica.

OWASP, l’Open Worldwide Application Security Project, ha riconosciuto la natura delle sfide di sicurezza delle API, ha condotto ricerche approfondite su incidenti di sicurezza delle API effettivamente segnalati, attacchi informatici e programmi di bug bounty, e ha creato linee guida per i rischi o vulnerabilità di sicurezza delle API più comuni e gravi.

Nei test di sicurezza adottiamo la prospettiva del nemico, cioè dell’attore minaccioso/hacker/attaccante. Non testiamo solo l’API esponendola a tutti gli scenari possibili in cui deve resistere ai requisiti degli utenti, sia scenari di base che anomali. Il nostro approccio non è quello dell’utente.

# ![Software e Test delle API](https://equixly.com/assets/blog/guide-to-api-security-testing/testing-api-security-issues.svg)

# Test di Sicurezza delle API e DAST, SAST, IAST e SCA

I termini “DAST”, “SAST”, “IAST” o “SCA” sono piuttosto comuni. Di cosa si tratta?

#### DAST

DAST sta per “test di sicurezza dinamico delle applicazioni”. Rientra nella categoria dei test black box, il che significa che il tester non possiede informazioni sul codice, sul design, sulla struttura e sulla superficie d’attacco del target.

Un DAST valuta la sicurezza del target in uno stato operativo, cioè durante l’esecuzione, motivo per cui è chiamato dinamico. Aiuta a stabilire se ci sono vulnerabilità basate sulle risposte del target alle richieste inviate.

I vantaggi dei DAST includono:

* È indipendente dal linguaggio e dalla piattaforma.
* Produce meno falsi positivi rispetto ad altri metodi di test.
* È efficace per identificare configurazioni di sicurezza errate.

Gli svantaggi di DAST sono i seguenti:

* È difficile da scalare.
* Non funziona per la scoperta/”discovery” delle API.
* Non ha visibilità sul codice.
* È lento.

#### SAST

L’acronimo SAST sta per “test di sicurezza statico delle applicazioni”. È un test white box, il che significa che il tester conosce il funzionamento interno del target di test – design, codice e struttura.

Un SAST è diverso da un DAST in quanto aiuta a trovare vulnerabilità nel codice sorgente. Analizza il codice senza eseguirlo, da cui deriva il termine “statico”.

Oltre a trovare vulnerabilità di sicurezza, come problemi di vali...