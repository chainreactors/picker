---
title: Codice formattato, ma migliaia di secret esposti: il problema del copia-incolla selvaggio
url: https://www.securityinfo.it/2025/11/26/codice-formattato-ma-migliaia-di-secret-esposti-il-problema-del-copia-incolla-selvaggio/?utm_source=rss&utm_medium=rss&utm_campaign=codice-formattato-ma-migliaia-di-secret-esposti-il-problema-del-copia-incolla-selvaggio
source: Securityinfo.it
date: 2025-11-26
fetch_date: 2025-11-27T03:12:46.553097
---

# Codice formattato, ma migliaia di secret esposti: il problema del copia-incolla selvaggio

Aggiornamenti recenti Novembre 26th, 2025 4:07 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Codice formattato, ma migliaia di secret esposti: il problema del copia-incolla selvaggio](https://www.securityinfo.it/2025/11/26/codice-formattato-ma-migliaia-di-secret-esposti-il-problema-del-copia-incolla-selvaggio/)
* [Torna Shalai Ulud: centinaia di pacchetti compromessi](https://www.securityinfo.it/2025/11/25/torna-shalai-ulud-centinaia-di-pacchetti-compromessi/)
* [DeepSeek R1 produce codice vulnerabile con prompt “politicamente sensibili”](https://www.securityinfo.it/2025/11/24/deepseek-r1-produce-codice-vulnerabile-con-prompt-politicamente-sensibili/)
* [CERT-AGID 15–21 novembre: attacchi a università, banche e PEC](https://www.securityinfo.it/2025/11/24/cert-agid-15-21-novembre-attacchi-universita-banche-pec/)
* [Come Firemon supporta i propri partner nel processo di migrazione da Skybox](https://www.securityinfo.it/2025/11/21/come-firemon-supporta-i-propri-partner-nel-processo-di-migrazione-da-skybox/)

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

## Codice formattato, ma migliaia di secret esposti: il problema del copia-incolla selvaggio

Nov 26, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Gestione dati](https://www.securityinfo.it/category/approfondimenti/gestione-dati/), [Gestione dati](https://www.securityinfo.it/category/news/gestione-dati-news/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Leaks](https://www.securityinfo.it/category/approfondimenti/leaks/), [Leaks](https://www.securityinfo.it/category/news/leaks-news/), [Minacce](https://www.securityinfo.it/category/approfondimenti/minacce/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/11/26/codice-formattato-ma-migliaia-di-secret-esposti-il-problema-del-copia-incolla-selvaggio/#respond)

---

I ricercatori di watchTowr Labs [hanno individuato](https://labs.watchtowr.com/stop-putting-your-passwords-into-random-websites-yes-seriously-you-are-the-problem/) **migliaia di secret, chiavi di autenticazione, username e password** e molti altri dati sensibili esposti sul web dopo essere stati **caricati su tool di formattazione online** come i noti JSONformatter e CodeBeautify.

La colpa è ovviamente di chi, per formattare velocemente il codice, lo copia e incolla su queste piattaforme, senza ragionare sul contenuto di ciò che sta condividendo. Il risultato? **Un dataset di oltre 80.000 parti di JSON** contenenti, tra gli altri dati, **chiavi private**, **credenziali Active Directory**, informazioni di configurazioni LDAP, credenziali FTP, **token JWT di utenti amministratori**, credenziali di pipeline CI/CD, richieste e risposte API complete e molti altri, compresa un’esportazione completa di tutte le credenziali dall’AWS Secret Manager.

![secret esposti](https://www.securityinfo.it/wp-content/uploads/2025/11/Gemini_Generated_Image_s57cbns57cbns57c.png)

Il problema non sta tanto nel fatto di copiare il codice e formattarlo online, ma di usare la funzionalità “Salva” dei tool che consente di **generare un link condivisibile** **con chiunque** del codice formattato; e con “chiunque” si intende, appunto, chiunque entri in possesso del link.

Generare un link valido non è così difficile: questi tool, oltre a mettere a disposizione una **sezione con tutti i link salvati di recente**, seguono un formato molto prevedibile per costruire gli URL; per un attaccante, è sufficiente usare uno script che visita la sezione dei link recenti, ne copia gli ID e invia una richiesta al server per ottenere i file salvati.

A rendere il tutto più preoccupante, come se non lo fosse già abbastanza, è il fatto che i dati esposti appartengono a organizzazioni di ogni settore, compreso quello delle infrastrutture critiche nazionali, il settore governativo, la sanità, il settore finanziario e il bancario.

Si parla di cinque anni di contenuti caricati su JSONformatter e un anno su CodeBeautify, per un totale di **oltre 50 GB di dati JSON annotati, con migliaia di secret esposti.**

Tra gli esempi di dati esposti individuati dal team di watchTowr Labs, ci sono uno **script PowerShell di un ente governativo che conteneva le password in chiaro per creare account amministratore locali** e chiavi di registro e una mail di onboarding caricata da un dipendente di un MSSP che conteneva le sue credenziali per l’accesso ai sistemi della società e di un loro grande cliente.ù

![](https://www.securityinfo.it/wp-content/uploads/2022/06/stockvault-digital-padlock-on-data-screen-web-and-data-security180399.jpg)

Digital padlock on data screen – Web and data security

È lecito chiedersi se gli attaccanti effettivamente sfruttano questi tool per cercare dati sensibili e credenziali e, nel caso, quanto di frequente. La risposta arriva sempre da watchTowr Labs: stando a un test effettuato dai ricercatori, dopo aver caricato dei falsi secret su CodeBeautify, gli attaccanti **hanno cominciato a testarli per l’accesso dopo 48 ore dal salvataggio dei file**. Considerando che i link sulla pagina degli URL generati di recente vengono cancellati dopo 24 ore dalla loro generazione, significa che gli attaccanti hanno immediatamente cercato e salvato le credenziali per testarle poi in un secondo momento.

Inizialmente, dopo essere stati contattati da watchTower Labs, sia JSONformatter che CodeBeautify avevano disabilitato temporaneamente la funzionalità “Recent Links”. Attualmente la sezione è tornata navigabile ed **è quindi di nuovo possibile accedere ai dati salvati.**A prescindere da questo, **la colpa è chiaramente di chi carica e condivide dati sensibili senza pensare alle conseguenze.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [chiavi API](https://www.securityinfo.it/tag/chiavi-api/), [CodeBeautify](https://www.securityinfo.it/tag/codebeautify/), [credenziali](https://www.securityinfo.it/tag/credenziali/), [data leak](https://www.securityinfo.it/tag/data-leak/), [formattazione codice](https://www.securityinfo.it/tag/formattazione-codice/), [JSONformatter](https://www.securityinfo.it/tag/jsonformatter/), [secret](https://www.securityinfo.it/tag/secret/)

[Torna Shalai Ulud: centinaia di pacchetti compromessi](https://www.securityinfo.it/2025/11/25/torna-shalai-ulud-centinaia-di-pacchetti-compromessi/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Leak Oracle Cloud: numerose compagnie confermano il furto di dati](https://www.securityinfo.it/wp-content/uploads/2025/03/126628-120x85.jpg)](https://www.securityinfo.i...