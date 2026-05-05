---
title: CISA avvisa: Copy Fail sfruttata per root sui sistemi Linux
url: https://www.securityinfo.it/2026/05/04/cisa-avvisa-copy-fail-sfruttata-per-root-sui-sistemi-linux/?utm_source=rss&utm_medium=rss&utm_campaign=cisa-avvisa-copy-fail-sfruttata-per-root-sui-sistemi-linux
source: Securityinfo.it
date: 2026-05-04
fetch_date: 2026-05-05T05:04:12.077743
---

# CISA avvisa: Copy Fail sfruttata per root sui sistemi Linux

Aggiornamenti recenti Maggio 4th, 2026 3:21 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [CISA avvisa: Copy Fail sfruttata per root sui sistemi Linux](https://www.securityinfo.it/2026/05/04/cisa-avvisa-copy-fail-sfruttata-per-root-sui-sistemi-linux/)
* [Mini Shai-Hulud: la supply chain SAP colpita da un simil-worm](https://www.securityinfo.it/2026/04/30/mini-shai-hulud-la-supply-chain-sap-colpita-da-un-simil-worm/)
* [Honeypot intelligenti: come gli agenti AI ingannano gli attaccanti AI](https://www.securityinfo.it/2026/04/29/honeypot-intelligenti-come-lai-viene-usata-per-ingannare-gli-attaccanti-automatizzati/)
* [I dati sono recuperabili (troppo) facilmente dalle auto moderne](https://www.securityinfo.it/2026/04/28/i-dati-sono-recuperabili-troppo-facilmente-dalle-auto-moderne/)
* [Reset password: una misura di sicurezza che diventa minaccia](https://www.securityinfo.it/2026/04/23/reset-password-una-misura-di-sicurezza-che-diventa-minaccia/)

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

## CISA avvisa: Copy Fail sfruttata per root sui sistemi Linux

Mag 04, 2026  [Redazione](https://www.securityinfo.it/author/redazione/ "Articoli scritti da Redazione")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2026/05/04/cisa-avvisa-copy-fail-sfruttata-per-root-sui-sistemi-linux/#respond)

---

CISA ha inserito **Copy Fail** tra le vulnerabilità sfruttate attivamente, segnalando che la falla viene già usata in attacchi reali per ottenere privilegi di root su sistemi Linux non aggiornati. Il bug, archiviato come **CVE-2026-31431**, riguarda il sottosistema crittografico del kernel Linux e consente a un utente locale non privilegiato di modificare in modo controllato la page cache di file leggibili, inclusi binari setuid-root come `/usr/bin/su`. In pratica, una presenza iniziale anche limitata sul sistema può essere trasformata in **controllo completo della macchina**.

### Perché Copy Fail è così pericolosa

Copy Fail non è una vulnerabilità remota autonoma: per sfruttarla serve già la possibilità di eseguire codice sul sistema. Questo però non la rende meno grave. In molti scenari moderni, soprattutto in cloud, CI/CD, ambienti multi-tenant e Kubernetes, l’esecuzione di codice non privilegiato è una condizione frequente. Un job malevolo in una pipeline, un container compromesso, un accesso SSH a basso privilegio o una web shell possono diventare il punto di partenza per una **escalation immediata a root**.

La criticità è amplificata dalla portata del bug. Secondo CERT-EU, **la vulnerabilità interessa le principali distribuzioni Linux con kernel costruiti a partire dal 2017**, mentre Microsoft cita tra gli ambienti impattati Red Hat, SUSE, Ubuntu e AWS Linux, oltre a un impatto potenziale su larga parte dei workload cloud Linux e dei cluster Kubernetes.

### Il cuore tecnico: AF\_ALG, algif\_aead e page cache

La vulnerabilità si trova in `algif_aead`, il componente che espone agli utenti lo stack crittografico AEAD del kernel attraverso socket **AF\_ALG**. AF\_ALG è un’interfaccia legittima: consente ai processi user space di usare primitive crittografiche implementate nel kernel. Il problema nasce da un’ottimizzazione introdotta nel 2017, pensata per rendere alcune operazioni più efficienti attraverso elaborazioni “in-place”, cioè usando gli stessi buffer come sorgente e destinazione.

Quell’ottimizzazione ha introdotto una condizione anomala nella gestione delle strutture `scatterlist`, usate dal kernel per descrivere aree di memoria non necessariamente contigue. In presenza di una specifica combinazione di operazioni, pagine appartenenti alla **page cache** possono finire dentro una destinazione considerata scrivibile. Il risultato è che un utente non privilegiato può ottenere una primitiva di scrittura limitata ma controllata: **quattro byte alla volta dentro la cache di un file leggibile**.

### Perché quattro byte bastano per ottenere root

A prima vista, una scrittura di quattro byte può sembrare troppo piccola per avere conseguenze serie. In realtà, nel contesto giusto è sufficiente. L’exploit pubblico mostra come sia possibile colpire un binario setuid-root, cioè un eseguibile che, quando viene lanciato, opera con privilegi elevati. **Se l’attaccante modifica in memoria alcune istruzioni del binario**, può far sì che l’esecuzione produca una shell con privilegi di root.

La sequenza sfrutta la combinazione tra socket AF\_ALG e la system call `splice()`. Quest’ultima consente di spostare dati tra file descriptor senza copiarli nello spazio utente, ed è proprio questa interazione con la page cache a rendere possibile l’attacco. **Il payload non modifica il file su disco**: altera la copia in memoria che il kernel usa per servire le letture successive. Quando il binario viene eseguito, il sistema legge la versione corrotta presente in cache e l’attaccante ottiene l’effetto desiderato.

### Il dettaglio più insidioso: la modifica non resta sul disco

Uno degli aspetti più pericolosi di Copy Fail è la sua **natura in-memory**. La pagina corrotta non viene marcata come “dirty” per la scrittura su disco, quindi il file originale rimane apparentemente intatto. Questo significa che controlli basati su checksum del file system o strumenti che confrontano i binari su disco possono non rilevare la modifica.

In termini pratici, l’attaccante può alterare temporaneamente il comportamento di un binario privilegiato **senza lasciare la classica traccia di una modifica persistente al file**. La compromissione avviene nella memoria del kernel, ma l’effetto è immediatamente visibile a livello di sistema perché la page cache è ciò che viene effettivamente consultato quando il file viene letto o eseguito.

### Container, cloud e CI/CD: gli ambienti più esposti

La falla è **particolarmente rilevante negli ambienti containerizzati**. La page cache è condivisa a livello host, quindi una primitiva di corruzione della cache può avere conseguenze oltre il confine apparente del container. Secondo l’analisi tecnica pubblicata dai ricercatori, lo stesso meccanismo può attraversare boundary container perché il target reale non è il file system isolato visto dal container, ma la page cache gestita dal kernel dell’host.

Questo rende Copy Fail **molto pericolosa in scenari Kubernetes e CI/CD**, dove è normale eseguire codice proveniente da repository, build, test automatici o workload temporanei. Un attaccante che riesce a introdurre codice in un runner di build o in un container con privilegi minimi può usare la vulnerabilità per scalare a root sull’host, con conseguenze dirette su segreti, immagini, pipeline, credenziali cloud e altri workload presenti nel...