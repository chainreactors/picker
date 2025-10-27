---
title: Le parole di Internet: fork bomb
url: http://attivissimo.blogspot.com/2022/10/le-parole-di-internet-fork-bomb.html
source: Il Disinformatico
date: 2022-10-22
fetch_date: 2025-10-03T20:38:10.999493
---

# Le parole di Internet: fork bomb

# [Il Disinformatico](https://attivissimo.blogspot.com/)

Un blog di Paolo Attivissimo, giornalista informatico e cacciatore di bufale

**Informativa privacy e cookie:** Questo blog include cookie di terze parti. Non miei ([dettagli](https://tinyurl.com/2p9apfu5))

[Prossimi eventi pubblici](https://attivissimo.me/disinformaticalendario/prossimi/) – [Donazioni](https://attivissimo.me/donazioni/) – [Sci-Fi Universe](https://scifiuniverse.it)

## Cerca nel blog

|  |  |
| --- | --- |
|  |  |

## 2022/10/21

### Le parole di Internet: *fork bomb*

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgh0X3SI_jcEHl946jFjNm66EefbzoJnv4BVmse_LkleDpn8czAtC0VcJRKJPyWUX-B6eYLUj0vu-dCzWOgg4Bd0j4-DL3G9tKOByk4NE6TQxCiIyiZc6rht2s1hv3fs-dxvw6R5YmiBZ9OrDPlfUyLZjBsfhG-LIsFFhHjDKz-rnqCX4gYXs8/s16000/fork-bomb-process.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgh0X3SI_jcEHl946jFjNm66EefbzoJnv4BVmse_LkleDpn8czAtC0VcJRKJPyWUX-B6eYLUj0vu-dCzWOgg4Bd0j4-DL3G9tKOByk4NE6TQxCiIyiZc6rht2s1hv3fs-dxvw6R5YmiBZ9OrDPlfUyLZjBsfhG-LIsFFhHjDKz-rnqCX4gYXs8/s820/fork-bomb-process.jpg)

*Questo articolo è disponibile anche in [versione podcast audio](https://attivissimo.blogspot.com/2022/10/podcast-rsi-zuckerberg-vuole-sapere.html).*

Due punti, aperta parentesi tonda, chiusa parentesi tonda, aperta parentesi
graffa, spazio, due punti, barra verticale, due punti, E commerciale, spazio,
chiusa parentesi graffa, punto e virgola, due punti.

Questi tredici caratteri, spazi compresi, sono tutto quello serve per mandare
in *crash* quasi tutti i computer. Non importa se usate Windows, Linux o
macOS: se digitate questa esatta sequenza di caratteri in una finestra di
terminale o in una riga di comando, il vostro computer quasi sicuramente si
bloccherà e sarà necessario riavviarlo, perdendo tutti i dati non salvati. Non
è necessario essere amministratori del computer.

Ovviamente digitare questa sequenza di caratteri non è un esperimento da
provare su un computer che state usando per lavoro o che non potete
permettervi di riavviare bruscamente.

Ma come è possibile che basti così poco?

Quella sequenza di caratteri non è una falla recente: è un problema conosciuto
da decenni e si chiama *fork bomb* o *rabbit virus* o ancora
*wabbit*. Il primo caso di *fork bomb* risale addirittura al 1969.
Non è neanche un virus: fa parte del *normale funzionamento* dei
computer.

Semplificando in maniera estrema, ogni programma o processo che viene eseguito
su un computer può essere duplicato, formando un processo nuovo che viene
eseguito anch’esso. Questa duplicazione si chiama *fork*, nel senso di
*“biforcazione”*. A sua volta, il processo nuovo può creare una copia di
sé stesso, e così via.

Se si trova il modo di far proseguire questa duplicazione indefinitamente,
prima o poi verranno creati così tanti processi eseguiti simultaneamente che
il computer esaurirà le risorse disponibili, come la memoria o il processore,
e quindi andrà in tilt, paralizzandosi per il sovraccarico e costringendo
l’utente a uno spegnimento brutale e a un riavvio.

Questa trappola letale è stata per molto tempo un’esclusiva dei sistemi Unix e
quindi anche di Linux, ma oggi esiste anche in macOS e in Windows 10 e
successivi. Questi sistemi operativi, infatti, includono quella che si chiama
*[shell](https://it.wikipedia.org/wiki/Shell_%28informatica%29)
bash*, ossia un particolare interprete dei comandi (chiamato *bash*) usato
anche dai sistemi Linux e Unix. Dare a questo interprete quei tredici
caratteri è un modo molto conciso di ordinargli di generare un processo che
generi un processo che generi un processo e così via.

Non è l’unica maniera di avviare questa reazione a catena: ce ne sono
[molte](https://it.wikipedia.org/wiki/Fork_bomb)
[al](https://www.imperva.com/learn/ddos/fork-bomb/)[tre](https://www.imperva.com/learn/ddos/fork-bomb/), anche per le
vecchie versioni di Windows, ma questa è particolarmente minimalista.

> :() definisce una funzione di nome ":" e il cui contenuto è quello che si trova fra le parentesi graffe
>
> :|:& è il contenuto della funzione, ed è una chiamata alla funzione stessa (":"), seguita da un *pipe* (che manda l’output della funzione chiamata a un’altra chiamata della funzione ":") e da un ampersand (che mette in background la chiamata)
>
> ; conclude la definizione della funzione
>
> : ordina di eseguire la funzione di nome ":"
>
> È forse più chiaro se si usa *bomba* per dare un nome “normale” alla funzione e si usa una notazione meno ermetica:
>
> bomba() {

Difendersi non è facilissimo per l’utente comune: ci sono dei
[comandi](https://www.imperva.com/learn/ddos/fork-bomb/) che
permettono di porre un limite al numero di processi che è possibile creare, ma
comunque non offrono una protezione perfetta. In alternativa, si può tentare
di disabilitare la shell bash in Windows, ma le conseguenze possono essere
imprevedibili.

In parole povere, il modo migliore per evitare una *fork bomb* è impedire
che un burlone o malintenzionato possa avvicinarsi, fisicamente o
virtualmente, alla tastiera del vostro computer.

*Fonti aggiuntive:
[Apple](https://support.apple.com/it-it/HT208050),* *[Cyberciti](https://www.cyberciti.biz/faq/understanding-bash-fork-bomb/), [Okta](https://www.okta.com/identity-101/fork-bomb/).*

Pubblicazione iniziale:
[21.10.22](https://attivissimo.blogspot.com/2022/10/le-parole-di-internet-fork-bomb.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/7421441/4930741896338045372 "Post per email")

Labels:
[Linux](https://attivissimo.blogspot.com/search/label/Linux),
[MacOS](https://attivissimo.blogspot.com/search/label/MacOS),
[parole di Internet](https://attivissimo.blogspot.com/search/label/parole%20di%20Internet),
[PodcastRSI](https://attivissimo.blogspot.com/search/label/PodcastRSI),
[radio](https://attivissimo.blogspot.com/search/label/radio),
[Windows 10](https://attivissimo.blogspot.com/search/label/Windows%2010)

#### Nessun commento:

[Posta un commento](https://www.blogger.com/comment/fullpage/post/7421441/4930741896338045372)

[Post più recente](https://attivissimo.blogspot.com/2022/10/podcast-rsi-zuckerberg-vuole-sapere.html "Post più recente")

[Post più vecchio](https://attivissimo.blogspot.com/2022/10/bluebleed-spasso-i-dati-privati-di.html "Post più vecchio")
[Home page](https://attivissimo.blogspot.com/)

Iscriviti a:
[Commenti sul post (Atom)](https://attivissimo.blogspot.com/feeds/4930741896338045372/comments/default)

Choose a language
English
Afrikaans
العربية
Azərbaycan
Беларуская
Български
Català
Český
Cymraeg
Danske
Deutsch
Ελληνικά
Euskal
Español
Eesti
فارسی
Suomalainen
Français
Gaeilge
Galego
हिन्दी
Hrvatski
Kreyòl
Magyar
Հայերեն
Bahasa Indonesia
Íoslainnis
עברית
日本
ქართული
한국어
Latinum
Lietuvas
Latvijā
Македонски
Melayu
Malti
Nederlandse
Norske (Bokmål)
Polski
Português
Română
Русский
Slovenská jazyku
Slovenski jezik
Shqiptar
Српски језик
Svenska
Swahili
ไทย
Filipino
Türk
Українське
اردو
Việt
ייִדיש
中文 (简体字)
中文 (正體字)

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhQ-_-OkaZJxWiZ8HkG3dGC9gbuPA1qB0VDZQ_nOM3eKADHVNjFHFpuxfv0jRYUqMFEy9I7T68WBC4RqG2fgk01IH3SXqiRjKw2b146wtndBtQV-IupobE5YcCFlmXWeIV8sQYgsw/s1600/Cattivissimo-by-francesco-lombardi-gianluigi-gatti.png)

Credit: Gianluigi Gatti

## Libri

[Luna? Sì, ci siamo andati!](http://luna1969.info)

[Moon Hoax: Debunked!](https://www.moonhoaxdebunked.com/)

[Almanacco dello Spazio](https://almanaccodellospazio.ch/)

[L’Efficercatore: uso avanzato dei motori di ricerca](https://efficercatore.blogspot.com/)

[Come diventare detective antibufala](https://www.generazioniconnesse.it/site/_file/documenti/Comunicazione/Fake_news/Dispensa_Docenti_decalogo_bastabufale.pdf) (guida commissionata da MIUR e Camera dei Deputati)

[Gli altri miei libri](https://attivissimo.blogspot.com/p/libri-pubblicati.html)

## Appuntamenti pubblici

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiwWo0VmlJW4KbR2K...