---
title: I cybercriminali prendono di mira l’autenticazione multi-fattore
url: https://www.securityinfo.it/2024/09/20/i-cybercriminali-prendono-di-mira-lautenticazione-multi-fattore/?utm_source=rss&utm_medium=rss&utm_campaign=i-cybercriminali-prendono-di-mira-lautenticazione-multi-fattore
source: Securityinfo.it
date: 2024-09-21
fetch_date: 2025-10-06T18:28:36.553174
---

# I cybercriminali prendono di mira l’autenticazione multi-fattore

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

## I cybercriminali prendono di mira l’autenticazione multi-fattore

Set 20, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Attacchi](https://www.securityinfo.it/category/approfondimenti/attacchi/), [Attacchi](https://www.securityinfo.it/category/news/attachi/), [Hacking](https://www.securityinfo.it/category/approfondimenti/hacking/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2024/09/20/i-cybercriminali-prendono-di-mira-lautenticazione-multi-fattore/#respond)

---

Secondo il [report del primo trimestre 2024](https://blog.talosintelligence.com/talos-ir-quarterly-trends-q1-2024/) di **Cisco Talos Incident Response** (Talos IR) i cybercriminali stanno prendendo di mira le debolezze dell’autenticazione multi-fattore: l’analisi evidenzia che **quasi la metà di tutti gli incidenti di sicurezza hanno riguardato la MFA.**

Nel 25% dei casi, la causa è stata l’**accettazione da parte degli utenti di notifiche push MFA fraudolente**, mentre nel 21% dei casi l’implementazione dell’autenticazione multi-fattore non era corretta.

Nel caso delle notifiche push non autorizzate, i cybercriminali sommergono gli utenti con avvisi MFA finché **le vittime, esasperate dai messaggi, accettano la richiesta e consentono l’accesso**. Cisco Duo, l’azienda di Cisco che si occupa di servizi MFA, ha rilevato, da giugno 2023 a maggio 2024, circa 15.000 attacchi basati su notifiche push. L’analisi riporta inoltre che questi attacchi avvengono principalmente all’inizio della giornata lavorativa, quando gli utenti si autenticano ai sistemi aziendali.

![autenticazione multi fattore](https://www.securityinfo.it/wp-content/uploads/2024/09/hands-1853302_1920.jpg)

Pixabay

Oltre alle notifiche push, per superare l’MFA i cybercriminali sfruttano i **token di sessione rubati** o usano **tecniche di ingegneria sociale** fingendosi qualcuno che la vittima conosce (come un collega del reparto IT) per ottenere le sue credenziali.

In alcuni casi **gli attaccanti prendono di mira un fornitore dell’azienda** per accedere agli account usando un dispositivo compromesso, oppure compromettono un singolo endpoint per **disattivare del tutto la protezione MFA**. Cisco Talos IR ha inoltre individuato attacchi che usano applicazioni software provenienti dal dark web che utilizzano script per disabilitare gli strumenti di sicurezza.

Per implementare correttamente l’MFA, i ricercatori di Cisco Talos consigliano di **abilitare il number matching** per avere un ulteriore livello di sicurezza e impedire agli utenti di approvare notifiche push dannose. È opportuno inoltre **configurare un alert per l’autenticazione**, in modo da individuare facilmente anomalie e modifiche alle policy dell’MFA, e **formare gli utenti** per aggiornarli sui pericoli a cui sono esposti.

**L’MFA andrebbe in ogni caso implementata per tutti i servizi critici**, compresi quelli di accesso remoto e gestione dell’accesso all’identità.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [autenticazione multi-fattore](https://www.securityinfo.it/tag/autenticazione-multi-fattore/), [Cisco Talos](https://www.securityinfo.it/tag/cisco-talos/), [compromissione](https://www.securityinfo.it/tag/compromissione/), [ingegneria sociale](https://www.securityinfo.it/tag/ingegneria-sociale/), [MFA](https://www.securityinfo.it/tag/mfa/), [notifiche push](https://www.securityinfo.it/tag/notifiche-push/)

[CERT-AGID 14 – 20 settembre: 778 IoC e una campagna di phishing che sfrutta lo SPID](https://www.securityinfo.it/2024/09/23/cert-agid-14-20-settembre-778-ioc-phishing-spid/)
[Il costo di un cyberattacco va oltre le perdite finanziarie dirette](https://www.securityinfo.it/2024/09/19/il-costo-di-un-cyberattacco-va-oltre-le-perdite-finanziarie-dirette/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Static Tundra sfrutta una vecchia vulnerabilità Cisco per spionaggio](https://www.securityinfo.it/wp-content/uploads/2025/08/StaticTundra_21-ago-2025CG-120x85.png)](https://www.securityinfo.it/2025/08/21/static-tundra-sfrutta-una-vecchia-vulnerabilita-cisco-per-spionaggio/ "Static Tundra sfrutta una vecchia vulnerabilità Cisco per spionaggio")

  [Static Tundra sfrutta una vecchia...](https://www.securityinfo.it/2025/08/21/static-tundra-sfrutta-una-vecchia-vulnerabilita-cisco-per-spionaggio/ "Permanent link to Static Tundra sfrutta una vecchia vulnerabilità Cisco per spionaggio")

  Ago 21, 2025  [0](https://www.securityinfo.it/2025/08/21/static-tundra-sfrutta-una-vecchia-vulnerabilita-cisco-per-spionaggio/#respond)
* [![SonicWall: Akira non sfrutta uno zero-day, ma una falla del 2024](https://www.securityinfo.it/wp-content/uploads/2025/08/Firewall-8-ago-2025CG-120x85.png)](https://www.securityinfo.it/2025/08/08/sonicwall-akira-non-sfrutta-uno-zero-day-ma-una-falla-del-2024/ "SonicWall: Akira non sfrutta uno zero-day, ma una falla del 2024")

  [SonicWall: Akira non sfrutta uno...](https://www.securityinfo.it/2025/08/08/sonicwall-akira-non-sfrutta-uno-zero-day-ma-una-falla-del-2024/ "Permanent link to SonicWall: Akira non sfrutta uno zero-day, ma una falla del 2024")

  Ago 08, 2025  [0](https://www.securityinfo.it/2025/08/08/sonicwall-akira-non-sfrutta-uno-zero-day-ma-una-falla-del-2024/#respond)
* [![PoisonSeed è riuscito ad aggirare la protezione FIDO](https://www.securityinfo.it/wp-content/uploads/2025/07/Gemini_Generated_Image_ud7ej8ud7ej8ud7e-120x85.png)](https://www.securityinfo.i...