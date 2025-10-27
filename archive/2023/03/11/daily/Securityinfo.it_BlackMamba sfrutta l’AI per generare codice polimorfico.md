---
title: BlackMamba sfrutta l’AI per generare codice polimorfico
url: https://www.securityinfo.it/2023/03/10/blackmamba-sfrutta-lai-per-generare-codice-polimorfico/?utm_source=rss&utm_medium=rss&utm_campaign=blackmamba-sfrutta-lai-per-generare-codice-polimorfico
source: Securityinfo.it
date: 2023-03-11
fetch_date: 2025-10-04T09:18:15.048775
---

# BlackMamba sfrutta l’AI per generare codice polimorfico

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

## BlackMamba sfrutta l’AI per generare codice polimorfico

Mar 10, 2023  [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/ "Articoli scritti da Dario Orlandi")
 [Concept](https://www.securityinfo.it/category/minacce-2/concept/), [Keylogger](https://www.securityinfo.it/category/minacce-2/keylogger/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [Minacce](https://www.securityinfo.it/category/minacce-2/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2023/03/10/blackmamba-sfrutta-lai-per-generare-codice-polimorfico/#respond)

---

I ricercatori di [HYAS Labs](https://www.hyas.com/) hanno dimostrato un attacco proof-of-concept, che hanno denominato BlackMamba, che sfrutta un **modello di linguaggio di grandi dimensioni** (LLM) per sintetizzare al volo una funzione di keylogger polimorfico.

L’attacco è veramente polimorfico poiché ogni volta che BlackMamba viene eseguito, **risintetizza la sua funzione di keylogging**, come hanno spiegato i ricercatori [in un articolo](https://www.hyas.com/blog/blackmamba-using-ai-to-generate-polymorphic-malware) pubblicato sul sito dell’azienda.

BlackMamba dimostra come **l’intelligenza artificiale possa aiutare il malware** a modificare un codice innocuo in fase di esecuzione senza la necessità di un’infrastruttura di comando e controllo, rendendo difficile la sua rilevazione da parte dei sistemi di sicurezza automatizzati.

I ricercatori di HYAS Labs hanno **testato l’attacco contro un sistema di rilevamento e risposta** degli endpoint (EDR) leader del settore, senza ricevere alcun avviso o rilevamento.

![](https://www.securityinfo.it/wp-content/uploads/2023/03/black_mamba_3-transformed.png)

## Esfiltrazione via Teams

BlackMamba utilizza la sua capacità di keylogging integrata per raccogliere informazioni sensibili, inclusi nomi utente, password e numeri di carte di credito, e poi **utilizza Microsoft Teams per inviare i dati raccolti** a un canale Teams dannoso.

MS Teams è uno strumento di comunicazione e collaborazione legittimo ampiamente utilizzato dalle organizzazioni, quindi gli autori di malware possono sfruttarlo per **aggirare le difese di sicurezza tradizionali**, come firewall e sistemi di rilevamento delle intrusioni.

Inoltre, poiché i dati vengono inviati su canali crittografati, **può essere difficile rilevare che un canale viene utilizzato per l’esfiltrazione**.

Il sistema di delivery di BlackMamba **si basa su un pacchetto Python open source**, il che consente agli sviluppatori di convertire gli script Python in file eseguibili autonomi che possono essere eseguiti su varie piattaforme, tra cui Windows, macOS e Linux.

Gli autori del proof-of-concept hanno commentato: “Le minacce poste da questa nuova generazione di malware sono molto reali. Eliminando la comunicazione C2 e generando nuovo codice univoco in fase di esecuzione, malware come **BlackMamba è praticamente non rilevabile dalle soluzioni di sicurezza predittiva attuali**”.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [BlackMamba](https://www.securityinfo.it/tag/blackmamba/), [IA](https://www.securityinfo.it/tag/ia/), [Intelligenza artificiale](https://www.securityinfo.it/tag/intelligenza-artificiale/), [keylogger](https://www.securityinfo.it/tag/keylogger/), [proof-of-concept](https://www.securityinfo.it/tag/proof-of-concept/), [Python](https://www.securityinfo.it/tag/python/), [Teams](https://www.securityinfo.it/tag/teams/)

[Il cybercrimine annulla le differenze di genere](https://www.securityinfo.it/2023/03/13/cybercrimine-genere-security/)
[Molti servizi cloud non consentono analisi forensi complete](https://www.securityinfo.it/2023/03/10/molti-servizi-cloud-non-consentono-attivita-forensi-complete/)

---

![](https://secure.gravatar.com/avatar/9ba6108fae91c2be66a7ef45ac2db49a?s=90&d=mm&r=g)

##### [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/)

##### Articoli correlati

* [![L’IA diventa arma e vittima per il cybercrimine: il report di Crowdstrike](https://www.securityinfo.it/wp-content/uploads/2025/09/ai-generated-7992462_1920-120x85.jpg)](https://www.securityinfo.it/2025/09/12/l-ia-diventa-arma-e-vittima-per-il-cybercrimine-il-report-di-crowdstrike/ "L’IA diventa arma e vittima per il cybercrimine: il report di Crowdstrike")

  [L’IA diventa arma e vittima per...](https://www.securityinfo.it/2025/09/12/l-ia-diventa-arma-e-vittima-per-il-cybercrimine-il-report-di-crowdstrike/ "Permanent link to L’IA diventa arma e vittima per il cybercrimine: il report di Crowdstrike")

  Set 12, 2025  [0](https://www.securityinfo.it/2025/09/12/l-ia-diventa-arma-e-vittima-per-il-cybercrimine-il-report-di-crowdstrike/#respond)
* [![Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-6138007_1920-2-120x85.jpg)](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/ "Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA")

  [Report Acronis: il ransomware rimane la...](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/ "Permanent link to Report Acronis: il ransomware rimane la minaccia principale grazie a phishing basato su IA")

  Set 11, 2025  [0](https://www.securityinfo.it/2025/09/11/report-acronis-il-ransomware-rimane-la-minaccia-principale-grazie-a-phishing-basato-su-ia/#respond)
* [![Hexstrike AI, nuovo tool di OffSec, è già stato preso di mira dal cybercrimine](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_amcol3amcol3amco-120x85.png)](https://www.security...