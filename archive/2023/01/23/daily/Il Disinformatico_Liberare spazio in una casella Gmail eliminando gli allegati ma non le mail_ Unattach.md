---
title: Liberare spazio in una casella Gmail eliminando gli allegati ma non le mail: Unattach
url: http://attivissimo.blogspot.com/2023/01/liberare-spazio-in-una-casella-gmail.html
source: Il Disinformatico
date: 2023-01-23
fetch_date: 2025-10-04T04:36:18.187492
---

# Liberare spazio in una casella Gmail eliminando gli allegati ma non le mail: Unattach

# [Il Disinformatico](https://attivissimo.blogspot.com/)

Un blog di Paolo Attivissimo, giornalista informatico e cacciatore di bufale

**Informativa privacy e cookie:** Questo blog include cookie di terze parti. Non miei ([dettagli](https://tinyurl.com/2p9apfu5))

[Prossimi eventi pubblici](https://attivissimo.me/disinformaticalendario/prossimi/) – [Donazioni](https://attivissimo.me/donazioni/) – [Sci-Fi Universe](https://scifiuniverse.it)

## Cerca nel blog

|  |  |
| --- | --- |
|  |  |

## 2023/01/22

### Liberare spazio in una casella Gmail eliminando gli allegati ma non le mail: Unattach

Le caselle gratuite di Gmail sono capienti già nella versione base gratuita (attualmente offrono circa 15 GB) e aumentarne le
dimensioni pagando non è difficile. Ma se ricevete o mandate tanti allegati,
noterete che riempiono molto spazio. È facile dimenticarsi che un singolo
allegato da 10 MB equivale a circa 10.000 mail, in termini di spazio occupato
(presumendo che una mail di solo testo occupi mediamente 1 KB).

La soluzione semplice è cancellare le mail che contengono allegati pesanti che
non vi servono più: è possibile elencarle andando in Gmail e digitando nella
casella di ricerca

*has:attachment larger:[dimensioni]*

Per esempio,

*has:attachment larger:10M*

elenca tutte le mail che hanno un allegato di dimensioni superiori ai 10
MB.

Questo filtro può essere affinato ulteriormente, per esempio specificando un
mittente se avete qualcuno che vi manda tanti allegati che dopo qualche tempo
non vi serve più avere in archivio nella mail. Per esempio,

*has:attachment larger:1M from:pippo@pippo-e-pluto.com older\_than:1y*

elenca tutte le mail con allegato grande almeno 1 MB che avete ricevuto da
*pippo@pippo-e-pluto.com* almeno un anno fa. L’[elenco completo degli operatori di Gmail](https://support.google.com/mail/answer/7190?hl=it)
offre molte altre opzioni.

---

Questo metodo, però, ha il difetto che elimina non solo l’allegato ma anche la
mail associata all’allegato. Se avete bisogno di conservare la mail, che è
leggera, ma non il suo ingombrante allegato, per esempio per tenere traccia di
comunicazioni di lavoro, in Gmail non c’è modo di farlo. Alcuni client, come
per esempio Thunderbird, offrono quest’opzione, da applicare manualmente alle singole mail, ma Gmail no.

Una soluzione è la web app [Unattach](https://unattach.app/), che
consente appunto di eliminare gli allegati lasciando però intatte le mail
corrispondenti; l’allegato viene sostituito da una nota, in calce alla mail,
che descrive l’allegato rimosso.

Per usare Unattach, che è gratuita nella versione limitata a 30 mail/mese e
costa 10 euro/dollari/franchi l’anno nella versione *Basic* che non ha
questo limite, si va a *https://unattach.app* e si clicca su
*Get Started* o su *Try with our free plan*, poi si clicca su
*Sign up with Google* (oppure si crea un account con mail e password), si
accetta la richiesta di collegare il proprio account Gmail a Unattach (è un
permesso revocabile), si accettano le condizioni d’uso e l’[informativa sulla privacy](https://unattach.app/privacy-policy)
e si clicca su *Start Unattach*.

Fatto questo, si clicca su *Sign in to Gmail* per dare gli ulteriori
consensi (Unattach deve poter leggere e scrivere nell’account di posta) e si
può cominciare.

Nella scheda *Basic search* si può fare una ricerca semplice, basata
sulle dimensioni degli allegati: compare un elenco delle mail che soddisfano
il criterio, ordinabile per dimensioni, data, mittente e oggetto.

Nella scheda *Advanced search*, invece, si possono immettere gli stessi
operatori che si possono usare in Gmail, e quindi per esempio si possono
cercare le mail che hanno allegati e sono state inviate da uno specifico
mittente prima di una certa data.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhSTQzJGUd7b1fjJlTShnOt_Iy7cN6PWQdp0K42m0vQgRqZB8Kt-00VaQSwaJhNxCk_1jzAXo92QKIwJxr2urJ0NaZ-MjJAf0jIH3xNvfO89V6JzG21VcS6gVQ_hoiMfHvTwAjOOkL2igZU-UwUHlUqASnTt6Nkaa6S7hAqTVnlBTYm3MAJcyM/s16000/Screenshot%202023-01-22%20at%2020.51.49_censored.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhSTQzJGUd7b1fjJlTShnOt_Iy7cN6PWQdp0K42m0vQgRqZB8Kt-00VaQSwaJhNxCk_1jzAXo92QKIwJxr2urJ0NaZ-MjJAf0jIH3xNvfO89V6JzG21VcS6gVQ_hoiMfHvTwAjOOkL2igZU-UwUHlUqASnTt6Nkaa6S7hAqTVnlBTYm3MAJcyM/s1048/Screenshot%202023-01-22%20at%2020.51.49_censored.jpg)

Si può scegliere di cancellare la mail, scaricare gli allegati, rimuoverli o
ridurne le dimensioni se sono immagini. Fatto questo, si selezionano le mail
che interessano, si clicca su *Process Selected Emails*, e il gioco è
fatto. Nel mio caso ho 2265 mail con allegati risalenti a più di due anni fa
provenienti da un singolo cliente; ho già salvato in archivio gli allegati e
quindi non mi serve tenerli nella casella di mail. Eliminarli mi libererà
quasi 3 GB di spazio su Gmail, dopo che avrò vuotato il Cestino di Gmail (andando a *https://mail.google.com/mail/u/0/#trash*).

Le mail alle quali è stato rimosso l’allegato ora hanno in calce un avviso se le apro in Gmail:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZmFdKchT7_3qTduTv7hcM1VHpN6Prx4GdgC6q3d2Jg1XKKzVpxyNq3QJis-vw_GaI6e6POPgWIUKcmMVD-u40y6sUMFAcaGXCcXC5u5yJwc-ZXFns1JfPpfUVAtGqx3hT9nfQ5810p8b5o2rZQcgbIL-8f9nnTVKdK0QqRM8MwejCHEHMmNk/s320/Screenshot%202023-01-22%20at%2021.08.02_censored.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZmFdKchT7_3qTduTv7hcM1VHpN6Prx4GdgC6q3d2Jg1XKKzVpxyNq3QJis-vw_GaI6e6POPgWIUKcmMVD-u40y6sUMFAcaGXCcXC5u5yJwc-ZXFns1JfPpfUVAtGqx3hT9nfQ5810p8b5o2rZQcgbIL-8f9nnTVKdK0QqRM8MwejCHEHMmNk/s340/Screenshot%202023-01-22%20at%2021.08.02_censored.jpg)

Se usate (anche) un client di posta in IMAP, come me, la modifica ci metterà un po’ ad arrivare anche alla copia locale delle mail. E ovviamente l’eliminazione degli allegati riduce anche lo spazio occupato sul disco locale dalla mail.

La spiegazione del metodo usato da Unattach è fornita in [questo articolo](https://blog.unattach.app/2022/07/how-to-delete-gmail-attachments.html), che sottolinea che Unattach è una web app che gira localmente nel browser dell’utente e usa le API di Google per accedere alla mail dell’utente; le mail non vengono mandate agli sviluppatori di Unattach o ad altri, come descritto nell’[informativa sulla privacy](https://unattach.app/privacy-policy). Questo, però, significa che l’app non è un fulmine: eliminare qualche migliaio di allegati richiede un’oretta abbondante.

Passare alla versione a pagamento è facile: si può pagare con PayPal o con le principali carte di credito.

Pubblicazione iniziale:
[22.1.23](https://attivissimo.blogspot.com/2023/01/liberare-spazio-in-una-casella-gmail.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/7421441/6768170213878033839 "Post per email")

Labels:
[Gmail](https://attivissimo.blogspot.com/search/label/Gmail),
[Google](https://attivissimo.blogspot.com/search/label/Google),
[mail](https://attivissimo.blogspot.com/search/label/mail)

#### Nessun commento:

[Posta un commento](https://www.blogger.com/comment/fullpage/post/7421441/6768170213878033839)

[Post più recente](https://attivissimo.blogspot.com/2023/01/lo-strano-caso-dello-spam-in-latino.html "Post più recente")

[Post più vecchio](https://attivissimo.blogspot.com/2023/01/tesla-il-video-di-guida-autonoma-del.html "Post più vecchio")
[Home page](https://attivissimo.blogspot.com/)

Iscriviti a:
[Commenti sul post (Atom)](https://attivissimo.blogspot.com/feeds/6768170213878033839/comments/default)

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
Shqipta...