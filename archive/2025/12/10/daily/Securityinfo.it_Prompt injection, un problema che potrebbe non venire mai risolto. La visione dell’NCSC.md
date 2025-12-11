---
title: Prompt injection, un problema che potrebbe non venire mai risolto. La visione dell’NCSC
url: https://www.securityinfo.it/2025/12/10/prompt-injection-un-problema-che-potrebbe-non-venire-mai-risolto-la-visione-dellncsc/?utm_source=rss&utm_medium=rss&utm_campaign=prompt-injection-un-problema-che-potrebbe-non-venire-mai-risolto-la-visione-dellncsc
source: Securityinfo.it
date: 2025-12-10
fetch_date: 2025-12-11T03:24:57.531859
---

# Prompt injection, un problema che potrebbe non venire mai risolto. La visione dell’NCSC

Aggiornamenti recenti Dicembre 10th, 2025 2:00 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Prompt injection, un problema che potrebbe non venire mai risolto. La visione dell’NCSC](https://www.securityinfo.it/2025/12/10/prompt-injection-un-problema-che-potrebbe-non-venire-mai-risolto-la-visione-dellncsc/)
* [React2Shell: più di 160.000 indirizzi IP vulnerabili, oltre 30 organizzazioni già colpite](https://www.securityinfo.it/2025/12/09/react2shell-piu-di-160-000-indirizzi-ip-vulnerabili-oltre-30-organizzazioni-gia-colpite/)
* [CERT-AGID 29 novembre – 5 dicembre: phishing a tema Governo italiano e Agenzia delle Entrate](https://www.securityinfo.it/2025/12/08/cert-agid-29-novembre-5-dicembre-phishing-governo-italiano-agenzia-entrate/)
* [Iniezione indiretta di prompt: a rischio le informazioni aziendali](https://www.securityinfo.it/2025/12/05/iniezione-indiretta-di-prompt-a-rischio-le-informazioni-aziendali/)
* [Dark Telegram in ritirata: aumentano le chiusure dei canali clandestini](https://www.securityinfo.it/2025/12/04/dark-telegram-in-ritirata-aumentano-le-chiusure-dei-canali-clandestini/)

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

## Prompt injection, un problema che potrebbe non venire mai risolto. La visione dell’NCSC

Dic 10, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Attacchi](https://www.securityinfo.it/category/approfondimenti/attacchi/), [Gestione dati](https://www.securityinfo.it/category/approfondimenti/gestione-dati/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/approfondimenti/minacce/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/), [Vulnerabilità](https://www.securityinfo.it/category/approfondimenti/vulnerabilita-approfondimenti/)
 [0](https://www.securityinfo.it/2025/12/10/prompt-injection-un-problema-che-potrebbe-non-venire-mai-risolto-la-visione-dellncsc/#respond)

---

Secondo il National Cyber Security Centre (NCSC), l’agenzia governativa del Regno Unito per la cybersecurity, **il problema della prompt injection (PI) potrebbe non venire mai risolto**.

In un [approfondimento](https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection) dedicato l’agenzia ha spiegato che, nonostante le due vulnerabilità vengano spesso accostate, sono in realtà concettualmente molto diverse. Assumere che siano simili significa rischiare di **sottovalutare la PI** e di conseguenza applicare  misure di mitigazione inefficaci.

“*Sebbene il confronto tra la prompt injection e la SQL injection possa essere allettante, è anche pericoloso. La seconda può essere adeguatamente mitigata con query parametrizzate, ma è probabile che la prima non possa mai essere adeguatamente mitigata allo stesso modo. **Il meglio che possiamo sperare è di ridurre la probabilità o l’impatto degli attacchi***” si legge nel post.

![prompt injection](https://www.securityinfo.it/wp-content/uploads/2025/12/Gemini_Generated_Image_vux53rvux53rvux5.png)

Il concetto dietro le due vulnerabilità è lo stesso: in entrambi i casi si tratta di una gestione errata di dati e istruzioni che consente di eseguire l’input utente come un comando. Nel caso della SQL injection la mitigazione standard è l’uso di **query parametrizzate**che trattano sempre l’input come dato e mai come istruzione.

Nel caso degli LLM questa distinzione non esiste: quando il chatbot riceve un prompt, lo elabora senza distinguere le istruzioni dai dati, cercando sempre di **prevedere il token successivo più probabile**. Poiché non c’è una separazione vera tra istruzione e dato a livello del modello, **non esiste un equivalente delle query parametrizzate deterministico e risolutivo**.

Ad oggi la mitigazione della prompt injection è un’area di ricerca molto attiva e include già diversi approcci, come l’individuazione dei tentativi di injection, l’addestramento dei modelli per prioritizzare le istruzioni rispetto a “*dati che sembrano istruzioni*” e istruire il modello su cosa sono i “*dati*“. Di fatto le metodologie si basano sempre sull’idea di separare ciò che è “dato” da ciò che è “istruzione”; poiché però gli LLM operano in maniera intrinsecamente diversa dagli altri sistemi, **la mitigazione non è definitiva.**

## Prompt injection: urge applicare strategie di mitigazione

Per ridurre il rischio, è fondamentale che sviluppatori e team di sicurezza comprendano che **la PI è un rischio persistente che non può essere mitigato completamente con un prodotto o un’appliance esterna**.

È necessario che i modelli e le applicazioni vengano progettate seguendo i principi del **Secure Design**, soprattutto quando l’LLM è autorizzato a chiamare strumenti esterni o API. La protezione deve includere: l’implementazione di controlli di sicurezza non-LLM che vincolino le azioni del sistema e l’applicazione del principio del *least privilege*.

È possibile inoltre usare tecniche per ridurre la probabilità che l’LLM agisca sulle istruzioni iniettate usando marcatori come i tag XML per incapsulare e separare la sezione “dati” dalle “istruzioni”. L’NCSC in questo caso sconsiglia di affidarsi a delle deny-list di frasi malevole, in quanto la complessità degli LLM offre infinite riformulazioni che possono eludere questi filtri.

![](https://www.securityinfo.it/wp-content/uploads/2025/12/Gemini_Generated_Image_emsoz8emsoz8emso.png)

Infine, è essenziale monitorare prompt e dati per identificare attività sospette, inclusi l’input e l’output completi dell’LLM, e le chiamate a strumenti o API. Poiché gli attaccanti spesso devono affinare i loro attacchi, il rilevamento e la risposta a chiamate API o strumenti fallite possono indicare le fasi iniziali di una violazione.

L’NCSC avverte che, come è successo con le SQL Injection, c’è il rischio che, se non si adottano fin da subito [approcci di sicurezza migliori](https://www.securityinfo.it/2025/06/24/prompt-injection-indiretta-google-la-sua-strategia-di-sicurezza-a-piu-livelli/), avvenga un picco di compromissioni e fughe di dati. “*Rischiamo di vedere questo modello ripetersi con la prompt injection, dato che stiamo per integrare la genAI nella maggior parte delle applicazioni. **Se queste applicazioni non sono progettate tenendo conto della prompt injection, potrebbe verificarsi un’ondata simile di violazioni*****“.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Intelligenza artificiale](https://www.securityinfo.it/tag/intelligenza-artificiale/), [LLM](https://www.securityinfo.it/tag/llm/), [mitigazione vulnerabilità](https://www.securityinfo.it/tag/mitigazione-vulnerabilita/), [prompt injection](https://www.sec...