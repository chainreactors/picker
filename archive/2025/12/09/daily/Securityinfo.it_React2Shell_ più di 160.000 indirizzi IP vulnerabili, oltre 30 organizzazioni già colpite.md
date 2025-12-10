---
title: React2Shell: più di 160.000 indirizzi IP vulnerabili, oltre 30 organizzazioni già colpite
url: https://www.securityinfo.it/2025/12/09/react2shell-piu-di-160-000-indirizzi-ip-vulnerabili-oltre-30-organizzazioni-gia-colpite/?utm_source=rss&utm_medium=rss&utm_campaign=react2shell-piu-di-160-000-indirizzi-ip-vulnerabili-oltre-30-organizzazioni-gia-colpite
source: Securityinfo.it
date: 2025-12-09
fetch_date: 2025-12-10T03:22:36.283878
---

# React2Shell: più di 160.000 indirizzi IP vulnerabili, oltre 30 organizzazioni già colpite

Aggiornamenti recenti Dicembre 9th, 2025 10:15 AM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [React2Shell: più di 160.000 indirizzi IP vulnerabili, oltre 30 organizzazioni già colpite](https://www.securityinfo.it/2025/12/09/react2shell-piu-di-160-000-indirizzi-ip-vulnerabili-oltre-30-organizzazioni-gia-colpite/)
* [CERT-AGID 29 novembre – 5 dicembre: phishing a tema Governo italiano e Agenzia delle Entrate](https://www.securityinfo.it/2025/12/08/cert-agid-29-novembre-5-dicembre-phishing-governo-italiano-agenzia-entrate/)
* [Iniezione indiretta di prompt: a rischio le informazioni aziendali](https://www.securityinfo.it/2025/12/05/iniezione-indiretta-di-prompt-a-rischio-le-informazioni-aziendali/)
* [Dark Telegram in ritirata: aumentano le chiusure dei canali clandestini](https://www.securityinfo.it/2025/12/04/dark-telegram-in-ritirata-aumentano-le-chiusure-dei-canali-clandestini/)
* [PickleScan, scoperti tre bug 0-day che permettono di iniettare payload malevoli nei modelli ML](https://www.securityinfo.it/2025/12/03/picklescan-scoperti-tre-bug-0-day-che-permettono-di-iniettare-payload-malevoli-nei-modelli-ml/)

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

## React2Shell: più di 160.000 indirizzi IP vulnerabili, oltre 30 organizzazioni già colpite

Dic 09, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/12/09/react2shell-piu-di-160-000-indirizzi-ip-vulnerabili-oltre-30-organizzazioni-gia-colpite/#respond)

---

**React2Shell**, una vulnerabilità di React che consente l’esecuzione di codice da remoto, è già stata sfruttata dagli attaccanti per **colpire più di 30 organizzazioni**di diversi settori.

La vulnerabilità (CVE-2025-55182), scoperta dal ricercatore di sicurezza Lachlan Davidson, è stata [resa nota](https://react.dev/blog/2025/12/03/critical-security-vulnerability-in-react-server-components) lo scorso 3 dicembre. Il bug consente a un attaccante di “***eseguire codice da remoto senza autenticazione**sfruttando un errore nel modo in cui React decodifica i payload inviati agli endpoint di React Server Function*“, come si legge nel blog della compagnia.

Il giorno dopo, il 4 dicembre, il ricercatore Maple3142 ha condiviso su X una [PoC](https://x.com/maple3142/status/1996687157789155647) per dimostrare l’efficacia degli attacchi che sfruttano React2Shell contro i server React vulnerabili.

![React2Shell](https://www.securityinfo.it/wp-content/uploads/2025/12/Gemini_Generated_Image_uj8xe1uj8xe1uj8x.png)

A distanza di qualche giorno, l’impatto di React2Shell appare preoccupante: secondo i [dati condivisi](https://dashboard.shadowserver.org/statistics/combined/time-series/?date_range=7&source=http_vulnerable&source=http_vulnerable6&tag=cve-2025-55182%2B&dataset=unique_ips&limit=100&group_by=tag&stacking=stacked&auto_update=on) e aggiornati quotidianamente dal gruppo ShadowServer, a oggi sono **165.712 gli indirizzi IP vulnerabili**, un numero che negli scorsi giorni ha continuato ad aumentare. Stando alla [mappa](https://dashboard.shadowserver.org/statistics/combined/map/?date_range=1&map_type=std&source=http_vulnerable&source=http_vulnerable6&tag=cve-2025-55182%2B&data_set=count&scale=log&auto_update=on) della distribuzione geografica degli IP, gli Stati Uniti contano la maggior parte degli indirizzi IP vulnerabili a livello globale.

Come riporta anche [Bleeping Computer](https://www.bleepingcomputer.com/news/security/react2shell-flaw-exploited-to-breach-30-orgs-77k-ip-addresses-vulnerable/), da quando la vulnerabilità è stata resa nota numerosi ricercatori e compagnie di sicurezza hanno segnalato uno **sfruttamento piuttosto diffuso del bug.**

Secondo i report condivisi, gli attaccanti sfruttano la vulnerabilità per eseguire una prima ricognizione sui server; in seguito, tentano di sottrarre file di configurazione e credenziali AWS ed eseguono comandi arbitrari. Durante queste intrusioni, gli attaccanti hanno distribuito malware quali **Snowlight** e **Vshell**, una backdoor comunemente usata dai cyberattaccanti cinesi per muoversi lateralmente nelle reti compromesse.

I ricercatori hanno collegato agli attacchi gruppi APT cinesi come Earth Lamia, Jackpot Panda e **UNC5174**, un gruppo che sembrerebbe essere legato al Ministero della Sicurezza dello Stato cinese.

Per proteggersi dalla vulnerabilità, gli sviluppatori devono **aggiornare React all’ultima versione** ed effettuare di nuovo build e deploy delle applicazioni. La CISA ha richiesto alle agenzie federali di applicare le patch entro il 26 dicembre.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [backdoor](https://www.securityinfo.it/tag/backdoor/), [React](https://www.securityinfo.it/tag/react/), [React2Shell](https://www.securityinfo.it/tag/react2shell/), [Snowlight](https://www.securityinfo.it/tag/snowlight/), [Vshell](https://www.securityinfo.it/tag/vshell/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[CERT-AGID 29 novembre – 5 dicembre: phishing a tema Governo italiano e Agenzia delle Entrate](https://www.securityinfo.it/2025/12/08/cert-agid-29-novembre-5-dicembre-phishing-governo-italiano-agenzia-entrate/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![PickleScan, scoperti tre bug 0-day che permettono di iniettare payload malevoli nei modelli ML](https://www.securityinfo.it/wp-content/uploads/2025/12/Gemini_Generated_Image_ydrt5rydrt5rydrt-120x85.png)](https://www.securityinfo.it/2025/12/03/picklescan-scoperti-tre-bug-0-day-che-permettono-di-iniettare-payload-malevoli-nei-modelli-ml/ "PickleScan, scoperti tre bug 0-day che permettono di iniettare payload malevoli nei modelli ML")

  [PickleScan, scoperti tre bug 0-day che...](https://www.securityinfo.it/2025/12/03/picklescan-scoperti-tre-bug-0-day-che-permettono-di-iniettare-payload-malevoli-nei-modelli-ml/ "Permanent link to PickleScan, scoperti tre bug 0-day che permettono di iniettare payload malevoli nei modelli ML")

  Dic 03, 2025  [0](https://www.securityinfo.it/2025/12/03/picklescan-scoperti-tre-bug-0-day-che-permettono-di-iniettare-payload-malevoli-nei-modelli-ml/#respond)
* [![ShadyPanda: oltre 4 milioni di browser infetti in una campagna durata 7 anni](https://www.securityinfo.it/wp-content/uploads/2025/12/Gemini_Generated_Image_hnl02xhnl02xhnl0-120x85.png)](https://www.securityinfo.it/2025/12/02/shadypanda-oltre-4-milioni-di-bro...