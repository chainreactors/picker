---
title: Un gruppo di ricercatori ha violato l’MFA di Microsoft in un’ora
url: https://www.securityinfo.it/2024/12/12/ricercatori-violano-mfa-di-microsoft-in-unora/
source: Over Security - Cybersecurity news aggregator
date: 2024-12-13
fetch_date: 2025-10-06T19:42:58.697742
---

# Un gruppo di ricercatori ha violato l’MFA di Microsoft in un’ora

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

## Un gruppo di ricercatori ha violato l’MFA di Microsoft in un’ora

Dic 12, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Hacking](https://www.securityinfo.it/category/news/hacking-news/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2024/12/12/ricercatori-violano-mfa-di-microsoft-in-unora/#respond)

---

Il team di sicurezza di Oasis ha scoperto una **vulnerabilità critica nell’implementazione di Microsoft dell’MFA** che consente a un attaccante di ottenere l’accesso all’account di un utente, comprese le email, i file di OneDrive, le chat di Teams e l’ambiente Azure Cloud.

Tal Hason, ricercatore del team, [ha spiegato](https://www.oasis.security/resources/blog/oasis-security-research-team-discovers-microsoft-azure-mfa-bypass) che realizzare l’exploit è stato molto semplice: **il gruppo ci ha messo solo un’ora**; inoltre, l’exploit non necessita dell’interazione utente e non ha generato alcun avviso di sicurezza per l’account.

![MFA Microsoft](https://www.securityinfo.it/wp-content/uploads/2024/12/cybersecurity-7119401_1920.jpg)

Quando l’utente naviga sulla pagina di login dei servizi Microsoft, gli viene assegnato un identificatore di sessione. Tra i metodi MFA supportati da Microsoft, c’è anche l’**uso di un’applicazione (un authenticator) che genera un codice di 6 cifre per completare il processo di login.** Il meccanismo supporta fino a 10 tentativi per una singola sessione, poi blocca l’accesso.

I ricercatori di Oasis hanno creato in poco tempo nuove sessioni per gli account e liste di codici; il numero elevato di tentativi ha esaurito il numero di opzioni per un codice a 6 cifre (1 milione di possibilità). Il team ha eseguito numerosi tentativi contemporaneamente e per di più **i proprietari degli account non hanno ricevuto alcun avviso per il numero di tentativi falliti.**

Un altro aspetto da tenere in considerazione è che **il codice TOTP generato è valido per più di 30 secondi**, l’impostazione base per applicazioni di autenticazione di questo tipo. I test di Oasis hanno dimostrato che nel caso di Microsoft, la tolleranza era di circa 3 minuti per ogni singolo codice; ciò permette di eseguire un numero di tentativi 6 volte superiore alla norma.

**“*Dato il tasso consentito, avevamo il 3% di possibilità di indovinare il codice entro l’intervallo di tempo esteso*“** ha spiegato Hason. “*Dopo 24 sessioni di questo tipo (circa 70 minuti), un attaccante avrebbe già superato il 50% di probabilità di ottenere un codice valido*“. Il team ha infatti applicato questo exploit con successo diverse volte.

![](https://www.securityinfo.it/wp-content/uploads/2024/12/675065c871bd7251153970ae_AD_4nXd343u0I_tqk0DNG60D3OqQow8PArvr8VqXKbJbH4rMSf9W27tco9Puj8-dH3_Sy-OHGQ_EnFFnBnAts_9zHWuKgPeVfpvKnkbiMklwhrJLayCc5M0AYN9k9yEb79HjqTwKrrscIw8f5hJVzP_lzk4.gif)

Dopo la scoperta della falla, Oasis ha contattato subito Microsoft e le due compagnie hanno collaborato per risolvere il problema. “*Anche se i dettagli specifici delle modifiche sono confidenziali, **possiamo confermare che Microsoft ha introdotto un limite più stringente ch entra in gioco dopo un certo numero di tentativi falliti**; il limite dura circa mezza giornata*” ha spiegato Hason.

Il team ha infine ricordato le buone pratiche per proteggersi dagli attacchi di furto di account, a cominciare dall’**abilitazione dell’MFA** per tutti gli utenti, soprattutto quelli con accesso ai dati critici. Oltre a ciò, è necessario **cambiare regolarmente la password** e implementare **meccanismi di alerting** di accesso all’account che mettano in evidenza gli avvisi di accessi effettuati correttamente.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [autenticazione](https://www.securityinfo.it/tag/autenticazione/), [exploit MFA](https://www.securityinfo.it/tag/exploit-mfa/), [MFA](https://www.securityinfo.it/tag/mfa/), [Microsoft](https://www.securityinfo.it/tag/microsoft/), [Oasis](https://www.securityinfo.it/tag/oasis/), [OTP](https://www.securityinfo.it/tag/otp/)

[Cybersecurity in Italia: cresce la sensibilità al tema, ma serve investire nella formazione](https://www.securityinfo.it/2024/12/13/cybersecurity-in-italia-cresce-la-sensibilita-al-tema-ma-serve-investire-nella-formazione/)
[ESET scopre il primo bootkit UEFI per Linux](https://www.securityinfo.it/2024/12/11/eset-scopre-il-primo-bootkit-uefi-per-linux/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![SonicWall: Akira non sfrutta uno zero-day, ma una falla del 2024](https://www.securityinfo.it/wp-content/uploads/2025/08/Firewall-8-ago-2025CG-120x85.png)](https://www.securityinfo.it/2025/08/08/sonicwall-akira-non-sfrutta-uno-zero-day-ma-una-falla-del-2024/ "SonicWall: Akira non sfrutta uno zero-day, ma una falla del 2024")

  [SonicWall: Akira non sfrutta uno...](https://www.securityinfo.it/2025/08/08/sonicwall-akira-non-sfrutta-uno-zero-day-ma-una-falla-del-2024/ "Permanent link to SonicWall: Akira non sfrutta uno zero-day, ma una falla del 2024")

  Ago 08, 2025  [0](https://www.securityinfo.it/2025/08/08/sonicwall-akira-non-sfrutta-uno-zero-day-ma-una-falla-del-2024/#respond)
* [![Secret Blizzard attacca le ambasciate straniere a Mosca tramite gli ISP](https://www.securityinfo.it/wp-content/uploads/2025/08/Gemini_Generated_Image_jk74qwjk74qwjk74-120x85.png)](https://www.securityinfo.it/2025/08/01/secret-blizzard-attacca-le-ambasciate-straniere-a-mosca-tramite-gli-isp/ "Secret Blizzard ...