---
title: Quando la truffa è talmente spavalda da rasentare l’elogio: Paypal e l’account Postfinance
url: http://attivissimo.blogspot.com/2022/12/quando-la-truffa-e-talmente-spavalda-da.html
source: Il Disinformatico
date: 2022-12-12
fetch_date: 2025-10-04T01:15:55.619468
---

# Quando la truffa è talmente spavalda da rasentare l’elogio: Paypal e l’account Postfinance

# [Il Disinformatico](https://attivissimo.blogspot.com/)

Un blog di Paolo Attivissimo, giornalista informatico e cacciatore di bufale

**Informativa privacy e cookie:** Questo blog include cookie di terze parti. Non miei ([dettagli](https://tinyurl.com/2p9apfu5))

[Prossimi eventi pubblici](https://attivissimo.me/disinformaticalendario/prossimi/) – [Donazioni](https://attivissimo.me/donazioni/) – [Sci-Fi Universe](https://scifiuniverse.it)

## Cerca nel blog

|  |  |
| --- | --- |
|  |  |

## 2022/12/11

### Quando la truffa è talmente spavalda da rasentare l’elogio: Paypal e l’account Postfinance

*Nota: alcuni dettagli di questo articolo sono stati modificati rispetto
alla realtà per esigenze di narrazione e per proteggere le identità delle
persone coinvolte. La sostanza tecnica dell’articolo è inalterata.
Questa è una versione estesa del testo del podcast del 16 dicembre 2022. Pubblicazione iniziale: 2022/12/11 10:51. Ultimo aggiornamento: 2022/12/22
12:40.*

Intendiamoci subito: un crimine è un crimine e come tale va condannato. Una
persona ha perso parecchi soldi a causa della truffa che sto per raccontarvi.
Ma la sfacciataggine e la spavalderia della tecnica usata dal criminale sono sorprendenti e confesso di avere un piccolo moto di
ammirazione per l’astuzia di chi l’ha concepita e messa in atto. In ogni caso, questo tipo originale di trappola informatica può essere un pericolo per molti, soprattutto nel periodo natalizio.

---

Questa storia inizia con una telefonata. Una persona mi chiama chiedendo aiuto
per risolvere una truffa: ha usato il proprio conto PayPal, sul quale aveva
accumulato del denaro, per inviare a se stessa circa duemila franchi, dando
ordine a PayPal di versarli sul suo conto Postfinance (la versione svizzera di
un conto corrente presso l’ufficio postale), ma i soldi non sono mai arrivati.

Non ci sono indicazioni che il suo computer sia stato attaccato o che qualcuno
abbia avuto accesso al suo conto PayPal, e l’ipotesi che qualcuno sia riuscito
a dirottare il suo trasferimento di denaro mentre era in transito sembra
tecnicamente improbabile. Frodi o errori da parte di PayPal o di Postfinance
sembrano ancora più implausibili. La vittima dice di essere sicura di essere entrata
direttamente nel proprio account PayPal e di aver dato le proprie
credenziali al sito originale, per cui è da escludere un *phishing* (furto di credenziali effettuato inducendo la vittima a visitare un sito che ha lo stesso aspetto di quello autentico ma è gestito dai criminali) o un
*man in the middle* (intercettazione delle comunicazioni della vittima con il sito autentico).

Sembra un mistero irrisolvibile, ma come mi capita spesso in situazioni come
questa chiedo alla vittima di descrivermi in dettaglio i passi che ha
compiuto, mentre io li ripercorro usando il *mio* conto PayPal come ambiente di prova.

La vittima
mi racconta che è entrata nel proprio conto e ha cliccato sull’opzione di invio
denaro nella pagina principale, etichettata *Send money* nella versione
in inglese del sito.

Lo faccio anch’io, e sul monitor del computer mi compare appunto l’opzione di inviare denaro, bene in vista al centro della
schermata:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEinvvbr67cjYUsx-8wkP5HM3ZC-mZnJhB8f34NIjWoXPWSrz4rV2iCVHzgLlQ-58b5F9M6U6aHbhtOWhL6UDz5d6Mu6-8TOe1jnBcGek-eEtcMQYBGXNUudJJR_4A49TD_xHLoSpCkIB0nB7Tbewd1nNiXCTd7R6VUiC1P1q59-5i9I4f5nPlU/s16000/Screenshot%202022-12-11%20at%2010.14.56_censored.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEinvvbr67cjYUsx-8wkP5HM3ZC-mZnJhB8f34NIjWoXPWSrz4rV2iCVHzgLlQ-58b5F9M6U6aHbhtOWhL6UDz5d6Mu6-8TOe1jnBcGek-eEtcMQYBGXNUudJJR_4A49TD_xHLoSpCkIB0nB7Tbewd1nNiXCTd7R6VUiC1P1q59-5i9I4f5nPlU/s1221/Screenshot%202022-12-11%20at%2010.14.56_censored.jpg)

La vittima mi spiega che a questo punto ha cliccato su *Send money*,
visto che doveva inviare del denaro, e ha digitato *Postfinance* nella
casella di ricerca del destinatario.

Ripeto i suoi passi, e quindi clicco su *Send money*. Mi compare la
casella di ricerca nella quale, appunto, si cerca il nome dell’utente al quale inviare denaro:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjuIDIn0hq-UCAokXogBCvyYwg6c582VndD76McmnszA2hRFQfAb_3qfbxzbjDqCL7aNtHRw1odD8WXC733oVuOPBbfoiHgdyEPsk8POh0O86lLvD1QxccaH3Cs8iSB2icB6NE0rejIyfAdTJ8Fk0K7wTpRzetHXhzmkAFGCHe737C6OTzavRQ/s16000/Screenshot%202022-12-11%20at%2010.21.38_censored.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjuIDIn0hq-UCAokXogBCvyYwg6c582VndD76McmnszA2hRFQfAb_3qfbxzbjDqCL7aNtHRw1odD8WXC733oVuOPBbfoiHgdyEPsk8POh0O86lLvD1QxccaH3Cs8iSB2icB6NE0rejIyfAdTJ8Fk0K7wTpRzetHXhzmkAFGCHe737C6OTzavRQ/s1226/Screenshot%202022-12-11%20at%2010.21.38_censored.jpg)

In questa casella digito *Postfinance*, come ha fatto la vittima, e mi compare sullo schermo l’account di nome *Postfinance*.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMpEPa6Fi42HGEZ4Myl8K_5PzAeG8Q1h3ZjnA5qumnlvVcvZfywzFujm0EN9u-V4Penf09TQCHV6-BC9ynfb7szBUb694N3vU0a03Ap30-65_ODLS6tPfKKLXxw2fqQQdWQrsYWTFwb6t1BRZDnWOJbBxWLGwe0DVarm-WxP11BUwnlmanRBI/s16000/Screenshot%202022-12-11%20at%2010.22.20_censored.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMpEPa6Fi42HGEZ4Myl8K_5PzAeG8Q1h3ZjnA5qumnlvVcvZfywzFujm0EN9u-V4Penf09TQCHV6-BC9ynfb7szBUb694N3vU0a03Ap30-65_ODLS6tPfKKLXxw2fqQQdWQrsYWTFwb6t1BRZDnWOJbBxWLGwe0DVarm-WxP11BUwnlmanRBI/s1227/Screenshot%202022-12-11%20at%2010.22.20_censored.jpg)

La vittima mi spiega che ha cliccato su questo account e ha immesso la cifra
da inviare, cliccando poi sul pulsante di invio. Da quel momento non ha più
visto i propri soldi.

Provo a farlo anch’io, con un importo simbolico di un centesimo, ma mi trattengo dal cliccare sul pulsante *Send Money Now.*

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjJ9YuZXkvZ3gdS3OLcdZd_hOU9m9nfrGotEgAKutbfShxpHo-YsKObUbFSMtbZiG59M927IPKpa2MPpINTiRrKk07FcbuiGLGPuJx02stCh6GO6J9N0pxRa-_bIheR4LCp4gEVbmcQz0lgdQCwQ9EovBuVHV_JEmVh82Cbn1mTlSjSqYUHwN8/s16000/Screenshot%202022-12-11%20at%2010.24.46_censored.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjJ9YuZXkvZ3gdS3OLcdZd_hOU9m9nfrGotEgAKutbfShxpHo-YsKObUbFSMtbZiG59M927IPKpa2MPpINTiRrKk07FcbuiGLGPuJx02stCh6GO6J9N0pxRa-_bIheR4LCp4gEVbmcQz0lgdQCwQ9EovBuVHV_JEmVh82Cbn1mTlSjSqYUHwN8/s1226/Screenshot%202022-12-11%20at%2010.24.46_censored.jpg)

Avete capito come si è svolta la frode?

Vi lascio un po’ di tempo per pensarci. Scrivete la vostra soluzione nei
commenti, se vi va.

---

### ALLERTA SPOILER: La soluzione

La vittima ha commesso un errore abbastanza comprensibile: ha usato la
funzione *Send money* invece di quella giusta, che ha un nome molto
simile, ossia *Transfer money*.

In questo modo la vittima, invece di
mandare i soldi al proprio conto Postfinance (che va preventivamente
registrato fra i conti destinatari autorizzati), ha mandato i soldi a un
truffatore che ha avuto l’idea semplice e geniale di creare un account di nome
*Postfinance* e ha avuto la spavalderia di confidare che PayPal
non avrebbe fatto alcun controllo significativo sui nomi degli account. E ha avuto ragione.

La vittima, poco pratica di PayPal e presa dalla fretta perché era in partenza
per un viaggio, ha pensato che scegliendo
*Postfinance* gli automatismi di PayPal avrebbero dedotto dai dati del mittente a quale conto andassero inviati i soldi. L’errore iniziale è stato suo, certo, ma è stato
facilitato dall’ambiguità fra *inviare* denaro e *trasferire* denaro
e soprattutto dal fatto che PayPal non sta facendo nulla di efficace per
evitare queste truffe: infatti ospita numerosissimi account che hanno nomi o
*nickname* palesemente ingannevoli.

Grazie anche alle segnalazioni dei lettori nei commenti qui sotto e su
[Mastodon](https://mastodon.uno/%40ildisinformatico/109494423960488320), è infatti emerso che fra gli utenti di PayPal, oltre a *Postfinance* (con
tanto di pratico e ingannevolissimo link rapido *Paypal.me/postfinance*), ci sono...