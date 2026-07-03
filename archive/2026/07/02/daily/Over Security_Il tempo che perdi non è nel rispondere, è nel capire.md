---
title: Il tempo che perdi non è nel rispondere, è nel capire
url: https://www.certego.net/blog/mttr-threat-intelligence-tempo-risposta/
source: Over Security
date: 2026-07-02
fetch_date: 2026-07-03T05:48:34.668383
---

# Il tempo che perdi non è nel rispondere, è nel capire

* [Why Certego](/why-certego/)
* Services

  [Managed Detection & Response](/services/managed-detection-and-response/)[Cyber Threat Intelligence](/services/cyber-threat-intelligence/)[Rapid Incident Response](/services/rapid-incident-response/)
* Platform

  [SecOps Platform](/platform/security-operations-platform/)[Detection Modules](/platform/detection-modules/)[Response Modules](/platform/response-modules/)[Threat Intelligence Modules](/platform/threat-intelligence-modules/)
* Resources

  [Blog](/blog/)[Events & Webinars](/resources/events-and-webinars/)[Datasheets & Whitepapers](/resources/datasheets-and-whitepapers/)
* Company

  [About Us](/company/about-us/)[SecOps Team](/company/security-operations-team/)[News](/company/news/)[Partners](/company/partners/)[Careers](/company/careers/)[Contact Us](/company/contact-us/)
* + [ð®ð¹](/it/blog/mttr-threat-intelligence-tempo-risposta/)

[Are you under attack?](/have-you-been-breached/)

July 02, 2026

## Il tempo che perdi non Ã¨ nel rispondere, Ã¨ nel capire

#### Come la Threat Intelligence accorcia la distanza tra l'alert e la decisione

![](data:image/svg+xml;charset=utf-8...)

![image](/static/7ac1345e1309cd27191f0c5b32d9f064/bd885/MTTR%20Threat%20Intelligence%20Certego%20-%20blog.png)![image](/static/7ac1345e1309cd27191f0c5b32d9f064/bd885/MTTR%20Threat%20Intelligence%20Certego%20-%20blog.png)

In un attacco informatico l'avversario non compete solo con le tue difese. Compete con il tuo orologio.

Ogni minuto che passa tra il primo segnale e la risposta Ã¨ un minuto in cui la compromissione si estende: un host in piÃ¹ raggiunto, una credenziale in piÃ¹ sottratta, un backup in piÃ¹ individuato. Per questo l'**MTTR â Mean Time to Respond**, il tempo medio di risposta â Ã¨ la misura concreta di quanto a lungo la tua organizzazione resta esposta mentre un attacco Ã¨ in corso.

E qui arriva la parte controintuitiva. Quando si prova ad abbassare l'MTTR, l'istinto Ã¨ aggiungere: piÃ¹ sensori, piÃ¹ regole, piÃ¹ alert. Ma la maggior parte del tempo di risposta non se ne va nel rispondere. Se ne va nel capire. E capire piÃ¹ in fretta non Ã¨ una questione di volume di dati: Ã¨ una questione di contesto.

# Cosa misura l'MTTR - Mean Time to Respond

L'MTTR Ã¨ una metrica composta. Assorbe la latenza di ogni fase della catena di risposta: rilevamento, triage dell'alert, investigazione, contenimento, eradicazione, ripristino. Un MTTR alto raramente significa "team lento". Quasi sempre indica un attrito strutturale da qualche parte in quella catena.

Il punto critico Ã¨ quasi sempre lo stesso: il triage e l'investigazione. Ã lÃ¬ che un analista, davanti a un alert, deve rispondere a domande tutt'altro che banali. Questo IP Ã¨ davvero malevolo o Ã¨ un falso positivo? Questo dominio a cosa Ã¨ collegato? Questo hash appartiene a una famiglia di malware nota? A che fase di un eventuale attacco corrisponde quello che sto vedendo?

Se la risposta a queste domande non Ã¨ giÃ  disponibile, l'analista la deve ricostruire. Un controllo reputazionale, una ricerca su un feed, un passaggio in sandbox, un confronto con un report. Ogni singolo passaggio dura pochi minuti â ma moltiplicato per centinaia di alert al giorno diventa il principale moltiplicatore dell'MTTR. E un team sommerso da questo lavoro manuale Ã¨ anche un team che fatica a distinguere il segnale vero dal rumore.

# Prevenire e capire: i due lavori della Threat Intelligence

Prima di entrare nel merito, una precisazione tecnica che spesso si perde: la Threat Intelligence non lavora su un solo tempo. Ne presidia due, distinti e complementari.

**La prima funzione Ã¨ preventiva**. Indicatori di compromissione nuovi e verificati â IP, domini, hash â vengono integrati in tempo reale nei controlli di sicurezza giÃ  in campo: blocklist dei firewall, IPS/IDS, proxy, risolutori DNS, SIEM. L'effetto Ã¨ bloccare la minaccia prima che causi danno. Qui la distanza tra alert e decisione non si accorcia: scompare. Ã il caso, per esempio, dell'aggiornamento automatico delle blocklist dei firewall: in casi reali documentati, l'integrazione degli IOC di Certego ha prodotto un incremento dei blocchi tra il **+10%** (settore finance) e il **+21%** (settore manufacturing), arrivando a fermare da **12 a 20 milioni di tentativi di connessione malevola in una sola settimana**. Sono attacchi che non sono mai diventati incidenti.

![Gallery 1](/static/adf3ed715f0c602c583684c290a7f28d/71c1d/ioc%20certego%20finance.png)

![Gallery 1](/static/53d4f468d91944cfcd817dd2a5f68a21/71c1d/ioc%20certego%20manufacturing.png)

**La seconda funzione Ã¨ analitica**. Nessuna prevenzione intercetta tutto: quando una minaccia supera la prima linea di difesa ed Ã¨ giÃ  in corso â o va ricostruita a posteriori â la Threat Intelligence fornisce il contesto per capirne natura, origine e portata, e rispondere di conseguenza. Ã qui che si gioca la distanza tra l'alert e la decisione.

Due funzioni, un solo obiettivo: ridurre quella distanza. Prevenendo, la si elimina. Analizzando, la si accorcia. Il resto di questo articolo si concentra sulla seconda â ma la prima resta il primo guadagno di tempo che un'intelligence di qualitÃ  ti mette in tasca.

# Il vero collo di bottiglia: il contesto mancante

Un alert senza contesto costringe a ripartire da zero. Un alert con contesto si chiude in pochi minuti.

Ã esattamente qui che vive la **Threat Intelligence**. Non come un elenco statico di indicatori da scaricare, ma come lo strato che porta il contesto dentro l'alert, nel momento esatto in cui serve. Quando un indicatore di compromissione (IOC) arriva giÃ  accompagnato da un verdetto affidabile, dalla famiglia di malware associata, dall'attore che lo utilizza e dalla fase della kill chain a cui appartiene, l'analista non deve piÃ¹ indagare: deve solo decidere.

Ed Ã¨ proprio questo spostamento â dall'indagare al decidere â il modo piÃ¹ efficace per comprimere l'MTTR su tutta la linea.

[![Gallery 1](/static/6435807a8cbc14655ff201e21e910106/71c1d/IOC%20certego%20MDR.png)](https://www.certego.net/blog/indicatori-di-compromissione-mdr/)

# Sul fronte dell'analisi, la Threat Intelligence accelera ogni fase di risposta

Quando la minaccia Ã¨ giÃ  dentro il perimetro, la Threat Intelligence non migliora una sola fase del ciclo di risposta: le tocca tutte.

* **Triage**. Quando un alert scatta contro un indicatore giÃ  caratterizzato, il verdetto e il contesto sono immediatamente disponibili. La decisione di escalation o chiusura non richiede ricerche aggiuntive.
* **Investigazione e Incident Response**. Conoscere giÃ  famiglia di malware, infrastruttura C2 collegata e fase della kill chain consente di stimare rapidamente la portata della compromissione e i possibili percorsi di movimento laterale, agendo su informazioni complete invece che ricostruirle sotto pressione.
* **Threat Hunting**. Gli indicatori piÃ¹ recenti diventano ipotesi di caccia immediate, mentre i dati storici possono essere ri-analizzati alla luce di IOC emersi solo in seguito, facendo emergere minacce sfuggite in passato.

Su ognuna di queste fasi, il risultato Ã¨ lo stesso: meno tempo speso a ricostruire, piÃ¹ tempo speso a decidere e contenere.

# Non basta un feed: serve una filiera

Qui sta il punto che fa la differenza. **La qualitÃ  della Threat Intelligence non dipende da quanti indicatori raccogli, ma da come li gestisci lungo l'intera filiera**.

I feed pubblici tendono a privilegiare la quantitÃ  a discapito della qualitÃ . Il risultato Ã¨ intelligence rumorosa: indicatori non verificati, datati, privi di contesto. Operativamente, Ã¨ la ricetta perfetta per aumentare i falsi positivi e quindi l'MTTR, non per ridurlo. Trasformare i dati grezzi in informazioni realmente azionabili richiede competenze e automazione lungo tutta la catena. Ã per questo che in Certego abbiamo costruito un **ecosistema proprietario di Threat Intelligence** il cui cuore sono due piattaforme: Quokka e IntelOwl.

**Quokka** Ã¨ il ce...