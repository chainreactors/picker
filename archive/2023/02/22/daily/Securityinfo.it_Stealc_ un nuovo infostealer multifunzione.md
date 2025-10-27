---
title: Stealc: un nuovo infostealer multifunzione
url: https://www.securityinfo.it/2023/02/21/stealc-un-nuovo-infostealer-multifunzione/?utm_source=rss&utm_medium=rss&utm_campaign=stealc-un-nuovo-infostealer-multifunzione
source: Securityinfo.it
date: 2023-02-22
fetch_date: 2025-10-04T07:47:51.551028
---

# Stealc: un nuovo infostealer multifunzione

Aggiornamenti recenti Ottobre 3rd, 2025 6:09 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)
* [Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)
* [Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/)
* [Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/)

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

## Stealc: un nuovo infostealer multifunzione

Feb 21, 2023  [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/ "Articoli scritti da Dario Orlandi")
 [Malware](https://www.securityinfo.it/category/news/malware-news/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [Minacce](https://www.securityinfo.it/category/minacce-2/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Trojan](https://www.securityinfo.it/category/minacce-2/trojan/)
 [0](https://www.securityinfo.it/2023/02/21/stealc-un-nuovo-infostealer-multifunzione/#respond)

---

Un [nuovo report](https://blog.sekoia.io/stealc-a-copycat-of-vidar-and-raccoon-infostealers-gaining-in-popularity-part-1/) dei ricercatori di sicurezza di [Sekoia](https://www.sekoia.io/en/homepage/) ha segnalato la crescente popolarità di **un nuovo infostealer, chiamato Stealc**, che è stato molto pubblicizzato sul dark web nelle ultime settimane.

I ricercatori di Sekoia hanno **individuato il nuovo ceppo a gennaio** e hanno iniziato a individuarlo all’opera in the wild all’inizio di febbraio.

Stealc è un malware promosso su forum e canali dedicati da un utente chiamato Plymouth. Plymouth ha presentato Stealc come un **malware con ampie capacità di furto di dati** e un pannello di amministrazione facile da usare.

Oltre al targeting dei dati del browser, delle estensioni e dei portafogli di criptovaluta, Stealc ha un grabber di file personalizzabile per rubare qualsiasi tipo di file desiderato. Plymouth ha promosso il malware su vari forum e canali privati di Telegram, **offrendo campioni di prova** ai potenziali clienti.

![](https://www.securityinfo.it/wp-content/uploads/2023/02/xss_plymouth_free_tests.png)

Fonte: Sekoia

**Stealc viene sviluppato attivamente** e Plymouth ha creato un canale Telegram dedicato ai changelog della nuova versione. Plymouth ha anche affermato che Stealc si basa sui progetti Vidar, Raccoon, Mars e Redline.

I ricercatori hanno scoperto più di 40 server C2 per Stealc e diverse decine di campioni utilizzati attivamente, indicando che **il** **nuovo malware ha attirato l’interesse dei criminali informatici**.

Questa popolarità può essere spiegata con il fatto che i clienti con accesso al pannello di amministrazione possono generare nuovi sample, aumentando le possibilità che il **malware raggiunga un pubblico più ampio.**

Anche se questo non è un buon modello di business, i ricercatori ritengono che Stealc **rappresenti una minaccia non trascurabile**, poiché potrebbe essere adottato da criminali meno tecnici.

## Una dotazione ricca

**Stealc ha aggiunto nuove funzioni** dalla sua prima versione di gennaio, tra cui una funzione per randomizzare gli URL C2, un migliore sistema di ricerca e ordinamento dei registri (file rubati) e un’esclusione per le vittime in Ucraina.

![](https://www.securityinfo.it/wp-content/uploads/2023/02/Timeline-Stealc1.png)

La timeline di Stealc (Fonte: Sekoia)

**Sekoia ha analizzato un campione di Stealc** e ha scoperto che il malware ha una build leggera di soli 80 Kbyte, utilizza Dll legittime di terze parti, è scritto in C e abusa delle funzioni Api di Windows. La maggior parte delle sue stringhe sono offuscate con RC4 e base64, e il malware esfiltra automaticamente i dati rubati.

Stealc supporta 22 browser Web, 75 plug-in e 25 wallet; una volta distribuito, esegue controlli anti-analisi per garantire che non venga eseguito in un ambiente virtuale o sandbox. **Il malware raccoglie i dati dai browser, dalle estensioni e dalle app**, esegue un grabber di file personalizzato e infine esfiltra tutto verso il server C2.

Alla fine delle operazioni, **il malware rimuove sé stesso e i file Dll scaricati** dall’host compromesso per cancellare le tracce dell’infezione.

I ricercatori hanno identificato un metodo di distribuzione di Stealc tramite **video di YouTube che spiegano come installare software pirata**, collegandosi a un sito di download. Il malware è integrato nell’installer del software e, una volta eseguito, inizia a svolgere le sue funzioni e comunicare con il server C2.

Sekoia ha condiviso **indicatori di compromissione e regole** [Yara](https://github.com/SEKOIA-IO/Community/tree/main/IOCs/stealc/yara_rules) e [Suricata](https://github.com/SEKOIA-IO/Community/tree/main/IOCs/stealc/suricata_rules) per aiutare le aziende a difendersi. Si consiglia agli utenti di evitare l’installazione di software piratato e di scaricare solo dai siti ufficiali degli sviluppatori per ridurre il rischio di infezioni da malware.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [infostealer](https://www.securityinfo.it/tag/infostealer/), [Mars](https://www.securityinfo.it/tag/mars/), [Raccoon](https://www.securityinfo.it/tag/raccoon/), [Redline](https://www.securityinfo.it/tag/redline/), [Sekoia](https://www.securityinfo.it/tag/sekoia/), [Stealc](https://www.securityinfo.it/tag/stealc/), [Vidar](https://www.securityinfo.it/tag/vidar/)

[La maggior parte dei ransomware sfrutta vulnerabilità note da anni](https://www.securityinfo.it/2023/02/21/ransomware-vulnerabilita-note/)
[Un terzo dei malware integra oltre 20 tattiche di attacco](https://www.securityinfo.it/2023/02/21/il-malware-e-sempre-piu-multifunzione/)

---

![](https://secure.gravatar.com/avatar/9ba6108fae91c2be66a7ef45ac2db49a?s=90&d=mm&r=g)

##### [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/)

##### Articoli correlati

* [![Nuova variante del malware XCSSET prende di mira gli sviluppatori Xcode su macOS](https://www.securityinfo.it/wp-content/uploads/2025/09/MalwareCrypto-29-set-2025CG-120x85.png)](https://www.securityinfo.it/2025/09/26/nuova-variante-del-malware-xcsset-prende-di-mira-gli-sviluppatori-xcode-su-macos/ "Nuova variante del malware XCSSET prende di mira gli sviluppator...