---
title: Il dominio italiano di Excite riutilizzato in una campagna di malspam via PEC
url: https://cert-agid.gov.it/news/il-dominio-italiano-di-excite-riutilizzato-in-una-campagna-di-malspam-via-pec/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-17
fetch_date: 2025-10-06T18:27:54.879508
---

# Il dominio italiano di Excite riutilizzato in una campagna di malspam via PEC

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
* Il dominio italiano di Excite riutilizzato in una campagna di malspam via PEC

# Il dominio italiano di Excite riutilizzato in una campagna di malspam via PEC

16/09/2024

 [excite](https://cert-agid.gov.it/tag/excite/)
[PEC](https://cert-agid.gov.it/tag/pec/)
[vidar](https://cert-agid.gov.it/tag/vidar/)

![](https://cert-agid.gov.it/wp-content/uploads/2024/09/email_pec_excite.png)

Questo fine settimana è stata identificata e contrastata una campagna malevola che utilizzava alcuni **account PEC compromessi** per colpire altri utenti del servizio di Posta Elettronica Certificata.

Il messaggio, firmato da un presunto creditore, richiede il pagamento di un importo di 1305 euro, minacciando azioni legali in caso di mancato pagamento entro cinque giorni. La comunicazione include **un link per scaricare una fattura** che potrebbe essere un tentativo di phishing o di un malware, [come osservato](https://cert-agid.gov.it/news/vidar-insiste-in-italia-con-campagne-via-pec/) nelle campagne precedenti.

Questa volta il link punta a una url sul vecchio dominio [**Excite.it**,](https://it.wikipedia.org/wiki/Excite) noto portale italiano in voga negli anni ’90 *([qui](https://web.archive.org/web/20210621022554/http%3A//info.excite.it/) la pagina info su archive.org)*.

Fortunatamente, sia le URL identificate che il dominio principale non distribuiscono alcun payload, ma richiedono una basic authentication.

![](https://cert-agid.gov.it/wp-content/uploads/2024/09/excite_it_2024-09-16.png)

Grazie alla fattiva collaborazione con i Gestori PEC, la campagna è stata contrastata e gli Indicatori di Compromissione (IoC) sono stati condivisi con le Pubbliche Amministrazioni accreditate al flusso IoC, portando al blocco del dominio principale di **Excite**.

È fondamentale rimanere vigili di fronte a queste truffe e verificare sempre l’autenticità delle richieste di pagamento, anche quando provengono da una casella PEC. Nel dubbio, per queste problematiche è utilizzabile la casella **malware@cert-agid.gov.it** per richiedere gli eventuali controlli del caso.

Taggato
[excite](https://cert-agid.gov.it/tag/excite/)
[PEC](https://cert-agid.gov.it/tag/pec/)
[vidar](https://cert-agid.gov.it/tag/vidar/)

## Navigazione articoli

[Notizia precedente Sintesi riepilogativa delle campagne malevole nella settimana del 7 – 13 settembre](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-7-13-settembre/)

[Prossima notizia: Vidar compare ancora in una nuova campagna malspam che sfrutta le caselle PEC](https://cert-agid.gov.it/news/vidar-compare-ancora-in-una-nuova-campagna-malspam-che-sfrutta-le-caselle-pec/)

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