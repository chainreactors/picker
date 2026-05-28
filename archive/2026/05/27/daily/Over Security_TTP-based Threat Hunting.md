---
title: TTP-based Threat Hunting
url: https://roccosicilia.com/2026/05/27/ttp-based-threat-hunting/
source: Over Security
date: 2026-05-27
fetch_date: 2026-05-28T06:03:22.155892
---

# TTP-based Threat Hunting

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/divulgazione/)
* [Progetti](https://roccosicilia.com/progetti/)

[cyber security](https://roccosicilia.com/category/cyber-security/), [hacking](https://roccosicilia.com/category/hacking/), [study with me](https://roccosicilia.com/category/study-with-me/)

## [TTP-based Threat Hunting](https://roccosicilia.com/2026/05/27/ttp-based-threat-hunting/)

Published by

Rocco Sicilia

on

[27 Maggio 2026](https://roccosicilia.com/2026/05/27/ttp-based-threat-hunting/)

[![TTP-based Threat Hunting](https://roccosicilia.com/wp-content/uploads/2026/05/gemini-threat-hunting.png)](https://roccosicilia.com/2026/05/27/ttp-based-threat-hunting/)

Il titolo di questo post riprende, volutamente, il [documento di MITRE](https://www.mitre.org/sites/default/files/2021-11/prs-19-3892-ttp-based-hunting.pdf) a cui si ispira: 36 pagine di saggezza che, se lavori nel mondo della cyber security, devi leggere, assimilare e comprendere molto bene.

L’obiettivo è solo introdurre il tema ed evidenziare i motivi che lo rendono importante sia per il mondo Defense che per il mondo Offensive. Per i primi è abbastanza ovvio: le minacce evolvono, molte strutture hanno raggiunto dei limiti tecnici oggettivi con il modello di detection “reattivo” ed è necessario valutare evoluzioni. Per il mondo dei security test (di ogni tipo) è necessario considerare delle evoluzioni significative: oltre alla tradizionale verifica sulla presenza di vulnerabilità sfruttabili ed il loro impatto (Penetration Testing) dobbiamo necessariamente valutare la capacità di detection di minacce moderne tramite l’utilizzo di soluzione specifiche come EDR/XDR/SIEM/ecc. e la capacità di analisi dei blue team. Il nostro lavoro (io mi occupo di security test) cambia radicalmente e si sposta dall’eseguire singole tecniche allo strutturare una strategia di attacco realistica.

Nota: ovviamente non è mia intenzione sostenere che i Penetration Test “tradizionali” non servano più, dobbiamo semplicemente fare i conti con nuove tipologie di test che ci possono aiutare a valutare meglio le nostre difese cyber.

Partiamo dal problema: molte strutture mature utilizzano IoC e BIoC per costruire regole di detection in grado di utilizzare elementi noti come gli artefatti o i comportamenti mappabili. Questo modello ci porta ad un progressivo miglioramento della capacità di detection in quanto più elementi conosco più sono in grado di intercettare anomalie.

Va considerato che gli IoC sono qualcosa di molto statico con una validità temporanea: un IP viene considerato malevolo per un certo periodo, poi solitamente torna ad essere un normalissimo IP. I comportamenti sono qualcosa di più stabile che l’attaccante tende a seguire in diversi contesti e non hanno una effettiva “scadenza”.

Quello che ci stiamo dicendo è che mentre il mio C2 server può cambiare IP dall’oggi al domani per consentirmi di presentarmi per qualche giorno con un IP pulito, il modo con cui gestisco la comunicazione tra target e C2 (beaconing) non subisce enormi cambiamenti nel breve periodo. Posso cambiare protocollo, modificare gli intervalli di comunicazione o i metodo di trasmissione dei dati ma la struttura della mia azione non varia.

Ora, se fosse possibile avere una mappa completa delle varie azioni di attacco che comprenda me migliaia di variati sul tema, ci basterebbe fare tutte le regole del cosa (tante) ed avremmo risolto il problema: metto in detection tutti i comportamenti possibili e l’attaccante non ha modo di muoversi.
Sappiamo che questo è impossibile ed a questo si somma un problema molto pratico: detection rules basate sui comportamenti tendono a generare falsi positivi che vanno poi indagati, analizzati e gestiti. **Come ne usciamo?**

Mio parere, rinforzato dalla lettura del documento che ho citato, i Red Teamer devono iniziare a lavorare fianco a fianco con i Threat Hunter. Dobbiamo diventare un unico team dove i primi generano schemi di attacco, possibili varianti e work around per costruire dei TTP realistici che vadano ad arricchire la base strutturata che già abbiamo e su questo confronto formulare le ipotesi da cui far partire dei task di threat hunting.

Se trovi utili i contenuti che condiviso e vuoi restare aggiornato puoi sostenere il mio progetto di divulgazione [iscrivendoti al mio Substack](https://roccosicilia.substack.com/subscribe). Per gli abbonati metto a disposizione articoli e video di approfondimento.

Esempio (cosa successa veramente in diverse occasioni): il SOC ha già attivato delle regole di detection in relazione alle principali piattaforme utilizzate come C2 dai Threat Actor ma durante un test una specifica modifica custom del beaconing ha consentito di aggirare le rules. **La capacità del Red Team di aggirare le regole presenti deve essere messa a disposizione anche del team di Threat Hunting per andare a caccia di varianti della minaccia e migliorare la capacità di detection.** Questo modello non si implementa da solo e non c’è un unico modo per farlo.

Visto che da questo blog passa anche gente molto competente mi piacerebbe raccogliere qualche opinione strutturata.

### Condividi:

* Invia un link a un amico via e-mail (Si apre in una nuova finestra)
  E-mail
* [Condividi su LinkedIn (Si apre in una nuova finestra)
  LinkedIn](https://roccosicilia.com/2026/05/27/ttp-based-threat-hunting/?share=linkedin)
* [Condividi su Telegram (Si apre in una nuova finestra)
  Telegram](https://roccosicilia.com/2026/05/27/ttp-based-threat-hunting/?share=telegram)
* [Condividi su WhatsApp (Si apre in una nuova finestra)
  WhatsApp](https://roccosicilia.com/2026/05/27/ttp-based-threat-hunting/?share=jetpack-whatsapp)

### Mi piace:

Mi piace Caricamento in corso…

### Rispondi[Annulla risposta](/2026/05/27/ttp-based-threat-hunting/#respond)

←[Precedente: Threat Hunting and Defending #1 (study)](https://roccosicilia.com/2026/05/24/threat-hunting-and-defending-1-study/)

Ciao,

### sono Rocco

![](https://roccosicilia.com/wp-content/uploads/2025/04/photo.jpeg?w=389)

… e questo è mio sito personale dove condivido idee, riflessioni ed esperienze su hacking e sicurezza informatica.

### Let’s connect

* [Substack](https://roccosicilia.substack.com/profile/notes)

* [YouTube](https://youtube.com/%40roccosicilia)

* [LinkedIn](https://www.linkedin.com/in/roccosicilia/)

### Rimani aggiornato!

Iscriviti per ricevere gli update dei nuovi post e video.

Digita la tua e-mail…

→

### Recent posts

* [![TTP-based Threat Hunting](https://roccosicilia.com/wp-content/uploads/2026/05/gemini-threat-hunting.png)](https://roccosicilia.com/2026/05/27/ttp-based-threat-hunting/)

  ## [TTP-based Threat Hunting](https://roccosicilia.com/2026/05/27/ttp-based-threat-hunting/)
* [![Threat Hunting and Defending #1 (study)](https://roccosicilia.com/wp-content/uploads/2026/05/gemini-threat-hunting.png)](https://roccosicilia.com/2026/05/24/threat-hunting-and-defending-1-study/)

  ## [Threat Hunting and Defending #1 (study)](https://roccosicilia.com/2026/05/24/threat-hunting-and-defending-1-study/)
* [![Giochiamo insieme #1](https://roccosicilia.com/wp-content/uploads/2025/01/cybersecurity-test-serie.png)](https://roccosicilia.com/2026/05/22/giochiamo-insieme-1/)

  ## [Giochiamo insieme #1](https://roccosicilia.com/2026/05/22/giochiamo-insieme-1/)
* [![Postcast live (test)](https://roccosicilia.com/wp-content/uploads/2026/01/copertina_2026_2kpx.jpg)](https://roccosicilia.com/2026/05/22/postcast-live-test/)

  ## [Postcast live (test)](https://roccosicilia.com/2026/05/22/postcast-live-test/)
* [![MISP how-to: integrazione di feeds](https://roccosicilia.com/wp-content/uploads/2026/05/misp-screen.png)](https://roccosicilia.com/2026/05/13/misp-ed-integrazione-di-feeds/)

  ## [MISP how-to: integrazione di feeds](https://roccosicilia.com/2026/05/13/misp-ed-integrazione-di-feeds/)
* [![Info ...