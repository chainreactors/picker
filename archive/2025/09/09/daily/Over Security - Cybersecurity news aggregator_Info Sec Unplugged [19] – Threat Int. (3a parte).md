---
title: Info Sec Unplugged [19] – Threat Int. (3a parte)
url: https://roccosicilia.com/2025/09/08/info-sec-unplugged-18-threat-int-3a-parte/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-09
fetch_date: 2025-10-02T19:52:17.033634
---

# Info Sec Unplugged [19] – Threat Int. (3a parte)

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/progetto-di-divulgazione/)
* [Sostieni il progetto](https://roccosicilia.com/sostieni-il-progetto/)
* [English version](https://medium.com/%40roccosicilia)

[cyber security](https://roccosicilia.com/category/cyber-security/), [ita](https://roccosicilia.com/category/ita/), [update](https://roccosicilia.com/category/update/), [vlog & podcast](https://roccosicilia.com/category/vlog-podcast/)

## [Info Sec Unplugged [19] – Threat Int. (3a parte)](https://roccosicilia.com/2025/09/08/info-sec-unplugged-18-threat-int-3a-parte/)

Published by

Rocco Sicilia

on

[8 settembre 2025](https://roccosicilia.com/2025/09/08/info-sec-unplugged-18-threat-int-3a-parte/)

[![Info Sec Unplugged [19] – Threat Int. (3a parte)](https://roccosicilia.com/wp-content/uploads/2024/12/podcast.png?w=541)](https://roccosicilia.com/2025/09/08/info-sec-unplugged-18-threat-int-3a-parte/)

Questa è una puntata un po’ particolare: da questo episodio la versione audio su [**spreaker**](https://www.spreaker.com/podcast/info-sec-unplugged--6025156) sarà quella completa e disponibile online sulle piattaforme podcast mentre sul mio canale [YouTube](https://youtube.com/%40roccosicilia) e sul blog pubblicherà un video/post di accompagnamento gli highlight e qualche approfondimento.

Info Sec Unplugged [19]

La puntata è la terza parte di un argomento complesso: la Threat Intelligence. Ci siamo dati l’obiettivo di provare a spiegare come questo processo si “incastra” in una struttura operativa, a cosa serve e come si può utilizzare per migliorare la propria postura di sicurezza. Per chiudere questa serie di tre episodi abbiamo utilizzato un esempio pratico: l’analisi di una semplice scampagna di phishing per ripercorrere i passi che un analista può fare per raccogliere informazioni da un elemento semplice come una email.

## Approfondimenti

#### L’analisi di una email

Durante la puntata facciamo riferimento all’analisi dell’intestazione e del corpo di una email indicando che in questa parti del contenuto ci sono diverse informazioni utili che possiamo raccogliere.

Per fare un esempio che quasi tutti posso replicare facilmente potete selezionare una email dal vostro account Gmail e scegliere l’opzione *Show Original*. Dovrebbe aprirsi una nuova pagina sul vostro browser con la versione “estesa” del messaggio di posta elettronica dove, nella parte iniziale, troverete una serie di stringhe che probabilmente faticherete a decifrare.

![](https://roccosicilia.com/wp-content/uploads/2025/09/image-1.png?w=1024)

Header di un messaggio di spam nella mia mailbox Gmail

In questa parte del messaggio di posta ci sono informazioni preziose sull’origine dell’email che, anche se in parte contraffatte, possono essere annotate e documentate in quanto potrebbero costituire un elemento utile all’analisi.

Ad esempio, per il Threat Actor è sicuramente facile falsificare un indirizzo email mittente – *edu@cma7c.h8i.fouri.web.za* in questo caso – un po’ più complesso falsificare il dominio o il sistema che ha fisicamente inviato l’email, rispettivamente *cma7c.h8i.fouri.web.za* e *157.180.69.114*. Questi dati possono essere un buon punto di partenza per avviare un’indagine.

#### Analisi dei link

Nel corpo del massaggio spesso ci sono link che portano a pagine web che, come nel caso dell’esempio fatto durante il podcast, servono a portare l’utente ad inserire i propri dati che vengono poi raccolti dagli autori della campagna di phishing/scam.

In questa campagna viene utilizzato un trucco per “pulire” il link presente nell’email inserendo un riferimento che punta ad una risorsa cloud storage di Google:

![](https://roccosicilia.com/wp-content/uploads/2025/09/image-2.png?w=1024)

Link ad una risorsa hosted da Google

Difficilmente i sistemi anti-spam ed in generale i sistemi di detection bloccano questo tipo di link. Nel caso specifico si può osservare come questo tipo di link sia ampiamente documentato su VirusTotal come infrastruttura abitualmente utilizzata per scam/phishing:

![](https://roccosicilia.com/wp-content/uploads/2025/09/image-3.png?w=1024)

316 community report a cui vado ad aggiungere il mio

Più interessante, come in un altro caso analizzato, il contenuto della pagina a cui si punta:

```
<meta http-equiv="refresh" content="3; url=http://static.239.113.98.91.clients.your-server.de">

<script>
var fragment = window.location.href.split('#')[1] || ''; // fallback to empty string if no fragment
document.location.href = 'http://static.239.113.98.91.clients.your-server.de/' + fragment;
</script>
```

Un semplice redirect verso un’altra pagina che poi rimanda ad un altro sito (loiete[.]com) che infine ci porta sul sito di phishing (dinusreal[.]store).

#### Unire i puntini

Raccogliere i singoli elementi e documentarli nel dettagli porta ad ottenere una collezione di artefatti (ip, url, frammenti di JS, testi di email, sender, ecc) che presi singolarmente non hanno particolare significato, ma se organizzati in un unico evento che descrive una campagna di phishing acquistano molto significato.

Sono dati a cui un analista può accedere tramite ricerche mirate e che possono essere correlati con altri dati. Sono informazioni che possiamo far consumare ai sistemi di detection o che possiamo utilizzare per attivare policies più stringenti in base alle esigenze della nostra infrastruttura e degli utenti che la utilizzano.

Ovvio, prima devo avere uno strumento che mi consenta tutto questo (come MISP) ed un team o un partner che mi aiuti ad integrare questo tesoretto di informazioni nei miei sistemi di detection.

## Conclusioni

La Threat Int. è un tema molto complesso, il fatto di aver dedicato tre puntate sol per introdurlo penso sia un elemento che lo testimonia. È anche una disciplina estremamente utile che, a vali livelli, tutte le organizzazioni devono iniziare a considerare. È un tema che sicuramente riprenderemo nel podcast.

Vi ricorso, importantissimo, il link al **[podcast su Spreaker](https://www.spreaker.com/podcast/info-sec-unplugged--6025156)** e, come sempre, se gli argomenti che porto vi interessano e volere restare aggiornati su tutto quello che pubblico oltre al Podcast potete iscrivervi a questo Blog lasciando la vostra email o seguirmi sui miei canale diretti:

* YouTube: [https://youtube.com/@roccosicilia](https://youtube.com/%40roccosicilia)
* Patreon: <https://patreon.com/roccosicilia>
* Reddit: <https://www.reddit.com/r/SheliakNotes/>

Digita la tua e-mail…

Iscriviti

### Condividi:

* Fai clic per inviare un link a un amico via e-mail (Si apre in una nuova finestra)
  E-mail
* [Fai clic qui per condividere su LinkedIn (Si apre in una nuova finestra)
  LinkedIn](https://roccosicilia.com/2025/09/08/info-sec-unplugged-18-threat-int-3a-parte/?share=linkedin)
* [Fai clic per condividere su Telegram (Si apre in una nuova finestra)
  Telegram](https://roccosicilia.com/2025/09/08/info-sec-unplugged-18-threat-int-3a-parte/?share=telegram)
* [Fai clic per condividere su WhatsApp (Si apre in una nuova finestra)
  WhatsApp](https://roccosicilia.com/2025/09/08/info-sec-unplugged-18-threat-int-3a-parte/?share=jetpack-whatsapp)

Mi piace Caricamento…

### Lascia un commento [Cancella risposta](/2025/09/08/info-sec-unplugged-18-threat-int-3a-parte/#respond)

Δ

Questo sito utilizza Akismet per ridurre lo spam. [Scopri come vengono elaborati i dati derivati dai commenti](https://akismet.com/privacy/).

←[Precedente: Assume Breach: evoluzione di uno scenario](https://roccosicilia.com/2025/09/05/assume-breach-evoluzione-di-uno-scenario/)

[Successivo: Live del 05.09.2025: http\_c2](https://roccosicilia.com/2025/09/09/live-del-05-09-2025-http_c2/)→

Ciao,

### sono Rocco

![](https://sheliakblog.wordpress.com/wp-content/uploads/2025/04/photo.jpeg?w=389)

… e questo è mio sito personale dove condivido idee, riflessioni ed esperi...