---
title: Microsoft annuncia il Zero Trust DNS per garantire connessioni più sicure
url: https://www.securityinfo.it/2024/05/10/microsoft-annuncia-il-zero-trust-dns/
source: Over Security - Cybersecurity news aggregator
date: 2024-05-11
fetch_date: 2025-10-06T17:18:42.147897
---

# Microsoft annuncia il Zero Trust DNS per garantire connessioni più sicure

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

## Microsoft annuncia il Zero Trust DNS per garantire connessioni più sicure

Mag 10, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [News](https://www.securityinfo.it/category/news/), [Tecnologia](https://www.securityinfo.it/category/news/tecnologia-news/)
 [0](https://www.securityinfo.it/2024/05/10/microsoft-annuncia-il-zero-trust-dns/#respond)

---

Microsoft ha deciso di gestire le vulnerabilità DNS [annunciando](https://techcommunity.microsoft.com/t5/networking-blog/announcing-zero-trust-dns-private-preview/ba-p/4110366) l’arrivo di **Zero Trust DNS**, un framework che mira a rendere più sicure le connessioni dei sistemi.

“Nel mondo moderno, è molto più probabile che le destinazioni di rete utili siano definite da nomi di dominio a lunga durata piuttosto che da indirizzi IP a lunga durata. Tuttavia, l’applicazione dei confini dei nomi di dominio (come il blocco del traffico associato a un nome di dominio proibito) è sempre stata problematica, poiché **richiede la violazione della crittografia o l’affidamento a segnali di testo in chiaro inaffidabili**, come l’ispezione DNS sulla porta 53 o l’ispezione SNI” spiega **Tommy Jensen**, PM tecnico in Microsoft.

**Il DNS è uno dei punti più vulnerabili dei sistemi**: per avere completa visibilità sul traffico, gli amministratori di rete devono rinunciare all’autenticazione cifrata delle comunicazioni e gestire il traffico in chiaro, senza autenticazione da parte del server o del client.

Il nuovo framework supporta l’approccio Zero Trust per proteggere i dispositivi da connessioni potenzialmente dannose, **rifiutando qualsiasi** **comunicazione** a meno che il nomi di dominio del server non sia esplicitamente approvato e il suo lookup DNS sia autenticato e cifrato.

![rete web network](https://www.securityinfo.it/wp-content/uploads/2024/05/network-4636686_1920.jpg)

## Come funziona il Zero Trust DNS di Windows

Il framework **integra il client DNS di Windows e la Windows Filtering Platform** per attivare una protezione basata sui nomi di dominio, così che il sistema risolva solo quelli consentiti. Gli amministratori possono definire una configurazione specifica che può includere anche una lista di indirizzi IP, certificati di server Protective o certificati di autenticazione dei client.

Windows **bloccherà tutto il traffico in uscita IPv4 e IPv6 tranne le connessioni ai server Protective DNS e il traffico DHCP, DHCPv6 e NDP.** Quando uno dei server Protective DNS risponderà con una risoluzione dell’indirizzo IP, verranno attivate eccezioni per le connessioni in uscita per tale indirizzo IP; ciò garantirà che tutte le applicazioni e i servizi che usano la configurazione DNS di sistema potranno connettersi agli indirizzi IP risolti.

Al contrario, se un’applicazione o un servizio tenterà  di comunicare con un indirizzo non appreso tramite ZTDNS e non presente nelle eccezioni, il traffico **verrà bloccato di default.** Usando il ZTDNS gli amministratori potranno implementare approcci Zero trust più robusti, etichettando il traffico IPv4 e IPv6 in uscita senza doversi appoggiare al traffico DNS in chiaro. Gli admin possono inoltre **bloccare il traffico il cui dominio associato non può essere identificato in sicurezza.**

Jensen [spiega](https://techcommunity.microsoft.com/t5/networking-blog/deployment-considerations-for-windows-ztdns-client/ba-p/4113372) che, per quanto la feature possa essere potente, **non è in grado di proteggere i dispositivi da qualsiasi tipo connessione**: qualsiasi tipo di virtualizzazione che implementa il proprio stack di rete, e che quindi è in grado di superare la Windows Filtering Platform, riuscirà a eludere i controlli del ZTDNS, così come le tecnologie che bypassano lo stack di rete di Windows come XDP o DPDK.

Zero Trust DNS è disponibile in preview privata e **in futuro verrà integrato nelle nuove versioni di Windows.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [DNS](https://www.securityinfo.it/tag/dns/), [Microsoft](https://www.securityinfo.it/tag/microsoft/), [sicurezza connessioni](https://www.securityinfo.it/tag/sicurezza-connessioni/), [traffico di rete](https://www.securityinfo.it/tag/traffico-di-rete/), [Zero Trust DNS](https://www.securityinfo.it/tag/zero-trust-dns/)

[CERT-AGID 04 maggio – 10 maggio: 23 campagne malevole e il phishing multibanking che ha sfruttato la Presidenza del Consiglio dei Ministri](https://www.securityinfo.it/2024/05/13/cert-agid-04-maggio-10-maggio-phishing-multibanking-smishing-malware/)
[Anatomia del data breach che ha colpito il MITRE](https://www.securityinfo.it/2024/05/10/anatomia-del-data-breach-che-ha-colpito-il-mitre/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Secret Blizzard attacca le ambasciate straniere a Mosca tramite gli ISP](https://www.securityinfo.it/wp-content/uploads/2025/08/Gemini_Generated_Image_jk74qwjk74qwjk74-120x85.png)](https://www.securityinfo.it/2025/08/01/secret-blizzard-attacca-le-ambasciate-straniere-a-mosca-tramite-gli-isp/ "Secret Blizzard attacca le ambasciate straniere a Mosca tramite gli ISP")

  [Secret Blizzard attacca le ambasciate...](https://www.securityinfo.it/2025/08/01/secret-blizzard-attacca-le-ambasciate-straniere-a-mosca-tramite-gli-isp/ "Permanent link to Secret Blizzard attacca le ambasciate straniere a Mosca tramite gli ISP")

  Ago 01, 2025  [0](https://www.securityinfo.it/2025/08/01/secret-blizzard-attacca-le-ambasciate-straniere-a-mosca-tramite-gli-isp/#respond)
* [![Grave alerta SharePoint: attacco in corso che elude le difese](https://www.securityinfo.it/wp-content/uploads/2025/07/SharePoint_lug-2025CG-120x85.png)](https://www.s...