---
title: Deep‑Dive Forense in Box per iOS
url: https://djangofaiola.blogspot.com/2026/03/deepdive-forense-in-box-per-ios.html
source: Instapaper: Unread
date: 2026-03-12
fetch_date: 2026-03-13T04:07:59.296765
---

# Deep‑Dive Forense in Box per iOS

[Skip to content](#mainnbt)

# [Appunti di Informatica Forense](https://djangofaiola.blogspot.com/)

## Digital Forensics and Incident Response Research

* [Home page](http://djangofaiola.blogspot.com/)
* [Downloads](https://djangofaiola.blogspot.com/p/downloads.html)

## martedì 10 marzo 2026

Published marzo 10, 2026 by Django Faiola with [0 comment](https://djangofaiola.blogspot.com/2026/03/deepdive-forense-in-box-per-ios.html#comment-form)

# [Deep‑Dive Forense in Box per iOS](https://djangofaiola.blogspot.com/2026/03/deepdive-forense-in-box-per-ios.html)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEilBA1co0_l-ReMC7YWMbz81p2wdMF95Bx1WS6QNSnnj6KP0QYbkifHzndWehs4Im4PBa4o1pknOW7RRHgmWUKriNPrdDHTROAapiwi7fn3O1WdQuYD9pRltpes2pjmjvaKyK3JXDOnwFn8PjYu9d194QTgWz8hQs4X7a2m7hb6lHHZUtrKk6ueSQa2WTs/s1600/box_icon.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEilBA1co0_l-ReMC7YWMbz81p2wdMF95Bx1WS6QNSnnj6KP0QYbkifHzndWehs4Im4PBa4o1pknOW7RRHgmWUKriNPrdDHTROAapiwi7fn3O1WdQuYD9pRltpes2pjmjvaKyK3JXDOnwFn8PjYu9d194QTgWz8hQs4X7a2m7hb6lHHZUtrKk6ueSQa2WTs/s200/box_icon.png)

### Indice dei contenuti

* [Percorsi](#paths)
* [Profilo utente](#account)
* [Tutti i file](#allfiles)
* [Elementi marcati offline](#offline)
* [Raccolte e preferiti](#collections)
* [Commenti e annotazioni](#fileactivity)
* [Anteprime e originali](#previews)
* [Recenti](#recents)
* [iLEAPP](#iLEAPP)

### Introduzione

**Box** per iOS è un'applicazione gratuita
sviluppata da [Box, Inc.](https://www.box.com),
azienda statunitense specializzata in soluzioni di cloud content management e collaborazione aziendale. L’app consente di accedere, archiviare, condividere e gestire file direttamente da dispositivi iPhone e iPad, integrandosi con numerosi servizi di produttività e garantendo elevati standard di sicurezza e protezione dei dati.

Per una panoramica completa delle funzionalità dell’applicazione:
<https://www.box.com>

App Store:
<https://apps.apple.com/it/app/box-the-power-of-content-ai/id290853822>

Per lo studio di questa applicazione è stata adottata una metodologia comparativa, esaminando i dati provenienti da due scenari differenti: un'estrazione fisica di un iPhone 8 (iOS 16.7.12) con Box v5.34.1 e un backup iTunes cifrato di un iPhone SE (2nd gen) (iOS 18.5) con installata la versione più recente di Box (v5.54.0).

### Percorsi

Per semplicità, nel documento verranno utilizzate le seguenti abbreviazioni:

**<ADC>**=/private/var/mobile/Containers/Data/Application/<UUID>/

**<AGC>**=/private/var/mobile/Containers/Shared/AppGroup/<UUID>/

Strutture di interesse forense:

| Path | File name | File type |
| --- | --- | --- |
| **<AGC>**/Library/Preferences/ | group.net.box.BoxNet.plist | Plist |
| **<AGC>**/Documents/db/ | Item.db | SQLite |
| **<AGC>**/File Provider Storage/boxpreview/<userID>/db/ | PreviewItem.db | SQLite |
| **<AGC>**/Documents/offlinefilesinfo/ | itemIDs.plist | Plist |
| **<AGC>**/Documents/offlinefilesinfo/ | lastDownloadDates.plist | Plist |
| **<AGC>**/File Provider Storage/boxpreview/<userID>/cache/files/<fileID>/ | \* | Various |

### Profilo utente

La configurazione dell’account è memorizzata nel file di
preferenze group.net.box.BoxNet.plist, situato nel percorso **<AGC>**/Library/Preferences/. All’interno del Plist è presente il dizionario lastUserJSON che contiene i metadati relativi all’ultimo utente autenticato sull’applicazione.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgnhJg2YI16hDcPwqQ7SZpNK_Z8VkDinsWJQ4IAGU_4WrxTDeq7o6ipxw0ZnbnuVNcCuq8q81tvSUEpJQfIYyhoO2CHc3W3l19-3p7aQtTZjFWQUh69hcUViPny38ebnmRloUa9HLzTzhbiqvWxgxRpc5TVoJ49xxsVYtNlAjoyf35JHwVVrwefhn3xpyA/w640-h380/box_account_plist.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgnhJg2YI16hDcPwqQ7SZpNK_Z8VkDinsWJQ4IAGU_4WrxTDeq7o6ipxw0ZnbnuVNcCuq8q81tvSUEpJQfIYyhoO2CHc3W3l19-3p7aQtTZjFWQUh69hcUViPny38ebnmRloUa9HLzTzhbiqvWxgxRpc5TVoJ49xxsVYtNlAjoyf35JHwVVrwefhn3xpyA/s1026/box_account_plist.png)

Per la visualizzazione del file è stato utilizzato dfDataViewer, il mio strumento (ancora in fase di sviluppo) per l'ispezione di formati strutturati quali Plist/BPlist, JSON/JSONB, XML/BXML, ASN.1, Protobuf e LevelDB.

Le proprietà più rilevanti presenti in lastUserJSON sono:

* created\_at: 2024-09-29T05:55:27-07:00 - data di creazione dell’account in ISO 8601 con fuso orario (29 settembre 2024 12:55:27).
* login: dj\*\*\*@\*\*\*.it - indirizzo email dell’utente.
* name: dj\*\*\*@\*\*\*.it - nome visualizzato.
* has\_custom\_avatar: False - indica se l’utente ha impostato un avatar personalizzato.
* enterprise: null - tipo di account (null per account gratuito; { id: "11446498", type: "enterprise", name: "Acme Inc." }).
* id: 36844\*\*\* - identificatore univoco dell’utente.
* timezone: America/Los\_Angeles - fuso orario dell’account.
* language: it - codice della lingua (ISO 639‑1).
* max\_upload\_size: 262144000 - dimensione massima dei file caricabili in byte (262.14 MB).
* space\_amount: 10737418240 - quota totale in byte (10.74 GB).
* space\_used: 4268002649 - spazio usato in byte (4.27 GB).

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhKLXCDEeB6HW_n8uN7UNjLmoMvTzHrIidzlVjaRBrmFx6IPEISKu2cZ-bPxCTVccSRivwtmklMIe8gIJvsWaYUqi-ZgfxtvfTnKO7hDfZFGH267_AFE7ir1cDm3XQbTw2w2fyV9K2U3xhcELDodurfUm94CKl2xoCcWYH5iCoaurLtuVa-QrI3uxoLD3s/w400-h356/box_account_phone.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhKLXCDEeB6HW_n8uN7UNjLmoMvTzHrIidzlVjaRBrmFx6IPEISKu2cZ-bPxCTVccSRivwtmklMIe8gIJvsWaYUqi-ZgfxtvfTnKO7hDfZFGH267_AFE7ir1cDm3XQbTw2w2fyV9K2U3xhcELDodurfUm94CKl2xoCcWYH5iCoaurLtuVa-QrI3uxoLD3s/s1500/box_account_phone.png)

### Tutti i file

Il database SQLite Item.db, situato nel percorso **<AGC>**/Documents/db/, rappresenta l'archivio principale attraverso cui l’app Box gestisce la totalità degli elementi presenti nel cloud dell’utente. Al suo interno sono conservati i riferimenti a file e cartelle, la struttura logica che li collega e l’insieme dei metadati necessari alla sincronizzazione e alla rappresentazione dei contenuti.

L’interfaccia dell’applicazione mostra i file in una struttura ad albero, ma il database adotta un modello di archiviazione completamente flat. Ogni elemento è descritto da un record autonomo nella tabella items, mentre la gerarchia viene ricostruita tramite campi relazionali come parentID.

La figura seguente mostra la rappresentazione del campo jsonData relativo all’elemento Django.mp4, utile per comprendere la struttura interna con cui Box serializza i metadati dei singoli file.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjh5mcvITh3QemS2wIfGT4g5D3n2nO1cgufQvZ6bzKX82cyhxZPpYtsavDtaMdXrsOz7pG38rgJ2uHjx6fGEoWvQNgFvipcD3apFC3hhrtar88cB2GD_IXsthWtSEvmmZP4RM3FPXrdMVQ_XNamNnYeU0Qmac7orLsiiLZycotkgROn-mthBL7R2CILXs4/w640-h380/box_allfiles_jsondata.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjh5mcvITh3QemS2wIfGT4g5D3n2nO1cgufQvZ6bzKX82cyhxZPpYtsavDtaMdXrsOz7pG38rgJ2uHjx6fGEoWvQNgFvipcD3apFC3hhrtar88cB2GD_IXsthWtSEvmmZP4RM3FPXrdMVQ_XNamNnYeU0Qmac7orLsiiLZycotkgROn-mthBL7R2CILXs4/s1026/box_allfiles_jsondata.png)

I campi chiave di interesse sono:

* modelID: 1659897439061 - identificatore univoco dell’elemento (chiave primaria).
* type:
  file - tipo di elemento (file
  o folder).
* name:
  Django.mp4 - nome del file o della
  cartella.
* parentID:
  286956667057 - identificatore della
  cartella genitore, modelID.
* lastNetworkFetchedTimestamp:
  1767015862.94753 - data e ora
  dell’ultima sincronizzazione con il server in Unix Epoch (29 dicembre 2025 13:44:22).
* jsonData: struttura complessa in
  formato JSON utilizzata per incapsulare i metadati estesi.

All’interno di jsonData sono
presenti ulteriori informazioni rilevanti quali:

* created\_at:
  2024-09-29T22:05:44-07:00 - data e ora
  di creazione su Box in ISO 8601 con fuso orario (30 settembre 2024 05:05:44).
* modified\_at:
  2024-09-29T22:05:44-07:00 - data e ora
  dell’ultima modifica ...