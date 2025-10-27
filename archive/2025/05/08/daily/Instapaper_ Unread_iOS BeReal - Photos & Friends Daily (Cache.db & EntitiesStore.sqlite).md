---
title: iOS BeReal - Photos & Friends Daily (Cache.db & EntitiesStore.sqlite)
url: https://djangofaiola.blogspot.com/2025/05/ios-bereal-photos-friends-daily-cachedb.html
source: Instapaper: Unread
date: 2025-05-08
fetch_date: 2025-10-06T22:39:06.745574
---

# iOS BeReal - Photos & Friends Daily (Cache.db & EntitiesStore.sqlite)

[Skip to content](#mainnbt)

# [Appunti di Informatica Forense](https://djangofaiola.blogspot.com/)

## Digital Forensics and Incident Response Research

* [Home page](http://djangofaiola.blogspot.com/)
* [Downloads](https://djangofaiola.blogspot.com/p/downloads.html)

## sabato 3 maggio 2025

Published maggio 03, 2025 by Django Faiola with [0 comment](https://djangofaiola.blogspot.com/2025/05/ios-bereal-photos-friends-daily-cachedb.html#comment-form)

# [iOS BeReal - Photos & Friends Daily (Cache.db & EntitiesStore.sqlite)](https://djangofaiola.blogspot.com/2025/05/ios-bereal-photos-friends-daily-cachedb.html)

### [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjvnUsECkFqsSwt9kJczyEYuaRaSc7WlbGaWAkZnmbAafPqR9j0YeZJZM7AEHLlSRKLLUeWldRQhVW1LRtvSfk2ylYfenq-I-SY17TEfm-Lz7CAjSsxsjVABWrDMPmuIOpoXgs_WKmX9vQzIM_PE4nFSHdsg3an5cM5d722ATp1vYo9SmTkWQwTzDhSYAQ/s1600/bereal_icon.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjvnUsECkFqsSwt9kJczyEYuaRaSc7WlbGaWAkZnmbAafPqR9j0YeZJZM7AEHLlSRKLLUeWldRQhVW1LRtvSfk2ylYfenq-I-SY17TEfm-Lz7CAjSsxsjVABWrDMPmuIOpoXgs_WKmX9vQzIM_PE4nFSHdsg3an5cM5d722ATp1vYo9SmTkWQwTzDhSYAQ/s217/bereal_icon.png)

### Indice dei contenuti

* [Cache.db](#cache_db)
* [Account](#account)
* [Persone](#persons)
* [I miei Amici](#friends)
* [Richieste di amicizia](#friend_requests)
* [Utenti bloccati](#blocked_list)
* [Le tue Memorie](#memories)
* [BeReal appuntati](#pinned_memories)
* [Commenti sui BeReal](#memories_comments)
* [RealMojis](#realmojis)
* [EntitiesStore.sqlite](#entities_store_sqlite)

+ [Account](#entities_store_sqlite_account)
+ [Amici](#entities_store_sqlite_friends)
+ [Post](#entities_store_sqlite_posts)
+ [Commenti](#entities_store_sqlite_comments)
+ [RealMojis](#entities_store_sqlite_realmojis)

* [Da fare](#todo)
* [iLEAPP](#iLEAPP)

### Introduzione

Questo secondo articolo è un approfondimento dell'analisi di BeReal
focalizzato principalmente sul database SQLite Cache.db presente nell'Internal App Path "/Library/Caches/AlexisBarreyat.BeReal/", la cache.

Durante l'analisi condotta nel precedente articolo [iOS BeReal - Photos & Friends Daily](https://djangofaiola.blogspot.com/2025/03/ios-bereal-photos-friends-daily.html), ho postato diversi BeReal mentre ascoltavo la musica con Spotify per
ricostruire l'object music del JSON, ma non ho trovato alcun riferimento
negli stessi mentre nelle risposte alle richieste API nel database
Cache.db sono presenti.

Un nuovo "attore è entrato in scena", il database
EntitiesStore.sqlite presente
nell'Internal App Group Path "/" del contenitore di gruppo  condiviso "**/private/var/mobile/Containers/Shared/AppGroup/<APP\_GUID>**". In realtà questo database SQLite era già presente da qualche versione, ma
non popolato e in continuo aggiornamento. Una nuova banca dati ricca di
informazioni: utenti, post, commenti, realmoji etc.

BeReal è un social network francese lanciato nel 2020 da Alexis Berreyat
e Kevin Per maggiori dettagli sulle funzionalità dell'app
consulta <https://bereal.com>.

App Store: <https://apps.apple.com/us/app/bereal-photos-friends-daily/id1459645446>

Per lo studio di questa app sono state utilizzate le versioni 4.0.0 (Dec 18, 2024) e successive fino alla 4.18.0 (Apr 14,
2025) del mio iPhone 8 iOS 16.7.10 test e quelle delle immagine pubbliche
di [Josh Hickman](https://thebinaryhick.blog/) iOS 17.3, 16.1.2 e 15.3.1 con le rispettive versioni 2.24.0, 1.21.4 e 1.1.0.

### Percorsi

Di seguito lo stralcio di BeReal del poster della SANS “[iOS Third-Party Apps Forensics Reference Guide Poster](https://sansorg.egnyte.com/dl/UmmCriT4sU)” con le informazioni più rilevanti per l’analisi dell’app.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjVcBGzFORkHwbcbvvbAZNOgB3uV4S1eP6pB9iXasuAlxghKVIf7Nb8BGAsM-gIaR_-Qw7R-AUFkdx3g_EjwjpHAqckdKQKU-qPpe4Rqyz20pfWGebSI2SdT7H-_84EMvR0sfD8959b9erL8FMVI79NUu71E63t-iDld9PfFvtxTEeB-lRjZKQlk_C2PsI/w640-h240/bereal_sans.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjVcBGzFORkHwbcbvvbAZNOgB3uV4S1eP6pB9iXasuAlxghKVIf7Nb8BGAsM-gIaR_-Qw7R-AUFkdx3g_EjwjpHAqckdKQKU-qPpe4Rqyz20pfWGebSI2SdT7H-_84EMvR0sfD8959b9erL8FMVI79NUu71E63t-iDld9PfFvtxTEeB-lRjZKQlk_C2PsI/s1200/bereal_sans.png)

### Cache.db

Una breve introduzione sul database
Cache.db prima di iniziare l'analisi
serve a chiarire i concetti che seguiranno. Questo database SQLite tiene
traccia dei dati che l'app ha ricevuto da fonti esterne come un server o
internet, una cache per velocizzare il caricamento se necessario. Due sono le
tabelle principali di interesse:

* cfurl\_cache\_response: contiene i dati
  e l'ora della richiesta;
* cfurl\_cache\_receiver\_data: contiene i
  dati ricevuti dal server in risposta alla richiesta al server tramite la
  tabella cfurl\_cache\_response.

Mettere in relazione queste tabelle è importante in quanto può fornire
informazioni che non sono memorizzate altrove; ad esempio come detto
precedentemente, i brani musicali ascoltati durante la pubblicazione del
BeReal. Se la dimensione dei dati è di 4096 byte o superiore sono
 memorizzati su file (cfurl\_cache\_response.isDataOnFs=1) con il nome dell'UUID assegnato al campo
cfurl\_cache\_receiver\_data.receiver\_data, altrimenti sono memorizzati nel database (cfurl\_cache\_response.isDataOnFs=0) come BLOB.

Per prima cosa bisogna ricostruire le relazioni delle tabelle di questo
database SQLite:

> SELECT
>   cr.request\_key AS "URL",
>
> datetime(strftime("%s", cr.time\_stamp), 'unixepoch') AS "timestamp",
>
> crd.isDataOnFS,
>   crd.receiver\_data AS "data"
> FROM
> cfurl\_cache\_response AS "cr"
> LEFT JOIN cfurl\_cache\_receiver\_data AS
> "crd" ON (cr.entry\_ID = crd.entry\_ID)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjDSjt_uArKvLcCCvLV3zBRvKohw7V_aHdjuKwBUxuMvUoggMiJNj3MPl8T8M1FXxki0BHtbSzK28ebwvYFEMFI6uo2ux36oroizi6MJI4VDDGity5wY47IF7eCUq11z1Wt9-NdchfwVuvXqqqjPMwguS98eLHbZtA1M0XC1FSKb_y8ssbPrTvvCiIrOkQ/w640-h338/bereal_cache_db.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjDSjt_uArKvLcCCvLV3zBRvKohw7V_aHdjuKwBUxuMvUoggMiJNj3MPl8T8M1FXxki0BHtbSzK28ebwvYFEMFI6uo2ux36oroizi6MJI4VDDGity5wY47IF7eCUq11z1Wt9-NdchfwVuvXqqqjPMwguS98eLHbZtA1M0XC1FSKb_y8ssbPrTvvCiIrOkQ/s1599/bereal_cache_db.png)

Non entro nel dettaglio delle tabelle, quello che maggiormente interessa sono
i campi:

* cfurl\_cache\_response.request\_key
  (URL): è la stringa di richiesta al server;
* cfurl\_cache\_receiver\_data.isDataOnFS
  (isDataOnFS): indica che i dati sono
  1=esterni su file,
  0=incorporati nel campo data;
* cfurl\_cache\_receiver\_data.receiver\_data
  (data): contiene i dati ricevuti o il nome del file presente nella
  sottocartella "fsCachedData".

### Account

L'API di richiesta del profilo: https://mobile-l7.bereal.com/api/person/me

> SELECT
>     crd.entry\_ID,
>     cr.request\_key AS "URL",
>     crd.isDataOnFS,
>     crd.receiver\_data
> FROM cfurl\_cache\_response AS "cr"
> LEFT JOIN cfurl\_cache\_receiver\_data AS "crd" ON (cr.entry\_ID = crd.entry\_ID)
> WHERE cr.request\_key REGEXP "https:\/\/mobile[-\w]\*\.bereal\.com\/api\/person\/me$"

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhhDQvhHtbk6g4Y9algV6J5J2gJWSn_fXdej7DlKdEDEZJ3M7Hin9dkMDs5zuek6412ySVZTNNaARlYmjO7dRQ3wSllxFS6ozmsIBjdM7eiRax_ssE63aN6mkdQuwhposA3Rnv0BbkvOqwKGbZEB5MaqXpWSE08tfxuQZLUX_7xDH_ILGjxgwhI4Q6Z70M/w640-h78/bereal_account_db.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhhDQvhHtbk6g4Y9algV6J5J2gJWSn_fXdej7DlKdEDEZJ3M7Hin9dkMDs5zuek6412ySVZTNNaARlYmjO7dRQ3wSllxFS6ozmsIBjdM7eiRax_ssE63aN6mkdQuwhposA3Rnv0BbkvOqwKGbZEB5MaqXpWSE08tfxuQZLUX_7xDH_ILGjxgwhI4Q6Z70M/s1599/bereal_account_db.png)

La risposta in JSON:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgv0Hu-Gfe1gSVmpBn0yVMmhLXpz7Gcu5QE5muFVH-iEScwQwgv6lQ_Dl0cXV0R0dWvM3rl0P-HevZ-JslA478GTyIeUIOxCHyA1zWggUMy2EJ_OyrlJ8Odr2ZGVFqHH5uS2Qgnzr7IbBlW5W4dLxKSO0fWJ0DYbicjcDyekEvTUFSeFkWTbNprNmxp5CQ/w640-h372/bereal_account_cache_json.png)](http...