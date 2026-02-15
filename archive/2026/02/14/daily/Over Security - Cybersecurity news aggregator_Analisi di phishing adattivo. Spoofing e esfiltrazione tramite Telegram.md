---
title: Analisi di phishing adattivo. Spoofing e esfiltrazione tramite Telegram
url: https://cert-agid.gov.it/news/analisi-di-phishing-adattivo-spoofing-e-esfiltrazione-tramite-telegram/
source: Over Security - Cybersecurity news aggregator
date: 2026-02-14
fetch_date: 2026-02-15T04:26:22.401995
---

# Analisi di phishing adattivo. Spoofing e esfiltrazione tramite Telegram

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
* Analisi di phishing adattivo. Spoofing e esfiltrazione tramite Telegram

# Analisi di phishing adattivo. Spoofing e esfiltrazione tramite Telegram

14/02/2026

 [adattivo](https://cert-agid.gov.it/tag/adattivo/)
[telegram](https://cert-agid.gov.it/tag/telegram/)

Il messaggio analizzato è stato ricevuto su una casella di posta dedicata alla raccolta e al monitoraggio di email sospette e campagne di phishing/malspam. Si tratta di un indirizzo configurato appositamente per intercettare questo genere di contenuti al fine di analizzarne tecniche e modalità operative.

![](https://cert-agid.gov.it/wp-content/uploads/2026/02/image-1.png)

È opportuno evidenziare che messaggi con caratteristiche analoghe vengono normalmente recapitati a utenti finali quando il server di posta del dominio bersaglio non è configurato correttamente sotto il profilo dell’autenticazione e delle policy di sicurezza.

Nel caso in esame, il messaggio ha oggetto relativo a un presunto pagamento e contiene in allegato un file HTML. Il testo è essenziale, privo di riferimenti verificabili, costruito con lo scopo di indurre il destinatario ad aprire l’allegato.

Si tratta di un esempio che si inserisce nel fenomeno noto come **phishing adattivo**, [ampiamente descritto nei nostri comunicati](https://cert-agid.gov.it/tag/adattivo/).

L’analisi tecnica evidenzia l’uso combinato di due tecniche semplici ma efficaci. **Spoofing del dominio mittente** e **allegato HTML attivo** per la sottrazione di credenziali. Nel campione analizzato, l’allegato simula una pagina di autenticazione e tenta di inviare le credenziali a un canale controllato dall’attaccante tramite la **Telegram Bot API**.

## Spoofing del mittente

Il messaggio appare provenire da un indirizzo interno all’organizzazione. L’analisi degli header SMTP ha però mostrato che l’invio è avvenuto tramite infrastrutture esterne non autorizzate.

È uno schema ricorrente. Si sfruttano server compromessi o account SMTP abusati per aumentare la probabilità di consegna e superare controlli superficiali. Senza allineamento e applicazione effettiva di **SPF**, **DKIM** e **DMARC** con policy restrittive, l’origine può essere falsificata con relativa facilità.

## L’allegato HTML come vettore

L’allegato è una pagina HTML con JavaScript integrato. Una volta aperto nel browser, **si comporta come una piccola applicazione**. Può interagire con il DOM e inviare richieste HTTP verso l’esterno senza richiedere installazione o privilegi elevati.

![](https://cert-agid.gov.it/wp-content/uploads/2026/02/image-2.png)

Nel caso analizzato, la pagina riproduce una schermata di login generica con campi **Email** e **Password**, accompagnata da messaggi che richiamano sicurezza e autenticazione obbligatoria. L’obiettivo è sfruttare uno schema familiare in modo che l’utente riconosce la forma e completa l’azione.

Il file include anche un meccanismo di targeting: un valore preimpostato in un campo nascosto viene copiato in una variabile JavaScript e utilizzato per precompilare il form con l’email del destinatario. **L’allegato può quindi essere personalizzato per una vittima o per un dominio specifico.**

## Offuscamento e raccolta di contesto

Lo script principale è incapsulato in una chiamata `document.write(unescape(...))`. Non si tratta di un offuscamento avanzato, ma è spesso sufficiente a rendere meno immediata la lettura del codice e a eludere controlli basati su pattern elementari.

Prima dell’esfiltrazione lo script tenta di raccogliere alcune informazioni, come l’**IP pubblico** e dati geografici approssimativi, tramite servizi esterni.

![](https://cert-agid.gov.it/wp-content/uploads/2026/02/image-3.png)

La presenza del *timestamp* e del contatore dei tentativi consente all’attaccante di comprendere la dinamica dell’interazione. L’*hostname* permette di verificare se il file è stato aperto localmente, su un dominio web o in un ambiente di analisi.

Nel codice è inoltre presente un commento che richiama una presunta “FOR EDUCATIONAL DEMONSTRATION ONLY”, questo tipo di dicitura è abbastanza frequente nei kit riutilizzati.

Questi elementi vengono aggiunti al messaggio inviato all’attaccante e consentono di **classificare le credenziali** sottratte in base al **contesto geografico** e **organizzativo**.

Le credenziali non hanno tutte lo stesso valore. Informazioni aggiuntive come paese di origine, dominio coinvolto o contesto temporale permettono una selezione preliminare e aumentano la loro appetibilità nei circuiti di rivendita illecita.

## CAPTCHA e simulazione del flusso di autenticazione

La pagina integra un CAPTCHA validato solo lato client. Serve solo a rendere il flusso più credibile e a simulare un controllo di sicurezza.

Dopo l’inserimento delle credenziali, il sistema mostra messaggi come “*Checking credentials*” e successivamente “*Login failed*”. La password viene cancellata e il CAPTCHA rigenerato. Dopo più tentativi è previsto un **reindirizzamento verso un sito legittimo**, così da ridurre il sospetto e chiudere l’interazione con un comportamento plausibile.

## Esfiltrazione tramite Telegram

La componente più rilevante è l’invio dei d...