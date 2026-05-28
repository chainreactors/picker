---
title: iOS Foursquare Swarm - Digging Deeper New Artifacts Unearthed
url: https://djangofaiola.blogspot.com/2026/05/ios-foursquare-swarm-digging-deeper-new.html
source: Instapaper: Unread
date: 2026-05-27
fetch_date: 2026-05-28T06:03:56.500682
---

# iOS Foursquare Swarm - Digging Deeper New Artifacts Unearthed

[Skip to content](#mainnbt)

# [Appunti di Informatica Forense](https://djangofaiola.blogspot.com/)

## Digital Forensics and Incident Response Research

* [Home page](http://djangofaiola.blogspot.com/)
* [Downloads](https://djangofaiola.blogspot.com/p/downloads.html)

## lunedì 25 maggio 2026

Published maggio 25, 2026 by Django Faiola with [0 comment](https://djangofaiola.blogspot.com/2026/05/ios-foursquare-swarm-digging-deeper-new.html#comment-form)

# [iOS Foursquare Swarm - Digging Deeper: New Artifacts Unearthed](https://djangofaiola.blogspot.com/2026/05/ios-foursquare-swarm-digging-deeper-new.html)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjyFm1DLDbfYjVRpNnYXtquynTKGVnvoH0KH3liEigC7U_xzD6TOEHzQ44CzfxnMx6tgTjRdTZXVNWHqamhuZl9VZooHBSo-E3i-36WU4PFrRytw-iyQhR9yQIfYcbUhQtTJZbuhYdeuP-KFK-_lPptreXsi0qJn6kb8h02j7oTtzfpqN3Z0it_RWOIEP0/w640-h350/foursquare_swarm_title.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjyFm1DLDbfYjVRpNnYXtquynTKGVnvoH0KH3liEigC7U_xzD6TOEHzQ44CzfxnMx6tgTjRdTZXVNWHqamhuZl9VZooHBSo-E3i-36WU4PFrRytw-iyQhR9yQIfYcbUhQtTJZbuhYdeuP-KFK-_lPptreXsi0qJn6kb8h02j7oTtzfpqN3Z0it_RWOIEP0/s1408/foursquare_swarm_title.png)

### Indice dei contenuti

* [PINRemoteImage](#cache_images)
* [Account](#account)
* [Contatti](#contacts)
* [Rubrica](#address_book)
* [Check-in](#checkins)
* [Consigli (Tips)](#tips)
* [Adesivi (Stickers)](#stickers)
* [Cronologia delle venue](#venues_history)
* [Le foto](#photos)
* [Commenti](#all_comments)
* [Richieste di amicizia](#friend_requests)
* [Piani (Plans)](#plans)
* [Eventi (Events)](#events)
* [Bollettini (Feeds)](#feeds)
* [Liste Salvate](#saved_list)
* [Cronologia delle posizioni passive](#passive_loc_hist)
* [Pilgrim logs](#plog)
* [iLEAPP/LAVA](#iLEAPP)

### Introduzione

Nel precedente articolo è stata presentata una prima analisi di Swarm per iOS;
chi non avesse ancora letto il contenuto può consultare
[iOS Foursquare Swarm - Check-in App](https://djangofaiola-test.blogspot.com/2024/12/ios-foursquare-swarm-check-in-app.html). In occasione dell'adeguamento del codice al nuovo framework iLEAPP è emersa
l'opportunità di approfondire l'analisi degli artefatti di Swarm, migliorando
i dati esistenti e identificando nuovi artefatti.

Quelli di interesse risiedono principalmente nel database
/Library/Caches/foursquare.sqlite situato all'interno
dell'App Data Container (ADC):
/private/var/mobile/Containers/Data/Application/<UUID>/.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhllGCBAxLcGhGwRqALIDZbzvbhh7Ua3eK89pf7nNklkwNmJjuMCwfNLFDcCoV_NuoVjg5eJj8U9R0eGhcaYNwizOG5E7PRYbdTte_ZEd51GpNtah5f8Lnxd6webmchLMqMOpg1KlbwMHOmFmoq7TNBQflb-vpG-NPU63BC64sL8FQNlXZ75gfdWia5Bd0/w640-h149/sans_foursquare_swarm.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhllGCBAxLcGhGwRqALIDZbzvbhh7Ua3eK89pf7nNklkwNmJjuMCwfNLFDcCoV_NuoVjg5eJj8U9R0eGhcaYNwizOG5E7PRYbdTte_ZEd51GpNtah5f8Lnxd6webmchLMqMOpg1KlbwMHOmFmoq7TNBQflb-vpG-NPU63BC64sL8FQNlXZ75gfdWia5Bd0/s1200/sans_foursquare_swarm.png)

### PINRemoteImage

PINRemoteImage (disponibile su
[GitHub](https://github.com/pinterest/PINRemoteImage)) è una libreria open source che utilizza PINDiskCache per garantire una
persistenza su disco ottimizzata, finalizzata al recupero rapido, al
caricamento asincrono e alla gestione efficiente della memoria durante il
rendering di immagini scaricate da fonti remote.

All'interno del percorso:
<ADC>/Library/Caches/com.pinterest.PINDiskCache.PINRemoteImageManagerCache/
l’analisi ha evidenziato che la libreria non utilizza un database SQL per
l’indicizzazione, ma organizza i dati tramite un file system a oggetti. I file
salvati presentano nomi corrispondenti alla URL encoding degli indirizzi
sorgente originali.

L’ispezione della directory mostra una grande varietà di contenuti: immagini
dei check‑in, sticker, foto profilo degli utenti e altre risorse grafiche. La
presenza di formati differenti (come .jpg
e .png), spesso replicati in più
risoluzioni pre‑calcolate, conferma che l’applicazione sfrutta questa cache
per mantenere un set visivo completo e consultabile offline.

Nello specifico, la struttura dei percorsi codificati rivela le seguenti
convenzioni:

* %2Foriginal%2F: rappresenta l’immagine
  sorgente nel formato originale: /original/.
* %2FwidthW%2F: contiene la versione
  dell’immagine con larghezza specifica e aspect ratio invariato: es.
  /width576/;
* %2FWH%2F: versione ritagliata e centrata
  con larghezza e altezza identiche: es. /150/;
* %2FWxH%2F: come il precedente, ma con
  larghezza e altezza esplicitamente definite: es.
  /146x152/.

Esempio di file presente nella cache:
https%3A%2F%2Ffastly%2E4sqi%2Enet%2Fimg%2Fsticker%2F150%2Fpizza\_61927f%2Epng
Decodifica:
https://fastly.4sqi.net/img/sticker/150/pizza\_61927f.png

📌**Nota:** Nelle query illustrate a seguire, la ricostruzione dei percorsi delle immagini all'interno della cache viene effettuata solo con il valore original. Tuttavia, all'interno del modulo iLEAPP sono implementate le funzioni \_build\_photo\_map() e \_check\_in\_media\_with\_suffix(). Queste routine hanno lo scopo di mappare capillarmente tutti i file multimediali presenti e selezionare dinamicamente la risorsa disponibile alla miglior risoluzione (qualità massima).

### Account

Per la ricostruzione dell’account, come indicato nel poster, è sufficiente il
database SQLite <ADC>/Library/Caches/foursquare.sqlite, e in particolare la
tabella ZFSUSER. La query è stata
leggermente migliorata includendo anche la biografia dell’utente, il numero di amici e il
contatore delle mayorship.

I campi ZPHOTOPREFIX e
ZPHOTOSUFFIX  come descritto nella
sezione dedicata a [PINRemoteImage](#cache_images),
consentono inoltre la ricostruzione dell’immagine del profilo se presente nella
cache.

```
SELECT
  U.Z_PK AS "U_PK",
  FU.Z_PK AS "FU_PK",
  datetime(U.ZSWARMCREATEDAT + 978307200, 'unixepoch') AS "created",
  datetime(U.ZJOINEDAT + 978307200, 'unixepoch') AS "joined_at",
  U.ZFIRSTNAME,
  U.ZLASTNAME,
  U.ZBIO,
  U.ZGENDER,
  date(U.ZBIRTHDAY + 978307200, 'unixepoch') AS "birthday",
  U.ZHOMECITY,
  U.ZPHONE,
  U.ZEMAIL,
  FU.ZMONGOID AS "facebook",
  U.ZTWITTER,
  U.ZCANONICALURL,
  IIF(U.ZPHOTOPREFIX IS NOT NULL AND U.ZPHOTOSUFFIX IS NOT NULL,
    U.ZPHOTOPREFIX || 'original' || U.ZPHOTOSUFFIX, '') AS "orig_photo",
  U.ZCHECKINPINGS,
  coalesce(U.ZFRIENDSCOUNT, 0) AS "friends",
  coalesce(U.ZCHECKINSCOUNT, 0) AS "checkins",
  coalesce(U.ZMAYORSHIPSCOUNT, 0) AS "mayorship",
  U.ZMONGOID AS "uid"
FROM ZFSUSER AS "U"
LEFT JOIN ZFSFACEBOOKUSER AS "FU" ON (U.ZFACEBOOKUSER = FU.Z_PK)
WHERE U.ZRELATIONSHIP = 'self'
```

Esempio di record (U\_PK=3) con i nuovi campi:

* ZBIO:
  Consulente Informatico Forense - Digital Forensics Consultant
  (biografia).
* ZCHECKINPINGS:
  off (condivisione del vicinato:
  nearby=attivo,
  off=disattivato).
* ZFRIENDSCOUNT: 1 (numero di amici).
* ZMAYORSHIPSCOUNT: 0 (numero di mayorship attualmente possedute).

### Contatti

I contatti sono presenti nella tabella
ZFSUSER del database SQLite
<ADC>/Library/Caches/foursquare.sqlite. La query è stata aggiornata per rifinire la classificazione delle relazioni
utente e per integrare i contatori di attività e i flag di stato, garantendo
una visione più accurata e pulita della cerchia sociale rispetto alle
versione precedente.

```
SELECT
  U.Z_PK AS "U_PK",
  datetime(U.ZLASTMENTIONED + 978307200, 'unixepoch') AS "last_mentioned",
  CASE
    WHEN U.ZUSERTYPE IS NULL THEN 'N/A'
    WHEN U.ZUSERTYPE = '' THEN 'N/D'
    WHEN U.ZUSERTYPE = 'brand' Then 'Brand'
    WHEN U.ZUSERTYPE = 'celebrity' Then 'Celebrity'
    WHEN U.ZUSERTYPE = 'venuePage' Then 'Venue Page'
    WHEN U.ZUSERTYPE = 'page' Then 'Page'
    WHEN U.ZUSERTYPE = 'chain' Then 'Chain'
    ELSE UPPER(SUBSTR(U.ZUSERTYPE, 1, 1)) || SUBSTR(U.ZUSERTYPE, 2)
  END AS "user_type",
  CASE
    WHEN U.ZRELATIONSHIP IS NULL THEN 'N/A'
    ELSE
      CASE LOWER(U.ZRELATIONSHIP)
        WHEN 'self' THEN 'Self'
        WHEN 'friend' THEN 'Fri...