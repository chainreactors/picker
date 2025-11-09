---
title: Analisi di Remcos RAT diffuso in Italia con campagna ClickFix a tema GLS
url: https://cert-agid.gov.it/news/analisi-di-remcos-rat-diffuso-in-italia-con-campagna-clickfix-a-tema-gls/
source: Over Security - Cybersecurity news aggregator
date: 2025-11-08
fetch_date: 2025-11-09T03:14:40.195941
---

# Analisi di Remcos RAT diffuso in Italia con campagna ClickFix a tema GLS

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
* Analisi di Remcos RAT diffuso in Italia con campagna ClickFix a tema GLS

# Analisi di Remcos RAT diffuso in Italia con campagna ClickFix a tema GLS

08/11/2025

 [ClickFix](https://cert-agid.gov.it/tag/clickfix/)
[GLS](https://cert-agid.gov.it/tag/gls/)
[remcos](https://cert-agid.gov.it/tag/remcos/)

![](https://cert-agid.gov.it/wp-content/uploads/2025/11/image-1024x567.png)

È in corso una campagna malspam, diffusa su larga scala, che utilizza il **brand GLS** come esca per indurre gli utenti a compilare un presunto modulo di riconsegna.

Le email presentano come oggetto “*Indirizzo non valido, compila il modulo 8900395*” e contengono un testo che simula una comunicazione del servizio clienti GLS, segnalando un problema nella consegna di un pacco e invitando a compilare un allegato.

L’allegato, un file **XHTML**, contiene codice JavaScript offuscato mediante operazioni `XOR` che, una volta decodificato, reindirizza l’utente verso il dominio malevolo ospitato sulla piattaforma *Netlify*.

![](https://cert-agid.gov.it/wp-content/uploads/2025/11/2025-11-08_11-44-1024x524.png)
![](https://cert-agid.gov.it/wp-content/uploads/2025/11/2025-11-08_11-45-1024x694.png)

Il sito replica l’aspetto del portale GLS e sfrutta la tecnica [**ClickFix**](https://cert-agid.gov.it/tag/clickfix/): tramite istruzioni di ingegneria sociale induce la vittima a copiare e incollare comandi nel terminale che scaricano o eseguono codice dannoso compromettendo il sistema.

Già osservata in campagne recenti, la tecnica usa un falso `CAPTCHA` per convincere l’utente a compiere azioni apparentemente legittime (incollare comandi o eseguire scorciatoie) che in realtà attivano codice dannoso. L’esecuzione manuale rende la campagna più difficile da intercettare e neutralizzare.

Seguendo le istruzioni del falso `CAPTCHA` viene eseguito un comando `mshta` che richiama un file `.hta` remoto passando un parametro che probabilmente funge da identificativo. Dall’analisi delle email, l’URL al file HTA rimane costante mentre il parametro varia puntualmente.

Il file HTA risulta totalmente offuscato. Il codice viene decodificato all’apertura tramite una funzione `XOR` con chiave inclusa nello script.

![](https://cert-agid.gov.it/wp-content/uploads/2025/11/2025-11-08_11-55-1024x418.png)

*Codice deoffuscato con Cyberchef*

Il payload ha lo scopo di scaricare da un dominio secondario un file binario e avviarlo sul sistema.

All’analisi preliminare del file binario si rileva la presenza di una risorsa denominata `SETTINGS`, elemento tipico riscontrato nei sample di **Remcos RAT**. Questo suggerisce che il binario possa essere una build di Remcos e quindi finalizzato a controllo remoto, raccolta dati e caricamento/avvio di payload secondari.

![](https://cert-agid.gov.it/wp-content/uploads/2025/11/image-1.png)

Dall’analisi della risorsa `SETTINGS` emerge chiaramente la tipica configurazione di **Remcos**, una tra le minacce più diffuse nel panorama italiano insieme a *Formbook*.

![](https://cert-agid.gov.it/wp-content/uploads/2025/11/2025-11-08_14-52.png)

*Configurazione Remcos RAT cifrata*

Una volta estratti tutti i valori utili, l’analisi tramite **CyberChef** consente di decodificare la risorsa `SETTINGS` e identificare i dettagli di configurazione rilevanti (C2, agent ID, intervalli, etc.), utili per il blocco tramite IoC e la correlazione degli incidenti.

![](https://cert-agid.gov.it/wp-content/uploads/2025/11/image-2-1024x405.png)

*Decodifica configurazione Remcos RAT*

## Conclusioni

Le campagne basate sulla tecnica **ClickFix** sono ormai una tendenza consolidata: da circa un anno questo metodo viene sfruttato sempre più spesso per distribuire malware attraverso inganni che spingono l’utente a eseguire manualmente comandi dannosi.

In Italia la prima evidenza documentata risale al [gennaio](https://cert-agid.gov.it/news/analisi-di-una-campagna-lumma-stealer-con-falso-captcha-condotta-attraverso-domino-italiano-compromesso/) di quest’anno, quando la tecnica è stata utilizzata per diffondere [Lumma Stealer](https://cert-agid.gov.it/tag/lumma-stealer/), uno dei principali infostealer in circolazione. Da allora, pur essendo stati osservati diversi tentativi, nel nostro Paese non si sono registrate campagne massive mirate, a differenza di quanto accade in altri contesti internazionali dove il fenomeno è molto più diffuso.

I malware writer prediligono questa tecnica perché consente di aggirare i sistemi di sicurezza automatici. Il codice malevolo non viene scaricato o eseguito direttamente, ma solo dopo l’intervento dell’utente. L’esecuzione manuale rende il rilevamento più difficile per antivirus, sandbox e sistemi EDR, offrendo un alto tasso di successo a fronte di uno sforzo tecnico relativamente basso.

ClickFix rappresenta quindi un’evoluzione dell’ingegneria sociale applicata al malware delivery. Non punta a sfruttare vulnerabilità del software, ma quella più semplice e sempre attuale: l’interazione umana.

## Indicatori di compromissione

Il CERT-AGID ha già condiviso i relativi IoC con le organizzazioni [accreditate al flusso...