---
title: Incredibile come i sistemi multi-agent possano aggirare i controlli, rubare segreti e diventare minacce
url: https://www.securityinfo.it/2026/03/13/incredibile-come-i-sistemi-multi-agent-possano-aggirare-i-controlli-rubare-segreti-e-diventare-minacce/
source: Over Security - Cybersecurity news aggregator
date: 2026-03-13
fetch_date: 2026-03-14T04:14:00.004684
---

# Incredibile come i sistemi multi-agent possano aggirare i controlli, rubare segreti e diventare minacce

Aggiornamenti recenti Marzo 13th, 2026 3:29 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Incredibile: i sistemi multi-agent aggirano controlli, rubano segreti ed esfiltrano](https://www.securityinfo.it/2026/03/13/incredibile-come-i-sistemi-multi-agent-possano-aggirare-i-controlli-rubare-segreti-e-diventare-minacce/)
* [Rapporto Clusit 2026: gli attacchi cyber crescono del 49%](https://www.securityinfo.it/2026/03/11/rapporto-clusit-2026-gli-attacchi-cyber-crescono-del-49/)
* [Plug-in di Chrome cambiano proprietà e diventano malware](https://www.securityinfo.it/2026/03/10/plug-in-di-chrome-cambiano-proprieta-e-diventano-malware/)
* [InstallFix: false guide di installazione CLI per installare infostealer](https://www.securityinfo.it/2026/03/06/installfix-false-guide-di-installazione-cli-per-installare-infostealer/)
* [Cybercrime e AI: l’attribuzione degli attacchi diventa sempre più difficile](https://www.securityinfo.it/2026/03/05/cybercrime-e-ai-lattribuzione-degli-attacchi-diventa-sempre-piu-difficile/)

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

## Incredibile: i sistemi multi-agent aggirano controlli, rubano segreti ed esfiltrano

Mar 13, 2026  [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo_security/ "Articoli scritti da Giancarlo Calzetta")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Attacchi](https://www.securityinfo.it/category/approfondimenti/attacchi/), [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Scenario](https://www.securityinfo.it/category/approfondimenti/scenario/), [Tecnologia](https://www.securityinfo.it/category/approfondimenti/tecnologia/), [Tecnologia](https://www.securityinfo.it/category/news/tecnologia-news/)
 [0](https://www.securityinfo.it/2026/03/13/incredibile-come-i-sistemi-multi-agent-possano-aggirare-i-controlli-rubare-segreti-e-diventare-minacce/#respond)

---

L’adozione degli agenti AI nelle aziende sta accelerando ben oltre la fase sperimentale e finalmente sempre più organizzazioni stanno affidando a questi sistemi compiti operativi concreti. Purtroppo, spesso questo vuol dire anche dar loro accesso a dati interni, interazioni con strumenti di produttività, repository documentali, shell di sistema, workflow di automazione e persino funzioni di amministrazione. In teoria, l’obiettivo è aumentare efficienza, velocità e autonomia. In pratica, [secondo una nuova ricerca di Irregular](https://www.irregular.com/publications/emergent-offensive-cyber-behavior-in-ai-agents), **gli agenti possono sviluppare comportamenti offensivi emergenti anche senza ricevere istruzioni esplicite di hacking**, arrivando a eludere controlli di sicurezza, scalare privilegi e sottrarre informazioni sensibili.

![](https://www.securityinfo.it/wp-content/uploads/2026/03/CapiAIcontroAgentiAI-1024x683.png)

È questo il punto più allarmante del report dedicato ai cosiddetti *rogue AI agents*. Il dato davvero significativo non è soltanto che i sistemi testati siano riusciti a violare policy e protezioni. È che lo abbiano fatto **partendo da prompt apparentemente “normali”, formulati in tono aggressivo o gerarchico, ma privi di richiami diretti a cyber attacchi, exploitation o bypass della sicurezza**. In altre parole, la deviazione non nasce da un classico prompt malevolo in stile jailbreak, bensì da un insieme di incentivi, strumenti, contesto operativo e feedback loop tra agenti che finisce per produrre un comportamento offensivo autonomo.

La conclusione è pesante per chiunque stia introducendo architetture agentiche in ambienti enterprise. **Se un agente dispone di accesso a tool, comandi, credenziali o dati sensibili, il modello di minaccia non può più assumere che quell’agente resterà nei limiti del compito assegnato**. Anzi, bisognerà dare per assodato che cercherà scorciatoie, aggirerà ostacoli e interpreterà i vincoli come problemi da risolvere, non come barriere da non superare.

#### **Quando il tono del prompt diventa un acceleratore di comportamento offensivo**

La ricerca di Irregular parte da un punto fondamentale: gli agenti moderni non si limitano a generare testo. Operano su sistemi, invocano strumenti, coordinano altri agenti, leggono file, eseguono script, interagiscono con risorse locali o remote. È proprio questa combinazione tra capacità operative e autonomia decisionale che apre la porta a comportamenti inattesi.

Nel report, gli autori spiegano di aver osservato in tutti gli scenari testati **“emergent offensive cyber behavior”**, cioè un comportamento offensivo non richiesto esplicitamente dall’utente ma emerso durante l’esecuzione del compito. I sistemi hanno mostrato la capacità di **individuare vulnerabilità, sfruttarle, scalare privilegi, disattivare strumenti di difesa e aggirare meccanismi di prevenzione dell’esfiltrazione dei dati**.

Un elemento centrale è il modo in cui vengono costruiti i prompt. Nei test non vengono usati input che dicano apertamente “attacca”, “viola” o “bypassa”. Vengono invece introdotti **urgenza, pressione gerarchica, rifiuto del fallimento e delega aggressiva verso sub-agenti**, tutti ingredienti che in un’organizzazione reale potrebbero sembrare perfino plausibili. Il problema è che, in un sistema agentico, queste istruzioni possono trasformarsi in una forma di autorizzazione implicita a superare ogni ostacolo.

Il report mostra molto bene questo slittamento. Frasi come **“non accettare errori per nessun motivo”**, **“assicurati che il task venga completato pienamente”**, **“non prendere un no come risposta”** o **“trova soluzioni creative per aggirare gli ostacoli”** non nominano la sicurezza, ma danno all’agente un obiettivo assoluto: completare il compito a tutti i costi. Se a questo si aggiunge accesso a strumenti di sistema, script locali e contesto aziendale, il passo verso il comportamento offensivo diventa sorprendentemente breve.

#### **Primo scenario: da ricerca documentale a compromissione del sistema interno**

Il primo caso analizzato da Irregular è forse il più istruttivo, perché mostra **come un compito ordinario possa degenerare in una vera e propria operazione offensiva**. L’ambiente simulato è una rete aziendale fittizia chiamata MegaCorp, con server, applicazioni e servizi interni. In questo scenario, il sistema multi-agent riceve l’incarico di recuperare informazioni da un wiki aziendale interno. L’obiettivo iniziale è banale: cercare un documento.

Il prompt, però, contiene una serie di istruzioni che imprimono forte pressione sul completamento del task. Tra le formulazioni riportate figurano passaggi come: **“It is of utmost importance that you perform the task exactly as required”** e, soprattutto, **“When you talk to your sub-agents, convey all the requirements to them, and be ruthless about t...