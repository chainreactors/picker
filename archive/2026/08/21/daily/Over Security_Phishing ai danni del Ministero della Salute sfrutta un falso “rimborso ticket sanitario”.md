---
title: Phishing ai danni del Ministero della Salute sfrutta un falso “rimborso ticket sanitario”
url: https://cert-agid.gov.it/news/phishing-ai-danni-del-ministero-della-salute-sfrutta-un-falso-rimborso-ticket-sanitario/
source: Over Security
date: 2026-08-21
fetch_date: 2026-08-22T02:52:22.812115
---

# Phishing ai danni del Ministero della Salute sfrutta un falso “rimborso ticket sanitario”

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
* Phishing ai danni del Ministero della Salute sfrutta un falso “rimborso ticket sanitario”

# Phishing ai danni del Ministero della Salute sfrutta un falso “rimborso ticket sanitario”

21/08/2026

 [Ministero salute](https://cert-agid.gov.it/tag/ministero-salute/)
[phishing](https://cert-agid.gov.it/tag/phishing/)

Il CERT-AGID ha avuto evidenza di una campagna di phishing veicolata tramite email che utilizza il nome e le grafiche del **Ministero della Salute** allo scopo di acquisire informazioni personali e dati delle carte di pagamento delle vittime.

La comunicazione fraudolenta, con oggetto *“Hai diritto a un rimborso”*, comunica al destinatario la possibilità di ricevere un accredito di **278,26 euro** per un presunto doppio pagamento di un ticket sanitario. Il mittente `fondisanitari@gov.it` viene falsificato attraverso tecniche di *spoofing* per indurre il destinatario a considerare l’email come proveniente dalla Pubblica Amministrazione e a seguire il collegamento contenuto nel messaggio.

![](https://cert-agid.gov.it/wp-content/uploads/2026/08/Screenshot-from-2026-08-21-11-17-21.png)

*Email di phishing*

## Dettagli della campagna

L’email fa riferimento a presunte verifiche sui pagamenti sanitari che avrebbero condotto alla rilevazione di un possibile accredito spettante e invita l’utente, al fine di ottenere il rimborso, a cliccare su un pulsante *“Conferma i tuoi dati”* che lo conduce al sito malevolo.

Le pagine fraudolente propongono una procedura articolata in quattro fasi:

* **Accesso al servizio**: viene richiesto alla vittima di inserire codice fiscale e data di nascita per proseguire.
* **Visualizzazione del rimborso**: il sito mostra una pratica fittizia con causale *“Doppio pagamento ticket sanitario”*, un codice di riferimento e l’importo di 278,26 euro indicato come pronto per l’accredito.
* **Inserimento dei dati personali**: la successiva schermata richiede nome e cognome, indirizzo email, numero di cellulare e indirizzo di residenza completo, comprensivo di comune, provincia e CAP.
* **Acquisizione dei dati della carta**: per ricevere il presunto rimborso vengono infine richiesti intestatario, numero della carta, data di scadenza e CVV. Il sito indica inoltre che la carta deve supportare il sistema 3-D Secure e che le carte prepagate non sarebbero accettate.

![](https://cert-agid.gov.it/wp-content/uploads/2026/08/Screenshot-from-2026-08-20-17-50-03-1-1024x565.png)
![](https://cert-agid.gov.it/wp-content/uploads/2026/08/Screenshot-from-2026-08-21-10-24-05-1-1024x575.png)
![](https://cert-agid.gov.it/wp-content/uploads/2026/08/Screenshot-from-2026-08-21-10-43-16-1-1024x575.png)
![](https://cert-agid.gov.it/wp-content/uploads/2026/08/Screenshot-from-2026-08-21-11-29-35-1-1024x567.png)

Le informazioni raccolte consentono ai criminali di disporre sia di un insieme completo di dati identificativi e di contatto, sia dei dettagli necessari per tentare operazioni non autorizzate con la carta di pagamento. I dati possono inoltre essere utilizzati per realizzare ulteriori campagne mirate di smishing, vishing o phishing bancario.

## Azioni di contrasto

Il CERT-AGID ha richiesto la dismissione del dominio che ospita le pagine fraudolente e ha informato il Ministero della Salute. Gli Indicatori di Compromissione (IoC) sono stati condivisi con le Pubbliche Amministrazioni e con le [organizzazioni accreditate al flusso IoC](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/).

## Indicatori di Compromissione

Al fine di rendere pubblici i dettagli della campagna odierna si riportano di seguito gli IoC rilevati:

**Link:** [Download IoC](https://cert-agid.gov.it/wp-content/uploads/2026/08/phishing_MinisteroSalute_21-08-2026.json)

Taggato
[Ministero salute](https://cert-agid.gov.it/tag/ministero-salute/)
[phishing](https://cert-agid.gov.it/tag/phishing/)

## Navigazione articoli

[Notizia precedente Falso “rimborso farmaci” sfruttato per un phishing a tema Fascicolo Sanitario Elettronico](https://cert-agid.gov.it/news/falso-rimborso-farmaci-sfruttato-per-un-phishing-a-tema-fascicolo-sanitario-elettronico/)

[Prossima notizia: Sintesi riepilogativa delle campagne malevole nella settimana del 15 – 21 agosto](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-15-21-agosto/)

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