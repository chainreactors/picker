---
title: MyHidden/HiddenApp è davvero sicura?
url: https://www.ihteam.net/hacking-news/myhidden-hiddenapp-e-sicura-o-truffa/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-22
fetch_date: 2025-10-02T20:30:11.901432
---

# MyHidden/HiddenApp è davvero sicura?

[Skip to the content](#site-content)

[![IHTeam Security Blog](https://www.ihteam.net/wp-content/uploads/smlogo_2.png)](https://www.ihteam.net/)IHTeam Security Blog

Menu

* [Home](/)
* [Papers](https://www.ihteam.net/papers_tutorial/)

Close Menu

* [Home](/)
* [Papers](https://www.ihteam.net/papers_tutorial/)

Categories

[Hacking News](https://www.ihteam.net/hacking-news/)

# MyHidden/HiddenApp è davvero sicura?

* Post author

  By r00t
* Post date

  [20 September 2025](https://www.ihteam.net/hacking-news/myhidden-hiddenapp-e-sicura-o-truffa/)
* [No Comments on MyHidden/HiddenApp è davvero sicura?](https://www.ihteam.net/hacking-news/myhidden-hiddenapp-e-sicura-o-truffa/#respond)

![hiddenapp-logo](https://www.ihteam.net/wp-content/uploads/logo-hiddenapp.png)

Negli ultimi mesi, l’app **MyHidden** (o anche conosciuta come **HiddenApp**) è apparsa sull’App Store promettendo messaggi e chiamate “non intercettabili” grazie a “tecnologia militare”. Ma è davvero così sicura come afferma? Abbiamo analizzato l’app per capire se vale i 34,99 € all’anno che richiede. Se siete arrivati a questo blog o vi è stato linkato da qualcuno, sappiate che l’app è una **TRUFFA**. Ma partiamo dall’inizio.

## **Cosa promette MyHidden / HiddenApp:**

Dalla pagina dell’app su Apple Store (<https://apps.apple.com/it/app/myhidden/id6502858900>) leggiamo:

> Hidden è un’app di messaggistica con tecnologia militare. Hidden non richiede l’identificazione del cliente e fornisce un servizio per l’invio di messaggi e chiamate vocali non intercettabili. Hidden non può essere hackerato tramite sistemi trojan.

Trovo poco significativo l’utilizzo dell’espressione “tecnologia militare”, che di per sé non ha un reale valore tecnico e viene spesso impiegata per impressionare chi ha meno familiarità con il settore. Inoltre, l’affermazione secondo cui l’applicazione sarebbe immune da trojan o spyware è priva di fondamento. L’applicazione in questione utilizza un framework chiamato React Native, insieme al motore Hermes: strumenti pensati esclusivamente per lo sviluppo di applicazioni, non per offrire protezione contro minacce sofisticate come trojan o spyware.

## **I primi segni che dovrebbero farci storcere il naso**:

* Disponibilità limitata: L’applicazione è reperibile esclusivamente sull’Apple Store. Curiosamente, la versione Android è già stata rimossa dal Play Store (chissà come mai?)

[![hiddenapp-ios-1](https://www.ihteam.net/wp-content/uploads/ios_page_1-1024x909.png)](https://www.ihteam.net/wp-content/uploads/ios_page_1.png)
[![hiddenapp-ios-2](https://www.ihteam.net/wp-content/uploads/ios_page_screenshots.png)](https://www.ihteam.net/wp-content/uploads/ios_page_screenshots.png)
[![hiddenapp-ios-3](https://www.ihteam.net/wp-content/uploads/ios_page_2-1024x927.png)](https://www.ihteam.net/wp-content/uploads/ios_page_2.png)

* Restrizioni geografiche: È possibile scaricare l’app solo con un account Apple italiano. Ho provato con un account estero, ma senza successo. Viene spontaneo chiedersi: perché impedire l’accesso agli utenti stranieri?
* Dominio fresco: Il sito https://www.myhidden.uk/ è stato registrato di recente (17/01/2024) e si appoggia a un hosting condiviso su ServerPlan, una scelta che sicuramente non fa pensare a grandi investimenti infrastrutturali.

[![myhidden.uk-whois](https://www.ihteam.net/wp-content/uploads/whois-852x1024.png)](https://www.ihteam.net/wp-content/uploads/whois.png)

* Sviluppatori in letargo: L’app è sviluppata da ‘TETRIS IA. LTD’, una società dormiente con sede a Londra. “Dormiente” significa che non presenta né entrate né uscite, e il direttore attuale risulta essere un certo Emanuele Mangiapia (anche citato in questo articolo su ADN: https://www.adnkronos.com/Archivio/tecnologia/hiddenapp-ecco-lapplicazione-per-scambiare-messaggi-senza-cedere-dati\_5Noj8YMTZv46XcP3evTDzz )

[![tetris-ia-ltd-owner](https://www.ihteam.net/wp-content/uploads/tetris_ia_limited-763x1024.png)](https://www.ihteam.net/wp-content/uploads/tetris_ia_limited.png)
[![tetris-ia-ltd-balance](https://www.ihteam.net/wp-content/uploads/tetris_ia_dormant.png)](https://www.ihteam.net/wp-content/uploads/tetris_ia_dormant.png)

* Monetizzazione sospetta: L’applicazione richiede un pagamento prima ancora di poter essere effettivamente utilizzata. Un dettaglio che, diciamolo, non contribuisce certo a dissipare i dubbi.

## **La realtà tecnica dietro MyHidden / HiddenApp:**

Da buon appassionato di tecnologia, ho deciso di concedere una chance a questa nuovissima e “sicurissima” applicazione, iniziando con un’analisi statica dell’applicazione iOS. Il primo dettaglio interessante che emerge riguarda il dominio con cui l’app comunica una volta avviata:

[![hiddenapp-endpoints](https://www.ihteam.net/wp-content/uploads/api_endpoints_from_main.jsbundle-1024x228.png)](https://www.ihteam.net/wp-content/uploads/api_endpoints_from_main.jsbundle.png)

‘backend.myhidden.uk’ è un sottodominio del sito vetrina principale, che punta a un server VPS situato in Germania. Nulla di male, se non fosse che si tratta di una soluzione dal costo di poche decine di euro al mese. Non proprio il massimo della sicurezza enterprise.

L’applicazione si avvale anche di una serie di servizi esterni, tutti ben noti nel panorama tech:

* Google Firebase: utilizzato per l’analisi dei crash e come database. Un classico, insomma.
* Twilio: gestisce le comunicazioni vocali e video. Nulla di male, ma è interessante sapere che le conversazioni passano anche da qui.
* Stripe: si occupa dei pagamenti. Affidabile, certo, ma sempre un altro attore coinvolto.

È quindi evidente che la comunicazione non rimane confinata al server di MyHidden, ma viene distribuita tra una serie di grandi aziende, ciascuna con i propri sistemi, policy e infrastrutture. In altre parole, la “riservatezza assoluta” tanto sbandierata sembra più un concetto relativo… e parecchio condiviso.

A rendere il tutto ancora più pittoresco è la quantità di servizi e porte lasciate allegramente in ascolto sulla VPS del backend: 21/FTP, 22/SSH, 25/SMTP, 53/DNS, 80/HTTP, 110/POP3, 143/IMAP, 443/HTTP, 465/SMTP, 993/IMAP, 995/POP3, 4190/PIGEONHOLE, 8443/HTTP, 8880/HTTP. Insomma, un vero e proprio buffet per chi ama la varietà.

[![hiddenapp-backend-ports](https://www.ihteam.net/wp-content/uploads/censys-1024x564.png)](https://www.ihteam.net/wp-content/uploads/censys.png)

Per quanto riguarda la sicurezza delle comunicazioni, il certificato SSL utilizzato per proteggere l’API è stato generato gratuitamente tramite Let’s Encrypt. Una scelta sicuramente economica, ma che non trasmette esattamente l’idea di una fortezza digitale.

[![hiddenapp-ssl-certificates](https://www.ihteam.net/wp-content/uploads/ssl_certificates-1024x730.png)](https://www.ihteam.net/wp-content/uploads/ssl_certificates.png)

A questo punto, vale la pena analizzare come l’applicazione gestisce i dati degli utenti, sia localmente che sul backend, e soprattutto verificare se le rassicuranti dichiarazioni del direttore Mangiapia trovano riscontro nei fatti:

* Non esiste profilazione
* Non c’è un database
* Gli utenti sono e restano totalmente anonimi

In fase di registrazione dobbiamo scegliere uno username e una password, senza alcuna verifica email. Un processo snello, certo, che ci ha portato direttamente alla pagina dei pagamenti gestiti da Stripe. Tuttavia, con una semplice analisi, abbiamo notato che al momento del login viene già assegnato un token di sessione (JWT, peraltro firmato con HS256, non proprio lo stato dell’arte in termini di sicurezza). Questo ci ha permesso di saltare il pagamento di 7,99€ e testare l’app come utenti “premium” a costo zero. Un affare, almeno per noi.

[![hiddenapp-login-request-response](https://www.ihteam.net/wp-content/uploads/login_jwt-1024x530.png)](https://www.ihteam.net/wp-content/uploads/login_jwt.png)

Il token di sessione, insieme a tutte le informazioni restituite dopo il login, viene salvato in chiaro su un database SQLite locale, invece di u...