---
title: Maritime cybersecurity: vulnerabilità dei sistemi navali, AIS spoofing e GPS spoofing
url: https://www.ictsecuritymagazine.com/articoli/maritime-cybersecurity/
source: ICT Security Magazine
date: 2025-11-20
fetch_date: 2025-11-21T03:14:09.181766
---

# Maritime cybersecurity: vulnerabilità dei sistemi navali, AIS spoofing e GPS spoofing

[Salta al contenuto](#main)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

* [Home](https://www.ictsecuritymagazine.com/)
* [Articoli](https://www.ictsecuritymagazine.com/argomenti/articoli/)
* RubricheEspandi
  + [Cyber Security](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)
  + [Cyber Crime](https://www.ictsecuritymagazine.com/argomenti/cyber-crime/)
  + [Cyber Risk](https://www.ictsecuritymagazine.com/argomenti/cyber-risk/)
  + [Cyber Law](https://www.ictsecuritymagazine.com/argomenti/cyber-law/)
  + [Digital Forensic](https://www.ictsecuritymagazine.com/argomenti/digital-forensic/)
  + [Digital ID Security](https://www.ictsecuritymagazine.com/argomenti/digital-id-security/)
  + [Business Continuity](https://www.ictsecuritymagazine.com/argomenti/business-continuity/)
  + [Digital Transformation](https://www.ictsecuritymagazine.com/argomenti/digital-transformation/)
  + [Cyber Warfare](https://www.ictsecuritymagazine.com/argomenti/cyber-warfare/)
  + [Ethical Hacking](https://www.ictsecuritymagazine.com/argomenti/ethical-hacking/)
  + [GDPR e Privacy](https://www.ictsecuritymagazine.com/argomenti/gdpr-e-privacy/)
  + [IoT Security](https://www.ictsecuritymagazine.com/argomenti/iot-security/)
  + [Industrial Cyber Security](https://www.ictsecuritymagazine.com/argomenti/industrial-cyber-security/)
  + [Blockchain e Criptovalute](https://www.ictsecuritymagazine.com/argomenti/blockchain-e-criptovalute/)
  + [Intelligenza Artificiale](https://www.ictsecuritymagazine.com/argomenti/intelligenza-artificiale/)
  + [Geopolitica e Cyberspazio](https://www.ictsecuritymagazine.com/argomenti/geopolitica-cyberspazio/)
  + [Interviste](https://www.ictsecuritymagazine.com/argomenti/interviste/)
* [Notizie](https://www.ictsecuritymagazine.com/argomenti/notizie/)
* [Pubblicazioni](https://www.ictsecuritymagazine.com/pubblicazioni/)
* [Cybersecurity Video](https://www.ictsecuritymagazine.com/argomenti/cybersecurity-video/)
* [Eventi](https://www.ictsecuritymagazine.com/eventi/)
* [Newsletter](https://www.ictsecuritymagazine.com/newsletter/)

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine1403) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Forum ICT Security 2025](https://www.ictsecuritymagazine.com/wp-content/uploads/banner-header-2025.jpg)](https://www.ictsecuritymagazine.com/eventi/forumictsecurity2025)

![La maritime cybersecurity nel settore marittimo evidenzia come la digitalizzazione delle navi esponga sistemi critici a gravi rischi di cyberattacchi.](https://www.ictsecuritymagazine.com/wp-content/uploads/maritime-cybersecurity.jpeg)

# Maritime cybersecurity: vulnerabilità dei sistemi navali, AIS spoofing e GPS spoofing

A cura di:[Redazione](#molongui-disabled-link)  Ore 20 Novembre 202511 Novembre 2025

La digitalizzazione del settore marittimo ha generato un paradosso inquietante: mentre le navi moderne navigano con precisione millimetrica grazie a sistemi GPS, ECDIS e comunicazioni satellitari, questa stessa interconnessione le ha rese vulnerabili a minacce che i progettisti di vent’anni fa non avrebbero potuto immaginare. Il [settore marittimo trasporta oltre](https://unctad.org/topic/transport-and-trade-logistics/review-of-maritime-transport) l’80% del commercio mondiale, eppure la sua infrastruttura digitale presenta vulnerabilità sistemiche che sfidano i tradizionali paradigmi della sicurezza informatica.

A differenza degli ambienti IT convenzionali, i sistemi navali operano in una convergenza complessa tra tecnologie *legacy*, protocolli industriali non progettati per essere sicuri, e l’isolamento fisico che paradossalmente ha ritardato l’adozione di pratiche di *hardening* basilari. La [cybersecurity marittima non è](https://www.ictsecuritymagazine.com/articoli/cyber-risk-aeronautico-e-navale-una-comparazione-con-la-industrial-cybersecurity/) più una questione teorica da conferenze accademiche, ma una realtà operativa che interseca diritto internazionale, sicurezza nazionale e continuità del commercio globale.

## L’architettura delle vulnerabilità nei sistemi navali: convergenza IT/OT e protocolli non sicuri

I sistemi di bordo moderni rappresentano un ecosistema ibrido dove coesistono tecnologie OT (*Operational Technology*) e IT tradizionale, spesso senza una vera segmentazione di rete. Gli *Electronic Chart Display and Information Systems* (ECDIS) dialogano con i sistemi di controllo del motore, che a loro volta sono connessi alle reti amministrative utilizzate dall’equipaggio per email e comunicazioni. Questa convergenza crea quella che in termini forensi definiremmo una “catena di compromissione continua”: l’accesso a un componente apparentemente secondario può diventare il vettore per il controllo di sistemi critici.

Il problema fondamentale risiede nella natura stessa dei protocolli marittimi. Il [sistema AIS è obbligatorio](https://www.imo.org/en/ourwork/safety/pages/ais.aspx) per navi sopra le 300 tonnellate lorde impegnate in viaggi internazionali, trasmette in chiaro su frequenze VHF non criptate (161.975 MHz e 162.025 MHz) informazioni critiche: identità della nave, posizione, rotta, velocità. Questa trasparenza, nata per prevenire collisioni e facilitare il monitoraggio del traffico marittimo secondo la Convenzione SOLAS, è diventata una superficie d’attacco permanente.

Con apparecchiature *Software Defined Radio* (SDR) dal costo di poche centinaia di euro, è possibile non solo intercettare ma anche iniettare messaggi AIS contraffatti. L’AIS *spoofing* non è un’ipotesi teorica. Il Center for Advanced Defense Studies (C4ADS) [ha documentato quasi 10.000](https://insidegnss.com/new-report-details-gnss-spoofing-including-denial-of-service-attacks/) incidenti di *spoofing* tra febbraio 2016 e novembre 2018, colpendo 1.311 imbarcazioni commerciali. Questi fenomeni rivelano pattern anomali difficilmente spiegabili con malfunzionamenti tecnici: navi che “teletrasportano” la propria posizione di centinaia di chilometri, *transponder* che riportano coordinate nel deserto, identità MMSI (*Maritime Mobile Service Identity*) duplicate simultaneamente in oceani diversi.

Dal punto di vista tecnico, l’AIS *spoofing* sfrutta l’assenza di autenticazione nei [protocolli NMEA 0183 e](https://www.nmea.org/) NMEA 2000, standard de facto nell’industria nautica. Un attaccante può trasmettere messaggi AIS Type 1, 2 o 3 (*position reports*) contraffatti utilizzando *software open source*, sovrapponendo la propria trasmissione a quella legittima sfruttando la potenza del segnale o il *timing*. La *detection* di questi attacchi richiede capacità di correlazione avanzata: confronto con dati radar indipendenti, analisi delle impossibilità fisiche (accelerazioni incompatibili con il tipo di nave), controllo della coerenza longitudinale dei dati trasmessi.

## GPS spoofing e jamming: come gli attacchi ai sistemi di navigazione minacciano la sicurezza marittima

Gli attacchi ai sistemi di navigazione rappresentano un’evoluzione qualitativa della minaccia. Nel giugno 2017, [nel Mar Nero oltre](https://maritime-executive.com/editorials/mass-gps-spoofing-attack-in-black-sea) venti navi hanno simultaneamente riportato posizioni GPS false che le collocavano all’aeroporto di Gelendžik, a decine di chilometri dalla loro posizione reale. Questo incidente, il primo caso documentato su larga scala di GPS *spoofing* marittimo, ha dimostrato la fattibilità operativa di questi attacchi su scala geografica ampia. Successive analisi hanno documentato fenomeni simili nel Golfo Persico, nel Mar Cinese Meridionale e nelle acque territoriali russe, suggerendo un uso sistematico di [tecnologie di *electronic...