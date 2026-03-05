---
title: Phishing OAuth: campagne contro enti pubblici sfruttano Microsoft
url: https://www.securityinfo.it/2026/03/04/phishing-via-oauth-campagne-contro-enti-pubblici-sfruttano-i-redirect-di-microsoft-entra-per-distribuire-malware/?utm_source=rss&utm_medium=rss&utm_campaign=phishing-via-oauth-campagne-contro-enti-pubblici-sfruttano-i-redirect-di-microsoft-entra-per-distribuire-malware
source: Securityinfo.it
date: 2026-03-04
fetch_date: 2026-03-05T04:07:33.446498
---

# Phishing OAuth: campagne contro enti pubblici sfruttano Microsoft

Aggiornamenti recenti Marzo 4th, 2026 10:30 AM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Phishing OAuth: campagne contro enti pubblici sfruttano Microsoft](https://www.securityinfo.it/2026/03/04/phishing-via-oauth-campagne-contro-enti-pubblici-sfruttano-i-redirect-di-microsoft-entra-per-distribuire-malware/)
* [Android: 129 vulnerabilità corrette, zero-day Qualcomm già sfruttata](https://www.securityinfo.it/2026/03/03/android-129-vulnerabilita-corrette-zero-day-qualcomm-gia-sfruttata/)
* [Una falla in Chrome sfrutta Gemini Live per scopi malevoli](https://www.securityinfo.it/2026/03/02/una-falla-in-chrome-sfrutta-gemini-live-per-scopi-malevoli/)
* [Paradosso ransomware, pagamenti in calo ma attacchi ai massimi storici](https://www.securityinfo.it/2026/02/27/paradosso-ransomware-pagamenti-in-calo-ma-attacchi-ai-massimi-storici/)
* [Google API Keys: le chiavi pubbliche diventano credenziali sensibili](https://www.securityinfo.it/2026/02/27/google-api-keys-le-chiavi-pubbliche-diventano-credenziali-sensibili/)

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

## Phishing OAuth: campagne contro enti pubblici sfruttano Microsoft

Mar 04, 2026  [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo_security/ "Articoli scritti da Giancarlo Calzetta")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2026/03/04/phishing-via-oauth-campagne-contro-enti-pubblici-sfruttano-i-redirect-di-microsoft-entra-per-distribuire-malware/#respond)

---

Nuove campagne di phishing stanno sfruttando in modo strumentale il protocollo OAuth per distribuire malware e compromettere endpoint aziendali, con un focus particolare su organizzazioni governative e del settore pubblico. A diffondere la notizia è stata Microsoft stessa che ha rilevato un abuso sistematico dei meccanismi di redirect legittimi previsti dallo standard di autorizzazione.

![](https://www.securityinfo.it/wp-content/uploads/2026/03/OATH_Abuse-1024x572.png)

Secondo quanto comunicato dal team di sicurezza di Redmond, alcune applicazioni OAuth malevole sono già state disabilitate su Microsoft Entra ID, ma **attività correlate risultano ancora in corso e richiedono monitoraggio continuo**. Non sono stati resi noti dettagli su scala e impatto delle campagne.

### **OAuth come vettore: quando il redirect diventa arma**

OAuth (Open Authorization) è lo standard utilizzato per consentire l’accesso a servizi online tramite credenziali di terze parti, come Google, Facebook o Apple, attraverso l’uso di access token. Una delle funzionalità previste dallo standard permette agli identity provider di **reindirizzare l’utente verso una landing page** in caso di errore durante il processo di autenticazione. E proprio questa caratteristica viene sfruttata dagli attaccanti.

I criminali creano URL OAuth apparentemente legittimi, utilizzando provider come Microsoft Entra ID o Google Workspace, ma **manipolano specifici parametri** per generare volutamente un errore nel processo di login. L’errore innesca un redirect verso una pagina sotto il controllo degli attaccanti, dalla quale viene scaricato il payload malevolo.

Un esempio di URL osservato nelle campagne contro Entra ID include parametri come scope non validi e prompt=none, combinati in modo tale da produrre **un comportamento anomalo** pur mantenendo un’apparenza coerente con una richiesta OAuth standard.

Come evidenziato dai ricercatori Microsoft, **l’obiettivo non è il furto degli access token**, poiché l’utente non concede alcun permesso all’applicazione. Lo scopo è invece forzare un errore che attivi il meccanismo di redirect, trasformando un flusso legittimo in un veicolo di distribuzione malware.

### **Dalla mail al C2: la catena di infezione**

Le campagne iniziano con email di phishing che simulano richieste di firma elettronica, notifiche di registrazioni di riunioni Teams, reset password Microsoft 365 o contenuti a tema politico. I link malevoli vengono inseriti nel corpo del messaggio o, in alcuni casi, nascosti in allegati PDF.

Gli indicatori suggeriscono l’uso di strumenti di mass mailing preconfigurati, oltre a soluzioni custom sviluppate in Python e Node.js. Sono stati impiegati anche servizi cloud di posta elettronica e macchine virtuali ospitate nel cloud per la distribuzione delle email.

Una volta attivato il redirect OAuth, la vittima viene condotta su **piattaforme di phishing-as-a-service come EvilProxy**, in grado di intercettare credenziali e cookie di sessione.

In una delle campagne documentate, il redirect conduceva a un percorso /download/XXXX che **avviava automaticamente il download di un archivio ZIP**. Il contenuto includeva file LNK e loader basati su HTML smuggling.

L’apertura del file LNK innescava **l’esecuzione di un comando PowerShell** che avviava una fase di ricognizione del sistema. Successivamente veniva eseguito un file legittimo, steam\_monitor.exe, utilizzato per effettuare side-loading di una DLL malevola denominata crashhandler.dll.

La DLL provvedeva a **decrittare crashlog.dat** ed eseguire il payload finale in memoria, stabilendo una connessione outbound verso un endpoint di command-and-control esterno.

### **Persistenza e rotazione dei domini: evasione dinamica**

Un ulteriore elemento critico riguarda la flessibilità dell’infrastruttura attaccante. Ospitando il payload su URI di redirect controllati, gli attori malevoli possono **ruotare rapidamente domini e destinazioni** quando vengono bloccati dai filtri di sicurezza.

Questo approccio rende più complessa l’attività di detection basata su blacklist statiche e impone l’adozione di controlli comportamentali e analisi dei flussi OAuth anomali.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [crashhandler.dll](https://www.securityinfo.it/tag/crashhandler-dll/), [credential interception](https://www.securityinfo.it/tag/credential-interception/), [DLL side-loading](https://www.securityinfo.it/tag/dll-side-loading/), [EvilProxy](https://www.securityinfo.it/tag/evilproxy/), [LNK malware](https://www.securityinfo.it/tag/lnk-malware/), [malware delivery](https://www.securityinfo.it/tag/malware-delivery/), [Microsoft Entra ID](https://www.securityinfo.it/tag/microsoft-entra-id/), [OAuth phishing](https://www.securityinfo.it/tag/oauth-phishing/), [OAuth redirect abuse](https://www.securityinfo.it/tag/oauth-redirect-abuse/), [OAuth URL manipulation](https://www.securityinfo.it/tag/oauth-url-manipulation/), [phishing-as-a-service](https://www.securityinfo.it/tag/phishing-as-a-service/), [PowerShell attack chain](https://www.securityinfo.it/tag/powershell-attack-chain/), [sicurezza enti pubblici](https://www.securityinfo.it/tag/sicurezza-enti-pubblici/), [steam\_monitor.exe abuse](https://www.securityin...