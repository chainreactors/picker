---
title: I distributori di sigarette italiani attaccati con messaggi pro-Cospito sono trovabili su Shodan
url: https://attivissimo.blogspot.com/2023/03/i-distributori-di-sigarette-italiani.html
source: Instapaper: Unread
date: 2023-03-28
fetch_date: 2025-10-04T10:56:29.891582
---

# I distributori di sigarette italiani attaccati con messaggi pro-Cospito sono trovabili su Shodan

# [Il Disinformatico](https://attivissimo.blogspot.com/)

Un blog di Paolo Attivissimo, giornalista informatico e cacciatore di bufale

**Informativa privacy e cookie:** Questo blog include cookie di terze parti. Non miei ([dettagli](https://tinyurl.com/2p9apfu5))

[Prossimi eventi pubblici](https://attivissimo.me/disinformaticalendario/prossimi/) – [Donazioni](https://attivissimo.me/donazioni/) – [Sci-Fi Universe](https://scifiuniverse.it)

## Cerca nel blog

|  |  |
| --- | --- |
|  |  |

## 2023/03/27

### I distributori di sigarette italiani attaccati con messaggi pro-Cospito sono trovabili su Shodan. E ora anche su Google

Durante il fine settimana appena concluso numerosi distributori di sigarette
in Italia sono stati violati da intrusi informatici che hanno alterato i
prezzi di vendita delle sigarette, portandoli a 10 centesimi, e hanno
sostituito le immagini visualizzate sugli schermi di questi distributori con
immagini in favore di Alfredo Cospito, un detenuto in sciopero della fame da
oltre cinque mesi per protesta contro il regime di carcere duro al quale è
sottoposto.

Trovate tutti i dettagli della vicenda su
[*Il Post*](https://www.ilpost.it/2023/03/27/attacco-hacker-distributori-sigarette-anarchici-cospito/). Il presidente nazionale di AssoTabaccai ha dichiarato al
*Corriere* che gli risulta che una delle aziende interessate, la
Laservideo,*“utilizzi un sistema per cui è il server centrale a inviare informazioni ai
distributori. Quindi hackerando il server centrale, è stato possibile
entrare contemporaneamente in tutti i distributori”*.

Non entro nel merito politico della notizia: segnalo soltanto che i
distributori di sigarette della [Laservideo](http://www.laservideo.it) sono facilissimi da trovare online
tramite un comune motore di ricerca per l’Internet delle Cose come [Shodan](https://www.shodan.io), nel
quale è sufficiente immettere la richiesta

*http.html:'laservideo' country:IT*

per ottenere un elenco degli indirizzi IP e delle porte aperte di questi
distributori. Non perdo neanche tempo a mascherare i dati, visto che reperirli è assolutamente banale:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg7GC66oLAjGyvYK_gu6b537SF3wrzzWABBMJwSAMxskWcj1-FxeEE0a_P-ibzK24xmlz6kmG8Cc5WoWHTkI3Q47hQoO9Xt3738D57J2YKLesaldOxDPp0_fT7MYje-HbgOVVPLq-yoXOpk_3yijq5XpshLgh6IZURBU0ScUyI8jwCpo0hzKrU/s16000/Screenshot%202023-03-27%20at%2009.57.12.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg7GC66oLAjGyvYK_gu6b537SF3wrzzWABBMJwSAMxskWcj1-FxeEE0a_P-ibzK24xmlz6kmG8Cc5WoWHTkI3Q47hQoO9Xt3738D57J2YKLesaldOxDPp0_fT7MYje-HbgOVVPLq-yoXOpk_3yijq5XpshLgh6IZURBU0ScUyI8jwCpo0hzKrU/s1566/Screenshot%202023-03-27%20at%2009.57.12.png)

Risulta insomma che questi distributori non sono protetti dietro una VPN, ma sono accessibili *direttamente su Interne*t e *con un normale browser* tramite la
porta 90:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjCZ35wZxlEWfIyFt1R9ATEb03Ir_XJW8HwaZQDFZHYFg9ioxHpn4G5XvTeYPCTj5ZJiIrWSwRyMmmpUfGj5bnpWlUP932sUS84DhseCq4HPi6wSWUaNLoCfCaiYizMYziB-3tUoSJVI97whfl7pPb_Dyn2nrnAkFijQ41pKHUuoflFM0M7MCA/s16000/Screenshot%202023-03-27%20at%2010.12.25.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjCZ35wZxlEWfIyFt1R9ATEb03Ir_XJW8HwaZQDFZHYFg9ioxHpn4G5XvTeYPCTj5ZJiIrWSwRyMmmpUfGj5bnpWlUP932sUS84DhseCq4HPi6wSWUaNLoCfCaiYizMYziB-3tUoSJVI97whfl7pPb_Dyn2nrnAkFijQ41pKHUuoflFM0M7MCA/s1565/Screenshot%202023-03-27%20at%2010.12.25.png)

Questo è il contenuto *[pubblicamente accessibile](http://79.62.159.58:90/FrmLogin.aspx)* della pagina di login di uno di questi distributori:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiP8E5Ic4K4Dij1I1pO_sJqC7xToCwQtNAOC-2t1N7uVKHgjPM4xJ1DiTsF62SGrZb8EVz-HT9zaAe8nvmCCoh-nnnNUkKiMn7AvyUz7BjPc-_OACFhZoaO3pD3iHA7eqlg5QjdRHMwerJ5zSLTJAM9tfcJoKqF496fvc9Nw7BkZIP94bt4Xa0/s16000/Screenshot%202023-03-27%20at%2009.58.54.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiP8E5Ic4K4Dij1I1pO_sJqC7xToCwQtNAOC-2t1N7uVKHgjPM4xJ1DiTsF62SGrZb8EVz-HT9zaAe8nvmCCoh-nnnNUkKiMn7AvyUz7BjPc-_OACFhZoaO3pD3iHA7eqlg5QjdRHMwerJ5zSLTJAM9tfcJoKqF496fvc9Nw7BkZIP94bt4Xa0/s1333/Screenshot%202023-03-27%20at%2009.58.54.png)

Ovviamente non ho modo di sapere se le password di questi distributori sono robuste e diversificate, come richiederebbe la sicurezza informatica più elementare, ma sulla base di questi fatti sospetto che la tesi dell’hackeraggio del “server centrale” non sia quella più plausibile.

---

**2023/03/28 9:20.** Dai commenti emerge che i distributori sono reperibili anche semplicemente in Google, una volta che si sa qual è la stringa di testo che li caratterizza: è sufficiente cercare *“Inserire Nome Utente e Password forniti da Laservideo”*.

Inoltre Laservideo ha [dichiarato](https://www.distributoriautomaticisigarette.it/) pubblicamente che *“Contrariamente a quanto riportato da molti organi di stampa, l'attacco hacker di sabato 25 marzo non ha riguardato i server centrali Laservideo ma ha colpito puntualmente solo una parte minoritaria dei distributori, agendo direttamente attraverso la connessione delle singole tabaccherie.”*

Pubblicazione iniziale:
[27.3.23](https://attivissimo.blogspot.com/2023/03/i-distributori-di-sigarette-italiani.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/7421441/5054715246087978135 "Post per email")

Labels:
[attacchi informatici](https://attivissimo.blogspot.com/search/label/attacchi%20informatici),
[Internet delle cose](https://attivissimo.blogspot.com/search/label/Internet%20delle%20cose),
[Shodan](https://attivissimo.blogspot.com/search/label/Shodan)

#### Nessun commento:

[Posta un commento](https://www.blogger.com/comment/fullpage/post/7421441/5054715246087978135)

[Post più recente](https://attivissimo.blogspot.com/2023/03/podcast-rsi-story-come-hackerare-un.html "Post più recente")

[Post più vecchio](https://attivissimo.blogspot.com/2023/03/twitter-fine-dei-bollini-blu-classici.html "Post più vecchio")
[Home page](https://attivissimo.blogspot.com/)

Iscriviti a:
[Commenti sul post (Atom)](https://attivissimo.blogspot.com/feeds/5054715246087978135/comments/default)

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

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiwWo0VmlJW4KbR2KYCr10iEPHo1F2w37XMCsBe5YIHWIkZiTTkwcN6y_lIPVZN5bLGrtRczw_v5yBt1gR4s-sJkJ5lF9aXXgNJAF9TQ3LtGxygFpUy8zxCOOjP4YWq4t27h8HnIQ/s200/calendar-flat-icon-01-.jpg)](https://attivissimo.me/disinformaticalendario/prossimi/)

[Prossimi eventi pubblici](https://attivissimo.me/disinformaticalendario/prossimi/)

[Eventi pu...