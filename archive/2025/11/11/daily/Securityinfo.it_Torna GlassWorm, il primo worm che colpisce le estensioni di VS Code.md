---
title: Torna GlassWorm, il primo worm che colpisce le estensioni di VS Code
url: https://www.securityinfo.it/2025/11/11/torna-glassworm-il-primo-worm-che-colpisce-le-estensioni-di-vs-code/?utm_source=rss&utm_medium=rss&utm_campaign=torna-glassworm-il-primo-worm-che-colpisce-le-estensioni-di-vs-code
source: Securityinfo.it
date: 2025-11-11
fetch_date: 2025-11-12T03:12:56.901090
---

# Torna GlassWorm, il primo worm che colpisce le estensioni di VS Code

Aggiornamenti recenti Novembre 11th, 2025 5:59 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Torna GlassWorm, il primo worm che colpisce le estensioni di VS Code](https://www.securityinfo.it/2025/11/11/torna-glassworm-il-primo-worm-che-colpisce-le-estensioni-di-vs-code/)
* [Knownsec colpita da un catastrofico breach: esposti oltre 12.000 documenti sensibili](https://www.securityinfo.it/2025/11/10/knownsec-colpita-da-un-catastrofico-breach-esposti-oltre-12-000-documenti-sensibili/)
* [CERT-AGID 1–7 novembre: phishing su Banca d’Italia e Agenzia delle Entrate](https://www.securityinfo.it/2025/11/10/cert-agid-1-7-novembre-phishing-su-banca-ditalia-e-agenzia-delle-entrate/)
* [In aumento gli attacchi russi e lo spionaggio contro Ucraina ed Europa. Il report di ESET](https://www.securityinfo.it/2025/11/07/in-aumento-gli-attacchi-russi-e-lo-spionaggio-contro-ucraina-ed-europa-il-report-di-eset/)
* [Appalti nel settore cyber, premi a chi sceglie le soluzioni di Paesi NATO e terzi. Tra questi anche Israele](https://www.securityinfo.it/2025/11/06/appalti-nel-settore-cyber-premi-a-chi-sceglie-le-soluzioni-di-paesi-nato-e-terzi-tra-questi-anche-israele/)

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

## Torna GlassWorm, il primo worm che colpisce le estensioni di VS Code

Nov 11, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/11/11/torna-glassworm-il-primo-worm-che-colpisce-le-estensioni-di-vs-code/#respond)

---

I ricercatori di Koi Security [hanno segnalato](https://www.koi.ai/blog/glassworm-returns-new-wave-openvsx-malware-expose-attacker-infrastructure) il ritorno di **GlassWorm**, il **primo worm che colpisce le estensioni di VS Code sul marketplace OpenVSX**.

Il worm era stato individuato per la prima volta quasi tre settimane fa dalla compagnia in centinaia di pacchetti software open-source. Una volta installato sui sistemi, il malware si autoreplica in altri progetti modificando i file di configurazione delle estensioni. Il worm è particolarmente difficile da contrastare perché utilizza **tecniche di offuscamento avanzate**, infettando il codice senza essere individuato.

Per propagarsi nella supply chain, GlassWorm individua e raccoglie le credenziali NPM, Git e GitHub, usandole poi per compromettere altri pacchetti ed estensioni. Tra le capacità più significative del worm ci sono il deploy di server proxy SOCKS sulle macchine infettate e l’installazione di server VCN per l’accesso remoto ai dispositivi.

![GlassWorm](https://www.securityinfo.it/wp-content/uploads/2025/11/Gemini_Generated_Image_jeouo0jeouo0jeou.png)

Il 21 ottobre, pochi giorni dopo la segnalazione, OpenVSX  aveva comunicato che la problematica era stata risolta; il 6 novembre, però, il team di Koi Security ha individuato una nuova ondata di infezioni del worm. Nel dettaglio, il malware è stato individuato in ai-driven-dev.ai-driven-dev, adhamu.history-in-sublime-merge e yasuyuky.transient-emacs. L’impatto stimato è di circa **10.000 infezioni aggiuntive.**

I ricercatori di Koi Security sono riusciti a individuare un endpoint esposto sul server degli attaccanti ed esfiltrare dati dalla loro architettura. Dalle informazioni reperite è emerso che **le vittime del worm sono diffuse in tutto il mondo**; tra queste ci sono sia sviluppatori indipendenti che organizzazioni, compresa un’**entità governativa del Medio Oriente**.

“*Non si tratta di vittime ipotetiche. Si tratta di organizzazioni reali e persone reali le cui credenziali sono state raccolte, i cui computer potrebbero essere utilizzati come infrastruttura proxy criminale e le cui reti interne potrebbero essere già state compromesse*” avvertono i ricercatori.

Dai dati trovati nei server il team di Koi Security ha scoperto che **gli attaccanti parlano il russo** e che usano RedExt, un’estensione browser open-source per il framework C2. I ricercatori sono riusciti inoltre a entrare in possesso degli user ID di diverse piattaforme di messaggistica e di scambio di criptovalute degli attaccanti.

“*GlassWorm è un esempio del perché **la visibilità e la governance dell’intera catena di fornitura del software non sono più opzionali***” sottolineano i ricercatori. “*Quando il malware può essere letteralmente invisibile, quando i worm possono auto-propagarsi attraverso credenziali rubate, quando l’infrastruttura di attacco non può essere smantellata, gli strumenti di sicurezza tradizionali non sono sufficienti*“.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [attacco supply chain](https://www.securityinfo.it/tag/attacco-supply-chain/), [autopropagazione](https://www.securityinfo.it/tag/autopropagazione/), [extensioni](https://www.securityinfo.it/tag/extensioni/), [GlassWorm](https://www.securityinfo.it/tag/glassworm/), [VSCode](https://www.securityinfo.it/tag/vscode/), [Worm](https://www.securityinfo.it/tag/worm/)

[Knownsec colpita da un catastrofico breach: esposti oltre 12.000 documenti sensibili](https://www.securityinfo.it/2025/11/10/knownsec-colpita-da-un-catastrofico-breach-esposti-oltre-12-000-documenti-sensibili/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Un attacco supply chain ha compromesso oltre 40 pacchetti NPM](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_px0h5ppx0h5ppx0h-120x85.png)](https://www.securityinfo.it/2025/09/16/un-attacco-supply-chain-ha-compromesso-oltre-40-pacchetti-npm/ "Un attacco supply chain ha compromesso oltre 40 pacchetti NPM")

  [Un attacco supply chain ha compromesso...](https://www.securityinfo.it/2025/09/16/un-attacco-supply-chain-ha-compromesso-oltre-40-pacchetti-npm/ "Permanent link to Un attacco supply chain ha compromesso oltre 40 pacchetti NPM")

  Set 16, 2025  [0](https://www.securityinfo.it/2025/09/16/un-attacco-supply-chain-ha-compromesso-oltre-40-pacchetti-npm/#respond)
* [![Npm, attacco supply chain: compromesso un package con 45.000 download settimanali](https://www.securityinfo.it/wp-content/uploads/2025/05/hacking-4038037_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/05/09/npm-attacco-supply-chain-compromesso-un-package-con-45-000-download-settimanali/ "Npm, attacco supply chain: compromesso un package con 45.000 download settimanali")

  [Npm, attacco supply chain: compromesso...](https://www.securityinfo.it/2025/05/09/npm-attacco-supply-chain-compromesso-un-package-con-45-000-download-settimanali/ "Permanent link to Npm, attacco supply ...