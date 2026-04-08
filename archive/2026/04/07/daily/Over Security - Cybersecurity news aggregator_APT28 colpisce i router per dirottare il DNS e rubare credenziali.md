---
title: APT28 colpisce i router per dirottare il DNS e rubare credenziali
url: https://www.securityinfo.it/2026/04/07/apt28-colpisce-i-router-per-dirottare-il-dns-e-rubare-credenziali/
source: Over Security - Cybersecurity news aggregator
date: 2026-04-07
fetch_date: 2026-04-08T04:38:49.165270
---

# APT28 colpisce i router per dirottare il DNS e rubare credenziali

Aggiornamenti recenti Aprile 7th, 2026 2:30 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [APT28 colpisce i router per dirottare il DNS e rubare credenziali](https://www.securityinfo.it/2026/04/07/apt28-colpisce-i-router-per-dirottare-il-dns-e-rubare-credenziali/)
* [Strategia cybersecurity USA verso un modello più assertivo e industriale](https://www.securityinfo.it/2026/04/03/strategia-cybersecurity-usa-verso-un-modello-piu-assertivo-e-industriale/)
* [Proxy residenziali: quando la reputazione degli IP smette di funzionare](https://www.securityinfo.it/2026/04/02/proxy-residenziali-quando-la-reputazione-degli-ip-smette-di-funzionare/)
* [Vertex AI e il rischio dei “double agent” AI](https://www.securityinfo.it/2026/04/01/vertex-ai-e-il-rischio-dei-double-agent-ai/)
* [Vibecoding: l’AI accelera lo sviluppo ma moltiplica i rischi](https://www.securityinfo.it/2026/03/31/vibecoding-lai-accelera-lo-sviluppo-ma-moltiplica-i-rischi/)

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

## APT28 colpisce i router per dirottare il DNS e rubare credenziali

Apr 07, 2026  [Redazione](https://www.securityinfo.it/author/redazione/ "Articoli scritti da Redazione")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2026/04/07/apt28-colpisce-i-router-per-dirottare-il-dns-e-rubare-credenziali/#respond)

---

Secondo un’analisi pubblicata dal National Cyber Security Centre britannico e supportata da dati di Microsoft Threat Intelligence, **il gruppo APT28 continua a compromettere router domestici e per piccoli uffici per manipolare il DNS e intercettare credenziali sensibili**, utilizzando infrastrutture di rete apparentemente innocue come trampolino verso obiettivi più rilevanti. La campagna, attribuita al collettivo noto come **Fancy Bear** e legato all’intelligence militare russa GRU, ci ricorda come anche i dispositivi di rete periferici possano diventare elementi strategici per operazioni di cyber-spionaggio su larga scala.

![](https://www.securityinfo.it/wp-content/uploads/2026/04/Diverted-1024x529.png)

### **Hijacking DNS sui router SOHO: il vettore invisibile**

Il cuore dell’operazione consiste nello sfruttamento di vulnerabilità nei router small office e domestici, modificando i parametri DNS per reindirizzare il traffico verso infrastrutture controllate dagli attaccanti. **La compromissione del router trasforma ogni dispositivo collegato in un potenziale bersaglio, ereditando automaticamente le configurazioni malevole**, inclusi laptop, smartphone e sistemi aziendali remoti.

Quando le vittime cercano servizi diffusi come Outlook o altre piattaforme enterprise, vengono indirizzate verso pagine clone perfettamente credibili. **L’inserimento delle credenziali su questi portali falsificati consente ad APT28 di raccogliere password legittime senza compromettere direttamente l’infrastruttura target**, mantenendo l’operazione estremamente difficile da rilevare.

### **Router consumer come punto di ingresso verso ambienti enterprise**

Le attività osservate indicano che gli attacchi non sono necessariamente mirati a singoli individui di alto valore, ma piuttosto opportunistici. Tuttavia, **la compromissione di router posizionati “a monte” di organizzazioni rilevanti consente al gruppo di ottenere accesso indiretto a reti aziendali e dati sensibili**, sfruttando connessioni fidate e traffico apparentemente legittimo.

Microsoft Threat Intelligence ha identificato **oltre 200 organizzazioni e circa 5.000 dispositivi coinvolti** nell’infrastruttura DNS malevola attribuita a Forest Blizzard, denominazione interna di APT28: evidentemente **un’operazione distribuita su larga scala che utilizza l’ecosistema domestico come infrastruttura di raccolta credenziali**, senza indicazioni di compromissione diretta dei servizi Microsoft.

### **Dispositivi coinvolti e persistenza della campagna**

Tra i dispositivi citati compaiono diversi router TP-Link, mentre attività analoghe avevano già coinvolto apparati Cisco monitorati dal 2021. Un cluster separato ha interessato router MikroTik, molti dei quali localizzati in Ucraina. **Il controllo di questi dispositivi può fornire intelligence operativa, inclusi pattern di traffico e accesso a sistemi con valore militare o strategico**, ampliando l’impatto oltre il semplice credential harvesting.

La manipolazione DNS non è l’unico obiettivo. Secondo Microsoft, gli accessi ottenuti possono essere riutilizzati per ulteriori operazioni, inclusi attacchi DDoS o distribuzione di malware. **La trasformazione dei router compromessi in nodi multiuso rende l’infrastruttura resiliente e riutilizzabile per campagne successive**, aumentando la durata operativa dell’attacco.

### **Precedenti operazioni e malware Jaguar Tooth**

Le campagne attuali si inseriscono in un pattern già osservato negli anni precedenti. In advisory pubblicate nel 2023, il NCSC (**National Cyber Security Centre**, l’agenzia governativa del Regno Unito responsabile della sicurezza informatica nazionale) aveva documentato attacchi simili contro router Cisco utilizzati per distribuire il malware Jaguar Tooth. **Questo payload permetteva l’installazione di backdoor persistenti, facilitando compromissioni successive e accessi laterali**, dimostrando l’evoluzione da semplice DNS hijacking a piattaforme di intrusione più sofisticate.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [APT28](https://www.securityinfo.it/tag/apt28/), [Cisco router](https://www.securityinfo.it/tag/cisco-router/), [compromissione router domestici](https://www.securityinfo.it/tag/compromissione-router-domestici/), [cyber spionaggio russo](https://www.securityinfo.it/tag/cyber-spionaggio-russo/), [DNS hijacking](https://www.securityinfo.it/tag/dns-hijacking/), [Fancy Bear](https://www.securityinfo.it/tag/fancy-bear/), [Forest Blizzard](https://www.securityinfo.it/tag/forest-blizzard/), [Jaguar Tooth malware](https://www.securityinfo.it/tag/jaguar-tooth-malware/), [Microsoft Threat Intelligence](https://www.securityinfo.it/tag/microsoft-threat-intelligence/), [MikroTik](https://www.securityinfo.it/tag/mikrotik/), [ncsc](https://www.securityinfo.it/tag/ncsc/), [phishing infrastrutturale](https://www.securityinfo.it/tag/phishing-infrastrutturale/), [router compromise](https://www.securityinfo.it/tag/router-compromise/), [router SOHO](https://www.securityinfo.it/tag/router-soho/), [sicurezza DNS](https://www.securityinfo.it/tag/sicurezza-dns/), [TP-Link](https://www.securityinfo.it/tag/tp-link/)

[Strategia cybersecurity USA verso un modello più assertivo e industriale](https://www.securityinfo.it/2026/04/03/strategia-cybersecurity-usa-verso-un-modello-piu-assertivo-e-industriale/)

---

![](https://secure.gravatar.com/avatar/57d6369d65bf9ebecae...