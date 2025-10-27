---
title: Parallels Desktop: un bug 0-day consente di ottenere i permessi di root sui Mac
url: https://www.securityinfo.it/2025/02/25/parallels-desktop-un-bug-0-day-consente-di-ottenere-i-permessi-di-root-sui-mac/
source: Over Security - Cybersecurity news aggregator
date: 2025-02-26
fetch_date: 2025-10-06T20:39:55.410819
---

# Parallels Desktop: un bug 0-day consente di ottenere i permessi di root sui Mac

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

## Parallels Desktop: un bug 0-day consente di ottenere i permessi di root sui Mac

Feb 25, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [Hacking](https://www.securityinfo.it/category/news/hacking-news/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/02/25/parallels-desktop-un-bug-0-day-consente-di-ottenere-i-permessi-di-root-sui-mac/#respond)

---

Jin Mickey, un ricercatore di sicurezza, [ha rivelato](https://jhftss.github.io/Parallels-0-day/) che una **vulnerabilità 0-day di Parallels Desktop** consente a un attaccante di **ottenere i permessi di root sui sistemi macOS**. Il bug, identificato come CVE-2024-34331, abiliterebbe ben due exploit per l’escalation dei privilegi.

Parallels Desktop è un software che consente di **virtualizzare ambienti Windows e Linux sui sistemi macOS**. Il bug era stato individuato a maggio 2024 e Parallels, il vendor del software, aveva rilasciato una patch per risolverlo; il **fix** però, stando alle evidenze di Jin Mickey, non è stato del tutto risolutivo.

![Parallels Desktop](https://www.securityinfo.it/wp-content/uploads/2025/02/macbook-pro-2381729_1920.jpg)

La patch introdotta da Parallels verifica se il tool `createinstallmedia` è attendibile e, in caso positivo, lo esegue con privilegi di root. Il ricercatore ha individuato due metodi per bypassare questa verifica, rendendo Parallels Desktop di nuovo vulnerabile ad attacci di escalation dei privilegi.

Il primo exploit è di tipo **TOCTOU** (Time-Of-Check to Time-Of-Use), ovvero una classe di attacchi che sfrutta le race condition per manipolare l’esecuzione di determinati flussi. In questo caso, un attaccante può inserirsi tra la verifica del certificato e l’esecuzione del tool per rimpiazzare `createinstallmedia` con un’esecuzione malevola creata ad hoc.

Il secondo exploit permette invece a un attaccante di alterare un binario eseguibile con certificato **iniettando un file DYLIB direttamente nel binario**, bypassando la fase di verifica. In questo caso, l’attacco colpisce la funzione `do_repack_manual`.

Il ricercatore aveva individuato i due exploit poco dopo il rilascio del fix e aveva subito contattato sia la Zero Day Initiative che Parallels per condividere la sua scoperta; nonostante ciò, tuttora non ha ricevuto risposta né dall’uno, né dall’altro. “*Dato che il vendor ha lasciato questa vulnerabilità non risolta per oltre sette mesi, nonostante la divulgazione precedente, **ho scelto di rendere pubblico questo exploit*** ***0-day*“** ha spiegato Jin Mickey. “***Il mio obiettivo è quello di sensibilizzare gli utenti e di esortarli a ridurre i rischi in modo proattivo**, poiché gli aggressori potrebbero sfruttare questa falla in modo incontrollato*“.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [bug 0-day](https://www.securityinfo.it/tag/bug-0-day/), [escalation dei privilegi](https://www.securityinfo.it/tag/escalation-dei-privilegi/), [exploit](https://www.securityinfo.it/tag/exploit/), [macOS](https://www.securityinfo.it/tag/macos/), [Parallels Desktop](https://www.securityinfo.it/tag/parallels-desktop/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[Scoperta GitVenom, campagna che sfrutta GitHub per rubare criptovalute](https://www.securityinfo.it/2025/02/26/scoperta-gitvenom-campagna-che-sfrutta-github-per-rubare-criptovalute/)
[Bybit vittima di un furto di criptovalute per 1.5 miliardi di dollari](https://www.securityinfo.it/2025/02/24/bybit-vittima-di-un-furto-di-criptovalute-per-1-5-miliardi-di-dollari/)

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
* [![Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali](https://www.s...