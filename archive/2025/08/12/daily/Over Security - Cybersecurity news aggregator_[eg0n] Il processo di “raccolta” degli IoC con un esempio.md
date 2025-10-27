---
title: [eg0n] Il processo di “raccolta” degli IoC con un esempio
url: https://roccosicilia.com/2025/08/11/eg0n-il-processo-di-raccolta-degli-ioc-con-un-esempio/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-12
fetch_date: 2025-10-07T00:49:53.087134
---

# [eg0n] Il processo di “raccolta” degli IoC con un esempio

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/progetto-di-divulgazione/)
* [Sostieni il progetto](https://roccosicilia.com/sostieni-il-progetto/)
* [English version](https://medium.com/%40roccosicilia)

[cyber security](https://roccosicilia.com/category/cyber-security/), [hacking](https://roccosicilia.com/category/hacking/), [ita](https://roccosicilia.com/category/ita/)

## [[eg0n] Il processo di “raccolta” degli IoC con un esempio](https://roccosicilia.com/2025/08/11/eg0n-il-processo-di-raccolta-degli-ioc-con-un-esempio/)

Published by

Rocco Sicilia

on

[11 agosto 2025](https://roccosicilia.com/2025/08/11/eg0n-il-processo-di-raccolta-degli-ioc-con-un-esempio/)

[![[eg0n] Il processo di “raccolta” degli IoC con un esempio](https://roccosicilia.com/wp-content/uploads/2025/08/parlo-di-ioc-e-threat-intelligence-fai-una-cosa-semplice-1.png?w=1024)](https://roccosicilia.com/2025/08/11/eg0n-il-processo-di-raccolta-degli-ioc-con-un-esempio/)

Questo post è una serie di riflessioni a *voce alta* legata al progetto [eg0n](https://github.com/b1th0rn/eg0n).

Uno degli obiettivi di base a cui non vogliamo/voglio rinunciare è arrivare a generare delle liste di IoC immediatamente consumabili dai sistemi di detection/protection come Firewall, IDS, EDR e tutte le soluzioni a cui affidate la sicurezza della vostra rete. Questo risultato richiede dei passaggi sui cui stiamo ragionando assieme e che probabilmente rivedremo nel corso del progetto.

Abbiamo affiancato ad **eg0n** una istanza **MISP** – <https://misp.bithorn.org> – per mettere a disposizione della community uno strumento che è oggi considerato uno standard per quanto riguarda la raccolta e l’analisi degli IoC. MISP è un software molto utile ma con tante limitazioni (ne ho parlato recentemente in un video che vi riporto qui sotto) e non poteva essere lo strumento definitivo per il progetto.

Il video fatto in collaborazione con @esadecimale

La raccolta può avvenire in diversi modi, quelli di cui possiamo disporre a T0 sono i dati forniti dagli analisti che partecipano al progetto ed i dati forniti tramite gli honeypot. Con questo set di base di informazioni è possibile portare sull’istanza MISP l’analisi di eventi legati ad azioni di Threat Actor con i relativi artefatti individuati. In questo processo la cura per il dettaglio deve essere maniacale: più sono le informazioni che vengono portate sulla piattaforma e più è probabile arricchire e correlare dati con altri eventi tracciati e registrati dalla community.

Vorrei inoltre evitare gli “errori” che ho visto commettere in altre MISP community: è vero che di base si tratta di un “grosso DB” molto articolato ma la cosa peggiore che possiamo fare è usarlo come un elencone di artefatti. Provo a spiegarmi meglio: ovviamente all’interno di un evento devono essere inseriti gli artefatti utili all’analisi ma devono essere ripotati anche gli elementi di contesto. **MISP documenta l’evento con tutti i suoi elementi**, gli artefatti sono alcuni degli elementi.

Probabilmente la cosa migliore è fare un esempio e quasi certamente farò dei video dedicati all’argomento. Supponiamo di voler documentare un evento specifico come una campagna di phishing: per prima cosa va considerato se ha senso creare un evento nuovo o se di tratta di informazioni che possono arricchire eventi esistenti.

![](https://roccosicilia.com/wp-content/uploads/2025/08/image-2.png?w=1024)

Una selezione di SPAM / Phishing

Se buttate un occhio nella posta elettronica che automaticamente il vostro provider vi propone come SPAM potreste trovare qualche esempio con cui esercitarvi. Ho preso alcuni eventi recenti di un mio account e sembrerebbe che nel mese di luglio (non ho evidenza del passato in quanto faccio pulizia) si è mosso qualcosa per il brand visibile come mittente nello screenshot. Analizzando il contenuto possiamo andare a caccia di elementi per capire se si tratta di banale SPAM o se è qualcosa di più vicino alla truffa o al phishing.

## Elementi legati alla comunicazione

Sto argomentando un esempio e vorrei cercare di non tralasciare dettagli. Le e-mail sono, come si sa, uno strumento di comunicazione per mandare un messaggio ad “A” a “B”. Affinché io possa scrivere una e-mail a qualcuno è necessaria una certa infrastruttura di base e dei servizi tra cui la connessione ad Internet (ovvio) ed i servizi di posta elettronica (ovvio). Questi servizi funzionano grazie al fatto che esistono altri servizi come il DNS. Per farla breve, quando inviamo una email succedono un sacco di cose che l’utente non vede ma di cui abbiamo delle tracce all’interno del messaggio di posta elettronica, o meglio, nel suo header.

In questo caso specifico dall’integrazione possiamo sicuramente recuperare l’**indirizzo email del mittente**, il **domain name** associato ed il **server** che è stato utilizzato per inviare il messaggio di posta elettronica:

```
[...]
From: <info_fty@webin-764.non.nsp.mk.ua>
[...]
header.from=webin-764.non.nsp.mk.ua
[...]
Received: from static.114.69.180.157.clients.your-server.de
[...]
```

Questi dati sono al momento semplici elementi tecnici e, mentre l’indirizzo email è facilmente manipolabile dal mittente, domain name e IP del server da cui è partito il messaggio sono più difficili da manipolare e in questi casi forse è anche poco utile.

## Elementi legati al contenuto

Nel corpo del messaggio ovviamente ci sono elementi che possiamo prendere in considerazione per capire meglio il contesto. In particolare quando si tratta di phishing potremmo provare elementi come tracker, link a siti esterni e allegati. Ogni elemento ha una funzione specifica.

I tracker consentono al Threat Actor di capire se l’e-mail è stata visualizzata e consente di ottenere alcune informazioni di base come l’IP pubblico della rete della vittima. Solitamente sono inserito come link all’interno dell’email o come contenuto esterno (es: una immagine) che il client può caricare.

![](https://roccosicilia.com/wp-content/uploads/2025/08/image-3.png?w=1024)

Estratto degli “href”

Essendo solitamente dei link li su può individuare andando a caccia dei tag href all’interno del corpo dell’email. Ne esistono due in questo caso e come si vede dalla URL si tratta di un link che puntano ad una risorsa Google ed in particolare ad un GCP Bucket con nome “lijhy”.

Se si va ad analizzare la risposta alla GET vediamo meglio cosa succede, vi risparmio i vari “jump” e vi riporto lo screenshot relativo al caricamento del contenuto del bucket (ammesso stia interpretando correttamente):

![](https://roccosicilia.com/wp-content/uploads/2025/08/image-4.png?w=1024)

Analisi della risposta (BurpSuite)

Sulla destra si vede chiaramente il contenuto del bucket con la chiamata JS responsabile della redirect:

```
document.location.href = 'http://static.148.85.180.157.clients.your-server.de/' + fragment;
```

La variabile *fragment* è valorizzata poco sopra ed equivale a tutto ciò che viene passato in URL dopo il carattere *#*. In pratica la URL viene riscritta modificando il solo dominio di destinazione. I due link si comportano allo stesso modo, è evidente che lo scopo del threat actor è portare l’utente ad accedere al sito target.

---

La mia attività di ricerca ed i progetti che porto avanti sono auto-sostenuti. Se ti interessano gli argomenti che porto puoi supportarmi tramite il [**mio canale Patreon**](https://patreon.com/roccosicilia). Per restare aggiornato su articoli, video e live puoi iscriverti al blog:

Digita la tua e-mail…

Iscriviti

---

Sugli elementi trovati va fatta una considerazione: come accennato in un recente [post su LinkedIn](https://www.linkedin.com/posts/roccosicilia_cybersecurity-trick-activity-7359601768768397314-gx6i?utm_source=share&utm_medium=member_desktop&rcm=ACoAAATK5U0By2qlNbOT_QThQp0s692DGhr_JfU), la URL storage.cloud.google.com è stata classificata come sospe...