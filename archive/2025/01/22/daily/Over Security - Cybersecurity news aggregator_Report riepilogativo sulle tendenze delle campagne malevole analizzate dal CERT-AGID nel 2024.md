---
title: Report riepilogativo sulle tendenze delle campagne malevole analizzate dal CERT-AGID nel 2024
url: https://cert-agid.gov.it/news/report-riepilogativo-sulle-tendenze-delle-campagne-malevole-analizzate-dal-cert-agid-nel-2024/
source: Over Security - Cybersecurity news aggregator
date: 2025-01-22
fetch_date: 2025-10-06T20:12:27.202416
---

# Report riepilogativo sulle tendenze delle campagne malevole analizzate dal CERT-AGID nel 2024

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
* Report riepilogativo sulle tendenze delle campagne malevole analizzate dal CERT-AGID nel 2024

# Report riepilogativo sulle tendenze delle campagne malevole analizzate dal CERT-AGID nel 2024

21/01/2025

 [2024](https://cert-agid.gov.it/tag/2024/)

Questo report offre un quadro sintetico sui numeri delle principali campagne malevole osservate dal CERT‑AGID nel corso del 2024 che hanno colpito soggetti pubblici e privati afferenti alla propria *constituency*.

Le informazioni qui presentate sono state raccolte tramite diverse fonti, tra le quali le segnalazioni spontanee provenienti da soggetti privati o Pubbliche Amministrazioni, le rilevazioni dei sistemi automatizzati del CERT-AGID impiegati a difesa proattiva della propria *constituency*, le analisi dettagliate di campioni di malware e le indagini sugli incidenti trattati.

## Analisi delle tendenze generali

Dall’analisi delle tendenze generali riscontrate nel periodo considerato, si sono contraddistinte, nel vasto panorama delle minacce informatiche, le seguenti:

* **aumento delle campagne via caselle PEC compromesse**: l’utilizzo di caselle di Posta Elettronica Certificata (PEC) compromesse è triplicato rispetto all’anno precedente, con un picco di attività registrato nella seconda metà del 2024. Questo vettore, sempre ambito dagli attori malevoli, consente di rendere più verosimili le campagne di [phishing](https://cert-agid.gov.it/news/caselle-pec-sempre-piu-usate-nel-phishing-per-le-frodi-bancarie/) e permette di aumentare la distribuzione di [malware](https://cert-agid.gov.it/tag/vidar/) come **Vidar**;
* **incremento dell’uso di bot Telegram come C2**: quest’anno si è registrato un significativo aumento dell’utilizzo improprio di [bot Telegram come server di Command and Control (C2) per attività di phishing e distribuzione di malware](https://cert-agid.gov.it/tag/telegram/). Questa strategia permette agli attori malevoli di gestire con un buon grado di anonimato le comunicazioni con i sistemi compromessi.
* **in crescita la registrazione di domini potenzialmente ingannevoli**: durante il 2024 sono stati registrati numerosi domini che richiamano il nome di enti noti come **[INPS](https://cert-agid.gov.it/news/rilevata-campagna-malware-spynote-mascherata-come-app-inps-mobile/)**, **Agenzia delle Entrate** e **Polizia di Stato**. Sebbene alcuni siano stati realmente utilizzati per campagne di phishing e altre truffe, la maggior parte di essi è rimasta inattiva o è attualmente in vendita.
* **prevalenza degli infostealertra i software malevoli:** gli infostealer hanno rappresentato la categoria di malware più diffusa, veicolati principalmente tramite archivi compressi di tipo ZIP e RAR. Questi formati continuano a essere i vettori iniziali più usati, spesso contenenti script o eseguibili utili ad avviare la catena di infezione;
* **incremento delle minacce per sistemi Android**: le campagne malevole rivolte ai dispositivi mobili hanno registrato un notevole aumento rispetto all’anno precedente. Malware come Irata e SpyNote sono stati diffusi tramite smishing e file APK malevoli, con lo scopo principale di rubare credenziali bancarie e codici OTP, eseguendo transazioni fraudolente in tempo reale.

## I dati riepilogativi del 2024

Nel corso del 2024, il CERT-AGID ha individuato e contrastato un totale di **1767** campagne malevole, condividendo con la sua [constituency](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/) un totale di **19.939** Indicatori di Compromissione (IoC).

|  | Malware | Phishing |
| --- | --- | --- |
| Famiglie rilevate / Brand coinvolti | 69 | 133 |
| Campagne censite | 639 | 1128 |
| Indicatori di Compromissione (IoC) diramati | 6645 | 13294 |

In totale sono state identificate **69 famiglie di malware**. Dei sampleanalizzati, circa il 67% rientra nella categoria degli Infostealer, mentre il restante 33% in quella dei RAT (Remote Access Trojan). Nel contesto di attacchi di phishing/smishing, che hanno coinvolto complessivamente **133 brand**, l’obiettivo principale è stato il furto di credenziali bancarie, di credenziali di accesso a webmail e, nel caso dello smishing ai danni di INPS, il furto di documenti di identità.

## I 10 malware più diffusi in Italia

![](https://cert-agid.gov.it/wp-content/uploads/2025/01/malware-2024.png)

Nel corso del 2024, **AgentTesla** si è affermato come il malware più diffuso in Italia, seguito da **Formbook** e **Remcos**. Appena fuori dai primi 10, con 10 eventi, troviamo anche [Vidar](https://cert-agid.gov.it/news/ritorna-vidar-in-italia-con-una-campagna-di-malspam-tramite-pec/), un Malware-as-a-Service appartenente alla categoria degli Infostealer, veicolato tramite indirizzi **PEC** compromessi.

## I 10 “temi” più sfruttati per veicolare malware

![](https://cert-agid.gov.it/wp-content/uploads/2025/01/themes-malware-2024.png)

I principali “temi” sfruttati rimangono simili a quelli degli anni precedenti. Particolarmente ricorrente è stato il tema Pagamenti, utilizzato in ben **141** campagne. I malware più frequentemente diffusi mediante tale argomento sono s...