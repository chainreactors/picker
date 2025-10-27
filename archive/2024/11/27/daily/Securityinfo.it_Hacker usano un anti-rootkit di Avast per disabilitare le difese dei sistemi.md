---
title: Hacker usano un anti-rootkit di Avast per disabilitare le difese dei sistemi
url: https://www.securityinfo.it/2024/11/26/hacker-usano-un-anti-rootkit-di-avast-per-disabilitare-le-difese-dei-sistemi/?utm_source=rss&utm_medium=rss&utm_campaign=hacker-usano-un-anti-rootkit-di-avast-per-disabilitare-le-difese-dei-sistemi
source: Securityinfo.it
date: 2024-11-27
fetch_date: 2025-10-06T19:21:30.583747
---

# Hacker usano un anti-rootkit di Avast per disabilitare le difese dei sistemi

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

## Hacker usano un anti-rootkit di Avast per disabilitare le difese dei sistemi

Nov 26, 2024  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [Hacking](https://www.securityinfo.it/category/news/hacking-news/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Malware](https://www.securityinfo.it/category/news/malware-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2024/11/26/hacker-usano-un-anti-rootkit-di-avast-per-disabilitare-le-difese-dei-sistemi/#respond)

---

Di recente i ricercatori di Trellix [hanno scoperto](https://www.trellix.com/blogs/research/when-guardians-become-predators-how-malware-corrupts-the-protectors/) una nuova campagna malware che usa un driver di un a**nti-rootkit di Avast per disabilitare le difese dei sistemi** e prenderne il controllo. Di fatto gli attaccanti sfruttano i software di sicurezza come un’arma per ottenere il controllo del sistema ed eseguire altre azioni malevole.

La catena di attacco comincia proprio con la diffusione del driver dell’anti-rootkit di [Avast](https://www.securityinfo.it/2024/07/09/avast-rilascia-un-decryptor-per-il-ransomware-donex/). Trishaan Kalra, ricercatore della compagnia, spiega che invece di usare un driver creato appositamente, **gli attaccanti usano un driver kernel legittimo**; in questo modo, i software di sicurezza non sollevano alert all’utente.

Una volta che il driver è stato installato ed è in esecuzione, il malware ottiene accesso di livello kernel al sistema e procede con l’**interruzione dei** **processi di sicurezza in esecuzione**. Il malware è in grado di terminare ben 142 processi legati ad antivirus e soluzioni EDR ampiamente usati accedendo a una lista di nomi hard-coded.

![Avast anti-rootkit](https://www.securityinfo.it/wp-content/uploads/2024/11/Trellix.jpg)

La lista di processi di sicurezza che il malware può interrompere. Credits: Trellix

Dopo l’esecuzione iniziale, il malware comincia ad acquisire screenshot di tutti i processi attivi del sistema. Una volta ottenuto l’intero elenco, il malware confronta i nomi dei processi con quelli presenti nella lista hard-coded; se uno o più nomi corrispondono, **il malware crea un handle per ciascun processo e sfrutta il driver Avast per terminarlo.**

Per contrastare questa minaccia, Kalra consiglia di definire delle regole nei tool di sicurezza per identificare e bloccare i driver vulnerabili in base alla loro firma o hash. “***L’integrazione di questa regola in una soluzione EDR antivirus garantisce che anche i driver legittimi con vulnerabilità vengano bloccati efficacemente**, aggiungendo un livello cruciale di protezione contro gli attacchi avanzati basati sui driver*” spiega Kalra.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [anti-rootkit](https://www.securityinfo.it/tag/anti-rootkit/), [antivirus](https://www.securityinfo.it/tag/antivirus/), [Avast](https://www.securityinfo.it/tag/avast/), [campagna malware](https://www.securityinfo.it/tag/campagna-malware/), [EDR](https://www.securityinfo.it/tag/edr/), [software di sicurezza](https://www.securityinfo.it/tag/software-di-sicurezza/)

[Ingecom Ignition: "Siamo più forti, ma dobbiamo farci conoscere"](https://www.securityinfo.it/2024/11/27/ingecom-ignition-siamo-piu-forti-ma-dobbiamo-farci-conoscere/)
[Oltre 400.000 sistemi sono esposti alle vulnerabilità più sfruttate del 2023](https://www.securityinfo.it/2024/11/25/oltre-400-000-sistemi-sono-esposti-alle-vulnerabilita-piu-sfruttate-del-2023/)

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
* [![Il ransomware Medusa usa un driver malevolo per bloccare le difese EDR](https://www.securityinfo.it/wp-content/uploads/2025/03/2808-1-120x85.jpg)](https://www.securityinfo.it/2025/03/21/il-ransomware-medusa-usa-un-driver-malevolo-per-bloccare-le-difese-edr/ "Il ransomware Medusa usa un driver malevolo per bloccare le difese EDR")

  [Il r...