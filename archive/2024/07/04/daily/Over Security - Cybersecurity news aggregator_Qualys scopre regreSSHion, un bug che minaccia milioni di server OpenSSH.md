---
title: Qualys scopre regreSSHion, un bug che minaccia milioni di server OpenSSH
url: https://www.securityinfo.it/2024/07/03/qualys-scopre-regresshion-un-bug-che-minaccia-milioni-di-server-openssh/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-04
fetch_date: 2025-10-06T17:45:45.851512
---

# Qualys scopre regreSSHion, un bug che minaccia milioni di server OpenSSH

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

## Qualys scopre regreSSHion, un bug che minaccia milioni di server OpenSSH

Lug 03, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2024/07/03/qualys-scopre-regresshion-un-bug-che-minaccia-milioni-di-server-openssh/#respond)

---

Il team di sicurezza Qualys, fornitore di soluzioni di sicurezza cloud, [ha scoperto](https://blog.qualys.com/vulnerabilities-threat-research/2024/07/01/regresshion-remote-unauthenticated-code-execution-vulnerability-in-openssh-server) una **vulnerabilità ad alta criticità che colpisce OpenSSH**. Il bug, soprannominato “**regreSSHion**“, consente a un attaccante non autenticato di **eseguire codice remoto nel server OpenSSH nei sistemi Linux basato su glibc.**

Il nome della vulnerabilità deriva dal fatto che si tratta di una **regressione di un bug già patchato**, il CVE-2006-5051, risolta nel 2006. Stando al team di ricercatori di Qualys, la regressione è stata introdotta a ottobre 2020 con la versione 8.5p1 di OpenSSH ed è **rimasta inosservata per quattro anni.**

![regreSSHion](https://www.securityinfo.it/wp-content/uploads/2024/07/background-1900329_1920.jpg)

Pixabay

OpenSSH è una suite di utility di sicurezza di rete basate sul protocollo SSH che viene usato come standard su molti sistemi Unix-like, inclusi macOS e Linux. Come spiegano i ricercatori di Qualys, **OpenSSH è un tool critico per abilitare comunicazioni sicure su reti insicure** ed è particolarmente apprezzato per la sua capacità di scalare facilmente anche su reti enterprise, di implementare controlli di accesso robusti e di rendere sicuri processi automatizzati su diversi ambienti.

Se sfruttata, questa vulnerabilità può consentire a un attaccante di **compromettere l’intero sistema target ed eseguire comandi arbitrari coi massimi privilegi**; ciò porta a un controllo completo del sistema, con la possibilità di installare malware, di accedere ai e manipolare i dati sensibili e di creare backdoor per ottenere accesso persistente. Oltre a questo, l’exploit facilita lo spostamento laterale nella rete.

Ottenere i privilegi di root consente inoltre a un attaccante di bypassare meccanismi di sicurezza  come firewall, sistemi di logging e di individuazione degli accessi per nascondere le proprie attività.

I ricercatori di Qualys spiegano che il bug non è semplice da sfruttare perché è dovuto a una race condition che consente a più processi di accedere e manipolare le risorse condivise senza controllo. **Per eseguire correttamente l’exploit sono necessari più tentativi** ma, evidenzia il team, i nuovi progressi nel campo del deep learning potrebbero aumentare notevolmente il tasso di successo e fornire un enorme vantaggio agli attaccanti.

I ricercatori hanno identificato **più di 14 milioni di istanze server OpenSSH potenzialmente vulnerabili** ed esposte a Internet, con più di 700.000 mila istanze sicuramente vulnerabili.

![](https://www.securityinfo.it/wp-content/uploads/2024/06/hacker-6512174_1920.jpg)

“*Qualys ha sviluppato un exploit funzionante per la vulnerabilità regreSSHion. Nell’ambito del processo di divulgazione, abbiamo dimostrato con successo l’exploit al team OpenSSH per aiutarlo a comprendere e a porre rimedio alla situazione. **Non rilasciamo i nostri exploit, perché dobbiamo lasciare il tempo necessario per l’applicazione delle patch***” hanno spiegato i ricercatori, sottolineando però che altri team sarebbero in grado di replicare i loro risultati.

Per proteggersi da regreSSHion, i ricercatori invitano gli amministratori di rete ad **applicare il prima possibile le patch di OpenSSH**, installando versioni non vulnerabili; è necessario inoltre limitare gli accessi SSH, segmentare la rete e implementare soluzioni per il monitoraggio delle attività.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Linux](https://www.securityinfo.it/tag/linux/), [OpenSSH](https://www.securityinfo.it/tag/openssh/), [Qualys](https://www.securityinfo.it/tag/qualys/), [race condition](https://www.securityinfo.it/tag/race-condition/), [regreSSHion](https://www.securityinfo.it/tag/regresshion/), [regressione](https://www.securityinfo.it/tag/regressione/)

[Cisco risolve una vulnerabilità zero-day sfruttata da Velvet Ant](https://www.securityinfo.it/2024/07/03/cisco-risolve-una-vulnerabilita-zero-day-sfruttata-da-velvet-ant/)
[Le imprese migliorano le difese per accedere alle cyberassicurazioni](https://www.securityinfo.it/2024/07/02/le-imprese-migliorano-le-difese-per-accedere-alle-cyberassicurazioni/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![File Linux usati per furto di dati e spionaggio: la campagna di APT36](https://www.securityinfo.it/wp-content/uploads/2025/08/cyber-security-4785679_1920-120x85.png)](https://www.securityinfo.it/2025/08/25/file-linux-usati-per-furto-di-dati-e-spionaggio-la-campagna-di-apt36/ "File Linux usati per furto di dati e spionaggio: la campagna di APT36")

  [File Linux usati per furto di dati e...](https://www.securityinfo.it/2025/08/25/file-linux-usati-per-furto-di-dati-e-spionaggio-la-campagna-di-apt36/ "Permanent link to File Linux usati per furto di dati e spionaggio: la campagna di APT36")

  Ago 25, 2025  [0](https://www.securityinfo.it/2025/08/25/file-linux-usati-per-furto-di-dati-e-spionaggio-la-campagna-di-apt36/#respond)
* [![Due bug LPE consentono di ottenere i privilegi di root su Linux](https://www.se...