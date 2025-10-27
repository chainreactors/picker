---
title: In atto una campagna di phishing bancario a tema SPID
url: https://cert-agid.gov.it/news/in-atto-una-campagna-di-phishing-bancario-a-tema-spid/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-19
fetch_date: 2025-10-06T18:27:30.555081
---

# In atto una campagna di phishing bancario a tema SPID

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
* In atto una campagna di phishing bancario a tema SPID

# In atto una campagna di phishing bancario a tema SPID

18/09/2024

 [banking](https://cert-agid.gov.it/tag/banking/)
[phishing](https://cert-agid.gov.it/tag/phishing/)
[SPID](https://cert-agid.gov.it/tag/spid/)

È stata segnalata al CERT-AGID una campagna di phishing particolarmente sofisticata che sfrutta il servizio **SPID** per carpire le credenziali di accesso degli utenti di diversi istituti bancari italiani.

La pagina web fraudolenta, approfittando dell’ampia diffusione del *Sistema Pubblico di Identità Digitale* e presentando una grafica molto simile a quella utilizzata da AGID, invita l’utente ad aggiornare le proprie credenziali per rinnovare la propria identità digitale e poter continuare ad accedere ai servizi online che richiedono l’autenticazione tramite SPID.

![](https://cert-agid.gov.it/wp-content/uploads/2024/09/phishing_bancario_SPID_1.png)

Cliccando sul link, l’utente viene indirizzato a un sito che richiede di selezionare il proprio istituto bancario per poi procedere con la verifica dell’identità.

![](https://cert-agid.gov.it/wp-content/uploads/2024/09/phishing_bancario_SPID_2.png)

Una volta scelta la banca si viene reindirizzati alla pagina di phishing vera e propria che replica accuratamente il form di login dell’istituto selezionato.

Tramite ulteriori analisi, è stato rilevato che il template utilizzato per la campagna è predisposto *anche* per il rilascio di un eventuale APK qualora la pagina sia visualizzata da dispositivo mobile Android.

Si raccomanda pertanto di non fare click su link presenti in email o messaggi sospetti, a verificare attentamente l’autenticità dei siti web visitati e, soprattutto, a non inserire credenziali all’interno di pagine ospitate su domini non ufficiali come quello della campagna odierna.

## **Indicatori di Compromissione**

Al fine di rendere pubblici i dettagli per il contrasto di questa campagna, vengono di seguito riportati gli indicatori rilevati, già diramati attraverso il [Feed IoC](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/) del CERT-AGID a tutti le pubbliche amministrazioni accreditate.

**Link:** [Download IoC](https://cert-agid.gov.it/wp-content/uploads/2024/09/SPID_2024-09-18.json)

Taggato
[banking](https://cert-agid.gov.it/tag/banking/)
[phishing](https://cert-agid.gov.it/tag/phishing/)
[SPID](https://cert-agid.gov.it/tag/spid/)

## Navigazione articoli

[Notizia precedente Vidar compare ancora in una nuova campagna malspam che sfrutta le caselle PEC](https://cert-agid.gov.it/news/vidar-compare-ancora-in-una-nuova-campagna-malspam-che-sfrutta-le-caselle-pec/)

[Prossima notizia: Lumma Stealer diffuso tramite notifica di falsa vulnerabilità di sicurezza sul proprio progetto GitHub](https://cert-agid.gov.it/news/lumma-stealer-diffuso-tramite-notifica-di-falsa-vulnerabilita-di-sicurezza-sul-proprio-progetto-github/)

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