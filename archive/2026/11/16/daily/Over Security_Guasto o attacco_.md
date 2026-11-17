---
title: Guasto o attacco?
url: https://www.certego.net/blog/guasto-o-attacco-cosa-fare-nelle-ore-in-cui-non-lo-sai-ancora-cybersecurity/
source: Over Security
date: 2026-11-16
fetch_date: 2026-11-17T09:57:22.011716
---

# Guasto o attacco?

* [Why Certego](/why-certego/)
* Services

  [Managed Detection & Response](/services/managed-detection-and-response/)[Cyber Threat Intelligence](/services/cyber-threat-intelligence/)[Rapid Incident Response](/services/rapid-incident-response/)
* Platform

  [SecOps Platform](/platform/security-operations-platform/)[Detection Modules](/platform/detection-modules/)[Response Modules](/platform/response-modules/)[Threat Intelligence Modules](/platform/threat-intelligence-modules/)
* Resources

  [Blog](/blog/)[Events & Webinars](/resources/events-and-webinars/)[Datasheets & Whitepapers](/resources/datasheets-and-whitepapers/)
* Company

  [About Us](/company/about-us/)[SecOps Team](/company/security-operations-team/)[News](/company/news/)[Partners](/company/partners/)[Careers](/company/careers/)[Contact Us](/company/contact-us/)
* + [ð®ð¹](/it/blog/guasto-o-attacco-cosa-fare-nelle-ore-in-cui-non-lo-sai-ancora-cybersecurity/)

[Are you under attack?](/have-you-been-breached/)

November 16, 2026

## Guasto o attacco?

#### Cosa fare nelle ore in cui non lo sai ancora

![](data:image/svg+xml;charset=utf-8...)

![image](/static/a20e19f0eab42c7c9416443a37ac3401/bd885/Guasto%20o%20attacco_%20certego%20blog.png)![image](/static/a20e19f0eab42c7c9416443a37ac3401/bd885/Guasto%20o%20attacco_%20certego%20blog.png)

GiovedÃ¬ 12 novembre Microsoft 365 si Ã¨ fermato in tutto il mondo: per quasi due giorni posta, calendari e servizi collegati hanno smesso di funzionare, in tutto o in parte. VenerdÃ¬ 13 la FAA (Federal Aviation Administration, l'ente federale per l'aviazione civile) ha bloccato tutti i decolli negli Stati Uniti per piÃ¹ di quattro ore. E lo stesso venerdÃ¬ sono comparse email di phishing che sfruttavano il disservizio Microsoft, con tanto di numero d'incidente vero.

Tre episodi in due giorni, e ogni volta la stessa domanda: Ã¨ un attacco?

Per lo stop dei voli, nessuno ha saputo rispondere per ore. Per Microsoft la risposta era scontata: un guasto globale, dichiarato dal fornitore stesso. Ed Ã¨ proprio dentro quella certezza che si Ã¨ infilato l'attacco.

## La finestra in cui nessuno sa

Tra il primo sintomo e una causa affidabile passa sempre del tempo. Chiamiamola finestra di ambiguitÃ . Non Ã¨ un'eccezione, e capita anche a chi di infrastrutture vive.

Con la FAA Ã¨ andata cosÃ¬. Il 13 novembre i decolli sono stati fermati alle 15:54 ora di New York, per Â«circostanze straordinarie e ragioni di sicurezzaÂ». La spiegazione Ã¨ arrivata piÃ¹ di quattro ore e mezza dopo, in conferenza stampa: apparati di telecomunicazione obsoleti, andati in sovraccarico. Accanto al segretario ai Trasporti c'era il capo della Sicurezza Interna, che ha detto di non avere prove di un attacco nÃ© di legami con il disservizio Microsoft. PiÃ¹ tardi ha aggiunto che l'ipotesi restava sul tavolo.

Il 18 novembre 2025, alle 11:20 UTC, la rete di Cloudflare ha cominciato a non consegnare piÃ¹ il traffico. Nel post-mortem l'azienda ammette di aver pensato, all'inizio, a un DDoS di dimensioni enormi. A spingere in quella direzione c'era anche una coincidenza: la status page, ospitata fuori dall'infrastruttura Cloudflare, era andata giÃ¹ nello stesso momento. La causa vera era un file usato dal sistema di Bot Management, raddoppiato di dimensione dopo una modifica ai permessi di un database.

Il 28 aprile 2025 la penisola iberica Ã¨ rimasta senza corrente. Tra le ipotesi circolate c'Ã¨ stata anche quella di un attacco informatico, poi esclusa dalle autoritÃ . Il rapporto del governo spagnolo, presentato il 17 giugno, ha parlato di un Â«fenomeno di sovratensioniÂ» dall'origine multifattoriale.

Succede anche al contrario. A ottobre, nei supermercati francesi, l'attacco si Ã¨ presentato con i sintomi di un guasto: banchi frigo che si scaldano, di notte. Le prime anomalie verso le 23; molti punti vendita se ne sono accorti solo all'apertura del lunedÃ¬. Un guasto, finchÃ© non succede in centinaia di negozi nello stesso momento.

Non Ã¨ incompetenza. Nelle prime ore guasto e attacco producono gli stessi sintomi: servizi che non rispondono, autenticazioni che falliscono, traffico anomalo, posta che non arriva. E piÃ¹ un'azienda dipende da servizi di terzi, piÃ¹ quei sintomi nascono in sistemi che non controlla e non vede.

## Era un guasto. Ma non solo

Il caso Microsoft dice qualcosa di diverso, perchÃ© lÃ¬ di ambiguitÃ  ce n'era poca. Il disservizio Ã¨ partito il 12 novembre alle 17:17 ora italiana e in poco piÃ¹ di due ore si Ã¨ esteso a tutte le regioni e ai servizi che dipendono dalla posta. Microsoft lo ha tracciato come incidente EX1550543 e ha dichiarato di non avere evidenze di attivitÃ  malevola. Sulla causa precisa ci Ã¨ voluta una notte di aggiornamenti; sulla natura del problema c'erano pochi dubbi. La conclusione piÃ¹ naturale, in azienda, era anche la piÃ¹ ragionevole: Ã¨ un problema di Microsoft, si aspetta.

Ma una risposta ovvia ha due effetti collaterali: abbassa la guardia e diventa la spiegazione di tutto.

Il primo effetto l'ha sfruttato una campagna di phishing che Microsoft Threat Intelligence ha intercettato giÃ  il 13 novembre ([Cybersecurity News](https://cybersecuritynews.com/active-password-stealing-attack-microsoft-365/)). Oggetto Â«OutageÂ» seguito da un codice di sei caratteri, mittente con il nome dell'organizzazione bersaglio seguito da Â«Service HealthÂ». Nel testo, il numero d'incidente vero e un avviso: la posta trattenuta durante il disservizio sarebbe stata cancellata entro 24 ore, a meno di cliccare per recuperarla.

La campagna su EX1550543 non inventava quasi nulla. Il disservizio era vero, il numero dell'incidente pure, e la posta in ritardo era un sintomo che gli utenti stavano vivendo davvero. Di inventato, nella storia che raccontava, c'era solo la minaccia: Microsoft, nel frattempo, aveva esteso a 48 ore la finestra di timeout, perchÃ© i messaggi in ritardo arrivassero comunque.

Lo abbiamo scritto a settembre parlando di phishing italiano: un'esca non deve essere sofisticata, deve essere plausibile al momento giusto. E il giorno dopo un disservizio globale, l'email piÃ¹ plausibile di tutte Ã¨ un avviso sul disservizio. Per questo, in giornate cosÃ¬, la regola utile non Ã¨ Â«riconosci il falsoÂ» ma Â«non fidarti del canaleÂ». Microsoft stessa ricorda che un numero d'incidente reale non rende sicuri i link di un'email, e che lo stato dei servizi va verificato direttamente nell'admin center.

Il secondo effetto Ã¨ meno visibile. Quando tutti sanno che la posta non funziona, ogni anomalia ha giÃ  un colpevole: l'accesso che fallisce, la richiesta MFA inattesa, la casella che non si apre. Â«Ã il disservizio.Â» Per qualche ora un'attivitÃ  malevola puÃ² confondersi nel rumore, senza che nessuno la guardi due volte. Un guasto certo non chiude la domanda sulla sicurezza. La cambia: da Â«Ã¨ un attacco?Â» a Â«chi lo sta sfruttando?Â»

Non Ã¨ una novitÃ . Il 19 luglio 2024, verso l'una di notte ora di New York, un aggiornamento difettoso di CrowdStrike ha mandato in crash quasi 8,5 milioni di dispositivi Windows in tutto il mondo. Anche lÃ¬ la natura del problema Ã¨ stata chiara quasi subito: lo stesso giorno il CEO ha scritto pubblicamente che non si trattava di un incidente di sicurezza nÃ© di un attacco ([IBM](https://www.ibm.com/think/news/recent-crowdstrike-outage-what-you-should-know)). Eppure nei giorni successivi sono comparse email di phishing che si spacciavano per il supporto CrowdStrike, e decine di domini sosia con parole come Â«fixÂ» o Â«recoveryÂ». Il 20 luglio CrowdStrike Intelligence segnalava giÃ  un archivio ZIP presentato come hotfix, che conteneva HijackLoader.

[![Gallery 1](/static/c0b33eedae3259cb3a2f9878bb9a20ec/71c1d/PHP2Shell%20website%20certego.png)](https://www.certego.net/blog/php2shell-quando-due-vulnerabilita-mettono-a-rischio-le-fondamenta-del-web/)

## Agire bene prima di sapere

Che la risposta arrivi dopo ore o sembri ovvia da subito, per le prime ore serve un'altra domanda. Non Â«Ã¨ un attacco?Â», ma Â«cosa...