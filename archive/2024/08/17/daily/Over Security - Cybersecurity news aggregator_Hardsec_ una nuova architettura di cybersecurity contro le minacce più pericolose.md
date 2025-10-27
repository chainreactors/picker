---
title: Hardsec: una nuova architettura di cybersecurity contro le minacce più pericolose
url: https://www.securityinfo.it/2024/08/16/hardsec-una-nuova-architettura-di-cybersecurity-contro-le-minacce-piu-pericolose/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-17
fetch_date: 2025-10-06T18:07:45.689337
---

# Hardsec: una nuova architettura di cybersecurity contro le minacce più pericolose

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

## Hardsec: una nuova architettura di cybersecurity contro le minacce più pericolose

Ago 16, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Minacce](https://www.securityinfo.it/category/approfondimenti/minacce/), [RSS](https://www.securityinfo.it/category/rss/), [Tecnologia](https://www.securityinfo.it/category/approfondimenti/tecnologia/)
 [0](https://www.securityinfo.it/2024/08/16/hardsec-una-nuova-architettura-di-cybersecurity-contro-le-minacce-piu-pericolose/#respond)

---

Quando le minacce informatiche diventano più pericolose, la cybersecurity si fa più “dura” per contrastarle: è così che nasce l’**Hardsec** (Hardware Security), un’architettura di cybersicurezza emergente che vuole rivoluzionare il modo in cui si pensa alla sicurezza, superando i problemi tradizionali.

![Hardsec](https://www.securityinfo.it/wp-content/uploads/2024/08/security-4851428_1920.jpg)

Pixabay

I software di protezione contro le cyberminacce soffrono anch’essi di problemi di sicurezza e possono essere compromessi. “***Il software che viene eseguito su una CPU che è (approssimativamente) una macchina di Turing è per natura difficile da proteggere contro le compromissioni*“** si legge sul [white paper](https://hardsec.com/) dell’architettura redatto da Sandy Macadam; passare alla sicurezza a livello di hardware è però costoso e poco flessibile, tanto da essere impraticabile.

La soluzione è l’approccio Hardsec, il quale utilizza i **dispositivi Field Programmable Gate Array** (FPGA) che garantisce l’eliminazione delle minacce sfruttando le **implementazioni *non-Turing*.**

Gli FPGA sono dei **circuiti integrati che possono essere riprogrammati ripetutamente nel tempo**; questa caratteristica gli permette di essere più robusti a livello di cybersecurity in quanto, se un’implementazione si rileva errata o se servono nuove feature, i dispositivi possono essere riprogrammati facilmente.

Il fatto che questi dispositivi possano essere riprogrammati implica che, potenzialmente, anche un attaccante può farlo; per prevenire questa possibilità**, l’architettura Hardsec è stata sviluppata per dipendere dalla disposizione fisica delle connessioni.** Poiché gli FPGA possono essere riprogrammati solo usando specifici pin fisici, gli attaccanti che non hanno accesso a questi pin non possono alterare la sicurezza dei dispositivi.

Nel dettaglio, un’implementazione FPGA ha un meccanismo di gestione dei pin che è separato dai percorsi di input e output del dispositivo, quindi se l’attaccante ha accesso fisico solo a questi due, non può comunque riprogrammare L’FPGA.

![](https://www.securityinfo.it/wp-content/uploads/2024/08/image001.png)

Credits: Sandy Macadam

Usando la logica hardware degli FPGA in combinazione con le soluzioni software più robuste è possibile implementare una **difesa solida contro le minacce più pericolose in circolazione.**

The Hacker News [sottolinea](https://thehackernews.com/2024/08/why-hardsec-matters-from-protecting.html) che questo tipo di protezione è particolarmente indicata per settori altamente regolamentati, come il governativo, il finanziario e quello della difesa, i quali devono rispettare standard di settore molto severi.

Diverse agenzie governative e organizzazioni di cybersecurity, come il Dipartimento della Difesa statunitense, il NIST e l’NCSC, stanno già spingendo le aziende a implementare l’approccio Hardsec.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [architettura di cybersecurity](https://www.securityinfo.it/tag/architettura-di-cybersecurity/), [circuiti integrati](https://www.securityinfo.it/tag/circuiti-integrati/), [cybersecurity](https://www.securityinfo.it/tag/cybersecurity/), [FPGA](https://www.securityinfo.it/tag/fpga/), [Hardsec](https://www.securityinfo.it/tag/hardsec/), [protezione](https://www.securityinfo.it/tag/protezione/)

[CERT-AGID 10 luglio – 16 agosto: cPanel e webmail sotto attacco](https://www.securityinfo.it/2024/08/19/cert-agid-10-luglio-16-agosto-cpanel-webmail-sotto-attacco/)
[0.0.0.0 Day, la vulnerabilità "maggiorenne" che colpisce i principali browser](https://www.securityinfo.it/2024/08/14/0-0-0-0-day-la-vulnerabilita-maggiorenne-che-colpisce-tutti-i-principali-browser/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Ondata di attacchi brute-force contro le VPN Fortinet, poi FortiManager](https://www.securityinfo.it/wp-content/uploads/2025/08/FortinetVPN13-ago-2025CG-120x85.png)](https://www.securityinfo.it/2025/08/12/ondata-di-attacchi-brute-force-contro-le-vpn-fortinet-poi-fortimanager/ "Ondata di attacchi brute-force contro le VPN Fortinet, poi FortiManager")

  [Ondata di attacchi brute-force contro...](https://www.securityinfo.it/2025/08/12/ondata-di-attacchi-brute-force-contro-le-vpn-fortinet-poi-fortimanager/ "Permanent link to Ondata di attacchi brute-force contro le VPN Fortinet, poi FortiManager")

  Ago 12, 2025  [0](https://www.securityinfo.it/2025/08/12/ondata-di-attacchi-brute-force-contro-le-vpn-fortinet-poi-fortimanager/#respond)
* [![SonicWall: Akira non sfrutta uno zero-day, ma una falla del 2024](https://www.securityinfo.it/wp-content/uploads/2025/08/Firewall-8-ago-2025CG-120x85.png)](https://www.securityinfo.it/2025/08/08/sonicwall-akira-non-sfrutta-uno-zero-day-ma-una-falla-del-2024/ "SonicWall: Akira non sfrutta uno zero-day, ma una falla del 2024")

  [SonicWall: Akira non sfrutta uno...](https://www.securityinfo.it/2025/08/08/sonicwall-akira-non-sfrutta-uno-zero-day-ma-una-falla-del-2024/ "Permanent link to SonicWall: Akira non sfrutta uno zero-day, ma una falla del...