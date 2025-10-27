---
title: Un invito Google Calendar bastava per prendere il controllo di Gemini
url: https://www.securityinfo.it/2025/08/11/un-invito-google-calendar-bastava-per-prendere-il-controllo-di-gemini/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-12
fetch_date: 2025-10-07T00:49:14.129460
---

# Un invito Google Calendar bastava per prendere il controllo di Gemini

Aggiornamenti recenti Ottobre 6th, 2025 5:03 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Impennata delle scansioni dei portali di login di Palo Alto Networks: +500%](https://www.securityinfo.it/2025/10/06/impennata-delle-scansioni-dei-portali-di-login-di-palo-alto-networks-500/)
* [Microsoft Sentinel: arriva l’era degli agenti AI e della difesa predittiva](https://www.securityinfo.it/2025/10/06/microsoft-sentinel-arriva-lera-degli-agenti-ai-e-della-difesa-predittiva/)
* [CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)

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

## Un invito Google Calendar bastava per prendere il controllo di Gemini

Ago 11, 2025  [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo_security/ "Articoli scritti da Giancarlo Calzetta")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/08/11/un-invito-google-calendar-bastava-per-prendere-il-controllo-di-gemini/#respond)

---

Una vulnerabilità in **Google Calendar** consentiva a un attaccante di **compromettere a distanza l’assistente Gemini** — l’LLM di Google — sfruttando un semplice invito a un evento. La falla, individuata dai ricercatori di SafeBreach, permetteva di **esfiltrare dati personali**, controllare dispositivi smart home e persino avviare applicazioni sullo smartphone della vittima, il tutto **senza che l’utente facesse nulla di anomalo**.

![](https://www.securityinfo.it/wp-content/uploads/2025/08/Calendar11-ago-2025CG-1024x683.png)

### L’attacco: prompt injection nascosto nel titolo di un evento

Il meccanismo sfruttava un **prompt injection indiretto** inserito nel titolo di un evento Google Calendar. Una volta che la vittima chiedeva a Gemini qualcosa di banale, come *“Quali sono i miei eventi di oggi?”*, l’assistente recuperava l’elenco dal calendario, includendo il titolo malevolo.

Il testo malevolo veniva così **interpretato da Gemini come un’istruzione legittima**, senza che il modello fosse in grado di distinguere tra contenuto innocuo e comando ostile. In questo modo, un cybercriminale poteva ordinare all’LLM di accedere alle email e **estrarre informazioni sensibili**; cancellare o modificare eventi sul calendario, aprire URL per **ottenere l’indirizzo IP** della vittima, avviare **videochiamate su Zoom,** controllare dispositivi domestici connessi tramite Google Home.

### Nessuna interazione “sospetta” richiesta

Secondo i ricercatori, **non era necessario alcun accesso privilegiato al modello** e le protezioni integrate, come il filtro dei prompt, non impedivano l’attacco. L’unico requisito era che l’evento malevolo fosse incluso tra quelli letti da Gemini.

Per aumentare la furtività, l’attaccante poteva inviare sei inviti in sequenza, **nascondendo quello malevolo** tra i più vecchi: infatti, Google Calendar mostra solo i cinque eventi più recenti, mentre gli altri restano nascosti dietro al tasto *“Mostra altro”*. Gemini, tuttavia, li legge tutti quando interroga il calendario.

In pratica, **la vittima non vedeva il titolo malevolo** a meno che non espandesse manualmente la lista eventi.

### Un problema ricorrente per Gemini

Non è la prima volta che l’assistente AI di Google è vulnerabile a questo tipo di attacco. **Lo scorso mese**, Marco Figueroa di Mozilla aveva segnalato un altro caso di prompt injection capace di preparare **campagne di phishing mirato**.

Questa nuova dimostrazione evidenzia il rischio intrinseco di dare a un LLM **permessi estesi e capacità di azione trasversali** su più servizi. È proprio questa integrazione profonda a renderlo utile — e al tempo stesso a esporlo ad abusi potenzialmente devastanti.

### La risposta di Google

Google ha confermato di aver **corretto la vulnerabilità** prima che potesse essere sfruttata attivamente, ringraziando Ben Nassi e il team di SafeBreach per la **responsible disclosure**.

> “La loro ricerca ci ha permesso di comprendere meglio nuovi vettori di attacco e accelerare il rilascio di difese all’avanguardia ora già operative per proteggere gli utenti”, ha dichiarato **Andy Wen**, senior director per la sicurezza di Google Workspace. “È un ottimo esempio dell’importanza del red-teaming e della collaborazione tra settori”.

Google ha inoltre ribadito di essere al lavoro su **nuove misure di mitigazione** per proteggere Gemini da attacchi avversariali sempre più sofisticati.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [AI security](https://www.securityinfo.it/tag/ai-security/), [furto dati](https://www.securityinfo.it/tag/furto-dati/), [Gemini](https://www.securityinfo.it/tag/gemini/), [Google Calendar](https://www.securityinfo.it/tag/google-calendar/), [google workspace](https://www.securityinfo.it/tag/google-workspace/), [prompt injection](https://www.securityinfo.it/tag/prompt-injection/), [SafeBreach](https://www.securityinfo.it/tag/safebreach/), [sicurezza informatica](https://www.securityinfo.it/tag/sicurezza-informatica/), [Smart Home](https://www.securityinfo.it/tag/smart-home/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[Ondata di attacchi brute-force contro le VPN Fortinet, poi FortiManager](https://www.securityinfo.it/2025/08/12/ondata-di-attacchi-brute-force-contro-le-vpn-fortinet-poi-fortimanager/)
[CERT-AGID 2 – 8 agosto: rubati documenti d’identità a clienti di hotel italiani](https://www.securityinfo.it/2025/08/11/cert-agid-2-8-agosto-rubati-documenti-didentita-a-clienti-di-hotel-italiani/)

---

![](https://secure.gravatar.com/avatar/d6a6ecdad542d883704003e541413ca8?s=90&d=mm&r=g)

##### [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo_security/)

##### Articoli correlati

* [![Microsoft Sentinel: arriva l’era degli agenti AI e della difesa predittiva](https://www.securityinfo.it/wp-content/uploads/2025/10/Microsoft-Sentinel_3ott-2025CG-120x85.png)](https://www.securityinfo.it/2025/10/06/microsoft-sentinel-arriva-lera-degli-agenti-ai-e-della-difesa-predittiva/ "Microsoft Sentinel: arriva l’era degli agenti AI e della difesa predittiva")

  [Microsoft Sentinel: arriva l’era...](https://www.securityinfo.it/2025/10/06/microsoft-sentinel-arriva-lera-degli-agenti-ai-e-della-difesa-predittiva/ "Permanent link to Microsoft Sentinel: arriva...