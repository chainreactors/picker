---
title: Hacker russi fruttano un bug 0-day di 7-Zip per distribuire SmokeLoader
url: https://www.securityinfo.it/2025/02/05/hacker-russi-fruttano-un-bug-0-day-di-7-zip-per-distribuire-smokeloader/?utm_source=rss&utm_medium=rss&utm_campaign=hacker-russi-fruttano-un-bug-0-day-di-7-zip-per-distribuire-smokeloader
source: Securityinfo.it
date: 2025-02-06
fetch_date: 2025-10-06T20:39:42.300875
---

# Hacker russi fruttano un bug 0-day di 7-Zip per distribuire SmokeLoader

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

## Hacker russi fruttano un bug 0-day di 7-Zip per distribuire SmokeLoader

Feb 05, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/02/05/hacker-russi-fruttano-un-bug-0-day-di-7-zip-per-distribuire-smokeloader/#respond)

---

Il team di Threat Hunting della Zero Day Initiative di Trend Micro [ha individuato](https://www.trendmicro.com/en_us/research/25/a/cve-2025-0411-ukrainian-organizations-targeted.html) una **campagna malware che sfruttava un** **bug 0-day di 7-Zip per distribuire il malware SmokeLoader.**

La vulnerabilità, tracciata come CVE-2025-0411, consente a un attaccante di e**ludere i controlli del Mark-of-The-Web** (MoTW), un meccanismo di protezione di Windows che blocca l’esecuzione automatica di script e applicazioni non riconosciute.

Quando un utente scarica un file dal web, la feature lo identifica come sospetto per evitare che venga eseguito accidentalmente. Il bug di 7-Zip consente di eludere questi controlli semplicemente incapsulando un archivio dentro l’altro: il programma infatti non propaga correttamente i controlli di MoTW anche agli archivi interni, dove gli attaccanti possono **inserire script ed eseguibili senza preoccuparsi che vengano bloccati.**

![bug 7-Zip](https://www.securityinfo.it/wp-content/uploads/2025/02/download.png)

## La campagna per distribuire SmokeLoader

Per distribuire SmokeLoader servendosi del bug di 7-Zip, gli attaccanti hanno inviato **email di phishing a diversi funzionari e dipendenti di organizzazioni ucraine.** I messaggi chiedevano agli utenti di aprire il materiale allegato con una certa urgenza, senza specificare a cosa si riferisse.

Gli allegati erano dei file .zip che contenevano a loro volta un archivio creato ad hoc; questo sfruttava la **manipolazione tipografica** per eseguire degli attacchi omografici, nei quali cioè vengono usati caratteri speciali  “mascherati” da quelli classici.

Nel caso della campagna in esame, i cybercriminali hanno usato il carattere cirillico “Es” per **camuffare l’archivio interno da file .doc**; in questo modo, gli utenti ignari aprivano il file e consentivano così l’esecuzione dei contenuti dell’archivio senza i controlli MoTW.

Nel dettaglio, l’apertura del file portava all’esecuzione di un file .URL presente nell’archivio che puntava a un server controllato dagli attaccanti; questo, a sua volta, scaricava un altro file .zip che conteneva l’**eseguibile di SmokeLoader mascherato da file .pdf.**

A quel punto, dopo aver aperto il file .pdf appena scaricato, SmokeLoader veniva installato sul dispositivo. Il malware è in grado di **sottrarre dati, eseguire attacchi DDoS e minare criptovalute**, oltre a scaricare nuovi moduli per potenziare le proprie attività.

![](https://www.securityinfo.it/wp-content/uploads/2025/01/network-4851079_1920.jpg)

## Le vittime del bug di 7-Zip

Dietro la campagna ci sono diversi gruppi cybercriminali russi. Gli attacchi hanno colpito **organizzazioni governative e non in Ucraina** per scopi di cyberspionaggio. Tra le vittime ci sono , tra le altre, il Ministro della Giustizia, alcune aziende manifatturiere, una farmacia, una compagnia assicurativa e l’azienda di trasporti pubblici della nazione.

I ricercatori sottolineano che gli attaccanti **hanno preso di mira organizzazioni di dimensioni ridotte**, più piccole rispetto agli organi governativi solitamente presi di mira; il motivo è che queste realtà, pur essendo sottoposte a una pressione cyber molto intensa, spesso dedicano abbastanza attenzione alla sicurezza o **non possiedono le capacità necessarie per proteggersi.** “*Queste organizzazioni minori possono diventare dei validi punti cardine per gli attaccanti per infiltrarsi in organizzazioni governative più* *grandi*“.

Alcuni degli account compromessi usati nella campagna potrebbero essere stati ottenuti da attacchi precedenti ed **è possibile che i nuovi account colpiti vengano usati in operazioni future.**

## Come proteggersi

Il team di Trend Micro ha scoperto il bug lo scorso settembre e ha immediatamente avvertito Igor Pavlov, il creatore di 7-Zip. **La vulnerabilità è stata risolta nella versione 24.09 del software**, rilasciata il 30 novembre.

Oltre ad aggiornare il software alla versione risolutiva, i ricercatori consigliano di implementare misure di sicurezza stringenti per il **controllo delle email, con tecnologie di filtraggio e anti-spam avanzate**, e di istruire i dipendenti a difendersi dagli attacchi di phishing.

È inoltre necessario sfruttare l’URL filtering per bloccare l’accesso a domini malevoli, disabilitare l’esecuzione automatica dei file con origini non riconosciute e configurare i sistemi in modo che richiedano sempre all’utente il **permesso esplicito per eseguire uno script o un’applicazione.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [0-day](https://www.securityinfo.it/tag/0-day/), [7-Zip](https://www.securityinfo.it/tag/7-zip/), [bug](https://www.securityinfo.it/tag/bug/), [conflitto russo-ucraino](https://www.securityinfo.it/tag/conflitto-russo-ucraino/), [SmokeLoader](https://www.securityinfo.it/tag/smokeloader/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/), [Windows MoTW](https://www.securityinfo.it/tag/windows-motw/)

[Silent Lynx: il gruppo APT torna all'attacco contro Kyrgyzstan e Turkmenistan](https://www.securityinfo.it/2025/02/06/silent-lynx-il-gruppo-apt-torna-allattacco-contro-kyrgyzstan-e-turkmenistan/)
[Sophos acqui...