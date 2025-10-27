---
title: BlueBleed, a spasso i dati privati di oltre 150.000 organizzazioni grazie ai cloud malconfigurati
url: http://attivissimo.blogspot.com/2022/10/bluebleed-spasso-i-dati-privati-di.html
source: Il Disinformatico
date: 2022-10-22
fetch_date: 2025-10-03T20:38:13.912772
---

# BlueBleed, a spasso i dati privati di oltre 150.000 organizzazioni grazie ai cloud malconfigurati

# [Il Disinformatico](https://attivissimo.blogspot.com/)

Un blog di Paolo Attivissimo, giornalista informatico e cacciatore di bufale

**Informativa privacy e cookie:** Questo blog include cookie di terze parti. Non miei ([dettagli](https://tinyurl.com/2p9apfu5))

[Prossimi eventi pubblici](https://attivissimo.me/disinformaticalendario/prossimi/) – [Donazioni](https://attivissimo.me/donazioni/) – [Sci-Fi Universe](https://scifiuniverse.it)

## Cerca nel blog

|  |  |
| --- | --- |
|  |  |

## 2022/10/21

### BlueBleed, a spasso i dati privati di oltre 150.000 organizzazioni grazie ai *cloud* malconfigurati

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgaDiKMN48lXld5h1M9PWFCwVWjqnB0s4hMjiJPvyKZQgteekwONYXopb6NFQmw6g7uOX3lLrlz93vAUcTv1uHxeVQtBpdDljn0w2H0jHOraW7yeTuJVuIYdXFcJEcOagLuYDqwoK1w73vs2ea4UXN-Ktu0pUjZVIpMqKhhyPap3BFR4ogP2I8/s320/Screen%20Shot%202022-10-20%20at%2011.10.21.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgaDiKMN48lXld5h1M9PWFCwVWjqnB0s4hMjiJPvyKZQgteekwONYXopb6NFQmw6g7uOX3lLrlz93vAUcTv1uHxeVQtBpdDljn0w2H0jHOraW7yeTuJVuIYdXFcJEcOagLuYDqwoK1w73vs2ea4UXN-Ktu0pUjZVIpMqKhhyPap3BFR4ogP2I8/s1507/Screen%20Shot%202022-10-20%20at%2011.10.21.png)

*Questo articolo è disponibile anche in
[versione podcast audio](https://attivissimo.blogspot.com/2022/10/podcast-rsi-zuckerberg-vuole-sapere.html).*

Il 19 ottobre scorso Microsoft ha
[annunciato](https://msrc-blog.microsoft.com/2022/10/19/investigation-regarding-misconfigured-microsoft-storage-location-2/)
che i dati riservati di alcuni suoi clienti e potenziali clienti sono stati
resi pubblicamente accessibili via Internet a causa di un *suo* errore di
configurazione. I dati includono dettagli delle strutture aziendali, le
fatture, i listini prezzi, i dettagli dei progetti, i nomi e numeri di
telefono dei dipendenti e il contenuto delle loro mail.

L’azienda minimizza e nota che l’errore è stato corretto poco dopo la sua
segnalazione da parte della società di sicurezza informatica SOCRadar il 24
settembre scorso, ma
[alcuni](https://twitter.com/KiPos_info/status/1577745070941503488)
[esperti](https://twitter.com/GossiTheDog/status/1582819993263099905)
non sono altrettanto rassicuranti.

I dati sono stati infatti catalogati da siti come
[Grayhat Warfare](https://buckets.grayhatwarfare.com/) e come
avviene sempre in questi casi non c’è modo di sapere quanti malintenzionati
hanno avuto il tempo di procurarsene una copia.

> The Microsoft bucket has been publicly indexed for months, it's called
> olyympusv2 hosted on Azure blob storage - it was publicly readable. It's
> even in search engines.<https://t.co/5iBIb2qvue>
> [pic.twitter.com/5zjC0IC4wh](https://t.co/5zjC0IC4wh)
>
> — Kevin Beaumont (@GossiTheDog)
> [October 20, 2022](https://twitter.com/GossiTheDog/status/1583042989219139590?ref_src=twsrc%5Etfw)

Secondo l’[avviso pubblicato da SOCRadar](https://socradar.io/sensitive-data-of-65000-entities-in-111-countries-leaked-due-to-a-single-misconfigured-data-bucket/), il problema non riguarda soltanto Microsoft ma tocca anche Amazon e Google,
che hanno malconfigurato vari server contenenti dati sensibili dei propri
clienti aziendali.

SOCRadar ha raccolto le informazioni su queste violazioni di riservatezza in
un’[apposita pagina del proprio sito](https://socradar.io/labs/bluebleed), che consente di sapere se un’azienda è coinvolta o meno digitandone il nome
di dominio nella casella di ricerca, e ha dato alla vicenda il nome
*BlueBleed*.

In totale sono circa 150.000 le aziende interessate, che appartengono a 123
paesi. Le mail rese troppo visibili sono circa un milione e gli utenti sono
circa 800.000. Responsabilmente, SOCRadar non rivela i dati ma si limita a
dire se sono presenti o meno negli archivi resi eccessivamente accessibili dai
servizi *cloud* di Microsoft, Amazon e Google. Se la vostra azienda usa
servizi *cloud* di questi tre grandi nomi è opportuno dedicare un minuto
a un controllo per vedere se è fra quelle coinvolte.

Va ricordato che i dati ottenuti da fughe di questo genere vengono solitamente
utilizzati dai criminali online per ricatti ed estorsioni o per carpire
illecitamente la fiducia dei dipendenti di un’azienda presa di mira
manifestando di conoscere informazioni aziendali riservate, ma vengono anche a
volte semplicemente rivenduti al miglior offerente, per cui non è mai il caso
di ignorare segnalazioni di *cloud* colabrodo come questa.

---

**2022/10/27 8:45.** I *bucket* lasciati aperti non sono finiti:

> I found another of the MSFT Bluebleed buckets, with the SQL databases. Contains databases Datastore, WMIDataStore, Olympusv2Backup and Datawarehouse\_backup - has been kicking around for some time. [pic.twitter.com/s35dN0C7Sg](https://t.co/s35dN0C7Sg)
>
> — Kevin Beaumont (@GossiTheDog) [October 26, 2022](https://twitter.com/GossiTheDog/status/1585218199796482048?ref_src=twsrc%5Etfw)

*Fonte aggiuntiva:
[Bleeping Computer](https://www.bleepingcomputer.com/news/security/microsoft-data-breach-exposes-customers-contact-info-emails/), [Graham Cluley](https://grahamcluley.com/microsoft-bluebleed-data-breach-customer-details-and-email-content-exposed/).*

Pubblicazione iniziale:
[21.10.22](https://attivissimo.blogspot.com/2022/10/bluebleed-spasso-i-dati-privati-di.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/7421441/3798836300371229320 "Post per email")

Labels:
[Amazon](https://attivissimo.blogspot.com/search/label/Amazon),
[cloud](https://attivissimo.blogspot.com/search/label/cloud),
[falle di sicurezza](https://attivissimo.blogspot.com/search/label/falle%20di%20sicurezza),
[Google](https://attivissimo.blogspot.com/search/label/Google),
[Microsoft](https://attivissimo.blogspot.com/search/label/Microsoft),
[PodcastRSI](https://attivissimo.blogspot.com/search/label/PodcastRSI),
[radio](https://attivissimo.blogspot.com/search/label/radio)

#### Nessun commento:

[Posta un commento](https://www.blogger.com/comment/fullpage/post/7421441/3798836300371229320)

[Post più recente](https://attivissimo.blogspot.com/2022/10/le-parole-di-internet-fork-bomb.html "Post più recente")

[Post più vecchio](https://attivissimo.blogspot.com/2022/10/meta-quest-pro-sorveglia-dove-guardi.html "Post più vecchio")
[Home page](https://attivissimo.blogspot.com/)

Iscriviti a:
[Commenti sul post (Atom)](https://attivissimo.blogspot.com/feeds/3798836300371229320/comments/default)

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

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiwWo0VmlJW4KbR2KYCr10iEPHo1F2w37XMCsBe5YIHWIkZiTTkwcN6y_lIPVZN5bLGrtRczw_v5yBt1...