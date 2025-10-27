---
title: Ritorna Vidar in Italia con una campagna di malspam tramite PEC
url: https://cert-agid.gov.it/news/ritorna-vidar-in-italia-con-una-campagna-di-malspam-tramite-pec/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-07
fetch_date: 2025-10-06T18:05:20.547414
---

# Ritorna Vidar in Italia con una campagna di malspam tramite PEC

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
* Ritorna Vidar in Italia con una campagna di malspam tramite PEC

# Ritorna Vidar in Italia con una campagna di malspam tramite PEC

06/08/2024

 [PEC](https://cert-agid.gov.it/tag/pec/)
[vidar](https://cert-agid.gov.it/tag/vidar/)

![](https://cert-agid.gov.it/wp-content/uploads/2024/08/email-vidar-pec.png)

Una massiccia campagna di malspam, avviata nella notte tra il 5 e il 6 agosto, ha tentato di diffondere su larga scala il malware **[Vidar](https://cert-agid.gov.it/tag/vidar/)** attraverso messaggi indirizzati alle caselle di Posta Elettronica Certificata. Gli attacchi, che hanno interessato un numero considerevole di utenti PEC, sono stati portati a termine durante la nottata, sfruttando un template già noto per diffondere il malware attraverso account PEC precedentemente violati.

Questa volta il file ottenuto dal link nel corpo del messaggio è un file JavaScript progettato per scaricare ed eseguire uno script PowerShell:

![](https://cert-agid.gov.it/wp-content/uploads/2024/08/image-1024x575.png)

![](https://cert-agid.gov.it/wp-content/uploads/2024/08/image-1-1024x415.png)

Il deoffuscamento del codice PowerShell rivela l’URL utilizzato per scaricare il payload finale in PowerShell. In questo caso è possibile ottenere il risultato grazie a poche righe di codice Python:

![](https://cert-agid.gov.it/wp-content/uploads/2024/08/image-2-1024x427.png)

*URL ottenuto da codice Python*

**Vidar** è un Malware as a Service della famiglia degli infostealer che, una volta compromesso un sistema, raccoglie diverse informazioni quali:

* password, cookie, cronologia e auto completamento dei browser più diffusi;
* portafogli digitali;
* dati relativi alle carte di credito;
* dati di autenticazione Telegram;
* credenziali di accesso FTP, WINSCP, MAIL.

## Azioni di contrasto

Le attività di contrasto sono state già messe in atto con il supporto dei Gestori PEC che hanno provveduto a bloccare gli indirizzi coinvolti nell’invio delle mail malevole. Gli IoC relativi alla campagna sono stati diramati attraverso il [Feed IoC](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/) del CERT-AgID verso i Gestori PEC e verso le strutture accreditate.

Si invita a prestare sempre attenzione a questo genere di comunicazioni. Nel dubbio, è possibile inoltrare email ritenute sospette alla casella di posta **malware@cert-agid.gov.it**

## Indicatori di Compromissione

Al fine di rendere pubblici i dettagli della campagna odierna si riportano di seguito gli IoC rilevati:

**Link:** [Download IoC](https://cert-agid.gov.it/wp-content/uploads/2024/08/vidar_pec_06-08-2024.json)

Taggato
[PEC](https://cert-agid.gov.it/tag/pec/)
[vidar](https://cert-agid.gov.it/tag/vidar/)

## Navigazione articoli

[Notizia precedente Sintesi riepilogativa delle campagne malevole nella settimana del 27 luglio – 2 agosto](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-27-luglio-2-agosto/)

[Prossima notizia: Nuova campagna italiana StrRat: disponibile una ricetta CyberChef per decodificare il malware](https://cert-agid.gov.it/news/nuova-campagna-italiana-strrat-disponibile-una-ricetta-cyberchef-per-decodificare-il-malware/)

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