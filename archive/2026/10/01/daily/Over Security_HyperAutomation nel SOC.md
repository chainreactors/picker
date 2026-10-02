---
title: HyperAutomation nel SOC
url: https://www.certego.net/blog/mdr-soc-hyperautomation/
source: Over Security
date: 2026-10-01
fetch_date: 2026-10-02T07:49:24.032658
---

# HyperAutomation nel SOC

* [Why Certego](/why-certego/)
* Services

  [Managed Detection & Response](/services/managed-detection-and-response/)[Cyber Threat Intelligence](/services/cyber-threat-intelligence/)[Rapid Incident Response](/services/rapid-incident-response/)
* Platform

  [SecOps Platform](/platform/security-operations-platform/)[Detection Modules](/platform/detection-modules/)[Response Modules](/platform/response-modules/)[Threat Intelligence Modules](/platform/threat-intelligence-modules/)
* Resources

  [Blog](/blog/)[Events & Webinars](/resources/events-and-webinars/)[Datasheets & Whitepapers](/resources/datasheets-and-whitepapers/)
* Company

  [About Us](/company/about-us/)[SecOps Team](/company/security-operations-team/)[News](/company/news/)[Partners](/company/partners/)[Careers](/company/careers/)[Contact Us](/company/contact-us/)
* + [ð®ð¹](/it/blog/mdr-soc-hyperautomation/)

[Are you under attack?](/have-you-been-breached/)

October 01, 2026

## HyperAutomation nel SOC

#### Rispondere alla velocitÃ  â¨degli attacchi AIâ¨e ridurre il carico operativo â¨per il cliente

![](data:image/svg+xml;charset=utf-8...)

![image](/static/78d453be31f46dd926d895029d7a703a/bd885/HyperAutomation%20Certego%20MDR.png)![image](/static/78d453be31f46dd926d895029d7a703a/bd885/HyperAutomation%20Certego%20MDR.png)

Nella gestione di un incidente, rilevare un attacco non Ã¨ tutto: **conta anche quanto velocemente lo si contiene**. Per questo il MTTR (Mean Time To Respond), il tempo medio tra rilevazione e risposta, Ã¨ un indicatore sempre piÃ¹ importante.

I motivi sono due. Il primo Ã¨ la velocitÃ  degli attaccanti, che usano l'intelligenza artificiale per accorciare proprio le fasi tra il primo accesso e il controllo della rete. La finestra utile per intervenire si riduce, e la partita si decide nei minuti che seguono l'alert.

Il secondo Ã¨ che la risposta dipende ancora da attivitÃ  manuali, e in alcuni casi Ã¨ necessaria l'attivitÃ  del cliente guidata dal provider MDR. Il lavoro manuale da ridurre, quindi, non Ã¨ solo quello degli analisti MDR, ma anche quello di chi lavora dentro le aziende.

Ã qui che entra in gioco l'**HyperAutomation**.

## Il breakout time si accorcia

Il **breakout time** Ã¨ il tempo tra l'accesso iniziale di un attaccante e l'inizio del suo movimento laterale nella rete della vittima. Ã la misura piÃ¹ concreta della finestra a disposizione di chi difende.

Secondo le piÃ¹ recenti analisi di threat intelligence, nel 2025 il breakout time medio degli attacchi di matrice criminale (eCrime) Ã¨ sceso a **29 minuti**. Rispetto al 2024 gli attaccanti sono stati il 65% piÃ¹ veloci, e il caso piÃ¹ rapido osservato Ã¨ durato **27 secondi**.

A comprimere questi tempi contribuisce l'intelligenza artificiale. Una [ricerca di Anthropic](https://www.anthropic.com/news/AI-enabled-cyber-threats-mitre-attack) ha mappato su MITRE ATT&CK 832 account bloccati per attivitÃ  malevole tra marzo 2025 e marzo 2026. Parte di questi risultati Ã¨ confluita nel [Data Breach Investigations Report (DBIR) 2026](https://www.verizon.com/business/resources/reports/dbir/) di Verizon.

Il quadro che emerge Ã¨ netto: l'uso dell'AI si sta spostando dall'accesso iniziale alle attivitÃ  svolte dentro la rete compromessa. Gli attaccanti piÃ¹ pericolosi la concentrano sulle fasi operative piÃ¹ impegnative: **discovery degli account, movimento laterale ed escalation dei privilegi**. Sono proprio le attivitÃ  che determinano il breakout time.

Non solo: gli attori piÃ¹ evoluti costruiscono architetture che permettono ai modelli di concatenare piÃ¹ fasi dell'attacco con un intervento umano minimo. Se l'attacco procede a velocitÃ  macchina, una risposta che dipende da passaggi manuali parte in svantaggio.

## Cos'Ã¨ l'HyperAutomation (e perchÃ© non Ã¨ la SOAR di ieri)

Con **HyperAutomation** si intende l'automazione end-to-end dei processi di sicurezza: dalla ricezione dell'alert all'arricchimento, fino al contenimento e alla notifica. Non si tratta di automatizzare singoli task, ma di orchestrare l'intera catena di azioni tra strumenti diversi.

L'idea non Ã¨ nuova. Le piattaforme SOAR (Security Orchestration, Automation and Response) hanno dimostrato per prime il valore dell'automazione nel SOC. Si basano perÃ² su playbook statici e script personalizzati, costruiti e mantenuti da ingegneri dedicati.

Quando un'API cambia, il playbook si rompe. Quando arriva uno scenario non previsto, l'alert torna in coda a un analista. L'HyperAutomation nasce per superare questi limiti:

| Aspetto | SOAR tradizionale | HyperAutomation |
| --- | --- | --- |
| Architettura | Monolitica, rallenta nei picchi di alert | Cloud-native ed event-driven, scala in modo elastico |
| Integrazioni | Sviluppate e mantenute a mano, fragili ai cambi di API | Centinaia di connettori nativi, mantenuti dalla piattaforma |
| Ruolo dell'AI | Assente o marginale | Agenti AI per triage, arricchimento e investigazione |
| Controllo umano | Spesso binario: tutto automatico o tutto manuale | Autonomia calibrata per tipo di azione e livello di rischio |

Un aspetto merita attenzione: nelle piattaforme piÃ¹ mature l'AI aiuta a **ragionare** sull'alert, mentre le azioni di risposta restano **deterministiche**. Il contenimento passa da workflow definiti e validati, che si comportano ogni volta allo stesso modo.

Per un provider MDR conta anche la scala. Chi protegge decine di ambienti diversi ha bisogno di un'architettura multi-tenant, capace di reggere i picchi di alert senza mettere in coda le azioni di contenimento.

## In un servizio MDR, la response fa la differenza

Detection e analisi sono il cuore di un servizio MDR, e oggi possono contare su telemetria ricca e strumenti maturi. La differenza, perÃ², si gioca subito dopo: quando l'alert Ã¨ confermato e la minaccia va contenuta.

A quel punto entrano in gioco i passaggi manuali: accedere a piÃ¹ console, autenticarsi su ognuna, individuare l'host o l'utente giusto, coordinarsi con il team IT del cliente. Di notte o nel weekend, quando le persone da coinvolgere non sono davanti a uno schermo, i tempi si allungano ancora. **Ogni secondo perso tra login multipli, cambi di console e coordinamento manuale Ã¨ tempo regalato all'attaccante.**

In molti modelli MDR, inoltre, il SOC segnala l'incidente e indica cosa fare, ma l'esecuzione resta parzialmente in carico anche al cliente. Ogni incidente si traduce cosÃ¬ in lavoro operativo per il suo team, spesso fuori orario.

Questo non significa togliere le persone dal processo. In un servizio MDR **la componente umana resta fondamentale**: sono gli analisti a leggere il contesto e a investigare. Sono loro a distinguere un falso positivo da un attacco reale e a guidare la risposta agli incidenti piÃ¹ complessi.

L'HyperAutomation si concentra invece su attivitÃ  specifiche: ripetitive, urgenti e ben definite. In questi casi la decisione si prende a monte, nel playbook, e al momento dell'incidente va solo eseguita, in fretta e senza errori. L'automazione agisce direttamente sugli strumenti giÃ  presenti nell'infrastruttura del cliente:

* **Endpoint**: isolamento dell'host compromesso tramite l'EDR.
* **Rete**: blocco degli indirizzi IP malevoli e del traffico sospetto, tramite sonde e dispositivi di rete.
* **IdentitÃ**: disattivazione dell'utente, revoca delle sessioni attive e reset della password, su Active Directory e sulle piattaforme cloud.
* **Comunicazione**: notifica al team giusto sul canale corretto e aggiornamento del ticket, con il riepilogo delle azioni svolte.

Il cliente non deve piÃ¹ eseguire in prima persona le attivitÃ  di contenimento. Viene informato in tempo reale, mentre il SOC prosegue l'investigazione con la minaccia giÃ  circoscritta.

## Un esempio pratico: lo stesso incidente, due risposte

Per capire cosa cambia davvero, mettiamo a confronto i due approcci sullo stesso scenario. Un alert segnala la compromissione di una postazione e il SOC conferma l'incidente. Per contenerlo servono tre azioni, in sequ...