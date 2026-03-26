---
title: Magento sotto attacco: PolyShell, sfruttamento di massa in pochi giorni
url: https://www.securityinfo.it/2026/03/25/magento-sotto-attacco-polyshell-sfruttamento-di-massa-in-pochi-giorni/?utm_source=rss&utm_medium=rss&utm_campaign=magento-sotto-attacco-polyshell-sfruttamento-di-massa-in-pochi-giorni
source: Securityinfo.it
date: 2026-03-25
fetch_date: 2026-03-26T04:31:56.996124
---

# Magento sotto attacco: PolyShell, sfruttamento di massa in pochi giorni

Aggiornamenti recenti Marzo 25th, 2026 2:50 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Magento sotto attacco: PolyShell, sfruttamento di massa in pochi giorni](https://www.securityinfo.it/2026/03/25/magento-sotto-attacco-polyshell-sfruttamento-di-massa-in-pochi-giorni/)
* [API sotto attacco: la sicurezza dell’AI passa dall’infrastruttura applicativa](https://www.securityinfo.it/2026/03/24/api-sotto-attacco-la-sicurezza-dellai-passa-dallinfrastruttura-applicativa/)
* [AWS Bedrock: otto vettori che trasformano l’AI in un punto d’ingresso](https://www.securityinfo.it/2026/03/23/aws-bedrock-otto-vettori-che-trasformano-lai-in-un-punto-dingresso/)
* [La cybersecurity OT in Italia tra maturità limitata e pressioni normative](https://www.securityinfo.it/2026/03/19/la-cybersecurity-ot-in-italia-tra-maturita-limitata-e-pressioni-normative/)
* [DarkSword: exploit chain iOS tra zero-day, spyware e cybercrimine](https://www.securityinfo.it/2026/03/18/darksword-exploit-chain-ios-tra-zero-day-spyware-e-cybercrime-finanziario/)

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

## Magento sotto attacco: PolyShell, sfruttamento di massa in pochi giorni

Mar 25, 2026  [Redazione](https://www.securityinfo.it/author/redazione/ "Articoli scritti da Redazione")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2026/03/25/magento-sotto-attacco-polyshell-sfruttamento-di-massa-in-pochi-giorni/#respond)

---

La vulnerabilità **“PolyShell” in Magento Open Source e Adobe Commerce** è passata dalla disclosure alla compromissione su larga scala in tempi estremamente rapidi: secondo Sansec, azienda specializzata in sicurezza informatica, **lo sfruttamento di massa è iniziato il 19 marzo 2026**, appena due giorni dopo la divulgazione pubblica, e oggi le tracce di attacco risultano presenti su **circa il 56,7% degli store ancora vulnerabili**.

![](https://www.securityinfo.it/wp-content/uploads/2026/03/MagentoSottoAttacco-1024x683.png)Questa velocità è coerente con un pattern ormai ricorrente nell’e-commerce: quando un bug consente una catena semplice e automatizzabile, gli attori malevoli trasformano la scansione in infezione in poche ore, soprattutto su piattaforme diffuse e con installazioni eterogenee come Magento. Sansec, inoltre, ha pubblicato una lista di indirizzi IP utilizzati per lo scanning mirato degli shop, segnale che **la fase di ricognizione e selezione delle vittime** è già industrializzata.

### **Il cuore del problema: upload “travestito” via REST API**

Dal punto di vista tecnico, PolyShell riguarda il modo in cui la **REST API di Magento gestisce l’upload di file** associati alle “custom options” di un articolo nel carrello. In pratica, quando una product option è di tipo file, la piattaforma può finire per accettare e processare contenuti caricati dall’utente, con il rischio che un attaccante invii un **file “poliglotta”**: un oggetto che appare come immagine o risorsa legittima, ma che contiene anche porzioni eseguibili o utili a innescare altre condizioni pericolose. Se la configurazione del web server e del contesto applicativo lo permette, questo meccanismo può aprire la strada a **remote code execution (RCE)**, oppure a **account takeover** tramite stored cross-site scripting (XSS), sfruttando contenuti persistenti che vengono poi renderizzati o interpretati in un contesto privilegiato. In altre parole, non è “solo” un bug di input validation, ma un punto d’ingresso che, combinato con scelte di configurazione e catene note, può trasformare un e-commerce in una piattaforma di esecuzione per l’attaccante.

### **Patch gap e gestione del rischio: cosa sappiamo sulle correzioni**

La finestra operativa degli attaccanti è stata favorita anche dal consueto problema del **“patch gap” tra fix e produzione**. Adobe ha indicato che una correzione è stata resa disponibile in **Magento/Adobe Commerce 2.4.9-beta1 il 10 marzo 2026**, ma il fix non risulta ancora arrivato ovunque, lasciando molte installazioni senza un aggiornamento “production-ready” immediato. Sul fronte ufficiale, il bollettino di sicurezza Adobe (APSB26-05) conferma l’esistenza di vulnerabilità che, se sfruttate con successo, possono portare anche a **esecuzione di codice**, escalation di privilegi e letture arbitrarie del file system, pur dichiarando di non essere a conoscenza di exploit in-the-wild per le vulnerabilità trattate dal bulletin. In questo scenario, la pratica difensiva più realistica non è aspettare “la patch perfetta”, ma **ridurre subito l’esposizione**: capire se l’istanza è raggiungibile e attaccabile via API, verificare l’eventuale presenza di anomalie in percorsi e file di upload, e potenziare telemetria e controlli attorno ai flussi di checkout.

### **WebRTC skimmer: esfiltrazione cifrata e anti-controlli “tradizionali”**

Nel quadro degli attacchi attribuiti o sospetti legati allo sfruttamento, Sansec segnala anche la consegna di un **nuovo payment-card skimmer** che usa WebRTC per stabilire un canale di comunicazione e trasporto dati più elusivo rispetto ai classici beacon HTTP. L’elemento tecnico qui è importante: **WebRTC può usare DataChannels su UDP con DTLS**, quindi l’esfiltrazione avviene in modo cifrato e fuori dal perimetro di molti controlli pensati per traffico web “standard”, con un impatto potenziale anche su siti che applicano politiche CSP restrittive. Sansec descrive un loader JavaScript leggero che si collega a un C2 hardcoded via WebRTC, evitando il signaling tipico grazie a uno scambio SDP “forgiato”; quindi, riceve un secondo stadio sul canale cifrato e lo esegue cercando di **bypassare la CSP** riutilizzando un nonce già valido oppure ricorrendo a fallback più aggressivi. Per ridurre il rischio di rilevamento immediato, l’esecuzione viene posticipata con meccanismi come **requestIdleCallback**, spostando l’attività malevola in un momento di minore attenzione e rumore applicativo.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [account takeover](https://www.securityinfo.it/tag/account-takeover/), [Adobe Commerce](https://www.securityinfo.it/tag/adobe-commerce/), [attacchi in-the-wild](https://www.securityinfo.it/tag/attacchi-in-the-wild/), [card skimming](https://www.securityinfo.it/tag/card-skimming/), [checkout security](https://www.securityinfo.it/tag/checkout-security/), [CSP bypass](https://www.securityinfo.it/tag/csp-bypass/), [DTLS](https://www.securityinfo.it/tag/dtls/), [file upload](https://www.securityinfo.it/tag/file-upload/), [indicatori di compromissione](https://www.securityinfo.it/tag/indicatori-di-compromissione/), [Magento](https://www.securityinfo.it/tag/magento/), [Magento Open Source](https:/...