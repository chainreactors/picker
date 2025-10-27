---
title: Lumma Stealer diffuso tramite notifica di falsa vulnerabilità di sicurezza sul proprio progetto GitHub
url: https://cert-agid.gov.it/news/lumma-stealer-diffuso-tramite-notifica-di-falsa-vulnerabilita-di-sicurezza-sul-proprio-progetto-github/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-19
fetch_date: 2025-10-06T18:26:49.680132
---

# Lumma Stealer diffuso tramite notifica di falsa vulnerabilità di sicurezza sul proprio progetto GitHub

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
* Lumma Stealer diffuso tramite notifica di falsa vulnerabilità di sicurezza sul proprio progetto GitHub

# Lumma Stealer diffuso tramite notifica di falsa vulnerabilità di sicurezza sul proprio progetto GitHub

18/09/2024

 [github](https://cert-agid.gov.it/tag/github/)
[lumma stealer](https://cert-agid.gov.it/tag/lumma-stealer/)

![](https://cert-agid.gov.it/wp-content/uploads/2024/09/github-scanner-notification.png)

In queste ore molti utenti di GitHub stanno ricevendo un’email allarmante con il titolo “**IMPORTANT! Security Vulnerability Detected in your Repository (Issue #1)**“. Il messaggio, apparentemente inviato dal “*GitHub Security Team*“, avvisa i destinatari di una presunta vulnerabilità di sicurezza nei loro repository e invita a contattare un link sospetto.

Tuttavia, è emerso che il dominio *github-scanner**[**.com* è stato registrato solo oggi ed è usato con lo scopo di distribuire malware.

![](https://cert-agid.gov.it/wp-content/uploads/2024/09/github-scanner-popup-1-1024x605.png)
![](https://cert-agid.gov.it/wp-content/uploads/2024/09/github-scanner-popup-2-1024x605.png)

Cliccando sul link viene mostrato un avviso ingannevole che invita gli utenti a compiere 3 operazioni: premere **`Windows+R`**, poi **`Ctrl+V`** ed in fine `Enter` per dimostrare di non essere un bot. Questa combinazione di tasti viene utilizzata per eseguire codice malevolo (powershell) riportato nel seguente codice ***Javascript***

![](https://cert-agid.gov.it/wp-content/uploads/2024/09/github-scanner-javascript-code.png)

Il compito dello script è quello di rilasciare il codice ***PowerShell*** descritto nella costante `captchaText` ed eseguito grazie ai comandi successivi: `Windows+R` (apre la finestra di dialogo “Esegui”), `Ctrl+V` (incolla il codice malevolo dentro il campo “Esegui”) e **`Enter`** (per eseguire il codice). In questo modo verrà avviato il download e l’esecuzione di un eseguibile `l6E.exe`. che verrà rinominato in locale con il nome `SysSetup.exe`

![](https://cert-agid.gov.it/wp-content/uploads/2024/09/github-scanner-powershell.png)

L’eseguibile in questione è il noto malware **Lumma Stealer**, progettato per rubare informazioni sensibili dagli utenti, inclusi dati di accesso e informazioni personali.

Se il malware non riesce a connettersi alla propria lista di domini C2, viene attivata una routine che provvede ad ottenere informazioni da profili Steam community. Questa pratica è [già stata osservata](https://t.me/certagid/583) lo scorso anno con il malware `Vidar`, ma in questo caso le url dei C2 sono riportati in forma cifrata.

![](https://cert-agid.gov.it/wp-content/uploads/2024/09/github-scanner-lumma-steam-c2.png)

## **Indicatori di Compromissione**

Al fine di rendere pubblici i dettagli per il contrasto di questa campagna, vengono di seguito riportati gli indicatori rilevati, già diramati attraverso il [Feed IoC](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/) del CERT-AGID a tutti le pubbliche amministrazioni accreditate.

**Link:** [Download IoC](https://cert-agid.gov.it/wp-content/uploads/2024/09/github-scanner_lumma_18-09-2024.json)

Taggato
[github](https://cert-agid.gov.it/tag/github/)
[lumma stealer](https://cert-agid.gov.it/tag/lumma-stealer/)

## Navigazione articoli

[Notizia precedente In atto una campagna di phishing bancario a tema SPID](https://cert-agid.gov.it/news/in-atto-una-campagna-di-phishing-bancario-a-tema-spid/)

[Prossima notizia: Sintesi riepilogativa delle campagne malevole nella settimana del 14 – 20 settembre](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-14-20-settembre/)

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