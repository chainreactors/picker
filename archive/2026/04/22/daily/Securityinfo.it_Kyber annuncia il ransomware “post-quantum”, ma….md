---
title: Kyber annuncia il ransomware “post-quantum”, ma…
url: https://www.securityinfo.it/2026/04/22/kyber-annuncia-il-ransomware-post-quantum-ma/?utm_source=rss&utm_medium=rss&utm_campaign=kyber-annuncia-il-ransomware-post-quantum-ma
source: Securityinfo.it
date: 2026-04-22
fetch_date: 2026-04-23T04:44:58.397195
---

# Kyber annuncia il ransomware “post-quantum”, ma…

Aggiornamenti recenti Aprile 22nd, 2026 2:07 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Kyber annuncia il ransomware “post-quantum”, ma…](https://www.securityinfo.it/2026/04/22/kyber-annuncia-il-ransomware-post-quantum-ma/)
* [L’App europea di verifica dell’età è stata bucata in due minuti](https://www.securityinfo.it/2026/04/17/lapp-europea-di-verifica-delleta-e-stata-bucata-in-meno-di-due-minuti/)
* [Recovery scam: quando la truffa colpisce due volte](https://www.securityinfo.it/2026/04/16/recovery-scam-quando-la-truffa-colpisce-due-volte/)
* [Supply chain: il 69% delle aziende pronto a co-finanziare la sicurezza](https://www.securityinfo.it/2026/04/15/supply-chain-il-69-delle-aziende-pronto-a-finanziare-la-sicurezza-dei-fornitori/)
* [Donne e cybersecurity: crescono le nuove leve e alcune sfide](https://www.securityinfo.it/2026/04/14/donne-e-cybersecurity-crescono-le-nuove-leve-e-alcune-sfide/)

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

## Kyber annuncia il ransomware “post-quantum”, ma…

Apr 22, 2026  [Redazione](https://www.securityinfo.it/author/redazione/ "Articoli scritti da Redazione")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Tecnologia](https://www.securityinfo.it/category/news/tecnologia-news/)
 [0](https://www.securityinfo.it/2026/04/22/kyber-annuncia-il-ransomware-post-quantum-ma/#respond)

---

**Kyber** è un gruppo ransomware relativamente recente che ha attirato un po’ di attenzione su di sé per le ultime operazioni condotte e una postura piuttosto esibizionista nel dark Web. Questa settimana, ha pubblicato un post a proposito di un attacco riuscito usando un sistema di cifratura post-quantum per bloccare i dati della vittima.  Dietro la narrativa tecnologica avanzata si nasconde, però, una realtà più complessa, in cui marketing criminale e implementazione tecnica non sempre coincidono.

![](https://www.securityinfo.it/wp-content/uploads/2026/04/Ransomwarepubblicita-1024x559.png)

Secondo [l’analisi pubblicata da Rapid7](https://www.rapid7.com/blog/post/tr-kyber-ransomware-double-trouble-windows-esxi-attacks-explained/), la gang ha sviluppato **due varianti distinte** del ransomware, entrambe utilizzate nello stesso attacco per massimizzare l’impatto su infrastrutture eterogenee.

### **Attacchi coordinati tra Windows e VMware ESXi**

La strategia operativa di Kyber è ben precisa: **colpire simultaneamente ambienti virtualizzati e server tradizionali**, ogni ambiente con una versione dedicata del malware. Le due varianti analizzate condividono infatti lo stesso campaign ID e la stessa infrastruttura di pagamento basata su Tor, suggerendo l’azione di un unico affiliato.

Ci sono, però, differenze evidenti tra le due. La variante dedicata a VMware ESXi è progettata per **ambienti virtualizzati enterprise**, dove può **censire tutte le macchine virtuali, cifrare i datastore e modificare le interfacce di gestione** con messaggi di riscatto, guidando le vittime nel processo di pagamento.

Parallelamente, la versione Windows — sviluppata in Rust — prende di mira i file server e introduce anche funzionalità sperimentali per **interagire con ambienti Hyper-V**, ampliando ulteriormente la superficie d’attacco.

### **Il “falso” post-quantum e la realtà crittografica**

Il punto più interessante di tutta la vicenda riguarda la presunta adozione di crittografia post-quantum. La gang pubblicizza l’uso di **Kyber1024**, un algoritmo di key encapsulation appartenente alla famiglia delle tecnologie post-quantum. Tuttavia, l’analisi tecnica rivela una situazione diversa. **Nella variante Linux/ESXi, il post-quantum non è realmente utilizzato** perché il ransomware impiega **ChaCha8 per la cifratura dei file e RSA-4096 per la protezione delle chiavi**, seguendo schemi già consolidati nel panorama ransomware.

Diverso il caso della variante Windows, dove Kyber1024 viene effettivamente implementato — ma con un ruolo limitato. Come chiarisce Rapid7, **Kyber non cifra direttamente i dati**, ma protegge le chiavi simmetriche utilizzate da algoritmi tradizionali come AES-CTR.

Il risultato è che **l’introduzione del post-quantum non cambia l’impatto operativo dell’attacco**. Senza la chiave privata degli attaccanti, i dati restano comunque irrecuperabili, indipendentemente dall’algoritmo utilizzato.

### **Tecniche di distruzione e anti-recovery sempre più aggressive**

La variante Windows appare più evoluta anche per quanto riguarda le tecniche di sabotaggio dei sistemi compromessi. Il malware è progettato per **eliminare ogni possibile via di recupero dei dati**, attraverso una serie coordinata di azioni.

Tra queste emergono la **cancellazione delle shadow copies**, la disattivazione dei meccanismi di ripristino, l’interruzione di servizi critici come SQL Server ed Exchange e la rimozione dei backup. Inoltre, il ransomware procede con la **pulizia dei log di sistema e del cestino**, rendendo più difficile anche l’attività forense post-incidente.

Interessante — e quasi ironico — è **la presenza di un mutex che sembra fare riferimento a una canzone sulla piattaforma Boomplay**, un dettaglio che suggerisce un certo grado di personalizzazione o “firma” degli sviluppatori.

Resta il fatto che in questa fase **Kyber sta facendo più marketing che sfoggio di capacità tecnologiche avanzate**. Il motivo non è chiarissimo dal momento che non c’è alcun motivo per un gruppo ransomware di “farsi pubblicità”, ma evidentemente anche l’ego dei criminali vuole la sua parte.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [crittografia post quantum sicurezza](https://www.securityinfo.it/tag/crittografia-post-quantum-sicurezza/), [cybercrime evoluzione](https://www.securityinfo.it/tag/cybercrime-evoluzione/), [kyber ransomware](https://www.securityinfo.it/tag/kyber-ransomware/), [kyber1024](https://www.securityinfo.it/tag/kyber1024/), [post quantum ransomware](https://www.securityinfo.it/tag/post-quantum-ransomware/), [ransomware esxi](https://www.securityinfo.it/tag/ransomware-esxi/), [ransomware windows rust](https://www.securityinfo.it/tag/ransomware-windows-rust/), [rapid7 analisi](https://www.securityinfo.it/tag/rapid7-analisi/)

[L’App europea di verifica dell’età è stata bucata in due minuti](https://www.securityinfo.it/2026/04/17/lapp-europea-di-verifica-delleta-e-stata-bucata-in-meno-di-due-minuti/)

---

![](https://secure.gravatar.com/avatar/57d6369d65bf9ebecae351af675ce2fd?s=90&d=mm&r=g)

##### [Redazione](https://www.securityinfo.it/author/redazione/)

##### Articoli correlati

##### Altro in questa categoria

* [![L’App europea di verifica dell’età è stata bucata in due minuti](https://www.securityinfo.it/wp-content/uploads/2026/04/AgeVerificationBuggata-120x85.png)](https://www.securityinfo.it/2026/04/17/...