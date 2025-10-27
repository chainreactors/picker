---
title: AsyncRAT distribuito in Italia tramite componenti steganografici
url: https://cert-agid.gov.it/news/asyncrat-distribuito-in-italia-tramite-componenti-steganografici/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-28
fetch_date: 2025-10-06T22:30:05.741465
---

# AsyncRAT distribuito in Italia tramite componenti steganografici

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
* AsyncRAT distribuito in Italia tramite componenti steganografici

# AsyncRAT distribuito in Italia tramite componenti steganografici

27/05/2025

 [AsyncRAT](https://cert-agid.gov.it/tag/asyncrat/)

Il CERT-AGID ha avuto evidenza di una campagna malspam attiva oggi in Italia, scritta in lingua inglese, con l’obiettivo di compromettere i sistemi delle vittime attraverso l’uso del malware AsyncRAT.

![](https://cert-agid.gov.it/wp-content/uploads/2025/05/email-1.png)

L’email, apparentemente inviata dalla compagnia di costruzioni araba “Arabian Construction Co”, comunica alla vittima di essere stata identificata come potenziale fornitore e la invita a consultare informazioni dettagliate nel file allegato. Tuttavia, non c’è alcun allegato; al suo posto, è presente un link (nella sezione RFQ) che rimanda al download di un file TAR condiviso tramite la piattaforma Box.com.

![](https://cert-agid.gov.it/wp-content/uploads/2025/05/image-11.png)

L’archivio TAR contiene un file JavaScript, opportunamente offuscato, che rilascia ed esegue un comando PowerShell progettato per scaricare una risorsa da uno spazio di storage di posta elettronica di una casella Aruba.

![](https://cert-agid.gov.it/wp-content/uploads/2025/05/image-12-1024x336.png)

In realtà, il campione finale può essere scaricato direttamente dall’URL assegnata alla variabile `$gangbusters` che deve essere invertita, ma la catena di compromissione segue un percorso differente.

Il file ottenuto dalla url `$picle` è una GIF che presenta al suo interno un codice codificato in `Base64` e racchiuso tramite i tag `<<sudo_png>>` e `<<sudo_odt>>`.

![](https://cert-agid.gov.it/wp-content/uploads/2025/05/image-13.png)

La decodifica del codice restituisce una DLL che viene invocata dal codice PowerShell con alcuni parametri, tra cui l’URL invertita assegnata alla variabile `$gangbuster`. Dopo aver effettuato alcuni controlli sulla macchina in cui viene eseguita, inclusa la verifica della presenza di una Virtual Machine, la DLL provvede a scaricare il campione finale ed eseguirlo.

![](https://cert-agid.gov.it/wp-content/uploads/2025/05/image-14-1024x395.png)

Il malware finale è AsyncRAT, che abbiamo già osservato essere distribuito attraverso diversi loader in più occasioni. AsyncRAT è un malware di tipo RAT progettato per fornire accesso remoto non autorizzato ai sistemi infetti. Consente agli attaccanti di controllare e monitorare le macchine compromesse, rubare dati sensibili e eseguire comandi a distanza.

Ulteriori approfondimenti [rivelano](https://bazaar.abuse.ch/browse/tag/webmail-aruba-it--ajaxfile/) che la stessa GIF è stata utilizzata recentemente per infettare le vittime tramite anche altri malware, tra cui Remcos, Formbook, Avemaria e MassLogger.

## Azioni di contrasto

Grazie alla collaborazione con Aruba la risorsa è stata già dismessa. Gli IoC relativi alla campagna sono stati tempestivamente diramati attraverso il [Feed IoC](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/) del CERT-AGID verso le strutture accreditate.

Si raccomanda di prestare sempre la massima attenzione a questo tipo di comunicazioni, in particolare quando contengono collegamenti ritenuti sospetti. Nel dubbio, è sempre possibile inoltrare le email ritenute sospette alla casella di posta **malware@cert-agid.gov.it**

## Indicatori di Compromissione

Al fine di rendere pubblici i dettagli della campagna odierna si riportano di seguito gli IoC rilevati:

**Link:**

* [Download IoC](https://cert-agid.gov.it/wp-content/uploads/2025/05/asyncrat_27-05-2025.json) 27/05/2025
* [Download IoC](https://cert-agid.gov.it/wp-content/uploads/2025/05/asyncrat_28-05-2025.json) 28/05/2025 *(Aggiornamento via [Telegram](https://t.me/certagid/833))*

Taggato
[AsyncRAT](https://cert-agid.gov.it/tag/asyncrat/)

## Navigazione articoli

[Notizia precedente Sintesi riepilogativa delle campagne malevole nella settimana del 17 – 23 maggio](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-17-23-maggio/)

[Prossima notizia: Sintesi riepilogativa delle campagne malevole nella settimana del 24 – 30 maggio](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-24-30-maggio/)

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