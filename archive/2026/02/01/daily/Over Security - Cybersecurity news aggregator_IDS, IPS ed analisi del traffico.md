---
title: IDS, IPS ed analisi del traffico
url: https://roccosicilia.com/2026/01/31/ids-ips-ed-analisi-del-traffico/
source: Over Security - Cybersecurity news aggregator
date: 2026-02-01
fetch_date: 2026-02-02T04:16:14.824783
---

# IDS, IPS ed analisi del traffico

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/progetto-di-divulgazione/)
* [Sostieni il progetto](https://roccosicilia.com/sostieni-il-progetto/)
* [English version](https://medium.com/%40roccosicilia)

[cyber security](https://roccosicilia.com/category/cyber-security/), [hacking](https://roccosicilia.com/category/hacking/), [ita](https://roccosicilia.com/category/ita/), [study with me](https://roccosicilia.com/category/study-with-me/)

## [IDS, IPS ed analisi del traffico](https://roccosicilia.com/2026/01/31/ids-ips-ed-analisi-del-traffico/)

Published by

Rocco Sicilia

on

[31 gennaio 2026](https://roccosicilia.com/2026/01/31/ids-ips-ed-analisi-del-traffico/)

[![IDS, IPS ed analisi del traffico](https://roccosicilia.com/wp-content/uploads/2025/08/image-1.png?w=1024)](https://roccosicilia.com/2026/01/31/ids-ips-ed-analisi-del-traffico/)

Qualche giorno fa ho parlato di [traffic sniffing](https://roccosicilia.com/2025/12/31/punto-di-sniffing/), argomento che mi avrebbe portato a parlare di Intrusion Detection/Prevention System e ad una ulteriore evoluzione del lab e dei test che potrò/potremo fare. Ho parlato di questi strumenti nella [serie dedicata ai temi Defense](https://www.patreon.com/collection/1640938?view=expanded) su Patreon che eventualmente potete utilizzare per approfondire la questione, in questo post andiamo direttamente sui temi operativi ed utilizziamo solo la componente IDS per i test. L’obiettivo di questo LAB è mettersi nelle condizioni di analizzare il traffico all’interno di una rete ed intercettare anomalie riconoscibili dalle peculiarità del traffico che si sta osservando.

## Lab Setup

![](https://roccosicilia.com/wp-content/uploads/2026/01/image-7.png?w=1024)

Schema di rete

Cercherò di dare più dettagli possibili così da consentire una replica del setup che ho utilizzato pur considerando che non è necessaria una replica esatta. Il mio lab si sta arricchendo di diversi elementi per i miei esperimenti di Penetration Testing e Detection in ambienti controllati e in questa occasione si è aggiunta la macchina che nello schema ho chiamato “detection1”. Si tratta di una guest Ubuntu Server che ho intensione di utilizzare come base per gli strumenti di detection ed per il lab in questione è stato installato l’IDS Suricata.

> Nota: ci sono mille guide per installare Suricata a cui si aggiunge questo mio video in cui ho deciso di fare uno spiegone da zero:

Lo strumento IDS per funzionare deve ricevere una copia del traffico che transita in rete per poi analizzarlo a caccia di elementi che indichino una minaccia. Si può trattare di firme statiche, come uno specifico pacchetto o payload noto, o di pattern riconducibili ad azioni malevole. L’elemento da considerare per il setup del lab è il fatto che la sonda deve ricevere una copia del traffico, cose relativamente semplice in un ambiente virtualizzato in quanto possiamo configurare la porta della macchina sonda in modalità promiscua al fine di ottenere l’invio di tutti i frame relativi al traffico delle VMs anche alla NIC della sonda oltre che verso la porta di destinazione. Considerando lo schema di rete allegato sopra, la sonda sarà in grado di vedere tutto il traffico delle guest collegate al vSwitch.

![](https://roccosicilia.com/wp-content/uploads/2026/02/screenshot-2026-02-01-at-17.34.30.png?w=1024)

Conf. della NIC su vBox

Per rendere l’esperienza fedele ad un contesto reale ci servono anche altre due guest su cui indagare: nel caso del mio lab sono la macchina virtuale “kali” e la macchina virtuale “win 7” che, come suggeriscono i nomi, sono rispettivamente la macchina che useremo come base per lanciare gli attacchi e la macchina su cui predisporremo delle vulnerabilità *exploitabili* comodamente.

Per come è configurato il mio lab, con il firewall che è una guest sullo stesso host VirtualBox con la NIC “interna” sullo stesso vSwitch delle guest, anche il traffico da e verso internet per le guests del server viene replicato verso l’IDS. Questa configurazione ci tornerà utile nei labs in cui giocare con i C2.

## Suricata

Come detto nel mio home lab ho deciso di utilizzare Suricata come IDS configurato in modo da osservare tutto il traffico che transita dal vSwitch. In particolare nella mia configurazine ho attivato EVE (Extensible Event Format) che mi permette di avere il dettaglio JSON del traffico (utilissimo per portare poi i dati sul SIEM, ma sarà oggetto di altro post).

![](https://roccosicilia.com/wp-content/uploads/2026/02/screenshot-2026-02-01-at-17.44.38.png?w=753)

Con questa configurazione, al netto delle regole di detection, disponiamo di un file di log in JSON che ci permette di avere un’ottimo livello di comprensione dei dati.

![](https://roccosicilia.com/wp-content/uploads/2026/02/image.png?w=1024)

Contenuto del log eve.json filtrando per la stringa “dns”

Ora che Suricata può vedere tutto il traffico e noi ci siamo messi nelle condizioni di poter visualizzare almeno i metadati (e qualcosa di più) possiamo istruire l’IDS con delle regole che cerchino specifici pattern o dati.

Ho pubblicato in video in cui ho illustrato alcune semplici regole che qui vi riporto, in particolare può essere interessante come creare una regola per intercettare uno specifico exploit come eternalblue:

```
  alert tcp any any -> any 445 (msg:"Possible ETERNALBLUE Remote Code Execution Attempt - Metasploit"; content:"|FF 53 4D 42|"; content:"|51 00|"; classtype:trojan-activity; sid:1000004; rev:1;)
```

In questo semplice esempio (che deriva da alcune analisi di hackers-arise.com) la regola genera un alert in caso venga osservato uno specifico contenuto definito con una sequenza di byte in un pacchetto TCP verso la porta 445.

Video di sintesi

Questo tipo di regola è molto semplice, ma Suricata consente di creare regole molto più complesso basate su varie condizioni o comportamenti.

## Next step

Mentre scrivevo questo post e registravo il video mi sono reso conto che potrebbe essere utile per chi segue questi contenuti disporre di un lab minimale con cui giocare. Ho deciso che nelle prossime settimane preparerò degli articoli tecnici con lo step by spet per la creazione del lab di base. Ci metterò un po’ ma è anche la scusa per discutere delle diverse tecnologie utilizzate.

---

Se questo tipo di contenuti ti interessa e lo trovi utili per i tuoi studi o il tuo lavoro puoi sostenere il mio progetto di divulgazione iscrivendoti ai miei canali, in particolare su [YuoTube](https://youtube.com/%40roccosicilia) e [Patreon](https://patreon.com/roccosicilia). Puoi rimanere aggiornato su quello che faccio iscrivendoti a questo blog:

Digita la tua e-mail…

Iscriviti

### Condividi:

* Invia un link a un amico via e-mail (Si apre in una nuova finestra)
  E-mail
* [Condividi su LinkedIn (Si apre in una nuova finestra)
  LinkedIn](https://roccosicilia.com/2026/01/31/ids-ips-ed-analisi-del-traffico/?share=linkedin)
* [Condividi su Telegram (Si apre in una nuova finestra)
  Telegram](https://roccosicilia.com/2026/01/31/ids-ips-ed-analisi-del-traffico/?share=telegram)
* [Condividi su WhatsApp (Si apre in una nuova finestra)
  WhatsApp](https://roccosicilia.com/2026/01/31/ids-ips-ed-analisi-del-traffico/?share=jetpack-whatsapp)

Mi piace Caricamento…

### Lascia un commento [Cancella risposta](/2026/01/31/ids-ips-ed-analisi-del-traffico/#respond)

Δ

Questo sito utilizza Akismet per ridurre lo spam. [Scopri come vengono elaborati i dati derivati dai commenti](https://akismet.com/privacy/).

←[Precedente: Info Sec Unplugged – CISO e vCISO](https://roccosicilia.com/2026/01/11/info-sec-unplugged-ciso-e-vciso/)

Ciao,

### sono Rocco

![](https://sheliakblog.wordpress.com/wp-content/uploads/2025/04/photo.jpeg?w=389)

… e questo è mio sito personale dove condivido idee, riflessioni ed esperienze su hacking e sicurezza informatica.

### Let’s connect

* [Patreon]...