---
title: NoName057(16) – DDoSia tool – Analisi tecnica - CYBEROO CERT - Tech Updates | Cybersecurity
url: https://cert.cyberoo.com/noname05716-ddosia-tool-analisi-tecnica/
source: Over Security - Cybersecurity news aggregator
date: 2024-03-02
fetch_date: 2025-10-04T12:13:06.954884
---

# NoName057(16) – DDoSia tool – Analisi tecnica - CYBEROO CERT - Tech Updates | Cybersecurity

[Skip to main content](#ajax-content-wrap)

Premi enter per la ricerca o ESC per chiudere

Close Search

* [*Menu*](#sidewidgetarea)

[![CYBEROO CERT - Tech Updates | Cybersecurity](https://cert.cyberoo.com/wp-content/uploads/2023/10/CYBEROO-logo.svg)](https://cert.cyberoo.com)

[Ricerca](#searchbox)

[*Menu*](#sidewidgetarea)

* [*Menu*](#sidewidgetarea)

* [Vai al Tech Blog](https://cert.cyberoo.com)

* [Contacts](https://cyberoo.com/contacts/)
* [![Italiano](https://cert.cyberoo.com/wp-content/plugins/sitepress-multilingual-cms/res/flags/it.svg)](https://cert.cyberoo.com/noname05716-ddosia-tool-analisi-tecnica/)
* [![Inglese](https://cert.cyberoo.com/wp-content/plugins/sitepress-multilingual-cms/res/flags/en.svg)](https://cert.cyberoo.com/en/noname05716-ddosia-tool-analysis-report/)
* [Ricerca](#searchbox)

[Articoli Cert](https://cert.cyberoo.com/category/articoli-cert/)

# NoName057(16) – DDoSia tool – Analisi tecnica – Updated

22 Marzo 20245 min read

[Home](https://cert.cyberoo.com/) » NoName057(16) – DDoSia tool – Analisi tecnica – Updated

### **Introduzione: i****l contesto**

DDoSia, un toolkit di attacco utilizzato per perpetrare Distributed Denial of Service (DDoS), è stato creato e utilizzato dal gruppo hacktivista nazionalista NoName057(16), che sostiene la Russia. Questo gruppo prende di mira principalmente i Paesi che hanno espresso critiche nei confronti dell’invasione russa all’Ucraina.

Il progetto DDoSia è stato avviato su Telegram all’inizio del 2022. Il canale Telegram principale di NoName057(16) ha attirato subito migliaia di iscritti.

Originariamente sviluppato in Python, DDoSia utilizzava i thread della CPU per avviare simultaneamente più richieste di rete. Inizialmente si affidava al protocollo HTTP per la comunicazione Command & Control (C2), con configurazioni JSON (JavaScript Object Notation) distribuite dal server C2.

Nell’aprile 2023, Avast ha pubblicato un articolo che esaminava il flusso di rete tra gli utenti di DDoSia e il C2. In risposta, gli amministratori di DDoSia hanno rilasciato una nuova versione del loro campione il giorno successivo. Questa versione aggiornata ha introdotto un ulteriore meccanismo di sicurezza volto a nascondere l’elenco degli obiettivi trasmesso dal C2 agli utenti.

**Cyberoo IRT ha analizzato l’ultima versione dello strumento, rilasciata durante dicembre 2023, per scoprire il meccanismo di decifratura ed estrarre l’elenco di obiettivi nel file json.**

Rispetto alle versioni precedentemente analizzate, NoName057(16) ha completamente rivisto il meccanismo di autenticazione, rendendo ancora più complessa l’analisi e introducendo un ulteriore layer di cifratura.

###

### **Analisi: esecuzione e comunicazione del tool**

*![DDosia](https://cert.cyberoo.com/wp-content/uploads/2024/03/DDosia-img-01-esecuzione-tool.png)*

*Figura 1 – Esecuzione del tool*

Dopo l’esecuzione del malware, inizia una richiesta POST all’URL hxxp://[IP]/client/login per autenticarsi con il server Command & Control (C2). Nell’header cookie sono presenti 2 valori; U e C e nel campo body un file json con il contenuto cifrato.

*![DDosia](https://cert.cyberoo.com/wp-content/uploads/2024/03/DDosia-img-02-cattura-traffico-login.png)*

*Figura 2 – Cattura del traffico durante il processo di login*

Se l’autenticazione va a buon fine (come in figura 2), il server risponde con un epoch.

Successivamente, ad autenticazione avvenuta, il client effettua un’ulteriore chiamata per recuperare l’elenco dei target:

*![DDosia](https://cert.cyberoo.com/wp-content/uploads/2024/03/DDosia-img-03-chiamata-GET-lista-target.png)*

*Figura 3 – Chiamata GET per recuperare la lista dei target*

La chiamata differisce solo in 2 parti rispetto a quella di login: User-Agent e Cookie, in cui appare un ulteriore valore “K” con una stringa codificata in base32.

Se la chiamata è formattata correttamente, il server risponde con un json cifrato di lunghezza variabile, dipendentemente dal numero di target oggetto degli attacchi (come in figura 3).

Lo User-Agent utilizzato durante le chiamate è preso randomicamente da un elenco presente all’interno dell’eseguibile.

*![DDosia](https://cert.cyberoo.com/wp-content/uploads/2024/03/DDosia-img-04-elenco-user-agent.png)*

*Figura 4 – Elenco non esaustivo degli User-Agent*

L’algoritmo di cifratura utilizzato durante il login ed il recupero dei target è AES-GCM.

### **Reverse engineering del file eseguibile**

L’effort che NoName057 impiega nello sviluppo del client è elevato e il risultato è chiaramente visibile durante il reverse engineering del binario.

L’analisi statica risulta difficile a causa della natura del binario (scritta in linguaggio Go) ed è stato necessario affiancare anche l’analisi dinamica, nonché il debugging step-by-step.

Dopo l’analisi statica e le sessioni di debug, Cyberoo ha carpito le informazioni ed i passaggi necessari per recuperare la lista dei target. Di seguito, **tutti i passaggi per effettuare il login**:

* Creazione dell’header “Cookie” con i 2 parametri U e C:
  + **U**: Hash fornito dal bot Telegram di NoName per effettuare l’autenticazione (contenuto nel file client\_id.txt)
  + **C**: GUID del pc che sta eseguendo il tool, ottenuto tramite lettura della chiave di registro “HKLM\SOFTWARE\Microsoft\Cryptography\Machine Guid + PID del processo
  + **Body JSON**: il body che viene inviato è il risultato della cifratura AES-GCM + codifica in base64 del risultato e formattazione in JSON. La chiave di cifratura è ottenuta dal GUID sottratto dei primi 10 caratteri + il pid + uno “0” finale (esempio: 630-4d81-a47f-3aa052407e33-21080).

Il contenuto in chiaro del body è un JSON con svariate informazioni del pc, come ad esempio il nome, il timestamp dell’esecuzione, gli ultimi 27 caratteri dell’hash client\_id.txt, il GUID completo, numeri delle CPU, versione del sistema operativo e architettura. In più è presente un valore “key” contenente 17 caratteri alfanumerici generati randomicamente durante ogni esecuzione.

Non sono presenti dati personali o identificabili.

**Passaggi per recuperare la lista dei target**:

* Creazione dello stesso identico header utilizzato durante l’autenticazione, con l’aggiunta del parametro “K”, ottenuto dalla generazione randomica di una stringa di 260 caratteri alfanumerici, successivamente codificata in base32.
* A chiamata avvenuta, la risposta del C2 contiene un JSON con il campo “data”, contenente un blob codificato in base64 e cifrato sempre in AES-GCM.
* La chiave di decifratura è la stessa identica utilizzata durante la cifratura iniziale nella fase di login (key).

Qui sotto sono descritte le **modalità per recuperare i valori IV e TAG necessari per la decifratura del dato**:

* Calcolo IV – nonce
  + Prendere il testo cifrato e decodificarlo in base64;
  + Prendere i 24 primi caratteri e convertirli in byte.
* Calcolo del TAG
  + Prendere il testo cifrato, decodificarlo in base64;
  + Prendere gli ultimi 32 caratteri e convertirli in byte.

Il testo cifrato si riferisce al valore del campo dati convertito in base64, con l’esclusione dei primi 24 caratteri (12 byte) e degli ultimi 32 caratteri (16 byte). Applicando questa modifica, diventa possibile recuperare il valore in chiaro del campo dati.

*![](https://cert.cyberoo.com/wp-content/uploads/2023/12/attacco-ddos4.jpg)*

*Figura 5 – Lista dei target decifrata*

Il campo dati decifrato contiene l’elenco completo del target.

###

### **Conclusione**

L’analisi dello strumento DDoS evidenzia l’importanza del reverse engineering e della Threat intelligence per comprenderne le funzionalità, identificare potenziali vulnerabilità e sviluppare contromisure efficaci.

Dopo l’analisi del tool, CYBEROO ha scritto un tool privato per avere una panoramica in tempo reale dell’elenco dei bersagli e fornire informazioni a tutti i suoi clienti attraverso la piattaforma CSI.

SHARE THIS

* [Whatsapp](https://web.whatsapp.com/send?text=https://cert.cyberoo.com/noname05716-ddosia-tool-analisi-tecnica...