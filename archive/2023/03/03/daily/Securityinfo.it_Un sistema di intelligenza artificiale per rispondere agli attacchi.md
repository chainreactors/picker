---
title: Un sistema di intelligenza artificiale per rispondere agli attacchi
url: https://www.securityinfo.it/2023/03/02/intelligenza-artificiale-attacchi-informatici/?utm_source=rss&utm_medium=rss&utm_campaign=intelligenza-artificiale-attacchi-informatici
source: Securityinfo.it
date: 2023-03-03
fetch_date: 2025-10-04T08:33:22.226928
---

# Un sistema di intelligenza artificiale per rispondere agli attacchi

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

## Un sistema di intelligenza artificiale per rispondere agli attacchi

Mar 02, 2023  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Attacchi](https://www.securityinfo.it/category/approfondimenti/attacchi/), [RSS](https://www.securityinfo.it/category/rss/), [Tecnologia](https://www.securityinfo.it/category/approfondimenti/tecnologia/)
 [0](https://www.securityinfo.it/2023/03/02/intelligenza-artificiale-attacchi-informatici/#respond)

---

I ricercatori del Dipartimento di Energia del Pacific Northwest National Laboratory (PNNL) hanno sviluppato **un sistema di intelligenza artificiale per la difesa dagli attacchi informatici.** Il team ha effettuato una serie di prove in un ambiente di simulazione, dove il sistema **è riuscito a bloccare il 95% degli attacchi**.

[Come riportato da Robert Lemos](https://www.darkreading.com/emerging-tech/researchers-create-ai-cyber-defender-that-reacts-to-attackers), **i ricercatori hanno simulato uno scenario di attacchi multi-stage**, in cui ognuno di essi aveva un livello di persistenza e abilità diversi. Il team ha utilizzato 15 delle tattiche descritte nel framework [MITRE ATT&CK](https://www.securityinfo.it/2022/07/21/mitre-engenuity-test-e-un-test-affidabile/), e ha seguito i 7 step della catena di attacco, dall’accesso iniziale alle fasi finali di impatto ed esfiltrazione dei dati.

![intelligenza artificiale attacchi](https://www.securityinfo.it/wp-content/uploads/2023/03/7970721_3820574-scaled.jpg)

Freepik

L’obiettivo del sistema era impedire agli attaccanti di raggiungere la fase finale della catena, altrimenti l’attacco sarebbe stato considerato concluso.

La simulazione prevedeva che il sistema fosse già compromesso, e che quindi la rete neurale dovesse individuare gli attacchi in atto e bloccarli. **Il risultato è stato raggiunto utilizzando il *reinforcement learning***, una tecnica di machine learning in cui la rete neurale rinforza o indebolisce i parametri del singolo neurone per raggiungere la soluzione migliore, basandosi su un punteggio ottenuto a ogni fase.

I ricercatori hanno individuato un metodo in particolare, i**l Deep Q Network**, che **è riuscito a individuare e bloccare un’alta percentuale degli attacchi**. Come [riportato nel paper](https://arxiv.org/pdf/2302.01595.pdf), l’obiettivo del sistema non era solo impedire agli attacchi di raggiungere la fase finale della catena, ma soprattutto di **bloccare la progressione il prima possibile**.

![intelligenza artificiale attacchi](https://www.securityinfo.it/wp-content/uploads/2023/03/8562956_25550-scaled.jpg)

abstract low poly connection lines digital technology background

Il team del PNNL ha dimostrato che **l’utilizzo di una rete neurale a supporto della cybersicurezza non è più un’utopia**, anche se c’è ancora molta strada da fare. Il sistema va ancora perfezionato e non può ancora operare in autonomia. **Una delle sfide principali riguarda l’interpretabilità dei risultati**, visto che la rete neurale al momento lavora come una black-box; inoltre, **il sistema potrebbe essere compromesso dagli attaccanti.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Deep Learning](https://www.securityinfo.it/tag/deep-learning/), [Intelligenza artificiale](https://www.securityinfo.it/tag/intelligenza-artificiale/), [MITRE framework](https://www.securityinfo.it/tag/mitre-framework/), [pnnl](https://www.securityinfo.it/tag/pnnl/), [reinforcement learning](https://www.securityinfo.it/tag/reinforcement-learning/), [rete neurale](https://www.securityinfo.it/tag/rete-neurale/)

[Il 91% delle librerie open source non è aggiornato](https://www.securityinfo.it/2023/03/02/il-91-delle-librerie-open-source-non-e-aggiornato/)
[Il 79% delle aziende italiane ha subito un attacco di phishing](https://www.securityinfo.it/2023/03/01/il-79-delle-aziende-italiane-ha-subito-un-attacco-di-phishing/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![L’IA diventa arma e vittima per il cybercrimine: il report di Crowdstrike](https://www.securityinfo.it/wp-content/uploads/2025/09/ai-generated-7992462_1920-120x85.jpg)](https://www.securityinfo.it/2025/09/12/l-ia-diventa-arma-e-vittima-per-il-cybercrimine-il-report-di-crowdstrike/ "L’IA diventa arma e vittima per il cybercrimine: il report di Crowdstrike")

  [L’IA diventa arma e vittima per...](https://www.securityinfo.it/2025/09/12/l-ia-diventa-arma-e-vittima-per-il-cybercrimine-il-report-di-crowdstrike/ "Permanent link to L’IA diventa arma e vittima per il cybercrimine: il report di Crowdstrike")

  Set 12, 2025  [0](https://www.securityinfo.it/2025/09/12/l-ia-diventa-arma-e-vittima-per-il-cybercrimine-il-report-di-crowdstrike/#respond)
* [![Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-6138007_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/ "Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA")

  [Report Acronis: il ransomware rimane la...](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/ "Permanent link to Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA")

  Set 11, 2025  [0](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/#respond)
* [![Hexstrike AI, nuovo tool di OffSec, è g...