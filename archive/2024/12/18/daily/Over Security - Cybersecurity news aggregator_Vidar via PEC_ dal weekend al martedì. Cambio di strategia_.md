---
title: Vidar via PEC: dal weekend al martedì. Cambio di strategia?
url: https://cert-agid.gov.it/news/vidar-via-pec-dal-weekend-al-martedi-cambio-di-strategia/
source: Over Security - Cybersecurity news aggregator
date: 2024-12-18
fetch_date: 2025-10-06T19:44:20.307479
---

# Vidar via PEC: dal weekend al martedì. Cambio di strategia?

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
* Vidar via PEC: dal weekend al martedì. Cambio di strategia?

# Vidar via PEC: dal weekend al martedì. Cambio di strategia?

17/12/2024

 [PEC](https://cert-agid.gov.it/tag/pec/)
[vidar](https://cert-agid.gov.it/tag/vidar/)

Nelle prime ore del 17 dicembre 2024, Vidar è tornato a colpire con una nuova campagna malware mirata agli utenti italiani, sfruttando ancora una volta **caselle PEC compromesse**. A differenza delle precedenti ondate, che erano state veicolate nella notte tra domenica e lunedì, questa campagna è stata distribuita nella mattina di martedì, probabilmente con l’obiettivo di raggiungere le vittime in un momento diverso della settimana.

![](https://cert-agid.gov.it/wp-content/uploads/2024/12/email_vidar.png)

Il vettore utilizzato è sempre lo stesso: un’e-mail scritta in modo formale, con un linguaggio convincente e intimidatorio, che simula un sollecito di pagamento legato a un presunto contratto inadempiuto. Nel corpo del messaggio, un link invita a scaricare una “*fattura*” che, in realtà, è un file **JavaScript malevolo** denominato *Fattura.js*. Questo file, una volta aperto, innesca l’infezione del sistema, permettendo al malware di sottrarre informazioni sensibili.

## Domini random e temporizzati

La campagna è stata rilevata alle 00:30, e le operazioni di mitigazione, in collaborazione con i Gestori PEC, sono iniziate pochi minuti dopo, alle 00:35. Nel corso del monitoraggio sono stati identificati e bloccati **133 domini di secondo livello** utilizzati per distribuire il malware. [Come osservato nella campagna precedente](https://cert-agid.gov.it/news/il-malware-vidar-evolve-con-nuove-strategie-di-diversificazione-dei-domini/), gli URL, che sfruttano path randomizzati per complicare l’identificazione preventiva, sono **rimasti inattivi nelle prime fasi dell’attacco**, per poi attivarsi nelle ore successive.

## Cambiamento di strategia o contrattempo?

La ripetizione di queste campagne mette in luce l’adattabilità degli attori dietro Vidar, sempre pronti a modificare non solo i dettagli tecnici, come gli URL e i metodi di distribuzione, ma anche la tempistica degli attacchi. La scelta di veicolare questa campagna nelle prime ore di un martedì mattina, anziché nella consueta finestra tra domenica e lunedì, potrebbe riflettere diversi fattori. Potrebbe trattarsi di un semplice problema logistico occorso durante il fine settimana, che ha ritardato l’attivazione del malware. Oppure, potrebbe essere una strategia deliberata, volta a colpire gli utenti in un momento di maggiore operatività, quando sono già concentrati sulle attività lavorative e meno inclini a sospettare di e-mail ricevute di primo mattino. Qualunque sia la ragione, questo cambiamento sottolinea l’attenzione dei criminali nel variare approcci e tempistiche per massimizzare l’efficacia delle loro campagne.

## Azioni di contrasto

Le attività di contrasto sono state già messe in atto con il supporto dei Gestori PEC. Gli IoC relativi alla campagna sono stati diramati attraverso il [Feed IoC](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/) del CERT-AGID verso i Gestori PEC e verso le strutture accreditate.

Si raccomanda di prestare sempre la massima attenzione alle comunicazioni ricevute via PEC, in particolare quando contengono link ritenuti sospetti. Nel dubbio, è sempre possibile inoltrare le email ritenute sospette alla casella di posta **malware@cert-agid.gov.it**

## Indicatori di Compromissione

Al fine di rendere pubblici i dettagli della campagna odierna si riportano di seguito gli IoC rilevati:

**Link:** [Download IoC](https://cert-agid.gov.it/wp-content/uploads/2024/12/vidar_17-12-2024.json)

Taggato
[PEC](https://cert-agid.gov.it/tag/pec/)
[vidar](https://cert-agid.gov.it/tag/vidar/)

## Navigazione articoli

[Notizia precedente Sintesi riepilogativa delle campagne malevole nella settimana del 7 – 13 dicembre](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-7-13-dicembre/)

[Prossima notizia: Falso avviso di consegna: una nuova campagna di smishing colpisce gli utenti di Poste Italiane](https://cert-agid.gov.it/news/falso-avviso-di-consegna-una-nuova-campagna-di-smishing-colpisce-gli-utenti-di-poste-italiane/)

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