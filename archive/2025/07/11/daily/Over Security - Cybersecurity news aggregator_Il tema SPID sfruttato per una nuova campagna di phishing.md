---
title: Il tema SPID sfruttato per una nuova campagna di phishing
url: https://cert-agid.gov.it/news/il-tema-spid-sfruttato-per-una-nuova-campagna-di-phishing/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-11
fetch_date: 2025-10-06T23:50:03.054828
---

# Il tema SPID sfruttato per una nuova campagna di phishing

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
* Il tema SPID sfruttato per una nuova campagna di phishing

# Il tema SPID sfruttato per una nuova campagna di phishing

10/07/2025

 [AgID](https://cert-agid.gov.it/tag/agid/)
[phishing](https://cert-agid.gov.it/tag/phishing/)
[SPID](https://cert-agid.gov.it/tag/spid/)

A brevissima distanza dall’[ultima campagna di phishing a tema **SPID**](https://cert-agid.gov.it/news/in-corso-una-nuova-campagna-di-phishing-a-tema-spid/) rilevata, è stata individuata dal CERT-AGID una nuova minaccia rivolta agli utenti del servizio.

![](https://cert-agid.gov.it/wp-content/uploads/2025/07/phishing_spid_page_2025-07-10-scaled.png)

La campagna di phishing è diffusa tramite email fraudolente con oggetto *“Suo certificato digitale è stato appena rinnovato.”* che invitano a scaricare un presunto nuovo certificato digitale, necessario per accedere ai servizi SPID. Il link presente nel corpo dell’email rimanda a una finta pagina di login SPID, dove viene chiesto di inserire le proprie credenziali di accesso.

![](https://cert-agid.gov.it/wp-content/uploads/2025/07/phishing_spid_email_2025-07-10.png)

Le comunicazioni, indirizzate a caselle di posta di aziende, del tipo `info@example.it`, sono apparentemente provenienti dall’indirizzo `noreply@spid.gov.it`. Tuttavia, da un’analisi approfondita è emerso queste email sono inviate da server di terze parti e non presentano alcuna firma DKIM, e di conseguenza dovrebbero essere rifiutate dai server di posta riceventi. Oltre alla mancanza di verifica della firma, le email in questione possono essere recapitate solo se il server destinatario non esegue correttamente l’autenticazione SPF.

## Azioni di contrasto

AgID ha richiesto, al fine di prevenire ulteriori furti di dati, la disattivazione del dominio ospitante la pagine di phishing e la disattivazione del servizio di hosting. Gli Indicatori di Compromissione (IoC) relativi a questa campagna sono stati diramati attraverso il [feed](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/) del CERT-AGID verso le strutture accreditate.

L’Agenzia raccomanda di prestare sempre la massima attenzione a questo tipo di comunicazioni, in particolare quando contengono collegamenti ritenuti sospetti. Nel dubbio, è sempre possibile inoltrare le email ritenute sospette alla casella di posta **malware@cert-agid.gov.it**

Si raccomanda inoltre a tutti coloro i quali utilizzano una propria infrastruttura di posta elettronica di implementare i sistemi di verifica e autenticazione delle comunicazioni in arrivo [SPF](https://it.wikipedia.org/wiki/Sender_Policy_Framework), [DMARC](https://it.wikipedia.org/wiki/DMARC) e [DKIM](https://it.wikipedia.org/wiki/DomainKeys_Identified_Mail) al fine di prevenire lo [spoofing](https://cert-agid.gov.it/glossario/spoofing/).

## Indicatori di Compromissione

Al fine di rendere pubblici i dettagli della campagna odierna si riportano di seguito gli IoC rilevati:

**Link:** [Download IoC](https://cert-agid.gov.it/wp-content/uploads/2025/07/phishing_spid_ioc_2025-07-10.json)

Taggato
[AgID](https://cert-agid.gov.it/tag/agid/)
[phishing](https://cert-agid.gov.it/tag/phishing/)
[SPID](https://cert-agid.gov.it/tag/spid/)

## Navigazione articoli

[Notizia precedente Vulnerabilità critica in Citrix riscontrata su host italiani](https://cert-agid.gov.it/news/vulnerabilita-critica-in-citrix-riscontrata-su-host-italiani/)

[Prossima notizia: Sintesi riepilogativa delle campagne malevole nella settimana del 5 – 11 luglio](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-5-11-luglio/)

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