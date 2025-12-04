---
title: In atto una campagna di phishing che sfrutta le insegne del Governo per sottrarre dati bancari
url: https://cert-agid.gov.it/news/in-atto-una-campagna-di-phishing-che-sfrutta-le-insegne-del-governo-per-sottrarre-dati-bancari/
source: Over Security - Cybersecurity news aggregator
date: 2025-12-03
fetch_date: 2025-12-04T03:19:05.178966
---

# In atto una campagna di phishing che sfrutta le insegne del Governo per sottrarre dati bancari

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
* In atto una campagna di phishing che sfrutta le insegne del Governo per sottrarre dati bancari

# In atto una campagna di phishing che sfrutta le insegne del Governo per sottrarre dati bancari

03/12/2025

 [governo](https://cert-agid.gov.it/tag/governo/)
[PCM](https://cert-agid.gov.it/tag/pcm/)
[phishing](https://cert-agid.gov.it/tag/phishing/)

Il CERT-AGID ha rilevato una nuova campagna di phishing che sfrutta indebitamente il nome e le insegne del **Governo Italiano** e della **Presidenza del Consiglio dei Ministri** per sottrarre credenziali di accesso bancarie. La campagna viene veicolata tramite email con oggetto “*Verifica dei Dati Bancari – Governo Italiano*”. Il messaggio, che fa riferimento ad una presunta “operazione puramente amministrativa” finalizzata all’aggiornamento dei dati, invita subdolamente l’utente a cliccare su un link presente nel corpo del messaggio.

![](https://cert-agid.gov.it/wp-content/uploads/2025/12/Screenshot-from-2025-12-03-09-57-45.png)

Il collegamento reindirizza a una pagina web che riproduce fedelmente la grafica istituzionale della Presidenza del Consiglio dei Ministri. All’interno è presente un menu a tendina (“*Scegliete la vostra banca*”) che consente alla vittima di selezionare il proprio istituto di credito da una lista che comprende alcuni fra i principali gruppi, nazionali e non, come: **Intesa Sanpaolo**, **UniCredit**, **Monte dei Paschi di Siena**, **BNL**, **ING**, **BPER**, **BCC**, **Fineco**, **Crédit Agricole** e **PostePay**.

![](https://cert-agid.gov.it/wp-content/uploads/2025/12/Screenshot-from-2025-12-03-10-00-51.png)

Una volta effettuata la selezione, l’utente viene reindirizzato verso uno specifico portale contraffatto che simula la **pagina di login della banca scelta**, con l’obiettivo di carpirne le credenziali di accesso (codice cliente, PIN/password).

![](https://cert-agid.gov.it/wp-content/uploads/2025/12/phishing_multibanca.jpg)

**Azioni di contrasto** **e Indicatori di Compromissione**

Il CERT-AGID ha già provveduto a richiedere la rimozione del dominio malevolo al *registrar* e a diramare gli indicatori di compromissione (IoC) associati alla campagna a tutti gli Enti accreditati.

Al fine di rendere pubblici i dettagli di questa campagna, si riportano di seguito gli indicatori rilevati.

**Link:** [Download IoC](https://cert-agid.gov.it/wp-content/uploads/2025/12/phishing_PCM_03-12-2025.json)

Taggato
[governo](https://cert-agid.gov.it/tag/governo/)
[PCM](https://cert-agid.gov.it/tag/pcm/)
[phishing](https://cert-agid.gov.it/tag/phishing/)

## Navigazione articoli

[Notizia precedente IA agentica e sicurezza informatica: online l’analisi del CERT-AgID](https://cert-agid.gov.it/news/ia-agentica-e-sicurezza-informatica-online-lanalisi-del-cert-agid/)

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