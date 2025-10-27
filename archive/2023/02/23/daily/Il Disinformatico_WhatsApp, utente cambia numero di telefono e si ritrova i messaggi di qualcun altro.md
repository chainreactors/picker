---
title: WhatsApp, utente cambia numero di telefono e si ritrova i messaggi di qualcun altro
url: http://attivissimo.blogspot.com/2023/02/whatsapp-utente-cambia-numero-di.html
source: Il Disinformatico
date: 2023-02-23
fetch_date: 2025-10-04T07:53:02.983329
---

# WhatsApp, utente cambia numero di telefono e si ritrova i messaggi di qualcun altro

# [Il Disinformatico](https://attivissimo.blogspot.com/)

Un blog di Paolo Attivissimo, giornalista informatico e cacciatore di bufale

**Informativa privacy e cookie:** Questo blog include cookie di terze parti. Non miei ([dettagli](https://tinyurl.com/2p9apfu5))

[Prossimi eventi pubblici](https://attivissimo.me/disinformaticalendario/prossimi/) – [Donazioni](https://attivissimo.me/donazioni/) – [Sci-Fi Universe](https://scifiuniverse.it)

## Cerca nel blog

|  |  |
| --- | --- |
|  |  |

## 2023/02/22

### WhatsApp, utente cambia numero di telefono e si ritrova i messaggi di qualcun altro

*[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg03m8MrW4rZnf_Ntd2NJRtfbL2htSGMfaspbVtCiHDnPGEAJBTxVX8q4czl3sH7mNr-CxsREGIF7MGof29iiIJM6frtLSZJ-ajZhuC7GqYelfNMTM1nGoi3yUju1dGj8CVomiVKYrqQ_f817XZKh8o8nF3dIciwyJJc3GLb24w8tvOeK4M36Q/s320/Whatsapp-logo-macOS-2023-02.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg03m8MrW4rZnf_Ntd2NJRtfbL2htSGMfaspbVtCiHDnPGEAJBTxVX8q4czl3sH7mNr-CxsREGIF7MGof29iiIJM6frtLSZJ-ajZhuC7GqYelfNMTM1nGoi3yUju1dGj8CVomiVKYrqQ_f817XZKh8o8nF3dIciwyJJc3GLb24w8tvOeK4M36Q/s418/Whatsapp-logo-macOS-2023-02.png)*

*Ultimo aggiornamento: 2023/02/22 17:35.*

Scavalcare la crittografia *end-to-end* di WhatsApp e leggere tutti i
messaggi di un altro utente è facile. Così facile che può capitare addirittura
per caso: basta avere il numero di telefono di quell’utente (in altre parole,
è sufficiente essere un *end* di quell’*end-to-end*).

[The Register](https://www.theregister.com/2023/02/21/accidental_whatsapp_account_takeover/)
e
[Gizmodo](https://gizmodo.com/whatsapp-new-phone-number-account-problem-group-chats-1850124309)
hanno pubblicato il racconto della disavventura capitata a un utente europeo
che ha involontariamente avuto accesso a tutti i messaggi privati e ai gruppi
WhatsApp di un’altra persona.

L’utente diventato intruso per caso si chiama Ugo e per molto tempo ha avuto
un account WhatsApp legato al suo numero di telefono cellulare svizzero. A
ottobre scorso si è trasferito in Francia per lavoro e si è procurato un
numero di telefono cellulare francese, con relativa SIM nuova. Durante tutto
questo periodo ha continuato a usare WhatsApp senza problemi, ricevendo e
mandando messaggi come al solito.

Alla fine del mese di ottobre 2022 ha cambiato il proprio numero nell’app di
WhatsApp, dando quello francese. A quel punto il suo telefono è stato inondato
da tutti i gruppi e i messaggi personali e di lavoro di qualcun altro, quasi
tutti in italiano, e la sua foto di profilo è diventata quella di quella
persona (una donna). Ugo ha cercato di spiegare ai suoi interlocutori che lui
non era la persona con la quale credevano di parlare, ma senza molto successo.

In pratica, senza volerlo Ugo aveva preso il pieno controllo dell’account
WhatsApp di un’altra persona a lui sconosciuta.

Il padre di Ugo, che per lavoro ha esperienza nel settore e che ho contattato
direttamente via mail, mi ha spiegato che ha usato l’apposita
[pagina di segnalazione](https://www.facebook.com/whitehat) di Meta
per avvisare del possibile *bug* di sicurezza: la risposta di Meta è
stata che non è un difetto di WhatsApp, ma è un problema degli operatori
telefonici, che riutilizzano i numeri di telefono.

Fra l’altro, si tratta di un problema noto e addirittura
[documentato nelle FAQ di WhatsApp](https://faq.whatsapp.com/3347469605523961?cms_id=3347469605523961&draft=false):

> Tutti gli account WhatsApp sono collegati a un numero di cellulare. Dal
> momento che riutilizzare i numeri di telefono è una prassi piuttosto comune
> per gli operatori di telefonia mobile, è possibile che il precedente
> proprietario del tuo numero di telefono usasse WhatsApp.

In pratica, qualche tempo prima la donna di cui Ugo stava leggendo i messaggi
WhatsApp aveva chiuso il numero di telefonino che usava per WhatsApp. Quel
numero era tornato disponibile e l’operatore telefonico lo aveva riutilizzato,
assegnandolo a Ugo.

Questa possibilità di accedere ai messaggi WhatsApp di un altro utente è una
falla di privacy considerevole, e il bello è che è nota
[almeno da tre anni](https://www.vice.com/en/article/bv8mqd/how-i-hacked-whatsapp-account). Se qualcuno ha modo di farsi dare dall’operatore telefonico una SIM che ha
il numero della persona presa di mira, può leggerne tutti i messaggi. È una
tecnica chiamata *SIM swap*: i criminali informatici la usano contattando
gli operatori telefonici e spacciandosi per la vittima, chiedendo una SIM
nuova perché, dicono, quella corrente non funziona più o è stata smarrita. Nei
paesi nei quali gli operatori non verificano attentamente l’identità degli
utenti, la SIM nuova finisce nelle mani del criminale, che a quel punto può
ricevere tutti gli SMS di autenticazione dei vari servizi online della vittima
e prendere il controllo in particolare delle sue piattaforme social.

Nel caso di Ugo non c’è stata alcuna intenzione criminosa, ma la sua vicenda
dimostra che la riservatezza dei messaggi online non è robusta come molti
pensano.

Per contenere questo problema dei numeri riciclati, normalmente gli operatori
hanno un periodo piuttosto lungo di cosiddetta “quarantena”, durante il quale
il numero non viene riassegnato a nessuno, e WhatsApp dichiara che se si
accorge che un account non viene usato per un mese e mezzo e poi ricomincia a
essere usato su un dispositivo nuovo, eliminerà i dati del vecchio account. Ma
a Ugo e alla donna che è diventata sua vittima non intenzionale non è andata
così, perché l’account della donna *non era inattivo*. La donna aveva
cambiato numero di telefono e aveva continuato a usare WhatsApp sul nuovo
numero, ma senza cambiare il numero *nell’app*.

Infatti se non si avvisa WhatsApp del cambio di numero, WhatsApp continua a
credere che l’account sia associato ancora al numero vecchio, come dimostra il
padre di Ugo con un video dettagliatissimo, in cui usa due numeri di telefono
svizzeri e fa vedere che scambiando le SIM i due utenti, chiamiamoli Andrea e
Beatrice, continuano a ricevere i messaggi dei rispettivi account WhatsApp
come se niente fosse, nonostante lo scambio di SIM nei loro telefoni.

Ma se Andrea avvisa WhatsApp del cambio di numero, il suo telefono comincia a
ricevere i messaggi WhatsApp di Beatrice, perché il telefono di Andrea
contiene la SIM che prima era nel telefono di Beatrice.

Normalmente WhatsApp protegge il cambio di numero contro gli abusi inviando al
numero *vecchio* un SMS contenente un codice di sicurezza. Ma in questo
caso il vecchio numero di Beatrice ora ce l’ha Andrea, che quindi riceve il
codice e ha tutto il necessario per prendere il controllo dell’account
WhatsApp di Beatrice.

Va chiarito che questa tecnica non consente accesso ai messaggi
*passati* di WhatsApp: permette di leggere soltanto i messaggi che sono
stati inviati al proprietario precedente del numero *dopo* che il nuovo
proprietario ha usato quel numero per WhatsApp. Ma già così, ricevere le
comunicazioni e le foto destinate a un’altra persona e poterla impersonare
online, senza che quella persona lo sappia, è parecchio invadente e
preoccupante.

Va anche sottolineato che questa situazione offre un canale di sorveglianza
molto semplice alle forze di polizia: è sufficiente che chiedano all’operatore
telefonico di generare una seconda SIM con lo stesso numero e avranno accesso
ai messaggi WhatsApp inviati alla persona sorvegliata. Nel caso di altri
sistemi di messaggistica, come Telegram, che conservano i messaggi sui propri
server, questa tecnica probabilmente consente anche di recuperare tutti i
messaggi *passati*.

Noi utenti possiamo ridurre il rischio di violazioni della privacy come questa
con due passi piuttosto semplici. Il primo è attivare l’autenticazione a due
fattori su WhatsApp, sotto
*Impostazioni - Account - Verifica in due passaggi*. Il secondo è
avvisare WhatsApp se cambiamo numero, andando in
*Impostazioni - Account - Cambia numero*. Andrebbe fatto comunque, perché
altrimenti in caso di qualu...