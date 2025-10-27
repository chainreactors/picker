---
title: Una nuova campagna sfrutta Selenium Grid per il mining di Monero
url: https://www.securityinfo.it/2024/07/29/una-nuova-campagna-sfrutta-selenium-grid-per-il-mining-di-monero/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-30
fetch_date: 2025-10-06T17:46:09.552992
---

# Una nuova campagna sfrutta Selenium Grid per il mining di Monero

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

## Una nuova campagna sfrutta Selenium Grid per il mining di Monero

Lug 29, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2024/07/29/una-nuova-campagna-sfrutta-selenium-grid-per-il-mining-di-monero/#respond)

---

I ricercatori di Wiz hanno scoperto una nuova campagna in corso che sfrutta i servizi **Selenium Grid** p**er effettuare mining di Monero**. Soprannominata “**SeleniumGreed**“, gli attacchi fanno leva su server mal configurati dei servizi per eseguire un cryptominer.

![Selenium Grid](https://www.securityinfo.it/wp-content/uploads/2024/07/cyber-4747175_1920.jpg)

Pixabay

Grid è un componente della suite Selenium che offre un API che consente di eseguire e interagire con browser web sulle macchine registrare. Insieme a IDE, Builder e WebDriver permettere di gestire in maniera automatizzata i browser ed è **usato principalmente come framework di testing.**

I ricercatori spiegano che **poiché Grid è pensato solo per l’utilizzo nelle reti aziendali interne, non offre controlli di sicurezza**. “*Idealmente, questi servizi non dovrebbero mai essere esposti su Internet*” scrive il team di Wiz Research. Il componente non ha nemmeno meccanismi di autenticazione: qualsiasi utente con accesso web all’hub di gestione può interagire con le singole macchine registrate, il che comporta un **rischio di sicurezza molto elevato** se il servizio vien eseguito su una macchina connessa alla rete pubblica e con protezione inadeguata.

Inizialmente gli attaccanti inviano una richiesta all’hub di Grid vulnerabile contenente uno script, il quale a sua volte contiene un payload decodificato in base64. Il payload in questione **crea una reverse shell per eseguire ulteriori comandi**, tra i quali il download e l’esecuzione del miner.

Il miner è **XMRig**, un software open-source di cryptomining molto comune tra i cyberattaccanti, che viene fatto eseguire in background. Stando all’analisi dei ricercatori, il gruppo dietro quest’ultima campagna sarebbe attivo da più di un anno.

Nella documentazione di Grid, Selenium [sottolinea](https://www.selenium.dev/documentation/grid/getting_started/#warning) l’importanza di **non esporre il servizio sul web pubblico** a causa dell’assenza di meccanismi di sicurezza, elencando i rischi che ne conseguirebbero, ma evidentemente l’avviso non è stato recepito correttamente da tutte le organizzazioni.

Nella campagna individuata dai ricercatori, gli attaccant**i hanno usato una vecchia versione di Selenium** (v.3.141.59) per eseguire comandi da remoto, ma il team ha confermato che è possibile eseguire lo stesso attacco anche nelle ultime versioni; per questo è probabile che la campagna si evolva per colpire le release più nuove.

Aggiornare il software in questo caso è inutile: poiché Grid è per sua natura vulnerabile, per proteggersi dagli attacchi è consigliato o rendere le macchine raggiungibili solo da rete interna, oppure **implementare controlli di sicurezza mirati** per restringere gli accessi e **impostare meccanismi di autenticazione robusti.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [autenticazione](https://www.securityinfo.it/tag/autenticazione/), [cryptomining](https://www.securityinfo.it/tag/cryptomining/), [mining di cryptovalute](https://www.securityinfo.it/tag/mining-di-cryptovalute/), [Monero](https://www.securityinfo.it/tag/monero/), [Selenium](https://www.securityinfo.it/tag/selenium/), [Selenium Grid](https://www.securityinfo.it/tag/selenium-grid/)

[Stargazer Goblin ha creato 3.000 account GitHub per diffondere malware](https://www.securityinfo.it/2024/07/30/stargazer-goblin-ha-creato-3-000-account-github-per-diffondere-malware/)
[CERT-AGID 20 – 26 luglio: 39 campagne malevole e nuove combolist su Telegram](https://www.securityinfo.it/2024/07/29/cert-agid-20-26-luglio-39-campagne-malevole-e-nuove-combolist-su-telegram/)

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
* [![Trasferimento di passkey e credenziali tra provider: la proposta della FIDO Alliance](http...