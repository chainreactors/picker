---
title: HinataBot, la botnet che sfrutta vulnerabilità in router e server per sferrare attacchi DDoS
url: https://www.cybersecurity360.it/news/hinatabot-la-botnet-che-sfrutta-vulnerabilita-in-router-e-server-per-sferrare-attacchi-ddos/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-21
fetch_date: 2025-10-04T10:11:10.585513
---

# HinataBot, la botnet che sfrutta vulnerabilità in router e server per sferrare attacchi DDoS

[Vai al contenuto principale](#main-content)
[Vai al footer](#footer-content)

![logo](data:image/png;base64...)![logo](https://cdnd360.it/networkdigital360/nd360-neg.svg)

[I NOSTRI SERVIZI](https://www.cybersecurity360.it/about-network)

Menu

[![Vai alla homepage di CyberSecurity](data:image/png;base64...)![Vai alla homepage di CyberSecurity](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/03/cybersecurity_logo-768x55.png)](https://www.cybersecurity360.it)

## HinataBot, la botnet che sfrutta vulnerabilità in router e server per sferrare attacchi DDoS

* [Cybersecurity Nazionale](https://www.cybersecurity360.it/cybersecurity-nazionale/)
* Malware e attacchi
  + [Malware e attacchi](https://www.cybersecurity360.it/nuove-minacce/)
  + [Ransomware](https://www.cybersecurity360.it/nuove-minacce/ransomware/)
* Norme e adeguamenti
  + [Norme e adeguamenti](https://www.cybersecurity360.it/legal/)
  + [Privacy e Dati personali](https://www.cybersecurity360.it/legal/privacy-dati-personali/)
* [Soluzioni aziendali](https://www.cybersecurity360.it/soluzioni-aziendali/)
* [Cultura cyber](https://www.cybersecurity360.it/cultura-cyber/)
* [News, attualità e analisi Cyber sicurezza e privacy](https://www.cybersecurity360.it/news/)
* [Corsi cybersecurity](https://www.cybersecurity360.it/corsi-cybersecurity/)
* [Chi siamo](https://www.cybersecurity360.it/about/)

* [![Vai alla homepage di CyberSecurity](data:image/png;base64...)![Vai alla homepage di CyberSecurity](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/03/cybersecurity_neg_logo-768x55.png)](https://www.cybersecurity360.it)
* Seguici
* + [twitter](https://twitter.com/Cybersec360)
  + [linkedin](https://www.linkedin.com/company/cybersecurity360/)
  + [Newsletter](https://www.cybersecurity360.it/newsletter-signin/)
  + [Rss Feed](#rssModal)
  + [Chi siamo](https://www.cybersecurity360.it/about)
* AREA PREMIUM
* [Whitepaper](https://www.cybersecurity360.it/whitepaper/)
* [Eventi](https://www.cybersecurity360.it/eventi/)
* [Webinar](https://www.cybersecurity360.it/webinar/)
* CANALI
* [Cybersecurity nazionale](https://www.cybersecurity360.it/cybersecurity-nazionale/)
* [Malware e attacchi](https://www.cybersecurity360.it/nuove-minacce/)
* + [Ransomware](https://www.cybersecurity360.it/nuove-minacce/ransomware/)* [Norme e adeguamenti](https://www.cybersecurity360.it/legal/)
  * + [Privacy e Dati personali](https://www.cybersecurity360.it/legal/privacy-dati-personali/)* [Soluzioni aziendali](https://www.cybersecurity360.it/soluzioni-aziendali/)
    * [Cultura cyber](https://www.cybersecurity360.it/cultura-cyber/)
    * [L'esperto risponde](https://www.cybersecurity360.it/esperto-risponde/)
    * [News, attualità e analisi Cyber sicurezza e privacy](https://www.cybersecurity360.it/news/)
    * [Corsi cybersecurity](https://www.cybersecurity360.it/corsi-cybersecurity/)
    * [Chi siamo](https://www.cybersecurity360.it/about/)

[Cybersecurity nazionale](https://www.cybersecurity360.it/cybersecurity-nazionale/)
[Malware e attacchi](https://www.cybersecurity360.it/nuove-minacce/)
[Norme e adeguamenti](https://www.cybersecurity360.it/legal/)
[Soluzioni aziendali](https://www.cybersecurity360.it/soluzioni-aziendali/)
[Cultura cyber](https://www.cybersecurity360.it/cultura-cyber/)
[L'esperto risponde](https://www.cybersecurity360.it/esperto-risponde/)
[News, attualità e analisi Cyber sicurezza e privacy](https://www.cybersecurity360.it/news/)
[Corsi cybersecurity](https://www.cybersecurity360.it/corsi-cybersecurity/)
[Chi siamo](https://www.cybersecurity360.it/about/)

L'ANALISI TECNICA

# HinataBot, la botnet che sfrutta vulnerabilità in router e server per sferrare attacchi DDoS

* [Home](https://www.cybersecurity360.it)
* [News, attualità e analisi sulla Cyber sicurezza](https://www.cybersecurity360.it/news/)

È stata individuata una nuova botnet DDoS basata su Golang: soprannominata HinataBot (il nome “Hinata” deriva da un personaggio della popolare serie anime, Naruto), sfrutta vecchie vulnerabilità note per compromettere router e server. Ecco tutti i dettagli e i consigli di mitigazione

Pubblicato il 20 Mar 2023

[Salvatore Lombardo](https://www.cybersecurity360.it/giornalista/salvatore-lombardo/)

Funzionario informatico, Esperto ICT, Socio Clusit e autore

![botnet computer zombie](data:image/png;base64...)![botnet computer zombie](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2018/10/botnet.jpg)

Si chiama **HinataBot** la nuova [botnet](https://www.cybersecurity360.it/nuove-minacce/botnet-cosa-sono-come-funzionano-e-come-proteggere-la-rete-aziendale-dagli-zombie-del-web/) che, **sfruttando vecchie vulnerabilità in router e server non aggiornati**, sferra [attacchi DDoS](https://www.cybersecurity360.it/nuove-minacce/ddos-cosa-sono-questi-attacchi-hacker-e-come-stanno-evolvendo/) potenzialmente molto massicci.

La [scoperta](https://www.akamai.com/blog/security-research/hinatabot-uncovering-new-golang-ddos-botnet) del nuovo malware è stata fatta dal Security Intelligence Response Team (SIRT) di Akamai che ha notato le attività del bot all’interno dei propri honeypot HTTP e SSH mentre abusava di vecchie vulnerabilità e credenziali deboli.

In particolare, i tentativi di infezione osservati avrebbero incluso lo sfruttamento del servizio SOAP miniigd su dispositivi **Realtek SDK** ([CVE-2014-8361](https://nvd.nist.gov/vuln/detail/CVE-2014-8361)), dell’esecuzione arbitraria di codice remoto su **router Huawei HG532** ([CVE-2017-17215](https://nvd.nist.gov/vuln/detail/cve-2017-17215)) e di **server Hadoop YARN** esposti (CVE N/A).

Indice degli argomenti

* [Attacchi DDoS da 3,3 Tbps: la capacità offensiva di HinataBot](#Attacchi_DDoS_da_33_Tbps_la_capacita_offensiva_di_HinataBot)
* [I bot emergenti scritti in Golang](#I_bot_emergenti_scritti_in_Golang)
* [Non abbassare la guardia](#Non_abbassare_la_guardia)

## Attacchi DDoS da 3,3 Tbps: la **capacità offensiva di HinataBot**

Il rapporto spiega come, mediante il reverse engineering del bot e simulando un server di comando e controllo C2, sia stato possibile testare le capacità offensive della botnet eseguendo le due funzioni di attacco scoperte nelle più recenti varianti di HinataBot (udp\_flood e http\_flood) in un periodo di 10 secondi.

![](data:image/png;base64...)![](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2023/03/word-image-63945-1.jpeg)

#### Funzioni di attacco scoperte (fonte: Akamai).

I test avrebbero consentito di stimare il dimensionamento dell’attacco, rivelando per l’http flood una generazione di 3,4 MB di dati di acquisizione di pacchetti e l’invio di 20.430 richieste http, per l’UDP flood, la creazione di 6.733 pacchetti per un totale di 421 MB di dati di acquisizione dei pacchetti.

Ciò dimostrerebbe come in un ipotetico attacco reale con 10.000 nodi bot (appena il 6,9% delle dimensioni della ben nota botnet Mirai) un flusso UDP raggiungerebbe una potenza di fuoco volumetrica di oltre 3,3 terabit al secondo (Tbps). Più modesta invece la potenza generata da un http flood di circa 27 gigabit al secondo (Gbps).

## **I bot emergenti scritti in Golang**

HinataBot è solo l’ultimo bot in ordine di tempo ad entrare a far parte della sempre crescente lista di bot emergenti basati su Go dopo [GoBruteforcer](https://www.cybersecurity360.it/news/gobruteforcer-il-malware-che-viola-i-server-web-con-attacchi-brute-force-i-dettagli/) e KmsdBot e uno dei numerosi tentativi pubblici di implementare Mirai in linguaggio Golang.

“La famiglia HinataBot fa affidamento su vecchie vulnerabilità e forza bruta su password deboli per la distribuzione. Questo è l’ennesimo esempio del perché password complesse e politiche di patching sono più importanti che mai”, conclude Akamai.

## **Non abbassare la guardia**

Gli esperti riferiscono inoltre che gli attori dietro HinataBot che originariamente avevano tentato di distribuire una variante Mirai generica (dotata di un pacchetto UPX), dall’inizio del 2023 stanno diffonde...