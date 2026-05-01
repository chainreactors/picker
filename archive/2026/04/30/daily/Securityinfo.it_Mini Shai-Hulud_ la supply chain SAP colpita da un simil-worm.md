---
title: Mini Shai-Hulud: la supply chain SAP colpita da un simil-worm
url: https://www.securityinfo.it/2026/04/30/mini-shai-hulud-la-supply-chain-sap-colpita-da-un-simil-worm/?utm_source=rss&utm_medium=rss&utm_campaign=mini-shai-hulud-la-supply-chain-sap-colpita-da-un-simil-worm
source: Securityinfo.it
date: 2026-04-30
fetch_date: 2026-05-01T05:39:48.644447
---

# Mini Shai-Hulud: la supply chain SAP colpita da un simil-worm

Aggiornamenti recenti Aprile 30th, 2026 5:30 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Mini Shai-Hulud: la supply chain SAP colpita da un simil-worm](https://www.securityinfo.it/2026/04/30/mini-shai-hulud-la-supply-chain-sap-colpita-da-un-simil-worm/)
* [Honeypot intelligenti: come gli agenti AI ingannano gli attaccanti AI](https://www.securityinfo.it/2026/04/29/honeypot-intelligenti-come-lai-viene-usata-per-ingannare-gli-attaccanti-automatizzati/)
* [I dati sono recuperabili (troppo) facilmente dalle auto moderne](https://www.securityinfo.it/2026/04/28/i-dati-sono-recuperabili-troppo-facilmente-dalle-auto-moderne/)
* [Reset password: una misura di sicurezza che diventa minaccia](https://www.securityinfo.it/2026/04/23/reset-password-una-misura-di-sicurezza-che-diventa-minaccia/)
* [Kyber annuncia il ransomware “post-quantum”, ma…](https://www.securityinfo.it/2026/04/22/kyber-annuncia-il-ransomware-post-quantum-ma/)

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

## Mini Shai-Hulud: la supply chain SAP colpita da un simil-worm

Apr 30, 2026  [Redazione](https://www.securityinfo.it/author/redazione/ "Articoli scritti da Redazione")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2026/04/30/mini-shai-hulud-la-supply-chain-sap-colpita-da-un-simil-worm/#respond)

---

La compromissione della supply chain software continua a evolvere, e l’operazione “Mini Shai-Hulud” rappresenta uno dei casi più interessanti e pericolosi osservati negli ultimi mesi. L’analisi [pubblicata da Wiz](https://www.wiz.io/blog/mini-shai-hulud-supply-chain-sap-npm) evidenzia come un numero limitato di pacchetti npm compromessi sia stato sufficiente per attivare **una catena di infezione capace di propagarsi tra ambienti di sviluppo, pipeline CI/CD e repository GitHub**, con un livello di automazione sempre più sofisticato. L’attacco è partito ieri, 29 aprile, ma ancora oggi sono stati identificati degli npm compromessi.

Ricordiamo che l’ecosistema SAP, e in particolare il Cloud Application Programming Model, rappresenta uno dei contesti più diffusi nelle aziende enterprise. Colpire questo layer significa **entrare direttamente nei processi di sviluppo che alimentano applicazioni critiche di business**.

![](https://www.securityinfo.it/wp-content/uploads/2026/04/SupplyChain-1024x576.png)

### **L’ingresso nella supply chain: pacchetti legittimi, codice malevolo**

L’attacco si basa su una tecnica ormai consolidata nel mondo npm: la pubblicazione di versioni “trojanizzate” di pacchetti legittimi. Nel caso specifico, alcuni moduli SAP sono stati modificati introducendo uno script di preinstallazione che viene eseguito automaticamente durante l’installazione delle dipendenze. Questo dettaglio è fondamentale. Il codice malevolo non viene eseguito dopo il deploy, ma **nel momento stesso in cui lo sviluppatore installa le dipendenze**; quindi, all’interno di ambienti fidati come workstation locali o pipeline automatizzate.

Lo script avvia un processo in più fasi. Inizialmente viene scaricato un runtime esterno, nel caso specifico Bun, utilizzato per eseguire un payload fortemente offuscato. Questo payload, di dimensioni superiori agli 11 MB, rappresenta il cuore dell’operazione: un framework completo per il furto di credenziali e la propagazione.

### **Il vero obiettivo: le credenziali degli sviluppatori**

A differenza di molte campagne tradizionali, l’obiettivo principale non è l’esecuzione diretta di codice malevolo sui sistemi finali, ma la raccolta sistematica di credenziali. Il malware è progettato per estrarre token e chiavi da molteplici fonti: GitHub, npm, ambienti cloud come AWS, Azure e GCP, fino a Kubernetes e vari browser. Del resto, le credenziali rappresentano oggi **la chiave di accesso più efficace per compromettere infrastrutture complesse**, perché consentono di muoversi lateralmente senza attivare controlli di sicurezza tradizionali.

I dati raccolti vengono cifrati e inviati verso repository GitHub controllati dagli attaccanti. Un elemento particolarmente interessante è che spesso questi repository vengono creati utilizzando le credenziali delle stesse vittime, trasformando ogni account compromesso in un ulteriore nodo di distribuzione.

Il salto di qualità rispetto ad attacchi precedenti sta nella capacità di auto-propagazione. Il malware utilizza i token raccolti per modificare repository GitHub, inserire workflow malevoli e pubblicare nuove versioni compromesse dei pacchetti.

Questo comportamento avvicina Mini Shai-Hulud a un worm, capace di espandersi autonomamente all’interno dell’ecosistema software. In alcuni casi, il codice introduce configurazioni malevole anche negli strumenti di sviluppo, come file di configurazione per ambienti come Visual Studio Code, che attivano nuovamente il payload quando il repository viene aperto.

Il risultato è una persistenza difficile da individuare. Non si tratta solo di un’infezione temporanea, ma di **una contaminazione che può riattivarsi nel tempo attraverso strumenti legittimi utilizzati quotidianamente dagli sviluppatori**.

Un elemento apparentemente rassicurante è la durata limitata dell’esposizione. I pacchetti compromessi sono rimasti disponibili per poche ore prima di essere rimossi e sostituiti con versioni pulite. Tuttavia, questo non riduce il rischio. Al giorno d’oggi, le pipeline CI/CD scaricano automaticamente dipendenze aggiornate e anche una finestra temporale ridotta è sufficiente per introdurre codice malevolo in ambienti produttivi o di sviluppo, da cui l’attaccante può poi espandersi. Questo aspetto evidenzia una criticità strutturale: **la velocità dei processi DevOps amplifica l’impatto delle compromissioni della supply chain**, riducendo il tempo disponibile per intercettarle.

### **Continuità con le campagne Shai-Hulud precedenti**

L’operazione si inserisce in una serie di **campagne già osservate negli ultimi mesi**, tutte riconducibili al nome Shai-Hulud. Le analisi indicano similitudini nelle tecniche e negli strumenti utilizzati, suggerendo una continuità operativa o almeno un riutilizzo di codice e metodologie.

Rispetto alle versioni precedenti, Mini Shai-Hulud introduce miglioramenti significativi, tra cui **cifratura avanzata dei dati esfiltrati e nuove tecniche di persistenza**. Inoltre, emerge un elemento particolarmente rilevante: l’uso di strumenti legati allo sviluppo assistito da AI come vettori di esecuzione, segnale di come anche questi ambienti stiano diventando parte della superficie di attacco.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [CI CD attack](https://www.securityinfo.it/tag/ci-cd-attack/), [credential stealing malware](https://www.securityinfo.it/tag/credential-stealing-malware/), [DevSecOp...