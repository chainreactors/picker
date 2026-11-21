---
title: Nuove vulnerabilità critiche e sfruttate ITW, attacchi alla penisola italiana, campagne APT e cyberspionaggio
url: https://www.telsy.com/nuove-vulnerabilita-critiche-e-sfruttate-itw-attacchi-alla-penisola-italiana-campagne-apt-e-cyberspionaggio/
source: Over Security
date: 2026-11-20
fetch_date: 2026-11-21T09:02:17.076037
---

# Nuove vulnerabilità critiche e sfruttate ITW, attacchi alla penisola italiana, campagne APT e cyberspionaggio

* Gruppo TIM

[![Telsy](https://www.telsy.com/wp-content/themes/telsy/images/Logo_Telsy_pos-hor_RGB.png)](https://www.telsy.com/)

[Per fare una ricerca scrivi qualcosa e premi "invio"](/?s=)

Chiudi

* [Chi siamo](https://www.telsy.com/chi-siamo/)
* Soluzioni
  + [Vai a Soluzioni](https://www.telsy.com/soluzioni/)
  + [Cyber](https://www.telsy.com/soluzioni/cyber-ita/)
  + [Crypto](https://www.telsy.com/soluzioni/crypto-ita/)
  + [Quantum](https://www.telsy.com/soluzioni/quantum-ita/)
* [Innovazione](https://www.telsy.com/innovazione/)
* [Lavora con noi](https://www.telsy.com/lavora-con-noi/)
* [Blog](https://www.telsy.com/blog/)

* News in evidenza
  + [20 Nov

    Nuove vulnerabilità critiche e sfruttate ITW, attacchi alla penisola italiana, campagne APT e cyberspionaggio](https://www.telsy.com/nuove-vulnerabilita-critiche-e-sfruttate-itw-attacchi-alla-penisola-italiana-campagne-apt-e-cyberspionaggio/)
  + [17 Nov

    La Fully Homomorphic Encryption: crittografia per la protezione del Cloud](https://www.telsy.com/fully-homomorphic-encryption-crittografia-protezione-cloud/)

[Nuove vulnerabilità critiche e sfruttate ITW, attacchi alla penisola italiana, campagne APT e cyberspionaggio](https://www.telsy.com/nuove-vulnerabilita-critiche-e-sfruttate-itw-attacchi-alla-penisola-italiana-campagne-apt-e-cyberspionaggio/)
[La Fully Homomorphic Encryption: crittografia per la protezione del Cloud](https://www.telsy.com/fully-homomorphic-encryption-crittografia-protezione-cloud/)
[Vedi tutte](https://www.telsy.com/blog/)

* [English](https://www.telsy.com/en/new-critical-vulnerabilities-exploited-itw-attacks-targeting-italy-apt-campaigns-and-cyberspionage/)
* [Italiano](https://www.telsy.com/nuove-vulnerabilita-critiche-e-sfruttate-itw-attacchi-alla-penisola-italiana-campagne-apt-e-cyberspionaggio/)

[Threat Intelligence](https://www.telsy.com/categoria/threat-intelligence/), [News](https://www.telsy.com/categoria/news/)

# Nuove vulnerabilità critiche e sfruttate ITW, attacchi alla penisola italiana, campagne APT e cyberspionaggio

20 Nov 2026

Condividi

## ![Weekly Threats hor Telsy](https://www.telsy.com/wp-content/uploads/Weekly-Threats-hor-Telsy.png)

## Vulnerabilità: falle sfruttate ITW e nuove criticità in PHP, Ruby, NGINX e Java

Il 17 e il 18 novembre 2026 la CISA ha aggiunto al catalogo KEV cinque vulnerabilità sfruttate ITW: **CVE-2026-115731** di Perforce Puppet Enterprise, una *Deserialization of Untrusted Data* che consente l’esecuzione di codice sul Puppet Server tramite un certificato agent valido, potenzialmente anche senza autenticazione in configurazioni con firma automatica non protetta; **CVE-2024-10441** di Synology DSM e BeeStation OS, che permette RCE ed è compresa nell’advisory richiamato dal produttore dopo recenti attacchi ransomware, senza conferme del suo specifico sfruttamento; **CVE-2026-40217** di BerriAI LiteLLM, che consente di aggirare la sandbox Python ed eseguire codice, sfruttata contro un honeypot per distribuire il miner [**XMRig**](https://www.telsy.com/tag/xmrig/); **CVE-2026-90436** di Apache Axis 1.x, una *Unsafe Reflection* che può permettere RCE non autenticata tramite messaggi SOAP malevoli, osservata contro Atlassian Confluence Data Center e segnalata anche su N-able N-central in configurazioni non predefinite; e **CVE-2026-90817** di Vanderbilt University REDCap, una *Code Injection* sfruttabile senza autenticazione conoscendo un hash valido di un sondaggio pubblico, anch’essa utilizzata in una campagna di distribuzione di XMRig. Parallelamente, il 17 novembre è stata divulgata **Java4Shell** (**CVE-2026-114938**), una *Heap-based Buffer Overflow* nel decoder Base64 di OpenJDK, che interessa specifiche versioni della JVM HotSpot su processori x86-64 con supporto AVX-512 VBMI. La falla può consentire RCE anche senza autenticazione, come dimostrato dai ricercatori su prodotti quali Keycloak, Jira, Confluence e Jenkins. Al 19 novembre GreyNoise aveva rilevato 187 richieste compatibili con tentativi di sfruttamento provenienti da cinque indirizzi IP malevoli, senza compromissioni confermate. Cloudflare ha inoltre osservato attività associate a Java4Shell e al framework AI ARTEX provenienti dallo stesso indirizzo IP, senza dimostrare l’impiego diretto del framework per sfruttare la falla. Il 18 novembre il progetto Ruby ha inoltre corretto sette vulnerabilità, collettivamente denominate **November2Shell**, che interessano la gestione delle espressioni regolari e delle stringhe. Tra queste figura **Ruby2Shell** (CVE-2026-132825), una *Heap Buffer Overflow* di un byte potenzialmente sfruttabile per RCE. Sono state dimostrate catene RCE per cinque delle sette falle, ma non risultano pubblici exploit RCE completi né confermati attacchi ITW. Sempre il 18 novembre sono state divulgate cinque vulnerabilità critiche di NGINX Open Source e NGINX Plus, denominate **NGINX2Root** e tutte valutate CVSS 9.2: **CVE-2026-123007** e **CVE-2026-123633** in HTTP/2, **CVE-2026-121810** in HTTP/3/QUIC, **CVE-2026-123634** nel resolver DNS e **CVE-2026-113425** nel mail proxy. Le falle possono consentire RCE non autenticata con i privilegi dei worker NGINX in specifiche configurazioni. I ricercatori hanno inoltre dimostrato un’escalation a root e l’evasione da container Docker concatenando una RCE con una distinta 0-day nel sottosistema SCTP del kernel Linux. Sono disponibili PoC pubbliche, mentre il 19 novembre il WASOC ha riferito segnalazioni di sfruttamento ITW di almeno una delle vulnerabilità HTTP/2, senza identificarla né fornire evidenze tecniche pubbliche. Infine, il 19 novembre il PHP Security Team ha corretto 18 vulnerabilità, di cui sette critiche. In particolare, per **CVE-2026-126714**, denominata **phpAfterShell**, i ricercatori hanno documentato una catena RCE che combina la manipolazione dei file di sessione con un’ulteriore vulnerabilità di corruzione della memoria in una classe nativa PHP. È disponibile una PoC pubblica per la manipolazione delle sessioni, mentre l’exploit RCE completo non è stato divulgato. Tra le ulteriori falle figura **CVE-2026-129291** (CVSS 8.8), che può consentire un’escalation locale dei privilegi fino a root in PHP-FPM. Non risultano confermati sfruttamenti ITW delle nuove vulnerabilità PHP.

## Italia: rilevate offensive di molteplici matrici

Nell’ultima settimana, il gruppo hacktivista [**Dark Storm Team**](https://www.telsy.com/tag/dark-storm-team/) ha rivendicato offensive DDoS ai danni di Fedespedi – Federazione nazionale delle imprese di spedizioni internazionali; Auta Marocchi S.p.A. (Autamarocchi); e Autotrasporti e Spedizioni Barone S.p.A.; mentre il collettivo hacktivista filorusso [**NoName057(16)**](https://www.telsy.com/tag/noname05716/) ha rivendicato due presunte compromissioni di sistemi di automazione degli edifici in Italia nell’ambito dell’operazione #OpItaly. In particolare, il 15 novembre ha dichiarato di aver ottenuto accesso completo al sistema domotico di una residenza presumibilmente riconducibile all’élite italiana, sostenendo di poter modificare climatizzazione, riscaldamento della piscina e illuminazione esterna. Il 19 novembre ha invece rivendicato l’accesso al sistema BMS/SCADA di un palazzetto sportivo italiano, affermando di poter intervenire su riscaldamento, ventilazione, centrale termica e produzione di acqua calda. Entrambe le rivendicazioni sono accompagnate da video dimostrativi e da messaggi contro il sostegno italiano all’Ucraina, ma non risultano conferme indipendenti delle compromissioni né di effettive alterazioni degli impianti. NoName057(16) figura, inoltre, tra i soggetti colpiti dalle nuove sanzioni adottate il 16 novembre dal Consiglio dell’Unione europea nei confronti di 30 persone fisiche e due entità, nell’ambito dei regimi relativi alle attività destabilizzanti russe e ai cyberattacchi. Il collettivo è stato sanzionato per le attività DDoS contro istituzioni, infrastrutture critiche e altri obiettivi europei. Tra le entità designate fi...