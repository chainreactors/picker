---
title: Scoperta una variante del ransomware Mallox basata su Kryptina
url: https://www.securityinfo.it/2024/09/25/scoperta-una-variante-del-ransomware-mallox-basata-su-kryptina/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-26
fetch_date: 2025-10-06T18:40:08.317308
---

# Scoperta una variante del ransomware Mallox basata su Kryptina

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

## Scoperta una variante del ransomware Mallox basata su Kryptina

Set 25, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Malware](https://www.securityinfo.it/category/news/malware-news/), [Minacce](https://www.securityinfo.it/category/minacce-2/), [News](https://www.securityinfo.it/category/news/), [Ransomware](https://www.securityinfo.it/category/minacce-2/ransomware/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2024/09/25/scoperta-una-variante-del-ransomware-mallox-basata-su-kryptina/#respond)

---

I ricercatori di SentinelLabs di SentinelOne [hanno scoperto](https://www.sentinelone.com/labs/kryptina-raas-from-unsellable-cast-off-to-enterprise-ransomware/) una **nuova variante del ransomware Mallox che usa una versione modificata del ransomware Kryptina per attaccare i sistemi Linux.**

Mallox, del gruppo TargetCompany, è un ransomware-as-a-service (RaaS) in uso dal 2021 che viene usato ancora oggi da numerosi affiliati. Anche Kryptina è una piattaforma RaaS, anche se più recente di Mallox, e offre funzionalità per automatizzare payload, gestire più gruppi e campagne e configurare i requisiti di pagamento del riscatto, come la somma e il tipo di pagamento accettato.

![ransomware Mallox](https://www.securityinfo.it/wp-content/uploads/2024/09/ransomware-2321110_1920.jpg)

Pixabay

Nonostante le feature, Kryptina non ha ricevuto l’attenzione che sperava dal mondo del cybercrimine, al punto ch**e l’ideatore della piattaforma ha deciso di smettere di venderla e di pubblicarne il codice sorgente.** In seguito, lo scorso maggio, i ricercatori di SentinelLabs hanno individuato un server di staging di un affiliato di Mallox che conteneva tutti i file sorgente di Kryptina, anche se modificati per supportare una nuova variante del ransomware.

“*L’uso di Kryptina da parte di questo affiliato sembra essere singolare: **le altre varianti Linux di Mallox non sono basate su Kryptina**, complicando ulteriormente la relazione tra Kryptina e Mallox*” spiegano i ricercatori di SentinelLabs.

Il nuovo ransomware, soprannominato “Mallox Linux 1.0”, usa le stesse routine di cifratura e decifratura di Kryptina e il template delle due note di riscatto è molto simile. A parte per i commenti modificati e la rimozione di qualsiasi riferimento ai creatori di Kryptina, **il codice sorgente dei due ransomware è praticamente lo stesso.**

Sul server i ricercatori hanno anche trovato delle cartelle relative a **14 potenziali vittime del ransomware**. Alcune cartelle contenevano tool per la cifratura e decifratura dei file, mentre altre erano vuote: è probabile che si riferissero a vittime già designate ma non ancora colpite.

Il server conteneva inoltre KLAPR.BAT, un tool usato per neutralizzare la protezione dei prodotti di Kaspersky quando necessario, un exploit per sfruttare una vulnerabilità di privilege escalation in Windows 10 e 11 (CVE-2024-21338), numerosi dropper per Mallox (per Windows) e vari altri dropper e payload malevoli.

![ransomware](https://www.securityinfo.it/wp-content/uploads/2024/02/ransomware-3998798_1920.jpg)

Pixabay

Secondo i ricercatori di SentinelOne, **la presenza di una variante di Mallox derivata da Kryptina è indicativa di come il panorama dei ransomware stia diventando sempre più complesso**, evolvendosi in un mix di toolset e codice ormai non più lineari. “*L’adozione di Kryptina da un affiliato attivo di Mallox rappresenta una sorta di ‘evoluzione’ del malware. Ancora più importante, dimostra il diffuso trend della **mercificazione dei ransomware***“.

Visto che il codice sorgente di Kryptina è di dominio pubblico per i cybercriminali, **è probabile che emergano nuove varianti basate su questo RaaS**. La crescente complessità del panorama delle minacce richiede alle aziende di implementare soluzioni di protezione robuste, effettuare backup regolari e istruire i dipendenti sulle buone pratiche di sicurezza.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Kryptina](https://www.securityinfo.it/tag/kryptina/), [Linux](https://www.securityinfo.it/tag/linux/), [Mallox](https://www.securityinfo.it/tag/mallox/), [Ransomware](https://www.securityinfo.it/tag/ransomware/), [ransomware-as-a-service](https://www.securityinfo.it/tag/ransomware-as-a-service/), [variante ransomware](https://www.securityinfo.it/tag/variante-ransomware/)

[Telegram "capitola": l'app fornirà le informazioni degli utenti alle autorità](https://www.securityinfo.it/2024/09/26/telegram-capitola-lapp-fornira-le-informazioni-degli-utenti-alle-autorita/)
[Il trojan Necro ha attaccato 11 milioni di utenti Android](https://www.securityinfo.it/2024/09/24/il-trojan-necro-ha-attaccato-11-milioni-di-utenti-android/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/wp-content/uploads/2025/10/Gemini_Generated_Image_t7m3xlt7m3xlt7m3-120x85.png)](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/ "RedHat vittima di un breach: sottratti oltre 500 GB di dati")

  [RedHat vittima di un breach: sottratti...](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/ "Permanent link to RedHat vittima di un breach: sottratti oltre 500 GB di dati")

  Ott 03, 2025  [0](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/#respond)
* [![Report Acronis: il ransomware rimane la...