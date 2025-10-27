---
title: Ursnif approda nel mondo delle app mobile: l’APK DroidJack viene veicolato come comunicazione Agenzia delle Entrate
url: https://cert-agid.gov.it/news/ursnif-approda-nel-mondo-delle-app-mobile-lapk-droidjack-viene-veicolato-come-comunicazione-agenzia-delle-entrate/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-28
fetch_date: 2025-10-04T10:54:26.999667
---

# Ursnif approda nel mondo delle app mobile: l’APK DroidJack viene veicolato come comunicazione Agenzia delle Entrate

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
* Ursnif approda nel mondo delle app mobile: l’APK DroidJack viene veicolato come comunicazione Agenzia delle Entrate

# Ursnif approda nel mondo delle app mobile: l’APK DroidJack viene veicolato come comunicazione Agenzia delle Entrate

27/03/2023

 [Agenzia Entrate](https://cert-agid.gov.it/tag/agenzia-entrate/)

Le campagne Ursnif a cui siamo ormai [abituati ad assistere](https://cert-agid.gov.it/news/malware/il-fenomeno-ursnif-in-italia-i-numeri-dellultima-ondata-di-campagne/) sono in costante evoluzione ma vi è sempre qualcosa che le accomuna: il tema **Agenzia delle Entrate**.

![](https://cert-agid.gov.it/wp-content/uploads/2023/03/email_agenzia-entrate_droidjack.png)

Lo screenshot pubblicato riguarda una email, che ci è stata segnalata in data odierna da [D3Lab](https://www.d3lab.net/), che ricalca le finte comunicazioni della Agenzia delle Entrate solitamente utilizzate per veicolare il malware Ursnif. Questa volta però il link non restituisce alcun file ma solo visitandolo con un dispositivo android rilascia un APK denominato **Agenzia.apk**.

Dalle analisi effettuate dal CERT-AGID il malware in questione risulta essere **[DroidJack](https://droidjack.net/)**, un RAT venduto come MaaS (al costo di 210 dollari) il cui scopo è quello di controllare da remoto il dispositivo compromesso, monitorare il traffico dei dati e intercettare le conversazioni.

Appena installato, il malware provvede a registrare il dispositivo compromesso comunicando al server C2 i dati su brand, modello, versione di Android e numero di telefono.

![](https://cert-agid.gov.it/wp-content/uploads/2023/03/doridjack_registrazione.png)

Inizia quindi ad acquisire informazioni presenti sul dispositivo e le conserva su un database SQLite (*SandroRat*):

![](https://cert-agid.gov.it/wp-content/uploads/2023/03/droidjack_sandrorat_sqlite.png)

DroidJack è in grado di **acquisire gli SMS**, i video (che salva in un file denominato “*video.3gp*“) e le **chiamate effettuate** (che verranno memorizzate in un file “*Record.amr*“).

I dati raccolti verranno successicamente cifrati con AES ed inoltrati sulla porta 1177 del C2, localizzato in Russia.

![](https://cert-agid.gov.it/wp-content/uploads/2023/03/droidjack_c2.png)

Il codice di DroidJack non è cambiato molto rispetto al 2016 quando fu veicolato per la prima volta come applicazione [Pokemon Go](https://blog.trustlook.com/pokemon-go-bundles-with-malicious-remote-administration-tool-droidjack/). L’algoritmo di cifratura, compresa la chiave AES utilizzata per cifrare i dati, risulta essere ancora la stessa.

![](https://cert-agid.gov.it/wp-content/uploads/2023/03/droidjack_aes.png)

Potrebbe quindi trattarsi di una vecchia versione (del 2016) riutilizzata con il solo cambio dell’indirizzo del server C2.

## Conclusioni

Dalla campagna odierna il CERT-AGID è riuscito da estrarre le URL (oltre 700) dai server di smistamento. È abbastanza chiaro che gli autori dietro questa campagna, rivolta ad utenti mobile (android), siano ancora una volta gli **stessi di Ursnif**.

* il tema è Agenzia delle Entrate;
* le e-mail utilizzano lo stesso oggetto;
* Il contenuto è identico a quello utilizzato per le campagne Ursnif;
* utilizzano i link dinamici Firebase;
* molte delle url sono state già riscontrate nella campagna Ursnif del 14 marzo.
* l’infrastruttura che distribuisce i file APK è la stessa delle campagne precedenti di Ursnif

Per la prima volta quindi assistiamo ad una campagna Ursnif rivolta ad utenti Android. L’apertura di un nuovo fronte da parte di Ursnif risulta ancora più preoccupante se considerata insieme alle massiccie ondate precedenti. Infatti non solo abbiamo assistito ad un notevole incremento degli attacchi in termini quantitativi ma adesso si aggiunge una svolta qualitativa, in cui gli autori hanno investito risorse per spostare il loro target da Windows ad Android.

I dati delle campagne Ursnif raccolti ed analizzati [precedentemente](https://cert-agid.gov.it/news/malware/il-fenomeno-ursnif-in-italia-i-numeri-dellultima-ondata-di-campagne/) mostravano chiaramente che gli utenti mobile rappresentavano un 30% delle potenziali vittime. E’ possibile che anche gli autori di Ursnif abbiano fatto simili considerazioni e che abbiano adottato una strategia data-driven per l’impostazione delle loro compagne.

Quale sia la necessità di una così capillare capacità di infezione non è facile da stabilirsi, fatto sta che il malware Ursnif sta mostrando in queste settimane una febbrile attività che ha come target l’Italia e che sembra avere nuova energia. Se questa tendenza continuerà o andrà a scemare è difficile da dire poichè non molto si sà degli autori di Ursnif (se non presumibilmente la nazionalità) e se le loro motivazioni siano puramente economiche o, visti i tempi, anche geopolitiche.

## Indicatori di Compromissione

Gli IoC relativi a questa campagna sono stati già condivisi con le organizzazioni [accreditate al flusso IoC](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/) del CERT-AgID.

**Link:** [Download IoC](https://cert-agid.gov.it/wp-content/uploads...