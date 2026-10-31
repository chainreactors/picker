---
title: PHP2Shell: diminuiscono le URL potenzialmente vulnerabili. Disponibili gli strumenti AgID
url: https://cert-agid.gov.it/news/php2shell-diminuiscono-le-url-potenzialmente-vulnerabili-disponibili-gli-strumenti-agid/
source: Over Security
date: 2026-10-30
fetch_date: 2026-10-31T07:48:31.635276
---

# PHP2Shell: diminuiscono le URL potenzialmente vulnerabili. Disponibili gli strumenti AgID

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
* PHP2Shell: diminuiscono le URL potenzialmente vulnerabili. Disponibili gli strumenti AgID

# PHP2Shell: diminuiscono le URL potenzialmente vulnerabili. Disponibili gli strumenti AgID

30/10/2026

 [IPA](https://cert-agid.gov.it/tag/ipa/)
[php](https://cert-agid.gov.it/tag/php/)
[php2shell](https://cert-agid.gov.it/tag/php2shell/)

La ricognizione del CERT-AGID del **29 ottobre 2026** mostra un ulteriore miglioramento: **l’1,7% degli indirizzi IPA esaminati dichiara una versione PHP potenzialmente vulnerabile**. Si tratta di **382 URL**, rispetto alle **650** della prima rilevazione del [22 ottobre](https://cert-agid.gov.it/news/php2shell-650-url-potenzialmente-vulnerabili-tra-gli-indirizzi-censiti-in-ipa/).

![](https://cert-agid.gov.it/wp-content/uploads/2026/10/php2shell-29-ottobre-2026-1024x422.png)

*PHP2Shell: Ricognizione del 29 ottobre 2026*

Il segnale più significativo riguarda **215 delle URL inizialmente segnalate, circa una su tre, che dichiarano ora una versione aggiornata**. Rispetto al controllo del [26 ottobre](https://cert-agid.gov.it/news/php2shell-168-url-inizialmente-segnalate-dichiarano-ora-una-versione-aggiornata/), altre **47 URL** sono passate da una versione potenzialmente vulnerabile a una dichiarata aggiornata.

La verifica ha riguardato lo stesso elenco di **22.371 indirizzi web censiti in IPA**, consentendo un confronto omogeneo tra le rilevazioni.

## **Come leggere il miglioramento**

I risultati sono compatibili con interventi di aggiornamento, la cui conferma richiede comunque verifiche direttamente sui server. La diminuzione dei rilevamenti comprende anche indirizzi che non espongono più la versione PHP o che non sono risultati raggiungibili: **non tutti i casi usciti dalla categoria potenzialmente vulnerabile possono quindi essere considerati risolti**.

Il controllo resta passivo, senza payload o tentativi di sfruttamento, e limitato agli indirizzi dell’elenco IPA esaminato. Non sono stati ricercati ulteriori sottodomini, applicazioni o servizi non censiti. L’assenza della versione PHP non permette di escludere le vulnerabilità: nasconderla è una buona pratica per ridurre le informazioni pubbliche, ma non sostituisce le patch.

## Segnalazioni e solleciti alle amministrazioni

Il CERT-AGID ha già segnalato i nuovi casi alle amministrazioni interessate e inviato un sollecito per quelli precedentemente notificati che continuano a dichiarare una versione potenzialmente vulnerabile.

L’invito è a verificare con i propri amministratori di sistema e fornitori **la versione PHP effettivamente in esecuzione e le correzioni installate**, comprese eventuali patch applicate tramite backport, estendendo i controlli ai servizi non inclusi nella rilevazione.

## Gli strumenti AgID a disposizione delle amministrazioni

AgID ha pubblicato nel proprio [repository PHP2Shell su GitHub](https://github.com/AgID/PHP2Shell/tree/beta) gli strumenti utilizzati per verificare e correggere i propri server, principalmente **Ubuntu** e, in misura minore, **Fedora**. Li mette così a disposizione delle amministrazioni e dei loro fornitori.

Gli script consentono di:

* verificare i pacchetti PHP installati;
* installare gli aggiornamenti disponibili;
* applicare mitigazioni temporanee;
* individuare nei sistemi eventuali segnali che richiedono approfondimento.

**L’utilizzo richiede personale tecnico qualificato**, una verifica preliminare della compatibilità e test preventivi, nel rispetto della documentazione e dello stato dei test riportati nel repository.

Alcune funzioni modificano le configurazioni e riavviano i servizi. Si raccomanda quindi di:

* eseguire gli script prima in un **ambiente di replica**;
* predisporre adeguate **procedure di backup**;
* pianificare una finestra di **manutenzione**.

Le mitigazioni temporanee non sostituiscono l’installazione degli aggiornamenti di sicurezza.

Il progetto è aperto al contributo di pubbliche amministrazioni, fornitori, tecnici qualificati e professionisti della sicurezza informatica, tramite segnalazioni e proposte di modifica sul repository GitHub.

Taggato
[IPA](https://cert-agid.gov.it/tag/ipa/)
[php](https://cert-agid.gov.it/tag/php/)
[php2shell](https://cert-agid.gov.it/tag/php2shell/)

## Navigazione articoli

[Notizia precedente Phishing PagoPA: nuove campagne a tema multe diffuse tramite PEC compromesse](https://cert-agid.gov.it/news/phishing-pagopa-nuove-campagne-a-tema-multe-diffuse-tramite-pec-compromesse/)

[Prossima notizia: Sintesi riepilogativa delle campagne malevole nella settimana del 24 – 30 ottobre](https://cert-agid.gov.it/news/sintesi-riepilogativa-delle-campagne-malevole-nella-settimana-del-24-30-ottobre/)

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

![Logo del CERT-PA](/wp-content/themes/c...