---
title: Il data breach contro Salesloft impatta centinaia di servizi
url: https://www.securityinfo.it/2025/09/02/il-data-breach-contro-salesloft-impatta-centinaia-di-servizi/?utm_source=rss&utm_medium=rss&utm_campaign=il-data-breach-contro-salesloft-impatta-centinaia-di-servizi
source: Securityinfo.it
date: 2025-09-03
fetch_date: 2025-10-02T19:34:40.647620
---

# Il data breach contro Salesloft impatta centinaia di servizi

Aggiornamenti recenti Ottobre 1st, 2025 2:22 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Il 60% dei firewall non supera i controlli di conformità: la ricerca di FireMon](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)
* [Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/)
* [Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/)
* [CERT-AGID 20–26 settembre: phishing, malware e PEC compromesse](https://www.securityinfo.it/2025/09/29/cert-agid-20-26-settembre-phishing-malware-e-pec-compromesse/)
* [Nuova variante del malware XCSSET prende di mira gli sviluppatori Xcode su macOS](https://www.securityinfo.it/2025/09/26/nuova-variante-del-malware-xcsset-prende-di-mira-gli-sviluppatori-xcode-su-macos/)

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

## Il data breach contro Salesloft impatta centinaia di servizi

Set 02, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Intrusione](https://www.securityinfo.it/category/news/intrusione/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/09/02/il-data-breach-contro-salesloft-impatta-centinaia-di-servizi/#respond)

---

Lo scorso 20 agosto **Salesloft** [aveva avvertito](https://trust.salesloft.com/?uid=Drift%2FSalesforce+Security+Notification) di un incidente di sicurezza che ha colpito Drift, il proprio chatbot di IA usato per convertire le interazioni utente in lead di Salesforce. Gli attaccanti sono riusciti a **entrare in possesso di token Drift OAuth** per accedere a istanze di Salesforce e **sottrarre grandi volumi di dati.**

“***L’autore dell’attacco ha esportato sistematicamente grandi volumi di dati da numerose istanze aziendali di Salesforce.** GTIG ritiene che l’obiettivo principale dell’autore dell’attacco fosse quello di raccogliere credenziali. Dopo aver sottratto i dati, il gruppo ha cercato tra i dati informazioni riservate che potessero essere potenzialmente utilizzate per compromettere gli ambienti delle vittime*” ha spiegato Google Threat Intelligence Group in un report.

![Salesloft](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_evjthoevjthoevjt.png)

La campagna, iniziata l’8 agosto e durata almeno fino al 18 agosto, sarebbe a opera del gruppo UNC6395. Se inizialmente sembrava che il pericolo fosse limitato solo a quei clienti che integrano Drift in Salesforce, gli ultimi aggiornamenti di Google avvertono che **la campagna impatta anche su altre integrazioni.**“*Consigliamo ora a tutti i clienti Salesloft Drift di **considerare tutti i token memorizzati o connessi alla piattaforma Drift come potenzialmente compromessi***” si legge nel report aggiornato.

Come si legge su un articolo di Krebs On Security, questo significa che potenzialmente **gli hacker hanno sottratto token d’autenticazione per centinaia di servizi che si possono integrare con la piattaforma**, inclusi Slack, Google Workspace, Amazon S3, Azure e OpenAI.

Per quanto riguarda i suoi servizi, Google ha revocato i token compromessi degli utenti impattati e ha temporaneamente disabilitato l’integrazione tra Workspace e Drift. La compagnia ha invitato inoltre tutti i clienti di Salesloft Drift che integrano la piattaforma a revocare e ruotare le credenziali per le applicazioni connesse.

Nell’ultima [comunicazione](https://trust.salesloft.com/?uid=ACTION+NEEDED%3A+Drift+API+Integrations), Salesloft ha specificato di aver ingaggiato Mandiant e Coalition per analizzare e gestire l’incidente. “*Consigliamo a tutti i clienti Drift che gestiscono le proprie connessioni Drift ad applicazioni di terze parti tramite chiave API di **revocare in modo proattivo la chiave esistente e riconnettersi utilizzando una nuova chiave API per queste applicazioni.** Ciò riguarda solo le integrazioni Drift basate su chiave API. Le applicazioni OAuth vengono gestite direttamente da Salesloft*” ha dichiarato la compagnia.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [data breach](https://www.securityinfo.it/tag/data-breach/), [Google](https://www.securityinfo.it/tag/google/), [Salesforce](https://www.securityinfo.it/tag/salesforce/), [Salesloft](https://www.securityinfo.it/tag/salesloft/), [Salesloft Drift](https://www.securityinfo.it/tag/salesloft-drift/), [token autenticazione](https://www.securityinfo.it/tag/token-autenticazione/)

[Hexstrike AI, nuovo tool di OffSec, è già stato preso di mira dal cybercrimine](https://www.securityinfo.it/2025/09/03/hexstrike-ai-nuovo-tool-di-offsec-e-gia-stato-preso-di-mira-dal-cybercrimine/)
[Velociraptor, tool per l'analisi forense digitale, è stato sfruttato per l'accesso remoto](https://www.securityinfo.it/2025/09/01/velociraptor-tool-per-lanalisi-forense-digitale-e-stato-sfruttato-per-laccesso-remoto/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![SonicWall vittima di un breach, la compagnia chiede ai clienti di resettare le credenziali](https://www.securityinfo.it/wp-content/uploads/2025/09/cyber-security-3411499_1920-120x85.jpg)](https://www.securityinfo.it/2025/09/19/sonicwall-vittima-di-un-breach-la-compagnia-chiede-ai-clienti-di-resettare-le-credenziali/ "SonicWall vittima di un breach, la compagnia chiede ai clienti di resettare le credenziali")

  [SonicWall vittima di un breach, la...](https://www.securityinfo.it/2025/09/19/sonicwall-vittima-di-un-breach-la-compagnia-chiede-ai-clienti-di-resettare-le-credenziali/ "Permanent link to SonicWall vittima di un breach, la compagnia chiede ai clienti di resettare le credenziali")

  Set 19, 2025  [0](https://www.securityinfo.it/2025/09/19/sonicwall-vittima-di-un-breach-la-compagnia-chiede-ai-clienti-di-resettare-le-credenziali/#respond)
* [![Google e la privacy: sanzione multimilionaria per informazioni fuorvianti](https://www.securityinfo.it/wp-content/uploads/2025/09/security-4868167_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/09/10/google-e-la-privacy-sanzione-multimilionaria-per-informazioni-fuorvianti/ "Google e la privacy: sanzione multimilionaria per informazioni fuorvianti")

  [Google e la privacy: sanzione...](https://www.securityinfo.it/2025/09/10/google-e-la-privacy-sanzione-multimilionaria-per-informazioni-fuorvianti/ "Permanent link to Google e la privacy: sanzione multimiliona...