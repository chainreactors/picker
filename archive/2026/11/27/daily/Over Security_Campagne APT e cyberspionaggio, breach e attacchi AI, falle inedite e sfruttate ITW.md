---
title: Campagne APT e cyberspionaggio, breach e attacchi AI, falle inedite e sfruttate ITW
url: https://www.telsy.com/campagne-apt-e-cyberspionaggio-breach-e-attacchi-ai-falle-inedite-e-sfruttate-itw/
source: Over Security
date: 2026-11-27
fetch_date: 2026-11-28T09:42:49.715862
---

# Campagne APT e cyberspionaggio, breach e attacchi AI, falle inedite e sfruttate ITW

* Gruppo TIM

[![Telsy](https://www.telsy.com/wp-content/themes/telsy/images/Logo_Telsy_pos-hor_RGB.png)](https://www.telsy.com/)

[Per fare una ricerca scrivi qualcosa e premi "invio"](/?s=)

Chiudi

* [Chi siamo](https://www.telsy.com/chi-siamo/)
* Soluzioni
  + [Vai a Soluzioni](https://www.telsy.com/soluzioni/)
  + [Cyber](https://www.telsy.com/soluzioni/cyber-ita/)
  + [Crypto](https://www.telsy.com/soluzioni/crypto-ita/)
  + [Quantum](https://www.telsy.com/soluzioni/quantum-ita/)
* [Innovazione](https://www.telsy.com/innovazione/)
* [Lavora con noi](https://www.telsy.com/lavora-con-noi/)
* [Blog](https://www.telsy.com/blog/)

* News in evidenza
  + [27 Nov

    Campagne APT e cyberspionaggio, breach e attacchi AI, falle inedite e sfruttate ITW](https://www.telsy.com/campagne-apt-e-cyberspionaggio-breach-e-attacchi-ai-falle-inedite-e-sfruttate-itw/)
  + [20 Nov

    Nuove vulnerabilità critiche e sfruttate ITW, attacchi alla penisola italiana, campagne APT e cyberspionaggio](https://www.telsy.com/nuove-vulnerabilita-critiche-e-sfruttate-itw-attacchi-alla-penisola-italiana-campagne-apt-e-cyberspionaggio/)

[Campagne APT e cyberspionaggio, breach e attacchi AI, falle inedite e sfruttate ITW](https://www.telsy.com/campagne-apt-e-cyberspionaggio-breach-e-attacchi-ai-falle-inedite-e-sfruttate-itw/)
[Nuove vulnerabilità critiche e sfruttate ITW, attacchi alla penisola italiana, campagne APT e cyberspionaggio](https://www.telsy.com/nuove-vulnerabilita-critiche-e-sfruttate-itw-attacchi-alla-penisola-italiana-campagne-apt-e-cyberspionaggio/)
[Vedi tutte](https://www.telsy.com/blog/)

* [English](https://www.telsy.com/en/apt-and-cyber-espionage-campaigns-breaches-and-ai-driven-attacks-newly-disclosed-vulnerabilities-and-flaws-exploited-itw/)
* [Italiano](https://www.telsy.com/campagne-apt-e-cyberspionaggio-breach-e-attacchi-ai-falle-inedite-e-sfruttate-itw/)

[Threat Intelligence](https://www.telsy.com/categoria/threat-intelligence/), [News](https://www.telsy.com/categoria/news/)

# Campagne APT e cyberspionaggio, breach e attacchi AI, falle inedite e sfruttate ITW

27 Nov 2026

Condividi

## ![Weekly Threats hor Telsy](https://www.telsy.com/wp-content/uploads/Weekly-Threats-hor-Telsy.png)

## APT e cyberspionaggio: operazioni internazionali, impiego dell’AI e sorveglianza con spyware

Il gruppo [**UNC5221**](https://www.telsy.com/tag/unc5221/), ritenuto legato alla Cina, ha condotto una campagna di cyberspionaggio sfruttando due 0-day. Alla fine di agosto 2026 ha ottenuto l’accesso iniziale tramite **CVE-2026-102764** in BeyondTrust Remote Support, per poi raggiungere sistemi Linux interni e installarvi le web shell **SLIMSAVAGE** e **CAGEMATCH**. A inizio settembre ha sfruttato **CVE-2026-123890**, un bypass dell’autenticazione in VMware vCenter Server corretto il 19 novembre. Il gruppo ha impiegato **BONESAW** per ottenere accesso amministrativo ed estrarre il database di vCenter e **SAWSNAKE** per falsificare token SAML. Nel corso dell’operazione ha inoltre distribuito le backdoor **BEARBONES** e **LAZYBONES**, quest’ultima con Slack come canale C2, e ha sottratto credenziali, chiavi crittografiche e dati di Active Directory. Sempre in Asia, un avversario con possibili legami con la Cina ha impiegato [**Cairn**](https://www.telsy.com/tag/cairn/), framework open-source di penetration testing basato su agenti AI autonomi, contro università dell’Asia orientale tra l’8 e il 10 settembre. I log di un’istanza esposta documentano tentativi falliti contro un server Redis e un server GPU, oltre alla compromissione di un server MONAI Label. Gli agenti hanno individuato autonomamente **CVE-2026-133968**, una 0-day di tipo Path Traversal, e l’hanno sfruttata per ottenere accesso con privilegi root. L’impiego dell’AI ricorre anche nelle evidenze pubblicate il 25 novembre su [**ARTEX**](https://www.telsy.com/tag/artex/). Oltre alle attività già documentate di [**Storm-0940**](https://www.telsy.com/tag/storm-0940/) e [**Storm-3358**](https://www.telsy.com/tag/storm-3358/), il framework è stato associato a [**GhostEmperor**](https://www.telsy.com/tag/ghostemperor/) e **UAT4356**, legati alla Cina, e a **Lazarus Group** e **LAWRENCIUM**, legati alla Corea del Nord. Target ed effetti delle operazioni dei quattro gruppi non sono stati divulgati. Sul versante nordcoreano, una nuova ondata della campagna [**PolinRider**](https://www.telsy.com/tag/polinrider/) ha interessato, al 24 novembre, 375 repository pubblici GitHub appartenenti a 260 account. Il loader, incorporato nei sorgenti, utilizzava transazioni Ethereum per recuperare codice JavaScript e individuare il server C2. La catena poteva eseguire codice con i privilegi dell’utente o del runner CI. Restano ignoti il numero di sistemi su cui il codice è stato eseguito e le eventuali esfiltrazioni. Le ondate precedenti sono state ricondotte a **Lazarus Group** e l’attribuzione di quella più recente resta da confermare. Un possibile legame con la Corea del Nord è stato ipotizzato, con bassa confidenza, anche per **UAT-12643**, avversario finanziariamente motivato che ha preso di mira utenti Windows distribuendo [**Overlord RAT**](https://www.telsy.com/tag/overlord-rat/) per il controllo remoto, **Good Game Stealer** per sottrarre credenziali e dati dei wallet e **Clipboard Hijacker** per sostituire gli indirizzi di destinazione dei trasferimenti di criptovalute. Le esche e i dati ricercati suggeriscono un interesse per utenti di criptovalute e piattaforme di gioco e per personale amministrativo e contabile, anche in Europa. Tra le operazioni di spionaggio ancora prive di attribuzione figura **Operation ShadowCloud**, rivolta principalmente a enti governativi in Asia e Africa. In un’organizzazione taiwanese l’avversario ha utilizzato lo strumento di amministrazione remota **MeshAgent** e il DLL Side-Loading per distribuire le backdoor Windows **GitDoor** e **GraphDoor**, che si appoggiavano a servizi legittimi come GitHub, Ably e SharePoint per lo scambio di comandi e dati. Su sistemi infetti da **GraphDoor** sono stati osservati anche beacon [**Cobalt Strike**](https://www.telsy.com/tag/cobalt-strike/). Le sovrapposizioni con attività di [**GhostEmperor**](https://www.telsy.com/tag/ghostemperor/) suggeriscono il possibile coinvolgimento di un gruppo sinofono. Nel Mediterraneo orientale e in Medio Oriente, l’iraniano **Volant Manticore** ha preso di mira organizzazioni di Cipro e dell’Arabia Saudita.  Tra le esche figurava il curriculum di una professionista fittizia del turismo, creato con l’AI per distribuire **KuboShell**, una backdoor Windows che usa IPFS per il comando e controllo. Il gruppo l’ha usata per la ricognizione e per distribuire **Homa Framework**, che include una reimplementazione del client **MuddyC2Go**. I ricercatori valutano con confidenza media l’ipotesi che il gruppo sia composto da ex membri di [**MuddyWater**](https://www.telsy.com/tag/muddywater/). Sul fronte europeo, almeno dalla metà di ottobre [**UNC5792**](https://www.telsy.com/tag/unc5792/), associato al Servizio federale per la sicurezza russo (FSB), avrebbe preso di mira giornalisti, esponenti politici e membri della società civile, tra cui sostenitori dell’Ucraina. La campagna di spear phishing sfruttava account già compromessi e falsi inviti a videoconferenze o gruppi su Signal e Telegram per indirizzare i destinatari verso pagine destinate a sottrarre dati di autenticazione o ad associare dispositivi agli account delle vittime. Sempre in Europa, un’inchiesta pubblicata l’11 novembre ha esaminato l’impiego degli spyware commerciali [**Pegasus**](https://www.telsy.com/tag/pegasus/), [**Predator**](https://www.telsy.com/en/tag/predator/) e **Graphite** contro giornalisti, attivisti e oppositori politici in cinque Paesi. In Grecia, quattro dirigenti legati a Intellexa sono stati condannati in primo grado, mentre restano da identificare i mandanti della sorveglianza del giornalista Thanasis Koukakis. In Polonia, una commissione parlamentar...