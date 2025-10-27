---
title: Poi la gente si chiede come mai i dati personali finiscono a spasso
url: https://attivissimo.blogspot.com/2023/01/poi-la-gente-si-chiede-come-mai-i-dati.html
source: Instapaper: Unread
date: 2023-02-01
fetch_date: 2025-10-04T05:25:33.793376
---

# Poi la gente si chiede come mai i dati personali finiscono a spasso

# [Il Disinformatico](https://attivissimo.blogspot.com/)

Un blog di Paolo Attivissimo, giornalista informatico e cacciatore di bufale

**Informativa privacy e cookie:** Questo blog include cookie di terze parti. Non miei ([dettagli](https://tinyurl.com/2p9apfu5))

[Prossimi eventi pubblici](https://attivissimo.me/disinformaticalendario/prossimi/) – [Donazioni](https://attivissimo.me/donazioni/) – [Sci-Fi Universe](https://scifiuniverse.it)

## Cerca nel blog

|  |  |
| --- | --- |
|  |  |

## 2023/01/30

### Dati a spasso: elenco clienti assicurativi leggibile e modificabile da chiunque (aggiornamento: caso forse risolto)

*Ultimo aggiornamento: 2023/01/02 10:15. L’articolo è stato riscritto per
tenere conto degli aggiornamenti e per fornire un contesto più ampio.*

Quasi sempre i criminali informatici vengono immaginati e rappresentati come
maghi della tastiera che sanno scovare e rubare qualunque dato digitale usando
tecniche di penetrazione sofisticatissime, ma spesso queste tecniche non sono
affatto necessarie, perché i dati sono stati messi maldestramente a
disposizione del primo che passa e sono accessibili via Internet da chiunque
abbia una minima capacità informatica.

Per esempio, pochi giorni fa mi è arrivata in via confidenziale la
segnalazione di un sito aperto a chiunque che contiene quello che sembra
essere un elenco di dati assicurativi di clienti italiani, probabilmente della
zona di Chieti. Nomi, cognomi, indirizzi, codici fiscali, dettagli delle
polizze assicurative, e altro ancora.

Ma soprattutto contiene una voce dell’elenco che non è un nome e cognome di
cliente ma è un avviso:
*“Buongiorno questo database è accessibile a chiunque via Internet”*,
tutto in maiuscolo. Segno che qualcuno ha già trovato questo archivio, si è
accorto che è non solo leggibile da chiunque ma è anche *modificabile* da
chiunque, e ha pensato di lasciare un cordiale ma ben visibile avviso.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEijO5yR6uCwFWPIGLqmnXSS75IDYR4QyEhRCRW9aKey3XjNMTymowqp1erq4Gqcn7CrY3ABBHrZkzuzwVIeW4tTTl7YPeqi75v70jyCabaOPkJb5Ur35oHXr8gp9C2UkwdaMi-3qtafulHk0JZBrFuvmyewzqcuC9SeFDbWUzKdRrZY7vkw3b4/w640-h298/Screenshot%202023-01-30%20at%2011.56.24_censored.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEijO5yR6uCwFWPIGLqmnXSS75IDYR4QyEhRCRW9aKey3XjNMTymowqp1erq4Gqcn7CrY3ABBHrZkzuzwVIeW4tTTl7YPeqi75v70jyCabaOPkJb5Ur35oHXr8gp9C2UkwdaMi-3qtafulHk0JZBrFuvmyewzqcuC9SeFDbWUzKdRrZY7vkw3b4/s1640/Screenshot%202023-01-30%20at%2011.56.24_censored.jpg)

Trovare queste perle non è difficile. Esistono motori di ricerca appositi,
come [Shodan](https://www.shodan.io), che ho citato tante volte qui
e che fanno la stessa cosa che fa Google, ossia esplorano e catalogano tutta
Internet, e prendono nota dei siti che hanno degli accessi non protetti. È
sufficiente sfogliare uno di questi motori di ricerca per trovare di tutto:
telecamere di sorveglianza accessibili, server leggibili e scrivibili da
chiunque, e pagine Web come questa. Esattamente come con Google, è sufficiente
immettere le parole chiave giuste.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgb5dVMQOqERLKzxhQulB5TFNINFDDhd5x19bxFAwtfctwpGsGshPJEfMk3nfUkUe8_HoR7OpDiEKGehrnSdXVZMyRT6_agBUisQ8X89MK9iChvvO8c64FxQrsFIVBhpvetRCtQkj-pwPVCQ_7mpDqbldHnAIeqAI3m4RbILDEwvqXi2HL98_g/w640-h368/Screenshot%202023-01-30%20at%2011.49.31%20crop_censored.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgb5dVMQOqERLKzxhQulB5TFNINFDDhd5x19bxFAwtfctwpGsGshPJEfMk3nfUkUe8_HoR7OpDiEKGehrnSdXVZMyRT6_agBUisQ8X89MK9iChvvO8c64FxQrsFIVBhpvetRCtQkj-pwPVCQ_7mpDqbldHnAIeqAI3m4RbILDEwvqXi2HL98_g/s1634/Screenshot%202023-01-30%20at%2011.49.31%20crop_censored.jpg)

E a proposito di Google, molto spesso questi siti vulnerabili sono catalogati
anche da Google, appunto, anche se trovarli in questo modo richiede molta più
fatica. Infatti nel caso che mi è stato segnalato, il sito contenente
l’archivio di dati personali di assicurati italiani è non solo reperibile in
Google ma è anche nella sua *cache*, ossia nella copia temporanea che
Google fa di tutti i siti che visita. Questo vuol dire che i dati saranno
accessibili, almeno in parte, anche per qualche tempo dopo che il sito
lasciato incautamente aperto sarà stato finalmente messo in sicurezza.

Qualche giorno fa ho contattato via mail quella che credo sia la ditta
responsabile, la cui identità è trovabile frugando pazientemente in dettaglio nei dati e
documenti pubblicamente accessibili. Mentre attendevo la risposta, ho notato
che l’archivio non risultava più pubblicamente accessibile via Internet, anche
se la copia cache è tuttora presente in Google. Probabilmente l’avviso
lasciato in bella vista ha attirato positivamente l’attenzione dei
responsabili del sito. Non è una soluzione elegante, ma perlomeno è efficace.

Finora non ho ricevuto nessuna risposta formale dalla ditta in questione, ma mi è arrivato un messaggio Telegram di qualcuno che sembra parlare a nome di questa ditta e dice che si tratta di *“una versione alfa non in produzione”* che contiene *“dati totalmente fittizi anche se costruiti coerentemente”*. Non ho modo di verificare questa dichiarazione e posso solo sperare che la versione definitiva sia un po’ meno accessibile e disinvoltamente scrivibile di questa, perché provare un database lasciandolo aperto a tutti su Internet, in modo che possa essere riscritto, cancellato o devastato dal primo vandalo che passa, non è comunque una buona prassi di sicurezza informatica.

Pubblicazione iniziale:
[30.1.23](https://attivissimo.blogspot.com/2023/01/poi-la-gente-si-chiede-come-mai-i-dati.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/7421441/6703382007536819376 "Post per email")

Labels:
[dati a spasso](https://attivissimo.blogspot.com/search/label/dati%20a%20spasso),
[disastri informatici](https://attivissimo.blogspot.com/search/label/disastri%20informatici),
[privacy](https://attivissimo.blogspot.com/search/label/privacy),
[sicurezza informatica](https://attivissimo.blogspot.com/search/label/sicurezza%20informatica)

#### Nessun commento:

[Posta un commento](https://www.blogger.com/comment/fullpage/post/7421441/6703382007536819376)

[Post più recente](https://attivissimo.blogspot.com/2023/01/capelli-da-record-nello-spazio.html "Post più recente")

[Post più vecchio](https://attivissimo.blogspot.com/2023/01/podcast-rsi-spam-in-latino-spam-su.html "Post più vecchio")
[Home page](https://attivissimo.blogspot.com/)

Iscriviti a:
[Commenti sul post (Atom)](https://attivissimo.blogspot.com/feeds/6703382007536819376/comments/default)

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

[Gli altri miei libri](https://attivi...