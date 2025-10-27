---
title: NimDoor su macOS: nel mirino delle APT nordcoreane l’ecosistema crypto e Web3
url: https://www.ictsecuritymagazine.com/notizie/nimdoor-malware/
source: ICT Security Magazine
date: 2025-07-09
fetch_date: 2025-10-06T23:55:39.473443
---

# NimDoor su macOS: nel mirino delle APT nordcoreane l’ecosistema crypto e Web3

[Salta al contenuto](#main)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

* [Home](https://www.ictsecuritymagazine.com/)
* [Articoli](https://www.ictsecuritymagazine.com/argomenti/articoli/)
* RubricheEspandi
  + [Cyber Security](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)
  + [Cyber Crime](https://www.ictsecuritymagazine.com/argomenti/cyber-crime/)
  + [Cyber Risk](https://www.ictsecuritymagazine.com/argomenti/cyber-risk/)
  + [Cyber Law](https://www.ictsecuritymagazine.com/argomenti/cyber-law/)
  + [Digital Forensic](https://www.ictsecuritymagazine.com/argomenti/digital-forensic/)
  + [Digital ID Security](https://www.ictsecuritymagazine.com/argomenti/digital-id-security/)
  + [Business Continuity](https://www.ictsecuritymagazine.com/argomenti/business-continuity/)
  + [Digital Transformation](https://www.ictsecuritymagazine.com/argomenti/digital-transformation/)
  + [Cyber Warfare](https://www.ictsecuritymagazine.com/argomenti/cyber-warfare/)
  + [Ethical Hacking](https://www.ictsecuritymagazine.com/argomenti/ethical-hacking/)
  + [GDPR e Privacy](https://www.ictsecuritymagazine.com/argomenti/gdpr-e-privacy/)
  + [IoT Security](https://www.ictsecuritymagazine.com/argomenti/iot-security/)
  + [Industrial Cyber Security](https://www.ictsecuritymagazine.com/argomenti/industrial-cyber-security/)
  + [Blockchain e Criptovalute](https://www.ictsecuritymagazine.com/argomenti/blockchain-e-criptovalute/)
  + [Intelligenza Artificiale](https://www.ictsecuritymagazine.com/argomenti/intelligenza-artificiale/)
  + [Geopolitica e Cyberspazio](https://www.ictsecuritymagazine.com/argomenti/geopolitica-cyberspazio/)
  + [Interviste](https://www.ictsecuritymagazine.com/argomenti/interviste/)
* [Notizie](https://www.ictsecuritymagazine.com/argomenti/notizie/)
* [Pubblicazioni](https://www.ictsecuritymagazine.com/pubblicazioni/)
* [Cybersecurity Video](https://www.ictsecuritymagazine.com/argomenti/cybersecurity-video/)
* [Eventi](https://www.ictsecuritymagazine.com/eventi/)
* [Newsletter](https://www.ictsecuritymagazine.com/newsletter/)

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine1403) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Forum ICT Security 2025](https://www.ictsecuritymagazine.com/wp-content/uploads/banner-header-2025.jpg)](https://www.ictsecuritymagazine.com/eventi/forumictsecurity2025)

![malware NimDoor](https://www.ictsecuritymagazine.com/wp-content/uploads/freepik__malware-nimdoor__25475.jpeg)

# NimDoor su macOS: nel mirino delle APT nordcoreane l’ecosistema crypto e Web3

A cura di:[Redazione](#molongui-disabled-link)  Ore 8 Luglio 20258 Luglio 2025

Il malware NimDoor è una nuova minaccia individuata su macOS, impiegata da gruppi hacker nordcoreani per colpire aziende del settore Web3 e criptovalute. La notizia di questa campagna ha destato grande attenzione sia per il coinvolgimento diretto di asset crypto sia per l’elevato livello di sofisticazione tecnica della minaccia. Infatti, NimDoor rappresenta un salto di qualità nel toolkit offensivo nordcoreano: è un backdoor compilato nel linguaggio Nim (inusuale su macOS) e adotta tattiche avanzate di offuscamento e persistenza, rendendo l’analisi e il rilevamento particolarmente difficili.

La scelta di bersagli nel mondo Web3 riflette inoltre gli obiettivi finanziari dei gruppi APT della Corea del Nord, che negli ultimi anni hanno puntato sempre più ai furti di criptovalute per finanziare il regime. Basti pensare che il famigerato gruppo Lazarus è accusato di aver sottratto circa 1,5 miliardi di dollari da un exchange (Bybit) nel febbraio 2025, contribuendo al record di 1,34 miliardi di dollari rubati in criptovalute nel solo 2024.

## Vettori d’attacco: social engineering e falso update Zoom

Gli attacchi NimDoor iniziano con tecniche di social engineering ben congegnate. Gli operatori nordcoreani si spacciano per contatti fidati su Telegram, convincendo le vittime a organizzare incontri su Calendly (un servizio di scheduling). Successivamente inviano via email un apparente link a una riunione Zoom, invitando l’utente ad eseguire uno script di aggiornamento Zoom SDK “necessario” prima della call. In realtà, il file scaricato – *zoom\_sdk\_support.scpt* – è un AppleScript malevolo travestito da aggiornamento.

Questo script è riempito con 10.000 righe vuote e contiene un refuso intenzionale (“Zook SDK Update” invece di “Zoom SDK Update”) per nascondere il codice maligno e sfuggire a controlli sommari. Le ultime righe dello script contattano un server di command-and-control (C2) all’indirizzo *support.us05web-zoom[.]forum* (scelto per somigliare al dominio legittimo di Zoom) e scaricano un secondo stage dell’infezione. I ricercatori hanno identificato vari domini paralleli con schema simile (us05web-zoom.pro, .cloud, etc.), segno di una campagna mirata più ampia con URL unici per ciascun target.

Il secondo stage avviato dall’AppleScript conduce al download di due file binari Mach-O (a e installer) nella directory temporanea del sistema, che danno il via a due catene di infezione parallele. Il primo eseguibile, chiamato a, è compilato in C++ e funge da loader: scrive sul disco un payload cifrato (netchk) e innesca una serie di operazioni di decrittazione e depistaggio che culminano nello scaricamento di script Bash finalizzati all’esfiltrazione di dati. Il secondo eseguibile, installer, è compilato in Nim e si occupa di stabilire la persistenza del malware nel sistema.

Installer infatti deposita altri due payload Nim (GoogIe LLC – con la “i” maiuscola ingannevole al posto della “L” minuscola – e CoreKitAgent), che servono a garantire l’accesso duraturo al Mac infetto e meccanismi di recupero in caso di riavvio o rimozione.

## Caratteristiche tecniche di NimDoor: injection, comunicazioni cifrate e furto dati

Una delle caratteristiche più notevoli di NimDoor è l’uso di una tecnica di process injection raramente osservata su macOS. Il componente loader (InjectWithDyldArm64, identificato anche come a) lancia un processo benigno (Target) in stato sospeso e vi inietta in memoria il codice del payload trojan (trojan1\_arm64), per poi riprendere l’esecuzione del processo infetto.

Questo approccio richiede privilegi speciali su macOS: infatti il malware dispone delle entitlements Apple dedicate al debugging e all’accesso ai task (com.apple.security.cs.debugger e com.apple.security.get-task-allow) per poter effettuare l’iniezione di codice. Dopo l’injection, NimDoor stabilisce una connessione con il suo server C2 usando wss (WebSocket sicuro su TLS) invece dei protocolli HTTP/S tradizionali.

L’uso di WebSocket cifrato su macOS è insolito e consente comunicazioni bidirezionali persistenti col C2, mascherate dal traffico HTTPS standard. Inoltre, i ricercatori hanno scoperto che NimDoor applica più livelli di cifratura (algoritmo RC4 combinato con encoding Base64 e chiavi differenti) ai messaggi scambiati, aggiungendo ulteriore offuscamento ai dati trasmessi.

Attraverso il canale C2, il malware può ricevere comandi da eseguire sul sistema della vittima (es. raccolta informazioni di sistema, esecuzione di comandi arbitrari, modifica della directory corrente, ecc.) e inviare indietro i risultati in formato JSON.

NimDoor dimostra anche capacità estese di furto dati. Una volta compromesso il sistema, vengono attivati script Bash dedicati all’esfiltrazione silenziosa di informazioni sensibili. In particolare, uno script denominato upl raccoglie credenziali e dati dai principali browser (Arc, Brave, Chrome, Edge, Firefox), copiandone elementi come cronologia, cookie e password. Lo script prende di mira anche file di sistema critic...