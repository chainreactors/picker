---
title: Riflessione sulle Free WiFi
url: https://roccosicilia.com/2025/01/20/riflessione-sulle-free-wifi/
source: Instapaper: Unread
date: 2025-01-22
fetch_date: 2025-10-06T20:13:25.605828
---

# Riflessione sulle Free WiFi

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/progetto-di-divulgazione/)
* [Sostieni il progetto](https://roccosicilia.com/sostieni-il-progetto/)
* [English version](https://medium.com/%40roccosicilia)

[cyber security](https://roccosicilia.com/category/cyber-security/), [ita](https://roccosicilia.com/category/ita/)

## [Riflessione sulle Free WiFi](https://roccosicilia.com/2025/01/20/riflessione-sulle-free-wifi/)

Published by

Rocco Sicilia

on

[20 gennaio 2025](https://roccosicilia.com/2025/01/20/riflessione-sulle-free-wifi/)

[![Riflessione sulle Free WiFi](https://roccosicilia.com/wp-content/uploads/2025/01/wireless-security-risk.png?w=595)](https://roccosicilia.com/2025/01/20/riflessione-sulle-free-wifi/)

Nel feed di LinkedIn di qualche giorno fa mi sono imbattuto in un post di un mio contatto che lavora in campo info-sec. e che, con una certa leggerezza e senza argomentare, sosteneva che i rischi legati all’utilizzo incauto di reti wireless “open” trovate in giro per il mondo sono molto sopravvalutati.

Come dicevo il post che ho incrociato su LinkedIn non argomentava ulteriormente la posizione, quindi non conosco le ragioni tecniche alla base di questa opinione. Ho invece delle ragioni tecniche che mi fanno pensare il contrario e, con l’obiettivo di avviare una discussione costruttiva, le espongo qui in forma estesa e su LinkedIn, per questioni di spazio, in forma sintetica.

Non voglio fare pipponi accademici, preferisco raccontarvi alcuni scenari relativamente semplici da implementare che costituiscono un rischio concreto in quanto molto efficaci, soprattutto nei confronti dei target che tendono a fidarsi delle reti aperte che incontrano.

## Evil Twin come base

Partiamo dallo scenario più popolare. Sul piano tecnico si tratta di un Access Point configurato con lo stesso SSID (e, se possibile, MAC address) di un punto di accesso lecito. Esempio classico: la biblioteca dove prendete i vostri libri ha una rete open con nome *BiblioNet* e il threat actor configura il suo AP con lo stesso SSID e, visto che non gli costa fatica, utilizza anche lo stesso MAC address.

Lato client le versioni più recenti dei sistemi operativi tendono ad aggregare in una singola voce gli SSID uguali e con le stesse caratteristiche tecniche nascondendo il singolo AP (sto semplificando molto). Quando l’utente selezionerà la rete a cui collegarsi non avrà modo di distinguere tra l’AP legittimo ed il gemello malvagio e, solitamente, vince quello con il segnale più potente.

![](https://roccosicilia.com/wp-content/uploads/2025/01/image-12.png?w=1024)

Schema di sintesi dello scenario.

Ne consegue che se il threat actor si piazza in prossimità di una sorgente che può facilmente imitare, come una rete wireless open, ed utilizza un dispositivo con una potenza di segnale sufficientemente alta, come risultato otterrà che molti client si collegheranno al sui Access Point prima di accedere alla rete target. In pratica il dispositivo del threat actor si troverà tra i client ed il punt di accesso lecito.

## Il problema non è tanto il traffico, ma…

Probabilmente chi ritiene questo scenario a basso rischio si basa sul fatto che buona parte del traffico verso i servizi che abitualmente utilizziamo è cifrato, intercettarlo sarebbe quindi inutile. Questa affermazione è di base corretta, **ma intercettare il traffico è solo una delle azioni che il threat actor può considerare**.

Va considerato che il client si trova sullo stesso dominio di broadcast del threat actor che probabilmente gli sta anche passando, via DHCP, configurazioni a livello IP, gateway e DNS. È quindi relativamente semplice generare risposte a richieste DNS tali da dirottare il traffico verso un sito malevolo. Ad esempio se costruisco un servizio DNS che contiene una propria zona per il dominio roccosicilia.com potrei risolvere con un IP a mio piacimento le richieste dei client verso <http://www.roccosicilia.com> dirottandole su una custom page da me gestita. Questa semplice tecnica può essere usata per presentare all’utente finte login-form allo scopo di raccogliere credenziali valide.

## Comportamenti automatici

I sistemi operativi gestiscono in autonomia diversi processi per funzionare e rispondono ad una serie di configurazioni con procedure spesso completamente automatizzate. Ad esempio se il nostro sistema operativo è configurato per collegarsi ad una specifica share di rete o utilizza servizi specifici come dei proxy server, è molto probabile che al boot questi servizi vengano contattati per eseguire l’autenticazione e consentirci di, seguendo l’esempio della share di rete, trovare una unità disco già disponibile nel nostro File Explorer.

Cosa succedere quando il nostro laptop si collega ad una rete in cui non ci sono le risorse DNS che gli consentono di risolvere il nome host che condivide la share a cui solitamente ci si connette in automatico? Di default sono attivi dei protocolli che eseguono diverse attività a supporto dei servizi di rete, ad esempio nel caso citato il client invierebbe una richiesta in broadcast cercando nel proprio broadcast domain l’host in questione.

Conoscendo questo comportamento il threat actor potrebbe predisporre un tool in grado di intercettare la richiesta e rispondere al client come se fosse il servizio di cui è alla ricerca. Il client a questo punto riterrà di aver trovato la risorsa che stava cercando e tenterà di autenticarsi inviando il proprio hash **NTLMv1/v2 o LMv2**.

Ora, gli hash di per se non garantiscono accessi ai sistemi ma possono essere utilizzati in diversi scenari: è possibile valutare il cracking dell’hash se lunghezza e complessità della password lo consentono, elemento che potremmo non conoscere. Se lo scenario lo consente è anche plausibile valutare attacchi di tipo NTLM relay, quest’ultimo presenta diversi limiti a livello di scenario in quanto prevede una serie di condizioni acquisite.

---

Se trovi utili i miei contenuti e vuoi supportare il mio progetto di divulgazione puoi iscriverti alla mia pagina [Patreon](https://patreon.com/roccosicilia).

Per rimanere aggiornato puoi registrarti al blog con la tua email, riceverai una notifica alla pubblicazione di nuovi articoli.

Digita la tua e-mail…

Iscriviti

---

## In sintesi

Rischi correlati all’utilizzo di reti wireless open ne esistono e non sono necessariamente legati alla rete a cui ci si collega, anzi, sono opportunità di contesto che il threat actor può utilizzare.

Mi sono limitato ad un paio di esempi ma va considerato tutto quello che potenzialmente un threat actor può fare quando si trova a poter gestire il gateway di un device, ovviamente non sempre esiste la possibilità di compromettere la macchina target ma i rischi non sono da sottovalutare.

Se hai una opinione differente o vuoi condividere la tua esperienza in merito a questo argomento, sentiti libero di commentare o di scrivermi direttamente, mi fa sempre piacere confrontarmi con altri colleghi di settore.

## Update

A poche ore dalla pubblicazione del post, a seguito di diverse domande da parte dei lettori e della Patreon community, ho pubblicato due video di approfondimento:

* Sul mio [canale YouTube](https://www.youtube.com/watch?v=pOZY4c9mi78) accessibile a tutti
* Sul [canale Patreon](https://patreon.com/roccosicilia) con alcuni approfondimenti chiesti dai sostenitori

### Condividi:

* Fai clic per inviare un link a un amico via e-mail (Si apre in una nuova finestra)
  E-mail
* [Fai clic qui per condividere su LinkedIn (Si apre in una nuova finestra)
  LinkedIn](https://roccosicilia.com/2025/01/20/riflessione-sulle-free-wifi/?share=linkedin)
* [Fai clic per condividere su Telegram (Si apre in una nuova finestra)
  Telegram](https://roccosicilia.com/2025/01/20/riflessione-sulle-free-wifi/?share=telegram)
* [Fai clic per condividere su WhatsApp (Si apre in una nuova finestra)
  WhatsApp]...