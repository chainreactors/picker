---
title: Badala Injector ha colpito un milione di siti WordPress
url: https://www.securityinfo.it/2023/04/18/badala-injector-ha-colpito-un-milione-di-siti-wordpress/?utm_source=rss&utm_medium=rss&utm_campaign=badala-injector-ha-colpito-un-milione-di-siti-wordpress
source: Securityinfo.it
date: 2023-04-19
fetch_date: 2025-10-04T11:35:33.604400
---

# Badala Injector ha colpito un milione di siti WordPress

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

## Badala Injector ha colpito un milione di siti WordPress

Apr 18, 2023  [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/ "Articoli scritti da Dario Orlandi")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Campagne malware](https://www.securityinfo.it/category/approfondimenti/campagne-malware/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/approfondimenti/vulnerabilita-approfondimenti/)
 [0](https://www.securityinfo.it/2023/04/18/badala-injector-ha-colpito-un-milione-di-siti-wordpress/#respond)

---

Una campagna di malware chiamata [Balada Injector](https://blog.sucuri.net/2023/04/balada-injector-synopsis-of-a-massive-ongoing-wordpress-malware-campaign.html?web_view=true), individuata e descritta dai ricercatori di [Sucuri](https://www.sucuri.net/), **ha infettato almeno 1 milione di siti web basati** **su WordPress** utilizzando una serie vulnerabilità legati a plugin e temi.

La campagna è **attiva almeno dal 2017** e inietta nei siti codice dannoso (incluso un numero significativo di vulnerabilità zero day) per reindirizzare i visitatori a siti con contenuti pericolosi, come offerte di supporto tecnico, vincite alla lotteria e notifiche per la risoluzione di Captcha.

![](https://www.securityinfo.it/wp-content/uploads/2023/04/balada_injector_charcode.png)

Fonte: Sucuri

Gli script iniettati **cercano anche file che contengono informazioni sensibili o utili e caricano backdoor** per l’accesso persistente ai siti compromessi.

La campagna non mostra segni di rallentamento: solo nel 2022, **il malware è stato rilevato oltre 141.000 volte** dai ricercatori di Sucuri; nel 67% dei casi, questi siti caricano script da domini Balada Injector noti.

## Una campagna multiforme

La campagna Balada Injector ha una serie di tratti distintivi che hanno permesso ai ricercatori di Sucuri di attribuire tutte le attività osservate a un’unica identità. **La campagna utilizza più backdoor**, nomi di dominio a rotazione e reindirizzamenti spam.

Tuttavia, il tratto più distintivo è l’utilizzo di **vulnerabilità nei plugin e nei temi di WordPress**. Balada Injector aggiunge rapidamente al suo arsenale le vulnerabilità appena divulgate e talvolta zero day, iniziando massicce ondate di infezioni entro poche ore dalla divulgazione.

![](https://www.securityinfo.it/wp-content/uploads/2023/04/linux_malware_virustotal_collection.png)

Fonte: Sucuri

La campagna **segue una precisa cadenza negli attacchi**, con nuove ondate di attività che si verificano ogni due settimane, con pause intermedie che sono probabilmente utilizzate per raccogliere e testare vulnerabilità appena segnalate e zero-day.

Le vulnerabilità più vecchie continuano a far parte del mix, con alcune che **rimangono in uso per mesi o anche anni** dopo essere state risolte tramite patch.

## L’ecosistema WordPress è vulnerabile

L’ambiente WordPress è **un obiettivo popolare per i criminali informatici**, sia per la sua grande diffusione sia perché l’ecosistema dei plugin presta il fianco a molti attacchi. Attualmente WordPress è alla base del 60% dei siti Web, il che lo rende un terreno fertile per i bug sfruttabili.

[iThemes](https://ithemes.com/), che tiene traccia dei difetti dell’ecosistema dei plug-in, ha contato **un totale di 1.425 vulnerabilità** di plugin e temi WordPress divulgati nel 2022. Il rapporto ha anche rilevato che i plug-in e i temi WordPress vulnerabili sono il motivo principale per cui i siti WordPress vengono violati.

![](https://www.securityinfo.it/wp-content/uploads/2023/04/stephen-phillips-hostreviews-co-uk-sSPzmL7fpWc-unsplash-scaled.jpg)

**WordPress dev’essere aggiornato regolarmente**, soprattutto se l’installazione contiene molti plugin e codice di terze parti.

Per proteggersi da Balada Injector e altre minacce legate a WordPress, le organizzazioni dovrebbero prima di tutto assicurarsi che **tutto il software del loro sito Web sia aggiornato**, rimuovere plug-in e temi inutilizzati e utilizzare un firewall per applicazioni Web.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [Balada Injector](https://www.securityinfo.it/tag/balada-injector/), [plugin](https://www.securityinfo.it/tag/plugin/), [Sucuri](https://www.securityinfo.it/tag/sucuri/), [WordPress](https://www.securityinfo.it/tag/wordpress/), [Zero-day](https://www.securityinfo.it/tag/zero-day/)

[ChatGPT: aumentano i furti e la compravendita di account premium](https://www.securityinfo.it/2023/04/19/chatgpt-aumentano-furti-account-premium/)
[Il traffico DDoS ha raggiunto 436 petabit in un giorno](https://www.securityinfo.it/2023/04/18/il-traffico-ddos-ha-raggiunto-436-petabit-in-un-giorno/)

---

![](https://secure.gravatar.com/avatar/9ba6108fae91c2be66a7ef45ac2db49a?s=90&d=mm&r=g)

##### [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/)

##### Articoli correlati

* [![Asana: un bug nell’integrazione AI esponeva i dati aziendali](https://www.securityinfo.it/wp-content/uploads/2025/06/AI_Vulnerabilità_20-giu-2025CG-120x85.png)](https://www.securityinfo.it/2025/06/19/asana-un-bug-nellintegrazione-ai-espone-i-dati-aziendali-al-rischio/ "Asana: un bug nell’integrazione AI esponeva i dati aziendali")

  [Asana: un bug nell’integrazione AI...](https://www.securityinfo.it/2025/06/19/asana-un-bug-nellintegrazione-ai-espone-i-dati-aziendali-al-rischio/ "Permanent link to Asana: un bug nell’integrazione AI esponeva i dati aziendali")

  Giu 19, 2025  [0](https://www.securityinfo.it/2025/06/19/asana-un-bug-nellintegrazione-ai-espone-i-dati-aziendali-al-rischio/#respond)
* [![Una vulnerabilità di un plugin di WordPress mette a rischio più di 4 milioni di siti](https://www.securityinfo.it/wp-content/uploads/2024/11/wordpress-923188_1920-120x85.jpg)](https://www.securityinfo.it/2024/11/18/una...