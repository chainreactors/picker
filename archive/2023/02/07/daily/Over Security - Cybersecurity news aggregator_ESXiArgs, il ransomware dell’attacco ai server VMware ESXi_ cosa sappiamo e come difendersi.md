---
title: ESXiArgs, il ransomware dell’attacco ai server VMware ESXi: cosa sappiamo e come difendersi
url: https://www.cybersecurity360.it/nuove-minacce/ransomware/esxiargs-il-ransomware-dellattacco-ai-server-vmware-esxi-cosa-sappiamo-e-come-difendersi/
source: Over Security - Cybersecurity news aggregator
date: 2023-02-07
fetch_date: 2025-10-04T05:52:49.340419
---

# ESXiArgs, il ransomware dell’attacco ai server VMware ESXi: cosa sappiamo e come difendersi

[Vai al contenuto principale](#main-content)
[Vai al footer](#footer-content)

![logo](data:image/png;base64...)![logo](https://cdnd360.it/networkdigital360/nd360-neg.svg)

[I NOSTRI SERVIZI](https://www.cybersecurity360.it/about-network)

Menu

[![Vai alla homepage di CyberSecurity](data:image/png;base64...)![Vai alla homepage di CyberSecurity](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/03/cybersecurity_logo-768x55.png)](https://www.cybersecurity360.it)

## ESXiArgs, il ransomware dell’attacco ai server VMware ESXi: cosa sappiamo e come difendersi

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

# ESXiArgs, il ransomware dell’attacco ai server VMware ESXi: cosa sappiamo e come difendersi

* [Home](https://www.cybersecurity360.it)
* [Attacchi hacker e Malware: le ultime news in tempo reale](https://www.cybersecurity360.it/nuove-minacce/)
* [Ransomware](https://www.cybersecurity360.it/nuove-minacce/ransomware/)

Nei recenti attacchi su scala globale in cui sono stati presi di mira i server VMware ESXi non aggiornati gli attori della minaccia hanno utilizzato il nuovo ransomware ESXiArgs. Ecco tutti i dettagli e i consigli per mitigare la minaccia

Pubblicato il 06 Feb 2023

[Antonio Pontrelli](https://www.cybersecurity360.it/giornalista/antonio-pontrelli/)

Responsabile del SOC Exprivia

![ESXiArgs, il ransomware dell’attacco ai server VMware ESXi: cosa sappiamo e come difendersi](data:image/png;base64...)![ESXiArgs, il ransomware dell’attacco ai server VMware ESXi: cosa sappiamo e come difendersi](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2023/02/Ransomware-ESXiArgs.jpg)

Il 4 febbraio scoro il CSIRT Italia ha diramato un [bollettino](https://www.csirt.gov.it/contenuti/rilevato-lo-sfruttamento-massivo-della-cve-202121974-in-vmware-esxi-al01-230204-csirt-ita), poi ripreso in un comunicato stampa dell’Agenzia per la Cybersicurezza Nazionale, in merito allo sfruttamento massivo della vulnerabilità CVE-2021–21974 in VMware ESXi che ha consentito ad attori delle minacce di condurre attacchi a livello globale usando il **ransomware ESXiArgs**, così come avevamo [riportato nel nostro articolo di ieri](https://www.cybersecurity360.it/nuove-minacce/attacco-hacker-globale-cosa-sappiamo-degli-impatti-in-italia/).

Dal grafico seguente si può vedere come, attualmente, in Italia sono **5** i server ESXi vittime degli attacchi ransomware ESXiArgs, a fronte dei **791** server affetti in tutto il mondo.

![](data:image/png;base64...)![](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2023/02/word-image-62388-1.png)

#### Fonte: Osservatorio Cybersecurity di Exprivia.

Purtroppo questi numeri possono sia diminuire che aumentare. Diminuire perché gli amministratori di sistemi possono mettere offline i server fisici compromessi e aumentare perché nuovi server vengono compromessi.

Tralasciando per un momento l’attacco ai server VMware ESXi in corso, è utile soffermarsi su un aspetto non di poco conto. Attualmente **in Italia risultano esposti su Internet ben 1.018 server VMware ESXi** e in particolare la Login Page che, mediante un [**attacco di tipo brute force sulle password**](https://www.cybersecurity360.it/nuove-minacce/brute-force-cosa-sono-gli-attacchi-a-forza-bruta-come-farli-e-prevenirli/), consente di risalire alle credenziali d’accesso della console.

Purtroppo, le brutte notizie non finiscono qui perché dei 1.018 server VMware ESXi esposti su internet, il **78%** presenta una vecchia versione del sistema operativo, quindi con diverse vulnerabilità presenti e non ancora risolte.

![](data:image/png;base64...)![](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2023/02/Versioni-VMware-ESXi-esposte.jpg)

#### Fonte: Osservatorio Cybersecurity di Exprivia.

Gli attaccanti, dunque, prendono di mira i server VMware ESXi privi di patch di sicurezza sfruttando, come pubblicato dal CSIRT Italiano, la vulnerabilità **CVE-2021-21974**, resa nota il 4 gennaio 2021 e già patchata dal vendor il 23 febbraio 2021.

Qualora sfruttata, tale vulnerabilità, con score CVSS v3 pari a 8.8, di tipo “heap buffer overflow” sulla componente OpenSLP, può portare all’esecuzione di codice arbitrario da remoto: un attaccante che risiede nello stesso segmento di rete di ESXi, infatti, avendo accesso alla porta 427(porta utilizzata dal servizio SLP) può sfruttare la vulnerabilità del servizio OpenSLP con conseguente esecuzione di codice remoto.

Le versioni di VMware ESXi affette da tale vulnerabilità sono:

* VMware ESXi 6.5
* VMware ESXi 6.7
* VMware ESXi 7.0
* VMware Cloud Foundation (ESXi) 3.x
* VMware Cloud Foundation (ESXi) 4.x

Indice degli argomenti

* [I dettagli del nuovo ransomware ESXiArgs](#I_dettagli_del_nuovo_ransomware_ESXiArgs)
* [Come mitigare l’attacco ransomware a VMware ESXi](#Come_mitigare_lattacco_ransomware_a_VMware_ESXi)

## **I dettagli del nuovo ransomware ESXiArgs**

Sul server ESXi violato, vengono scaricati remotamente e salvati nella cartella **/tmp** i seguenti file:

* **Encrypt*...