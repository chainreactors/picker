---
title: Anubis, un nuovo ransomware che integra un wiper
url: https://www.securityinfo.it/2025/06/16/anubis-un-nuovo-ransomware-che-integra-un-wiper/?utm_source=rss&utm_medium=rss&utm_campaign=anubis-un-nuovo-ransomware-che-integra-un-wiper
source: Securityinfo.it
date: 2025-06-17
fetch_date: 2025-10-06T22:57:13.793456
---

# Anubis, un nuovo ransomware che integra un wiper

Aggiornamenti recenti Ottobre 6th, 2025 3:00 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Microsoft Sentinel: arriva l’era degli agenti AI e della difesa predittiva](https://www.securityinfo.it/2025/10/06/microsoft-sentinel-arriva-lera-degli-agenti-ai-e-della-difesa-predittiva/)
* [CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)
* [Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)

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

## Anubis, un nuovo ransomware che integra un wiper

Giu 16, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/06/16/anubis-un-nuovo-ransomware-che-integra-un-wiper/#respond)

---

I ricercatori di Trend Micro [hanno individuato](https://www.trendmicro.com/en_us/research/25/f/anubis-a-closer-look-at-an-emerging-ransomware.html) **Anubis**, un nuovo malware usato in operazioni **Ransomware-as-a-Service** che non si limita a cifrare i file, ma anche a cancellarli con un wiper.

“*Anubis è un gruppo identificato di recente che si distingue per abbinare la crittografia a capacità più distruttive, come la cancellazione di directory che influisce pesantemente sulle possibilità di recupero dei file. Data la sua breve storia e l’uso di un modello di estorsione a più livelli, **Anubis ha tutte le caratteristiche di un’operazione RaaS in evoluzione e flessibile***” hanno affermato i ricercatori.

![Anubis](https://www.securityinfo.it/wp-content/uploads/2025/06/Gemini_Generated_Image_olrxraolrxraolrx-scaled.jpg)

Anubis

Come riporta Trend Micro, il gruppo dietro il ransomware ha fatto la sua comparsa su X lo scorso dicembre; nello stesso periodo, Trend Micro ha individuato un malware ancora in fase di sviluppo chiamato Sphinx. Comparando i binari dei due malware, il team ha scoperto che erano praticamente identici, fatta eccezione solo per la funzione che generava la nota del riscatto.

Anubis ha cominciato la sua attività a inizio anno e si è distinto per la sua **funzionalità aggiuntiva di wiper**: il ransomware infatti è anche in grado di cancellare cartelle e file essenziali per il ripristino dei sistemi dopo la cifratura, complicando di fatto la risposta delle vittime. Questa capacità non fa altro che **aumentare la pressione sulle imprese** **colpite** e quindi incrementare la probabilità che cedano al pagamento del riscatto.

Secondo i ricercatori di Trend Micro, gli attaccanti utilizzano lo spear phishing per l’accesso iniziale ai sistemi, condividendo link o allegati malevoli contenenti il payload del ransomware. Il wiper non viene eseguito sempre, ma solo se gli attaccanti hanno impostato uno specifico parametro per l’esecuzione (“WIPEMODE”) per **cancellare permanentemente il contenuto di specifici file**.

![Anubis](https://www.securityinfo.it/wp-content/uploads/2025/06/Anubis.png)

Credits: Trend Micro

“*Combinando RaaS con strategie di monetizzazione aggiunte, come i programmi di affiliazione per il ransomware dei dati e la monetizzazione dell’accesso, **Anubis sta massimizzando il suo potenziale di guadagno** ed espandendo la sua portata all’interno dell’ecosistema dei criminali informatici*” sottolinea Trend Micro.

Le indicazioni per proteggersi da Anubis, come da altri ransomware, includono una maggiore attenzione ai contenuti delle email, backup regolari, possibilmente offline, implementazione di un piano di recovery robusto, un controllo degli accessi stringente e preciso, l’uso di tool di sandboxing per l’analisi dei file prima dell’esecuzione e scansioni aggiornamenti software regolari.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Anubis](https://www.securityinfo.it/tag/anubis/), [Ransomware](https://www.securityinfo.it/tag/ransomware/), [ransomware-as-a-service](https://www.securityinfo.it/tag/ransomware-as-a-service/), [Sphinx](https://www.securityinfo.it/tag/sphinx/), [Trend Micro](https://www.securityinfo.it/tag/trend-micro/), [wiper](https://www.securityinfo.it/tag/wiper/)

[Fog ransomware, un ransomware anomalo a una finanziaria asiatica](https://www.securityinfo.it/2025/06/17/fog-ransomware-un-ransomware-anomalo-a-una-finanziaria-asiatica/)
[EchoLeak: è arrivata la prima vulnerabilità zero clic per le IA (Microsoft 365 Copilot)](https://www.securityinfo.it/2025/06/13/echoleak-e-arrivata-la-prima-vulnerabilita-zero-clic-per-le-ia-microsoft-365-copilot/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/wp-content/uploads/2025/10/Gemini_Generated_Image_t7m3xlt7m3xlt7m3-120x85.png)](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/ "RedHat vittima di un breach: sottratti oltre 500 GB di dati")

  [RedHat vittima di un breach: sottratti...](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/ "Permanent link to RedHat vittima di un breach: sottratti oltre 500 GB di dati")

  Ott 03, 2025  [0](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/#respond)
* [![Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-6138007_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/ "Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA")

  [Report Acronis: il ransomware rimane la...](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/ "Permanent link to Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su ...