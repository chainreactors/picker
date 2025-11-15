---
title: Vulnerabilità di Fortinet FortiWeb sfruttata per creare utenti admin
url: https://www.securityinfo.it/2025/11/14/vulnerabilita-di-fortinet-fortiweb-sfruttata-per-creare-utenti-admin/?utm_source=rss&utm_medium=rss&utm_campaign=vulnerabilita-di-fortinet-fortiweb-sfruttata-per-creare-utenti-admin
source: Securityinfo.it
date: 2025-11-14
fetch_date: 2025-11-15T03:09:13.666499
---

# Vulnerabilità di Fortinet FortiWeb sfruttata per creare utenti admin

Aggiornamenti recenti Novembre 14th, 2025 4:56 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Vulnerabilità di Fortinet FortiWeb sfruttata per creare utenti admin](https://www.securityinfo.it/2025/11/14/vulnerabilita-di-fortinet-fortiweb-sfruttata-per-creare-utenti-admin/)
* [Crescono le truffe ai danni dei consumatori, preoccupano quelle basate su IA. Il report di Bitdefender](https://www.securityinfo.it/2025/11/13/crescono-le-truffe-ai-danni-dei-consumatori-preoccupano-quelle-basate-su-ia-il-report-di-bitdefender/)
* [Fantasy Hub: scoperto un nuovo RAT Android che prende il controllo totale del dispositivo](https://www.securityinfo.it/2025/11/12/fantasy-hub-scoperto-un-nuovo-rat-android-che-prende-il-controllo-totale-del-dispositivo/)
* [Torna GlassWorm, il primo worm che colpisce le estensioni di VS Code](https://www.securityinfo.it/2025/11/11/torna-glassworm-il-primo-worm-che-colpisce-le-estensioni-di-vs-code/)
* [Knownsec colpita da un catastrofico breach: esposti oltre 12.000 documenti sensibili](https://www.securityinfo.it/2025/11/10/knownsec-colpita-da-un-catastrofico-breach-esposti-oltre-12-000-documenti-sensibili/)

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

## Vulnerabilità di Fortinet FortiWeb sfruttata per creare utenti admin

Nov 14, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/11/14/vulnerabilita-di-fortinet-fortiweb-sfruttata-per-creare-utenti-admin/#respond)

---

Una presunta v**ulnerabilità di Fortinet FortiWeb** sta venendo attivamente sfruttata per **creare utenti admin**. A riportarlo è Daniel Card, ricercatore di [PwnDefend](https://www.pwndefend.com/2025/11/13/suspected-fortinet-zero-day-exploited-in-the-wild/), spiegando che si dovrebbe trattare di un **bug di Path Traversal** non ancora patchata. Inizialmente il problema era stato individuato dalla compagnia Defused ed è stato dettagliato negli ultimi giorni da Card.

![Fortinet FortiWeb](https://www.securityinfo.it/wp-content/uploads/2025/11/Gemini_Generated_Image_fzqj3kfzqj3kfzqj.png)

Il ricercatore spiega che, utilizzando uno specifico endpoint (`/api/v2.0/cmdb/system/admin%3F/../../../../../cgi-bin/fwbcgi`), è possibile inserire un payload nella richiesta POST che crea **un utente con privilegi di amministratore**, garantendo agli attaccanti accesso persistente al sistema.

“*Questo payload sembra crea un account utente locale con livello admin sul dispositivo colpito. Ho un firewall Fortinet in esecuzione e non sono riuscito a confermare l’effetto dell’attacco*” afferma Card, aggiungendo però che, analizzando l’endpoint, è altamente probabile che la vulnerabilità sia effettivamente quella presunta.

Dalle analisi effettuate sono emersi una serie di payload che riportavano la creazione di utenti con username quali, tra gli altri, Testpoint, trader1, trader2, test1234point che sembrano per l’appunto indicare una serie di exploit di verifica. In un post su X, i ricercatori WatchTowr  hanno in seguito condiviso l’exploit funzionante.

> another exploited in-the-wild FortiWeb vuln? It must be Thursday! [pic.twitter.com/F9TQgdJQ4l](https://t.co/F9TQgdJQ4l)
>
> — watchTowr (@watchtowrcyber) [November 13, 2025](https://twitter.com/watchtowrcyber/status/1989017336632996337?ref_src=twsrc%5Etfw)

Come riporta [Bleeping Computer](https://www.bleepingcomputer.com/news/security/fortiweb-flaw-with-public-poc-actively-exploited-to-create-admin-users/), il team di WatchTowr ha anche rilasciato un [tool](https://github.com/watchtowrlabs/watchTowr-vs-Fortiweb-AuthBypass) per aiutare gli amministratori di sistema a identificare i dispositivi vulnerabili. La testata sottolinea che, al momento, **non c’è alcun riferimento al bug sul portale di Fortinet dedicato agli avvisi di sicurezza**. Bleeping Computer ha contattato direttamente la compagnia per fare chiarezza sulla questione, ma non ha ancora ricevuto risposta.

I prodotti colpiti sono i **Fortinet FortiWeb con versione inferiore alla 8.0.2**. Agli amministratori di sistema è caldamente consigliato aggiornare il prima possibile i dispositivi vulnerabili e, nel frattempo, assicurarsi che gli endpoint di gestione siano raggiungibili solo entro reti sicure.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [accesso persistente ai sistemi](https://www.securityinfo.it/tag/accesso-persistente-ai-sistemi/), [Fortinet FortiWeb](https://www.securityinfo.it/tag/fortinet-fortiweb/), [path traversal](https://www.securityinfo.it/tag/path-traversal/), [privilegi amministratore](https://www.securityinfo.it/tag/privilegi-amministratore/), [utenti admin](https://www.securityinfo.it/tag/utenti-admin/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[Crescono le truffe ai danni dei consumatori, preoccupano quelle basate su IA. Il report di Bitdefender](https://www.securityinfo.it/2025/11/13/crescono-le-truffe-ai-danni-dei-consumatori-preoccupano-quelle-basate-su-ia-il-report-di-bitdefender/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Scoperte nuove vulnerabilità di ChatGPT che portano a leak di dati](https://www.securityinfo.it/wp-content/uploads/2025/11/Gemini_Generated_Image_8yofud8yofud8yof-120x85.png)](https://www.securityinfo.it/2025/11/05/scoperte-nuove-vulnerabilita-di-chatgpt-che-portano-a-leak-di-dati/ "Scoperte nuove vulnerabilità di ChatGPT che portano a leak di dati")

  [Scoperte nuove vulnerabilità di...](https://www.securityinfo.it/2025/11/05/scoperte-nuove-vulnerabilita-di-chatgpt-che-portano-a-leak-di-dati/ "Permanent link to Scoperte nuove vulnerabilità di ChatGPT che portano a leak di dati")

  Nov 05, 2025  [0](https://www.securityinfo.it/2025/11/05/scoperte-nuove-vulnerabilita-di-chatgpt-che-portano-a-leak-di-dati/#respond)
* [![Il codice generato da IA pone molti rischi di sicurezza](https://www.securityinfo.it/wp-content/uploads/2025/10/Gemini_Generated_Image_pc4c3ipc4c3ipc4c-120x85.png)](https://www.securityinfo.it/2025/10/31/il-codice-generato-da-ia-pone-molti-rischi-di-sicurezza/ "Il codice generato da IA pone molti rischi di sicurezza")

  [Il codice generato da IA pone molti...](https://www.securityinfo.it/2025/10/31/il-codice-generato-da-ia-pone-molti-rischi-di-sicurezza/ "Permanent link to Il codice generato da IA pone molti rischi di sicurezza")

  Ott 31, 2025  [0](https://www.securityinfo.it/2025/10/31/il-codice-generato-da-ia-pone-molti-rischi-di-sicurezza/#respond)
* [![Atlas, browser basato...