---
title: Il plugin Social Login di WordPress soffre di una vulnerabilità critica
url: https://www.securityinfo.it/2023/06/30/il-plugin-social-login-di-wordpress-soffre-di-una-vulnerabilita-critica/?utm_source=rss&utm_medium=rss&utm_campaign=il-plugin-social-login-di-wordpress-soffre-di-una-vulnerabilita-critica
source: Securityinfo.it
date: 2023-07-01
fetch_date: 2025-10-04T11:57:00.122260
---

# Il plugin Social Login di WordPress soffre di una vulnerabilità critica

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

## Il plugin Social Login di WordPress soffre di una vulnerabilità critica

Giu 30, 2023  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2023/06/30/il-plugin-social-login-di-wordpress-soffre-di-una-vulnerabilita-critica/#respond)

---

I ricercatori di sicurezza di [Wordfence](https://www.wordfence.com/blog/2023/06/miniorange-addresses-authentication-bypass-vulnerability-in-wordpress-social-login-and-register-wordpress-plugin/) hanno individuato una v**ulnerabilità presente nei plugin di miniOrange Social Login e Register usati su WordPress e attivi su più di 30.000 siti.**

Il plugin permette di eseguire il login tramite social e di condividere contenuti [WordPress](https://www.securityinfo.it/2023/04/18/badala-injector-ha-colpito-un-milione-di-siti-wordpress/) sulla piattaforma dalla quale si è fatto l’accesso, come Facebook, LinkedIn, Twitter, Discord o Twitch.

La vulnerabilità, identificata come CVE-2023-2982, ha ricevuto un punteggio di 9,8 su 10 ed è quindi **catalogata come critica**. I plugin di WordPress si sono rivelati **vulnerabili agli attacchi di authentication bypass**: un attaccante non autenticato è in grado di accedere a qualsiasi account del sito, compreso quello di amministratore, una volta entrato in possesso delle email di registrazione.

![Wordpress plugin - Credits: mishoo- Depositphotos](https://www.securityinfo.it/wp-content/uploads/2023/06/Depositphotos_18235681_L.jpg)

Credits: mishoo- Depositphotos

Nel dettaglio, il problema sta nel modo in cui viene memorizzata la **chiave di cifratura** per le informazioni di login: nelle versioni vulnerabili del plugin, **la chiave è codificata direttamente nel codice.** Una volta entrati in possesso della chiave, gli attaccanti possono creare delle richieste ad hoc contenenti l’email della vittima per bypassare la fase di autenticazione e compromettere l’intero sito.

**La vulnerabilità colpisce la versione 7.6.4 dei plugin e tutte le precedenti.** Wordfence ha avvertito miniOrange della vulnerabilità e la società ha rilasciato una prima patch il 12 giugno, nella quale era però presente un altro bug; due giorni dopo, il 14 giugno, miniOrange ha rilasciato l’**aggiornamento definitivo nella versione 7.6.5.**

Wordfence e miniOrange invitano gli utenti WordPress a controllare la presenza dei plugin ed eventualmente aggiornarlo all’ultima versione rilasciata. Gli utenti Wordfence Premium, Wordfence Care e Wordfence Response dovrebbero già aver ricevuto un firewall per proteggersi dalla vulnerabilità, ma è comunque fondamentale aggiornare la versione dei plugin il prima possibile.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [autenticazione](https://www.securityinfo.it/tag/autenticazione/), [authentication bypass](https://www.securityinfo.it/tag/authentication-bypass/), [miniorange](https://www.securityinfo.it/tag/miniorange/), [social login](https://www.securityinfo.it/tag/social-login/), [Wordfence](https://www.securityinfo.it/tag/wordfence/), [WordPress](https://www.securityinfo.it/tag/wordpress/)

[ThirdEye, un nuovo infostealer russo che migliora a vista d'occhio](https://www.securityinfo.it/2023/06/30/thirdeye-un-nuovo-infostealer-russo-che-migliora-a-vista-docchio/)
[Nuove tecniche di social engineering sfruttano le notifiche del browser](https://www.securityinfo.it/2023/06/29/nuove-tecniche-di-social-engineering-sfruttano-le-notifiche-del-browser/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Milioni di account Google “defunti” sono vulnerabili a un bug di OAuth](https://www.securityinfo.it/wp-content/uploads/2025/01/google-1762248_1920-120x85.png)](https://www.securityinfo.it/2025/01/15/milioni-di-account-google-defunti-sono-vulnerabili-a-un-bug-di-oauth/ "Milioni di account Google “defunti” sono vulnerabili a un bug di OAuth")

  [Milioni di account Google...](https://www.securityinfo.it/2025/01/15/milioni-di-account-google-defunti-sono-vulnerabili-a-un-bug-di-oauth/ "Permanent link to Milioni di account Google “defunti” sono vulnerabili a un bug di OAuth")

  Gen 15, 2025  [0](https://www.securityinfo.it/2025/01/15/milioni-di-account-google-defunti-sono-vulnerabili-a-un-bug-di-oauth/#respond)
* [![Un gruppo di ricercatori ha violato l’MFA di Microsoft in un’ora](https://www.securityinfo.it/wp-content/uploads/2024/12/cybersecurity-7119401_1920-120x85.jpg)](https://www.securityinfo.it/2024/12/12/ricercatori-violano-mfa-di-microsoft-in-unora/ "Un gruppo di ricercatori ha violato l’MFA di Microsoft in un’ora")

  [Un gruppo di ricercatori ha violato...](https://www.securityinfo.it/2024/12/12/ricercatori-violano-mfa-di-microsoft-in-unora/ "Permanent link to Un gruppo di ricercatori ha violato l’MFA di Microsoft in un’ora")

  Dic 12, 2024  [0](https://www.securityinfo.it/2024/12/12/ricercatori-violano-mfa-di-microsoft-in-unora/#respond)
* [![Una vulnerabilità di un plugin di WordPress mette a rischio più di 4 milioni di siti](https://www.securityinfo.it/wp-content/uploads/2024/11/wordpress-923188_1920-120x85.jpg)](https://www.securityinfo.it/2024/11/18/una-vulnerabilita-di-un-plugin-di-wordpress-mette-a-rischio-piu-di-4-milioni-di-siti/ "Una vulnerabilità di un plugin di WordPress mette a rischio più di 4 milioni di siti")

  [Una vulnerabilità di un plugin di...](https://www.securityinfo.it/2024/11/18/una-vulnerabilit...