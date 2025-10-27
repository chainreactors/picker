---
title: Un bug di Woocommerce mette a rischio mezzo milione di store
url: https://www.securityinfo.it/2023/03/28/un-bug-di-woocommerce-mette-a-rischio-mezzo-milione-di-store/?utm_source=rss&utm_medium=rss&utm_campaign=un-bug-di-woocommerce-mette-a-rischio-mezzo-milione-di-store
source: Securityinfo.it
date: 2023-03-29
fetch_date: 2025-10-04T11:03:14.139558
---

# Un bug di Woocommerce mette a rischio mezzo milione di store

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

## Un bug di Woocommerce mette a rischio mezzo milione di store

Mar 28, 2023  [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/ "Articoli scritti da Dario Orlandi")
 [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2023/03/28/un-bug-di-woocommerce-mette-a-rischio-mezzo-milione-di-store/#respond)

---

[Automattic](https://automattic.com/), l’azienda che sviluppa il CMS WordPress, ha emesso un aggiornamento di sicurezza riguardante centinaia di migliaia di siti web che utilizzano il diffusissimo plug-in di pagamento [WooCommerce](https://woocommerce.com/) per i negozi online, che vanta **oltre mezzo milione di installazioni** attive.

La patch risolve una vulnerabilità critica che potrebbe consentire agli aggressori di **ottenere l’accesso amministrativo agli store** vulnerabili senza autenticazione. Il difetto è stato segnalato da Michael Mazzolini di [GoldNetwork](https://www.gold-network.ch/) e colpisce WooCommerce Payments 4.8.0 e le versioni successive.

Secondo l’analisi di [WordFence](https://www.wordfence.com/), gli aggressori non autenticati possono sfruttare il bug per fingersi amministratori e **prendere il completo controllo di un sito web** senza alcuna interazione da parte dell’utente e senza implementare tattiche di ingegneria sociale.

## Lo sfruttamento non è ancora iniziato

[Patchstack](https://patchstack.com/) ritiene il problema molto preoccupante, perché questa vulnerabilità non richiede autenticazione; è quindi **molto probabile che presto sarà sfruttata massicciamente**.

Il team di WooCommerce **ha rilasciato un aggiornamento di sicurezza** che corregge il problema e afferma di non aver trovato alcuna prova che questa grave falla sia stata presa di mira o sfruttata in the wild.

![](https://www.securityinfo.it/wp-content/uploads/2023/03/1539812909032-transformed.jpeg)

Beau Lebens, Head of Engineering di WooCommerce

Beau Lebens, Head of Engineering di WooCommerce, ha dichiarato “Al momento non abbiamo prove che la vulnerabilità sia stata sfruttata al di fuori del nostro programma di test di sicurezza. **Non crediamo che i dati degli store o dei clienti siano stati compromessi** a causa di questa vulnerabilità”.

“Abbiamo immediatamente **disattivato i servizi interessati e mitigato il problema** per tutti i siti Web ospitati su WordPress.com, Pressable e WPVIP”, ha proseguito Lebens.

“Abbiamo fornito una correzione **e lavorato con il team di WordPress.org Plugins per aggiornare automaticamente i siti** che eseguono WooCommerce Payments con versioni comprese tra la 4.8.0 e la 5.6.1. L’aggiornamento è attualmente in fase di applicazioni automatica per il maggior numero possibile di negozi”, ha concluso Lebens.

Gli amministratori che ospitano un’installazione di WordPress sui propri server dovranno invece aggiornare manualmente WooCommerce; la procedura è quella consueta: dalla dashboard di amministrazione di WP, **fare clic su Plugin e cercare WooCommerce Payments** nell’elenco.

Se il sistema segnala una nuova versione disponibile per il download, bisognerebbe **scaricarla e installarla immediatamente** utilizzando la funzione di upgrade integrata.

![](https://www.securityinfo.it/wp-content/uploads/2023/03/stephen-phillips-hostreviews-co-uk-sSPzmL7fpWc-unsplash-scaled.jpg)

Dopo aver messo al sicuro i siti, si consiglia di **verificare la presenza di nuovi utenti amministratori e post sospetti** aggiunti di recente.

Se si trovassero prove di attività inattese, è opportuno **aggiornare immediatamente tutte le password di amministratore e generare nuove chiavi API** per i servivi eventualmente collegati.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Automattic](https://www.securityinfo.it/tag/automattic/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/), [Woocommerce](https://www.securityinfo.it/tag/woocommerce/), [WordPress](https://www.securityinfo.it/tag/wordpress/)

[Gruppo hacker cinese sospettato degli attacchi zero-day a Fortinet](https://www.securityinfo.it/2023/03/29/gruppo-hacker-cinese-zero-day-fortinet/)
[Meta presenta una nuova kill chain adatta a ogni tipo di attacco, o quasi](https://www.securityinfo.it/2023/03/28/meta-kill-chain-attacchi/)

---

![](https://secure.gravatar.com/avatar/9ba6108fae91c2be66a7ef45ac2db49a?s=90&d=mm&r=g)

##### [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/)

##### Articoli correlati

* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_d4x8rid4x8rid4x8-120x85.png)](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  [Firewall Cisco sotto attacco: una nuova...](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Permanent link to Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  Set 29, 2025  [0](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/#respond)
* [![Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.](https://www.securityinfo.it/wp-content/uploads/2025/09/ai-generated-9053184_1920-120x85.jpg)](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/ "Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.")

  [Attaccanti sfruttano un bug di...](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-u...