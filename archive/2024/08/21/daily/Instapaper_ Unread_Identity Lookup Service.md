---
title: Identity Lookup Service
url: https://djangofaiola.blogspot.com/2024/08/identity-lookup-service.html
source: Instapaper: Unread
date: 2024-08-21
fetch_date: 2025-10-06T18:05:28.734706
---

# Identity Lookup Service

[Skip to content](#mainnbt)

# [Appunti di Informatica Forense](https://djangofaiola.blogspot.com/)

## Digital Forensics and Incident Response Research

* [Home page](http://djangofaiola.blogspot.com/)
* [Downloads](https://djangofaiola.blogspot.com/p/downloads.html)

## giovedì 8 agosto 2024

Published agosto 08, 2024 by Django Faiola with [0 comment](https://djangofaiola.blogspot.com/2024/08/identity-lookup-service.html#comment-form)

# [Identity Lookup Service](https://djangofaiola.blogspot.com/2024/08/identity-lookup-service.html)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEirmDKs31XbJTNIzbCK5oj_Am_Nppa0no6EyuC_Eyk5XYXFV3ZQN4wYm2v6IKX-ZIVwrCLxPGaoc43gCnWuxXTl4OTWlsGrOeadfEMRMWUEcdERpSxp0l5hbeN7bK3tCIh3r9AfQmSUv1FpdA8JECTU-AImMu_v4QjjChncDUKmrToH2ens50vAbD3zAHI/s320/identityservices.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEirmDKs31XbJTNIzbCK5oj_Am_Nppa0no6EyuC_Eyk5XYXFV3ZQN4wYm2v6IKX-ZIVwrCLxPGaoc43gCnWuxXTl4OTWlsGrOeadfEMRMWUEcdERpSxp0l5hbeN7bK3tCIh3r9AfQmSUv1FpdA8JECTU-AImMu_v4QjjChncDUKmrToH2ens50vAbD3zAHI/s1000/identityservices.png)

### Indice dei contenuti

* [La struttura del record di autenticazione](#authentication)
* [idstatuscache.plist](#idstatuscache)
* [Percorsi](#percorsi)
* [Il dubbio "Cellebrite"](#dubbio)
* [Conclusioni](#conclusioni)
* [iLEAPP](#iLEAPP)

### Introduzione

#

Nel 2019 la Cellebrite pubblica l'articolo [How iOS Properties Files Can Confirm a Suspect’s Contacts Even If
Deleted](https://cellebrite.com/en/how-ios-properties-files-can-confirm-a-suspects-contacts-even-if-data-deleted/) dove in sintesi spiega l'importanza di trovare un archivio affidabile
delle comunicazioni tra le parti che sia permanente e legittimo da
consultare durante le indagini e in tribunale.

L'identificazione dell'elenco dei contatti sul telefono cellulare di un
sospettato è sempre stata una sfida, poiché la deliberata cancellazione
delle informazioni da parte del sospetto porta alla necessità di trovare un
modo corretto dal punto di vista forense per recuperale.

La ricercatrice della Cellebrite [Izhar Carmel](https://cellebrite.com/en/author/izharcarmel/)
ha scoperto che il file com.apple.identityservices.idstatuscache.plist
presente nel percorso "/private/var/mobile/Library/Preferences/" è la cache che contiene i record delle autenticazioni degli ID
Apple.

Un utente Apple che utilizza iMessage o FaceTime, quando tenta di contattare
un destinatario, viene interrogato l'Enterprise Shared Services, il server
delle autenticazioni di Apple per la verifica dell'identità. A fine convalida,
se è la prima volta che si cerca il destinatario, viene creato un nuovo record
(dizionario) con l'ID del primo tentativo di contatto come numero
di telefono (es. tel:+14693560xxx) o
come indirizzo email (es. mailto:joshuahickmanxxx@gmail.com) e la data dell'evento stesso nel dizionario associato al servizio
utilizzato (es. com.apple.madrid).

Non è necessario che l'operazione per esempio dell'invio del messaggio venga
portata a termine; il nuovo record viene comunque registrato nella cache.
Questi record non vengono sovrascritti dalle successive ricerche o
selezione dello stesso destinatario e per la stessa applicazione.

Successivamente nel 2020 pubblica [How to Use the Identity Lookup Service in Cellebrite Physical Analyzer](https://cellebrite.com/en/how-to-use-the-identity-lookup-service-in-cellebrite-physical-analyzer/), una demo video con l'analisi dell'artefatto.

**Identity Lookup Service (Servizio di Ricerca dell'Identità)** è
il servizio di Apple che gestisce l'autenticazione dei processi. Questi dati
confermano solo che è avvenuta l'autenticazione del destinatario e non danno nessuna informazione utile per quanto
riguarda l'avvenuto invio di un messaggio o l'avvio di una conversazione. E'
solo un indizio che indica che qualcosa è successo, ma per dimostrare che
qualcosa è realmente avvenuto, bisogna tracciarlo altrove.

Per lo studio di questo artefatto è stata utilizzata una
delle immagini pubbliche di iOS note nel settore e in particolare quella di [Josh Hickman iOS 14.3](https://thebinaryhick.blog/2021/02/20/ios-14-macos-big-sur-lots-of-images/) disponibile su [MediaFire](https://www.mediafire.com/file_premium/iszzhjatyjwmq8o/iOS_14-3_-_Apple_iPhone_SE.tar/file) e i dati estratti dal mio iPhone 8 con iOS 16.7.8.

### La struttura del record di autenticazione

Per la visualizzazione ho usato **dfDataViewer**, il mio visualizzatore di (B)Plist, JSON(B), (B)XML, ASN.1, Protobuf,
LevelDB, etc. ancora in fase di sviluppo e non pubblico.

com.apple.identityservices.idstatuscache.plist

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhESEwGqSeippCyAhzoxEL21IByImAHuQ-JwWr8nVPP46UUmKMHgK7kDn9l2X4GIYdTuX2OyV7RWOipppLKeCQFt2dOJLDcOj6dSz1fbRMT3pbVTaS8xxs0TrBL7DM4g5oY4RyV2U7-ydyEG-mGdRmc6miIPo7H_spmHIfvuuRUxr8CwDO21MhyphenhypheniXQuIQA/w640-h372/identityservices_idstatuscache_plist.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhESEwGqSeippCyAhzoxEL21IByImAHuQ-JwWr8nVPP46UUmKMHgK7kDn9l2X4GIYdTuX2OyV7RWOipppLKeCQFt2dOJLDcOj6dSz1fbRMT3pbVTaS8xxs0TrBL7DM4g5oY4RyV2U7-ydyEG-mGdRmc6miIPo7H_spmHIfvuuRUxr8CwDO21MhyphenhypheniXQuIQA/s1538/identityservices_idstatuscache_plist.png)

Il servizio com.apple.ess:
(FaceTime)

* tel:+19192895xxx: (numero di
  telefono)

+ IDStatus: 2 (1=iDevice,
  2=Not iDevice);
+ LookupDate: 635363625.519218 (timestamp della verifica dell'identità come real nel formato MAC
  Absolute Time 18 febbraio 2021 17:53:45);

* ...

Il servizio com.apple.madrid:
(iMessage)

* tel:+14693560xxx: (numero di
  telefono)

+ IDStatus:
  2 (Not iDevice);
+ LookupDate:
  635433067.361745 (19 febbraio 2021 13:11:07);

* ...

com.apple.ess e com.apple.madrid sono gli identificatori dei servizi. E' noto a tutti che com.apple.madrid è l'identificatore del servizio iMessage e che com.apple.private.alloy.facetime.video
è quello di FaceTime Video; ma come è possibile associare questi servizi a
un nome da visualizzare? La risposta è nella directory "/System/Library/IdentityServices/ServiceDefinitions/" che contiene un serie di file Plist con le definizioni dei servizi.

com.apple.iMessage.plist

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiuQNnw9tJRhaehQC7oPY2RpYjG7lE5AgFnrknRfi5UOiJbLneO5M3XzhlkzkWoqk5QudH3SIniakOl1bpH2G3LX8ZztrqnF9dB_ppGS5BVV_rcf7CFJHSEhWM-URc8l2kLj17ag9WB2rieIw3yUYgHfpKECxNhzsw-NHo78fcvdb4CrZV2wk_4I2mr2sk/w640-h372/identityservices_services_imessage_plist.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiuQNnw9tJRhaehQC7oPY2RpYjG7lE5AgFnrknRfi5UOiJbLneO5M3XzhlkzkWoqk5QudH3SIniakOl1bpH2G3LX8ZztrqnF9dB_ppGS5BVV_rcf7CFJHSEhWM-URc8l2kLj17ag9WB2rieIw3yUYgHfpKECxNhzsw-NHo78fcvdb4CrZV2wk_4I2mr2sk/s1538/identityservices_services_imessage_plist.png)

Queste sono le chiavi rappresentative per una corretta mappatura degli
identificatori (Identifier e LegacyIdentifier) con il nome da visualizzare (DisplayName) oppure con il nome del servizio (ServiceName):

* DisplayName: iMessage
  (nome visualizzato "applicazione");
* Identifier: com.apple.madrid (identificatore univoco);
* LegacyIdentifier: com.apple.iMessage (identificatore univoco nelle vecchie versioni);
* ServiceName: Messenger (nome del servizio).

Quindi da questo file si ottengono due associazioni (id
= valore):

1. com.apple.madrid =
   iMessage
2. com.apple.iMessage =
   iMessage

Altri esempi di associazioni:

* com.apple.private.ac =
  Calling
* com.apple.ess =
  FaceTime
* com.apple.private.alloy.sms =
  SMSRelay
* com.apple.private.alloy.maps =
  Maps
* com.apple.private.alloy.nearby
  = Nearby

### idstatuscache.plist

A partire dalla versione iOS 14.7.0 il file com.apple.identityservices.idstatuscache.plist è vuoto o assente. La mia attenzione è stata catturata durante
l'utilizzo di FaceTime, quando digitando per la prima volta i destinatari,
sono stati autenticati in Blu per i
dispositivi Apple e in Verde per gli
altri, con un tempo superiore rispetto alla successiva ricerca...