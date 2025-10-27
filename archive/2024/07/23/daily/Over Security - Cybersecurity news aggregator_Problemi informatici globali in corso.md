---
title: Problemi informatici globali in corso
url: https://cert-agid.gov.it/news/problemi-informatici-globali-in-corso/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-23
fetch_date: 2025-10-06T17:44:34.189896
---

# Problemi informatici globali in corso

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
* Problemi informatici globali in corso

# Problemi informatici globali in corso

19/07/2024

 [BSoD](https://cert-agid.gov.it/tag/bsod/)
[CrowdStrike](https://cert-agid.gov.it/tag/crowdstrike/)
[Microsoft](https://cert-agid.gov.it/tag/microsoft/)

![](https://cert-agid.gov.it/wp-content/uploads/2024/07/111856107.webp)

*L’articolo verrà aggiornato progressivamente con ulteriori [dettagli risolutivi](#dettagli-risolutivi) o [informazioni sulle nuove minacce](#informazioni-sulle-nuove-minacce).*

Le prime analisi suggeriscono che l’origine del problema sia un malfunzionamento del software EDR dell’azienda **[CrowdStrike](https://www.crowdstrike.com/blog/statement-on-windows-sensor-update/)**, conosciuto come *Falcon Sensor*, che pare abbia compromesso il funzionamento delle applicazioni in cloud dell’ecosistema Microsoft 365 con il suo sistema operativo.

Un aggiornamento difettoso di questo software ha causato l’inutilizzabilità di numerosi PC e server a livello mondiale, provocando la comparsa della schermata blu di errore di Windows (BSoD).

Un dirigente di CrowdStrike [suggerisce di applicare un workaround](https://twitter.com/brody_n77/status/1814185935476863321) per sbloccare in emergenza una postazione impattata dal problema.

![](https://cert-agid.gov.it/wp-content/uploads/2024/07/Screenshot-from-2024-07-19-11-12-21.png)

La situazione è in continua evoluzione e attualmente sono in fase di studio soluzioni per risolvere il problema.

## Dettagli risolutivi

[20/07/2024] **CrowdStrike** ha [pubblicato un articolo](https://www.crowdstrike.com/blog/technical-details-on-todays-outage/) che riassume i dettagli tecnici dell’accaduto.

[21/07/2024] **Microsoft** [ha rilasciato](https://techcommunity.microsoft.com/t5/intune-customer-success/new-recovery-tool-to-help-with-crowdstrike-issue-impacting/ba-p/4196959) uno strumento USB per aiutare gli amministratori IT.

# Attenzione alle soluzioni alternative per aggirare il problema

![](https://cert-agid.gov.it/wp-content/uploads/2024/07/fake-update-crashstrike-1024x892.jpg)

Il CERT-AGID continua a monitorare le implicazioni e gli impatti dell’incidente informatico che ha causato un down massivo di servizi e sistemi legati a **Microsoft** e **CrowdStrike** questa mattina.

⚠️ È stato osservato che utenti malintenzionati stanno diffondendo false procedure di workaround tramite canali social, includendo link a siti malevoli o ingannevoli.

💣 Per proteggere la propria constituency da questo ulteriore rischio, il CERT sta fornendo [tramite il proprio feed](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/) gli **IoC** relativi a questi siti malevoli.

📌 Consigliamo vivamente di non seguire siti o canali non verificati per risolvere il problema, ma di fare riferimento esclusivamente alle istruzioni fornite dai canali ufficiali.

➡️ https://status.cloud.microsoft/
➡️ https://azure.status.microsoft/en-gb/status
➡️ https://www.crowdstrike.com/blog/statement-on-windows-sensor-update/

## Informazioni sulle nuove minacce

[20/07/2024] **CrowdStrike** ha rilevato e pubblicato in giornata [un elenco di domini](https://www.crowdstrike.com/blog/falcon-sensor-issue-use-to-target-crowdstrike-customers/) creati ad-hoc che impersonano il proprio marchio e che potrebbero essere utilizzati per future operazioni di social engineering.

[20/07/2024] È emerso che l’incidente CrowdStrike è stato sfruttato per distribuire il malware [RemcosRAT](https://app.any.run/tasks/5f515fa2-bd4a-49fd-88e2-d35b0c8376d9/).

![](https://cert-agid.gov.it/wp-content/uploads/2024/07/image-2.png)

[21/07/2024] Continuano le campagne che sfruttano l’evento per distribuire [malware](https://www.virustotal.com/gui/file/4491901eff338ab52c85a77a3fbd3ce80fda738046ee3b7da7be468da5b331a3/detection).

![](https://cert-agid.gov.it/wp-content/uploads/2024/07/image-3.png)

Il CERT-AGID sta aggiornando costantemente il [Flusso di IoC](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/) da inviare alle pubbliche amministrazioni accreditate.

Taggato
[BSoD](https://cert-agid.gov.it/tag/bsod/)
[CrowdStrike](https://cert-agid.gov.it/tag/crowdstrike/)
[Microsoft](https://cert-agid.gov.it/tag/microsoft/)

## Navigazione articoli

[Notizia precedente Campagne di phishing ai danni del Ministero degli Affari Esteri e della Cooperazione Internazionale](https://cert-agid.gov.it/news/campagne-di-phishing-ai-danni-del-ministero-degli-affari-esteri-e-della-cooperazione-internazionale/)

[Prossima notizia: Sintesi riepilogativa delle campagne malevole nella settimana del 13 – 19 luglio 2024](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-13-19-luglio-2024/)

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

![Logo del CE...