---
title: Come funziona Cicada3301 e il suo programma per gli affiliati
url: https://www.securityinfo.it/2024/10/21/come-funziona-cicada3301-e-il-suo-programma-per-gli-affiliati/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-22
fetch_date: 2025-10-06T18:55:32.859146
---

# Come funziona Cicada3301 e il suo programma per gli affiliati

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

## Come funziona Cicada3301 e il suo programma per gli affiliati

Ott 21, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Malware](https://www.securityinfo.it/category/approfondimenti/malware/), [Minacce](https://www.securityinfo.it/category/approfondimenti/minacce/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2024/10/21/come-funziona-cicada3301-e-il-suo-programma-per-gli-affiliati/#respond)

---

Di recente il team di [Group-IB](https://www.group-ib.com/blog/cicada3301/) è riuscito a ottenere accesso al **pannello degli affiliati di Cicada3301**, un ransomware-as-a-service scoperto lo scorso giugno che ha colpito numerose realtà dei settori critici, soprattutto negli Stati Uniti e nel Regno Unito. Da giugno, il gruppo **ha preso di mira 30 organizzazioni in soli tre mesi** e ha pubblicato sul proprio sito i dati sottratti.

Il gruppo ha cominciato a cercare affiliati (pentester e access broker) sul forum RAMP del dark web poco prima di cominciare le sue operazioni. Coloro che vogliono  diventare affiliati del gruppo devono prendere parte a una piccola intervista; inoltre, la richiesta è di non colpire i Paesi della Comunità degli Stati Indipendenti. I cybercriminali dietro Cicada3301 chiedono inoltre un **20% del riscatto ottenuto dalle vittime.**

![Cicada3301](https://www.securityinfo.it/wp-content/uploads/2024/10/ransomware-2321110_1920.jpg)

Il ransomware, **scritto in Rust**, può essere eseguito su Windows, Linux, ESXi e NAS. Il malware usa **ChaCha20** e **RSA** per la cifratura; questa operazione può essere eseguita in tre diverse modalità (Completa, Veloce, Automatica) e **permette di cifrare sia totalmente che parzialmente i file** per ottimizzare la velocità e l’impatto dell’attacco.

Il team di Group-IB è riuscito a ottenere l’accesso al pannello degli affiliati e approfondire le funzionalità del ransomware. Dall’interfaccia web del ransomware gli affiliati possono accedere a **chat**, **canali di supporto** e visualizzare gli account di sub-affiliati. L’interfaccia consente di costruire un locker personalizzato, generare una landing page, personalizzare le note di riscatto e il file storage per i dati sottratti.

Il pannello contiene anche una **dashboard** con informazioni quali il numero di compagnie attaccate, i dettagli di fingerprinting e il numero di login falliti o di successo. C’è inoltre una sezione “**Notizie**” dove il gruppo di Cicaca3001 pubblica eventuali aggiornamenti sul programma, la sezione “**Compagnie**” dove gli affiliati possono aggiungere le vittime da colpire e i dettagli dell’attacco e la sezione “FAQ” che specifica regole e linee guida per l’uso della piattaforma.

## Il flusso d’attacco di Cicada3301

Una volta infiltrato il sistema target, nel caso di sistema operativo Windows **il ransomware disabilita l’esecuzione automatica di Windows Recovery Environment**, cancella le copie shadow e pulisce il log degli eventi. Subito dopo, il malware interrompe processi e servizi in esecuzione, comprese le macchine virtuali. Infine, viene eseguito il locker per cominciare la cifratura dei file.

Nel caso della variante Linux, il ransomware esclude dalla cifratura i file .lock e .tml e quelli che si trovano nelle cartelle `/etc, /run, /usr, /sys, /dev, /bin, /lib, /boot, /snap, /proc, /sbin, /lib64, /cdrom`. Per i sistemi ESXi, invece, il ransomware per prima cosa elimina tutte le macchine virtuali in esecuzione e cancella tutti gli snapshot.

![ransomware](https://www.securityinfo.it/wp-content/uploads/2024/02/ransomware-3998798_1920.jpg)

Pixabay

Il team di Group-IB sottolinea che Cicada3301, con  il suo programma di affiliati, si è confermato come **una delle minacce più significative degli ultimi mesi**. “*Le loro operazioni sono caratterizzate da tattiche aggressive progettate per massimizzare l’impatto, come l’interruzione dei servizi essenziali, l’arresto delle macchine virtuali e la crittografia dei dati su varie piattaforme e condivisioni di* *rete*“.

Visto l’aumento del numero di minacce ransomware e della loro pericolosità, i ricercatori di Group-IB ricordano alle aziende di implementare l’**MFA per gli asset critici** e scegliere **soluzioni di EDR e XDR** per identificare la presenza di malware il prima possibile. È inoltre indispensabile avere una s**trategia di backup robusta**, **mantenere aggiornati i software** e investire sulla **formazione dei dipendenti.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [affiliati](https://www.securityinfo.it/tag/affiliati/), [Cicada3301](https://www.securityinfo.it/tag/cicada3301/), [cifratura](https://www.securityinfo.it/tag/cifratura/), [Ransomware](https://www.securityinfo.it/tag/ransomware/), [ransomware-as-a-service](https://www.securityinfo.it/tag/ransomware-as-a-service/), [riscatto](https://www.securityinfo.it/tag/riscatto/)

[I SOC dedicano quasi due ore al giorno all'analisi di falsi positivi](https://www.securityinfo.it/2024/10/21/i-soc-dedicano-quasi-due-ore-al-giorno-allindagine-di-falsi-positivi/)
[Netskope: connettività cloud sicura e veloce per ogni azienda](https://www.securityinfo.it/2024/10/20/netskope-connettivita-cloud-sicura-e-veloce-per-ogni-azienda/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/wp-content/uploads/2025/10/Gemini_Generated_Image_t7m3xlt7m3xlt7m3-120x85.png)](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-bre...