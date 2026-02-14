---
title: False estensioni AI su Chrome: rubano API e sessioni
url: https://www.securityinfo.it/2026/02/13/false-estensioni-ai-su-chrome-rubano-api-e-sessioni/?utm_source=rss&utm_medium=rss&utm_campaign=false-estensioni-ai-su-chrome-rubano-api-e-sessioni
source: Securityinfo.it
date: 2026-02-13
fetch_date: 2026-02-14T04:08:27.951083
---

# False estensioni AI su Chrome: rubano API e sessioni

Aggiornamenti recenti Febbraio 13th, 2026 2:30 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [False estensioni AI su Chrome: rubano API e sessioni](https://www.securityinfo.it/2026/02/13/false-estensioni-ai-su-chrome-rubano-api-e-sessioni/)
* [Effetto Domino: nel 2026 i fornitori sono le vulnerabilità più critiche](https://www.securityinfo.it/2026/02/12/effetto-domino-nel-2026-i-fornitori-sono-le-vulnerabilita-piu-critiche/)
* [Lummastealer risorge dalle ceneri: ancora una volta lo stop è momentaneo](https://www.securityinfo.it/2026/02/11/lummastealer-risorge-dalle-ceneri-ancora-una-volta-lo-stop-e-momentaneo/)
* [ZeroDayRAT: La Nuova Minaccia per Android e iOS](https://www.securityinfo.it/2026/02/10/zerodayrat-la-nuova-minaccia-per-android-e-ios/)
* [L’arma dell’autenticità: come il cybercrimine sta piegando i servizi SaaS](https://www.securityinfo.it/2026/02/09/larma-dellautenticita-come-il-cybercrimine-sta-piegando-i-servizi-saas/)

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

## False estensioni AI su Chrome: rubano API e sessioni

Feb 13, 2026  [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo_security/ "Articoli scritti da Giancarlo Calzetta")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Malware](https://www.securityinfo.it/category/news/malware-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2026/02/13/false-estensioni-ai-su-chrome-rubano-api-e-sessioni/#respond)

---

**Un’inquietante campagna di cyberspionaggio ha colpito almeno 260.000 utenti Chrome**, sfruttando il crescente interesse verso gli assistenti basati su intelligenza artificiale. Dietro un’apparente offerta di tool utili per scrivere, riassumere o leggere le email, si celano invece estensioni malevole progettate per rubare dati sensibili e informazioni personali.

**AiFrame: l’infrastruttura della truffa**

L’indagine è stata condotta da LayerX Security che ha ribattezzato l’operazione con il nome “AiFrame”. **Tutte le estensioni riconosciute all’interno di questa campagna malevola, ben 32, condividono lo stesso codice base e comunicano con domini remoti sotto il controllo di tapnetic[.]pro**, un’infrastruttura centralizzata che consente agli attaccanti di gestire in tempo reale i payload e le capacità delle estensioni.

Spesso, queste campagne durano poco dal momento che le estensioni vengono controllate spesso dagli esperti di sicurezza, ma AiFrame ha organizzato un sistema di “reincarnazione” automatica grazie al quale **diverse estensioni rimosse dallo store ufficiale sono ricomparse con nuovi ID**, mantenendo nome e funzionalità simili. È il caso di AI Sidebar, che dopo essere stata rimossa come “Gemini AI Sidebar” (con 80.000 installazioni) è riapparsa con un nuovo ID, già utilizzato da oltre 70.000 utenti.

![](https://www.securityinfo.it/wp-content/uploads/2026/02/API_Estensioni-1024x683.png)

**Iframe invisibili e attacchi silenziosi**

Uno degli elementi tecnici più pericolosi di AiFrame è l’uso degli iframe. **L’interfaccia dell’estensione non è reale, ma è un overlay caricato da remoto** che può essere modificato dinamicamente in ogni momento, senza passare da un aggiornamento ufficiale sul Chrome Web Store. Questo iframe è in grado di inviare comandi all’estensione, istruendola a leggere contenuti dalla pagina attiva.

Gli script iniettati sfruttano librerie come Readability di Mozilla per estrarre titoli, testi, metadata e contenuti leggibili. **Le informazioni raccolte, inclusi eventuali token di autenticazione e contenuti dinamici, vengono poi trasmesse al dominio remoto**, sfuggendo a ogni controllo dell’utente e di Google.

**Gmail nel mirino: accesso completo ai contenuti**

Circa la metà delle estensioni individuate si concentra su Gmail, implementando un codice comune per l’integrazione con la casella di posta. **L’estensione è in grado di leggere i messaggi visibili, accedere ai contenuti delle conversazioni, e persino intercettare i testi in fase di scrittura**. Tutti questi dati vengono silenziosamente inoltrati ai server remoti, senza che l’utente possa rendersene conto.

Il badge “Featured” assegnato ad alcune di queste estensioni, come nel caso di “AI Assistant”, aggrava ulteriormente la situazione: **l’etichetta di qualità contribuisce a consolidare un falso senso di sicurezza**, inducendo l’utente a fidarsi di un componente che, in realtà, agisce da agente malevolo nel browser.

**L’ingegneria sociale dell’intelligenza artificiale**

L’attacco è particolarmente insidioso perché sfrutta un fenomeno sociotecnico recente: **l’interazione conversazionale con gli assistenti AI ha abbattuto le barriere di diffidenza, portando gli utenti a condividere più facilmente dati e contesti personali**. Questa abitudine è stata trasformata dagli attaccanti in un punto di forza: gli iframe truccati simulano perfettamente le interfacce di strumenti noti come ChatGPT, Claude o Gemini, rendendo l’intercettazione praticamente invisibile.

Anche il riconoscimento vocale è stato utilizzato come vettore: alcune estensioni captano le parole pronunciate dagli utenti, le trascrivono e le inviano al server controllato dagli attaccanti, **aggiungendo un ulteriore livello di sorveglianza invisibile**.

**Ancora disponibili, ancora pericolose**

Nonostante la gravità della scoperta, molte delle estensioni malevole risultano ancora oggi disponibili sul Chrome Web Store. **Google, al momento della pubblicazione del report, non ha rilasciato alcun commento ufficiale sulla vicenda**.

Il report completo di LayerX elenca gli ID di tutte le estensioni coinvolte. Finché non verranno rimosse, **il consiglio è di sospendere ogni fiducia verso gli assistenti AI installabili come estensioni browser, almeno fino a una verifica rigorosa delle fonti e dei permessi richiesti**.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [AiFrame](https://www.securityinfo.it/tag/aiframe/), [API key leak](https://www.securityinfo.it/tag/api-key-leak/), [attacco iframe invisibile](https://www.securityinfo.it/tag/attacco-iframe-invisibile/), [Chrome Web Store](https://www.securityinfo.it/tag/chrome-web-store/), [estensioni Chrome malevole](https://www.securityinfo.it/tag/estensioni-chrome-malevole/), [estensioni pericolose](https://www.securityinfo.it/tag/estensioni-pericolose/), [furto dati Gmail](https://www.securityinfo.it/tag/furto-dati-gmail/), [Intelligenza artificiale](https://www.securityinfo.it/tag/intelligenza-artificiale/), [LayerX Security](https://www.securityinfo.it/tag/layerx-security/), [sicurezza browser](https://www.securityinfo.it/tag/sicurezza-browser/), [sicurezza informatica](https://www.securityinfo.it/tag/sicurezza-informatica/)

[Effetto Domino: nel 2026 i fornitori sono le vulnerabilità più critiche](https://www.securityinfo.it/2026/02...