---
title: Il 94% del lavoro di un MDR (che funziona) è quello che non vedi
url: https://www.certego.net/blog/il-lavoro-di-un-mdr-che-funziona-quello-che-non-vedi/
source: Over Security
date: 2026-08-28
fetch_date: 2026-08-29T08:32:53.416778
---

# Il 94% del lavoro di un MDR (che funziona) è quello che non vedi

* [Why Certego](/why-certego/)
* Services

  [Managed Detection & Response](/services/managed-detection-and-response/)[Cyber Threat Intelligence](/services/cyber-threat-intelligence/)[Rapid Incident Response](/services/rapid-incident-response/)
* Platform

  [SecOps Platform](/platform/security-operations-platform/)[Detection Modules](/platform/detection-modules/)[Response Modules](/platform/response-modules/)[Threat Intelligence Modules](/platform/threat-intelligence-modules/)
* Resources

  [Blog](/blog/)[Events & Webinars](/resources/events-and-webinars/)[Datasheets & Whitepapers](/resources/datasheets-and-whitepapers/)
* Company

  [About Us](/company/about-us/)[SecOps Team](/company/security-operations-team/)[News](/company/news/)[Partners](/company/partners/)[Careers](/company/careers/)[Contact Us](/company/contact-us/)
* + [ð®ð¹](/it/blog/il-lavoro-di-un-mdr-che-funziona-quello-che-non-vedi/)

[Are you under attack?](/have-you-been-breached/)

August 27, 2026

## Il 94% del lavoro di un MDR (che funziona) Ã¨ quello che non vedi

#### La catena che ferma il rumore, passo dopo passo

![](data:image/svg+xml;charset=utf-8...)

![image](/static/65a90ba34776a865cd4be83ae10d7678/bd885/MDR%20Riduzione%20del%20rumore%20Certego%20-%20blog.png)![image](/static/65a90ba34776a865cd4be83ae10d7678/bd885/MDR%20Riduzione%20del%20rumore%20Certego%20-%20blog.png)

Un ambiente enterprise, dodici mesi di osservazione. Il percorso Ã¨ questo:

**14,6 miliardi** di dati processati. **270,4 mila** eventi sospetti analizzati. **14,2 mila** allarmi scattati. **796** incidenti gestiti.

![Gallery 1](/static/a469942c79590706465ebd0b29fcf3ed/71c1d/infografica%20funnel.png)

La riduzione piÃ¹ ampia, in valore assoluto, Ã¨ la prima: dai miliardi alle centinaia di migliaia. Ã il lavoro delle macchine, ed Ã¨ un lavoro che nessuna organizzazione potrebbe fare a mano.

Ma la riduzione che conta davvero Ã¨ l'ultima. Tra i 14.200 allarmi scattati e i 796 incidenti gestiti e condivisi con il cliente c'Ã¨ un **-94%**.

Ã esattamente la parte del servizio che il cliente non percepisce, finchÃ© non apre le dashboard e scopre quanti allarmi sono stati esaminati e chiusi al posto suo.

E siccome quel 94% Ã¨ fatto di tecnologia e di giudizio umano, dipende interamente da due cose: quante segnalazioni la tecnologia riesce a filtrare a monte, e quante informazioni ha in mano l'analista quando apre l'allarme. Un analista senza contesto non filtra: scala. Ã qui che la catena a monte smette di essere un dettaglio tecnico e diventa la variabile che decide tutto.

## 1. Dalla telemetria agli eventi sospetti: 14,6 miliardi â 270,4 mila

Il primo stadio decide **cosa vale la pena guardare**, ed Ã¨ interamente automatico. La telemetria â processi, connessioni, eventi su file e registro, attivitÃ  utente â viene raccolta integralmente e passata al motore di detection.

**Halo**, la piattaforma di Detection Engineering di Certego, Ã¨ ciÃ² che rende la telemetria grezza degli endpoint accessibile e analizzabile, invece che solo parzialmente visibile dentro la console EDR/XDR di un fornitore terzo. Ed Ã¨ la condizione perchÃ© su quei dati si possa scrivere qualcosa di proprio.

PerchÃ© a questo stadio i rilevamenti hanno due origini diverse, e la differenza tra le due Ã¨ la ragione per cui servono entrambe.

Gli **alert nativi della soluzione EDR** nascono da una telemetria globale: milioni di endpoint, in ogni settore e in ogni Paese, che alimentano una logica costruita su ciÃ² che l'attaccante fa ovunque. Riconoscono i malware commodity, i tool di attacco noti, le tecniche giÃ  osservate su scala planetaria. Ã una capacitÃ  che nessuno puÃ² ricostruirsi in proprio.

Ha perÃ² un vincolo strutturale: Ã¨ una logica che deve funzionare per decine di migliaia di organizzazioni diverse, quindi per costruzione Ã¨ **one-size-fits-all**, calibrata sulla media di tutte e su nessuna in particolare. Funziona bene dappertutto, non funziona benissimo da nessuna parte.

Le **regole di detection scritte da Certego** non ripetono quel lavoro. Coprono ciÃ² che quella logica non Ã¨ progettata per vedere. Lavorano sulla telemetria grezza degli stessi endpoint, ma partono da due conoscenze che un modello globale non possiede: la normalitÃ  operativa di quella specifica azienda â gli applicativi verticali, il gestionale anni Duemila, gli script che girano in produzione alle tre di notte per ragioni legittime â e il modo in cui le minacce colpiscono il tessuto produttivo italiano: campagne malspam a tema fattura veicolate via PEC, kit di phishing localizzati, infrastrutture che testano per prime le imprese del nostro mercato. Difficilmente un vendor globale scriverÃ  una regola per una campagna che riguarda qualche centinaio di aziende in un solo Paese. Non Ã¨ una sua mancanza: Ã¨ una questione di prioritÃ  di scala.

Le due origini non si sovrappongono: non si tratta di ricevere due volte l'allarme sullo stesso evento, nÃ© di aggiungere una seconda coda da smaltire. Ã copertura che arriva dove l'altra si ferma.

Un imbuto cosÃ¬ stretto solleva perÃ² una domanda legittima. Scartare il 99,998% degli eventi Ã¨ un risultato solo se ciÃ² che resta Ã¨ tutto ciÃ² che conta: un filtro tarato troppo stretto non Ã¨ efficiente, Ã¨ cieco. Le regole costruite sul contesto servono esattamente a questo â far sÃ¬ che la riduzione del volume non si paghi in falsi negativi.

C'Ã¨ poi una quota di minacce che non compare nemmeno in questo conteggio, perchÃ© viene fermata prima di toccare gli endpoint: gli IOC verificati entrano nei controlli giÃ  in campo â blocklist dei firewall, IPS/IDS, proxy, resolver DNS, SIEM â e in casi documentati hanno prodotto un incremento dei blocchi tra il **+10%** nel finance e il **+21%** nel manufacturing, fino a **20 milioni** di tentativi di connessione malevola fermati in una settimana. Eventi che non sono mai esistiti.

## 2. Dagli eventi agli allarmi: 270,4 mila â 14,2 mila

Un attacco non si presenta come un evento. Si presenta come decine di eventi distinti, su host diversi, in momenti diversi: un dominio contattato, un processo anomalo, una chiave di registro modificata, una connessione in uscita. Trattarli separatamente significa moltiplicare il lavoro per venti e perdere la storia che li tiene insieme.

Il secondo stadio serve a ricomporli. Ã il compito di **PanOptikonÂ®**, la piattaforma di Unified Security Operations: alert nativi dell'EDR e rilevamenti prodotti dalle regole Certego entrano nella stessa pipeline, dove vengono deduplicati, correlati e aggregati in allarmi.

Qui il filtro cambia natura: non scarta, aggrega. Ed Ã¨ la ragione per cui i 14.200 allarmi che arrivano allo stadio successivo sono unitÃ  di lavoro sensate â ciascuna con la sua catena di eventi giÃ  ricostruita â invece di 270.400 frammenti da riassemblare a mano.

[![CFO Certego   blog](/static/99e4715e89468106c231737d194f9667/71c1d/CFO%20Certego%20-%20blog.png)](https://www.certego.net/blog/cybersecurity-per-cfo-dal-budget-al-rischio-di-impresa/)

## 3. Dagli allarmi agli incidenti: 14,2 mila â 796

Ã lo stadio del **-94%**, ed Ã¨ quello in cui la decisione la prende una persona.

Ogni allarme viene aperto, esaminato e classificato da un analista del team SecOps prima che possa diventare qualcosa su cui il cliente Ã¨ chiamato a collaborare. Novantaquattro volte su cento la conclusione Ã¨: il comportamento appartiene a un processo legittimo di quell'azienda, l'indicatore Ã¨ giÃ  noto e non contestualizzabile come minaccia attiva, l'anomalia ha una spiegazione operativa.

Detto cosÃ¬ sembra un lavoro di scarto. Ã l'opposto: **Ã¨ il punto in cui si decide, allarme per allarme, cosa merita l'attenzione di un'organizzazione**. E la qualitÃ  di quella decisione dipende da tre cose, tutte costruite prima.

â **L'arricchimento automatico.** I controlli reputazionali di routine sugli osservabili non sono lavoro da analista. **IntelOwl** â nato nella divisione R&D di Certego e oggi progetto ...