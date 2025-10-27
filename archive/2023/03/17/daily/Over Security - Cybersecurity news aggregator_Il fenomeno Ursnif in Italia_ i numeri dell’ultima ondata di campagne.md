---
title: Il fenomeno Ursnif in Italia: i numeri dell’ultima ondata di campagne
url: https://cert-agid.gov.it/news/malware/il-fenomeno-ursnif-in-italia-i-numeri-dellultima-ondata-di-campagne/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-17
fetch_date: 2025-10-04T09:53:05.533712
---

# Il fenomeno Ursnif in Italia: i numeri dell’ultima ondata di campagne

* [Vai al contenuto](#main)
* [Vai alla navigazione del sito](#menu "accedi al menu")

[![Logo CERT-AGID](/wp-content/themes/cert-agid/assets/images/cert-agid-logo-white.svg)](https://cert-agid.gov.it/)

# [CERT-AGID Computer Emergency Response Team AGID](https://cert-agid.gov.it/)

[Agenzia per
l'Italia Digitale](https://www.agid.gov.it)

[![Logo AgID - Agenzia per l'Italia Digitale](/wp-content/themes/cert-agid/assets/images/logo-agid.svg)](https://www.agid.gov.it)

Seguici su

* [RSS](https://cert-agid.gov.it/feed/ "RSS")
* [Telegram](https://t.me/certagid "Telegram")
* [X / Twitter](https://twitter.com/agidcert "X / Twitter")

cerca nel sito

[Menu](#menu "accedi al menu")

![Logo del CERT-PA](/wp-content/themes/cert-agid/assets/images/cert-agid-logo-black.svg)
CERT-AGID

<https://cert-agid.gov.it/>

## Menu di navigazione

* Documentazione
  + [Documenti AGID](https://cert-agid.gov.it/documenti-agid/)
  + [Pillole informative](https://cert-agid.gov.it/pillole-informative/)
  + [Flusso IoC](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/)
* [Chi siamo](https://cert-agid.gov.it/chi-siamo/)
* [Contatti](https://cert-agid.gov.it/contatti/)
* [Strumenti](https://cert-agid.gov.it/strumenti/)
  + [hashr](https://cert-agid.gov.it/hashr/)
  + [Verifica HTTPS e CMS](https://cert-agid.gov.it/verifica-https-cms/)
  + [Statistiche sulle campagne italiane di malware e phishing](https://cert-agid.gov.it/statistiche/)
* [Glossario](https://cert-agid.gov.it/glossario/)
  + [0day](https://cert-agid.gov.it/glossario/0day/)
  + [Botnet](https://cert-agid.gov.it/glossario/botnet/)
  + [Data breach](https://cert-agid.gov.it/glossario/data-breach/)
  + [DDOS-DOS](https://cert-agid.gov.it/glossario/ddos-dos/)
  + [Deep-Dark web](https://cert-agid.gov.it/glossario/deep-dark-web/)
  + [Defacing](https://cert-agid.gov.it/glossario/defacing/)
  + [Exploit](https://cert-agid.gov.it/glossario/exploit/)
  + [MITM](https://cert-agid.gov.it/glossario/mitm/)
  + [OSINT-CLOSINT](https://cert-agid.gov.it/glossario/osint-closint/)
  + [Phishing](https://cert-agid.gov.it/glossario/phishing/)
  + [Privilege escalation](https://cert-agid.gov.it/glossario/privilege-escalation/)
  + [Spam](https://cert-agid.gov.it/glossario/spam/)
  + [Spoofing](https://cert-agid.gov.it/glossario/spoofing/)
  + [SQLi-SQL Injection](https://cert-agid.gov.it/glossario/sqli-sql-injection/)
  + [XSS](https://cert-agid.gov.it/glossario/xss/)
* Link utili
  + [Agenzia per l’Italia Digitale](https://www.agid.gov.it/)
  + [CSIRT Italia](https://csirt.gov.it)
  + [CERT-GARR](https://www.cert.garr.it/)
  + [CNAIPIC](https://www.commissariatodips.it/profilo/cnaipic/index.html)
  + [CERT-DIFESA](https://www.difesa.it/smd/cor/cert-difesa/25338.html)

* [Home](https://cert-agid.gov.it/)
* [Notizie](https://cert-agid.gov.it/category/news/)
* [Malware](https://cert-agid.gov.it/category/news/malware/)
* Il fenomeno Ursnif in Italia: i numeri dell’ultima ondata di campagne

# Il fenomeno Ursnif in Italia: i numeri dell’ultima ondata di campagne

16/03/2023

 [Ursnif](https://cert-agid.gov.it/tag/ursnif/)

Come già anticipato dal CERT-AgID nelle scorse settimane, l’Italia è stata interessata da una importante campagna volta a distribuire il malware Ursnif. Dall’inizio del mese di marzo ad oggi sono state osservate almeno quattro campagne, che hanno avuto come temi **Agenzia delle Entrate** e MISE/MEF e che si sono distinte per il loro considerevole volume.

Il CERT-AgID ha contribuito al contrasto di questa ondata condividendo i dati relativi agli specifici IoC tramite il suo [apposito servizio](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/) e tramite post sui suoi canali social ([Telegram](https://t.me/certagid/454) e [Twitter](https://twitter.com/AgidCert/status/1632686769203302402)).

Il solo numero di indicatori individuati (più di 1200) rende l’idea della dimensione del fenomeno.

![](https://cert-agid.gov.it/wp-content/uploads/2023/03/image-1024x411.png)

**Ursnif è noto per variare spesso le sue TTP:** la tecnica maggiormente sfruttata consiste nell’uso di un [link dinamico di Firebase](https://firebase.google.com/docs/dynamic-links) presente all’interno dell’e-mail per indirizzare la vittima verso una pagina di smistamento ospitata su un server compromesso da cui si viene poi indirizzati verso un file di tipo ZIP, anch’esso ospitato su un server compromesso, contenente il *payload* (un collegamento ad un eseguibile su una share pubblica).

![](https://cert-agid.gov.it/wp-content/uploads/2023/03/image140.png)

Durante le azioni legate all’analisi e al contrasto del fenomeno è stato possibile recuperare alcune informazioni lasciate disponibili nelle pagine di smistamento. Queste sono localizzate su un unico server di backend dal quale sono state ricavate abbastanza liberamente informazioni sulle sue attività.

Questo tipo di informazioni ci hanno permesso di effettuare un’analisi più dettagliata sull’entità delle ondate di malware a cui abbiamo assistito.

## I dati delle campagne

I dati ritrovati contengono informazioni come indirizzo IP, User-Agent, data, ora, geolocalizzazione e classificazione dei dispositivi che hanno visitato la pagina di smistamento. Queste visite non corrispondono esattamente al numero di infezioni avvenute poichè un certo numero di vittime si ferma prima di aprire l’archivio ZIP e anche perchè una percentuale di visite proviene dai motori di ricerca e da strumenti automatici. Tuttavia osserveremo come vi sia un’evidente correlazione tra i picchi di visite ed i giorni in cui sono avvenute le campagne. Quanto di seguito riportato riguardano numeri relativi alle “visite” e non alle “infezioni”.

Al momento dell’analisi dei dati erano quasi **380.000** le visite alle pagine di smistamento. Il backend usato per indirizzare le vittime al payload è in grado di rilevare se la visita proviene da uno strumento automatico, ad esempio un motore di ricerca, per cui delle 380.000 visite solo **40.000** sono state classificate come provenienti da strumenti automatici.

### Le visite distribuite per giorno

![](https://cert-agid.gov.it/wp-content/uploads/2023/03/image-1-1024x475.png)

[[E’ disponibile una versione interattiva di questo grafico]](/wp-content/uploads/2023/03/ursnif-timeseries.html)

Due particolari risultano rilevanti in questo grafico:

1. Il numero di visite è piuttosto elevato, con picchi che toccano quasi 70.000 visite al giorno.
2. I picchi corrispondono ai giorni in cui sono iniziate le quattro campagne Ursnif che hanno interessato l’Italia nelle ultime due settimane.

### La heatmap

Può risultare interessante provare ad usare una *heatmap* per evidenziare eventuali ricorrenze nelle TTP di Ursnif. In particolare, provare a disegnare una mappa dei giorni e delle ore più “calde”, ovvero con più visite:

![](https://cert-agid.gov.it/wp-content/uploads/2023/03/image-2-1024x477.png)

Visite per giorno della settimana nell’ultimo mese (20/02/2023 – 20/03/2023)

![](https://cert-agid.gov.it/wp-content/uploads/2023/03/image-3-1024x477.png)

Visite per ora del giorno dal 21/02/2023 al 15/03/2023

[[E’ disponibile una versione interattiva di questo grafico]](/wp-content/uploads/2023/03/ursnif-heatmaps.html)

Si può notare come le campagne Ursnif siano pricipalmente concentrate nel mezzo della settimana (tra mercoledì e giovedì) ma lunedì 6 marzo Ursnif ha lanciato un’ulteriore campagna che ha prodotto notevoli risultati in termini di visite.

L’ora salvata nelle informazioni delle visite non è di facile interpretazione poichè non comprende il fuso orario. Ipotizzando che gli orari siano in UTC, la heatmap mostra che le visite siano raggruppate tutte nelle prima parte della giornata (l’Italia è un’ora avanti rispetto agli orari mostrati). Si evidenzia un picco nella notte tra il 6 ed il 7 marzo che non è di facile interpretazione, probabilmente dovuto a motori di ricerca o a *spillover* in altri Paesi.

### Visite per lingua

È evidente, come si evinc...