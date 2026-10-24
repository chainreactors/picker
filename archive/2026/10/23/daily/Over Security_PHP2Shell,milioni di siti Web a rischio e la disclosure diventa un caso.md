---
title: PHP2Shell,milioni di siti Web a rischio e la disclosure diventa un caso
url: https://www.securityinfo.it/2026/10/23/php2shellrischio-milioni-di-siti-web-a-rischio-e-la-disclosure-diventa-un-caso/
source: Over Security
date: 2026-10-23
fetch_date: 2026-10-24T06:47:49.294946
---

# PHP2Shell,milioni di siti Web a rischio e la disclosure diventa un caso

Aggiornamenti recenti Ottobre 23rd, 2026 6:17 AM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [PHP2Shell,milioni di siti Web a rischio e la disclosure diventa un caso](https://www.securityinfo.it/2026/10/23/php2shellrischio-milioni-di-siti-web-a-rischio-e-la-disclosure-diventa-un-caso/)
* [Midnight Mimosa, ancora malware Android installato prima dell’acquisto](https://www.securityinfo.it/2026/10/09/midnight-mimosa-ancora-malware-android-installato-prima-dellacquisto/)
* [Bitdefender crea una VPN per gli agenti AI](https://www.securityinfo.it/2026/09/21/bitdefender-crea-una-vpn-per-gli-agenti-ai/)
* [No Hat 2026, a Bergamo l’hacking incontra AI, cyber-spionaggio e droni](https://www.securityinfo.it/2026/09/11/no-hat-2026-a-bergamo-lhacking-incontra-ai-cyber-spionaggio-e-droni/)
* [Claude evade (di nuovo) e attacca tre aziende reali](https://www.securityinfo.it/2026/08/04/claude-evade-di-nuovo-e-compromette-tre-aziende-reali/)

* [Home](https://www.securityinfo.it)
* [News](https://www.securityinfo.it/category/news/)
* [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/)
* [Opinioni](https://www.securityinfo.it/category/opinioni/)
* [Top Malware](https://www.securityinfo.it/top-malware-page/)
* [Minacce](https://www.securityinfo.it/category/minacce-2/)
* [Guide alla sicurezza](http://www.securityinfo.it/guide-alla-sicurezza/)
* [Podcast](https://www.securityinfo.it/podcast-page/)
* [Strumenti Utili](https://www.securityinfo.it/category/strumenti-utili/)

* Search for:

## PHP2Shell,milioni di siti Web a rischio e la disclosure diventa un caso

Ott 23, 2026  [Redazione news](https://www.securityinfo.it/author/redazione-news/ "Articoli scritti da Redazione news")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Attacchi](https://www.securityinfo.it/category/approfondimenti/attacchi/), [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Tecnologia](https://www.securityinfo.it/category/news/tecnologia-news/), [Vulnerabilità](https://www.securityinfo.it/category/approfondimenti/vulnerabilita-approfondimenti/)
 [0](https://www.securityinfo.it/2026/10/23/php2shellrischio-milioni-di-siti-web-a-rischio-e-la-disclosure-diventa-un-caso/#respond)

---

**Le falle CVE-2026-109618 e CVE-2026-109619 consentono, in determinate condizioni, l’esecuzione di codice da remoto senza autenticazione. Individuate attraverso una combinazione di ricerca tradizionale e strumenti di intelligenza artificiale, hanno richiesto un intervento coordinato su scala internazionale. Ma fughe di informazioni e pubblicazioni anticipate hanno complicato la gestione dell’emergenza.**

Due vulnerabilità nel cuore di PHP, una diffusione potenzialmente enorme e una procedura di divulgazione coordinata compromessa proprio nelle ore precedenti al rilascio delle patch. È questa la vicenda di PHP2Shell, il nome con cui i ricercatori hanno identificato due falle critiche che interessano uno dei linguaggi di programmazione più utilizzati per realizzare siti Web e applicazioni online.

Le vulnerabilità, codificate CVE-2026-109618 e CVE-2026-109619, hanno entrambe ricevuto un punteggio CVSS 4.0 di 9,2 e, in determinate condizioni, possono consentire a un attaccante remoto, privo di credenziali, di eseguire codice sui server che utilizzano versioni vulnerabili di PHP.

Il 21 ottobre 2026 il progetto PHP ha pubblicato aggiornamenti straordinari per le versioni ancora supportate. La gravità della situazione ha portato anche a una presa di posizione congiunta della Commissione Europea, di ENISA, CERT-EU, Europol e della rete europea dei CSIRT, che hanno invitato le organizzazioni a intervenire immediatamente, dando priorità ai sistemi esposti su Internet.

## ![](https://www.securityinfo.it/wp-content/uploads/2026/10/Sviluppatore-frustrato-davanti-a-PHP2Shell-1024x576.png)

## Una vulnerabilità conosciuta dal 2024, ma sottovalutata

L’aspetto forse più interessante della vicenda riguarda la storia della prima vulnerabilità. Il problema alla base di CVE-2026-109618 era già emerso nel 2024, durante una verifica esterna della sicurezza del motore PHP.

All’epoca, tuttavia, il team di sviluppo non era riuscito a individuare una soluzione soddisfacente. Il difetto riguardava una parte particolarmente delicata del funzionamento interno del linguaggio e le possibili correzioni presentavano conseguenze difficili da valutare: incompatibilità con il software esistente, nuovi rischi di denial of service e potenziali problemi per le numerose estensioni sviluppate da terze parti.

Mancava inoltre una dimostrazione convincente che il problema potesse essere sfruttato per ottenere l’esecuzione di codice da remoto.

Il risultato fu uno stallo. Gli sviluppatori conoscevano il difetto, ma non avevano una prova della sua effettiva pericolosità né una correzione che considerassero sufficientemente sicura per l’intero ecosistema.

La situazione è cambiata nell’estate del 2026, quando nuovi strumenti di analisi del codice basati sull’intelligenza artificiale hanno contribuito a individuare percorsi di sfruttamento molto più pericolosi.

Secondo la ricostruzione pubblicata dalla PHP Foundation, il lavoro si è intensificato attraverso audit condotti con strumenti di Anthropic e OpenAI, oltre alle attività di ricercatori indipendenti e società specializzate.

## L’11 agosto la scoperta che cambia la valutazione del rischio

Il passaggio decisivo avviene l’11 agosto 2026. Ryan A, ricercatore della società di sicurezza Calif, segnala al progetto PHP una possibilità di esecuzione arbitraria di codice riconducibile alla stessa causa del problema di gestione della memoria identificato nel 2024.

Nella stessa giornata, OpenAI segnala indipendentemente la medesima causa di fondo. Seguono ulteriori risultati da parte di Wiz, il 24 agosto, e nuovi vettori di attacco individuati da OpenAI il 18 settembre.

Il coinvolgimento dell’intelligenza artificiale non significa che i sistemi automatici abbiano gestito autonomamente l’intera ricerca. Il contributo dei modelli è stato integrato con il lavoro degli specialisti, che hanno verificato le segnalazioni, riprodotto gli attacchi e collaborato alla preparazione delle correzioni.

È però significativo che una vulnerabilità rimasta irrisolta per quasi due anni sia diventata una priorità assoluta dopo che gli strumenti di ricerca assistita dall’AI hanno contribuito a dimostrarne le conseguenze.

Da quel momento, secondo la PHP Foundation, la correzione del problema è diventata l’attività principale del team di sicurezza, con sviluppatori impegnati anche durante i fine settimana e nelle ore notturne.

La vicenda dimostra quanto stia cambiando il rapporto tra individuazione delle vulnerabilità e capacità di correggerle: l’AI può accelerare la scoperta di problemi complessi, ma non elimina le difficoltà tecniche e organizzative necessarie a distribuire una patch affidabile.

## La disclosure doveva essere coordinata. Poi sono cominciate le fughe di notizie

Una volta confermata la gravità delle vulnerabilità, il progetto PHP ha organizzato una procedura di coordinated vulnerability disclosure, coinvolgendo ricercatori, distributori software, provider cloud e società di sicurezza.

L’obiettivo era rendere disponibili gli aggiornamenti contemporaneamente alla pubb...