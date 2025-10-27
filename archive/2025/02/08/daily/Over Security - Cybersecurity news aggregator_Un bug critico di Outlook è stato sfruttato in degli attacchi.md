---
title: Un bug critico di Outlook è stato sfruttato in degli attacchi
url: https://www.securityinfo.it/2025/02/07/un-bug-critico-di-outlook-e-stato-sfruttato-in-degli-attacchi/
source: Over Security - Cybersecurity news aggregator
date: 2025-02-08
fetch_date: 2025-10-06T20:40:08.986149
---

# Un bug critico di Outlook è stato sfruttato in degli attacchi

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

## Di nuovo, una vecchia vulnerabilità di Outlook viene sfruttata dai criminali

Feb 07, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/02/07/un-bug-critico-di-outlook-e-stato-sfruttato-in-degli-attacchi/#respond)

---

**Un bug critico e noto di Outlook è stato sfruttato in alcuni attacchi**: a dirlo è stata la [CISA](https://www.cisa.gov/news-events/alerts/2025/02/06/cisa-adds-five-known-exploited-vulnerabilities-catalog), aggiungendo la vulnerabilità alla lista di quelle attivamente utilizzate nelle campagne di cyberattacchi.

La vulnerabilità, tracciata come **[CVE-2024-21413](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2024-21413)**, era stata individuata dai ricercatori di [Check Point](https://research.checkpoint.com/2024/the-risks-of-the-monikerlink-bug-in-microsoft-outlook-and-the-big-picture/) un anno fa, proprio a febbraio. Si tratta di un bug di **validazione errata degli input** quando un utente apre con Outlook un’email che contiene dei link malevoli.

![bug Outlook](https://www.securityinfo.it/wp-content/uploads/2025/02/digital-8280790_1920.jpg)

Il client di posta di Microsoft utilizza un meccanismo di protezione che, quando l’utente prova ad aprire un link non riconosciuto, mostra un avviso di sicurezza e richiede la conferma specifica da parte dell’utente per navigare su link.

Modificando però l’indirizzo, in particolare con l’uso del protocollo `file://` per l’apertura di documenti remoti, e aggiungendo un punto esclamativo in fondo al link, insieme a del testo randomico, è possibile eludere le restrizioni di Outlook e **far accedere l’utente alla risorsa remota senza approvazione esplicita.**

Dopo che l’utente naviga al link inserito, gli attaccanti possono **sottrargli le credenziali NTLM** ed **eseguire codice arbitrario** sfruttando documenti Office malevoli, creati appositamente per lo scopo.

La vulnerabilità colpisce Outlook 2016 e Outlook 2019, ma anche diversi prodotti della suite Office come LTSC 2021 e Microsoft 365 Apps for Enterprise.

Microsoft aveva rilasciato il fix per la vulnerabilità pochi giorni dopo aver ricevuto l’avviso da Check Point e al tempo non c’erano indicazioni su exploit che la sfruttavano; ieri invece la CISA ha confermato che **il bug è stato usato in alcuni attacchi**, anche se non ha specificato né le campagne in cui è stato sfruttato, né se ci sono informazioni sull’identità degli attaccanti.

“***Questi tipi di vulnerabilità sono vettori di attacco frequenti per i cyberattaccanti** e rappresentano rischi significativi per l’organizzazione federal*e” ha specificato la CISA nell’avviso, invitando le compagnie ad **aggiornare il prima possibile i prodotti vulnerabili** con le patch di Microsoft.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Check Point](https://www.securityinfo.it/tag/check-point/), [CISA](https://www.securityinfo.it/tag/cisa/), [link malevoli](https://www.securityinfo.it/tag/link-malevoli/), [Outlook](https://www.securityinfo.it/tag/outlook/), [validazione impropria degli input](https://www.securityinfo.it/tag/validazione-impropria-degli-input/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[Truffa milionaria a nome del Ministro della Difesa : c'è deepfake o no? Non importa...](https://www.securityinfo.it/2025/02/07/truffa-milionaria-a-nome-del-ministro-della-difesa-ce-deepfake-o-no-non-importa/)
[Silent Lynx: il gruppo APT torna all'attacco contro Kyrgyzstan e Turkmenistan](https://www.securityinfo.it/2025/02/06/silent-lynx-il-gruppo-apt-torna-allattacco-contro-kyrgyzstan-e-turkmenistan/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_d4x8rid4x8rid4x8-120x85.png)](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  [Firewall Cisco sotto attacco: una nuova...](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Permanent link to Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  Set 29, 2025  [0](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/#respond)
* [![Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.](https://www.securityinfo.it/wp-content/uploads/2025/09/ai-generated-9053184_1920-120x85.jpg)](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/ "Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.")

  [Attaccanti sfruttano un bug di...](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/ "Permanent link to Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.")

  Set 24, 2025  [0](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/#respond)
* [![Una vulnerabilità critica di SAP S/4HANA è sta...