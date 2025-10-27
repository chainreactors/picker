---
title: Web shell e ransomware continuano a minacciare la sicurezza
url: https://www.securityinfo.it/2023/05/17/web-shell-e-ransomware-continuano-a-minacciare-la-sicurezza/?utm_source=rss&utm_medium=rss&utm_campaign=web-shell-e-ransomware-continuano-a-minacciare-la-sicurezza
source: Securityinfo.it
date: 2023-05-18
fetch_date: 2025-10-04T11:42:21.913428
---

# Web shell e ransomware continuano a minacciare la sicurezza

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

## Web shell e ransomware continuano a minacciare le imprese

Mag 17, 2023  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Apt](https://www.securityinfo.it/category/minacce-2/apt/), [Attacchi](https://www.securityinfo.it/category/news/attachi/), [Malware](https://www.securityinfo.it/category/news/malware-news/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [Minacce](https://www.securityinfo.it/category/minacce-2/), [News](https://www.securityinfo.it/category/news/), [Ransomware](https://www.securityinfo.it/category/minacce-2/ransomware/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2023/05/17/web-shell-e-ransomware-continuano-a-minacciare-la-sicurezza/#respond)

---

I risultati dell’[ultimo report di Talos Intelligence](https://blog.talosintelligence.com/quarterly-report-incident-response-trends-in-q1-2023/) hanno evidenziato un **aumento degli attacchi di tipo web shell** nel periodo gennaio-marzo 2023. Le minacce web-shell rappresentano un quarto del totale degli attacchi del Q1, mentre i **ransomware e pre-ransomware si sono rivelati in calo**: la percentuale si è ridotta dal 20% al 10% nei primi tre mesi dell’anno.

L’uso di web shell è **aumentato del 6% rispetto agli ultimi mesi del 2022.** Secondo quanto riportato da Talos, gli attaccanti hanno sfruttato **script disponibili sul web**, in particolare su **repository GitHub pubblici**, e in diversi linguaggi tra i quali PHP, ASP.NET e Perl.

I gruppi criminali hanno usato gli script per ottenere accesso persistente ai sistemi ed eseguire codice remoto per accedere ad altri dispositivi della rete e diffondere malware. Le **tattiche, tecniche e procedure usate per gli script sono associabili a quelle del gruppo FIN13**. L’attività di web shell del gruppo offre diverse funzionalità, tra le quali la possibilità di eseguire query sulle istanze Microsoft SQL, creare connessioni reverse-shell verso indirizzi IP esterni ed eseguire script PHP per usarli come proxy per connettersi ad altri servizi.

![Web shell](https://www.securityinfo.it/wp-content/uploads/2023/05/hacker-1952027_1920-1-1.jpg)

Pixabay

In molti casi **gli attaccanti hanno combinato diverse funzionalità per rafforzare la propria presenza nella rete aziendale** e raggiungere più dispositivi. Non sono ancora chiari i motivi dietro l’aumento della popolarità di questi attacchi, ma la possibilità di accedere con facilità agli script ne ha di certo favorito la diffusione.

Tra i settori più colpiti dai diversi attacchi spicca quello della sanità, sia pubblica che privata, seguito dalla vendita al dettaglio, dall’immobiliare e dal ricettivo.

## I ransomware non si arrestano

Non è detto che il numero di ransomware continuerà a diminuire, considerato anche che n**ell’ultimo mese questi attacchi sono nuovamente aumentati**. La maggior parte degli attacchi è riconducibile a gruppi hacker conosciuti come Vice Society.

Tra i ransomware più diffusi del Q1 2023, Talos riporta **Phobos** e **Daixin**. Il primo è attivo dal 2018 e sfrutta gli errori di configurazione del procotollo Remote Desktop Control per ottenere l’accesso alla rete aziendale; il secondo, più nuovo, è in realtà una famiglia di ransomware-as-a-service che accede ai sistemi sfruttando le vulnerabilità dei server VPN.

Di fronte alle campagna per la lotta ai ransomware promosse dai governi, **gli attaccanti hanno cominciato a creare nuovi gruppi per sfuggire ai controlli**. È il caso per esempio del gruppo Hive: lo scorso gennaio il Dipartimento della Giustizia degli Stati Uniti ha annunciato una campagna per contrastare e distruggere il gruppo che risulta però inattivo già dagli ultimi mesi del 2022.

## L’assenza di MFA mette a rischio la sicurezza

Uno dei principali impedimenti alla sicurezza, sottolinea Talos Intelligence, è la mancata implementazione dell’autenticazione multi-fattore: **più del 30% delle organizzazioni analizzate non ha abilitato l’MFA per account e servizi critici**, oppure non la usa affatto. I tool di monitoraggio di Talos hanno individuato numerosi incidenti che si sarebbero potuti evitare con un corretto processo di autenticazione.

![Web shell](https://www.securityinfo.it/wp-content/uploads/2023/05/close-up-hands-holding-smartphone-with-lock.jpg)

Freepik

I ricercatori dell’azienda consigliano di **disabilitare tutti gli accessi VPN per gli account che non usano l’autenticazione multi-fattore**, così da ridurre il rischio di accessi indesiderati. Oltre a ciò, per limitare gli attacchi web shell, Talos invita ad **aggiornare i software e installare le patch di sicurezza il prima possibile.**

**Il 45% degli attacchi ha sfruttato le applicazioni usate dagli utent**i, un aumento del 15% rispetto al Q4 del 2022 che lo ha reso il vettore di infezione principale dei primi tre mesi del 2023.

È opportuno quindi **rimuovere servizi, funzioni e protocolli inutilizzati** e ottenere piena visibilità dei sistemi esposti sul web. Infine, i ricercatori consigliano di **eseguire audit periodici e analizzare i log per individuare eventuali attività anomale.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [malware](https://www.securityinfo.it/tag/malware/), [MFA](https://www.securityinfo.it/tag/mfa/), [script](https://www.securityinfo.it/tag/script/), [Talos Intelligence](https://www.securityinfo.it/tag/talos-intelligence/), [VPN](https://www.securityinfo.it/tag/vpn/), [Web Shell](https://www.securityinfo.it/tag/web-shell/)

[Monti ha divulgato tutti i dati rubati all’Asl 1 Abruzzo](https://www.securityinfo.it/2023/05/17/monti-ha-divulgato-tutti-i-dati-rubati-allasl-1-abruzzo/)
[Gli attacchi evolvono e si adattano ai nuovi tool di sicurezza](https://www.securityinfo.it/2023/05/16/gli-attaccanti-evolvono-e-si-adattano-ai-nuovi-to...