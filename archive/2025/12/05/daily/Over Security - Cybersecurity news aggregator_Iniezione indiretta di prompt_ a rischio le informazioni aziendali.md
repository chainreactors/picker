---
title: Iniezione indiretta di prompt: a rischio le informazioni aziendali
url: https://www.securityinfo.it/2025/12/05/iniezione-indiretta-di-prompt-a-rischio-le-informazioni-aziendali/
source: Over Security - Cybersecurity news aggregator
date: 2025-12-05
fetch_date: 2025-12-06T03:11:35.430150
---

# Iniezione indiretta di prompt: a rischio le informazioni aziendali

Aggiornamenti recenti Dicembre 5th, 2025 4:48 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Iniezione indiretta di prompt: a rischio le informazioni aziendali](https://www.securityinfo.it/2025/12/05/iniezione-indiretta-di-prompt-a-rischio-le-informazioni-aziendali/)
* [Dark Telegram in ritirata: aumentano le chiusure dei canali clandestini](https://www.securityinfo.it/2025/12/04/dark-telegram-in-ritirata-aumentano-le-chiusure-dei-canali-clandestini/)
* [PickleScan, scoperti tre bug 0-day che permettono di iniettare payload malevoli nei modelli ML](https://www.securityinfo.it/2025/12/03/picklescan-scoperti-tre-bug-0-day-che-permettono-di-iniettare-payload-malevoli-nei-modelli-ml/)
* [ShadyPanda: oltre 4 milioni di browser infetti in una campagna durata 7 anni](https://www.securityinfo.it/2025/12/02/shadypanda-oltre-4-milioni-di-browser-infetti-in-una-campagna-durata-7-anni/)
* [Coupang conferma il data breach: esposti i dati di oltre 30 milioni di utenti](https://www.securityinfo.it/2025/12/01/coupang-conferma-il-data-breach-esposti-i-dati-di-oltre-30-milioni-di-utenti/)

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

## Iniezione indiretta di prompt: a rischio le informazioni aziendali

Dic 05, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Attacchi](https://www.securityinfo.it/category/approfondimenti/attacchi/), [Gestione dati](https://www.securityinfo.it/category/approfondimenti/gestione-dati/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/approfondimenti/minacce/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/12/05/iniezione-indiretta-di-prompt-a-rischio-le-informazioni-aziendali/#respond)

---

[Lakera](https://www.lakera.ai/blog), società di Check Point, ha pubblicato una ricerca in cui dimostra che **l’iniezione indiretta di prompt permette agli attaccanti di prendere di mira i dati acquisiti dall’IA e non i prompt inseriti dagli utenti.**

Con Gemini 3 il rischio di leak si moltiplica: secondo l’analisi dei ricercatori, gli attaccanti riescono a estrarre informazioni a livello aziendale come documenti, e-mail, link, PDF e contenuti condivisi.

Il team di Lakera evidenzia che, sebbene le capacità multimodali di Gemini 3 portano enormi vantaggi in termini di produttività, introducono nuove forme di rischio, come l’iniezione indiretta di prompt che porta al leak di dati sensibili.

![Iniezione indiretta prompt](https://www.securityinfo.it/wp-content/uploads/2025/12/artificial-intelligence-3382507_1920.jpg)

Il modello *gemini-3-pro-preview* è uno tra i sistemi attuali più potenti, in particolare per quanto riguarda gli scenari di estrazione diretta dei contenuti e di override delle istruzioni. “***La vera trasformazione di Gemini 3 non è ciò che il modello conosce, ma ciò a cui il modello può accedere*****”** affermano i ricercatori di Lakera.  Poiché l’IA ha a che fare con documenti, caselle di posta, API, flussi di lavoro e sistemi in tutto l’ambiente aziendale, di fatto il modello è autorizzato a dare pressoché qualsiasi cosa e accedere a ogni tipo di documento.

Gemini 3 è in grado di operare con un livello di autonomia molto elevato e, tra le altre cose, può riscrivere e instradare documenti, riassumere e agire su lunghi thread di e-mail, richiamare API e attivare automazioni del flusso di lavoro. Ciò significa che un attaccante, abusando dei prompt indiretti, può **manipolare e ottenere documenti sensibili**, inserendosi nel flusso operativo. “*Man mano che l’IA diventa parte del livello di esecuzione, la superficie di attacco si espande e gran parte di questa espansione è invisibile ai controlli di sicurezza esistenti*“.

Il pericolo aumenta se si considera che Gemini 3 introduce anche dei comportamenti “agentici”, ovvero la capacità di intraprendere azioni, non solo di fornire risposte. Di fatto, **l’IA ha ora un “potere” molto più elevato rispetto alla semplice ricerca.**

Lakera [ha rilevato](https://www.lakera.ai/blog/the-expanding-attack-surface-of-multimodal-llms) attacchi multimodali pratici, tra cui *jailbreak* basati sull’audio. I nuovi vettori d’attacco non sono coperti dagli attuali controlli di sicurezza delle e-mail, degli endpoint o dei contenuti.

Secondo il GenAI Security Readiness Report di Lakera,  le organizzazioni stanno adottando l’IA molto più rapidamente di quanto non stiano provvedendo alla sua sicurezza. La maggior parte di esse risulta priva di governance dell’IA, barriere protettive, soluzioni di monitoraggio degli agent e protezioni multimodali. L’avvento di Gemini 3 e in generale di tutte le IA in grado di manipolare documenti aziendali, amplifica questo divario.

L’IA è diventato il nuovo perimetro aziendale e per le organizzazioni è imperativo occuparsi di definire nuove strategie di sicurezza per proteggersi dalle nuove minacce.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Check Point](https://www.securityinfo.it/tag/check-point/), [data leak](https://www.securityinfo.it/tag/data-leak/), [Gemini 3](https://www.securityinfo.it/tag/gemini-3/), [informazioni aziendali](https://www.securityinfo.it/tag/informazioni-aziendali/), [iniezione indiretta prompt](https://www.securityinfo.it/tag/iniezione-indiretta-prompt/), [Lakera](https://www.securityinfo.it/tag/lakera/)

[Dark Telegram in ritirata: aumentano le chiusure dei canali clandestini](https://www.securityinfo.it/2025/12/04/dark-telegram-in-ritirata-aumentano-le-chiusure-dei-canali-clandestini/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Codice formattato, ma migliaia di secret esposti: il problema del copia-incolla selvaggio](https://www.securityinfo.it/wp-content/uploads/2025/11/Gemini_Generated_Image_s57cbns57cbns57c-120x85.png)](https://www.securityinfo.it/2025/11/26/codice-formattato-ma-migliaia-di-secret-esposti-il-problema-del-copia-incolla-selvaggio/ "Codice formattato, ma migliaia di secret esposti: il problema del copia-incolla selvaggio")

  [Codice formattato, ma migliaia di...](https://www.securityinfo.it/2025/11/26/codice-formattato-ma-migliaia-di-secret-esposti-il-problema-del-copia-incolla-selvaggio/ "Permanent link to Codice formattato, ma migliaia di secret esposti: il problema del copia-incolla selvaggio")

  Nov 26, 2025  [0](https://www.securityinfo.it/2025/11/26/codice-formattato-ma-migliaia-di-secret-esposti-il-problema-del-copia-incolla-selvaggio/#respond)
* [![Check Point acquisisce Veriti e la sua tecnologia di Preemptive Exposure Management](https://www.securityinfo.it/wp-content/uploads/2025/05/cybersecurity-6250709_1920-120x85.jpg)](https://www.securityinfo.it/2025/05/28/ch...