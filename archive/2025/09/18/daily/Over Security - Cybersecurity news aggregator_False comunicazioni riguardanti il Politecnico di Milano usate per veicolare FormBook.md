---
title: False comunicazioni riguardanti il Politecnico di Milano usate per veicolare FormBook
url: https://cert-agid.gov.it/news/false-comunicazioni-riguardanti-il-politecnico-di-milano-usate-per-veicolare-formbook/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-18
fetch_date: 2025-10-02T20:19:31.158778
---

# False comunicazioni riguardanti il Politecnico di Milano usate per veicolare FormBook

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
* False comunicazioni riguardanti il Politecnico di Milano usate per veicolare FormBook

# False comunicazioni riguardanti il Politecnico di Milano usate per veicolare FormBook

17/09/2025

 [formbook](https://cert-agid.gov.it/tag/formbook/)
[università](https://cert-agid.gov.it/tag/universita/)

Negli scorsi giorni il CERT-AGID ha individuato e analizzato una campagna mirata alla diffusione del malware **FormBook** tramite e‑mail dirette, presumibilmente, a operatori del settore edilizio.

Il messaggio, ben formattato e curato nei dettagli, simula di provenire da un ufficio del **Politecnico di Milano** e invita i destinatari a presentare un’offerta per un presunto progetto, con una scadenza ravvicinata.

![](https://cert-agid.gov.it/wp-content/uploads/2025/09/Phishing_POLIMI_email.png)

L’e-mail ingannevole invita il destinatario a consultare la documentazione allegata spingendolo ad aprire il file **ZIP** allegato, che invece di contenere uno o più documenti nasconde uno script **JS malevolo**.

![](https://cert-agid.gov.it/wp-content/uploads/2025/09/Phishing_POLIMI_script.png)

Il codice *JavaScript*, parzialmente offuscato, avvia uno script *PowerShell* che scarica ed esegue ulteriori componenti. Nella fase finale, questi componenti installano il trojan **FormBook**, ampiamente consciuto e progettato per sottrarre credenziali e dati sensibili.

## Un inganno aziendale credibile

La campagna, pur essendo tecnicamente semplice, **risulta credibile e ben orchestrata**: sfrutta dinamiche aziendali comuni, come inviti di partecipazione a progetti o proposte commerciali, per superare più facilmente la diffidenza dei destinatari. Questa somiglianza con situazioni reali aumenta la probabilità che i documenti vengano aperti e i contenuti malevoli, quindi, attivati. In questi casi conta poco la sofisticazione tecnica ma molto di più la capacità dell’attacco di incontrare le aspettative del ricevente.

## Raccomandazioni

Il CERT-AGID, che ha informato tempestivamente il Politecnico di Milano, invita gli utenti a prestare la massima attenzione ai messaggi sospetti e a seguire le solite precauzioni del caso:

1. **Verificare attentamente l’origine dei messaggi**: diffidare di comunicazioni provenienti da indirizzi email sconosciuti o appartenenti a domini sospetti, con errori di ortografia o variazioni rispetto al dominio ufficiale del mittente, o domini diversi da quelli attesi per l’interlocutore.
2. **Diffidare di allegati compressi come ZIP e RAR, specie se provenienti da mittenti non noti**: i file malevoli vengono spesso inviati all’interno di archivi perché ciò permette di eludere più facilmente i filtri antispam.
3. **Non aprire eseguibili, script o file con estensioni insolite**: controlla l’estensione dei file prima di aprirli e assicurati che corrisponda al tipo dichiarato (per esempio, *.pdf* per documenti PDF, *.jpg*/*.jpeg*/*.png*/*.webp* per immagini).
4. Segnalare i messaggi sospetti: inoltrare le comunicazioni dubbie al CERT-AGID all’indirizzo **malware@cert-agid.gov.it**

## Indicatori di Compromissione

Gli IoC relativi a questa campagna sono stati già condivisi con le organizzazioni [accreditate al flusso IoC](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/) del CERT-AGID.

**Link:** [Download IoC](https://cert-agid.gov.it/wp-content/uploads/2025/09/Phishing_POLIMI.json)

Taggato
[formbook](https://cert-agid.gov.it/tag/formbook/)
[università](https://cert-agid.gov.it/tag/universita/)

## Navigazione articoli

[Notizia precedente Campagna malware abusa di strumenti di RMM legittimi tramite falsa condivisione di documenti](https://cert-agid.gov.it/news/campagna-malware-abusa-di-strumenti-di-rmm-legittimi-tramite-falsa-condivisione-di-documenti/)

[Prossima notizia: Sintesi riepilogativa delle campagne malevole nella settimana del 13 – 19 settembre](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-13-19-settembre/)

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