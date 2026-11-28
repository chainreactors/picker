---
title: ClickFix: falsa verifica Cloudflare su un portale scolastico diffonde nuovo RAT Olympic 0.1.0
url: https://cert-agid.gov.it/news/clickfix-falsa-verifica-cloudflare-su-un-portale-scolastico-diffonde-nuovo-rat-olympic-0-1-0/
source: Over Security
date: 2026-11-27
fetch_date: 2026-11-28T09:42:50.971788
---

# ClickFix: falsa verifica Cloudflare su un portale scolastico diffonde nuovo RAT Olympic 0.1.0

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
* ClickFix: falsa verifica Cloudflare su un portale scolastico diffonde nuovo RAT Olympic 0.1.0

# ClickFix: falsa verifica Cloudflare su un portale scolastico diffonde nuovo RAT Olympic 0.1.0

27/11/2026

 [ClickFix](https://cert-agid.gov.it/tag/clickfix/)
[Donut](https://cert-agid.gov.it/tag/donut/)
[malware](https://cert-agid.gov.it/tag/malware/)
[Olympic](https://cert-agid.gov.it/tag/olympic/)
[PowerShell](https://cert-agid.gov.it/tag/powershell/)

Il CERT-AGID ha individuato una campagna che sfrutta una pagina malevola ospitata su un sottodominio riconducibile a un istituto scolastico italiano. La pagina imita una verifica **CAPTCHA** di Cloudflare e invita l’utente a eseguire manualmente un comando *PowerShell* per completare il presunto controllo di sicurezza.

La tecnica nota come **[ClickFix](https://cert-agid.gov.it/tag/ClickFix/)**, sfrutta la fiducia dell’utente in una procedura familiare per indurlo a eseguire istruzioni malevole sul proprio dispositivo. In questo caso, il comando avvia una catena di caricamento che porta all’esecuzione di **Olympic**, un trojan modulare per l’accesso remoto a sistemi Windows osservato per la prima volta dal CERT-AGID.

## La pagina malevola

Alla prima visita viene mostrata una schermata che riproduce graficamente una verifica di sicurezza Cloudflare, accompagnata dal messaggio «*To better prove you are not a robot*».

![](https://cert-agid.gov.it/wp-content/uploads/2026/11/Schermata-del-2026-11-26-15-06-09-2-1024x549.png)

Il finto popup invita l’utente a completare una presunta procedura di verifica seguendo le classiche istruzioni già viste in altre campagne ClickFix:

1. Premere la combinazione di tasti `Windows + X`.
2. Selezionare PowerShell o Terminale premendo il tasto `I`.
3. Incollare il contenuto precedentemente copiato tramite la combinazione `CTRL + V`.
4. Premere `Invio` per completare la verifica.

La procedura, ovviamente, non costituisce una reale verifica CAPTCHA, ma induce l’utente a eseguire direttamente un comando malevolo nel terminale di Windows.

## Il comando PowerShell

Il comando presentato dalla pagina, visibile dal sorgente, è il seguente:

![](https://cert-agid.gov.it/wp-content/uploads/2026/11/Schermata-del-2026-11-26-15-23-15.png)

L’analisi delle istruzioni evidenzia le seguenti operazioni:

* **Definizione del percorso:** individua la directory `%APPDATA%\uni2\` e imposta il nome del file eseguibile `Beautifull.exe`.
* **Creazione della directory:** utilizza `New-Item` per creare la cartella di destinazione, qualora non esista già.
* **Download del payload:** tramite `curl.exe`, scarica il contenuto restituito dall’indirizzo dal repository remoto salvandolo localmente con il nome `Beautifull.exe`.
* **Esecuzione:** verifica l’esistenza del file attraverso `Test-Path` e, in caso positivo, lo avvia mediante `Start-Process`.

L’esecuzione non necessita di privilegi amministrativi e non presenta particolari elementi che possano insospettire un utente poco esperto, soprattutto perché viene eseguito nell’ambito di una presunta procedura di verifica.

## Catena di distribuzione del RAT Olympic

L’analisi del file recuperato ha ricostruito una catena di caricamento a più stadi. Il primo eseguibile, nativo per Windows x64, avvia uno shellcode **Donut**, che carica in memoria un secondo eseguibile nativo. Quest’ultimo svolge la funzione di downloader.

La decodifica XOR della configurazione del downloader ha permesso di individuare il server di distribuzione.

![](https://cert-agid.gov.it/wp-content/uploads/2026/11/image-17-1024x425.png)

*Nuovo repository contattato*

Trattasi ancora una volta di un nuovo loader usato per contattare un nuovo repository dall’indirizzo ricavato e ottenere un ulteriore eseguibile.

L’eseguibile così recuperato contiene la stringa **`Olympic 0.1.0`** e il tag di build **`TOMAS_2`**. La versione `0.1.0` è quella dichiarata nel binario.

![](https://cert-agid.gov.it/wp-content/uploads/2026/11/image-20.png)

*Stringa ricorrente Olympic 0.1.0*

La configurazione in chiaro indica il server di comando e controllo del RAT e il tag **`TOMAS_2`**.

![](https://cert-agid.gov.it/wp-content/uploads/2026/11/image-19.png)

*Server C2 in chiaro*

**Olympic è un RAT modulare per Windows x64.** L’eseguibile gestisce l’identità del dispositivo, comunica con il server di comando e controllo tramite WebSocket e può scaricare, verificare e caricare in memoria moduli aggiuntivi. Include anche una procedura di autorimozione.

La tabella seguente riporta le funzionalità che l’agente può esporre tramite i suoi moduli.

| Funzionalità RAT | Evidenza nel campione |
| --- | --- |
| **Comando e controllo (C2)** | Apre un WebSocket su `/ws/publisher`, invia e riceve messaggi e costruisce `device-capabilities` e `device-profile` associati a un `deviceId`. |
| **Profilazione del dispositivo** | Gestisce un’identità locale e serializza un inventario dei browser installati. |
| **Caricamento di moduli** | Consulta catalogo e riferimenti di integrità, scarica pacchetti, ne verifica lo SHA-256 e dispone di un mapper PE32+ per caricarli...