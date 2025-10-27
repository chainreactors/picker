---
title: Happy 3rd Birthday to dfAPKdngrader
url: https://djangofaiola.blogspot.com/2024/10/happy-3rd-birthday-to-dfapkdngrader.html
source: Instapaper: Unread
date: 2024-10-29
fetch_date: 2025-10-06T18:55:50.066515
---

# Happy 3rd Birthday to dfAPKdngrader

[Skip to content](#mainnbt)

# [Appunti di Informatica Forense](https://djangofaiola.blogspot.com/)

## Digital Forensics and Incident Response Research

* [Home page](http://djangofaiola.blogspot.com/)
* [Downloads](https://djangofaiola.blogspot.com/p/downloads.html)

## sabato 26 ottobre 2024

Published ottobre 26, 2024 by Django Faiola with [3 comments](https://djangofaiola.blogspot.com/2024/10/happy-3rd-birthday-to-dfapkdngrader.html#comment-form)

# [Happy 3rd Birthday to dfAPKdngrader](https://djangofaiola.blogspot.com/2024/10/happy-3rd-birthday-to-dfapkdngrader.html)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjPoUjJpIFvi0FgTCJI_XjzU4vpCkR_iciQQP9ky9ew6O-uf-KgTb4J-5TA5SjIame68DsQSmdpikf7QW0Tt5QqsqPHoThRqgGCXYWxR7nwQblKjlKICLGgjGB2YiU4gfMEA3Ju0D_clvNfoS2JnynragYXdQtKTweJpeJG0SHY0rmsSzQMPIILbzN_0zo/s320/happy-third-birthday.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjPoUjJpIFvi0FgTCJI_XjzU4vpCkR_iciQQP9ky9ew6O-uf-KgTb4J-5TA5SjIame68DsQSmdpikf7QW0Tt5QqsqPHoThRqgGCXYWxR7nwQblKjlKICLGgjGB2YiU4gfMEA3Ju0D_clvNfoS2JnynragYXdQtKTweJpeJG0SHY0rmsSzQMPIILbzN_0zo/s512/happy-third-birthday.png)

Il 27 ottobre 2021 ho iniziato il progetto di **dfAPKdngrader** con lo scopo di fornire alla comunità forense uno strumento di semplice utilizzo e robusto allo stesso tempo, in grado di eseguire il metodo del downgrade delle app su dispositivi Android.

E' la prima volta che lo senti nominare? Leggi il post di riferimento del programma [dfAPKdngrader (Forensic extraction tool for Android Backup APK Downgrade method)](https://djangofaiola.blogspot.com/2023/08/dfapkdngrader.html).

Da allora sono trascorsi 3 anni e ad oggi posso dire che il progetto ha riscosso un discreto successo sia in Italia che all'estero.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgi6dLR2TeYw07tjDDMLp3wfHyHHgj6teFRaV5vtBkf1G94mA6wYrb31ukKytyBWAUAXgZt5ZvgLBtXqEQ5h11kebYlVLe4sdWb8cnma41iAlqIbkgiDbXx6KgEf3160mrW_FFZQuK9_d99zffv6PnQk3Y3jKDF2JYfLAacKa_YaJK2BkhO5NLnfKsh-Tk/w640-h392/dfAPKdngrader-about-0.4.0-eng.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgi6dLR2TeYw07tjDDMLp3wfHyHHgj6teFRaV5vtBkf1G94mA6wYrb31ukKytyBWAUAXgZt5ZvgLBtXqEQ5h11kebYlVLe4sdWb8cnma41iAlqIbkgiDbXx6KgEf3160mrW_FFZQuK9_d99zffv6PnQk3Y3jKDF2JYfLAacKa_YaJK2BkhO5NLnfKsh-Tk/s1362/dfAPKdngrader-about-0.4.0-eng.png)

Per festeggiare questo anniversario ho deciso di rilasciare la versione v0.4.0:

* **Added**: Riconoscimento automatico della lingua locale e caricamento del file .po/.mo con la lingua associata se esiste.
* **Added**: Forzatura della lingua passando il parametro --lang <code> all'avvio del programma; <code>=es per caricare il file con la lingua spagnola o <code>=de per quella tedesca etc. se presenti.
* **Added**: Schermata di riepilogo dei pacchetti sincronizzati online: nuovi, cambiati ed eliminati.
* **Added**: Schermata dispositivo: il messaggio di attenzione "Abilita resta attivo", se cliccato, svolge in automatico l'operazione.
* **Changed**: La struttura del file APKs.ini per il supporto della schermata di riepilogo (trasparente all'utente); "isCustom": true è obsoleto, sostituito con "state": "custom".
* **Added**: Migliorata l'interfaccia grafica per l'elenco dei pacchetti disponibili: aggiunto menu contestuale.
* **Added**: Opzione "Forza il caricamento di tutte le app (fallite o eseguite con successo" per il metodo di RIPRISTINO.
* **Fixed**: bug minori.

Oltre **400** sono ora le app disponibili per il downgrade, quasi 100 in più della precedente lista. Un pacchetto enorme e comunque piccolo se si considerano le app localizzate più popolari dei vari paesi.

Ribadisco, l'APK downgrade non è un metodo sostitutivo per l'estrazione dei dati ma un'alternativa, come dire di "ultima spiaggia", quando tutti gli altri non sono praticabili.

Schermata di riepilogo:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhR8oTq9iNgJwKl_-ejFUh_I9gn0qXtpKey0xeLe3L4gxH4KP0Uuu3zHLrowqdDx1hdqm8-Iuyw6QRyw-CO_vXSBB7w_r9k-TizPqrj8J7gLB5wvXQFfeLt1XahPusuokfrEFPD0bSCD9jVexvuaxc9F8ohrJUmE_EzTosLvoRVS7vBjb-aahdLky1r9HY/w640-h392/dfAPKdngrader-sync-0.4.0-eng.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhR8oTq9iNgJwKl_-ejFUh_I9gn0qXtpKey0xeLe3L4gxH4KP0Uuu3zHLrowqdDx1hdqm8-Iuyw6QRyw-CO_vXSBB7w_r9k-TizPqrj8J7gLB5wvXQFfeLt1XahPusuokfrEFPD0bSCD9jVexvuaxc9F8ohrJUmE_EzTosLvoRVS7vBjb-aahdLky1r9HY/s1362/dfAPKdngrader-sync-0.4.0-eng.png)

Riepilogo del package (doppio click) sulla riga:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi0lOozRFgoBvj-uhAGUYl2VB5TVW-UNjQD3xK1XeGElIWRk0mUoT8BPcR_7pEr4w0ESwBAwIPH31o2MkGoBwVvEvnqtuKtZxNnNoF6w9xfeoFJUC7DIRz0vU0Y8zjhqvscZHfzKdx9FME2aAGopyIUH8NOc7kkXewmCVBBIfz7MPR0AXdhklx5SvWEn_U/w640-h392/dfAPKdngrader-appinfo-0.4.0-eng.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi0lOozRFgoBvj-uhAGUYl2VB5TVW-UNjQD3xK1XeGElIWRk0mUoT8BPcR_7pEr4w0ESwBAwIPH31o2MkGoBwVvEvnqtuKtZxNnNoF6w9xfeoFJUC7DIRz0vU0Y8zjhqvscZHfzKdx9FME2aAGopyIUH8NOc7kkXewmCVBBIfz7MPR0AXdhklx5SvWEn_U/s1362/dfAPKdngrader-appinfo-0.4.0-eng.png)

Inoltre è possibile aprire il browser alla pagina dell'app all'interno del Play Store  (link WhatsApp Messenger nel caso in figura).

Colgo l'occasione per sottolineare che ho fornito con l'eseguibile anche i file PO (Portable Object) per chi fosse interessato a dare il suo contributo per il supporto multilingua. Inoltre se avete package personalizzati non inclusi nella mia lista, sentitevi liberi di condividerli 😂 .

👏 Grazie a tutti per aver apprezzato il mio lavoro. Un ringraziamento speciale va fatto a [Andrea Lazzarotto](https://andrealazzarotto.com) per avermi spinto a creare questo blog e per aver contribuito con i suoi preziosi suggerimenti a migliorare il prodotto.

### Ultima versione

[Windows](http://bit.ly/3DJOdiH) | [Linux](http://bit.ly/44T3jyj)

Il software è proprietario (Freeware - closed source) e per l'uso commerciale considera una piccola donazione valida come autorizzazione implicita al suo utilizzo.

### Elenco delle nuove app supportate

1. Airalo
2. AlfredCamera
3. Allegro
4. AM - Ashley Madison
5. Auto.ru
6. Bonjour RATP (RATP)
7. CallApp (CallApp Contacts)
8. Cartão Continente
9. Cashify
10. com.l
11. DAILYHOTEL (데일리호텔)
12. Daraz
13. Disco
14. Dolap
15. DoorDash
16. droom
17. EatSure (Faasos)
18. eHarmony
19. Eyecon
20. Familo (Familonet)
21. Favor
22. Feeld
23. Finally
24. Fiverr
25. foodora (OnlinePizza)
26. Foody
27. FREENOW for drivers (mytaxi)
28. GMX Mail (Mail)
29. Grab Driver
30. GrubHub
31. Hacoo (Hacoo SaraMart, Doop, SaraMart)
32. Hungama
33. iFood comida e mercado em casa
34. immowelt
35. ixigo
36. Jaumo
37. JD Sports
38. Justdial
39. Kaufland
40. Klook
41. Lalamove
42. Lazada
43. Lovely
44. Mail.ru
45. Match (match.com)
46. Mercado Libre
47. Mingle2
48. Myntra
49. Neenbo
50. Nextcloud
51. noon
52. OpenSooq (السوق المفتوح)
53. Ourtime Date, Meet 50+ Singles
54. ownCloud
55. OZON (OZON.ru)
56. pCloud
57. PedidosYa
58. Pegasus
59. PlantNet Plant Identification (Pl@ntNet)
60. Polarsteps
61. priceline
62. PURE
63. Ruhavik
64. Save Location GPS
65. Shop Samsung
66. Snapdeal
67. Spicy
68. Star Taxi
69. talabat
70. Tappsi Easy (Tappsi)
71. TAXI 18300
72. TAXI Deutschland
73. taxi.eu
74. TaxiMe Driver
75. Tchibo
76. Tellonym
77. TicketSwap
78. Tokopedia
79. Traveloka
80. Trendyol
81. TripCase
82. Turo
83. Vivino
84. Waiter
85. Wapa
86. Weather Underground
87. WEB.DE Mail (Mail)
88. Whoosh
89. Wikiloc
90. wine-searcher
91. Xe (Currency)
92. Yandex Disk
93. Yandex Weather
94. Yanolja (야놀자)
95. Yassir
96. Zipcar

[Invia tramite email](https://www.blogger.com/share-post.g?blogID=837713476890397786&postID=2812729564866332768&target=email "Invia tramite email")[Postalo sul blog](https://www.blogger.com/share-post.g?blogID=837713476890397786&postID=2812729564866332768&target=blog "Postalo sul blog")[Condividi su X](https://www.blogger.com/share-post.g?blogID=837713476890397786&postID=2812729564866332768&target=twitter "Condividi su X")[Co...