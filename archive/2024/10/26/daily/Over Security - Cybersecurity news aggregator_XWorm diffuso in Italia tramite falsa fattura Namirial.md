---
title: XWorm diffuso in Italia tramite falsa fattura Namirial
url: https://cert-agid.gov.it/news/xworm-diffuso-in-italia-tramite-falsa-fattura-namirial/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-26
fetch_date: 2025-10-06T18:54:50.018251
---

# XWorm diffuso in Italia tramite falsa fattura Namirial

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
* XWorm diffuso in Italia tramite falsa fattura Namirial

# XWorm diffuso in Italia tramite falsa fattura Namirial

25/10/2024

 [Namirial](https://cert-agid.gov.it/tag/namirial/)
[Xworm](https://cert-agid.gov.it/tag/xworm/)

![](https://cert-agid.gov.it/wp-content/uploads/2024/10/email-namirial-xworm.png)

Il CERT-AGID ha rilevato una campagna malevola volta alla diffusione del trojan **XWorm RAT,** distribuito tramite false email camuffate da comunicazioni ufficiali del gestore **Namirial**.

L’email, redatta in italiano, invita l’utente a visualizzare un documento PDF allegato e, nel caso in cui il file non si apra correttamente, suggerisce di utilizzare un link alternativo presente nel corpo del messaggio.

![](https://cert-agid.gov.it/wp-content/uploads/2024/10/fake-pdf-namirial-xworm.png)

In realtà, il file PDF funge da esca, poiché è protetto da password. Questo porta la vittima a cliccare sull’unico link alternativo disponibile che avvia il download di un archivio ZIP, ospitato su Dropbox, contenente un file URL. Da qui ha inizio la catena di compromissione.

Il file URL [sfrutta la funzionalità TryCloudflare](https://www.proofpoint.com/us/blog/threat-insight/threat-actor-abuses-cloudflare-tunnels-deliver-rats) che consente agli attaccanti di creare tunnel temporanei verso server locali e testare il servizio senza necessità di un account Cloudflare. Ogni tunnel genera un sottodominio casuale sul dominio *trycloudflare.com*, utilizzato per instradare il traffico attraverso la rete di Cloudflare verso il server locale.

![](https://cert-agid.gov.it/wp-content/uploads/2024/10/image.png)

Il file URL procede quindi al download di un file BAT, offuscato tramite lo strumento **BatchShield**. Questo può essere facilmente deoffuscato utilizzando un tool specifico denominato [BatchShield decryptor](https://github.com/Einstein2150/BatchShield-Decryptor).

![](https://cert-agid.gov.it/wp-content/uploads/2024/10/image-1.png)

BAT Offuscato

![](https://cert-agid.gov.it/wp-content/uploads/2024/10/image-2.png)

BAT Deoffuscato

A questo punto, il procedimento è ben noto, essendo già stato osservato in campagne precedenti. Viene scaricato un ulteriore archivio ZIP contenente l’interprete Python, utilizzato per eseguire gli script malevoli già inclusi nell’archivio. Questo processo porta al rilascio di uno dei seguenti malware: AsyncRAT, DCRat, GuLoader, VenomRAT, Remcos RAT o, come nel caso attuale, **XWorm**.

## Indicatori di Compromissione

Al fine di rendere pubblici i dettagli della campagna odierna si riportano di seguito gli IoC rilevati:

**Link:** [Download IoC](https://cert-agid.gov.it/wp-content/uploads/2024/10/xworm-namirial-25-10-2024.json)

Taggato
[Namirial](https://cert-agid.gov.it/tag/namirial/)
[Xworm](https://cert-agid.gov.it/tag/xworm/)

## Navigazione articoli

[Notizia precedente Sintesi riepilogativa delle campagne malevole nella settimana del 19 – 25 ottobre](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-19-25-ottobre/)

[Prossima notizia: Sintesi riepilogativa delle campagne malevole nella settimana del 26 ottobre – 1 novembre](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-26-ottobre-1-novembre/)

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