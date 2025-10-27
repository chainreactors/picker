---
title: La telemetria raccolta da Apple non è poi così anonima
url: https://www.securityinfo.it/2022/12/02/la-telemetria-raccolta-da-apple-non-e-poi-cosi-anonima/?utm_source=rss&utm_medium=rss&utm_campaign=la-telemetria-raccolta-da-apple-non-e-poi-cosi-anonima
source: Over Security - Cybersecurity news aggregator
date: 2022-12-03
fetch_date: 2025-10-04T00:25:15.028999
---

# La telemetria raccolta da Apple non è poi così anonima

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

## La telemetria raccolta da Apple non è poi così anonima

Dic 02, 2022  [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/ "Articoli scritti da Dario Orlandi")
 [News](https://www.securityinfo.it/category/news/), [Privacy](https://www.securityinfo.it/category/news/privacy-news/)
 [0](https://www.securityinfo.it/2022/12/02/la-telemetria-raccolta-da-apple-non-e-poi-cosi-anonima/#respond)

---

Il marketing di Apple sottolinea da molti anni [l’attenzione alla privacy](https://www.apple.com/it/privacy/) dell’azienda, che si schiera dalla parte degli utenti **contro le pratiche di tracciamento** e raccolta delle informazioni personali utilizzate diffusamente dalla maggioranza delle altre Big Tech, come Google o Meta.

I ricercatori di [Mysk](https://mysk.co/) hanno analizzato le comunicazioni di telemetria inviate da iOS verso i server Apple e hanno scoperto come in realtà le informazioni siano molto meno anonime di quanto dichiarato: i dati, infatti, includono un’identificazione numerica permanente e immodificabile, chiamata Directory Services Identifier (DSID), che è **collegata direttamente a informazioni personali** come il nome, il numero di telefono, la data di nascita o l’indirizzo email.

Secondo la [policy di Apple](https://www.apple.com/legal/privacy/data/it/device-analytics/), “I dati personali vengono trattati conformemente alle politiche di tutela della privacy di tipo differenziale. Tali informazioni non vengono salvate o vengono **rimosse dai resoconti** prima di essere inviate ad Apple”.

![](https://www.securityinfo.it/wp-content/uploads/2022/12/FiDbJSzX0AAYXd6-scaled.jpg)

Una schermata dei dati di telemetria inviati ai server Apple (fonte: Mysk via Twitter)

## Indifferenza alle impostazioni dell’utente

Le analisi condotte da Mysk hanno però evidenziato come il **DSID sia invece inviato ai server di Apple** nel pacchetto dati insieme a tutte le altre informazioni di telemetria. I ricercatori hanno analizzato nei dettagli le informazioni di telemetria generate da un iPhone jailbroken con iOS 14.6, riscontrando le anomalie evidenziate via [Twitter](https://twitter.com/mysk_co/status/1594515229915979776?s=20&t=8CvolWBRxabbvNdNzITTHg) e poi con un [video](https://www.youtube.com/watch?v=8JxvH80Rrcw) pubblicato su YouTube.

L’analisi ha poi coinvolto il più recente iOS 16: in questo caso, l’assenza di un jailbreak non ha consentito l’ispezione completa delle informazioni, che rimangono criptate, ma i pacchetti vengono inviati nello stesso modo, con la stessa frequenza e verso gli stessi server; non si nota nessuna variazione neppure attivando o disattivando l’opzione **Condividi dati iPhone** nelle impostazioni dedicate alla privacy.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [anonimizzazione](https://www.securityinfo.it/tag/anonimizzazione/), [Apple](https://www.securityinfo.it/tag/apple/), [iOS](https://www.securityinfo.it/tag/ios/), [iPhone](https://www.securityinfo.it/tag/iphone/), [Jailbreak](https://www.securityinfo.it/tag/jailbreak/), [Mysk](https://www.securityinfo.it/tag/mysk/), [telemetria](https://www.securityinfo.it/tag/telemetria/)

[Akamai: in aumento gli attacchi contro web app ed API](https://www.securityinfo.it/2022/12/02/akamai-attacchi-web-app-api/)
[Le sfide della cybersecurity per la tecnologia operativa](https://www.securityinfo.it/2022/12/01/cybersecurity-tecnologia-operativa/)

---

![](https://secure.gravatar.com/avatar/9ba6108fae91c2be66a7ef45ac2db49a?s=90&d=mm&r=g)

##### [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/)

##### Articoli correlati

* [![Apple rilascia una fix per una vulnerabilità di Safari già sfruttata in Chrome](https://www.securityinfo.it/wp-content/uploads/2025/07/Gemini_Generated_Image_1mvtjc1mvtjc1mvt-120x85.png)](https://www.securityinfo.it/2025/07/30/apple-rilascia-una-fix-per-una-vulnerabilita-di-safari-gia-sfruttata-in-chrome/ "Apple rilascia una fix per una vulnerabilità di Safari già sfruttata in Chrome")

  [Apple rilascia una fix per una...](https://www.securityinfo.it/2025/07/30/apple-rilascia-una-fix-per-una-vulnerabilita-di-safari-gia-sfruttata-in-chrome/ "Permanent link to Apple rilascia una fix per una vulnerabilità di Safari già sfruttata in Chrome")

  Lug 30, 2025  [0](https://www.securityinfo.it/2025/07/30/apple-rilascia-una-fix-per-una-vulnerabilita-di-safari-gia-sfruttata-in-chrome/#respond)
* [![Meta annuncia nuovi tool di sicurezza per Llama](https://www.securityinfo.it/wp-content/uploads/2025/05/124669-120x85.jpg)](https://www.securityinfo.it/2025/05/02/meta-annuncia-nuovi-tool-di-sicurezza-per-llama/ "Meta annuncia nuovi tool di sicurezza per Llama")

  [Meta annuncia nuovi tool di sicurezza...](https://www.securityinfo.it/2025/05/02/meta-annuncia-nuovi-tool-di-sicurezza-per-llama/ "Permanent link to Meta annuncia nuovi tool di sicurezza per Llama")

  Mag 02, 2025  [0](https://www.securityinfo.it/2025/05/02/meta-annuncia-nuovi-tool-di-sicurezza-per-llama/#respond)
* [![Apple risolve un bug 0-day di WebKit già sfruttato](https://www.securityinfo.it/wp-content/uploads/2025/03/2808-120x85.jpg)](https://www.securityinfo.it/2025/03/12/apple-risolve-un-bug-0-day-di-webkit-gia-sfruttato/ "Apple risolve un bug 0-day di WebKit già sfruttato")

  [Apple risolve un bug 0-day di WebKit...](https://www.securityinfo.it/2025/03/12/apple-risolve-un-bug-0-day-di-webkit-gia-sfruttato/ "Permanent link to Apple risolve un bug 0-day di WebKit già sfruttato")

  Mar 12, 2025  [0](https://www.securityinfo.it/2025/03/12/apple-risolve-un-bug-0-day-di-webkit-gia-sfruttato/#respond)
* [![Brutto momento per la crittografia in Europa: la privacy vacilla](https://www.securityinfo.it/wp-content/uploads/2025/02/Crittografia-120x85.png)](https://www.securityinfo.it/2025/02/28/brutto-momento-per-la-crittografia-in-europa-la-privacy-vacilla/ "Br...