---
title: L'attacco ai supermercati francesi: una vulnerabilità annunciata?
url: https://www.certego.net/blog/attacco-ai-supermercati-francesi-una-vulnerabilita-annunciata/
source: Over Security
date: 2026-10-13
fetch_date: 2026-10-14T06:53:08.082236
---

# L'attacco ai supermercati francesi: una vulnerabilità annunciata?

* [Why Certego](/why-certego/)
* Services

  [Managed Detection & Response](/services/managed-detection-and-response/)[Cyber Threat Intelligence](/services/cyber-threat-intelligence/)[Rapid Incident Response](/services/rapid-incident-response/)
* Platform

  [SecOps Platform](/platform/security-operations-platform/)[Detection Modules](/platform/detection-modules/)[Response Modules](/platform/response-modules/)[Threat Intelligence Modules](/platform/threat-intelligence-modules/)
* Resources

  [Blog](/blog/)[Events & Webinars](/resources/events-and-webinars/)[Datasheets & Whitepapers](/resources/datasheets-and-whitepapers/)
* Company

  [About Us](/company/about-us/)[SecOps Team](/company/security-operations-team/)[News](/company/news/)[Partners](/company/partners/)[Careers](/company/careers/)[Contact Us](/company/contact-us/)
* + [ð®ð¹](/it/blog/attacco-ai-supermercati-francesi-una-vulnerabilita-annunciata/)

[Are you under attack?](/have-you-been-breached/)

October 13, 2026

## L'attacco ai supermercati francesi: una vulnerabilitÃ  annunciata?

#### Quando una patch mancata diventa un rischio dâimpresa

![](data:image/svg+xml;charset=utf-8...)

![image](/static/201525c20ad143399870650f238e3282/bd885/Attacco%20supermercati%20francesi%20BLOG.png)![image](/static/201525c20ad143399870650f238e3282/bd885/Attacco%20supermercati%20francesi%20BLOG.png)

Nella notte tra domenica 11 e lunedÃ¬ 12 ottobre, frigoriferi e congelatori di centinaia di supermercati francesi hanno smesso di fare il loro lavoro. Secondo una testimonianza raccolta da Le Monde, le prime anomalie risalirebbero alle 23 circa, mentre gli effetti sarebbero diventati evidenti verso le 4 del mattino ([InformatiqueNews](https://www.informatiquenews.fr/magasins-systeme-intermarche-leclerc-et-monoprix-touches-par-cyberattaque-250707)). In molti negozi, a quanto pare, il problema Ã¨ stato scoperto solo lunedÃ¬ mattina.

Il bilancio Ã¨ ancora provvisorio e le stime cambiano di ora in ora. Nelle prime ricostruzioni si parlava di centinaia di punti vendita IntermarchÃ© e CoopÃ©rative U, mentre BleepingComputer, citando la stampa francese, indicava tra 250 e 350 negozi ([BleepingComputer](https://www.bleepingcomputer.com/news/security/cyberattack-shuts-down-refrigerators-at-french-supermarkets/)).

Il numero uno del gruppo Les MousquetairesâIntermarchÃ©, Thierry Cotillard, ha raccontato che gli attaccanti sono riusciti ad avviare da remoto lo sbrinamento di tutti i banchi refrigerati, facendone salire la temperatura fino a 50 gradi. Le conseguenze riportate: catena del freddo interrotta, tonnellate di prodotti da buttare e danni stimati in decine di milioni di euro. La procura di Parigi ha aperto un'indagine e ha segnalato anche alcuni principi d'incendio.

Il denominatore comune, secondo le ricostruzioni, sarebbe il sistema del produttore danese Danfoss che molte catene usano per gestire a distanza la refrigerazione dei punti vendita. Al centro ci sarebbero i controller della famiglia AK-SM: âsystem managerâ che coordinano tutti i regolatori del freddo di un negozio e li rendono gestibili da un'interfaccia web ([Team82](https://claroty.com/team82/research/freeze-the-controller-defrost-the-food-uncovering-vulnerabilities-in-danfoss-refrigeration-controllers)). Chi controlla il system manager, in pratica, controlla il freddo dell'intero punto vendita.

## Una vulnerabilitÃ  annunciata

Secondo una fonte vicina al primo ministro francese citata dall'AFP, l'ANSSI avrebbe individuato una vulnerabilitÃ  nel software di un'azienda danese e avrebbe giÃ  contattato il fornitore ([CBS News](https://www.cbsnews.com/news/cyberattack-supermarkets-refrigerators-france-fires-food-losses/)). Dalle fonti disponibili emergono poi tre elementi.

* **Le falle erano note.** Come si sia arrivati ai controller non Ã¨ ancora chiaro ([BleepingComputer](https://www.bleepingcomputer.com/news/security/cyberattack-shuts-down-refrigerators-at-french-supermarkets/)), ma di vulnerabilitÃ  pubbliche su questi prodotti ce n'erano diverse. Nel 2023 i ricercatori di Synacktiv avevano pubblicato un metodo per aggirare l'autenticazione dei vecchi system manager SM800 e SC255/SC355: un âcodice del giornoâ, calcolato a partire dalla sola data, accettato al posto della password. Danfoss aveva risposto che quei modelli erano giÃ  fuori supporto e aveva raccomandato di limitarne l'accesso dalla rete. Un meccanismo simile Ã¨ stato poi individuato da Claroty Team82 nel modello successivo, l'AK-SM 800A: la CISA, l'agenzia statunitense per la cybersicurezza, lo ha segnalato a maggio 2025 (CVE-2025-41450, CVSS 8,2), con la correzione nel firmware R4.2 ([CISA](https://www.cisa.gov/news-events/ics-advisories/icsa-25-140-03)). Ad agosto 2025 Ã¨ arrivato l'avviso su una seconda falla, una command injection che, una volta ottenuto l'accesso, permette di eseguire comandi sul sistema (CVE-2025-41451) ([BleepingComputer](https://www.bleepingcomputer.com/news/security/cyberattack-shuts-down-refrigerators-at-french-supermarkets/)).
* **Molti dispositivi sono raggiungibili da Internet.** LunedÃ¬ Baptiste Robert, CEO di Predicta Lab, ha contato 2.752 sistemi Danfoss esposti online, 1.590 dei quali in Francia, mentre il motore di ricerca Shodan ne indicizzava oltre 4.500 ([BleepingComputer](https://www.bleepingcomputer.com/news/security/cyberattack-shuts-down-refrigerators-at-french-supermarkets/)). Nella sua ricerca, Claroty Team82 aveva giÃ  individuato 2.765 AK-SM 800A con l'interfaccia di gestione raggiungibile da Internet ([Team82](https://claroty.com/team82/research/freeze-the-controller-defrost-the-food-uncovering-vulnerabilities-in-danfoss-refrigeration-controllers)). Non tutti sono necessariamente vulnerabili, ma tutti sono trovabili.
* **Molti impianti erano fuori supporto.** Secondo Danfoss, la maggior parte delle unitÃ  colpite erano prodotti legacy che non ricevono piÃ¹ aggiornamenti di sicurezza, come l'AK-SM800 (fuori supporto dal 2021) e l'AK-SC355 (dal 2016), oppure modelli attuali con firmware non aggiornato ([Cooling Post](https://www.coolingpost.com/world-news/danfoss-moves-to-mitigate-cyberattack/), [CBS News](https://www.cbsnews.com/news/cyberattack-supermarkets-refrigerators-france-fires-food-losses/)).

Per quanto emerso finora, insomma, non sembra essere servito uno zero-day. E non sarebbe nemmeno la prima volta: secondo una nota tecnica di Danfoss citata da InformatiqueNews, nel 2022 attacchi simili avevano colpito 16 supermercati in Russia e 40 in Israele, con controller AK-SM 800 privi di firewall o VPN.

Molto resta da chiarire, a partire dal punto d'ingresso: le ipotesi vanno dalle interfacce esposte su Internet alle credenziali deboli o rubate, fino agli account di manutenzione compromessi.

Non si sa con certezza nemmeno chi ci sia dietro: al momento non risultano rivendicazioni nÃ© attribuzioni. Ma per capire la portata del caso conta poco. Chiunque sia stato, l'effetto ricade sull'economia reale: merce distrutta, negozi chiusi, fornitori e consumatori coinvolti, e danni che, secondo quanto riportato, le assicurazioni potrebbero non coprire.

## PerchÃ© riguarda anche le aziende italiane

Sostituite il banco frigo con un PLC, una pressa o un forno industriale, e lo scenario non cambia. Ã il mondo dell'OT (Operational Technology) e dell'IoT industriale: sistemi che non gestiscono dati, ma processi fisici. Il manifatturiero Ã¨ uno dei pilastri dell'economia italiana, con un tessuto fatto in gran parte di piccole e medie imprese. Negli ultimi anni molte hanno collegato alla rete macchinari, linee e sistemi di supervisione, anche grazie agli incentivi di Industria 4.0, che chiedevano proprio l'interconnessione dei beni ai sistemi aziendali.

Manutenzione da remoto, dati in tempo reale e meno fermi sono vantaggi concreti. Ma ogni impianto connesso Ã¨ anche un possibile punto d'ingresso. E rispetto ai sistemi IT, questi dispositivi hanno quattro caratteristiche che li rendono piÃ¹ difficili da proteggere:

* **Cic...