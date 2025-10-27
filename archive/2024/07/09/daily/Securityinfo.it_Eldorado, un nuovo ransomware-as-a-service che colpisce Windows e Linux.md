---
title: Eldorado, un nuovo ransomware-as-a-service che colpisce Windows e Linux
url: https://www.securityinfo.it/2024/07/08/eldorado-un-nuovo-ransomware-as-a-service-che-colpisce-windows-e-linux/?utm_source=rss&utm_medium=rss&utm_campaign=eldorado-un-nuovo-ransomware-as-a-service-che-colpisce-windows-e-linux
source: Securityinfo.it
date: 2024-07-09
fetch_date: 2025-10-06T17:53:09.692029
---

# Eldorado, un nuovo ransomware-as-a-service che colpisce Windows e Linux

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

## Eldorado, un nuovo ransomware-as-a-service che colpisce Windows e Linux

Lug 08, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [Hacking](https://www.securityinfo.it/category/news/hacking-news/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Malware](https://www.securityinfo.it/category/news/malware-news/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2024/07/08/eldorado-un-nuovo-ransomware-as-a-service-che-colpisce-windows-e-linux/#respond)

---

I ricercatori di Group-IB [hanno scoperto](https://www.group-ib.com/blog/eldorado-ransomware/) **Eldorado**, un **ransomware-as-a-service** presente da marzo in grado di **cifrare file sui sistemi Windows e Linux.**

Il servizio è stato pubblicizzato su **RAMP**, uno dei forum di ransomware più noti e frequentati sul dark web. I ricercatori di Group-IB si sono infiltrati nel gruppo come pentesters e hanno scoperto che la gang era composta da individui russofoni.

![](https://www.securityinfo.it/wp-content/uploads/2024/07/ransomware-2321110_1920.jpg)

Pixabay

Eldorado usa Golang per abilitare l’operatività cross-platform, usa **Chacha20 per la cifratura dei file** e **RSA-OAEP per la cifratura delle chiavi**. Il ransomware è in grado di cifrare file su reti condivise usando il protocollo SMB e usa il nome della compagnia target, i dettagli della nota di riscatto e le credenziali di admin come parametri per ciascuna build del malware.

Dopo aver fatto richiesta di affiliazione al gruppo, gli attaccanti generano la build del ransomware specifica per l’affiliato sulla base dei parametri da lui specificati. **L’encryptor viene condiviso in quattro formati: esxi, esxi\_64, win e win\_64**. Insieme al malware viene fornito un manuale per l’uso che include, tra le altre cose, una serie di comandi e parametri da specificare per definire il perimetro della cifratura.

I file cifrati hanno estensione “.00000001” e durante il processo di cifratura viene loggato in console il progresso del ransomware. Al termine dell’operazione, il malware crea una nota di riscatto in .txt intitolata “HOW\_RETURN\_YOUR\_DATA” sia sul Desktop che nella cartella Documents con le istruzioni su come contattare l’affiliato dietro l’attacco. **Il testo della nota viene personalizzato in fase di build del ransomware.**

## L’impatto di Eldorado

Il ransomware, spiegano i ricercatori di sicurezza, non è basato sul codice sorgente di altri ransomware: **il gruppo ha creato il servizio da zero.** “*Sebbene sia relativamente nuovo e non sia un rebrand di gruppi di ransomware ben noti, **Eldorado ha dimostrato in breve tempo la sua capacità di infliggere danni significativi** ai dati, alla reputazione e alla continuità aziendale delle sue vittime*” si legge sul blog di Group-IB.

A giugno 2024 si contano **sedici compagnie appartenenti a diversi Paesi e di diversi settori vittime di Eldorado.** Tredici incidenti si sono verificati solo negli Stati Uniti, due in Italia e uno in Croazia. Il settore più colpito è quello dell’immobiliare (tre attacchi), seguito dall’educativo, dai servizi professionali, dal sanitario e dal manifatturiero, ognuno con due attacchi, e dalle telecomunicazioni, dai servizi per il business, dai servizi amministrativi, dai trasporti e dalle realtà governative e militari con un attacco ciascuno.

![Numero di attacchi di Eldorado per Paesi e industrie](https://www.securityinfo.it/wp-content/uploads/2024/07/Cattura.png)

Credits: Group-IB

Come sottolinea Group-IB, Eldorado è l’ennesima conferma che il panorama dei ransomware è in continua evoluzione e **sta mettendo a serio rischio la sicurezza delle aziende.**“*Il continuo sviluppo di nuovi ceppi di ransomware e l’emergere di sofisticati programmi di affiliazione dimostrano che la minaccia è lungi dall’essere contenuta. **Le organizzazioni devono rimanere vigili e proattive nei loro sforzi di cybersecurity per mitigare i rischi posti da queste minacce in continua evoluzione***” affermano i ricercatori.

Per rafforzare le difese, le imprese sono invitate a **implementare l’autenticazione multi-fattore** e scegliere soluzioni EDR per il monitoraggio degli endpoint e l’identificazione di attività sospette con approccio proattivo, permettendo ai team di sicurezza di agire non appena si presenta il problema.

In caso di successo degli attacchi, le aziende devono avere una **strategia di backup solida** che permetta di ripristinare in maniera efficiente i file cifrati, riducendo al minimo la perdita di dati.

Infine, non può mancare un processo di patching per mantenere i software aggiornati e ridurre il numero di vulnerabilità e la definizione di **programmi di training per i dipendenti**, aiutandoli a identificare attività sospette e tentativi di phishing.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [eldorado](https://www.securityinfo.it/tag/eldorado/), [Group-IB](https://www.securityinfo.it/tag/group-ib/), [Linux](https://www.securityinfo.it/tag/linux/), [Ransomware](https://www.securityinfo.it/tag/ransomware/), [ransomware-as-a-service](https://www.securityinfo.it/tag/ransomware-as-a-service/), [Windows](https://www.securityinfo.it/tag/windows/)

[L'importanza delle soluzioni MDR per la protezione aziendale](https://www.securityinfo.it/2024/07/08/limportanza-delle-soluzioni-mdr-per-la-protezione-aziendale/)
[Da ACN e DIE una campagna per diffondere la cultura di cybersecurity](https://www.securityinfo.it/2024/07/05/da-acn-e-die-una-campagna-per-diffondere-la-cultura-di-cybersecurity/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1...