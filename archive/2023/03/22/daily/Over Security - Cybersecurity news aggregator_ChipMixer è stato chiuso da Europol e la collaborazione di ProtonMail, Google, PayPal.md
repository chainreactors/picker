---
title: ChipMixer è stato chiuso da Europol e la collaborazione di ProtonMail, Google, PayPal
url: https://www.insicurezzadigitale.com/chipmixer-e-stato-chiuso-da-europol-e-la-collaborazione-di-protonmail-google-paypal/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-22
fetch_date: 2025-10-04T10:16:56.641539
---

# ChipMixer è stato chiuso da Europol e la collaborazione di ProtonMail, Google, PayPal

[(in)sicurezza digitale](https://insicurezzadigitale.com/)

* Incidenti e violazioni
  + [Roundup – Flash](https://insicurezzadigitale.com/category/roundup/)
  + [Incidenti e Violazioni](https://insicurezzadigitale.com/category/incidenti-e-violazioni/)
  + [Phishing](https://insicurezzadigitale.com/category/phishing/)
  + [Privacy](https://insicurezzadigitale.com/category/privacy/)
  + [Data Breach](https://insicurezzadigitale.com/category/data-breach/)
* [Ransomware](https://insicurezzadigitale.com/category/ransomware/)
* [Malware e Vulnerabilità](https://insicurezzadigitale.com/category/malware-e-vulnerabilita/)
  + [Analisi](https://insicurezzadigitale.com/category/analisi/)
* [La stampa dice](https://insicurezzadigitale.com/la-stampa-dice/)
* Altro…
  + [Chi siamo](https://insicurezzadigitale.com/chi-siamo/)
  + [> Whistleblowing <](https://insicurezzadigitale.com/whistleblowing/)
  + [Eventi](https://insicurezzadigitale.com/category/eventi/)
  + [Editoriali di Dario Fadda](https://blogsicurezza.myblog.it/)
  + [Data Leaks list](https://insicurezzadigitale.com/data-leaks-list/)
  + [Archivio Cyber Security Notes](https://insicurezzadigitale.com/archivio-cyber-security-notes/)
  + [Archivio Malware samples](https://insicurezzadigitale.com/archivio-malware-samples/)
  + [Infosec Tools list](/tool)
* Il Network
  + [NINAsec – Newsletter](https://ninasec.substack.com/)
  + [Spcnet.it](https://www.spcnet.it)
  + [Ziobudda](https://www.ziobudda.org)
  + [ilGlobale.it](https://www.ilglobale.it)
  + [SecureBulletin.com](https://securebulletin.com/)
* [I Forums](https://forum.ransomfeed.it/)

[Incidenti e Violazioni](https://insicurezzadigitale.com/category/incidenti-e-violazioni/)

# ChipMixer è stato chiuso da Europol e la collaborazione di ProtonMail, Google, PayPal

![](https://secure.gravatar.com/avatar/0706373a7341ff1dd0bc60952232b77edfc2fcce715f4397e0ecab569e94cfc0?s=48&d=mm&r=g)

Dario Fadda
21 Marzo 2023

![](https://insicurezzadigitale.com/wp-content/uploads/2023/03/Screenshot_2023-03-21_14_14_34-1024x610.png)

L’FBI, insieme ad Europol e altre sette autorità statali tra cui Svizzera e Germania, hanno messo sotto i ferri una piattaforma illegale, attiva dal 2017.

Non si tratta di una notizia perché i fatti di questo post si riferiscono al 14 marzo, ad ogni modo è utile evidenziare come si sia arrivati a questo risultato, mediante collaborazione attiva di colossi quali PayPal, ProtonMail e scarsa conoscenza dell’OPSEC per gli amministratori della piattaforma. Portando così all’**arresto dell’infrastruttura per il suo presunto coinvolgimento in attività di riciclaggio** di denaro e sequestrato quattro server, circa 1.909,4 Bitcoin in 55 transazioni (circa 44,2 milioni di euro) e 7 TB di dati.

La piattaforma ha permesso di riciclare denaro conseguito da attività illecite in criptovaluta, mascherandone il tracciamento per anni, che sono stati successivamente ritirati per ripulire gli indirizzi crittografici per un ulteriore prelievo in valuta forte. In poche parole, una lavanderia a gettoni per criminali informatici senza riserve sulla legalità.

Europol ha affermato che **ChipMixer ha contribuito a nascondere le tracce di denaro digitale per trafficanti di droga online, hacker militari russi e criminali informatici nordcoreani**. In tal modo, il mixer ha facilitato il riciclaggio di denaro di 152.000 Bitcoin.

LockBit, Dharma, Suncrypt e altri ransomware hanno riciclato denaro tramite ChipMixer. Oltre a spacciatori, contrabbandieri, pedofili e ladri di criptovalute.

Il [Dipartimento di Giustizia USA (DOJ)](https://www.justice.gov/opa/pr/justice-department-investigation-leads-takedown-darknet-cryptocurrency-mixer-processed-over-3) ha annunciato di aver incriminato **Minh Quoc Nguyen**, un cittadino vietnamita di Hanoi. Il presunto proprietario della piattaforma, di 49 anni è accusato di riciclaggio di denaro commerciale, gestione di un’attività di trasferimento di denaro senza licenza e anche furto di identità in relazione all’operazione di ChipMixer. Attualmente è [ricercato](https://www.fbi.gov/wanted/cyber/minh-quoc-nguyen) dall’FBI.

Nguyen ha utilizzato, nel corso degli anni, molti provider di posta elettronica clearnet e indirettamente ha utilizzato il proprio account PayPal per pagare i server, con i quali gestiva la piattaforma.

[![](https://www.insicurezzadigitale.com/wp-content/uploads/2023/03/linked.png)](https://www.insicurezzadigitale.com/wp-content/uploads/2023/03/linked.png)

Ecco gli account PayPal a lui associati, utilizzati per pagare il server:

[![](https://www.insicurezzadigitale.com/wp-content/uploads/2023/03/paypal.png)](https://www.insicurezzadigitale.com/wp-content/uploads/2023/03/paypal.png)

Dall’[atto giudiziario](https://www.justice.gov/opa/press-release/file/1574581/download) depositato, si legge che

```
La ricerca open source condotta sugli account di cui sopra ha rivelato che le informazioni identificative associate agli account sono principalmente persone con sede negli Stati Uniti, di circa 60-70 anni, ad eccezione dell'account associato a MINH NGUYEN. La ricerca in un database commerciale ha rivelato che alcune di queste persone sono decedute.

Secondo i registri PayPal per l'account PayPal V3 (l'account che paga per il server), il 27 dicembre 2022 è stato ricevuto un pagamento con carta di credito da MINH NGUYEN, indirizzo e-mail nqminh73@yahoo.com per $ 150,00 con il commento "Grazie."
```

L’FBI ha trovato transazioni con 70 diversi conti PayPal utilizzando gli indirizzi ProtonMail quando hanno scavato più a fondo nei conti PayPal di cui sopra. **Hanno quindi inviato richieste di record internazionali per i dati degli abbonati per questi account ProtonMail**. Di questi account, 24 hanno indicato jamessmithhelp@gmail.com come indirizzo email di recupero e 9 hanno indicato minhoba@ymail.com come indirizzo email di recupero.

Inoltre si evince anche la **collaborazione di Google** su tale operazione

```
I record di Google per l'account jamessmithhelp@gmail.com hanno rivelato i dati della cronologia delle posizioni. Da settembre 2016 a marzo 2022, sono stati associati 149.027 punti dati all'account che si è risolto a Ha Noi, in Vietnam, e dintorni. I dati della cronologia delle posizioni sono una combinazione di diverse fonti che includono cellulare, GPS e Wi-Fi, a dimostrazione del fatto che NGUYEN era fisicamente in Vietnam durante queste interrogazioni.
```

Tramite mandato di perquisizione Google ha restituito, per l’account jamessmithhelp@gmail.com, le ricerche di Nguyen sui modi per acquistare informazioni di identificazione personale. Sono state effettuate le seguenti ricerche su Google da tale account:

* “dove cercare ssn gratis per nome”
* “vendere ssn dob”
* “negozio ssn dob”
* “generatore di numeri ssn”

Insomma, in questa operazione possiamo sicuramente evidenziare come si sia mosso incautamente, anche il sospettato, dando per fortuna la possibilità alle autorità di venir rintracciato e perseguito. Una serie di leggerezze cyber che potrebbero costarci circa 40 anni di carcere.

##### < tags />

[chipmixer](https://insicurezzadigitale.com/tag/chipmixer/)[crypto](https://insicurezzadigitale.com/tag/crypto/)[infosec](https://insicurezzadigitale.com/tag/infosec/)

##### < condividi />

[Twitter](https://twitter.com/intent/tweet?text=ChipMixer+%C3%A8+stato+chiuso+da+Europol+e+la+collaborazione+di+ProtonMail%2C+Google%2C+PayPal&url=https://insicurezzadigitale.com/chipmixer-e-stato-chiuso-da-europol-e-la-collaborazione-di-protonmail-google-paypal/)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https://insicurezzadigitale.com/chipmixer-e-stato-chiuso-da-europol-e-la-collaborazione-di-protonmail-google-paypal/)
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://insicurezzadigitale.com/chipmixer-e-stato-chiuso-da-europol-e-la-collaborazione-di-protonmail-google-paypal/&title=ChipMixer+%C3%A8+stato+chiuso+da+Europol+e+la+collaborazione+di+ProtonMail%2C+Google%2C+PayPal)

[== a...