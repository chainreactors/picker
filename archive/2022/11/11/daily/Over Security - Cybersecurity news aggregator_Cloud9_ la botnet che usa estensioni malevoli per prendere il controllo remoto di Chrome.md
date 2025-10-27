---
title: Cloud9: la botnet che usa estensioni malevoli per prendere il controllo remoto di Chrome
url: https://www.cybersecurity360.it/news/botnet-cloud9-estensioni-malevoli-di-chrome-nel-mirino-degli-attaccanti/
source: Over Security - Cybersecurity news aggregator
date: 2022-11-11
fetch_date: 2025-10-03T22:24:47.050417
---

# Cloud9: la botnet che usa estensioni malevoli per prendere il controllo remoto di Chrome

[Vai al contenuto principale](#main-content)
[Vai al footer](#footer-content)

![logo](data:image/png;base64...)![logo](https://cdnd360.it/networkdigital360/nd360-neg.svg)

[I NOSTRI SERVIZI](https://www.cybersecurity360.it/about-network)

Menu

[![Vai alla homepage di CyberSecurity](data:image/png;base64...)![Vai alla homepage di CyberSecurity](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/03/cybersecurity_logo-768x55.png)](https://www.cybersecurity360.it)

## Cloud9: la botnet che usa estensioni malevoli per prendere il controllo remoto di Chrome

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

Remote access trojan (RAT)

# Cloud9: la botnet che usa estensioni malevoli per prendere il controllo remoto di Chrome

* [Home](https://www.cybersecurity360.it)
* [News, attualità e analisi sulla Cyber sicurezza](https://www.cybersecurity360.it/news/)

Zimperium ha rilevato una botnet che consente a cyber attaccanti di sfruttare estensioni malevoli di Chrome per prendere il controllo del browser e rubare account online, registrare le sequenze di tasti o arruolare il browser della vittima in attacchi DDoS. Ecco i consigli per una difesa efficace

Pubblicato il 10 Nov 2022

[Mirella Castigli](https://www.cybersecurity360.it/giornalista/mirella-castigli/)

Giornalista

![Google e il malware che abusa delle API: come mitigare il rischio](data:image/png;base64...)![Google e il malware che abusa delle API: come mitigare il rischio](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2022/05/ChromeLoader.jpg)

È stata scoperta una nuova [**botnet**](https://www.cybersecurity360.it/nuove-minacce/botnet-cosa-sono-come-funzionano-e-come-proteggere-la-rete-aziendale-dagli-zombie-del-web/) nota come **Cloud9** che permette ad attaccanti di sfruttare [estensioni malevoli](https://www.cybersecurity360.it/news/estensioni-del-browser-infette-hacking-criminale/) di Chrome, per prendere il controllo del browser.

“Questa campagna conferma come la mancanza di cultura di sicurezza da parte degli utenti sia un fattore che sta portando a un cambiamento nella strategia di attacco da parte dei criminali”, commenta **Paolo Passeri**, Cyber Intelligence Principal di Netskope.

Ecco come proteggersi dal remote access trojan (RAT) per Chromium, dunque per Google Chrome e Microsoft Edge.

Indice degli argomenti

* [La nuova botnet Cloud9](#La_nuova_botnet_Cloud9)
* [Come difendersi](#Come_difendersi)

## La nuova botnet Cloud9

La scoperta della botnet è importante perché Cloud9 permette ai cyber criminali di usare estensioni malevoli del browser Chrome.

“Il mondo dei MaaS – malware as a service –”, spiega , “è in rapida evoluzione, stimolato dalla crescita del mercato del cyber crime. Cloud9, così come tanti altri “competitor”, è la dimostrazione della capacità innovativa distorta che possiedono i threat actors”, Pierguido Iezzi, Ceo di Swascan.

Cloud9, infatti, è un’estensione dannosa per browser dotata di backdoor per i browser basati su Chromium, in grado di svolgere un’ampia gamma di attività cyber crime.

Consente di rubare account online, registrare le sequenze di tasti, iniettare annunci pubblicitari e codice JS dannoso, e arruolare il browser della vittima negli [attacchi DDoS](https://www.cybersecurity360.it/nuove-minacce/ddos-cosa-sono-questi-attacchi-hacker-e-come-stanno-evolvendo/).

La botnet Cloud9 per il browser, a tutti gli effetti, è un remote access trojan (RAT) per Chromium, inclusi Google Chrome e Microsoft Edge. Permette ai threat actor di eseguire comandi da remoto.

Le estensioni malevoli di Chrome non sono disponibili nel marketplace ufficiale di Chrome, ma circolano su canali alternativi come quelli che diffondono i falsi aggiornamenti di Adobe Flash Player.

“Questi ultimi”, continua Paolo Passeri, “stanno utilizzando in maniera crescente un modello che richieda una azione esplicita da parte della vittima (derivante da comportamenti imprudenti) come ad esempio l’installazione di una applicazione. Nel caso specifico i ricercatori hanno difatti constatato come il meccanismo più comune per la distribuzione della botnet Cloud9 consista nell’installazione di finti eseguibili relativi a programmi legittimi, e siti web malevoli mascherati da aggiornamenti per Adobe Flash Player, un plugin che appartiene al cimitero di Internet dal 2020 (con l’eccezione della Cina e pochi altri contesti specifici)”.

## Come difendersi

Per proteggersi da questi vettori d’attacco, occorre effettuare il download delle estensioni solo dai marketplace ufficiali e soprattutto mantenere aggiornati i sistemi operativi e le applicazioni.

Infatti “è anche preoccupante constatare che alcune funzioni della botnet, come l’installazione di malware sull’endpoint compromesso, richiedano lo sfruttamento di **vulnerabilità per cui una patch di sicurezza è disponibile da molti anni** (sino al 2014 nel caso di CVE-2014-6332). Questo dimostra **scarsa attenzione da parte degli utenti** (o delle loro organizzazioni, e questo sarebbe ancora peggio), verso le più basilar...