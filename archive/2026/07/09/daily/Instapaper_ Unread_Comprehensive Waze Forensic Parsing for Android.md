---
title: Comprehensive Waze Forensic Parsing for Android
url: https://djangofaiola.blogspot.com/2026/07/comprehensive-waze-forensic-parsing-for.html
source: Instapaper: Unread
date: 2026-07-09
fetch_date: 2026-07-10T06:00:03.893666
---

# Comprehensive Waze Forensic Parsing for Android

[Skip to content](#mainnbt)

# [Appunti di Informatica Forense](https://djangofaiola.blogspot.com/)

## Digital Forensics and Incident Response Research

* [Home page](http://djangofaiola.blogspot.com/)
* [Downloads](https://djangofaiola.blogspot.com/p/downloads.html)

## venerdì 3 luglio 2026

Published luglio 03, 2026 by Django Faiola with [0 comment](https://djangofaiola.blogspot.com/2026/07/comprehensive-waze-forensic-parsing-for.html#comment-form)

# [Comprehensive Waze Forensic Parsing for Android](https://djangofaiola.blogspot.com/2026/07/comprehensive-waze-forensic-parsing-for.html)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgO6EPyOkjPSQ6Tdc0YbuzNHI4i3mLQVfWafmxIVAOVMY5E8ODj8rUEmgEiLNR3kmzqyt832oUcwu5udzwEch4auNwb-ldAvCiVNT4JeTXmQTjaMlGk1YFAgq-I3GMsLZXU6wAzEUAazLLa4qpwKORTpnshiM_wuN4l7bWljqEvvKoOGa8O2QJVcHJyFes/w640-h350/waze_title.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgO6EPyOkjPSQ6Tdc0YbuzNHI4i3mLQVfWafmxIVAOVMY5E8ODj8rUEmgEiLNR3kmzqyt832oUcwu5udzwEch4auNwb-ldAvCiVNT4JeTXmQTjaMlGk1YFAgq-I3GMsLZXU6wAzEUAazLLa4qpwKORTpnshiM_wuN4l7bWljqEvvKoOGa8O2QJVcHJyFes/s1408/waze_title.png)

### Indice dei contenuti

* [Percorsi](#paths)
* [Track GPS Quality](#track_gps)
* [ALEAPP/LAVA](#ALEAPP)

### Introduzione

Dopo aver rilasciato e descritto il modulo di parsing per la versione iOS di Waze [Comprehensive Waze Forensic Parsing for iOS](https://djangofaiola.blogspot.com/2026/06/comprehensive-waze-forensic-parsing-for.html), ho completato lo sviluppo del parser specifico per la controparte Android, integrandolo nativamente all'interno del framework open-source [ALEAPP](https://github.com/abrignoni/ALEAPP) (Android Logs, Events, And Plists Parser) di [Alexis Brignoni](https://abrignoni.blogspot.com/).

Dal punto di vista investigativo, il valore probatorio, la tipologia di artefatti (cronologia ricerche, preferiti, eventi pianificati, navigazione text-to-speech, ecc.) e le logiche di normalizzazione e deduplicazione temporale ricalcano quanto già discusso per iOS. Anche i payload binari Protocol Buffers (cached\_data) mantengono la medesima organizzazione strutturale dei dati.

Per evitare inutili ripetizioni, questo articolo si concentra esclusivamente sulla mappatura dei percorsi Android e sulle specifiche modalità di gestione dei log diagnostici correnti e d'archivio implementate nello script waze.py.

Per una panoramica completa delle funzionalità dell’applicazione:
<https://www.waze.com/en/apps>

Google Play:
<https://play.google.com/store/apps/details?id=com.waze>

### Percorsi

Per semplicità, nel documento verrà utilizzata la seguente abbreviazione per indicare il percorso dei dati privati nell'archiviazione interna (Internal Storage) dell'applicazione:

**<IAP>**=/USERDATA/data/com.waze/    (**Internal App Path**)

Strutture di interesse forense:

| Path | File name | File type |
| --- | --- | --- |
| **<IAP>**/ | user.db | SQLite |
| **<**IAP**>**/ | user | Text (Key-Value) |
| **<**IAP**>**/ | session | Text (Key-Value) |
| **<**IAP**>**/ | waze\_log.txt | Log (Text) |
| **<**IAP**>**/ | spdlog.\*logdata | Log (Text) |
| **<**IAP**>**/ | \*\_\_spdlog.\*logdata.gz | Compressed Log (Text) |
| **<**IAP**>**/waze/ | cached\_data | Protobuf |
| **<**IAP**>**/waze/tts/ | tts.db | SQLite |

### Track GPS Quality

Una particolarità tecnica affrontata durante lo sviluppo riguarda la struttura e la varietà dei registri diagnostici dell'applicazione su Android. A differenza di quanto riscontrato su iOS, l'ambiente Android presenta elementi specifici sia per quanto riguarda i file correnti in chiaro, sia per la conservazione della memoria storica.

Nello specifico, sul piano corrente lo script estende l'analisi al file flat waze\_log.txt, un registro testuale non presente su iOS che coesiste insieme ai classici file .logdata. Sul piano storico, si evidenzia la presenza di file di log ruotati (riscontrati in analisi di release datate) che l'applicazione memorizza in formato compresso Gzip (\*\_\_spdlog.logdata.gz).

Per garantire che l'analista possa recuperare anche questi dati retrospettivi sulla telemetria e sulla qualità del segnale GPS senza dover estrarre e decomprimere manualmente i file dal dump, il modulo include il supporto nativo alla libreria gzip.

Il parser agisce identificando gli eventuali archivi storici compressi presenti nella directory ed eseguendo la decompressione on-the-fly direttamente in memoria, evitando così la scrittura di file temporanei sul disco di analisi. Infine, invia il flusso di testo decompresso alla stessa logica di parsing che elabora i log correnti (inclusi waze\_log.txt e i file .logdata), consolidando tutta la timeline temporale recuperabile in un unico flusso unificato e privo di ridondanze.

### ALEAPP/LAVA 💖

Lo script waze.py è ora pienamente integrato all'interno del progetto open-source [ALEAPP](https://github.com/abrignoni/ALEAPP) (Android Logs, Events, And Plists Parser) di [Alexis Brignoni](https://abrignoni.blogspot.com/).

L'interfaccia di [LAVA](https://www.leapps.org/) (LEAPP Artifact Viewer App) presenta i dati estratti in tabelle strutturate, facilitandone l'analisi e la consultazione. Di seguito sono riportati alcuni screenshot rappresentativi dei risultati ottenuti dal modulo su Android.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi9H4pg6RGC8TY89t_k0YmOwGJjyjSeI9Rh5xOn8hmJ_tTc5cjAUjkXf4rEfXjRbLqPwRvmN8tcjy54Az0erii9jldiqVS4dH9GA6y_FIO3LQirfsP9pNPsyoncH9gmLVUe-gzw_1fUWebUGsk4BkHjw_5Zu1nXEAocYJ0XNmFoUtF6EUGw6xongtdVoVU/w640-h346/waze_account_lava.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi9H4pg6RGC8TY89t_k0YmOwGJjyjSeI9Rh5xOn8hmJ_tTc5cjAUjkXf4rEfXjRbLqPwRvmN8tcjy54Az0erii9jldiqVS4dH9GA6y_FIO3LQirfsP9pNPsyoncH9gmLVUe-gzw_1fUWebUGsk4BkHjw_5Zu1nXEAocYJ0XNmFoUtF6EUGw6xongtdVoVU/s1920/waze_account_lava.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjZg6VTSGaAlWd6L06XDQ3N0LKzD9LmmFadV49wbohpxDcaqHfd9MCYtR6aPXxVwr0dE14zlGdjXb9NzZ83QFeQQvzyWX3Uz4a3KOLFfwUD10NaS3pTyHefdERLD2vUqGlqDqIRybLTYwBZVRQaiZEg-LR7S4Ks7xrSqUwDLGz1F0ViBcC10ls2jMYCF_s/w640-h346/waze_recents_lava.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjZg6VTSGaAlWd6L06XDQ3N0LKzD9LmmFadV49wbohpxDcaqHfd9MCYtR6aPXxVwr0dE14zlGdjXb9NzZ83QFeQQvzyWX3Uz4a3KOLFfwUD10NaS3pTyHefdERLD2vUqGlqDqIRybLTYwBZVRQaiZEg-LR7S4Ks7xrSqUwDLGz1F0ViBcC10ls2jMYCF_s/s1920/waze_recents_lava.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgZOixI19EgHkiYauuDTkuYS6l9efEjijzqG95I3INOHp2PhK2AB1_Y7J6fnTorXUreiv6LSdcjPJQ2y_uKR6of6Luvk51WWSiMP9PPmlFJ_EVnJxfBBUa50wRQgSfvgJcd9lZdaziZuAiARSKSHNArgi3jOITbcg_aclmhfkysxtytpS8v0BLHOWca3JU/w640-h346/waze_searched_lava.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgZOixI19EgHkiYauuDTkuYS6l9efEjijzqG95I3INOHp2PhK2AB1_Y7J6fnTorXUreiv6LSdcjPJQ2y_uKR6of6Luvk51WWSiMP9PPmlFJ_EVnJxfBBUa50wRQgSfvgJcd9lZdaziZuAiARSKSHNArgi3jOITbcg_aclmhfkysxtytpS8v0BLHOWca3JU/s1920/waze_searched_lava.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjMMZzAfRO85Hp3QY6J0L0tcWrW6LIQjom2AGQzIkWIDMjPewOOnHsqIa7a0N71FCwEllsysxRW967RxrX_UTgWP7kCUSJ8b0ouEEGyJ83MQu0sMwkDhg1fIDbEY5AX4yV-G6MyIPxAve8n710A-COWAR-dBR9BcZI5vj7UWqVFVSskJglT9jjYtWxrNWI/w640-h346/waze_session_lava.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjMMZzAfRO85Hp3QY6J0L0tcWrW6LIQjom2AGQzIkWIDMjPewOOnHsqIa7a0N71FCwEllsysxRW967RxrX_UTgWP7kCUSJ8b0ouEEGyJ83MQu0sMwkDhg1fIDbEY5AX4yV-G6MyIPxAve8n710A-COWAR-dBR9BcZI5vj7UWqVFVSskJglT9jjYtWxrNWI/s1920/waze_session_lava.png)

[Invia tramite email](https://www.blogger.com/share-post.g?blogID=837713476890397786&postID=5348423964542654545&target=email "Invia tramite email")[Postalo sul blog](https://www.blogger.com/share-post.g?blogID=837713476890397786&postID=5348423964542654545&target=blog "Postalo sul blog")[Condividi su X](https://www.blogger.com/share-post.g?blogID=837713476890397786&postID=5348423964542654545&target=twitter "Condividi su X")[Condividi su Fac...