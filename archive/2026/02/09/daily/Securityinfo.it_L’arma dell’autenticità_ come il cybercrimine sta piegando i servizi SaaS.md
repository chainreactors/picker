---
title: L’arma dell’autenticità: come il cybercrimine sta piegando i servizi SaaS
url: https://www.securityinfo.it/2026/02/09/larma-dellautenticita-come-il-cybercrimine-sta-piegando-i-servizi-saas/?utm_source=rss&utm_medium=rss&utm_campaign=larma-dellautenticita-come-il-cybercrimine-sta-piegando-i-servizi-saas
source: Securityinfo.it
date: 2026-02-09
fetch_date: 2026-02-10T04:27:24.176190
---

# L’arma dell’autenticità: come il cybercrimine sta piegando i servizi SaaS

Aggiornamenti recenti Febbraio 9th, 2026 2:40 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [L’arma dell’autenticità: come il cybercrimine sta piegando i servizi SaaS](https://www.securityinfo.it/2026/02/09/larma-dellautenticita-come-il-cybercrimine-sta-piegando-i-servizi-saas/)
* [n8n: nuove vulnerabilità critiche aggirano le patch di dicembre](https://www.securityinfo.it/2026/02/06/n8n-sotto-pressione-nuove-vulnerabilita-critiche-aggirano-le-patch-di-dicembre/)
* [TrendAI: il 2026 sarà l’anno dell’industrializzazione del cybercrime](https://www.securityinfo.it/2026/02/06/trendai-2026-anno-industrializzazione-cybercrime/)
* [Shadow Campaign: la nuova ondata di cyber-spionaggio globale](https://www.securityinfo.it/2026/02/05/shadow-campaign-la-nuova-ondata-di-cyber-spionaggio-globale/)
* [NTLM verso lo “switch-off”: Microsoft si prepara a bloccarlo di default](https://www.securityinfo.it/2026/02/03/ntlm-verso-lo-switch-off-microsoft-si-prepara-a-bloccarlo-di-default/)

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

## L’arma dell’autenticità: come il cybercrimine sta piegando i servizi SaaS

Feb 09, 2026  [Redazione](https://www.securityinfo.it/author/redazione/ "Articoli scritti da Redazione")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2026/02/09/larma-dellautenticita-come-il-cybercrimine-sta-piegando-i-servizi-saas/#respond)

---

Il panorama delle minacce informatiche è in continuo cambiamento e recentemente si sta assistendo a  una metamorfosi del phishing dove la tecnica del mascheramento cede il passo all’**abuso deliberato delle infrastrutture cloud** legittime. Check Point Software Technologies ha recentemente portato alla luce una campagna di phishing massiva che, invece di creare domini fraudolenti, utilizza le funzionalità native delle piattaforme **Software-as-a-Service (SaaS)** per veicolare truffe telefoniche. L’operazione ha già raggiunto numeri impressionanti, con circa **133.260 e-mail inviate** che hanno messo nel mirino oltre **20.000 aziende** a livello globale, sfruttando la reputazione di giganti come Microsoft, Zoom e Amazon.

![](https://www.securityinfo.it/wp-content/uploads/2026/02/Gemini_Generated_minorenni.png)

Questa strategia segna un cambio di paradigma fondamentale nel social engineering, poiché le esche non sono semplici imitazioni ma **comunicazioni generate dai sistemi reali** dei fornitori. Inserendo contenuti fraudolenti nei campi controllati dall’utente, come i dati del profilo o i metadati di fatturazione, gli attaccanti costringono le piattaforme a inviare notifiche ufficiali che superano indenni ogni controllo di autenticazione come **SPF, DKIM e DMARC**. Il risultato è un messaggio che eredita la totale **fiducia e autorevolezza** del brand mittente, rendendo quasi impossibile il rilevamento da parte dei sistemi di sicurezza automatizzati e abbassando drasticamente la soglia di sospetto degli utenti.

### Un fenomeno in rapida crescita

L’analisi dei dati evidenzia un’accelerazione verticale del fenomeno negli ultimi mesi: se nell’ultimo semestre si sono registrate circa 648.291 e-mail malevole, ben **463.773 di queste sono state concentrate negli ultimi tre mesi**. Questa impennata suggerisce che i criminali informatici considerino l’abuso del SaaS un meccanismo di distribuzione **estremamente scalabile e redditizio**. David Gubiani, Regional Director Security Engineering di Check Point, sottolinea come a peggiorare la situazione (rendendo gli attacchi potenzialmente molto più  efficaci) dopo il primo approccio tramite email, l’operatività venga spostata al telefono, tramite l’indicazione di chiamare il call center per sistemare il problema. In questo modo, si **bypassa l’analisi degli URL e il sandboxing**, trasferendo il cuore dell’attacco verso una manipolazione vocale diretta, dove il fattore umano diventa l’anello debole.

![](https://www.securityinfo.it/wp-content/uploads/2026/02/PhishingSaas_mercati.png)

I metodi identificati spaziano dalla manipolazione dei campi profilo su piattaforme come **YouTube e Malwarebytes**, alla generazione di notifiche di abbonamento fraudolente tramite i flussi di lavoro di **Microsoft Entra ID e Power BI**. Particolarmente sofisticato è l’abuso degli inviti di **Amazon Business**, dove gli aggressori inseriscono falsi addebiti e finti numeri di assistenza da chiamare direttamente nei campi dell’invito aziendale. In tutti questi casi, le piattaforme non sono state compromesse nel senso tradizionale del termine: sono le loro **funzionalità legittime a essere utilizzate impropriamente** per dare credibilità a una truffa che si conclude con una chiamata a un call center controllato dai criminali.

### USA bersaglio preferito, ma Europa al secondo posto

A livello settoriale, il comparto **Tecnologia e IT è il più colpito** con il 26,8% dei casi, seguito dalla produzione industriale e dal settore dell’istruzione. Geograficamente, gli **Stati Uniti rimangono il bersaglio principale**, ma l’Europa segue a ruota con una quota del 17,8%, a dimostrazione della portata globale dell’offensiva. La lezione per i difensori è chiara: la provenienza di un’e-mail da un dominio affidabile non è più una garanzia di sicurezza. È necessaria un’evoluzione delle strategie di difesa che passi attraverso l’**analisi contestuale dei messaggi** e una formazione degli utenti capace di riconoscere le nuove dinamiche del phishing vocale basato su servizi cloud.

![](https://www.securityinfo.it/wp-content/uploads/2026/02/Phishing_saas_Geo.png)

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Amazon Business](https://www.securityinfo.it/tag/amazon-business/), [brand impersonation](https://www.securityinfo.it/tag/brand-impersonation/), [Check Point Software](https://www.securityinfo.it/tag/check-point-software/), [cybersecurity](https://www.securityinfo.it/tag/cybersecurity/), [IT Security](https://www.securityinfo.it/tag/it-security/), [Microsoft 365](https://www.securityinfo.it/tag/microsoft-365/), [minacce informatiche 2026](https://www.securityinfo.it/tag/minacce-informatiche-2026/), [Phishing](https://www.securityinfo.it/tag/phishing/), [Protezione dati](https://www.securityinfo.it/tag/protezione-dati/), [SaaS abuse](https://www.securityinfo.it/tag/saas-abuse/), [sicurezza cloud](https://www.securityinfo.it/tag/sicurezza-cloud/), [sicurezza informatica](https://www.securityinfo.it/tag/sicurezza-informatica/), [social engineering](https://www.securityinfo.it/tag/social-engineering/), [truffe telefoniche](https://www.securityinfo.it/tag/truffe-telefoniche/), [Zoom](https://www.securityinfo.it/tag/zoom/)

[n8n: nuove vulnerabilità critiche aggirano le patch di dicembre](https://www.securityinfo.it/2026/02/06/n8n-sotto-pression...