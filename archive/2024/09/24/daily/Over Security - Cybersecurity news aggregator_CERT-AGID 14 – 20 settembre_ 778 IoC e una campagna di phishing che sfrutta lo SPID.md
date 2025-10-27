---
title: CERT-AGID 14 – 20 settembre: 778 IoC e una campagna di phishing che sfrutta lo SPID
url: https://www.securityinfo.it/2024/09/23/cert-agid-14-20-settembre-778-ioc-phishing-spid/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-24
fetch_date: 2025-10-06T18:30:09.547272
---

# CERT-AGID 14 – 20 settembre: 778 IoC e una campagna di phishing che sfrutta lo SPID

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

## CERT-AGID 14 – 20 settembre: 778 IoC e una campagna di phishing che sfrutta lo SPID

Set 23, 2024  [Stefano Silvestri](https://www.securityinfo.it/author/stefano-silvestri/ "Articoli scritti da Stefano Silvestri")
 [Hacking](https://www.securityinfo.it/category/news/hacking-news/), [Malware](https://www.securityinfo.it/category/news/malware-news/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [Phishing](https://www.securityinfo.it/category/news/phishing/), [Tecnologia](https://www.securityinfo.it/category/news/tecnologia-news/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2024/09/23/cert-agid-14-20-settembre-778-ioc-phishing-spid/#respond)

---

Nell’ultima settimana, il **CERT-AGID** ha condotto un’analisi approfondita delle minacce informatiche rilevanti per lo scenario italiano.

L’indagine ha portato all’identificazione di **56 campagne malevole**, di cui 41 specificamente mirate a obiettivi italiani e 15 di natura più generica ma con impatto sul territorio nazionale.

A seguito di questa attività, il CERT-AGID ha fornito ai suoi enti accreditati un totale di **778 indicatori di compromissione (IoC)**, strumenti essenziali per rilevare e contrastare queste minacce.

### I temi più rilevanti della settimana

Nell’ultima settimana, le campagne malevole sul territorio italiano hanno sfruttato **21 temi diversi**. Tra questi, il **Banking** è stato particolarmente colpito, con numerose campagne di phishing e smishing rivolte ai clienti di istituti come Intesa Sanpaolo, Monte dei Paschi di Siena, Banca Popolare di Sondrio e Poste Italiane. Inoltre, il malware Irata è stato diffuso tramite file APK ai danni dei clienti di N26.

Il tema degli **Ordini** è stato utilizzato per veicolare vari malware come FormBook, AgentTesla, Remcos e PXRECVOWEIWOEI attraverso email.

Le campagne legate ai **Documenti** hanno preso di mira DocuSign con attacchi di phishing e hanno diffuso i malware AgentTesla e AsyncRAT.

![](https://www.securityinfo.it/wp-content/uploads/2024/09/CERT-AGID-temi-3.png)

Fonte : CERT-AGID

Il tema dei **Pagamenti** è stato sfruttato sia per campagne di phishing che per la diffusione dei malware Vidar (tramite PEC) e Adwind (via email). Gli altri temi identificati sono stati impiegati per diverse campagne di malware e phishing.

Tra gli eventi di particolare interesse, è stata individuata una **nuova campagna che diffonde il malware Vidar attraverso PEC** compromesse, simulando richieste di pagamento per false fatture insolute e sfruttando un vecchio dominio del portale Excite.

È stata inoltre rilevata una **campagna di phishing bancario che sfrutta il tema SPID** per raccogliere le credenziali di accesso degli utenti di vari istituti bancari italiani, invitandoli a inserire i propri dati su una pagina web fraudolenta con il pretesto di rinnovare l’identità digitale.

Infine, è emersa una **nuova campagna mirata agli utenti di GitHub** per diffondere il malware Lumma Stealer, avvertendo i destinatari di una presunta vulnerabilità di sicurezza nei loro repository e inducendoli a compiere azioni che consentono l’esecuzione del codice malevolo.

### Malware della settimana

Nel corso della settimana sono state identificate **11 famiglie di malware** che hanno preso di mira l’Italia.

Tra le campagne più significative, **AgentTesla** si è distinto con cinque attacchi italiani incentrati sui temi “Documenti” e “Ordine” e veicolati tramite email con allegati BAT, EXE, ISO e RAR. Si registrano anche due campagne generiche, tutti diffusi tramite email con vari allegati EXE e ZIP.

**FormBook** ha lanciato due campagne italiane e una generica sul tema “Ordine”, mentre **Lumma Stealer** ha sfruttato i temi “Avvisi sicurezza” ed “Energia” in due campagne italiane che hanno sfruttato link malevoli ed email con allegati EXE e PDF.

**Vidar** ha condotto una campagna italiana focalizzata sui “Pagamenti”, utilizzando PEC con allegati JS. **AsyncRAT** ha colpito con una campagna italiana sul tema “Energia” e una generica sui “Documenti”, sfruttando email con allegati JAR e EXE.

![](https://www.securityinfo.it/wp-content/uploads/2024/09/CERT-AGID-malware-3.png)

Fonte : CERT-AGID

**Irata** si è concentrato sul settore bancario, diffondendosi tramite SMS con APK malevoli. **Umbral** è stato rilevato in una campagna generica veicolata via email.

**Remcos** ha preso di mira il settore bancario italiano con email contenenti allegati HTML. **VIPKeylogger** ha lanciato una campagna generica sui “Pagamenti”, mentre **PXRECVOWEIWOEI** si è diffuso attraverso una campagna generica sul tema “Ordine”, tramite email contenti link a file VBS.

Infine, **Adwind** ha colpito l’Italia con una campagna incentrata sui “Pagamenti”, utilizzando email con allegati HTML e PDF contenenti link a file JAR malevoli.

Queste diverse campagne mostrano la varietà e la sofisticazione delle minacce informatiche attuali, sfruttando temi comuni e metodi di diffusione diversificati per colpire utenti e organizzazioni in Italia.

### Phishing della settimana

Nell’ambito delle attività di monitoraggio delle minacce informatiche, la settimana appena trascorsa ha visto emergere un significativo numero di campagne di phishing, che hanno coinvolto complessivamente **22 marchi diversi**.

Tra le varie campagne rilevate, due in particolare si sono distinte per la loro intensità e frequenza. La prima ha preso di mira i clienti di **Intesa Sanpaolo**, uno dei maggiori gruppi bancari italiani.

Questa concentrazione di attacchi verso un’istituzione finanziaria così rilevante suggerisce un tentativo coordinato di sfruttare la vasta base clienti della banca, probabilmente mirando a ottenere credenziali di accesso e informazioni finanziarie sensibili...