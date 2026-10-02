---
title: Credenziali GitHub esposte anche nei dataset per l’addestramento dell’IA
url: https://cert-agid.gov.it/news/credenziali-github-esposte-anche-nei-dataset-per-laddestramento-dellia/
source: Over Security
date: 2026-10-01
fetch_date: 2026-10-02T07:49:22.990259
---

# Credenziali GitHub esposte anche nei dataset per l’addestramento dell’IA

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
* [Data breach](https://cert-agid.gov.it/category/news/data-breach/)
* Credenziali GitHub esposte anche nei dataset per l’addestramento dell’IA

# Credenziali GitHub esposte anche nei dataset per l’addestramento dell’IA

01/10/2026

 [github](https://cert-agid.gov.it/tag/github/)
[hugging face](https://cert-agid.gov.it/tag/hugging-face/)
[Intelligenza Artificiale](https://cert-agid.gov.it/tag/intelligenza-artificiale/)

Una ricerca di [Truffle Security](https://trufflesecurity.com/blog/github-repos-exposed-543699-credentials-nobody-revoked-them) ha individuato **543.699 credenziali ancora valide** all’interno di codice proveniente da repository pubblici GitHub.

Tra i dati esposti figurano API key, token di accesso, credenziali per database e account di servizio. L’analisi è stata condotta su **[The Stack v3](https://huggingface.co/datasets/HuggingFaceCode/stack-v3-train)**, un dataset pubblico di 15,9 TB, utilizzato per l’addestramento di modelli di intelligenza artificiale dedicati al codice e costruito a partire da circa **224 milioni di repository GitHub**.

![](https://cert-agid.gov.it/wp-content/uploads/2026/10/image-1-1024x641.png)

Il dato più rilevante che emerge dall’analisi è che l’età media delle credenziali ancora funzionanti era di **784 giorni**, mentre alcune risultavano pubblicate da diversi anni senza essere mai revocate.

Truffle Security fa emergere un aspetto interessante e spesso sottovalutato: **una volta pubblicata, una credenziale può essere già presente in altri file, fork o copie del repository**. Per questo eventuali credenziali esposte devono essere considerate compromesse e revocate o ruotate, prima ancora di procedere alla pulizia del repository e della relativa cronologia.

## Come verificare l’esposizione dei propri repository

Il CERT-AGID consiglia di verificare se i propri repository GitHub sono presenti nei dataset **The Stack**, a tal proposito è possibile utilizzare il servizio **[Am I in The Stack?](https://huggingface.co/spaces/HuggingFaceCode/in-the-stack)** che Hugging Face mette a disposizione e che consente di effettuare la verifica inserendo il nome utente o dell’organizzazione usato su GitHub.

![](https://cert-agid.gov.it/wp-content/uploads/2026/10/image-1024x496.png)

Inoltre, per individuare eventuali credenziali esposte nei repository della propria organizzazione su GitHub, è possibile utilizzare strumenti come [**TruffleHog**](https://github.com/trufflesecurity/trufflehog). Di seguito sono riportati alcuni comandi di esempio.

Scansione per l’intera organizzazione:

```
trufflehog github --org=NOME_ORGANIZZAZIONE
```

Scansione per un singolo repository:

```
trufflehog git https://github.com/USERNAME/REPOSITORY
```

L’opzione `--results=verified` limita, se aggiunta, i risultati alle credenziali che TruffleHog è riuscito a verificare come ancora utilizzabili.

## Link utili

* [Dataset Stack v3](https://huggingface.co/datasets/HuggingFaceCode/stack-v3-train)
* [Am I in The Stack?](https://huggingface.co/spaces/HuggingFaceCode/in-the-stack)
* [TruffleHog](https://github.com/trufflesecurity/trufflehog)

Taggato
[github](https://cert-agid.gov.it/tag/github/)
[hugging face](https://cert-agid.gov.it/tag/hugging-face/)
[Intelligenza Artificiale](https://cert-agid.gov.it/tag/intelligenza-artificiale/)

## Navigazione articoli

[Notizia precedente Sintesi riepilogativa delle campagne malevole nella settimana del 19 – 25 settembre](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-19-25-settembre/)

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