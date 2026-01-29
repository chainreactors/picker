---
title: Sfruttate utenze della PA compromesse per tentare il furto di credenziali Microsoft 365 tramite Figma
url: https://cert-agid.gov.it/news/sfruttate-utenze-della-pa-compromesse-per-tentare-il-furto-di-credenziali-microsoft-365-tramite-figma/
source: Instapaper: Unread
date: 2026-01-28
fetch_date: 2026-01-29T04:05:58.656612
---

# Sfruttate utenze della PA compromesse per tentare il furto di credenziali Microsoft 365 tramite Figma

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
* Sfruttate utenze della PA compromesse per tentare il furto di credenziali Microsoft 365 tramite Figma

# Sfruttate utenze della PA compromesse per tentare il furto di credenziali Microsoft 365 tramite Figma

27/01/2026

 [figma](https://cert-agid.gov.it/tag/figma/)

Il CERT-AGID ha individuato una nuova campagna di phishing che **sfrutta caselle email compromesse appartenenti a Pubbliche Amministrazioni** per veicolare messaggi verso destinatari, sempre nel perimetro della PA, con i quali l’indirizzo mittente aveva intrattenuto comunicazioni legittime prima di essere abusato.

L’attacco presenta elementi di continuità con [una campagna già osservata](https://cert-agid.gov.it/news/campagna-malevola-in-atto-abusa-di-utenze-pa-tramite-allegati-pdf-e-accesso-a-figma/), in cui allegati PDF inviati da account istituzionali verso altre caselle della PA inducevano l’utente a consultare una **risorsa malevola ospitata sulla piattaforma legittima Figma**, con l’obiettivo di aumentare la credibilità del contenuto e favorire l’interazione.

![](https://cert-agid.gov.it/wp-content/uploads/2026/01/email.png)

## Dettagli della campagna

I messaggi risultano inviati dalla casella mittente verso sé stessa, mentre i reali destinatari (le vittime) non sono visibili perché inseriti in copia conoscenza nascosta (CCN). La comunicazione invita l’utente a cliccare sul link presente nel corpo dell’email e contiene diversi allegati PDF che simulano documenti amministrativi relativi a fatture o presentazioni.

![](https://cert-agid.gov.it/wp-content/uploads/2026/01/documenti.png)

Anche all’interno dei file PDF è presente il medesimo link, che rimanda a una risorsa malevola personalizzata con il nome e il logo dell’Amministrazione la cui casella email è stata abusata, caricata su Figma. Figma è una piattaforma cloud per la condivisione collaborativa di contenuti digitali, accessibile via browser tramite link e utilizzata comunemente in contesti professionali. Al solito, l’utilizzo di una piattaforma legittima consente agli attaccanti di presentare contenuti apparentemente affidabili e di ridurre la probabilità che l’utente riconosca immediatamente la natura fraudolenta del messaggio.

![](https://cert-agid.gov.it/wp-content/uploads/2026/01/figma_1.png)

Da tale risorsa, tramite un nuovo collegamento, l’utente viene reindirizzato verso una pagina di login contraffatta, **finalizzata alla sottrazione di credenziali Microsoft 365**.​

![](https://cert-agid.gov.it/wp-content/uploads/2026/01/pagina_phishing.png)

*Screenshot della pagina malevola finalizzata al furto di credenziali*

## Perché questa variante è rilevante

Rispetto alla campagna precedentemente osservata, la variante attuale sposta il focus dalla sola interazione su una piattaforma legittima alla costruzione di un contesto visivo coerente con l’identità dell’ente (*brand spoofing*), aumentando la probabilità che l’utente completi il tentativo di autenticazione.​
L’adozione di una falsa pagina Microsoft mira inoltre a colpire direttamente un *asset* molto critico nel contesto PA: le credenziali di accesso ai servizi cloud e alla posta istituzionale, che possono essere riutilizzate per ulteriori compromissioni o ulteriori invii fraudolenti “a catena”.​

## Azioni di contrasto

Per mitigare il rischio e supportare le attività di contenimento, il CERT-AGID ha provveduto a:

* informare le amministrazioni coinvolte delle compromissioni rilevate;
* distribuire gli Indicatori di Compromissione alle PA [accreditate al flusso IoC](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/).

## Indicatori di compromissione

Al fine di rendere pubblici i dettagli di questa campagna si riportano di seguito gli indicatori rilevati.

**Link:** [Download IoC](https://cert-agid.gov.it/wp-content/uploads/2026/01/phishing_Microsoft_27-01-2026.json)

Taggato
[figma](https://cert-agid.gov.it/tag/figma/)

## Navigazione articoli

[Notizia precedente Sintesi riepilogativa delle campagne malevole nella settimana del 17 – 23 gennaio](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-17-23-gennaio/)

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