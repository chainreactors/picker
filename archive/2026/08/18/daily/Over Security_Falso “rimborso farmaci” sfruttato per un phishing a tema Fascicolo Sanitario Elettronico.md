---
title: Falso “rimborso farmaci” sfruttato per un phishing a tema Fascicolo Sanitario Elettronico
url: https://cert-agid.gov.it/news/falso-rimborso-farmaci-sfruttato-per-un-phishing-a-tema-fascicolo-sanitario-elettronico/
source: Over Security
date: 2026-08-18
fetch_date: 2026-08-19T02:57:40.044559
---

# Falso “rimborso farmaci” sfruttato per un phishing a tema Fascicolo Sanitario Elettronico

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
* Falso “rimborso farmaci” sfruttato per un phishing a tema Fascicolo Sanitario Elettronico

# Falso “rimborso farmaci” sfruttato per un phishing a tema Fascicolo Sanitario Elettronico

18/08/2026

 [Fascicolo Sanitario](https://cert-agid.gov.it/tag/fascicolo-sanitario/)
[phishing](https://cert-agid.gov.it/tag/phishing/)

Il CERT-AGID ha individuato una nuova campagna di pshihing che sfrutta grafiche e loghi istituzionali del **Fascicolo Sanitario Elettronico (FSE)**, del Ministero della Salute, del Dipartimento per la trasformazione digitale e del Ministero dell’Economia e delle Finanze, con l’obiettivo di sottrarre dati personali e dettagli delle carte di pagamento delle vittime.

La leva psicologica sfruttata è la promessa di un presunto **rimborso del 19% per l’acquisto di medicinali in farmacia** (per un importo di €20,73).

![](https://cert-agid.gov.it/wp-content/uploads/2026/08/Screenshot-from-2026-08-18-10-43-42.png)

*Homepage del sito malevolo*

## **Dettagli della campagna**

Il sito fraudolento si articola in quattro passaggi sequenziali progettati per massimizzare la credibilità della truffa e aggirare eventuali sistemi di analisi automatica:

1. **Verifica di sicurezza (*Captcha*)**: all’utente viene inizialmente presentata una schermata di verifica con una semplice operazione aritmetica per “confermare che non è un robot”. Questo passaggio introduce una finta percezione di sicurezza e serve a ostacolare i crawler automatici di rilevamento.
2. **Notifica del finto rimborso**: superato il controllo, compare la schermata di riepilogo istituzionale che informa l’utente dell’elaborazione della richiesta di rimborso per farmaci (€20,73, corrispondente alla detrazione fiscale del 19%), invitandolo a cliccare su “Conferma” per finalizzare la documentazione.
3. **Raccolta dati anagrafici (“Completa il tuo dossier”)**: la pagina successiva richiede l’inserimento di dati personali: cognome, nome, data di nascita, CAP, indirizzo di residenza, città, telefono ed email.
4. **Sottrazione dei dati di pagamento**: nella fase conclusiva viene richiesto l’inserimento completo dei dati della carta di pagamento (titolare, numero di carta, data di scadenza e codice CVV), con il pretesto dell’accredito del rimborso “entro 1 settimana lavorativa”.
5. **Schermata conclusiva di conferma (“Richiesta di rimborso trasmessa”)**: a valle dell’invio dei dati, la vittima viene reindirizzata a una pagina finale di riepilogo con tanto di finto “Numero di protocollo” e stato “In elaborazione”. Nel testo viene fatto esplicito richiamo all’**Agenzia delle Entrate**, con la promessa di accredito entro 7 giorni lavorativi e l’indicazione di un falso numero verde di assistenza.

![](https://cert-agid.gov.it/wp-content/uploads/2026/08/Screenshot-from-2026-08-18-10-41-05.png)
![](https://cert-agid.gov.it/wp-content/uploads/2026/08/Screenshot-from-2026-08-18-10-44-18.png)
![](https://cert-agid.gov.it/wp-content/uploads/2026/08/Screenshot-from-2026-08-18-10-45-09.png)
![](https://cert-agid.gov.it/wp-content/uploads/2026/08/Screenshot-from-2026-08-18-11-46-46.png)

La combinazione di dati anagrafici completi e dettagli della carta di pagamento consente agli attaccanti di:

* effettuare transazioni fraudolente online sfruttando i dati della carta;
* monetizzare i dati rivendendoli all’interno di circuiti illeciti;
* utilizzare il profilo anagrafico per ulteriori attacchi mirati di social engineering (es. vishing o smishing bancario).

## **Azioni di contrasto**

Il CERT-AGID ha già avviato le consuete attività di contrasto per la dismissione del dominio malevolo e ha provveduto a diramare gli **Indicatori di Compromissione (IoC)** alle Pubbliche Amministrazioni e alle [organizzazioni accreditate al flusso IoC](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/).

## Indicatori di Compromissione

Al fine di rendere pubblici i dettagli della campagna odierna si riportano di seguito gli IoC rilevati:

**Link:** [Download IoC](https://cert-agid.gov.it/wp-content/uploads/2026/08/phishing_FascicoloSanitario_18-08-2026.json)

Taggato
[Fascicolo Sanitario](https://cert-agid.gov.it/tag/fascicolo-sanitario/)
[phishing](https://cert-agid.gov.it/tag/phishing/)

## Navigazione articoli

[Notizia precedente Sintesi riepilogativa delle campagne malevole nella settimana del 8 – 14 agosto](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-8-14-agosto/)

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