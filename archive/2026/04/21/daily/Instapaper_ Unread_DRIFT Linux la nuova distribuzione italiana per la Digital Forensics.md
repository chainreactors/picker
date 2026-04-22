---
title: DRIFT Linux la nuova distribuzione italiana per la Digital Forensics
url: https://www.forenser.it/drift-linux-una-nuova-distribuzione-forense/
source: Instapaper: Unread
date: 2026-04-21
fetch_date: 2026-04-22T04:45:17.123813
---

# DRIFT Linux la nuova distribuzione italiana per la Digital Forensics

Search for:

 Search

Menu

Close

* [Servizi](https://www.forenser.it/servizi-informatica-forense/)
* [Formazione](https://www.forenser.it/formazione/)
* [News](https://www.forenser.it/news/)
* [Staff](https://www.forenser.it/staff/)
* [Press](https://www.forenser.it/press/)
  + [Video e TV](https://www.forenser.it/press/video-tv/)
  + [Radio](https://www.forenser.it/press/radio/)
  + [Quotidiani e Periodici](https://www.forenser.it/press/quotidiani-e-periodici/)
* [Guide](https://www.forenser.it/category/guide/)
* [Contatti](https://www.forenser.it/contatti/)
  + [Cookie Policy](https://www.forenser.it/contatti/cookie-policy/)
  + [Privacy Policy](https://www.forenser.it/contatti/privacy-policy/)

Search for:

 Search

[![Forenser Srl](https://www.forenser.it/wp-content/uploads/forenser-digital-investigations.png)](https://www.forenser.it/)

[Forenser Srl](https://www.forenser.it/)

Studio Informatica Forense

* [Servizi](https://www.forenser.it/servizi-informatica-forense/)
* [Formazione](https://www.forenser.it/formazione/)
* [News](https://www.forenser.it/news/)
* [Staff](https://www.forenser.it/staff/)
* [Press](https://www.forenser.it/press/)
  + [Video e TV](https://www.forenser.it/press/video-tv/)
  + [Radio](https://www.forenser.it/press/radio/)
  + [Quotidiani e Periodici](https://www.forenser.it/press/quotidiani-e-periodici/)
* [Guide](https://www.forenser.it/category/guide/)
* [Contatti](https://www.forenser.it/contatti/)
  + [Cookie Policy](https://www.forenser.it/contatti/cookie-policy/)
  + [Privacy Policy](https://www.forenser.it/contatti/privacy-policy/)

# DRIFT Linux: la nuova distribuzione italiana per la Digital Forensics

[![](https://secure.gravatar.com/avatar/65af508883433ee06fa507bcdcb1e77747fc2aba840a2130e6877e5be7ffdded?s=44&d=mm&r=g)](https://www.forenser.it/author/forenser/ "Posts by forenser")

[forenser](https://www.forenser.it/author/forenser/)
on
17 Aprile 2026

![DRIFT Linux](https://www.forenser.it/wp-content/uploads/Istantanea_2026-04-16_14-37-54.jpg)

******Estratto dell’interfaccia desktop di DRIFT Linux******

Nell’ambito delle distribuzioni Linux dedicate alla Digital Forensics e all’Incident Response, è stata recentemente rilasciata **DRIFT Linux** (Digital Forensics & Incident Response Toolkits), una nuova distribuzione italiana ideata da **Massimiliano Dal Cero**, basata su **Ubuntu 24.04 LTS (Noble)**.

Dalle prime informazioni disponibili e dai primi test svolti, il progetto sembra orientato a rispondere a esigenze operative concrete sul campo, si avvia velocemente, è una live distro forense completa dei tool indispensabili per la fase di acquisizione e copia forense ed è compatibile con buona parte dei dispositivi.

In Forenser dedichiamo costante attenzione alla ricerca e alla valutazione degli strumenti disponibili per le attività di analisi forense. Abbiamo avuto modo di testare **DRIFT Linux** nelle prime ore dalla sua uscita e in questo articolo condividiamo una prima panoramica delle caratteristiche tecniche che hanno attirato la nostra attenzione. Un approfondimento tecnico completo sarà disponibile a breve sul nostro sito.

Table of Contents

Toggle

* [Secure Boot Ready](#Secure_Boot_Ready)
* [Kernel Write Blocker nativo](#Kernel_Write_Blocker_nativo)
* [DRIFT Mount Manager e Connection Panel](#DRIFT_Mount_Manager_e_Connection_Panel)
* [DRIFT Forensics Web Acquire](#DRIFT_Forensics_Web_Acquire)
* [Acquisizione forense classica con Guymager](#Acquisizione_forense_classica_con_Guymager)
* [OpenTimestamps e tracciabilità delle evidenze](#OpenTimestamps_e_tracciabilita_delle_evidenze)
* [Conclusioni preliminari](#Conclusioni_preliminari)

## Secure Boot Ready

Uno degli aspetti che ha subito catturato la nostra attenzione riguarda la **compatibilità con Microsoft Secure Boot**. La distribuzione live si avvia su sistemi con Secure Boot abilitato senza richiedere la disattivazione dell’opzione nel BIOS/UEFI: una semplificazione operativa concreta, soprattutto quando si interviene su hardware moderno o in contesti aziendali in cui modificare le impostazioni di sicurezza potrebbe non essere possibile o opportuno.

## Kernel Write Blocker nativo

La protezione dell’integrità dei dati è gestita direttamente **a livello kernel**. I dispositivi collegati vengono mantenuti in sola lettura per impostazione predefinita fin dalle prime fasi del boot, riducendo il rischio di alterazioni accidentali sui supporti originali. L’eventuale sblocco in scrittura richiede un’azione esplicita da parte dell’operatore, con avviso ben visibile nell’interfaccia.

## DRIFT Mount Manager e Connection Panel

Il sistema include interfacce grafiche dedicate al controllo dell’ambiente di analisi. Il **Mount Manager** consente di gestire lo stato dei mount in modalità RO/RW, mentre il **Connection Panel** permette di governare in modo consapevole la connettività di rete — profilo particolarmente delicato in ambito forense, dove l’attivazione della rete deve avvenire solo quando necessario e in modo controllato.

## DRIFT Forensics Web Acquire

Tra i moduli di maggiore interesse vi è quello dedicato alla **web forensic acquisition**, che nei nostri primi test ha mostrato un workflow strutturato di raccolta e documentazione tecnica. Il modulo include la raccolta delle informazioni di rete, la cattura del traffico in formato **PCAP**, le chiavi **TLS/SSL**, la registrazione dello schermo e la generazione di un report finale. Un approccio integrato che semplifica la documentazione delle attività di acquisizione web.

## Acquisizione forense classica con Guymager

Tra gli strumenti integrati in DRIFTLinux figura Guymager, soluzione ampiamente collaudata per l’acquisizione forense di supporti fisici, che consente la creazione di immagini nei formati “.E01/.Exx” e “.dd”, il calcolo dei valori di hash MD5, SHA-1 e SHA-256, e la successiva verifica finale dell’acquisizione, al fine di confermare la corrispondenza tra la sorgente e la copia forense generata.

## OpenTimestamps e tracciabilità delle evidenze

Un ulteriore aspetto di interesse presente in DRIFT Linux è la possibilità di associare alle evidenze una **marcatura temporale verificabile tramite OpenTimestamps**, aggiungendo un livello aggiuntivo di tracciabilità al workflow di acquisizione. Si tratta di un elemento che contribuisce a rafforzare la verificabilità tecnica delle evidenze digitali prodotte.

## Conclusioni preliminari

Le prime analisi svolte nelle ore successive al rilascio di DRIFTLinux restituiscono l’immagine di un progetto tecnicamente interessante e chiaramente orientato alle esigenze operative della Digital Forensics, operativo e concreto.

Nei prossimi giorni pubblicheremo un **articolo dedicato** con un’analisi più approfondita delle principali funzionalità, nel frattempo, vi invitiamo a scoprire il progetto sul sito ufficiale: [driftlinux.org](https://driftlinux.org)

* Category:
  [Senza categoria](https://www.forenser.it/category/senza-categoria/)
* Tag:
  [acquisizione forense](https://www.forenser.it/tag/acquisizione-forense/), [copia forense](https://www.forenser.it/tag/copia-forense/), [digital forensics](https://www.forenser.it/tag/digital-forensics/), [indagini digitali](https://www.forenser.it/tag/indagini-digitali/), [informatica forense](https://www.forenser.it/tag/informatica-forense/)

## Navigazione articoli

[Previous: Previous post: Paolo Dal Checco e Andrea Galeazzi sul furto del canale Youtube](https://www.forenser.it/paolo-dal-checco-youtube-andrea-galeazzi-furto-hack-canale/)

## Contattaci

Email: info@forenser.it
PEC: forenser@pec.it
Telefono: 011 0447832
Fax: 011 19113070

## Dove Siamo

Forenser Srl
Via Schiaparelli, 12
10148 Torino (TO)
Italia

## Dati Fiscali

Forenser S.r.l.
P.IVA: 12385520015
REA: TO-1285941
Capitale Sociale: 10.000 € I.V.

©2023 Forenser Srl