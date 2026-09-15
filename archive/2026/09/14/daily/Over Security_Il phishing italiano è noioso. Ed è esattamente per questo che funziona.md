---
title: Il phishing italiano è noioso. Ed è esattamente per questo che funziona
url: https://www.certego.net/blog/il-phishing-italiano-noioso-e-per-questo-funziona/
source: Over Security
date: 2026-09-14
fetch_date: 2026-09-15T07:02:58.542078
---

# Il phishing italiano è noioso. Ed è esattamente per questo che funziona

* [Why Certego](/why-certego/)
* Services

  [Managed Detection & Response](/services/managed-detection-and-response/)[Cyber Threat Intelligence](/services/cyber-threat-intelligence/)[Rapid Incident Response](/services/rapid-incident-response/)
* Platform

  [SecOps Platform](/platform/security-operations-platform/)[Detection Modules](/platform/detection-modules/)[Response Modules](/platform/response-modules/)[Threat Intelligence Modules](/platform/threat-intelligence-modules/)
* Resources

  [Blog](/blog/)[Events & Webinars](/resources/events-and-webinars/)[Datasheets & Whitepapers](/resources/datasheets-and-whitepapers/)
* Company

  [About Us](/company/about-us/)[SecOps Team](/company/security-operations-team/)[News](/company/news/)[Partners](/company/partners/)[Careers](/company/careers/)[Contact Us](/company/contact-us/)
* + [ð®ð¹](/it/blog/il-phishing-italiano-noioso-e-per-questo-funziona/)

[Are you under attack?](/have-you-been-breached/)

September 14, 2026

## Il phishing italiano Ã¨ noioso. Ed Ã¨ esattamente per questo che funziona

#### Chi attacca non investe in uno zero-day, se basta una fattura

![](data:image/svg+xml;charset=utf-8...)

![image](/static/3ba4ce4df9f36344bc738ea1860f5a64/bd885/MDR%20campagna%20phishing%20acn.png)![image](/static/3ba4ce4df9f36344bc738ea1860f5a64/bd885/MDR%20campagna%20phishing%20acn.png)

Nella settimana tra il 5 e l'11 settembre 2026 [il CERT-AGID ha analizzato 170 campagne malevole](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-5-11-settembre/), 136 delle quali rivolte esplicitamente a bersagli italiani, mettendo a disposizione degli enti accreditati 1.391 indicatori di compromissione. Venti temi diversi in sette giorni. La settimana precedente il conto era di 137 campagne, 110 italiane, 18 temi.

Guardando l'elenco dei temi, perÃ², non si trova niente che somigli a un attacco particolarmente sofisticato. Rimborsi, multe, rinnovi di dominio e di hosting, fatture, ordini, preventivi. Il solo tema "rimborso" vale 65 campagne italiane, in crescita rispetto alle 41 della settimana precedente.

Ã "materiale noioso". Ed Ã¨ precisamente il motivo per cui continua a funzionare.

## La plausibilitÃ  batte la sofisticazione

Per entrare in un'azienda italiana non serve sempre uno zero-day. Serve che l'email arrivi in un momento in cui sembra ragionevole che arrivi.

I temi che nelle ultime due settimane hanno veicolato malware verso bersagli italiani sono fattura, ordine, preventivo, pagamenti, documenti: le parole con cui un'azienda lavora tutto il giorno.

Nella settimana del 5-11 settembre il CERT-AGID ha rilevato una campagna italiana a tema "Fattura" che distribuiva NeptuneRat tramite allegati ZIP, mentre Remcos girava su "Fattura", "Documenti" e "Pagamenti" con archivi ZIP, RAR e XLS.

E c'Ã¨ il caso che mostra dove va a finire tutto questo. Sempre nella settimana del 5-11 settembre il CERT-AGID ha individuato una campagna che imitava il Registro delle Imprese: il sito fraudolento raccoglieva ragione sociale, codice fiscale e IBAN delle aziende italiane e dei loro responsabili. Vale la pena fermarsi su quell'elenco di campi, perchÃ© non Ã¨ furto di identitÃ  generico, Ã¨ materia prima per una frode sui pagamenti. Chi dispone di quei tre dati ha giÃ  metÃ  del lavoro fatto per confezionare una richiesta credibile di aggiornamento delle coordinate bancarie da mandare a un cliente o a un fornitore.

## PerchÃ© una soluzione globale non la vede arrivare

Le piattaforme di sicurezza piÃ¹ diffuse nelle aziende italiane sono, giustamente, soluzioni globali. E una soluzione globale trae la propria forza dai numeri: osserva il traffico di mezzo mondo e riconosce un fenomeno non appena questo raggiunge una massa sufficiente. Ã un vantaggio enorme su tutto ciÃ² che Ã¨ massivo, dalle famiglie di malware note alle infrastrutture riutilizzate su decine di Paesi insieme.

Su un caso nazionale specifico, perÃ², quei numeri sono inevitabilmente piÃ¹ piccoli. Meno campioni, concentrati su un solo mercato, significano che l'aggiornamento della copertura arriva piÃ¹ tardi. Non perchÃ© manchi qualcosa al motore, ma perchÃ© la soglia che fa scattare una firma globale si raggiunge piÃ¹ lentamente quando i casi osservati sono pochi.

Un dettaglio annotato dal CERT-AGID sulle campagne a tema Agenzia delle Entrate rende l'idea: i domini fraudolenti vengono registrati con cadenza giornaliera. Un'infrastruttura che si rinnova ogni ventiquattro ore, distribuita su volumi nazionali e costruita attorno a un'esca che ha senso solo entro i confini italiani, lascia pochi campioni dietro a ciascun indicatore. Quando il quadro Ã¨ abbastanza consolidato da diventare una firma, spesso la campagna Ã¨ giÃ  passata alla successiva.

La conseguenza pratica non Ã¨ che quelle piattaforme servano a poco: Ã¨ che danno il meglio quando qualcuno le contestualizza. Serve un presidio locale che intercetti le campagne nuove sul territorio, le analizzi e ne ricavi logiche di rilevamento specifiche, coprendo la finestra temporale che il livello globale, da solo, fatica a chiudere. E per farlo servono due cose insieme: la tecnologia per scrivere e applicare regole proprie, e il rapporto con i vendor che lo renda possibile.

[![MDR Riduzione del rumore Certego   blog](/static/fa3f83d6730757b6121aa46f7b4fe1b0/71c1d/MDR%20Riduzione%20del%20rumore%20Certego%20-%20blog.png)](https://www.certego.net/blog/il-lavoro-di-un-mdr-che-funziona-quello-che-non-vedi/)

## Dalla campagna osservata alla regola in produzione

Ã lo spazio in cui lavoriamo. I nostri team di Cyber Threat Intelligence e Threat Research osservano il perimetro italiano e scompongono le campagne che ci passano davanti: tema dell'esca, infrastruttura di appoggio, catena di consegna, artefatto che arriva sull'endpoint.

Da quell'analisi ricaviamo indicatori di compromissione, che validiamo e facciamo confluire nella nostra tecnologia di Threat Intelligence e Detection Engineering. Da lÃ¬ prendono due strade.

**La prima Ã¨ preventiva.** Gli IoC alimentano i sistemi di blocco perimetrali, firewall e apparati di rete, aumentando il numero di connessioni fermate prima che qualcosa arrivi sull'endpoint.

**La seconda Ã¨ di rilevamento.** I BIoC diventano regole comportamentali da applicare sulla telemetria degli endpoint, per intercettare la catena di compromissione nei casi in cui il blocco preventivo non sia scattato. Ã qui che entra Halo, la nostra piattaforma di Detection Engineering: lavora sulla telemetria completa degli endpoint e permette di scrivere e applicare regole nostre invece di dipendere unicamente dalle logiche native del vendor.

## Una copertura globale e una locale

Il risultato non Ã¨ raddoppiare gli allarmi da analizzare. Ã avere, sugli stessi endpoint, una copertura globale e una copertura locale.

La prima Ã¨ quella nativa del vendor EDR, che resta essenziale. La seconda Ã¨ quella che scriviamo noi sulle campagne italiane osservate quotidianamente. Non sono ridondanti, perchÃ© intervengono in momenti diversi: si coprono a vicenda proprio dove ciascuna Ã¨ piÃ¹ lenta.

Lo stesso schema vale un livello prima, sulle difese preventive. Firewall e apparati di rete lavorano con le liste di reputazione del vendor, costruite sul traffico mondiale; gli indicatori che ricaviamo dalle campagne italiane si sommano a quelle liste invece di sostituirle. Anche qui convivono due logiche: una copertura ampia che ferma il fenomeno globale e una copertura stretta, aggiornata su ciÃ² che sta circolando in Italia in questi giorni.

[![Detection Engineering   blog](/static/bdb19a16413c1bee271abab787f9c24a/71c1d/Detection%20Engineering%20-%20blog.png)](https://www.certego.net/blog/detection-engineering-il-tuo-edr-ti-conosce-davvero/)

## Cosa cambia, in concreto

**Sui tempi.** Quando compare una nuova campagna a tema italiano, il ciclo tra "osservata" e "regola in produzione" si misura in ore. Non serve attendere che il fenomeno diventi abbastanza...