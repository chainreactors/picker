---
title: Truffa Safeguard: furto di account Telegram e connessione con lo smishing INPS
url: https://cert-agid.gov.it/news/truffa-safeguard-furto-di-account-telegram-e-connessione-con-lo-smishing-inps/
source: Over Security - Cybersecurity news aggregator
date: 2025-03-03
fetch_date: 2025-10-06T21:56:54.942531
---

# Truffa Safeguard: furto di account Telegram e connessione con lo smishing INPS

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
* Truffa Safeguard: furto di account Telegram e connessione con lo smishing INPS

# Truffa Safeguard: furto di account Telegram e connessione con lo smishing INPS

02/03/2025

 [inps](https://cert-agid.gov.it/tag/inps/)
[safeguard](https://cert-agid.gov.it/tag/safeguard/)
[telegram](https://cert-agid.gov.it/tag/telegram/)

Safeguard è un noto servizio, concepito per garantire la sicurezza delle transazioni nel mercato delle criptovalute, accessibile tramite la piattaforma di messaggistica Telegram. Tuttavia, la sua recente popolarità ha attirato l’attenzione dei criminali informatici, che stanno creando bot fraudolenti su Telegram per ingannare le vittime portando all’installazione di malware o al furto dell’accesso ai loro account.

Una [recente analisi](https://slowmist.medium.com/new-scam-technique-fake-safeguard-scam-on-telegram-bb4803bad521) ha rivelato l’esistenza di un falso bot di Safeguard che, una volta avviato, richiede all’utente di seguire tre passaggi come ulteriore verifica. L’obiettivo di questa truffa è eseguire codice PowerShell, sfruttando una tecnica già osservata per diffondere il malware [Lumma Stealer.](https://cert-agid.gov.it/news/analisi-di-una-campagna-lumma-stealer-con-falso-captcha-condotta-attraverso-domino-italiano-compromesso/)

![](https://cert-agid.gov.it/wp-content/uploads/2025/03/image.png)

In questi giorni il CERT-AGID ha avuto evidenza di un dominio, di recente registrazione, denominato `safeguard-telegram`. Questa pagina è collegata a due bot Telegram attualmente attivi, il cui obiettivo è indurre le vittime a scansionare un **QR code** per abilitare l’accesso da un nuovo dispositivo. In questo modo, la vittima concede ai criminali l’accesso al proprio account.

![](https://cert-agid.gov.it/wp-content/uploads/2025/03/tg1.png)
![](https://cert-agid.gov.it/wp-content/uploads/2025/03/image-3.png)

## Il collegamento con lo smishing INPS

Il dominio in questione espone pubblicamente alcune pagine contenenti informazioni sulla configurazione, tra cui il vero indirizzo IP del server che ospita il servizio di truffa.

![](https://cert-agid.gov.it/wp-content/uploads/2025/03/ssh_ip-1024x230.png)

L’indirizzo IP riportato nel file XML, accessibile tramite browser, risulta, [secondo Virustotal](https://www.virustotal.com/gui/ip-address/93.115.172.191/relations), collegato a due domini: `inps[.]ec` e `inps[.]io` quest’ultimo già rilevato ed analizzato nel [recente comunicato](https://cert-agid.gov.it/news/smishing-inps-nuova-truffa-minaccia-conseguenze-penali/).

![](https://cert-agid.gov.it/wp-content/uploads/2025/03/image-1.png)

La conferma del collegamento arriva visitando direttamente l’indirizzo IP, dove la pagina presenta contenuti e il logo di INPS usati per la truffa.

![](https://cert-agid.gov.it/wp-content/uploads/2025/03/image-2-1024x409.png)

Un ulteriore dettaglio interessante riguarda i link presenti nel menu superiore, che rimandano tutti a un altro dominio `inps[.]st`, anche questo risulta essere stato registrato di recente.

## Conclusioni

La truffa Safeguard e il collegamento alla truffa INPS mettono in luce come questo gruppo di criminali informatici stia sfruttando contemporaneamente due tipologie distinte di frodi per ottenere accesso alle informazioni delle vittime. Nel primo caso, attraverso bot fraudolenti, cercano di ottenere l’accesso agli account Telegram, mentre nel secondo caso mirano al furto di documenti d’identità tramite campagne di smishing.

## Indicatori di Compromissione

Gli IoC relativi a questa campagna sono stati già condivisi con le organizzazioni [accreditate al flusso IoC](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/) del CERT-AGID.

**Link:** [Download IoC](https://cert-agid.gov.it/wp-content/uploads/2025/03/safeguard-inps.json)

Taggato
[inps](https://cert-agid.gov.it/tag/inps/)
[safeguard](https://cert-agid.gov.it/tag/safeguard/)
[telegram](https://cert-agid.gov.it/tag/telegram/)

## Navigazione articoli

[Notizia precedente Sintesi riepilogativa delle campagne malevole nella settimana del 22 – 28 febbraio](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-22-28-febbraio/)

[Prossima notizia: Lumma Stealer e ClickFix: accoppiata malevola di nuovo in azione abusando di un dominio .it](https://cert-agid.gov.it/news/lumma-stealer-e-clickfix-accoppiata-malevola-di-nuovo-in-azione-abusando-di-un-dominio-it/)

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