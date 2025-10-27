---
title: Trovate vulnerabilità critiche nei sistemi di misurazione automatica del livello dei serbatoi
url: https://www.securityinfo.it/2024/10/02/trovate-vulnerabilita-critiche-nei-sistemi-di-misurazione-automatica-del-livello-dei-serbatoi/?utm_source=rss&utm_medium=rss&utm_campaign=trovate-vulnerabilita-critiche-nei-sistemi-di-misurazione-automatica-del-livello-dei-serbatoi
source: Securityinfo.it
date: 2024-10-03
fetch_date: 2025-10-06T18:53:07.106812
---

# Trovate vulnerabilità critiche nei sistemi di misurazione automatica del livello dei serbatoi

Aggiornamenti recenti Ottobre 6th, 2025 9:00 AM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)
* [Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)
* [Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/)

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

## Trovate vulnerabilità critiche nei sistemi di misurazione automatica del livello dei serbatoi

Ott 02, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2024/10/02/trovate-vulnerabilita-critiche-nei-sistemi-di-misurazione-automatica-del-livello-dei-serbatoi/#respond)

---

I ricercatori di Bitsight TRACE [hanno individuato](https://www.bitsight.com/blog/critical-vulnerabilities-discovered-automated-tank-gauge-systems) alcune **vulnerabilità 0-day critiche** in sei diversi **sistemi di misurazione automatica del livello dei serbatoi (ATG)** di cinque vendor.

I sistemi ATG sono in grado di monitorare e **registrare automaticamente il livello, il volume e la temperatura dei prodotti contenuti nei serbatoi di stoccaggio,** per esempio in quelli di benzina o altri carburanti delle stazioni di servizio. Questi sistemi si occupano anche di individuare eventuali perdite o altri problemi e notificare gli operatori con allarmi dedicati, oltre a intraprendere azioni di emergenza come la chiusura di valvole o di distributori.

![vulnerabilità serbatoi](https://www.securityinfo.it/wp-content/uploads/2024/10/filling-station-1839760_1920.jpg)

Gli attaccanti possono sfruttare questi bug per eseguire tutta una serie di azioni malevole, come per esempio **ottenere dati sensibili, disabilitare allarmi o interrompere l’erogazione dei servizi**; in particolari condizioni, un cybercriminale può riuscire a ottenere il controllo completo dei sistemi di monitoraggio.

I modelli di ATG più colpiti sono i Maglink LX e Maglink LX4 che contano 6 delle 11 vulnerabilità scoperte, seguiti dal Franklin TS-550, dall’OPW SiteSentinel, dal Proteus OEL8000 e dall’Alisonic Sibylla.

## Le vulnerabilità dei sistemi di misurazione dei serbatoi

In una sola settimana, i ricercatori di Bitsight TRACE hanno scoperto **11 vulnerabilità in 6 modelli di sistemi ATG**, di cui una un duplicato di un bug già esistente. Delle restanti 10, due hanno ottenuto un punteggio CVSS di 10 e altre cinque sono state segnalate come critiche.

Le due vulnerabilità più critiche consentono l’esecuzione di **comandi arbitrari sul sistema operativo**, mentre altre permettono a un attaccante di **superare i controlli di autenticazione**. Uno dei bug critici colpisce l’applicazione web di uno dei sistemi: uno degli account disponibili ha privilegi di amministrazione e **usa una password di default che non può essere modificata.**

**“*Tutte queste vulnerabilità permettono di ottenere pieni privilegi di amministratore sul dispositivo e, alcune di esse, accesso operativo completo al sistema*“** scrivono i ricercatori. Come altri sistemi ICS, gli ATG sono stati ideati decine di anni fa quando non si contemplavano misure di sicurezza robuste, tantomeno adeguate alle minacce moderne. Molti di questi sistemi, inoltre, non sono stati progettati per essere connessi ad ambienti pericolosi come Internet e, integrandoli alle nuove tecnologie per renderli più efficienti e avere accesso remoto, hanno ampliato significativamente la superficie di attacco.

![](https://www.securityinfo.it/wp-content/uploads/2024/10/gas-station-2665795_1920.jpg)

**Le conseguenze degli exploit che sfruttano questi bug variano da una “semplice” interruzione di servizio a danni fisici**: secondo i ricercatori di Bitsight, gli attaccanti possono modificare parametri critici che portano a perdite di carburante e a danneggiare altri componenti dell’infrastruttura, oltre che disabilitare gli allarmi. Esistono poi anche dei danni indiretti derivanti dal controllo di questi sistemi: gli attaccanti possono monitorare le vendite e ottenere insight finanziari sulle singole stazioni di servizio.

Non sono solo le stazioni di servizio a essere colpite da queste minaccia, ma anche aeroporti, sistemi governativi e compagnie del manifatturiero.

Nonostante non sia così semplice sfruttare queste vulnerabilità per alterare le funzionalità dei serbatoi, è indispensabile **migliorare la sicurezza dei sistemi ATG** per renderli più affidabili e resilienti a eventuali attacchi. I ricercatori di Bitsight, in particolare, chiedono un’evoluzione dell’industria verso una filosofia “secure by design”, anche se il cambiamento sarà lento e costoso.

Lo sforzo in questione deve coinvolgere più entità: non sono solo i produttori degli ATG a dover cambiare il proprio modus operandi, ma anche i clienti e i partner che devono impegnarsi a adottare misure di sicurezza per proteggere i sistemi, limitando gli accessi non autorizzati. Infine, la classe politica stessa deve comprendere a fondo i problemi di questi e tutti gli altri sistemi di controllo industriale per definire strategie e programmi che aiutino le imprese a sviluppare una cultura di cybersicurezza più robusta.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [automazione](https://www.securityinfo.it/tag/automazione/), [serbatoi](https://www.securityinfo.it/tag/serbatoi/), [sistemi ATG](https://www.securityinfo.it/tag/sistemi-atg/), [sistemi industriali](https://www.securityinfo.it/tag/sistemi-industriali/), [vulnerabilità critiche](https://www.securityinfo.it/tag/vulnerabilita-critiche/), [vulnerabilità zero-day](https://www.securityinfo.it/tag/vulnerabilita-zero-day/)

[Rischio umano: con Mimecast si minimizzano i rischi di attacchi a dipendenti e manager](https://www.securityinfo.it/2024/10/02/rischio-umano-con-mimecast-si-minimizzano-i-rischi-di-attacchi-a-dipendenti-e-manager/)
[CosmicBeet...