---
title: I prodotti SAP soffrono di vulnerabilità critiche
url: https://www.securityinfo.it/2023/06/30/i-prodotti-sap-soffrono-di-vulnerabilita-critiche/
source: Over Security - Cybersecurity news aggregator
date: 2023-07-01
fetch_date: 2025-10-04T11:55:56.199523
---

# I prodotti SAP soffrono di vulnerabilità critiche

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

## I prodotti SAP soffrono di vulnerabilità critiche

Giu 30, 2023  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [Prodotto](https://www.securityinfo.it/category/news/prodotto-news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2023/06/30/i-prodotti-sap-soffrono-di-vulnerabilita-critiche/#respond)

---

Fabian Hagg, ricercatore presso SEC Consult, [ha individuato **quattro vulnerabilità**](https://www.securityweek.com/details-disclosed-for-critical-sap-vulnerabilities-including-wormable-exploit-chain/) **che colpiscono alcuni prodotti SAP**; tra questi spiccano ERP Central Component, S/4HANA, BW/4HANA, Solution Manager, SAP for Oil & Gas, SAP for Utilities, Supplier RelationShip Management, Human Capital Management e Employee Central Payroll.

Le [vulnerabilità](https://www.securityinfo.it/2023/06/26/cisa-aggiunge-vulnerabilita-gia-sfruttate-al-proprio-catalogo/), identificate come CVE-2021-27610, CVE-2021-33677, CVE-2021-33684 e CVE-2023-0014 sono state scoperte durante l’analisi dell’interfaccia Remote Function Call per la comunicazione tra sistemi SAP. La **27610 e la 0014 sono state catalogate come critiche**; entrambe risiedono nell’architettura usata per le comunicazioni RFC e HTTP, sia interne ai sistemi che cross-systems.

Hagg ha spiegato che sfruttando queste vulnerabilità **un attaccante può compromettere l’intero sistema target**; per di più, ha affermato Johannes Greil, head of SEC Consult Vulnerability Lab, **la compromissione avviene senza alcuna interazione utente** e senza dover prima ottenere permessi sul sistema.

![SAP - Credits: weerapat- Deposiphotos](https://www.securityinfo.it/wp-content/uploads/2023/06/Depositphotos_45719579_L.jpg)

Credits: weerapat- Deposiphotos

Anche se questi sistemi generalmente possono essere raggiunti solo dall’interno, esistono alcune configurazioni che permettono di sfruttare le vulnerabilità direttamente dalla rete pubblica.

Le vulnerabilità, già pericolose di per sé, possono essere **combinate in una catena di attacco per eseguire codice remoto senza autenticazione.** Come [illustrato da Hagg](https://sec-consult.com/blog/detail/responsible-disclosure-of-an-exploit-chain-targeting-the-rfc-interface-implementation-in-sap-application-server-for-abap/), il team di ricercatori ha eseguito l’attacco con successo in un ambiente di test.

**SAP ha rilasciato aggiornamenti di sicurezza per tutte e quattro le vulnerabilità** e ha invitato gli utenti ad aggiornare il prima possibile i prodotti vulnerabili. Oltre all’aggiornamento, gli utenti devono seguire alcuni step di post-installazione, come indicato nelle [note di sicurezza](https://support.sap.com/en/my-support/knowledge-base/security-notes-news.html?anchorId=section_1194770574) condivise dall’azienda.

Al momento, spiegano i ricercatori di SEC Consult, **non esistono dei workaround** per limitare gli impatti delle vulnerabilità. Nel caso non si potessero aggiornare i sistemi, è consigliabile **limitare l’accesso alla rete ai server vulnerabili**, al fine di ridurre il più possibile la superficie di attacco.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [compromissione sistema](https://www.securityinfo.it/tag/compromissione-sistema/), [esecuzione remota codice](https://www.securityinfo.it/tag/esecuzione-remota-codice/), [SAP](https://www.securityinfo.it/tag/sap/), [SAP S/4HANA](https://www.securityinfo.it/tag/sap-s-4hana/), [SEC Consult](https://www.securityinfo.it/tag/sec-consult/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[Proton Pass, il password manager open-source che cripta anche gli indirizzi email](https://www.securityinfo.it/2023/07/03/proton-pass-il-password-manager-open-source-che-cripta-anche-gli-indirizzi-email/)
[ThirdEye, un nuovo infostealer russo che migliora a vista d'occhio](https://www.securityinfo.it/2023/06/30/thirdeye-un-nuovo-infostealer-russo-che-migliora-a-vista-docchio/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_d4x8rid4x8rid4x8-120x85.png)](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  [Firewall Cisco sotto attacco: una nuova...](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Permanent link to Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  Set 29, 2025  [0](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/#respond)
* [![Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.](https://www.securityinfo.it/wp-content/uploads/2025/09/ai-generated-9053184_1920-120x85.jpg)](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/ "Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.")

  [Attaccanti sfruttano un bug di...](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/ "Permanent link to Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.")

  ...