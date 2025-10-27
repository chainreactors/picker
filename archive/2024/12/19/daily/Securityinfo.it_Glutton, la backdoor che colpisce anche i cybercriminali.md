---
title: Glutton, la backdoor che colpisce anche i cybercriminali
url: https://www.securityinfo.it/2024/12/18/glutton-la-backdoor-che-colpisce-anche-i-cybercriminali/?utm_source=rss&utm_medium=rss&utm_campaign=glutton-la-backdoor-che-colpisce-anche-i-cybercriminali
source: Securityinfo.it
date: 2024-12-19
fetch_date: 2025-10-06T19:48:19.068861
---

# Glutton, la backdoor che colpisce anche i cybercriminali

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

## Glutton, la backdoor che colpisce anche i cybercriminali

Dic 18, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2024/12/18/glutton-la-backdoor-che-colpisce-anche-i-cybercriminali/#respond)

---

I ricercatori della compagnia di sicurezza XLab [hanno scoperto](https://blog.xlab.qianxin.com/glutton_stealthily_targets_mainstream_php_frameworks-en/) **Glutton**, una **backdoor in PHP** che colpisce non solo aziende e organizzazioni, ma anche altri **cybercriminali**.

Il team di XLab ha individuato le prime attività della backdoor lo scorso aprile, scoprendo una serie di payload PHP malevoli altamente modulari, in grado di eseguire in maniera indipendente o integrandosi tra di loro. **“*Questa analisi ha portato alla scoperta di un’avanzata backdoor in PHP mai documentata prima che abbiamo chiamato*Glutton** *per via della sua capacità di infettare numerosi file PHP e innestare `l0ader_shell`*” spiegano i ricercatori.

La backdoor è in grado di **esfiltrare informazioni** quali la versione dell’OS e di PHP e i dati sensibili di Baota Panel. Glutton è inoltre in grado di installare una **backdoor di Winnti ELF-based** e altre backdoor in PHP, oltre che iniettare codice in framework PHP popolari come Baota, ThinkPHP, Yii e Laravel.

![Glutton](https://www.securityinfo.it/wp-content/uploads/2024/12/backdoor.png)

## Analisi di Glutton

La backdoor è composta da numerosi componenti che, come anticipato, **possono eseguire funzioni in autonomia o essere composte per creare un framework più complesso**. “*Questo design modulare non solo migliora l’adattabilità degli attacchi, ma lo rende anche più difficile da individuare e tacciare durante le attività di difesa*” spiega il team di XLab.

Secondo i ricercatori di sicurezza, per distribuire il framework gli attaccanti sfruttano vulnerabilità dei sistemi, password ottenute da tecniche di brute-force e sfruttando sistemi già compromessi dell’ambiente cybercriminale.

Uno dei moduli più importanti è `client_task`: esso è in grado di **eseguire una backdoor PHP** ed eseguire periodicamente la funzione `fetch_task` per ottenere ed eseguire altri payload. Il modulo **supporta 22 comandi diversi** che comprendono funzioni per l’upload e il download di file, per creare, leggere o modificare file e per scansionare le cartelle dei metadati.

Un altro modulo centrale è il task\_loader, la cui funzione primaria è di **scaricare ed eseguire il payload specifico in base alle caratteristiche del sistema**. A questo si aggiunge `init_task`, il modulo che scarica ed esegue la backdoor Winnti e infetta i pannelli Baota e i file PHP, e il `client_loader`, un modulo refattorizzato di `init_task`, il quale introduce la capacità di scaricare ed eseguire un client *backdoored*per la compatibilità cross-platform e l’evasione dei controlli degli antivirus.

![](https://www.securityinfo.it/wp-content/uploads/2024/10/hacking-3112539_1920-1.png)

## Una backdoor colpisce anche i cybercriminali

Le vittime di Glutton si trovano principalmente in Cina e negli Stati Uniti e appartengono a settori quali i servizi IT, le business operation e le organizzazioni per la sicurezza sociale.

Ciò che stupisce è che la backdoor **colpisce anche sistemi venduti nel mercato cybercriminale**, con l’obiettivo di trasformare gli altri attaccanti in “pedine” da usare per i loro scopi. Secondo XLab, il team dietro Glutton userebbe la backdoor per sfruttare i sistemi cybercriminali e ottenere ancora più informazioni.

Nel dettaglio, il gruppo inietta la backdoor nei software venduti sui forum cybercriminali, solitamente false piattaforme di scommesse o di scambio di criptovalute. Una volta infettati questi sistemi, Glutton esegue il tool “HackBrowserData” per **estrarre informazioni sensibili dai browser dei criminali stessi.**

Anche se XLab ha confermato la veridicità della backdoor Winnti usata da Glutton, **non è detto che il nuovo malware sia attribuibile al gruppo**: la nuova backdoor è implementata in maniera molto semplificata e i meccanismi di offuscamento non sono robusti come quelli usati dal gruppo. “*Mentre il meccanismo di distribuzione di Glutton è molto simile a quello del gruppo Winnti, manca di furtività e l’implementazione semplicistica introduce incertezza*” spiegano i ricercatori. **XLab attribuisce comunque con “moderata confidenza” il tool al gruppo cinese.**

Per eliminare possibili infezioni di Glutton, il team di XLab consiglia di analizzare i file PHP per verificare la presenza di `l0ader_shell`, rimuovere i processi malevoli individuati e rafforzare la protezione delle cartelle temporanee creando un file `.donot` in `/tmp` per prevenire l’exploit.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [backdoor](https://www.securityinfo.it/tag/backdoor/), [Glutton](https://www.securityinfo.it/tag/glutton/), [PHP](https://www.securityinfo.it/tag/php/)

[Operazione BadBox fermata in Germania grazie a una sinkhole](https://www.securityinfo.it/2024/12/18/operazione-badbox-fermata-in-germania-grazie-a-una-sinkhole/)
[ESET Threat Report: Formbook è leader tra gli infostealer](https://www.securityinfo.it/2024/12/17/eset-threat-report-formbook-e-leader-tra-gli-infostealer/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![MuddyWater si evolve: attacchi più sofisticati e infrastruttura più resiliente](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/17/muddywater-si-evolve-attacchi-piu-sofisticati-e-infrastruttura-piu-resiliente/ "MuddyWater si evo...