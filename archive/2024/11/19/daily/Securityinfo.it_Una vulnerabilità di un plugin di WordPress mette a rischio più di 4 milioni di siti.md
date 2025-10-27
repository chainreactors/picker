---
title: Una vulnerabilità di un plugin di WordPress mette a rischio più di 4 milioni di siti
url: https://www.securityinfo.it/2024/11/18/una-vulnerabilita-di-un-plugin-di-wordpress-mette-a-rischio-piu-di-4-milioni-di-siti/?utm_source=rss&utm_medium=rss&utm_campaign=una-vulnerabilita-di-un-plugin-di-wordpress-mette-a-rischio-piu-di-4-milioni-di-siti
source: Securityinfo.it
date: 2024-11-19
fetch_date: 2025-10-06T19:20:57.065008
---

# Una vulnerabilità di un plugin di WordPress mette a rischio più di 4 milioni di siti

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

## Una vulnerabilità di un plugin di WordPress mette a rischio più di 4 milioni di siti

Nov 18, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2024/11/18/una-vulnerabilita-di-un-plugin-di-wordpress-mette-a-rischio-piu-di-4-milioni-di-siti/#respond)

---

István Márton, ricercatore di **Wordfence**, [ha individuato](https://www.wordfence.com/blog/2024/11/really-simple-security-vulnerability/) una **vulnerabilità critica** presente nel plugin **Really Simple Security** di WordPress. Il bug consente a un attaccante di ottenere i privilegi di amministratore e prendere il controllo dell’intero sito.

![vulnerabilità wordpress](https://www.securityinfo.it/wp-content/uploads/2024/11/wordpress-923188_1920.jpg)

La vulnerabilità, tracciata come **CVE-2024-10924**, è infatti un bug di **authentication bypass** che permette a un attaccante di ottenere accesso a qualsiasi account registrato sul sito, anche di amministratore, quando è abilitata l’autenticazione a due fattori.

**“*Questa è una delle vulnerabilità più gravi che abbiamo segnalato nei nostri 12 anni di storia come fornitore di sicurezza per WordPress*“** ha specificato Márton.

L’autenticazione a due fattori è stata aggiunta piuttosto di recente quando il [plugin](https://www.securityinfo.it/2024/10/15/rilasciato-il-fix-per-una-vulnerabilita-critica-di-jetpack-per-wordpress/) ha cambiato nome da “Really Simple SSL” a “Really Simple Security”. L’aggiornamento includeva anche funzionalità per la protezione del login e l’individuazione di vulnerabilità.

La feature di autenticazione però è stata implementata in maniera non sicura, col risultato che **qualsiasi utente non autenticato può prendere il controllo degli account registrato sul sito** usando una semplice API REST.

Secondo i dati riportati da Márton, il plugin viene usato da **oltre 4 milioni di siti**. Le versioni vulnerabili del plugin sono quelle dalla 9.0.0 alla 9.1.1.1.

Il ricercatore ha individuato il bug a inizio novembre e ha contattato immediatamente il team di Really Simple Security. Il team del plugin ha rilasciato una patch risolutiva pochi giorni dopo, disponibile nella versione 9.1.2.

Visti gli impatti della vulnerabilità, Wordfence consiglia agli amministratori di siti WordPress che usano il plugin di **aggiornarlo il prima possibile all’ultima versione.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [authentication bypass](https://www.securityinfo.it/tag/authentication-bypass/), [plugin wordpress](https://www.securityinfo.it/tag/plugin-wordpress/), [Really Simple Security](https://www.securityinfo.it/tag/really-simple-security/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/), [WordPress](https://www.securityinfo.it/tag/wordpress/)

[Scoperta una nuova variante del ransomware Helldown che colpisce Linux](https://www.securityinfo.it/2024/11/19/scoperta-una-nuova-variante-del-ransomware-helldown-che-colpisce-linux/)
[Le falle di sicurezza nei toolkit ML più diffusi](https://www.securityinfo.it/2024/11/15/le-falle-di-sicurezza-nei-toolkit-ml-piu-diffusi/)

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
* [![Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/09/08/una-vulnerabilita-critica-di-sap-s-4hana-e-stata-sfruttata-dai-cybecriminali/ "Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali")

  [Una vulnerabilità critica di SAP...](https://www.securityinfo.it/2025/09/08/una-vulnerabilita-critica-di-sap-s-4hana-e-stata-sfruttata-dai-cybecriminali/ "Permanent link to Una vulnerabilità...