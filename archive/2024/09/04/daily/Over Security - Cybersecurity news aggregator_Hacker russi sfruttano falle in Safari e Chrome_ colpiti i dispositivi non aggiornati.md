---
title: Hacker russi sfruttano falle in Safari e Chrome: colpiti i dispositivi non aggiornati
url: https://www.securityinfo.it/2024/09/03/hacker-russi-sfruttano-falle-in-safari-e-chrome-colpiti-i-dispositivi-non-aggiornati/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-04
fetch_date: 2025-10-06T18:31:05.123365
---

# Hacker russi sfruttano falle in Safari e Chrome: colpiti i dispositivi non aggiornati

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

## Hacker russi sfruttano falle in Safari e Chrome: colpiti i dispositivi non aggiornati

Set 03, 2024  [Stefano Silvestri](https://www.securityinfo.it/author/stefano-silvestri/ "Articoli scritti da Stefano Silvestri")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [Hacking](https://www.securityinfo.it/category/news/hacking-news/), [Malware](https://www.securityinfo.it/category/news/malware-news/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2024/09/03/hacker-russi-sfruttano-falle-in-safari-e-chrome-colpiti-i-dispositivi-non-aggiornati/#respond)

---

I ricercatori di sicurezza informatica hanno individuato diverse campagne di attacchi che sfruttano vulnerabilità nei browser **Safari** e **Chrome**, ora corrette, per infettare dispositivi mobili con malware che ruba informazioni.

Queste campagne, [segnalate dal Google Threat Analysis Group (TAG)](https://blog.google/threat-analysis-group/state-backed-attackers-and-commercial-surveillance-vendors-repeatedly-use-the-same-exploits/), hanno utilizzato **exploit già noti e per cui erano disponibili patch**, ma che risultavano ancora efficaci contro dispositivi non aggiornati.

Gli attacchi, osservati **tra novembre 2023 e luglio 2024**, si sono distinti per l’uso di **tecniche di watering hole**, ovvero la compromissione di siti web visitati frequentemente da utenti specifici, come i siti del governo mongolo cabinet.gov[.]mn e mfa.gov[.]mn, per distribuire gli exploit.

L’intrusione è stata attribuita con una certa sicurezza a un gruppo di hacker sponsorizzato dalla Russia, noto come **APT29 (o Midnight Blizzard)**. Ci sono infatti evidenti somiglianze tra gli exploit usati e quelli precedentemente collegati a fornitori di spyware commerciali come Intellexa e NSO Group, suggerendo un possibile riutilizzo degli exploit.

Le vulnerabilità sfruttate includono:

* CVE-2023-41993: una falla di WebKit che consente l’esecuzione di codice arbitrario quando si visualizzano contenuti web appositamente creati (corretta da Apple a settembre 2023).
* CVE-2024-4671: una falla di tipo use-after-free nel componente Visuals di Chrome, che permette l’esecuzione di codice arbitrario (corretta da Google a maggio 2024).
* CVE-2024-5274: una falla di tipo confusion nel motore V8 di JavaScript e WebAssembly che permette l’esecuzione di codice arbitrario (corretta da Google a maggio 2024).

![](https://www.securityinfo.it/wp-content/uploads/2024/09/chrome-safari.jpg)

Gruppi di hacker di Stato stanno sfruttando n-day exploit già utilizzati in passato come zero-day da fornitori di spyware commerciali.

Le campagne di novembre 2023 e febbraio 2024 hanno **compromesso i siti del governo mongolo per distribuire un exploit tramite un iframe** dannoso che puntava a un dominio controllato dagli hacker. Gli hacker si sono quindi avvalsi di un elemento HTML integrato nelle pagine web dei siti compromessi, che ha caricato contenuti da un’altra fonte in grado di eseguire codice pericoloso. Ciò nella maggior parte dei casi avviene senza che l’utente se ne accorga.

Quando questi siti venivano visitati con un dispositivo iOS, come un iPhone o un iPad, un **payload di ricognizione** veniva scaricato per eseguire controlli preliminari, prima di distribuire un **exploit che rubava i cookie del browser**.

Questo exploit è simile a uno utilizzato nel 2021 per rubare cookie di autenticazione da vari siti popolari, come Google e Facebook, inviandoli poi a un server controllato dagli attaccanti. Gli attacchi erano mirati principalmente a funzionari governativi di paesi europei, che ricevevano link dannosi tramite messaggi su LinkedIn.

A luglio 2024, il sito mfa.gov[.]mn è stato **nuovamente compromesso** per reindirizzare gli utenti Android che utilizzavano Chrome a un link dannoso, che sfruttava due vulnerabilità per installare un malware capace di rubare informazioni come **cookie**, **password** e **dati delle carte di credito**.

Questi attacchi evidenziano come gruppi di hacker sponsorizzati dallo Stato stiano sfruttando vulnerabilità già note (**n-day exploit**) che erano state utilizzate in passato come zero-day da fornitori di spyware commerciali. Ciò solleva il dubbio che tali exploit possano essere stati **acquistati da broker di vulnerabilità**, alimentando un mercato che continua a prosperare nonostante gli sforzi di Apple e Google per rafforzare la sicurezza dei loro prodotti.

Gli attacchi di tipo watering hole rimangono una minaccia significativa, **in grado di colpire gruppi specifici di utenti**, inclusi quelli che utilizzano dispositivi mobili, attraverso l’uso di exploit sofisticati che possono risultare efficaci anche su browser non aggiornati.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [attacco hacker](https://www.securityinfo.it/tag/attacco-hacker/), [hacker](https://www.securityinfo.it/tag/hacker/), [iframe](https://www.securityinfo.it/tag/iframe/), [watering hole](https://www.securityinfo.it/tag/watering-hole/)

[Gli italiani si preoccupano dell'eredità digitale dei defunti](https://www.securityinfo.it/2024/09/03/gli-italiani-si-preoccupano-delleredita-digitale-dei-defunti/)
[Aumentano gli attacchi alle applicazioni e alle API](https://www.securityinfo.it/2024/09/02/aumentano-gli-attacchi-alle-applicazioni-e-alle-api/)

---

![](https://secure.gravatar.com/avatar/d290cb647e218511e0408135528fb5f2?s=90&d=mm&r=g)

##### [Stefano Silvestri](https://www.securityinfo.it/author/stefano-silvestri/)

##### Articoli correlati

* [![Malware dentro il malware: trovate backdoor nel RAT Sakura](https://www.securityinfo.it/wp-content/uploads/2025/06/security-7057561_1920-120x85.jpg)](https://www.securityi...