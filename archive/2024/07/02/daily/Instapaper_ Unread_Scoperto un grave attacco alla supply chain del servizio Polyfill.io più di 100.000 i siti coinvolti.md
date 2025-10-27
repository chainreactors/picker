---
title: Scoperto un grave attacco alla supply chain del servizio Polyfill.io più di 100.000 i siti coinvolti
url: https://cert-agid.gov.it/news/scoperto-un-grave-attacco-alla-supply-chain-del-servizio-polyfill-io-piu-di-100-000-i-siti-coinvolti/
source: Instapaper: Unread
date: 2024-07-02
fetch_date: 2025-10-06T17:50:11.355959
---

# Scoperto un grave attacco alla supply chain del servizio Polyfill.io più di 100.000 i siti coinvolti

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
* Scoperto un grave attacco alla supply chain del servizio Polyfill.io: più di 100.000 i siti coinvolti

# Scoperto un grave attacco alla supply chain del servizio Polyfill.io: più di 100.000 i siti coinvolti

27/06/2024

 [polyfill](https://cert-agid.gov.it/tag/polyfill/)

Un recentissimo attacco alla supply chain ha colpito **Polyfill.io**, un web service ampiamente diffuso e utilizzato da **oltre 100.000 siti web**, che consente di garantire la compatibilità con le moderne funzionalità offerte dai browser più recenti anche ai browser più datati. In sostanza, un *polyfill* è un pezzo di codice, comunemente JavaScript, che aggiunge funzionalità moderne a browser più vecchi che nativamente non le supportano. E’ stato riscontrato che il dominio associato al servizio, **cdn.polyfill.io**, è stato compromesso, il ché ha favorito la possibilità di effettuare *injection* di codice malevolo al fine di ottenere reindirizzamenti a siti fraudolenti tramite i quali vengono catturati dati sensibili degli utenti.

# I fatti

[È stato scoperto](https://www-theregister-com.cdn.ampproject.org/c/s/www.theregister.com/AMP/2024/06/25/polyfillio_china_crisis/) che nel febbraio 2024, una compagnia cinese di nome ***Funnull*** ha acquistato il dominio *cdn.polyfill.io* e l’account GitHub associato. Successivamente a questa acquisizione il codice originale *polyfill.js* è stato alterato per generare script malevoli che si attivano in base agli header HTTP inviati dal browser dell’utente. Il client viene quindi indirizzato ad un falso dominio di Google Analytics (*www.googie-anaiytics[.]com*) che porta a siti indesiderati.

# Le vittime

[Risulta](https://www.bleepingcomputer.com/news/security/polyfillio-javascript-supply-chain-attack-impacts-over-100k-sites/) inoltre che il codice malevolo è **progettato per evitare il rilevamento da parte di utenti amministratori** del sito o degli strumenti di analisi web: si attiva solo in orari specifici e principalmente **su dispositivi mobili**, ritarda la sua esecuzione e ignora le sessioni amministrative. Questi meccanismi sofisticati hanno permesso di colpire un vasto numero di utenti senza destare immediatamente dei sospetti. Tra le vittime importanti al momento si riscontrano JSTOR, Intuit e il World Economic Forum.
Lo stesso autore originale di Polyfill, Andrew Betts, dopo la vendita del dominio ha raccomandato di non utilizzare più questo servizio.

# Sospensione del dominio

Il registrar Namecheap, gestore del dominio malevolo, ha già preso [provvedimenti sospendendo](https://x.com/malwrhunterteam/status/1806074377383121148) e bonificando il dominio compromesso.

Alla luce di tutto quanto emerso fin’ora, **si consiglia vivamente di rimuovere comunque del tutto Polyfill.io dai propri siti web**.

# Aggiornare le dipendenze

E’ fondamentale che i siti web che fanno riferimento al dominio originale di Polyfill aggiornino anche le loro dipendenze, poiché attualmente i servizi di Polyfill.io non sono più erogati e ciò potrebbe causare malfunzionamenti ai servizi che prima lo utilizzavano.

# Le fonti pubbliche

Le prime evidenze raccolte da questo CERT da due importanti fonti pubbliche:

* <https://polykill.io/>
* [https://publicwww.com/](https://publicwww.com/websites/%22cdn.polyfill.io%22/)

fanno emergere che sono stati impattati anche numerosi siti della PA nazionale, motivo per cui il CERT-AgID si è già attivato per allertare e mitigare le conseguenze di questo attacco verso le entità della propria constituency e, più in generale, verso entità delle PA coinvolte.

# Gli IoC per la PA

Il CERT-AgID ha già diramato gli indicatori di compromissione verso le strutture pubbliche accreditate al [Flusso IoC](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/).

Taggato
[polyfill](https://cert-agid.gov.it/tag/polyfill/)

## Navigazione articoli

[Notizia precedente L’infostealer 0bj3ctivity è tornato in azione](https://cert-agid.gov.it/news/linfostealer-0bj3ctivity-e-tornato-in-azione/)

[Prossima notizia: Sintesi riepilogativa delle campagne malevole nella settimana del 22 – 28 Giugno 2024](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-22-28-giugno-2024/)

![Logo del CERT-PA](/wp-content/themes/cert-agid/assets/images/cert-agid-logo-white.svg)
CERT-AGID

cerca nel sito

* [Contatti](https://cert-agid.gov.it/contatti/)
* [Privacy](https://cert-agid.gov.it/privacy/)
* [Note legali](https://cert-agid.gov.it/note-legali/)

#### Seguici su

* [RSS](https://cert-agid.gov.it/feed/ "RSS")
* [Telegram](https://t.me/certagid "Telegram")
* [X / Twitter](https://twitter.com/agidcert "X / Twitter")

![Logo del CERT-PA](/wp-content/themes/cert-agid/assets/images/cert-agid-logo-black.svg)
CERT-AGID

<https://cert-agid.gov.it/>