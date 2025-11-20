---
title: DragonForce evolve in un “cartello” ransomware e diventa più aggressivo
url: https://www.securityinfo.it/2025/11/19/dragonforce-evolve-in-un-cartello-ransomware-e-diventa-piu-aggressivo/
source: Over Security - Cybersecurity news aggregator
date: 2025-11-19
fetch_date: 2025-11-20T03:09:50.140238
---

# DragonForce evolve in un “cartello” ransomware e diventa più aggressivo

Aggiornamenti recenti Novembre 19th, 2025 4:49 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [DragonForce evolve in un “cartello” ransomware e diventa più aggressivo](https://www.securityinfo.it/2025/11/19/dragonforce-evolve-in-un-cartello-ransomware-e-diventa-piu-aggressivo/)
* [Rust riduce sensibilmente le vulnerabilità di memory safety in Android](https://www.securityinfo.it/2025/11/18/rust-riduce-sensibilmente-le-vulnerabilita-di-memory-safety-in-android/)
* [Impressionate! Un attacco DDoS da quasi 16 Tbps contro Azure](https://www.securityinfo.it/2025/11/18/impressionate-un-attacco-ddos-da-quasi-16-tbps-contro-azure/)
* [Il protocollo di rete “Finger” rinasce in attacchi ClickFix](https://www.securityinfo.it/2025/11/17/il-protocollo-di-rete-finger-rinasce-in-attacchi-clickfix/)
* [CERT-AGID 8–14 novembre: ondata di phishing su hosting, PagoPA e università](https://www.securityinfo.it/2025/11/17/cert-agid-8-14-novembre-ondata-di-phishing-su-hosting-pagopa-e-universita/)

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

## DragonForce evolve in un “cartello” ransomware e diventa più aggressivo

Nov 19, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/approfondimenti/minacce/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/11/19/dragonforce-evolve-in-un-cartello-ransomware-e-diventa-piu-aggressivo/#respond)

---

Di recente la Threat Research Unit di Acronis [ha analizzato](https://www.acronis.com/en/tru/posts/the-dragonforce-cartel-scattered-spider-at-the-gate/) nuove attività di **DragonForce**, una gang di ransomware-as-a-service (RaaS) che starebbe utilizzando **variante migliorata e più aggressiva del proprio malware.**

Comparso per la prima volta nel 2023, il gruppo ha fin da subito cominciato a reclutare partner su forum del darkweb per espandere le proprie attività malevole. Dall’inizio del 2025, DragonForce ha optato per un “rebranding” presentandosi come un **“cartello” ransomware**, rafforzando la sua posizione nella scena cybercriminale.

Questo cambiamento lo ha reso un fornitore di infrastrutture per gli altri cybercriminali, con il risultato che anche i gruppi che mancano di conoscenze tecniche specifiche possono usare facilmente il ransomware. I ricercatori di Acronis evidenziano che il modello scelto da DragonForce è particolarmente allettante per gli affiliati per due motivi: in primo luogo, i**l gruppo trattiene come fornitura del servizio soltanto il 20% dei guadagni**, lasciando il restante all’affiliato; in secondo luogo, segue un **approccio “white label”**che consente agli affiliati di usare il proprio brand e sviluppare le proprie varianti di ransomware.

![DragonForce](https://www.securityinfo.it/wp-content/uploads/2025/11/Gemini_Generated_Image_3043uh3043uh3043.png)

La gang ha creato il proprio ransomware basandosi prima su un builder **LockBit 3.0** per i software di crittografia, poi adottando un codice **Conti V3 personalizzato**.

La variante attuale è nata come miglioramento della crittografia usata da **Akira**, un gruppo ransomware rivale di DragonForce. La gang, che le debolezze del ransomware sono state rese note pubblicamente, **ha corretto i difetti di crittografia** che rendevano possibile individuare la chiave privata.

La nuova versione del malware è **pensata per colpire un ampio spettro di sistemi**, inclusi Windows, Linux e le infrastrutture di virtualizzazione ESXi. Il nuovo ransomware utilizza inoltre tecniche avanzate per l’individuazione e la disabilitazione di antivirus prima dell’esecuzione processi di crittografia.

## DragonForce e Scattered Spider

Tra i partner più famosi e attivi della gang c’è **Scattered Spider**, broker di accesso iniziale già noto per essersi affiliato ad altri operatori RaaS come BlackCat, RansomHub e Qilin. Insieme a DragonForce, al gruppo sono stati attribuiti gli [attacchi a Marks & Spencer](https://www.securityinfo.it/2025/05/23/ms-perde-un-terzo-dei-profitti-a-causa-di-un-attacco-informatico/) dello scorso maggio.

Dall’analisi di Acronis emerge una stretta collaborazione tra i due gruppi: “*L’intrusione tipicamente comincia con Scattered Spider che identifica le sue vittime eseguendo una ricognizione sui dipendenti dell’organizzazione per inventarsi un personaggio e un pretesto. Raccoglie informazioni sulle vittime come nome, ruolo e altre informazioni generali attraverso i social media e metodi di intelligence open source*” spiegano i ricercatori.

**Scattered Spider usa tattiche** **basate sull’ingegneria sociale**, come phishing telefonico (vishing), clonazione delle SIM e tecniche per aggirare l’autenticazione a due fattori. La partnership, di fatto, funziona come una catena di montaggio criminale: Scattered Spider si occupa di individuare i bersagli per rubarne le credenziali, penetrare nelle reti aziendali e in seguito esfiltrare dati sensibili; in seguito, distribuiscono il ransomware fornito da DragonForce per richiedere il riscatto.

L’alleanza di DragonForce non si limita solo a ScatteredSpider: il gruppo RaaS si è evoluto in un ecosistema molto ampio che coinvolge, tra gli altri, anche nomi noti quali LAPSUS$ e ShinyHunters.

Un’altra collaborazione interessante è quella con **Devman**: i ricercatori di Acronis hanno individuato campioni di ransomware di questo gruppo creati usando il builder di DragonForce. Ci sono anche numerose somiglianze nella struttura delle note di riscatto.

![ransomware](https://www.securityinfo.it/wp-content/uploads/2024/02/ransomware-3998798_1920.jpg)

Pixabay

Dalla fine del 2023, **DragonForce ha pubblicato i dati di oltre 200 vittime**, colpendo settori che vanno dalle compagnie aeree, alle assicurazioni e agli MSP. L’evoluzione verso un modello a “cartello” ha permesso al gruppo di stringere partnership specializzate che, unite a un rapido miglioramento delle tecniche e tattiche, hanno reso **DragonForce una delle minacce più significative per le organizzazioni.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Conti](https://www.securityinfo.it/tag/conti/), [DragonForce](https://www.securityinfo.it/tag/dragonforce/), [LockBit](https://www.securityinfo.it/tag/lockbit/), [Ransomware](https://www.securityinfo.it/tag/ransomware/), [ransomware-as-a-service](https://www.securityinfo.it/tag/ransomware-as-a-service/), [Scattered Spider](https://www.securityinfo.it/tag/scattered-spider/)

[Rust riduce sensibilmente le vulnerabilità di memory safety in Android](https://www.securityinfo.it/2025/11/18/rust-riduce-se...