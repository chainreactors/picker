---
title: Phishing su Microsoft via device code flow. Automazione e AI ne amplificano la diffusione. Impatto sulla PA italiana
url: https://cert-agid.gov.it/news/phishing-su-microsoft-via-device-code-flow-automazione-e-ai-ne-amplificano-la-diffusione-impatto-sulla-pa-italiana/
source: Over Security - Cybersecurity news aggregator
date: 2026-04-08
fetch_date: 2026-04-09T04:32:04.911713
---

# Phishing su Microsoft via device code flow. Automazione e AI ne amplificano la diffusione. Impatto sulla PA italiana

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
* [Intelligenza Artificiale](https://cert-agid.gov.it/category/news/intelligenza-artificiale-news/)
* Phishing su Microsoft via device code flow. Automazione e AI ne amplificano la diffusione. Impatto sulla PA italiana

# Phishing su Microsoft via device code flow. Automazione e AI ne amplificano la diffusione. Impatto sulla PA italiana

08/04/2026

 [Intelligenza Artificiale](https://cert-agid.gov.it/tag/intelligenza-artificiale/)
[Microsoft](https://cert-agid.gov.it/tag/microsoft/)
[oauth](https://cert-agid.gov.it/tag/oauth/)
[phishing](https://cert-agid.gov.it/tag/phishing/)

Due giorni fa, Microsoft ha diramato un’allerta globale su una nuova e sofisticata campagna di phishing che **sfrutta l’intelligenza artificiale** per colpire gli account aziendali. Come CERT-AgID, abbiamo già raccolto prove che confermano come questa minaccia stia **prendendo di mira anche la Pubblica Amministrazione italiana.**

Il meccanismo dell’attacco è molto astuto e sfrutta una funzione legittima chiamata *device code flow* o *flusso tramite codice dispositivo*, un sistema normalmente utilizzato per collegare all’account dispositivi senza tastiera. I criminali stanno abusando di questo passaggio, inviando messaggi convincenti che chiedono di inserire un **codice su una portale di autenticazione di Microsoft** con la scusa di un aggiornamento urgente o di una verifica di sicurezza.

Il vero pericolo sta nel fatto che **la pagina dove viene richiesto di inserire il codice e le proprie credenziali è quella vera**, e di conseguenza non può essere bloccata da sistemi di protezione e può ingannare anche un utente esperto. Nel momento in cui il codice viene digitato, si sta letteralmente aprendo la porta al criminale, permettendogli di entrare nell’account **scavalcando anche l’autenticazione a due fattori.**

Ciò che distingue questa campagna non è tanto la tecnica, già osservata in passato, ma il modo in cui viene eseguita. Gli attaccanti utilizzano automazioni su larga scala e strumenti basati su **intelligenza artificiale** per generare campagne sempre diverse, adattare i messaggi e gestire l’intero attacco in modo automatico. Questo rende l’operazione più veloce, più difficile da rilevare e replicabile su larga scala.

L’Intelligenza Artificiale non introduce una nuova tecnica di attacco, ma trasforma un meccanismo già noto[1](#48651adb-658a-4b4d-8fb9-1b1bfbda87ff) in un’operazione industriale, capace di colpire molte organizzazioni contemporaneamente con contenuti sempre diversi e difficili da bloccare.

## Catena di compromissione

Il **flusso tramite codice dispositivo**[2](#a4dfb85c-6291-4595-ac19-87a312b9d30b) è una modalità legittima di autenticazione tramite **OAuth**, supportata da Microsoft Identity Platform e pensata per poter effettuare il login su dispositivi con interfacce limite, come una smart TV, un dispositivo IoT o una stampante, dove risulta impossibile o comunque scomodo effettuare l’accesso in maniera tradizionale digitando le proprie credenziali. In questa procedura, viene presentato un breve codice sul dispositivo su cui l’utente sta tentando di accedere e viene chiesto di inserire tale codice nel browser di un secondo dispositivo per completare l’autenticazione. Sebbene questa modalità di autenticazione sia utile in situazioni particolari, rappresenta un compromesso in termini di sicurezza.

![](https://cert-agid.gov.it/wp-content/uploads/2026/04/schema-phishing-device-code-flow-1024x544.png)

In questa tipologia di phishing, il *threat actor* si inserisce in questa procedura di login: invece di essere un dispositivo legittimo a richiedere l’accesso, è l’attore malevolo ad avviare il flusso di autenticazione e a fornire all’utente un codice tramite un’esca. Quando l’utente inserisce il codice nella pagina di login nel proprio browser, **autorizza inconsapevolmente la sessione dell’attaccante**, concedendo l’accesso al proprio account senza divulgarne le credenziali.

### Email come vettore iniziale

La campagna è veicolata tramite e-mail ingannevoli che hanno sfruttato diversi temi, tra cui la condivisione di documenti, l’apposizione di firme elettroniche e notifiche di segreteria telefonica. Queste e-mail contengono diversi tipi di payload, tra cui URL inseriti direttamente nel corpo o in allegati PDF o HTML. L’obiettivo è quello di **indurre l’utente a cliccare su un link** che lo reindirizza a un’interfaccia dall’aspetto legittimo.

Per eludere gli scanner automatici di URL e le sandbox, le email di phishing non rimandano direttamente alla pagina finale ma impiegano **una serie di reindirizzamenti** attraverso domini legittimi compromessi e piattaforme serverless come AWS, Cloudflare e Vercel. Utilizzando questi domini, il traffico di phishing si “mimetizza” con il traffico cloud aziendale legittimo, impedendo l’attivazione dei meccanismi di blocco più semplici. È stato inoltre osservato l’utilizzo di nomi di sottodomini pensati per spacciarsi per servizi tecnici o amministrativi, di maniera tale che, anche se un URL viene segnalato, il relativo dominio può sembrare legittimo e non venire bloccato immediatamente.

### Generazione dinamica del codice disp...