---
title: Generare Un Seed Di Bitcoin Con Dei Dadi (Entropia)
url: http://darkwhite666.blogspot.com/2022/12/generare-un-seed-di-bitcoin-con-dei.html
source: Dark Space Blogspot
date: 2022-12-11
fetch_date: 2025-10-04T01:14:01.473661
---

# Generare Un Seed Di Bitcoin Con Dei Dadi (Entropia)

## Visualizzazioni Totali

[![Dark Space Blogspot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZgt0RUZjHgbkLsu7CbFNAiyAMd0qvDL2fubvcBv5c6R04keICe8K0ig6oXxzqa6519xC3S7eBHP3_F60rvo_NqafkHR83xyZwscmsQgwCw_EPQpiDWkgarGw08kUDwteX-zWL_I_uP1w/s1600/ask-fm.png)](https://darkwhite666.blogspot.com/)

TRA I PRIMI IN ITALIA A PARLARE DI BITCOIN (DAL 2012!): PER ESSERE SEMPRE AGGIORNATI SULLE NOVITA' TECNOLOGICHE DEL WEB SEGUITE LA PAGINA FACEBOOK (LINK A SINISTRA)

## domenica 11 dicembre 2022

### Generare Un Seed Di Bitcoin Con Dei Dadi (Entropia)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhEcX5lewDm8i4cE0pSCQsPrFRSSJ3KhWqPGbD0rRbs0ugeBacWAEX_E477ukIH2NtwWC4w1bl1aplG-LtIlB9Ln3uyxeTYdpsLlMTfuOzDakIkkayTnaReTRaxajdULnNBGTNwpotdvqKRgyfgPaPa3HAgHN8b0jhx9boj4yniTR87WrEFSjg1DwIf/w400-h293/hqdefault.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhEcX5lewDm8i4cE0pSCQsPrFRSSJ3KhWqPGbD0rRbs0ugeBacWAEX_E477ukIH2NtwWC4w1bl1aplG-LtIlB9Ln3uyxeTYdpsLlMTfuOzDakIkkayTnaReTRaxajdULnNBGTNwpotdvqKRgyfgPaPa3HAgHN8b0jhx9boj4yniTR87WrEFSjg1DwIf/s474/hqdefault.jpg)

Per avere una sicurezza maggiore quando si utilizza un wallet non custodial è possibile generare completamente offline un seed utilizzando l'entropia non del computer (che ci assegna un seed automatico di 12 o 24 parole) ma manualmente con dei dati (**[BIP39](https://medium.com/coinmonks/official-bip39-word-list-mnemonic-24f170ccfe62)**). Più è elevata l'entropia e più è sicuro il nostro seed. Entropia misura il disordine presente in un sistema fisico e nei processi fisici reali (irreversibili) aumenta sempre. In Informatica invece all'aumentare dell'entropia, diminuisce la quantità di informazione.

In generale l'entropia è utilizzata anche per generare password sicure, lanciando dei dadi. Ci sono dei portali online che ci indicano in quanto tempo la nostra password può essere craccata: [**Password Strength Checker**](https://delinea.com/resources/password-strength-checker) ed altri che ci indicano la complessità [**Rumkin Tools**](https://rumkin.com/tools/password/). Ad esempio per creare una password sicura, scelgo il numero di parole che comporranno la mia password (ad esempio 4 parole) e poi per ognuna lancio 5 volte i dadi, ottenendo 5 cifre (poi scaricando [**Diceware**](https://github.com/grempe/diceware) controllo questi 5 numeri a quale parola corrispondono, posso poi inserire numeri e caratteri alfanumerici). Tornando alla generazione del nostro seed per Bitcoin, per prima cosa scarichiamo il tool di Ian Coleman che poi utilizzeremo offline: [**IanColeman (Bip39)**](https://github.com/iancoleman/bip39/releases)

PROCEDIMENTO

Ciò che ci serve sono:

-moneta (testa/croce)

-4 dadi (con 6 facce)

Se lancio la moneta ed ottengo testa (head) avrò "h", poi lancio i 4 dadi e leggo da sinistra verso destra (o viceversa) i 4 numeri che mi escono, poi li vado a cercare nella tabella (**[BIP39](https://github.com/massmux/bip39-diceware-entropy)**) che contiene 2048 parole (elevate alla 12 mi indicano le possibili combinazioni). Ripeto questo procedimento per le 12 parole.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjje8o-4WAughLOILdyYFtVbit0VKp8iWEW7PewVAwUMeC6UummJiKLSL8CPfMjnJradnV3uOcUnShEOIJurxUNy-wOjtFvw_wiSaqLQFKQWO3XTfnJVBTwDLxEZUjVkKYysRqOINhCKS64j23HXkixj1wZ-6ZoXAiEW_G_By9ZTnI1hds_I0HLtkdh/w640-h382/Entropia%20Dadi.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjje8o-4WAughLOILdyYFtVbit0VKp8iWEW7PewVAwUMeC6UummJiKLSL8CPfMjnJradnV3uOcUnShEOIJurxUNy-wOjtFvw_wiSaqLQFKQWO3XTfnJVBTwDLxEZUjVkKYysRqOINhCKS64j23HXkixj1wZ-6ZoXAiEW_G_By9ZTnI1hds_I0HLtkdh/s1052/Entropia%20Dadi.png)

In seguito inserisco le 12 parole trovate nel tool di Coleman, la 12esima va cambiata (perchè è una checksum, cioè una parola di controllo). Se la mia 12esima parola ad esempio è Quiz (immagine di sotto), inserirò ad una ad una le 16 sopra sino a trovare quella giusta (utilizzo sempre il tool di Ian Coleman).

|  |
| --- |
| [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5IBz5wQbBG0QVXvpOlMUttkmsVNn-Cr4SWUQ9kiwdLPsKjBHK9G5BCCMF2vwQobGVHKiD1QW9Jc5SFHzqg0k9YKeFnPuDwmqTPJE3hSN4FE4bqd_0dnY-7R5vXoLVSXFuoqXqBk0AqLNkWOtwKy0pg_AVirthqWqtyGO9VVWXyNTjeFk7og9UEWJT/w640-h462/Seed.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5IBz5wQbBG0QVXvpOlMUttkmsVNn-Cr4SWUQ9kiwdLPsKjBHK9G5BCCMF2vwQobGVHKiD1QW9Jc5SFHzqg0k9YKeFnPuDwmqTPJE3hSN4FE4bqd_0dnY-7R5vXoLVSXFuoqXqBk0AqLNkWOtwKy0pg_AVirthqWqtyGO9VVWXyNTjeFk7og9UEWJT/s1050/Seed.png) |
|  |

Una volta che il seed viene segnalato giusto, posso inserirlo nel mio hardware wallet o software (tipo Electrum) con 12 parole (128 bit). Nel caso non venisse segnalato come valido, schiacciare su "options" e spuntare la casella su bip39. Se il seed ha 24 parole (256 bit), posso usare i dadi e la moneta trovando le 23 parole e poi la 24esima utilizzando questo tool che trova la checksum: [**BIP39checksum**](https://github.com/massmux/bip39checksum)

Per un PaperWallet si può usare: [**Papergen**](https://github.com/massmux/Papergen)

Per il bip85 (seed anche a 18 e 24 parole): [**Coldcard**](https://coldcard.com/docs/bip85)

Un altro procedimento sfrutta l'entropia dei numeri binari, assegnando lo 0 ai numeri 1, 3 e 5 e il binario 1 ai numeri 2, 4 e 6. Poi eseguo il calcolo seguendo questo schema (lo eseguo 23 volte per le 23 parole del mio seed, per la 24esima vale lo stesso discorso fatto prima):

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjIfq2Yib42AyQXTFTbeyhWFAkWgZt35E7AG9OUuJD3P79nIthCvqSlqO6aV67cRcXpBytpV6U7mywl3NMkTzwTfBQ9Ltvp0WJmHKqaFGul45Wfmo9x_TfkzldL1P0dl2yfqjPbTr-D67sgldlAKImU_ORCWOor8CjEiUg4uBlEIHzFCxHL688wbQ0j/w640-h472/Seed%20Dadi.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjIfq2Yib42AyQXTFTbeyhWFAkWgZt35E7AG9OUuJD3P79nIthCvqSlqO6aV67cRcXpBytpV6U7mywl3NMkTzwTfBQ9Ltvp0WJmHKqaFGul45Wfmo9x_TfkzldL1P0dl2yfqjPbTr-D67sgldlAKImU_ORCWOor8CjEiUg4uBlEIHzFCxHL688wbQ0j/s780/Seed%20Dadi.png)

In questo caso uso questo dizionario [**BIP39**](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt).

Il seed poi va finalizzato/importato su un wallet software/hardware, ricordo che è importante sempre svolgere queste operazioni offline. Una volta importato potrete connettere il dispositivo online.

Altrimenti è possibile scegliere le 24 parole a caso (delle 2048 disponibili), lanciando semplicemente il dado per 99 volte ottenendo 99 numeri da 1 a 6 quindi un'entropia di almeno 256 bit. Fatto questo esistono tool (meglio se usati offline) come quelli citati prima di Ian Coleman: [**Bip39**](https://iancoleman.io/bip39/) (spunto la casella "show entropy details" inserendo i 99 numeri in "entropy". Fatto questo otterrò le 12 o 24 parole (nel wallet [**Coldcard**](https://coldcard.com/docs/bip85) potrei inserire direttamente questi numeri, ottenendo il mio seed).

Pubblicato da
[DarkDave.|.666](https://www.blogger.com/profile/02696807736631988356 "author profile")

alle
[00:32](https://darkwhite666.blogspot.com/2022/12/generare-un-seed-di-bitcoin-con-dei.html "permanent link")

[![](//img1.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/1856644955194422917/8846237043505467578 "Post per email")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=1856644955194422917&postID=8846237043505467578&from=pencil "Modifica post")

[Invia tramite email](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=8846237043505467578&target=email "Invia tramite email")[Postalo sul blog](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=8846237043505467578&target=blog "Postalo sul blog")[Condividi su X](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=8846237043505467578&target=twitter "Condividi su X")[Condividi su Facebook](https://www.blogger.com/share-post.g?blogID=1856644955194422917&postID=8846237043505467578&target=facebook "Con...