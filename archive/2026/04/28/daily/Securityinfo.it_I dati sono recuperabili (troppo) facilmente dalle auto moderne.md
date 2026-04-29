---
title: I dati sono recuperabili (troppo) facilmente dalle auto moderne
url: https://www.securityinfo.it/2026/04/28/i-dati-sono-recuperabili-troppo-facilmente-dalle-auto-moderne/?utm_source=rss&utm_medium=rss&utm_campaign=i-dati-sono-recuperabili-troppo-facilmente-dalle-auto-moderne
source: Securityinfo.it
date: 2026-04-28
fetch_date: 2026-04-29T05:12:58.762742
---

# I dati sono recuperabili (troppo) facilmente dalle auto moderne

Aggiornamenti recenti Aprile 28th, 2026 3:11 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [I dati sono recuperabili (troppo) facilmente dalle auto moderne](https://www.securityinfo.it/2026/04/28/i-dati-sono-recuperabili-troppo-facilmente-dalle-auto-moderne/)
* [Reset password: una misura di sicurezza che diventa minaccia](https://www.securityinfo.it/2026/04/23/reset-password-una-misura-di-sicurezza-che-diventa-minaccia/)
* [Kyber annuncia il ransomware “post-quantum”, ma…](https://www.securityinfo.it/2026/04/22/kyber-annuncia-il-ransomware-post-quantum-ma/)
* [L’App europea di verifica dell’età è stata bucata in due minuti](https://www.securityinfo.it/2026/04/17/lapp-europea-di-verifica-delleta-e-stata-bucata-in-meno-di-due-minuti/)
* [Recovery scam: quando la truffa colpisce due volte](https://www.securityinfo.it/2026/04/16/recovery-scam-quando-la-truffa-colpisce-due-volte/)

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

## I dati sono recuperabili (troppo) facilmente dalle auto moderne

Apr 28, 2026  [Redazione](https://www.securityinfo.it/author/redazione/ "Articoli scritti da Redazione")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Attacchi](https://www.securityinfo.it/category/approfondimenti/attacchi/), [Attacchi](https://www.securityinfo.it/category/news/attachi/), [Hacking](https://www.securityinfo.it/category/approfondimenti/hacking/), [Hacking](https://www.securityinfo.it/category/news/hacking-news/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2026/04/28/i-dati-sono-recuperabili-troppo-facilmente-dalle-auto-moderne/#respond)

---

Come sappiamo, le auto moderne sono sempre più simili a sistemi IT distribuiti su quattro ruote. Sensori, centraline e moduli di comunicazione raccolgono e trasmettono una quantità crescente di dati, trasformando il veicolo in un nodo connesso all’interno di un ecosistema digitale. Ovviamente, sappiamo che questo significa nuove superfici di rischio, ma ci sono alcuni rischi che sarebbe relativamente semplice evitare e invece… [Un’analisi condotta dai ricercatori di Quarkslab](https://blog.quarkslab.com/tearing-down-a-car-telematic-unit-and-finding-an-accident-on-facebook.html?utm_source=FoT&utm_medium=email&utm_campaign=trucks-fot-slate-wayve-uber) dimostra come **i dati generati da un’auto possano essere estratti, correlati e ricostruiti fino a raccontare eventi reali della vita delle persone**.

![](https://www.securityinfo.it/wp-content/uploads/2026/04/AutoDigitali-1024x576.png)

### **Dal teardown hardware all’intelligence**

Il punto di partenza dello studio è stato l’analisi di una telematic control unit (TCU), uno dei componenti chiave nei veicoli connessi, appartenente a una BYD rottamata a causa di un incidente. Questi moduli gestiscono comunicazioni cellulari, servizi di emergenza e funzionalità avanzate come aggiornamenti OTA.

Attraverso tecniche di reverse engineering, i ricercatori hanno smontato fisicamente il dispositivo, estratto il firmware e analizzato il contenuto della memoria. Il risultato è stato sorprendente: la TCU conteneva **dati dettagliati relativi al funzionamento del veicolo, inclusi log e informazioni sugli eventi senza particolari accorgimenti di protezione**.

Il passo successivo ha portato l’indagine fuori dal perimetro tecnico. Incrociando queste informazioni con fonti pubbliche, è stato possibile collegare i dati estratti a un incidente reale documentato sui social network.

![](https://www.securityinfo.it/wp-content/uploads/2026/04/TCU-OSINT-1024x857.png)

### **Quando l’OSINT completa il puzzle**

L’elemento più interessante della ricerca non è tanto l’accesso ai dati embedded, quanto la loro mancanza di criptografia e la possibilità di correlarli con informazioni open source. L’utilizzo di tecniche di Open Source Intelligence (OSINT) ha permesso di **ricostruire una storia completa partendo da frammenti digitali apparentemente isolati**.

Questo approccio riporta in auge un rischio che abbiamo già visto in passato in diversi dispositivi, tipo gli HD all’interno dei computer dismessi o gettati in discarica con l’aggravante della vicinanza ai proprietari: i dati raccolti dai dispositivi IoT, inclusi quelli automotive, non sono pericolosi solo singolarmente, ma soprattutto quando combinati con altre fonti che le contestualizza.

### **Privacy e supply chain sotto pressione**

Lo studio mette in luce criticità rilevanti sul fronte della sicurezza e della privacy. Le TCU possono infatti conservare dati persistenti anche dopo essere state rimosse dal veicolo, rendendo possibile il recupero di informazioni da dispositivi acquistati sul mercato secondario.

Questo scenario introduce rischi lungo tutta la supply chain. Produttori, fornitori e operatori che gestiscono questi dispositivi devono considerare **la protezione dei dati non solo durante l’utilizzo, ma anche nel ciclo di vita completo del prodotto**, inclusa la dismissione.

La mancanza di meccanismi efficaci di cancellazione sicura può trasformare componenti dismessi in fonti di informazioni sensibili, con implicazioni per utenti finali, flotte aziendali e assicurazioni.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [automotive cyber risk](https://www.securityinfo.it/tag/automotive-cyber-risk/), [connected car security](https://www.securityinfo.it/tag/connected-car-security/), [cybersecurity automotive](https://www.securityinfo.it/tag/cybersecurity-automotive/), [data privacy automotive](https://www.securityinfo.it/tag/data-privacy-automotive/), [dati veicoli sicurezza](https://www.securityinfo.it/tag/dati-veicoli-sicurezza/), [ECU security](https://www.securityinfo.it/tag/ecu-security/), [IoT automotive](https://www.securityinfo.it/tag/iot-automotive/), [OSINT cybersecurity](https://www.securityinfo.it/tag/osint-cybersecurity/), [privacy auto connesse](https://www.securityinfo.it/tag/privacy-auto-connesse/), [telematic control unit TCU](https://www.securityinfo.it/tag/telematic-control-unit-tcu/)

[Reset password: una misura di sicurezza che diventa minaccia](https://www.securityinfo.it/2026/04/23/reset-password-una-misura-di-sicurezza-che-diventa-minaccia/)

---

![](https://secure.gravatar.com/avatar/57d6369d65bf9ebecae351af675ce2fd?s=90&d=mm&r=g)

##### [Redazione](https://www.securityinfo.it/author/redazione/)

##### Articoli correlati

##### Altro in questa categoria

* [![Reset password: una misura di sicurezza che diventa minaccia](https://www.securityinfo.it/wp-content/uploads/2026/04/TelefonoHacker-120x85.png)](https://www.securityinfo.it/2026/04/23/reset-password-una-misura-di-sicurezza-che-diventa-minaccia/ "Reset password: una misura di sicurezza che diventa minaccia")

  [Reset password: una misura di sicurezza...](https://www.securityinfo.it/2026/04/23/reset-passwor...