---
title: Distribuzione mirata in Italia di Adwind
url: https://cert-agid.gov.it/news/distribuzione-mirata-in-italia-di-adwind/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-17
fetch_date: 2025-10-06T22:28:52.754991
---

# Distribuzione mirata in Italia di Adwind

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
* Distribuzione mirata in Italia di Adwind

# Distribuzione mirata in Italia di Adwind

16/05/2025

 [adwind](https://cert-agid.gov.it/tag/adwind/)

Come già segnalato da [Fortinet](https://www.fortinet.com/blog/threat-research/multilayered-email-attack-how-a-pdf-invoice-and-geofencing-led-to-rat-malware), in questi giorni gli autori del RAT Adwind hanno avviato una campagna su larga scala, mirata a Spagna, Portogallo e Italia, per diffondere il malware tramite email contenenti allegati in formato PDF.

![](https://cert-agid.gov.it/wp-content/uploads/2025/05/image-2.png)

La campagna osservata dal CERT-AGID prevede l’utilizzo di un allegato **PDF**, solitamente denominato *Documento.pdf* o *Fattura.pdf*, contenente un collegamento a servizi di cloud storage come **OneDrive** o **Dropbox**, da cui viene scaricato un file VBS o HTML con codice offuscato, ma facilmente decodificabile.

## Controllo della lingua del browser

![](https://cert-agid.gov.it/wp-content/uploads/2025/05/image-9.png)
![](https://cert-agid.gov.it/wp-content/uploads/2025/05/image-10.png)

Il file HTML contiene uno script che verifica la lingua impostata nel browser. Sono state individuate due varianti del file: la prima controlla che la lingua non sia inglese, mentre la seconda esclude sia l’**inglese** che il **russo**. In entrambi i casi, se la lingua corrisponde a quelle escluse, il file VBS non viene scaricato e viene mostrato solo il PDF usato come decoy.

![](https://cert-agid.gov.it/wp-content/uploads/2025/05/image-5.png)

## Analisi del file VBS

![](https://cert-agid.gov.it/wp-content/uploads/2025/05/image-3.png)
![](https://cert-agid.gov.it/wp-content/uploads/2025/05/image-4-1024x871.png)

Il codice VBS, una volta deoffuscato, presenta una serie di commenti iniziali contenenti il testo della canzone *[Negro Drama](https://www.letras.com/racionais-mcs/63398/)*, seguito dal codice attivo che scarica un documento PDF da Google Drive utilizzando la stessa URL già segnalata da Fortinet. Durante l’apertura del finto documento PDF per distrarre la vittima, viene avviato in parallelo il download da *`ngrok.dev`* di un archivio ZIP di circa 90 MB.

## Il pacchetto completo

A differenza di quanto osservato da Fortinet, dove veniva scaricato un file JAR, quindi eseguibile solo in presenza di Java sul sistema, il pacchetto ZIP individuato in questa campagna contiene al suo interno sia l’ambiente Java necessario, sia il file JAR camuffato da immagine PNG (`InvoiceXpress.png`), che viene eseguito tramite uno script CMD (`InvoiceXpress.cmd`).

![](https://cert-agid.gov.it/wp-content/uploads/2025/05/image-6-1024x200.png)

Come già evidenziato, il file JAR è camuffato da immagine PNG. La presenza del file `checksum` all’interno del JAR, utilizzato per la configurazione, insieme alla struttura del codice, ne conferma l’attribuzione al malware [Adwind](https://cert-agid.gov.it/tag/adwind/).

![](https://cert-agid.gov.it/wp-content/uploads/2025/05/image-7.png)

La configurazione, cifrata tramite AES in modalità ECB, può essere decifrata facilmente utilizzando la seguente [ricetta CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)AES_Decrypt(%7B'option':'Hex','string':'a80ed2ef79e22f1d8af817cea1dbbf01'%7D,%7B'option':'Hex','string':''%7D,'ECB/NoPadding','Raw','Raw',%7B'option':'Hex','string':''%7D,%7B'option':'Hex','string':''%7D)&oeol=CRLF).

![](https://cert-agid.gov.it/wp-content/uploads/2025/05/image-8-1024x549.png)

L’analisi del dominio utilizzato come host (porta 4414) conferma, anche in questo caso, l’appartenenza del sottodominio al dominio *`localto.net`*, già rilevato nelle indagini di Fortinet e dalle analisi di [altri ricercatori](https://x.com/marsomx_/status/1920866457115660789) su X.

## Nota

Sebbene Adwind sia progettato per essere multipiattaforma, la variante analizzata, in linea con quelle [identificate negli anni precedenti,](https://cert-agid.gov.it/news/campagne-adwind-jrat-attive-contro-obiettivi-italiani/) è specificamente orientata all’infezione di sistemi Windows.

## **Indicatori di Compromissione**

Per facilitare le azioni di contrasto della campagna fraudolenta, di seguito vengono riportati gli IoC identificati durante l’analisi, che sono stati già condivisi con le PA accreditate al [Flusso IoC](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/) del CERT-AgID.

**Link:** [Download IoC](https://cert-agid.gov.it/wp-content/uploads/2025/05/adwind_16-05-2025.json)

Taggato
[adwind](https://cert-agid.gov.it/tag/adwind/)

## Navigazione articoli

[Notizia precedente Sintesi riepilogativa delle campagne malevole nella settimana del 3 – 9 maggio](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-3-9-maggio/)

[Prossima notizia: Sintesi riepilogativa delle campagne malevole nella settimana del 10 – 16 maggio](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-10-16-maggio/)

![Logo del CERT-PA](/wp-content/themes/cert-agid/assets/images/cert-agid-logo-white.svg)
CERT-A...