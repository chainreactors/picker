---
title: Non mettete regole troppo complesse alle vostre password
url: https://codiceinsicuro.it/2022/04/16/non-mettete-regole-troppo-complesse-alle-vostre-password/
source: Over Security - Cybersecurity news aggregator
date: 2022-12-17
fetch_date: 2025-10-04T01:48:04.549288
---

# Non mettete regole troppo complesse alle vostre password

[![Codice Insicuro](https://codiceinsicuro.it/assets/images/logo.png)](https://codiceinsicuro.it/)

* [Blog](https://codiceinsicuro.it/index.html)
* [About](https://codiceinsicuro.it/about)
* [Chi sono](https://codiceinsicuro.it/chi-sono/)
* [Talks](https://codiceinsicuro.it/talks/)
* [Contatti](https://codiceinsicuro.it/contatti)

Share

##### Iscriviti alla mailing list

Basta la tua email

![Paolo Perego](https://www.gravatar.com/avatar/d05560cd673cf2f4114012616fd57c33?s=250&d=mm&r=x)

[Paolo Perego](https://codiceinsicuro.it)[Follow](https://twitter.com/thesp0nge)
Specialista di sicurezza applicativa e certificato OSCE e OSCP, amo spaccare e ricostruire il codice in maniera sicura. Sono cintura nera di taekwon-do, marito e papà. Ranger Caotico Neutrale, scrivo su @codiceinsicuro.

# Non mettete regole troppo complesse alle vostre password

833
parole -  Lo leggerai in 4 minuti

---

Questa mattina, godendomi un sole caldo che ha sicuramente dato il buongiorno, ho letto questo tweet all’interno del mio feed.

> 2022. Sito di grandissima azienda privata che gestisce molti dati personali. [pic.twitter.com/i4Xy2H0XgI](https://t.co/i4Xy2H0XgI)
>
> — Federico Maggi (@phretor) [April 15, 2022](https://twitter.com/phretor/status/1514875162444931073?ref_src=twsrc%5Etfw)

La form del cambio password di questo sito, lamenta un’eccessiva lunghezza della password scelta dall’utente. Fermiamoci un attimo e ripetiamolo **molto** lentamente: la password che l’utente ha scelto è troppo lunga.

Le chance che quella password veleggi verso una memorizzazione in chiaro sono molto alte. Altrimenti, perché lamentarsi della lunghezza?

## La lunghezza e l’hash

In linguaggi come Java, C# o PHP, la gestione delle stringhe di testo è molto evoluta e quindi non è sicuramente una scelta per evitare un buffer overflow. Compito dell’interprete è quello di allocare dinamicamente la memoria in modo tale da evitare pattern molto più comuni in sorgenti scritti in linguaggio C.

Se si vuole memorizzare nel database, l’hash SHA256 della password, memorizzando la rappresentazione in caratteri esadecimali del risultato della funzione, ci servono 64 caratteri, se non ho sbagliato i conti. **Sessantaquattro**. La cosa importante, da tenere in considerazione è che questa dimensione è indipendente dalla lunghezza dell’input. Quindi, una password di 3 caratteri, una passphrase di 20 caratteri o il capitolo di un libro, quando dati in pasto ad una funzione SHA256 restituiranno una stringa di 64 caratteri. Potenza e mistero delle funzioni di hashing.

Se non ci credete, compito per casa è verificarlo voi stessi.

## Complessità, caratteri speciali e usabilità

Alzi la mano chi ama mettere una password complessa come `Rdaj£25!PdaDD21$` ? A nessuno, neanche agli esperti di sicurezza informatica, figuriamoci all’utente comune. Ora alzi la mano chi ama dover scegliere una password che soddisfi tante regole di complessità, ogni 3 mesi?

Pensate all’utente comune, quello che di solito viene preso come target in campagne mirate o che di solito clicca il link con l’immagine del gattino. Un utente con una buona dose di consapevolezza, ma che di mestiere fa altro e che non può ricordarsi codici senza un nesso logico che cambiano ogni 3 mesi.

Come persone che parlano di sicurezza applicativa a sviluppatori, dobbiamo renderci conto che abbiamo una grossa responsabilità. I nostri consigli devono essere fattibili, devono venire incontro all’utente e non devono essere onerosi da sviluppare.

Un codice troppo complesso da sviluppare, probabilmente conterrà errori e vulnerabilità oppure, cosa molto più probabile richiederà troppo tempo per essere realizzato e quindi al team di sviluppo, sarà chiesto di rilassare alcuni, se non tutti, dei vincoli che abbiamo dato loro.

Un set di regole troppo complesse, porterà l’utente finale scegliere una password come `Rdaj£25!PdaDD21$`1, scriverla su un foglietto e ogni tre mesi cambiare l’ultima cifra. Aggiungere un controllo sulla similarità della password aiuterebbe? No, inasprirebbe ancora di più l’utente e non è nostro interesse, né avere utenti scontenti, né bloccare la gente sulla password di accesso.

## Frasi, usiamo le frasi

Ne parlavo [circa cinque anni fa](https://codiceinsicuro.it/2017/03/13/entropia-password-e-passphrase/): la soluzione al problema di dare un segreto che sia semplice da ricordare ad un utente è quello di permettergli di scegliere qualcosa che il cervello memorizza in maniera semplice. Esclusi numeri e date, quello che siamo bravi a ricordare sono le frasi.

Il verso di una canzone o di una poesia, una frase di senso compiuto, una frase che ci siamo inventati, sono ottimi esempi di password:

* computazionalmente robuste
* resistenti ad un attacco basato su dizionario
* resistenti ad un attacco di password guessing a forza bruta

Perché quindi non permettere una password come “Il colore della mia stanza è blu”? Ho provato a pensare a motivazioni tecniche, problemi di encoding, problemi con la gestione degli spazi e, **giuro**, non mi è venuto in mente nulla di sensato.

Nel caso non avessi visto qualcosa di macroscopico, lasciami un commento. Sono proprio curioso di capire e magari di aiutarti a trovare una soluzione.

## Off by one

Perché reinventare la ruota? In un’epoca basata sui micro servizi, perché non creare un’API che sia un po’ flessibile e che possa essere utilizzata per il blocco “autenticazione”? Certo, magari la realtà X ha bisogno di una customizzazione particolare, in quel caso può usare questo mattoncino come base su cui partire.

Bene, oggi ho creato [questo repository](https://github.com/thesp0nge/deadly-simple-login-api). Sto pensando ad un’API scritta in Java, eseguita all’interno di un container, con un database configurabile e di default basato su SQLite3.

Questa API avrà le funzionalità di login, logout e cambio password e penso sarà solo il middleware in maniera tale che ognuno possa personalizzare le pagine come più gli aggrada. Anche il database ovviamente sarà personalizzabile via JDBC.

L’idea è levarsi dalle scatole quel set di regole complessità assurde che spesso sono chieste in fumosi documenti di compliance, scritti da persone che magari non hanno la minima idea del problema e che pensano veramente che “2 maiuscole, 3 numeri e 4 caratteri speciali” rendano una password più sicura, ottenendo in cambio l’ennesimo post-it attaccato al monitor.

Enjoy it!

16 Apr 2022
(Updated: Dec 16, 2022)

* [Riflessioni](/categories#Riflessioni)

* [#complessità](/tags#complessità)
* [#gdpr](/tags#gdpr)
* [#password](/tags#password)

Vuoi aiutarmi a portare avanti il progetto [Codice Insicuro](https://codiceinsicuro.it) con una donazione?
Fantastico, allora non ti basta che premere il pulsante qui sotto.

[Supporta il progetto](https://www.buymeacoffee.com/thesp0nge)

---

[« E se la soluzione al problema dell’antivirus fosse avere il codice open?](https://codiceinsicuro.it/2022/04/04/e-se-il-problema-dell-antivirus-fosse-avere-il-codice-open/)
[Password vs Passphrase: la cracking challenge »](https://codiceinsicuro.it/2022/04/21/password-vs-passphrase-la-cracking-challenge/)

---

### Simili a "Non mettete regole troppo complesse alle vostre password"

Se questo post ti è piaciuto, sono abbastanza sicuro che troverai questi contenuti altrettanto interessanti. Buona lettura.

![](https://codiceinsicuro.it/assets/images/)

##### Password vs Passphrase: la cracking challenge

Password cracking challenge: 5 hash da rompere (2 password e 3 passphrase). Quale hash resisterà più a lungo?

[Continua la lettura](/2022/04/21/password-vs-passphrase-la-cracking-challenge/)

![](https://codiceinsicuro.it/assets/images/red_signals.jpg)

##### Ecco come scegliere una password robusta

Oggi stavo scegliendo una playlist per il lavoro ed arrivo ad un video dal
titolo molto **bold**: Come creare una password robusta.

[Continua la lettura](/blog/ecco-come-scegliere-una-password-robusta/)

![](https://codiceinsicuro.it/assets/images/pa...