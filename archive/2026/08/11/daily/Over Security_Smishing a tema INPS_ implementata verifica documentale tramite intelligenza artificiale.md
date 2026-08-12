---
title: Smishing a tema INPS: implementata verifica documentale tramite intelligenza artificiale
url: https://cert-agid.gov.it/news/smishing-a-tema-inps-implementata-verifica-documentale-tramite-intelligenza-artificiale/
source: Over Security
date: 2026-08-11
fetch_date: 2026-08-12T04:02:32.456765
---

# Smishing a tema INPS: implementata verifica documentale tramite intelligenza artificiale

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
* Smishing a tema INPS: implementata verifica documentale tramite intelligenza artificiale

# Smishing a tema INPS: implementata verifica documentale tramite intelligenza artificiale

11/08/2026

 [inps](https://cert-agid.gov.it/tag/inps/)
[Intelligenza Artificiale](https://cert-agid.gov.it/tag/intelligenza-artificiale/)
[phishing](https://cert-agid.gov.it/tag/phishing/)

Nelle ultime giornate il CERT-AGID ha osservato un incremento delle campagne di phishing che sfruttano il nome, il logo e la grafica di **INPS**. Gli SMS fraudolenti invitano l’utente a procedere al controllo dei propri dati per garantire la continuità dell’erogazione dei servizi, con un link che conduce a un sito contraffatto.

![](https://cert-agid.gov.it/wp-content/uploads/2026/08/photo_2026-08-11_12-38-36-e1786453132308.jpg)

*SMS con link al sito fraudolento*

Le pagine fraudolente riproducono fedelmente la grafica dei portali istituzionali e propongono un percorso guidato in cinque fasi, identico nella struttura a quello già documentato nelle [precedenti campagne che hanno sfruttato il medesimo tema](https://cert-agid.gov.it/tag/inps/) e finalizzato al caricamento delle seguenti informazioni: **dettagli anagrafici**, **documenti identificativi**, **buste paga**, **CUD** e **selfie**.

![](https://cert-agid.gov.it/wp-content/uploads/2026/08/Screenshot-from-2026-08-11-14-42-57.png)

*Pagina di caricamento della carta di identità*

Ciò che cambia, in questa nuova ondata, è l’**introduzione di un ulteriore livello di controllo sui file caricati dalla vittima basato su un modello di intelligenza artificiale**.

Il sistema integrato nel sito fraudolento è in grado di descrivere correttamente il contenuto dell’immagine caricata e di confrontarlo con il tipo di documento richiesto. Nei test condotti, il sistema ha rifiutato correttamente diversi tipi di illustrazioni, restituendo un messaggio di errore che ne descrive puntualmente il contenuto reale (ad es. “*l’immagine mostra una macchina da caffè anziché un documento*“). Si tratta di un comportamento che va oltre i controlli euristici talvolta osservati nei kit di phishing (basati su risoluzione, sfocatura o luminosità dell’immagine) e che indica l’impiego di un modello di visione artificiale con reali capacità di comprensione semantica del contenuto.

È tuttavia da notare come il medesimo sistema ha accettato senza obiezioni documenti evidentemente non validi, come, ad esempio, una carta d’identità fittizia, recante un’evidente filigrana “FACSIMILE”.

![](https://cert-agid.gov.it/wp-content/uploads/2026/08/Screenshot-from-2026-08-11-14-43-22.png)

*Dettaglio dello sfruttamento di un modello di IA per la verifica del file caricato*

L’adozione di un modello IA per la validazione dei documenti caricati non è casuale: scartando automaticamente i caricamenti manifestamente errati o casuali, il sistema riduce il “rumore” nella mole di dati raccolti dai criminali, rendendo più efficiente lo sfruttamento successivo delle informazioni sottratte. Allo stesso tempo, introduce nella vittima una percezione di rigore e serietà del processo (rinforzata anche dall’etichetta “Verifica AI in corso…” mostrata durante il caricamento), aumentando la probabilità che l’utente completi l’intera procedura fornendo materiale di qualità più alta e quindi più sfruttabile.

## Analisi tecnica del flusso di validazione

L’analisi delle risposte HTTP generate durante il caricamento mostra che l’endpoint `upload_ajax.php` utilizza un risultato strutturato riconducibile a una validazione semantica basata sui campi **ok** e **motivo**. Quando il file viene accettato, la risposta espone un oggetto ai contenente `{"ok":true,"motivo":""}`; in caso di rifiuto, invece, la motivazione prodotta dal sistema viene apparentemente trasferita nel campo pubblico **error**, accompagnata da `ai_rifiuto:true` e dal suffisso applicativo fisso “*Ricarica una foto più chiara e leggibile*“.

Ulteriori prove hanno dimostrato che il componente **legge non soltanto la scena rappresentata, ma anche il testo incorporato nell’immagine**. Quando tale testo conferma la decisione attesa, per esempio dichiarando che l’immagine raffigura un leone e deve essere rifiutata, e richiede di completare il campo motivo, il sistema può includere nella risposta anche le istruzioni presenti nel file.

![](https://cert-agid.gov.it/wp-content/uploads/2026/08/image-1024x788.png)

Il comportamento evidenzia quindi una **mancata separazione tra contenuto visivo non fidato e istruzioni di controllo**, rendendo il processo vulnerabile a istruzioni veicolate attraverso il canale OCR/visivo.

In questo caso il sistema si è auto identificato come **Gemini 1.5 PRO**.

## **Attività di contrasto**

Il CERT-AGID ha attivato le procedure di dismissione dei domini malevoli individuati e ha provveduto a informare l’Ente interessato. Gli **Indicatori di Compromissione** (IoC) relativi alla campagna sono stati diramati attraverso il [feed](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/) del CERT-AGID verso tutte le organizzazioni accreditate.

## Indicatori di Compromissione

Al fine di rendere pubblici i dettagl...