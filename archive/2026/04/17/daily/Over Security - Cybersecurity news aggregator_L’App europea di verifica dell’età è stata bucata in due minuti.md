---
title: L’App europea di verifica dell’età è stata bucata in due minuti
url: https://www.securityinfo.it/2026/04/17/lapp-europea-di-verifica-delleta-e-stata-bucata-in-meno-di-due-minuti/
source: Over Security - Cybersecurity news aggregator
date: 2026-04-17
fetch_date: 2026-04-18T04:33:24.497927
---

# L’App europea di verifica dell’età è stata bucata in due minuti

Aggiornamenti recenti Aprile 17th, 2026 2:21 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [L’App europea di verifica dell’età è stata bucata in due minuti](https://www.securityinfo.it/2026/04/17/lapp-europea-di-verifica-delleta-e-stata-bucata-in-meno-di-due-minuti/)
* [Recovery scam: quando la truffa colpisce due volte](https://www.securityinfo.it/2026/04/16/recovery-scam-quando-la-truffa-colpisce-due-volte/)
* [Supply chain: il 69% delle aziende pronto a co-finanziare la sicurezza](https://www.securityinfo.it/2026/04/15/supply-chain-il-69-delle-aziende-pronto-a-finanziare-la-sicurezza-dei-fornitori/)
* [Donne e cybersecurity: crescono le nuove leve e alcune sfide](https://www.securityinfo.it/2026/04/14/donne-e-cybersecurity-crescono-le-nuove-leve-e-alcune-sfide/)
* [Social media vietati ai minori? In Australia non sta funzionando](https://www.securityinfo.it/2026/04/13/social-media-vietati-ai-minori-in-australia-non-sta-funzionando/)

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

## L’App europea di verifica dell’età è stata bucata in due minuti

Apr 17, 2026  [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo_security/ "Articoli scritti da Giancarlo Calzetta")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Tecnologia](https://www.securityinfo.it/category/news/tecnologia-news/)
 [0](https://www.securityinfo.it/2026/04/17/lapp-europea-di-verifica-delleta-e-stata-bucata-in-meno-di-due-minuti/#respond)

---

La nuova app europea per la verifica dell’età, presentata come soluzione privacy-friendly per l’accesso ai servizi online, è finita immediatamente sotto scrutinio e non ne è uscita bene. A poche ore dal lancio, un ricercatore di sicurezza ha dimostrato come sia possibile **aggirare i meccanismi di protezione in meno di due minuti**, sollevando dubbi sulla solidità dell’architettura e sulla reale efficacia del sistema.

Il progetto, promosso dalla Commissione europea, nasce con l’obiettivo di consentire agli utenti di **dimostrare la propria età senza condividere dati personali con le piattaforme**, riducendo la necessità di raccolta e gestione di informazioni sensibili. Un approccio che punta a coniugare compliance normativa e tutela della privacy, ma che, secondo i primi riscontri tecnici, potrebbe introdurre nuove superfici di attacco.

![](https://www.securityinfo.it/wp-content/uploads/2026/04/AgeVerificationBuggata-1024x683.png)

### **Un bypass semplice ma strutturale**

Le criticità evidenziate non riguardano una vulnerabilità isolata, ma **scelte progettuali che espongono il sistema a manipolazioni dirette da parte dell’utente**. Secondo quanto emerso, l’app memorizza localmente un PIN cifrato, ma senza legarlo in modo sicuro al vault identitario che contiene i dati di verifica.

Questo dettaglio apre la strada a un attacco relativamente semplice. Modificando alcuni file di configurazione e riavviando l’applicazione, è possibile **reimpostare il PIN mantenendo l’accesso alle credenziali già generate**, di fatto riutilizzando dati di identità sotto un nuovo controllo di accesso. Il risultato è un sistema che accetta credenziali precedenti senza una reale validazione del contesto.

### **Controlli aggirabili e sicurezza “resettable”**

Ulteriori criticità emergono nei meccanismi di difesa contro attacchi più aggressivi. Il sistema di rate limiting, fondamentale per prevenire tentativi ripetuti di accesso, è implementato come **un semplice contatore salvato nello stesso file di configurazione** modificabile. Azzerando questo valore, l’app perde memoria dei tentativi effettuati, rendendo possibili attacchi di forza bruta.

Anche **l’autenticazione biometrica risulta vulnerabile**. La sua attivazione è gestita tramite un flag booleano: modificandolo manualmente, è possibile disabilitare completamente il controllo, bypassando uno dei principali livelli di sicurezza previsti.

In altre parole: **i controlli di sicurezza possono essere alterati direttamente dall’utente, compromettendo l’intero modello di fiducia dell’applicazione**.

### **Un problema di design più che di bug**

La reazione della comunità di sicurezza è stata immediata. Diversi esperti hanno sottolineato come il problema non sia riconducibile a un semplice bug, ma a **una progettazione che non tiene conto dei principi fondamentali della sicurezza** mobile.

In particolare, è stata evidenziata **l’assenza di integrazione con componenti hardware sicuri**, come il secure enclave presente sui dispositivi moderni, che avrebbe potuto proteggere le informazioni critiche da modifiche locali.

Altri dubbi riguardano la logica stessa del sistema, inclusa la presenza di limiti temporali sulle credenziali di età. Un approccio che **solleva interrogativi sull’effettiva coerenza del modello**, considerando che l’età anagrafica non è un attributo soggetto a variazioni retroattive.

### **Una sicurezza ancora da dimostrare**

L’episodio evidenzia un punto critico per il futuro della regolamentazione digitale: **la sicurezza non può essere un elemento secondario rispetto alla compliance normativa**. Soluzioni progettate per proteggere gli utenti rischiano di ottenere l’effetto opposto se non supportate da architetture robuste e da una corretta implementazione dei controlli.

C’è da dire che l’approccio di rendere open source il codice dell’app testimonia la buona volontà dell’Unione e traccia un bel precedente di trasparenza e solidità. L’app, infatti, non è ancora scaricabile e la community si è attivata su Github per studiarla prima che potesse far danni. Chi è stato incaricato dello sviluppo è già al lavoro per tappare le numerose falle trovate e seguire i (saggi) consigli ricevuti dalla comunità di sicurezza.

D’altro canto, è abbastanza desolante il fatto che l’Unione costringa le aziende ad assumere una postura di sicurezza ben strutturata con norme severe e poi **crei un’app che sembra un colabrodo** per la gestione degli accessi online basati sull’età. Speriamo che questa cantonata insegni qualcosa per i progetti futuri.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [age verification app UE](https://www.securityinfo.it/tag/age-verification-app-ue/), [app sicurezza UE](https://www.securityinfo.it/tag/app-sicurezza-ue/), [biometric bypass](https://www.securityinfo.it/tag/biometric-bypass/), [bypass autenticazione PIN](https://www.securityinfo.it/tag/bypass-autenticazione-pin/), [cybersecurity Europa](https://www.securityinfo.it/tag/cybersecurity-europa/), [privacy digitale UE](https://www.securityinfo.it/tag/privacy-digitale-ue/), [rischio sorveglianza digitale](https://www.securityinfo.it/tag/rischio-sorveglianza-digitale/), [secure enclave mobile](https://www.securityinfo.it/tag/secure-enclave-mobile/), [sicurezza identità digitale](https://www.securityinfo.it/tag/sicurezza-identita-digitale/), [v...