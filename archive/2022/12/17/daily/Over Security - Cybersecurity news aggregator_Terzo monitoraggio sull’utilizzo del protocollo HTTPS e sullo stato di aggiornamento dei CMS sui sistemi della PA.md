---
title: Terzo monitoraggio sull’utilizzo del protocollo HTTPS e sullo stato di aggiornamento dei CMS sui sistemi della PA
url: https://cert-agid.gov.it/news/terzo-monitoraggio-sullutilizzo-del-protocollo-https-e-sullo-stato-di-aggiornamento-dei-cms-sui-sistemi-della-pa/
source: Over Security - Cybersecurity news aggregator
date: 2022-12-17
fetch_date: 2025-10-04T01:48:12.038298
---

# Terzo monitoraggio sull’utilizzo del protocollo HTTPS e sullo stato di aggiornamento dei CMS sui sistemi della PA

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
* Terzo monitoraggio sull’utilizzo del protocollo HTTPS e sullo stato di aggiornamento dei CMS sui sistemi della PA

# Terzo monitoraggio sull’utilizzo del protocollo HTTPS e sullo stato di aggiornamento dei CMS sui sistemi della PA

16/12/2022

 [CMS](https://cert-agid.gov.it/tag/cms/)
[HTTPS](https://cert-agid.gov.it/tag/https/)

Come previsto dal [Piano Triennale](https://docs.italia.it/italia/piano-triennale-ict/pianotriennale-ict-doc/it/2020-2022/capitolo-6-sicurezza-informatica/obiettivi-e-risultati-attesi-5.html) per l’informatica nella Pubblica Amministrazione, AgID ha effettuato una nuova rilevazione (di seguito *monitoraggio*) sull’utilizzo del protocollo HTTPS e lo stato di aggiornamento dei CMS nei sistemi della Pubblica Amministrazione.

Anche per questo terzo monitoraggio sono state utilizzate le [metodologie](https://cert-agid.gov.it/news/secondo-monitoraggio-dello-stato-di-aggiornamento-del-protocollo-https-e-dei-cms-sui-sistemi-della-pa/#Metodologia) già descritte in precedenza.

### Indice dei risultati

* [Risultati della scansione HTTPS](#https)
* [Risultati della scansione CMS](#cms)
* [Dati di utilizzo del servizio di autoverifica HTTPS/CMS](#autoverifica)
* [Conclusioni e osservazioni](#conclusioni)

# Risultati della scansione HTTPS

I siti soggetti a scansione per la verifica del protocollo HTTPS sono raggruppati in quattro categorie [come spiegato](https://cert-agid.gov.it/news/secondo-monitoraggio-dello-stato-di-aggiornamento-del-protocollo-https-e-dei-cms-sui-sistemi-della-pa/#Metodologia) nel monitoraggio del 2021:

* *Siti senza HTTPS*. Sono i siti che non implementano il protocollo HTTPS.
* *Siti con gravi problemi di sicurezza*. Sono i siti che hanno HTTPS ma la configurazione adottata è facilmente aggirabile (es: non hanno un certificato valido).
* *Siti malconfigurati*. Sono i siti che hanno HTTPS ma la configurazione usata, sebbene non immediatamente vulnerabile, non è più considerata idonea agli standard moderni (es: uso di cifrari CBC).
* *Siti sicuri*. Sono i siti che hanno HTTPS e la configurazione è adeguata agli standard moderni.

La percentuale di siti che utilizza una corretta configurazione **HTTPS** è più che **raddoppiata** (da 4149 a 9022) rispetto allo scorso anno (2021) e **quadruplicata** rispetto a due anni fa (erano 1766 nel 2020). Il miglioramento sul fronte dell’utilizzo di HTTPS è principalmente dovuto alle azioni correttive legate alla **rimozione del supporto alle versioni obsolete di TLS** (TLS 1.0 e 1.1) e, in misura minore, alla **forzatura dell’utilizzo di HTTPS tramite redirect da HTTP.**

![](https://cert-agid.gov.it/wp-content/uploads/2022/12/image-1024x637.png)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Categoria** | **Anno 2021** | **%** | **Anno 2022** | **%** |
| Sicuri | 4149 | 22% | 9022 | 47% |
| Gravi problemi | 10092 | 53% | 7802 | 41% |
| Mal configurati | 4549 | 23% | 2218 | 11% |
| Senza HTTPS | 340 | 2% | 223 | 1% |

### Siti senza HTTPS

Un importante miglioramento riguarda anche la percentuale di siti che **non supporta il protocollo HTTPS**. Rispetto ai risultati emersi dalla scansione precedente (2021) si è riscontrata una **diminuzione del 34%** (da 340 a 223 unità) e, rispetto alla scansione di due anni fa, il numero si è dimezzato (erano 445 nel 2020).

### Siti con gravi problemi di sicurezza

In questa categoria rientrano i siti con HTTPS facilmente aggirabile (es: certificato non corretto) o debole (es: cifrari con chiavi piccole o senza confidenzialità).

Questa è la categoria più complessa da analizzare: in termini assoluti la recente scansione ha evidenziato una dimuzione di circa 2200 unità di siti problematici.

Nei dettagli si nota però che le principali variazioni sono:

* Circa 2100 siti hanno implementato il redirect da HTTP ad HTTPS.
* Sono diminuiti i siti che facevano un redirect *verso HTTP* di circa 300 unità.
* C’è stata una diminuzione assoluta di quasi 1800 siti che hanno il certificato non corretto.
* Sono dimezzati i siti che usano al *massimo* TLS 1.0 e TLS 1.1 (da circa 4900 a circa 2200).

Si evidenzia quindi un abbandono delle versioni obsolete di TLS che, insieme ad uso corretto del reindirizzamento ad HTTPS ed all’utilizzo di un certificato valido, hanno portato ad un deciso ridimensionamento di questa categoria (dal 53% dei siti totali nel 2021 ad un 41% dei siti del 2022).

Al momento, la maggior parte dei siti della PA (il 47%) usa HTTPS in modo sicuro. Tuttavia i siti con gravi problemi di sicurezza sono ancora piuttosto vicini in termini percentuali (41%).
In questo anno si delinea quindi una dicotomia in cui da una parte ci sono siti correttamente configurati e dall’altra siti che hanno gravi errori di configurazione. Tra le due situazioni, i siti “irrecuperabili” (senza HTTPS) sono relativamente pochi (1%) mentre i restanti (11%) sono “quasi” correttamente configurati.

![](https://cert-agid.gov.it/wp-content/uploads/2022/12/image-2-1024x624.png)

|  |  |  |
| --- | --- | --- |
| **Problematica** | **2021** | **2022** |
| SSL 2.0 | 23 | 15 |
| SSL 3.0 | 581 | 390 |
| TLS 1.0 | 4864 | 2169 |
| TLS 1.1 | 4970 | 2256 |
| Certificato non...