---
title: Analisi di una campagna WsgiDAV multi-stage: falsa comunicazione da Agenzia Nazionale Finanziaria
url: https://cert-agid.gov.it/news/analisi-di-una-campagna-wsgidav-multi-stage-falsa-comunicazione-da-agenzia-nazionale-finanziaria/
source: Over Security - Cybersecurity news aggregator
date: 2026-03-03
fetch_date: 2026-03-04T04:04:15.383358
---

# Analisi di una campagna WsgiDAV multi-stage: falsa comunicazione da Agenzia Nazionale Finanziaria

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
* Analisi di una campagna WsgiDAV multi-stage: falsa comunicazione da Agenzia Nazionale Finanziaria

# Analisi di una campagna WsgiDAV multi-stage: falsa comunicazione da Agenzia Nazionale Finanziaria

03/03/2026

 [WsgiDAV](https://cert-agid.gov.it/tag/wsgidav/)

Il caso qui analizzato prende spunto da un’email di phishing con oggetto “**Informare servicii online ANBSC**“, ricevuta il 27 febbraio 2026. Il messaggio impersonifica la provenienza da un ente fiscale e utilizza il pretesto di una presunta irregolarità dichiarativa del 2025 per indurre il destinatario a cliccare sul link esterno:

![](https://cert-agid.gov.it/wp-content/uploads/2026/03/email.png)

L’oggetto dell’email fa riferimento alla “**ANBSC**“, acronimo dell’*Agenzia Nazionale per l’Amministrazione e la Destinazione dei Beni Sequestrati e Confiscati alla Criminalità Organizzata*, con sede in Via Ezio, Roma. Tuttavia, nel footer del messaggio è riportato l’indirizzo “**Via Giorgione 106, Roma**“, sede dell’Agenzia delle Entrate.

La presenza di riferimenti a due enti distinti suggerisce un tentativo generico di simulazione istituzionale, caratterizzato da incongruenze che ne riducono la credibilità formale ma possono risultare comunque efficaci in un contesto di social engineering.

## Analisi statica

L’email proviene da un account associato a un dominio universitario spagnolo. Nel corpo del messaggio è presente un collegamento che avvia una catena di redirect fino al download di un archivio `ZIP` contenente un file con estensione `.url` (collegamento internet di Windows):

![](https://cert-agid.gov.it/wp-content/uploads/2026/03/2026-03-03_12-26.png)

La sintassi indica un accesso remoto tramite WebDAV su connessione TLS. L’URL punta a uno script `.wsh` ospitato su un dominio esposto tramite Cloudflare Tunnel. L’apertura del file shortcut comporta quindi il recupero e l’esecuzione dello script remoto `elcqjyp.wsh`:

![](https://cert-agid.gov.it/wp-content/uploads/2026/03/2026-03-03_12-39.png)

Il file `.wsh` non contiene la logica malevola finale ma funge solo da loader intermedio e richiama un secondo stadio in JavaScript `.js`, anch’esso ospitato sullo stesso server remoto:

![](https://cert-agid.gov.it/wp-content/uploads/2026/03/2026-03-03_12-40.png)

*uweepyj.js*

Lo script JS utilizza oggetti COM di Windows (`Scripting.FileSystemObject` e `WScript.Shell`), per interagire con il file system e con la shell di sistema. Tramite WebDAV scarica il batch principale `qidctgy.bat` nella directory `Downloads` dell’utente e ne avvia l’esecuzione con `cmd /c`.

![](https://cert-agid.gov.it/wp-content/uploads/2026/03/2026-03-03_12-41-1024x348.png)

*qidctgy.bat*

Il file `qidctgy.bat` è l’orchestratore dello stadio iniziale. Non contiene il RAT, ma prepara l’ambiente e avvia lo stadio successivo.

### Documento esca

Alla prima esecuzione apre un PDF legittimo a tema fiscale per rafforzare il pretesto dell’email, quindi rilancia se stesso in modalità nascosta tramite PowerShell con l’opzione `-WindowStyle Hidden`.

![](https://cert-agid.gov.it/wp-content/uploads/2026/03/2026-03-03_12-43.png)

*PDF legittimo*

### La persistenza

In seguito, imposta come directory operativa `%LOCALAPPDATA%\mrbqm` e verifica la presenza di un eseguibile `python.exe`. Se assente, scarica la versione embedded 3.14.0 da *python.org* ed estrae il runtime nella cartella locale. Garantisce la sua persistenza scaricando un ulteriore file batch nella cartella Startup dell’utente, impostando la sua esecuzione automatica al login.

### Decifratura payload

Successivamente scarica tre file dal server remoto, `sb.py`, `new.bin` e `a.txt`, quindi avvia la decifratura del file `new.bin` tramite lo script python `sb.py` usando le chiavi contenute in `a.txt` tramite diverse operazioni **XOR**.

![](https://cert-agid.gov.it/wp-content/uploads/2026/03/2026-03-03_12-44.png)

*Chiavi presenti nel file a.txt*

`python sb.py -i new.bin -k a.txt`

Il processo non usa un’unica chiave, ma tre passaggi consecutivi in ordine inverso rispetto alla disposizione nel file:

1. il blob viene trasformato con la prima chiave operativa (key3);
   * **d1 = XOR(new.bin, key3)**
2. il risultato viene ritrasformato con la seconda (key2);
   * **d2 = XOR(d1, key2)**
3. infine con la terza chiave (key1).
   * **d3 = XOR(d2, key1)**

Al termine dei tre layer XOR si ottiene il payload finale che viene iniettato in memoria nel processo `explorer.exe` attraverso la sequenza:

```
CreateProcessA -> VirtualAllocEx -> WriteProcessMemory -> QueueUserAPC -> ResumeThread
```

![](https://cert-agid.gov.it/wp-content/uploads/2026/03/image.png)

*Injector Python*

Il codice malevolo viene eseguito dentro un processo legittimo (`explorer.exe`) e non nel processo originario, rendendo la rilevazione più difficile.

## Analisi dinamica

A questo punto si è reso necessario procedere con l’analisi dinamica, effettuando il dump completo del processo `explorer.exe`, il quale, come evidenziato dallo screenshot di Process Explorer, risulta avviato dal processo `python.exe`.

![](https://cert-agid.gov.it/wp-content/uploads/...