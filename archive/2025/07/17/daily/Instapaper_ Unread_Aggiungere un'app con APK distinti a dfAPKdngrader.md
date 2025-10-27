---
title: Aggiungere un'app con APK distinti a dfAPKdngrader
url: https://djangofaiola.blogspot.com/2025/07/aggiungere-unapp-con-apk-distinti.html
source: Instapaper: Unread
date: 2025-07-17
fetch_date: 2025-10-06T23:56:29.209352
---

# Aggiungere un'app con APK distinti a dfAPKdngrader

[Skip to content](#mainnbt)

# [Appunti di Informatica Forense](https://djangofaiola.blogspot.com/)

## Digital Forensics and Incident Response Research

* [Home page](http://djangofaiola.blogspot.com/)
* [Downloads](https://djangofaiola.blogspot.com/p/downloads.html)

## martedì 15 luglio 2025

Published luglio 15, 2025 by Django Faiola with [0 comment](https://djangofaiola.blogspot.com/2025/07/aggiungere-unapp-con-apk-distinti.html#comment-form)

# [Aggiungere un'app con APK distinti a dfAPKdngrader](https://djangofaiola.blogspot.com/2025/07/aggiungere-unapp-con-apk-distinti.html)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhxlahdOLswKkKwxmn2K78DzoaiFWIV2SKzHDdjqwla0QHs4gBbRcrWX7aoOkqEeO_5qEpvnVE37tKRU8pvZsA3GwcCo87imdj-vXL52WpkLwy5m6FSnu8Y5h5OXxW0ezhr1vGrUpu6h1B4nxAHUlAccZCjonJzwVnCL3vqEJLJtLUd4khr3wdIfaFp2KQ/s1600/APKdngrader-128.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhxlahdOLswKkKwxmn2K78DzoaiFWIV2SKzHDdjqwla0QHs4gBbRcrWX7aoOkqEeO_5qEpvnVE37tKRU8pvZsA3GwcCo87imdj-vXL52WpkLwy5m6FSnu8Y5h5OXxW0ezhr1vGrUpu6h1B4nxAHUlAccZCjonJzwVnCL3vqEJLJtLUd4khr3wdIfaFp2KQ/s128/APKdngrader-128.png)

### Introduzione

Nel precedente articolo [Aggiungere un'app a dfAPKdngrader](https://djangofaiola.blogspot.com/2023/08/aggiungere-unapp-dfapkdngrader.html), è stata descritta la procedura per integrare un'app personalizzata non inclusa nell'elenco predefinito dei package del software. In questo nuovo articolo, invece, viene approfondito il metodo per aggiungere un'app che non incorpora il supporto multi-architettura all'interno del medesimo package, condizione che richiede una gestione separata dei file APK.

Esistono applicazioni, dove il package APK è distribuito per una specifica architettura, ad esempio ARMv7. Per installare l'app su un dispositivo con architettura a 32 bit Intel (x86) o MIPS32, è necessario scaricare l'APK compatibile con tali architetture.

Nel precedente articolo, non l'ho scritto, ma [dfAPKdngrader](https://djangofaiola.blogspot.com/2023/08/dfapkdngrader.html) supporta anche questa modalità, in quanto l'identificazione dell'app non è basata principalmente sul nome del package come per molti altri software (ad es. packageName=com.whatsapp).

Su diversi dispositivi con sistema Android 10 o versione successive, è possibile che sia abilitata esclusivamente l'esecuzione di codice a 64 bit; in questi casi il supporto a 32 bit è stato rimosso rendendo impossibile il downgrade dell'app con le vecchie architetture come ARMv7. Di conseguenza, avere entrambi i package è fondamentale, soprattutto per garantire la compatibilità con i dispositivi più moderni.

Per comprendere meglio quanto è stato detto, di seguito viene mostrato come personalizzare l'app del lettore multimediale [Lark Player](https://play.google.com/store/apps/details?id=com.dywx.larkplayer&hl=en-US).

### Lark Player

Questa applicazione rappresenta un caso d'uso, in quanto presenta APK distinti per ciascuna architettura supportata. Prima di procedere alla descrizione della configurazione, di seguito sono riportati i due blocchi (oggetti) del file apk.json relativi ai package per l'architettura ARMv7 (ABI armeabi-v7a) e ARMv8-A (ABI arm64-v8a).

**file di configurazione apk.json:**

> {
>     "baseName": "com.dywx.larkplayer-v7a",
>     "packageName": "com.dywx.larkplayer",
>     "marketName": "Lark Player",
>     "category": "Music & Audio",
>     "versionCode": 22230104,
>     "versionName": "2.23.1",
>     "minSdk": 17,
>     "abiList": "armeabi-v7a",
>     "url": "1El6zoZD23k\_Fbhaw5LAgIkmN\_8aBbS7o",
>     "md5": "7c6650d968bbb229d1d9890261ec45e2"
> },
> {
>     "baseName": "com.dywx.larkplayer-v8a",
>     "packageName": "com.dywx.larkplayer",
>     "marketName": "Lark Player",
>     "category": "Music & Audio",
>     "versionCode": 22230107,
>     "versionName": "2.23.1",
>     "minSdk": 17,
>     "abiList": "arm64-v8a",
>     "url": "1JS1NnHI3G8oKNL4vFn-L8KFGrAlam8Yq",
>     "md5": "fb8c2d9235da0cac4515716b1b25f981"
> }

La versione dell'app (versionName) è la stessa per entrambe le configurazioni, almeno in questo caso, la 2.23.1. Tuttavia, è possibile definire versioni distinte, limitatamente a una per ciascuna tipologia di architettura.

La chiave baseName rappresenta l'identificatore univoco dei pacchetti. In assenza di un valore esplicito, o se lasciato vuoto, è associato al valore della chiave packageName per l'identificazione dell'applicazione. In tutte le configurazioni presenti nel file apk.json, non è mai stata utilizzata. Tutti gli APK  forniti sono prevalentemente multi-architettura come indicato dai valori definiti nella chiave abiList.

Per discriminare le due architetture della stessa app, sono stati definiti altrettanti identificatori (baseName): com.dywx.larkplayer-v7 per la l'architettura ARMv7 e com.dywx.larkplayer-v8 per l'architettura ARMv8-A. I due identificatori sono generici e devono essere ovviamente univoci. In questa configurazione è stata utilizzata la notazione "packageName-val". Per una Intel a 32 bit, ad esempio, com.dywx.larkplayer-i32 o com.dywx.larkplayer-x86.

Per questa app, nonostante versionName è 2.23.1 per entrambe le configurazioni, il versionCode è diverso: 22230104 e 22230107. Quindi fate molta attenzione a scrivere i valori appropriati.

Uno screenshot di questa nuova configurazione:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjRFm3fdVvUZrWxJxrs3jBDlOFGT-j-Jn2OhXZ6hxxd_dgzBKdq8a0N68LSpa6xcCcNYA6L_jf20VDYIdXUqaZzNsHFXQnefWekDW9G2iGh7UEfGuHEKrUj1Ses3fcolc2ESonb6e55dnKoos5mpKbbCWTWdrT_3Po8lVeIu9NWxn49Fc8HVRUSCTZUrCQ/w640-h396/dfAPKdngrader-multi-arch.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjRFm3fdVvUZrWxJxrs3jBDlOFGT-j-Jn2OhXZ6hxxd_dgzBKdq8a0N68LSpa6xcCcNYA6L_jf20VDYIdXUqaZzNsHFXQnefWekDW9G2iGh7UEfGuHEKrUj1Ses3fcolc2ESonb6e55dnKoos5mpKbbCWTWdrT_3Po8lVeIu9NWxn49Fc8HVRUSCTZUrCQ/s1026/dfAPKdngrader-multi-arch.png)

Volendo, è possibile assegnare a marketName un nome che consenta di capire a colpo d'occhio a quale versione è associato; ad esempio, Lark Player arm64-v8a o qualsivoglia altra denominazione.

**ATTENZIONE**: Non è stato ancora verificato, ma può accadere che un'app progettata per versioni di Android precedenti alla 10 o compatibile con istruzioni a 32 bit mostri, tra i pacchetti candidati al downgrade, entrambe le versioni. In tal caso, è consigliabile selezionare quella nativa anziché quella retrocompatibile.

In occasione di questo piccolo articolo, ho deciso di pubblicare anche la lista delle nuove app supportate.

Lo ripeto volentieri: se avete realizzato dei package di app non ancora presenti nell'elenco, contattatemi e li renderò disponibili a tutti!😄.

### Ultima versione

[Windows](http://bit.ly/3DJOdiH) | [Linux](http://bit.ly/44T3jyj)

Il software è proprietario (Freeware - closed source) e per l'uso commerciale considera una piccola donazione valida come autorizzazione implicita al suo utilizzo.

### Elenco delle nuove app supportate

1. NumBuster!
2. LovePlanet
3. Swiggy
4. PayByPhone
5. Domino's Pizza France
6. Yemeksepeti
7. Pull&Bear
8. MyPertamina
9. Pluto TV
10. Bolt Driver (Taxify Driver)
11. Yubo (Yellow)
12. WEBTOON
13. Mrsool
14. Hollister
15. Veepee
16. Orbitz
17. Trafi
18. Muzz (muzmatch)
19. 1km
20. Shopee
21. Wego
22. Fever
23. OpenTable
24. Wattpad
25. Tagged
26. Cloud (Cloud Mail.Ru)
27. willhaben
28. OfferUp
29. Beyond Menu
30. Microsoft Outlook
31. Lark Player

[Invia tramite email](https://www.blogger.com/share-post.g?blogID=837713476890397786&postID=2224354981957760553&target=email "Invia tramite email")[Postalo sul blog](https://www.blogger.com/share-post.g?blogID=837713476890397786&postID=2224354981957760553&target=blog "Postalo sul blog")[Condividi su X](https://www.blogger.com/share-post.g?blogID=837713476890397786&postID=2224354981957760553&target=twitter "Condividi su X")[Condividi su Facebook](https://www.blogger.com/share-post.g?blogID=837713476890397786&postID=2224354981957760553&target=facebook "Cond...