---
title: Le nuove tecniche d’attacco superano l’autenticazione multifattore
url: https://www.securityinfo.it/2023/03/08/autenticazione-multifattore-attacchi/?utm_source=rss&utm_medium=rss&utm_campaign=autenticazione-multifattore-attacchi
source: Over Security - Cybersecurity news aggregator
date: 2023-03-09
fetch_date: 2025-10-04T09:02:55.941391
---

# Le nuove tecniche d’attacco superano l’autenticazione multifattore

Aggiornamenti recenti Ottobre 3rd, 2025 6:09 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)
* [Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)
* [Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/)
* [Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/)

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

## Le nuove tecniche d’attacco superano l’autenticazione multifattore

Mar 08, 2023  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Attacchi](https://www.securityinfo.it/category/approfondimenti/attacchi/), [Hacking](https://www.securityinfo.it/category/approfondimenti/hacking/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2023/03/08/autenticazione-multifattore-attacchi/#respond)

---

**Per quanto l’autenticazione multifattore (MFA) sia considerata sicura, non protegge del tutto dagli attaccanti**, che continuano ad affinare le proprie tecniche per superare i controlli della sicurezza multi-factor. Come ha riportato **[Robert Lemos di DarkReading](https://www.darkreading.com/threat-intelligence/cyberattackers-double-down-bypassing-mfa)**, i cybercriminali si sono adattati alle ultime misure di sicurezza sviluppando nuove tecniche di attacco.

## Le nuove tecniche contro l’autenticazione multifattore

Di fronte a profili personali e lavorativi sempre più difficili da compromettere, **gli attaccanti hanno sviluppato nuove tecniche per superare l’autenticazione a più fattori.** Una di queste sfrutta l’anello in assoluto più debole della catena di protezione: l’essere umano. Durante un attacco **MFA flooding (o fatigue) l’attaccante tenta ripetutamente di loggarsi nell’account** **inondando la vittima di notifiche push**, nella speranza che clicchi su una di queste e consenta l’accesso.

Un altro attacco di social engineering consiste nel **richiedere un reset dell’account al supporto tecnico, fingendosi la vittima**, così da ottenere le nuove credenziali e farsi inviare l’OTP sul proprio dispositivo.

![autenticazione fattori](https://www.securityinfo.it/wp-content/uploads/2023/03/Depositphotos_631351850_L.jpg)

tete\_escape – Depositphotos

Anche il **browser** è diventato uno dei veicoli preferiti dai cybercriminali per sferrare nuovi attacchi: dopo che l’utente si è loggato sul suo account, **un attaccante può collezionare i cookie di sessione e utilizzare quello di autenticazione per effettuare il login.** Questo tipo di attacco sfrutta in maniera indiretta la sessione utente, senza neanche avere a che fare coi controlli di sicurezza.

Infine, anche **attacchi di tipo proxy o man-in-the-middle si possono rivelare molto efficaci**: gli attaccanti possono **compromettere l’intera infrastruttura di comunicazione tra il servizio e il server per ottenere le informazioni di login** in tempo reale. Si tratta, questa, di una tecnica che permette di superare la maggior parte dei metodi MFA.

## Contrastare i nuovi attacchi

Nonostante le misure di autenticazione siano migliorate, le imprese non possono stare completamente tranquille. Per il momento, la soluzione migliore contro questi attacchi è **scegliere un dispositivo fisico per l’autenticazione**, che si tratti di una chiave hardware o di un device di riconoscimento biometrico.

**La vera difficoltà, in questo caso, sta nel distribuire l’hardware tra i dipendenti**, soprattutto nelle realtà dove prevale il lavoro remoto, ed essere in grado di gestire l’eventuale perdita dei dispositivi. Bisogna considerare però che **gli attaccanti potrebbero comunque riuscire a ottenere il controllo dell’account sfruttando la tecnica del reset dell’account** o richiedendo un nuovo device, affermando di averlo perso. Se il supporto tecnico acconsente a proseguire col processo di reset, l’attaccante può superare facilmente i controlli di sicurezza.

![autenticazione fattori](https://www.securityinfo.it/wp-content/uploads/2023/03/Depositphotos_548126904_L.jpg)

ArtemisDiana – Depositophotos

Gli utenti non sono mai completamente al sicuro. Come si può contrastare il problema, quindi? Investire su metodi di autenticazione biometrici o con chiavi hardware rimane comunque la scelta migliore per mettere in difficoltà gli attaccanti, ma al contempo bisogna **formare adeguatamente gli utenti contro i tentativi di phishing** e inserire **step di autenticazione più stringenti per le richieste di reset** degli account.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [autenticazione a due fattori](https://www.securityinfo.it/tag/autenticazione-a-due-fattori/), [Man in the Middle](https://www.securityinfo.it/tag/man-in-the-middle/), [MFA](https://www.securityinfo.it/tag/mfa/), [MFA fatigue](https://www.securityinfo.it/tag/mfa-fatigue/), [multi factor authentication](https://www.securityinfo.it/tag/multi-factor-authentication/), [Phishing](https://www.securityinfo.it/tag/phishing/), [social engineering](https://www.securityinfo.it/tag/social-engineering/)

[Gli attacchi in Italia hanno toccato un nuovo massimo nel 2022](https://www.securityinfo.it/2023/03/08/gli-attacchi-in-italia-hanno-toccato-un-nuovo-massimo-nel-2022/)
[TPM 2.0: due vulnerabilità permettono di sovrascrivere le chiavi crittografiche](https://www.securityinfo.it/2023/03/07/tpm-vulnerabilita-chiavi-crittografiche/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Campagne basate su installer ScreenConnect distribuiscono RAT multipli](https://www.securityinfo.it/wp-content/uploads/2025/09/ai-generated-8976964_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/09/22/campagne-basate-su-installer-screenconnect-distribuiscono-rat-multipli-lanalisi-di-acronis-tru/ "Campagne basate su installer ScreenConnect distribuiscono RAT multipli")

  [Campagne basate su installer...](https://www.securityinfo.it/2025/09/22/campagne-basate-su-installer-screenconnect-distribuiscono-rat-multipli-lanalisi-di-acronis-tru/ "Permanent link to Campagne bas...