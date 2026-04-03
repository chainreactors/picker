---
title: Vertex AI e il rischio dei “double agent” AI
url: https://www.securityinfo.it/2026/04/01/vertex-ai-e-il-rischio-dei-double-agent-ai/
source: Over Security - Cybersecurity news aggregator
date: 2026-04-02
fetch_date: 2026-04-03T04:29:16.224252
---

# Vertex AI e il rischio dei “double agent” AI

Aggiornamenti recenti Aprile 2nd, 2026 4:00 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Proxy residenziali: quando la reputazione degli IP smette di funzionare](https://www.securityinfo.it/2026/04/02/proxy-residenziali-quando-la-reputazione-degli-ip-smette-di-funzionare/)
* [Vertex AI e il rischio dei “double agent” AI](https://www.securityinfo.it/2026/04/01/vertex-ai-e-il-rischio-dei-double-agent-ai/)
* [Vibecoding: l’AI accelera lo sviluppo ma moltiplica i rischi](https://www.securityinfo.it/2026/03/31/vibecoding-lai-accelera-lo-sviluppo-ma-moltiplica-i-rischi/)
* [Google: crittografia post-quantum entro il 2029](https://www.securityinfo.it/2026/03/27/google-crittografia-post-quantum-entro-il-2029-e-novita-sullautenticazione/)
* [Magento sotto attacco: PolyShell, sfruttamento di massa in pochi giorni](https://www.securityinfo.it/2026/03/25/magento-sotto-attacco-polyshell-sfruttamento-di-massa-in-pochi-giorni/)

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

## Vertex AI e il rischio dei “double agent” AI

Apr 01, 2026  [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo_security/ "Articoli scritti da Giancarlo Calzetta")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Tecnologia](https://www.securityinfo.it/category/approfondimenti/tecnologia/), [Tecnologia](https://www.securityinfo.it/category/news/tecnologia-news/)
 [0](https://www.securityinfo.it/2026/04/01/vertex-ai-e-il-rischio-dei-double-agent-ai/#respond)

---

Un [recente studio della Unit 42 di Palo Alto](https://unit42.paloaltonetworks.com/double-agents-vertex-ai/) ha messo in luce un aspetto ancora poco esplorato della sicurezza dei sistemi basati su agenti AI: **la possibilità che un agente distribuito in ambienti enterprise possa trasformarsi in un “doppiogiochista” (un  double agent) capace di compromettere l’intera infrastruttura cloud**. L’analisi si concentra sulla piattaforma Vertex AI di Google Cloud, evidenziando come configurazioni permissive e modelli di accesso predefiniti possano essere sfruttati per escalation di privilegi, esfiltrazione di dati e accesso a risorse interne sensibili.

![](https://www.securityinfo.it/wp-content/uploads/2026/04/Doppiogiochista-1024x683.png)

Il punto centrale è che **un agente AI compromesso non agisce come un attaccante esterno, ma come un insider con privilegi legittimi**, ampliando enormemente il potenziale impatto di una violazione. In ambienti come Google Cloud Vertex AI, dove gli agenti possono orchestrare servizi e interagire con risorse distribuite, questo scenario diventa particolarmente critico.

### **Permessi eccessivi e abuso dei Service Agent**

L’analisi tecnica ha evidenziato come il modello di autorizzazione di Vertex AI possa esporre a rischi significativi. In particolare, il Per-Project, Per-Product Service Agent (P4SA) associato agli agenti AI presenta, in configurazioni predefinite, privilegi eccessivamente ampi.

Attraverso un agente malevolo, i ricercatori sono riusciti a estrarre credenziali di servizio direttamente dal metadata endpoint interno di Google Cloud. Il risultato è che **l’agente può impersonare identità privilegiate e operare con accessi estesi su risorse cloud**, violando il principio del least privilege. Questa condizione consente di ottenere accesso completo in lettura ai bucket di Google Cloud Storage, includendo permessi come storage.buckets.list e storage.objects.get.

### **Dal progetto cliente all’infrastruttura Google: escalation inattesa**

Uno degli aspetti più rilevanti della ricerca riguarda **il passaggio dal contesto cliente al contesto “producer”**, ovvero l’infrastruttura gestita da Google stessa.

Utilizzando le credenziali sottratte, è stato possibile accedere a repository privati di Artifact Registry contenenti immagini container interne, tra cui componenti del Reasoning Engine. Questo implica che **un attaccante può ottenere accesso a codice proprietario e dettagli implementativi della piattaforma stessa**, con implicazioni dirette sulla sicurezza della supply chain. L’accesso non era disponibile per identità standard, **ma risultava abilitato per il service agent compromesso**, dimostrando una separazione dei privilegi non allineata ai principi di sicurezza più rigorosi.

### **Artifact Registry e visibilità sulla supply chain interna**

Un ulteriore livello di rischio emerge dalla possibilità di enumerare repository e pacchetti all’interno dell’Artifact Registry. La configurazione osservata ha consentito di scoprire immagini e componenti non documentati, offrendo una visibilità anomala sulla supply chain software interna. Questo significa che **un attaccante potrebbe mappare l’infrastruttura applicativa, individuare componenti vulnerabili e pianificare attacchi mirati**, anche senza accesso diretto ai contenuti.

Si tratta di un classico scenario di information disclosure che, in ambienti AI-driven, assume una portata molto più ampia.

### **Tenant project e esposizione di asset sensibili**

Durante il deployment di un agente, Vertex AI utilizza tenant project gestiti da Google. Anche in questo caso, le credenziali compromesse hanno permesso accesso a bucket contenenti artefatti sensibili.

Tra questi figurano file come Dockerfile.zip, requirements.txt e soprattutto code.pkl. Quest’ultimo introduce un rischio particolarmente critico: la serializzazione tramite pickle. È noto, infatti, che **la deserializzazione di oggetti pickle provenienti da fonti non affidabili può portare a remote code execution**, trasformando l’agente in un punto di persistenza per attacchi avanzati.

### **OAuth scope e rischio di espansione verso Google Workspace**

Un elemento strutturale emerso riguarda la configurazione degli OAuth scope associati agli agenti. Gli scope assegnati includono **accessi a servizi come Gmail, Drive e Calendar**. Anche se l’accesso effettivo richiede permessi IAM aggiuntivi, la presenza di scope così ampi rappresenta un rischio latente.

**La combinazione di token esposti e scope eccessivi potrebbe estendere l’attacco oltre il perimetro cloud, coinvolgendo servizi di collaborazione aziendale**, ampliando drasticamente la superficie di compromissione.

### **Supply chain AI e agenti malevoli: un nuovo vettore**

La ricerca evidenzia anche un rischio emergente legato alla diffusione di agenti AI preconfigurati. La possibilità di distribuire agenti tramite ADK e Agent Engine apre la strada a scenari in cui codice malevolo viene integrato in componenti apparentemente legittimi. In questo modo, **la supply chain AI diventa un vettore di attacco, dove agenti compromessi si presentano come strumenti produttivi ma operano come backdoor persistenti**. Questo fenomeno richiama dinamiche già osservate nel mondo open source, ma con un impatto amp...