---
title: Gli LLM non riescono (ancora) a sfruttare le vulnerabilità in autonomia
url: https://www.securityinfo.it/2024/05/03/gli-llm-non-riescono-ancora-a-sfruttare-le-vulnerabilita-in-autonomia/
source: Over Security - Cybersecurity news aggregator
date: 2024-05-04
fetch_date: 2025-10-06T17:17:03.049918
---

# Gli LLM non riescono (ancora) a sfruttare le vulnerabilità in autonomia

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

## Gli LLM non riescono (ancora) a sfruttare le vulnerabilità in autonomia

Mag 03, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Hacking](https://www.securityinfo.it/category/approfondimenti/hacking/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [Scenario](https://www.securityinfo.it/category/approfondimenti/scenario/)
 [0](https://www.securityinfo.it/2024/05/03/gli-llm-non-riescono-ancora-a-sfruttare-le-vulnerabilita-in-autonomia/#respond)

---

Sempre più spesso si discute delle crescenti capacità degli modelli di IA e dei rischi che derivano da usi scorretti, anche in ambito cybersecurity. Molti ricercatori di sicurezza si chiedono **fino a che punto gli LLM possono supportare le attività del cybercrimine**, per esempio creando campagne malware su larga scala o sfruttando vulnerabilità in autonomia, senza l’intervento umano.

Secondo [Chris Rohlf](https://struct.github.io/auto_agents_1_day.html), ricercatore di sicurezza, i modelli di IA non sono ancora in grado di scoprire e generare nuovi exploit per le vulnerabilità note dei sistemi in completa autonomia, ma solo di **sfruttare la conoscenza esistente per automatizzare il processo.**

Per illustrare la sua posizione, Rohlf analizza un paper in cui i ricercatori dimostrano come **un LLM sia stato capace di sfruttare quasi tutte le CVE usate nel test;** nel dettaglio, il gruppo ha sviluppato costruito un agente in grado di interfacciarsi con GPT-4 e altri modelli e ha testato le sue capacità di exploit con una lista di **15 vulnerabilità note.** Le CVE sono tutte presenti in software open source, citate molti altri paper accademici e, cosa più importante, sono state scoperte dopo il cut-off di conoscenza di GPT-4 per valutare se effettivamente l’agente stava “ragionando” sulla vulnerabilità e non semplicemente usando le informazioni che aveva già a disposizione.

Il test dei ricercatori ha dimostrato che **GPT-4 è riuscito a sfruttare l’87% delle vulnerabilità** semplicemente avendo accesso alla sua descrizione; in assenza di essa, il tasso di successo è sceso al 7%; al contrario, gli altri modelli non sono riusciti a sfruttare alcun bug pur avendo accesso alle stesse informazioni di GPT-4.

Visti i risultati, gli autori del paper concludono che il modello ha dimostrato la **capacità emergente di sfruttare autonomamente vulnerabilità** 1-day reali. Secondo Rohlf, però, si tratta di una **conclusione affrettata che non riflette le reali abilità degli LLM.**

![](https://www.securityinfo.it/wp-content/uploads/2024/04/artificial-intelligence-4469138_1920-1.jpg)

Pixabay

## Gli LLM non sono così bravi a sfruttare le vulnerabilità

Il ricercatore evidenzia innanzitutto che gli autori del paper non hanno rilasciato né i prompt utilizzati, né il codice dell’agente, né gli output del modello per evitare rischi di sicurezza, e ciò rende il loro **processo poco trasparente e difficile da approfondire.**

Rohlf spiega inoltre che l’agente illustrato nel paper presenta un modulo capace di effettuare ricerche sul web, di fatto in grado di trovare tutte le informazioni tecniche per sfruttare le CVE note. **Gli exploit delle vulnerabilità sono semplici da reperire e da eseguire**, composti solo da qualche linea di codice, e sono accessibili direttamente dal National Vulnerability Database. “In molti casi il link NVD è il primo risultato di ricerca su Google” afferma Rohlf.

L’agente basato su LLM non ha quindi dimostrato capacità innovative di ragionamento, ma ha semplicemente **usato le abilità che aveva per effettuare ricerche sul web ed eseguire gli exploit esistenti delle vulnerabilità;** nulla che un qualsiasi agente con moduli di web scraping non possa fare.

“La mia conclusione è che questa ricerca sta dimostrando la **capacità di GPT-4 di essere utilizzato come scanner e crawler intelligente** che si basa ancora su alcuni approcci di forza bruta anche una volta ottenuti i giusti passaggi di sfruttamento, e non una capacità emergente di cybersecurity” spiega Rohlf.

Si tratta di un caso d’uso legittimo e che può effettivamente velocizzare l’esecuzione di exploit, ma in questo caso **non si può parlare di “hacking autonomo” o di generazione automatica di exploit.** GPT-4 non sta scoprendo nuove vulnerabilità né sta generando nuove modalità di sfruttamento, ma sta semplicemente raccogliendo le informazioni già disponibili sul web per fornirle all’utente.

“La pubblicazione di ricerche di questo tipo, senza i dati a sostegno delle affermazioni, **può rafforzare la falsa idea che i modelli di IA siano pericolosi per la sicurezza informatica e debbano essere controllati.** Questo non è vero per lo stato dell’arte attuale dei modelli” afferma Rohlf.

Pur non trattandosi di una nuova capacità degli LLM, vale comunque la pena sottolineare che **questi chatbot hanno la reale capacità di velocizzare i processi manuali** e facilitare l’esecuzione di exploit anche a chi non ha conoscenze tecniche. D’altra parte, l’accesso a un grande volume di informazioni in poco tempo è un vantaggio significativo anche per chi si occupa della difesa dei sistemi.

**Gli LLM hanno un enorme potenziale di migliorare la cybersecurity** più di quanto non possa supportare il cybercrimine, ma, sostiene Rohlf, c’è ancora un grosso gap tra gli esperti di intelligenza artificiale e cybersecurity; di conseguenza, l’impressione è di combattere contro una minaccia molto più grossa di ciò che è in realtà.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [CVE](https://www.securityinfo.it/tag/cve/), [cybersecurity](https://www.securityinfo.it/tag/cybersecurity/), [GPT-4](https://www.securityinfo.it/tag/gpt...