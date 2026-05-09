---
title: Ecco il GitHub per fare di Claude un operatore OSINT avanzato
url: https://www.securityinfo.it/2026/05/08/ecco-il-github-per-fare-di-claude-un-operatore-osint-avanzato/?utm_source=rss&utm_medium=rss&utm_campaign=ecco-il-github-per-fare-di-claude-un-operatore-osint-avanzato
source: Securityinfo.it
date: 2026-05-08
fetch_date: 2026-05-09T05:08:58.954667
---

# Ecco il GitHub per fare di Claude un operatore OSINT avanzato

Aggiornamenti recenti Maggio 8th, 2026 12:03 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Ecco il GitHub per fare di Claude un operatore OSINT avanzato](https://www.securityinfo.it/2026/05/08/ecco-il-github-per-fare-di-claude-un-operatore-osint-avanzato/)
* [Un dipendente su otto considera accettabile vendere le credenziali](https://www.securityinfo.it/2026/05/07/un-dipendente-su-otto-considera-accettabile-vendere-le-credenziali/)
* [Quasar Linux RAT: malware che punta alla supply chain software](https://www.securityinfo.it/2026/05/06/quasar-linux-rat-malware-che-punta-alla-supply-chain-software/)
* [CISA avvisa: Copy Fail sfruttata per root sui sistemi Linux](https://www.securityinfo.it/2026/05/04/cisa-avvisa-copy-fail-sfruttata-per-root-sui-sistemi-linux/)
* [Mini Shai-Hulud: la supply chain SAP colpita da un simil-worm](https://www.securityinfo.it/2026/04/30/mini-shai-hulud-la-supply-chain-sap-colpita-da-un-simil-worm/)

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

## Ecco il GitHub per fare di Claude un operatore OSINT avanzato

Mag 08, 2026  [Redazione](https://www.securityinfo.it/author/redazione/ "Articoli scritti da Redazione")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Tecnologia](https://www.securityinfo.it/category/news/tecnologia-news/)
 [0](https://www.securityinfo.it/2026/05/08/ecco-il-github-per-fare-di-claude-un-operatore-osint-avanzato/#respond)

---

L’intelligenza artificiale sta, ovviamente e progressivamente, cambiando anche il modo in cui vengono condotte attività di reconnaissance, threat intelligence e analisi offensiva. Accanto ai tradizionali strumenti OSINT, stanno emergendo nuovi progetti che vanno oltre la pura automazione e puntano sulla capacità di guidare i Large Language Model attraverso metodologie operative strutturate. Uno degli esempi più interessanti è [Claude-OSINT](https://github.com/elementalsouls/Claude-OSINT), progetto pubblicato su GitHub dallo sviluppatore “ElementalSoul” e pensato per trasformare Claude Code in una piattaforma di supporto avanzata per analisti di sicurezza, red teamer e bug bounty hunter.

![](https://www.securityinfo.it/wp-content/uploads/2026/05/manifestazioneOsint-1024x683.png)

Il progetto non introduce un nuovo scanner o un motore di intelligence autonomo. La sua forza risiede invece nella capacità di **modificare il comportamento operativo del modello AI**, fornendogli workflow, metodologie investigative, tecniche di enumerazione e processi di analisi tipici di un professionista della sicurezza offensiva.

### **Un nuovo approccio all’OSINT basato sugli LLM**

A differenza dei framework OSINT tradizionali, **Claude-OSINT non si presenta come un insieme di utility standalone**. Il progetto sfrutta infatti il sistema di “skill” di Claude Code per estendere il contesto cognitivo del modello.

In pratica, il sistema inserisce all’interno dell’ambiente operativo di Claude una serie di istruzioni strutturate che **insegnano al modello come affrontare attività di reconnaissance**. Questo significa che Claude non si limita più a rispondere genericamente alle richieste dell’utente, ma inizia a seguire processi logici, sequenze investigative e metodologie di analisi coerenti con le pratiche del mondo offensive security.

Il repository contiene principalmente **due aree operative: osint-methodology e offensive-osint**. La prima definisce il modo in cui il modello deve ragionare durante la raccolta delle informazioni, mentre la seconda include template operativi, query, pattern regex, strategie di enumerazione e workflow tattici.

### **Uno strumento per risparmiare tempo in maniera sensata**

Per chi lavora nella cybersecurity offensiva, **la fase di reconnaissance rappresenta spesso una delle attività più lunghe e dispersive**. Identificare asset, correlare informazioni, individuare superfici di attacco e classificare le priorità richiede tempo e competenze avanzate.

Claude-OSINT prova a intervenire proprio su questo punto, aiutando il modello AI a **organizzare metodicamente le attività di raccolta delle informazioni**. Secondo la documentazione del progetto, il framework include decine di moduli dedicati all’asset discovery, numerosi pattern regex per l’identificazione di secret leakage e una vasta raccolta di query e dork utilizzabili durante le indagini OSINT.

L’obiettivo è trasformare Claude in una sorta di “copilota cognitivo” capace di **assistere il professionista nella costruzione di mappe relazionali**, nella ricerca di endpoint interessanti e nell’identificazione di possibili punti di esposizione.

### **Come funziona il sistema di skill**

Dal punto di vista tecnico, **Claude-OSINT si basa sul sistema di skill supportato da Claude Code**. Le skill sono file markdown strutturati, generalmente denominati SKILL.md, che vengono caricati all’interno dell’ambiente del modello per modificarne il comportamento operativo.

Questo significa che il framework non altera direttamente il modello AI, ma **agisce tramite prompt engineering avanzato e knowledge injection contestuale**. Una volta installate le skill, Claude acquisisce nuove capacità procedurali e metodologiche, imparando a seguire workflow specifici durante le attività di analisi.

Il progetto include **procedure per la gestione del tempo investigativo, classificazione degli asset, prioritizzazione delle attività, correlazione delle informazioni e costruzione di report operativi**. Sono presenti, inoltre, workflow dedicati all’enumerazione di domini, sottodomini, endpoint e possibili esposizioni di credenziali.

Dal punto di vista architetturale, questo approccio rappresenta un esempio molto interessante di “augmentation layer”: **invece di creare un nuovo motore AI**, il progetto costruisce uno strato specialistico sopra un modello generalista già esistente.

### **Installazione e avvio dell’ambiente**

Per **utilizzare Claude-OSINT** è necessario avere accesso a [Claude Code](https://code.claude.com), l’ambiente CLI sviluppato da [Anthropic](https://www.anthropic.com) per interagire con i modelli Claude.

L’installazione può essere eseguita tramite script ufficiali disponibili per Linux, macOS e Windows. Una volta configurato l’ambiente, **il repository GitHub va clonato localmente** e le directory contenenti le skill devono essere copiate nella cartella dedicata di Claude.

Dopo il caricamento delle skill, il modello può iniziare a utilizzare i workflow OSINT definiti dal framework. In pratica, **l’utente interagisce normalmente con Claude,** ma il comportamento del modello viene guidato dalle metodologie e dai processi introdotti dal progetto.

### **I limiti e i rischi di uno strumento del genere**

Gli stessi autori del progetto sottolineano come Claude-OSINT debba **essere utilizzato esclusivamente in contesti autorizzati** di red teaming, penetration testing...