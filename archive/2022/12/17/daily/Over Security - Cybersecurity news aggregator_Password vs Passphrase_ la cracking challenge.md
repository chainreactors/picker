---
title: Password vs Passphrase: la cracking challenge
url: https://codiceinsicuro.it/2022/04/21/password-vs-passphrase-la-cracking-challenge/
source: Over Security - Cybersecurity news aggregator
date: 2022-12-17
fetch_date: 2025-10-04T01:48:05.484147
---

# Password vs Passphrase: la cracking challenge

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

# Password vs Passphrase: la cracking challenge

370
parole -  Lo leggerai in 2 minuti

---

Settimana scorsa [ho scritto un post](https://codiceinsicuro.it/2022/04/16/non-mettete-regole-troppo-complesse-alle-vostre-password/) che su LinkedIN ha creato una vivace discussione.

Come potete vedere, accanto a commenti mirati a promuovere il proprio blog o commenti mirati a provare a rivendere qualche tecnologia proprietaria, la questione su cosa sia meglio tra password e passphrase è dibattuta e non sembra esserci una visione comune.

Per provare a rendere la cosa più interessante, oggi sempre [su LinkedIN ho lanciato](https://www.linkedin.com/posts/paolo-perego_non-mettete-regole-troppo-complesse-alle-activity-6922927684033417216-yz2F?utm_source=linkedin_share&utm_medium=member_desktop_web) una #passwordcrackingchallenge che ripropongo anche qui.

Come algoritmo di hash ho scelto uno sha256 senza usare salt. Le hash sono state generate usando il comando:

```

```
$ echo -n "stringa" | sha256sum
```

</div>Come policy per la password ho scelto: almeno 1 maiuscola, almeno 1 numero, almeno un carattere speciale, almeno 8 caratteri mentre per la passphrase ho pescato solo dall’italiano, solo caratteri minuscoli tranne i nomi di persona che sono stati scritti secondo le regole della nostra grammatica, che spero conosciate.

Questi gli hash:

```

```
 021911e07fbd55e6480cc9127b6da3cd5a25f57dc47a14213d298dc06a082a4f (Password di 13 caratteri)
f3ddebd7a0379a6626c19c95a068c173734f910c6c32d14936f34ec9a33290d9 (Password di 9 caratteri)
a6fabf6238568215f9f00cc5caad69ec96e46b33fd88e5591fcb502aef58fd44 (Passphrase di 4 parole italiane (frase di senso compiuto))
8345147c1367174a397cfe1e0695871197dc66f7d3c5f6a865f9106a87a34b3e (Passphrase di 4 parole italiane (frase non di senso compiuto))
7791a9337f4fcc36499a7ec123ef3d4c55b94fc1ffcacfc08d9fc1022d8f39e7 (Passphrase di 11 parole italiane (frase di senso compiuto, presa da una canzone))

```

</div>La sfida è, entro il 31 dicembre 2022, vedere quanti hash hanno resistito. Siete liberi di usare qualsiasi mezzo a vostra disposizione.

Mentre scrivevo questo post ho preso una decina di minuti per accompagnare mia figlia a danza e la [prima hash è già caduta](https://www.linkedin.com/feed/update/urn:li:activity:6922927684033417216?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A6922927684033417216%2C6922939189579628544%29):

```

```
f3ddebd7a0379a6626c19c95a068c173734f910c6c32d14936f34ec9a33290d9: P4ssw0rd_
```

</div>## Off by one

Lo scopo di questa challenge non è tanto confrontare password e passphrase empiricamente. Il confronto, come vedete dalla hash che è stata trovata, è su segreti che l’utente medio sceglie per via della loro mnemonicità.

Io sono convinto che le passphrase siano una scelta migliore di una parola chiave con astrusi meccanismi di complessità; complessità che è solo per l’utente non certo per un elaboratore per il quale un carattere… è pur sempre un carattere.

Happy cracking!
```
```
```

21 Apr 2022
(Updated: Dec 16, 2022)

* [Exploit e dintorni](/categories#Exploit-e-dintorni)
* [Riflessioni](/categories#Riflessioni)

* [#gdpr](/tags#gdpr)
* [#passphrase](/tags#passphrase)
* [#password](/tags#password)
* [#password cracking](/tags#password-cracking)
* [#sha256](/tags#sha256)

Vuoi aiutarmi a portare avanti il progetto [Codice Insicuro](https://codiceinsicuro.it) con una donazione?
Fantastico, allora non ti basta che premere il pulsante qui sotto.

[Supporta il progetto](https://www.buymeacoffee.com/thesp0nge)

---

[« Non mettete regole troppo complesse alle vostre password](https://codiceinsicuro.it/2022/04/16/non-mettete-regole-troppo-complesse-alle-vostre-password/)
[Sono tutti open con il source degli altri – reprise »](https://codiceinsicuro.it/2022/05/10/sono-tutti-open-con-il-source-degli-altri-reprise/)

---

### Simili a "Password vs Passphrase: la cracking challenge"

Se questo post ti è piaciuto, sono abbastanza sicuro che troverai questi contenuti altrettanto interessanti. Buona lettura.

![](https://codiceinsicuro.it/assets/images/)

##### Non mettete regole troppo complesse alle vostre password

Perché non usare una frase al posto di una password? Lasciamoci alle spalle regole di complessità obsolete e abbracciamo l'usabilità con un occhio di riguardo alla sicurezza.

[Continua la lettura](/2022/04/16/non-mettete-regole-troppo-complesse-alle-vostre-password/)

![](https://codiceinsicuro.it/assets/images/lock.png)

##### Come salvare la password dei propri utenti e vivere sereni un data breach

Ok, nessuno vive serenamente un data breach però ci sono accorgimenti che
possono mitigare parzialmente un’intrusione nel nostro backend.

[Continua la lettura](/blog/come-salvare-la-password-dei-propri-utenti-e-vivere-sereni-un-data-breach/)

![](https://codiceinsicuro.it/assets/images/red_signals.jpg)

##### Ecco come scegliere una password robusta

Oggi stavo scegliendo una playlist per il lavoro ed arrivo ad un video dal
titolo molto **bold**: Come creare una password robusta.

[Continua la lettura](/blog/ecco-come-scegliere-una-password-robusta/)

Please enable JavaScript to view the [comments powered by Disqus.](http://disqus.com/?ref_noscript)
[comments powered by Disqus](http://disqus.com)

![Codice Insicuro, blog di Cyber Security, sviluppo sicuro, code review e altro.](https://codiceinsicuro.it/assets/images/logo.png)   Non perdere neanche un **post**, [iscriviti](https://mailchi.mp/f53e49d3060b/codice-insicuro) ora alla mailing list

## Esplora →

[attackers (4)](https://codiceinsicuro.it/categories#attackers)
[Pick'n'chic (4)](https://codiceinsicuro.it/categories#Pick'n'chic)
[builders (1)](https://codiceinsicuro.it/categories#builders)
[sicurina (2)](https://codiceinsicuro.it/categories#sicurina)
[meditazione (2)](https://codiceinsicuro.it/categories#meditazione)
[servizio (1)](https://codiceinsicuro.it/categories#servizio)
[Sicurina (10)](https://codiceinsicuro.it/categories#Sicurina)
[Chiacchiere da bar (44)](https://codiceinsicuro.it/categories#Chiacchiere-da-bar)
[Spinaci (7)](https://codiceinsicuro.it/categories#Spinaci)
[Under attack (16)](https://codiceinsicuro.it/categories#Under-attack)
[L'angolo del libro (1)](https://codiceinsicuro.it/categories#L'angolo-del-libro)
[Doctor is in (2)](https://codiceinsicuro.it/categories#Doctor-is-in)
[Meditazione (6)](https://codiceinsicuro.it/categories#Meditazione)
[under (3)](https://codiceinsicuro.it/categories#under)
[News (3)](https://codiceinsicuro.it/categories#News)
[chiacchiere da pub (1)](https://codiceinsicuro.it/categories#chiacchiere-da-pub)
[Post (1)](https://codiceinsicuro.it/categories#Post)
[post (66)](https://codiceinsicuro.it/categories#post)
[getting-root (7)](https://codiceinsicuro.it/categories#getting-root)
[offensive (1)](https://codiceinsicuro.it/categories#offensive)
[Storie dal quotidiano (3)](https://codiceinsicuro.it/categories#Storie-dal-quotidiano)
[sviluppo (1)](https://codiceinsicuro.it/categories#sviluppo)
[Riflessioni (5)](https://codiceinsicuro.it/categories#Riflessioni)
[Exploit e dintorni (1)](https://codiceinsicuro.it/categories#Exploit-e-dintorni)
[Progetti (1)](https://codiceinsicuro.it/categories#Progetti)

Cop...