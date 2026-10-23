---
title: PHP2Shell: strumenti per verificare l’esposizione alle vulnerabilità critiche
url: https://cert-agid.gov.it/news/php2shell-strumenti-per-verificare-lesposizione-alle-vulnerabilita-critiche/
source: Over Security
date: 2026-10-22
fetch_date: 2026-10-23T06:46:32.941439
---

# PHP2Shell: strumenti per verificare l’esposizione alle vulnerabilità critiche

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
* PHP2Shell: strumenti per verificare l’esposizione alle vulnerabilità critiche

# PHP2Shell: strumenti per verificare l’esposizione alle vulnerabilità critiche

22/10/2026

 [CVE-2026-109618](https://cert-agid.gov.it/tag/cve-2026-109618/)
[CVE-2026-109619](https://cert-agid.gov.it/tag/cve-2026-109619/)
[php](https://cert-agid.gov.it/tag/php/)
[php2shell](https://cert-agid.gov.it/tag/php2shell/)

A seguito della [pubblicazione](https://cert-agid.gov.it/news/due-vulnerabilita-critiche-in-php-consentono-lesecuzione-di-codice-da-remoto-rilasciati-aggiornamenti-di-sicurezza/) delle vulnerabilità critiche **CVE-2026-109618** e **CVE-2026-109619**, il CERT-AGID segnala la disponibilità di due strumenti open source che, allo stato attuale, rappresentano soluzioni utili per supportare le amministrazioni nell’individuazione dei sistemi PHP potenzialmente vulnerabili.

Gli strumenti adottano approcci differenti, dal controllo della versione PHP all’analisi del comportamento del server mediante richieste HTTP appositamente predisposte.

## OpenAI PHP2Shell Checker

Lo strumento [OpenAI PHP2Shell Checker](https://github.com/openai/php2shell-checker) consente di verificare la versione PHP dichiarata da un server web oppure installata localmente, confrontandola con le versioni correttive disponibili.

Il controllo remoto si basa sull’analisi degli header HTTP e **non esegue tentativi di sfruttamento delle vulnerabilità**.

Per utilizzarlo, dopo aver scaricato il repository, è possibile eseguire:

**Verifica di un sito web:**

```
node phpcheck.js https://example.com
```

**Verifica della versione PHP locale:**

```
node phpcheck.js --local
```

Il programma restituisce un esito `OK`, `VULNERABLE` oppure `UNKNOWN`. Quest’ultimo indica che non è stato possibile determinare lo stato del sistema, ad esempio perché il server non espone la versione PHP.

OpenAI ha inoltre reso disponibile questi tool sotto forma di **skill per OpenAI Codex**, attraverso le quali è possibile effettuare le verifiche direttamente dall’assistente, sia su siti web remoti (`phpcheck-url`) sia su installazioni PHP locali (`phpcheck-server`).

## Assetnote PHP2Shell Scanner

Lo strumento [Assetnote PHP2Shell Scanner](https://github.com/assetnote/php2shell-scanner) effettua controlli più approfonditi, inviando richieste HTTP `multipart/form-data` appositamente costruite e analizzando eventuali anomalie nelle risposte del server, tra cui errori di memoria e interruzioni inattese dei processi PHP.

Dopo aver scaricato il repository e installato le dipendenze:

```
pip install -r requirements.txt
```

È possibile verificare un singolo servizio:

```
python3 scanner.py -u https://example.com -t 1
```

Oppure esaminare un elenco di servizi:

```
python3 scanner.py -l hosts.txt -t 1 -o risultati.json
```

L’opzione `-t 1` limita l’esecuzione a un solo thread, riducendo il carico dei test concorrenti.

**Attenzione:** a differenza del controllo di OpenAI, Assetnote esegue test attivi che possono generare errori o interferire con il funzionamento dei servizi. Si raccomanda pertanto di utilizzarlo esclusivamente su sistemi autorizzati, previa valutazione dei possibili impatti, preferibilmente in ambienti di test o durante finestre di manutenzione.

## Interpretazione dei risultati

Gli strumenti costituiscono un supporto alle verifiche, ma non garantiscono l’individuazione di tutti i sistemi vulnerabili. Un risultato negativo non esclude necessariamente la presenza delle vulnerabilità, mentre un risultato positivo, soprattutto nei controlli comportamentali, potrebbe richiedere ulteriori approfondimenti per escludere falsi positivi.

**Il CERT-AGID invita le amministrazioni a coinvolgere i rispettivi fornitori tecnologici nelle attività di verifica**, dando priorità ai servizi esposti su Internet e accertando l’effettiva applicazione degli aggiornamenti di sicurezza, comprese eventuali correzioni distribuite tramite backport.

La verifica della versione PHP effettivamente utilizzata dal servizio e delle patch installate rimane il riferimento principale per determinare lo stato di aggiornamento dei sistemi.

## Verifiche aggiuntive sui server

Qualora gli strumenti di verifica remota non riescano a determinare la versione PHP utilizzata, gli amministratori possono effettuare alcuni controlli direttamente sui sistemi.

**1. Verificare la versione PHP installata**

```
php -v
```

Il comando restituisce la versione dell’interprete PHP da riga di comando, che potrebbe differire da quella utilizzata dal servizio web.

**2. Identificare la modalità di esecuzione di PHP**

Per verificare se Apache utilizza il modulo PHP:

```
apachectl -M 2>/dev/null | grep -i php
```

Per individuare eventuali processi PHP-FPM attivi:

```
ps -eo pid,ppid,args | grep '[p]hp-fpm'
```

Questi controlli aiutano a individuare i componenti PHP in esecuzione, ma non ne attestano lo stato di aggiornamento.

**3. Verificare alcune impostazioni di PHP-FPM**

```
php-fpm8.4 -i | grep -E \
'session.upload_progress.enabled|memory_limit|fatal_error_backtraces'
```

Sostituire `php-fpm8.4` con l’eseguibile corrispondente alla versione installata. Il pa...