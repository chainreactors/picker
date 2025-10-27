---
title: DeepSeek: il top della tecnologia cinese dimentica di chiudere il database esposto
url: https://www.securityinfo.it/2025/01/31/deepseek-il-top-della-tecnologia-cinese-dimentica-di-chiudere-il-database-esposto/
source: Over Security - Cybersecurity news aggregator
date: 2025-02-01
fetch_date: 2025-10-06T20:36:49.587260
---

# DeepSeek: il top della tecnologia cinese dimentica di chiudere il database esposto

Aggiornamenti recenti Ottobre 6th, 2025 9:00 AM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)
* [Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)
* [Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/)

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

## DeepSeek: il top della tecnologia cinese dimentica di chiudere il database esposto

Gen 31, 2025  [Redazione](https://www.securityinfo.it/author/redazione/ "Articoli scritti da Redazione")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/01/31/deepseek-il-top-della-tecnologia-cinese-dimentica-di-chiudere-il-database-esposto/#respond)

---

La rapida ascesa della startup cinese di intelligenza artificiale, DeepSeek, è stata offuscata da una significativa **falla di sicurezza** che ha esposto tantissimi dati interni e degli utenti, sollevando serie preoccupazioni riguardo alla gestione della sicurezza. Questa vulnerabilità, scoperta dai ricercatori di sicurezza di Wiz, ha interessato un database ClickHouse che era **accessibile senza necessità di autenticazione**, consentendo a soggetti potenzialmente malevoli di accedere a informazioni cruciali.

![](https://www.securityinfo.it/wp-content/uploads/2025/01/DeepSeek2-300x300.png)

Il database ClickHouse, ospitato agli indirizzi `oauth2callback.deepseek.com:9000` e `dev.deepseek.com:9000`, offriva il **controllo completo sulle operazioni del database**. Ciò comprendeva l’accesso a dati interni, inclusi la cronologia delle chat, chiavi segrete, dettagli del backend, segreti delle API e metadati operativi. La vulnerabilità poteva essere sfruttata tramite l’interfaccia HTTP di ClickHouse, permettendo l’esecuzione di query SQL arbitrarie direttamente attraverso un browser. La **mancanza di autenticazione** implicava che chiunque fosse a conoscenza dell’indirizzo del database poteva potenzialmente accedervi e sfruttare la falla. I ricercatori hanno identificato oltre un milione di righe di log contenenti dati sensibili. Attraverso l’interfaccia di ClickHouse, era anche possibile sottrarre password e file direttamente dal server.

La falla di sicurezza ha consentito un **accesso non autorizzato a un’ampia gamma di informazioni**, inclusi dati personali degli utenti e potenziali documenti sensibili aziendali. La **mancanza di autenticazione** ha reso possibile la completa escalation dei privilegi all’interno dell’ambiente di DeepSeek, senza alcuna difesa. Nonostante DeepSeek abbia risolto la vulnerabilità dopo essere stata contattata dai ricercatori di Wiz, non è dato sapere se i dati siano finiti nelle mani di cybercriminali.

DeepSeek ha agito prontamente per risolvere la falla di sicurezza, con un aggiornamento pubblicato il 29 gennaio 2025, in cui dichiarava di aver identificato il problema (forse anche abbastanza palese) e di essere al lavoro per implementare una soluzione. Tuttavia, questo incidente ci riporta ai tempi dei bucket S3 aperti su AWS, un fenomeno ai tempi così diffuso e pericoloso da costringere Amazon a chiudere di default con password i bucket che venivano creati.

Questa situazione si colloca in un contesto più ampio di **preoccupazioni riguardanti la privacy e la sicurezza** connesse all’IA. Il Garante della Privacy italiano ha bloccato DeepSeek dopo aver ricevuto informazioni insufficienti sulla gestione dei dati. Il Garante ha inoltre notato che l’azienda ha dichiarato di non operare in Italia e di non essere quindi soggetta alla normativa europea. Anche l’Irish Data Protection Commission (DPC) ha inviato una richiesta simile. Sono anche emersi sospetti di **furto di proprietà intellettuale**, con accuse secondo cui DeepSeek potrebbe aver utilizzato l’API di OpenAI senza autorizzazione per addestrare i propri modelli, una pratica nota come “distillazione”. Infine, sono state sollevate preoccupazioni riguardo ai **legami di DeepSeek con il governo cinese**.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [AI](https://www.securityinfo.it/tag/ai/), [Bucket](https://www.securityinfo.it/tag/bucket/), [Governo Cinese](https://www.securityinfo.it/tag/governo-cinese/), [Intelligenza artificiale](https://www.securityinfo.it/tag/intelligenza-artificiale/), [LLM](https://www.securityinfo.it/tag/llm/), [Password](https://www.securityinfo.it/tag/password/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[CERT-AGID 25 – 31 gennaio: attacchi contro funzionari governativi e rappresentanti di ambasciate](https://www.securityinfo.it/2025/02/03/cert-agid-25-31-gennaio-attacchi-funzionari-governativi-rappresentanti-ambasciate/)
[Trovata una backdoor in due dispositivi cinesi per il monitoraggio dei pazienti](https://www.securityinfo.it/2025/01/31/trovata-una-backdoor-in-due-dispositivi-cinesi-per-il-monitoraggio-dei-pazienti/)

---

![](https://secure.gravatar.com/avatar/57d6369d65bf9ebecae351af675ce2fd?s=90&d=mm&r=g)

##### [Redazione](https://www.securityinfo.it/author/redazione/)

##### Articoli correlati

* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_d4x8rid4x8rid4x8-120x85.png)](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  [Firewall Cisco sotto attacco: una nuova...](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Permanent link to Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  Set 29, 2025  [0](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/#respond)
* [![Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia gov...