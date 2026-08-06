---
title: Phishing ai danni di ARERA utilizza il tema “bonus sociale idrico”
url: https://cert-agid.gov.it/news/phishing-ai-danni-di-arera-utilizza-il-tema-bonus-sociale-idrico/
source: Over Security
date: 2026-08-05
fetch_date: 2026-08-06T05:02:42.497969
---

# Phishing ai danni di ARERA utilizza il tema “bonus sociale idrico”

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
* Phishing ai danni di ARERA utilizza il tema “bonus sociale idrico”

# Phishing ai danni di ARERA utilizza il tema “bonus sociale idrico”

05/08/2026

 [ARERA](https://cert-agid.gov.it/tag/arera/)
[bonus idrico](https://cert-agid.gov.it/tag/bonus-idrico/)
[phishing](https://cert-agid.gov.it/tag/phishing/)

Il CERT-AGID ha individuato e contrastato un sito fraudolento che riproduce nome e logo di **ARERA** (Autorità di Regolazione per Energia Reti e Ambiente) allo scopo di carpire dati personali e finanziari agli utenti. Il pretesto è un rimborso legato al **bonus sociale idrico**, una misura realmente esistente volta a ridurre la spesa sostenuta per la fornitura idrica dei nuclei familiari in condizioni di disagio economico o fisico. Il sito illegittimo utilizza tecniche di *typosquatting* per aumentare la credibilità.

![](https://cert-agid.gov.it/wp-content/uploads/2026/08/Screenshot-From-2026-07-31-10-28-1.png)

*Homepage del sito malevolo*

## Dettagli sulla campagna malevola

La prima pagina imita la sezione ARERA dedicata al bonus idrico, invitando l’utente a digitare il proprio numero di telefono per controllare se ha diritto all’agevolazione. Una volta fornito il contatto, compare una pagina che mostra un finto importo di **€ 100,93** disponibile per l’erogazione insieme ai dettagli della pratica.

![](https://cert-agid.gov.it/wp-content/uploads/2026/08/Screenshot-From-2026-07-31-10-28-2.png)

*Pagina con l’“importo disponibile” e il riepilogo della pratica*

Successivamente la vittima viene indirizzata a una pagina che richiede la “verifica della carta di credito” al fine di poter ricevere l’importo. Intestatario, numero della carta, data di scadenza e codice CVV sono le informazioni richieste.

![](https://cert-agid.gov.it/wp-content/uploads/2026/08/Screenshot-From-2026-07-31-10-28-3.png)

*Pagina che richiede l’inserimento dei dati della carta di credito*

## Azioni di contrasto

Il CERT-AGID ha già ottenuto la dismissione del dominio malevolo e ha provveduto a informare l’Ente interessato. Gli **Indicatori di Compromissione** (IoC) relativi alla campagna sono stati diramati attraverso il [feed](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/) del CERT-AGID verso tutte le organizzazioni accreditate.

## Indicatori di Compromissione

Al fine di rendere pubblici i dettagli della campagna odierna si riportano di seguito gli IoC rilevati:

**Link:** [Download IoC](https://cert-agid.gov.it/wp-content/uploads/2026/08/phishing_ARERA_05-08-2026.json)

Taggato
[ARERA](https://cert-agid.gov.it/tag/arera/)
[bonus idrico](https://cert-agid.gov.it/tag/bonus-idrico/)
[phishing](https://cert-agid.gov.it/tag/phishing/)

## Navigazione articoli

[Notizia precedente Phishing a tema “multe” sfrutta il nome della Polizia di Stato e di pagoPA](https://cert-agid.gov.it/news/phishing-a-tema-multe-sfrutta-il-nome-della-polizia-di-stato-e-di-pagopa/)

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