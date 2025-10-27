---
title: Un bug consentiva il controllo remoto di molte auto connesse
url: https://www.securityinfo.it/2022/12/05/un-bug-consentiva-il-controllo-remoto-di-molte-auto-connesse/?utm_source=rss&utm_medium=rss&utm_campaign=un-bug-consentiva-il-controllo-remoto-di-molte-auto-connesse
source: Securityinfo.it
date: 2022-12-06
fetch_date: 2025-10-04T00:37:07.832305
---

# Un bug consentiva il controllo remoto di molte auto connesse

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

## Un bug consentiva il controllo remoto di molte auto connesse

Dic 05, 2022  [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/ "Articoli scritti da Dario Orlandi")
 [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2022/12/05/un-bug-consentiva-il-controllo-remoto-di-molte-auto-connesse/#respond)

---

Nissan, Honda, Toyota e Fca sono solo alcuni dei marchi più noti che utilizzano (o hanno utilizzato) la piattaforma di connettività [SiriusXM Connected Vehicle Services](https://www.siriusxmcvs.com/). Secondo il produttore, questa tecnologia è infatti utilizzata da oltre 15 produttori, che l’hanno implementata in **12 milioni di veicoli** per gestire 50 servizi diversi.

Alcuni analisti che si occupano di sicurezza [hanno infatti scoperto](https://twitter.com/samwcyo/status/1597792097175674880) che la piattaforma era utilizzata per **funzioni di gestione remota** dei veicoli da Acura, BMW, Honda, Hyundai, Infiniti, Jaguar, Land Rover, Lexus, Nissan, Subaru e Toyota.

Analizzando il traffico generato da e verso l’app di Nissan, hanno scoperto che era possibile costruire e inviare richieste Http contraffatte conoscendo soltanto il **numero identificativo del veicolo** (Vin). Questa informazione è molto spesso facile da individuare anche dall’esterno se si ha accesso fisico a un’auto parcheggiata, perché in molti casi viene riportata su un’etichetta collocata nella parte bassa del parabrezza.

## Accesso remoto

Una volta in possesso di questo numero identificativo, i ricercatori sono stati in grado di recuperare una grande quantità di **informazioni sull’auto e sul suo proprietario**, tra cui il nome completo, il numero di telefono, l’indirizzo e tutti i dettagli relativi all’auto.

![](https://www.securityinfo.it/wp-content/uploads/2022/12/Fix4IRaWIAACyWE.png)

Fonte: Sam Curry (@samwcyo), via Twitter

Inoltre, si poteva sfruttare il bug anche per inviare al veicolo **comandi remoti**: secondo il ricercatore Sam Curry, se l’auto era stata prodotta dopo il 2015 un attaccante avrebbe potuto tracciare la posizione, aprire e chiudere le serrature, avviare e fermare il motore, suonare il clacson o pilotare i fari.

Se invece il veicolo era più vecchio l’attacco avrebbe consentito soltanto **l’accesso alle informazioni complete del proprietario**.

I ricercatori hanno mantenuto i contatti con le aziende coinvolte fin dai primi riscontri e hanno comunicato prontamente le loro scoperte. SiriusXM ha quindi provveduto a **correggere la vulnerabilità immediatamente** una volta ricevuta la segnalazione.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [auto](https://www.securityinfo.it/tag/auto/), [bug](https://www.securityinfo.it/tag/bug/), [connected car](https://www.securityinfo.it/tag/connected-car/), [FCA](https://www.securityinfo.it/tag/fca/), [Hyundai](https://www.securityinfo.it/tag/hyundai/), [lexus](https://www.securityinfo.it/tag/lexus/), [Nissan](https://www.securityinfo.it/tag/nissan/), [subaru](https://www.securityinfo.it/tag/subaru/), [Toyota](https://www.securityinfo.it/tag/toyota/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[Il 2023 sarà l'anno del crime-as-a-service](https://www.securityinfo.it/2022/12/06/cybersecurity-previsioni-fortinet/)
[Come scegliere la VPN più affidabile](https://www.securityinfo.it/2022/12/05/scegliere-vpn-affidabile/)

---

![](https://secure.gravatar.com/avatar/9ba6108fae91c2be66a7ef45ac2db49a?s=90&d=mm&r=g)

##### [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/)

##### Articoli correlati

* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_d4x8rid4x8rid4x8-120x85.png)](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  [Firewall Cisco sotto attacco: una nuova...](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Permanent link to Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  Set 29, 2025  [0](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/#respond)
* [![Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.](https://www.securityinfo.it/wp-content/uploads/2025/09/ai-generated-9053184_1920-120x85.jpg)](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/ "Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.")

  [Attaccanti sfruttano un bug di...](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/ "Permanent link to Attaccanti sfruttano un bug di GeoServer per attaccare un’agenzia governativa U.S.A.")

  Set 24, 2025  [0](https://www.securityinfo.it/2025/09/24/attaccanti-sfruttano-un-bug-di-geoserver-per-attaccare-unagenzia-governativa-u-s-a/#respond)
* [![Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali](https://www.securityinfo.it/wp-content/uploads/2025/09/hacker-2300772_1920-1-120x85.jpg)](https://www.securityinfo.it/2025/09/08/una-vulnerabilita-critica-di-sap-s-4hana-e-stata-sfruttata-dai-cybecriminali/ "Una vulnerabilità critica di SAP S/4HANA è stata sfruttata dai cybecriminali")

  [Una vulnerabilità critica di SAP...](https://www.securityinfo.it/2025/09/08/una-vulnerabilita-critica-di-sap-s-4hana-e-stata-sfruttata-dai-cybecriminali/ "...